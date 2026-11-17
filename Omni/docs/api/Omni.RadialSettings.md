# <a id="Omni_RadialSettings"></a> Struct RadialSettings

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

Radial（対数）ワープのパラメータ一式です。

<p>
写像は Smooth Log ひとつだけです: <code>F(d) = S·log2(1 + d·M/S)</code>、S = <xref href="Omni.RadialSettings.RadialScale" data-throw-if-not-resolved="false"></xref> = 1（定数）。
線形域（ThresholdLinearLog）や曲線・S の選択は持ちません。近くがほぼ恒等（一様な拡大）になる構成では、
写像の扱いの誤りが近景で見えず、描画の不具合を見つけられないためです（2026-10-04 の判断）。
調整できるのは View Scale M（<code>Camera の Near ÷ 論理 near</code>）だけで、曲がり始めは論理距離で約 1/M です。
</p>
<xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref> の該当フィールドから取り込み、GPU頂点ワープ
（<code>Omni/RadialGlobalLit</code> シェーダーのOmni Radial写像）と
CPU側のTransform書き換えが同一のカーブを共有するための単一の正本です。
RuntimeのCPU写像は、この型のLogical演算を正本とします。

```csharp
[Serializable]
public struct RadialSettings : IEquatable<RadialSettings>
```

#### 実装するインターフェース（Implements）

[IEquatable<RadialSettings\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1)

## コンストラクター（Constructors）

### <a id="Omni_RadialSettings__ctor_System_Single_"></a> RadialSettings\(float\)

View Scale を指定して設定を生成します。無効な値は既定値へ丸められます。

```csharp
public RadialSettings(float log2ViewScale)
```

#### 引数（Parameters）

`log2ViewScale` [float](https://learn.microsoft.com/dotnet/api/system.single)

有限なlog2(M)。Mそのものは渡しません。

### <a id="Omni_RadialSettings__ctor_System_Single_Omni_Logical_Scalar__"></a> RadialSettings\(float, in Scalar\)

論理Far Clipを含む全パラメータを指定して設定を生成します。

```csharp
public RadialSettings(float log2ViewScale, in Scalar logicalFarClip)
```

#### 引数（Parameters）

`log2ViewScale` [float](https://learn.microsoft.com/dotnet/api/system.single)

`logicalFarClip` [Scalar](Omni.Logical.Scalar.md)

## フィールド（Fields）

### <a id="Omni_RadialSettings_DefaultFarClip"></a> DefaultFarClip

論理 Far Clip の既定値です。<xref href="Omni.RadialCamera.DefaultFarClip" data-throw-if-not-resolved="false"></xref>と揃えます。

```csharp
public static readonly Scalar DefaultFarClip
```

#### 値（Field Value）

 [Scalar](Omni.Logical.Scalar.md)

### <a id="Omni_RadialSettings_DefaultLog2ViewScale"></a> DefaultLog2ViewScale

View Scale（M。カーブへ渡す前の論理距離に掛かる倍率）の既定値です。
M=1は追加の入力倍率が等倍という意味で、写像自体を恒等変換にはしません（原点近傍の傾きは 1/ln2）。

```csharp
public const float DefaultLog2ViewScale = 0
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_RadialSettings_RadialScale"></a> RadialScale

放射スケールS（距離が2倍になるごとに進む描画距離、Unity単位）です。定数で、設定はありません。
GPU の <code>RadialWarp.hlsl</code> も同じ値（S = 1）で写像します。

```csharp
public const float RadialScale = 1
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

## プロパティ（Properties）

### <a id="Omni_RadialSettings_Default"></a> Default

SceneView Radial編集の既定設定です。

```csharp
public static RadialSettings Default { get; }
```

#### 値（Property Value）

 [RadialSettings](Omni.RadialSettings.md)

### <a id="Omni_RadialSettings_FarClip"></a> FarClip

論理 Far Clip 距離です。常に正で有限な値を返します。

<p>
対数ワープは論理 R〜∞ を有限の描画距離へ畳むため、上限を置かないと「どこまで見えるか」が
Unity 側の <xref href="UnityEngine.Camera.farClipPlane" data-throw-if-not-resolved="false"></xref> とカリング側のハードコード値という、
誰も指定していない値で決まってしまいます。これはその上限を明示するための値で、
CPUカリング錐台の far と、GPU実クリップ far の要求値の両方に効きます。
</p>
<p>
既存のシリアライズ済みアセット（Bakeデータや ProjectSettings）にはこのキーが無いため、
0以下（＝未設定）は既定値へ丸めます。
</p>

```csharp
public Scalar FarClip { get; }
```

#### 値（Property Value）

 [Scalar](Omni.Logical.Scalar.md)

### <a id="Omni_RadialSettings_Log2ViewScale"></a> Log2ViewScale

log2(View Scale)です。Mはカーブへ渡す前の距離に適用します（M-inside）。
実数倍率MをCPU上で実体化しません。

```csharp
public float Log2ViewScale { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

## メソッド（Methods）

### <a id="Omni_RadialSettings_ApplyTo_Omni_RadialCamera_"></a> ApplyTo\(RadialCamera\)

<xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref> へこの設定を転写し、GPUワープをCPUワープに揃えます。

```csharp
public bool ApplyTo(RadialCamera driver)
```

#### 引数（Parameters）

`driver` [RadialCamera](Omni.RadialCamera.md)

転写先のドライバ。nullの場合は何もしません。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

転写した場合はtrue。

### <a id="Omni_RadialSettings_Equals_Omni_RadialSettings_"></a> Equals\(RadialSettings\)

```csharp
public bool Equals(RadialSettings other)
```

#### 引数（Parameters）

`other` [RadialSettings](Omni.RadialSettings.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_RadialSettings_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object obj)
```

#### 引数（Parameters）

`obj` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_RadialSettings_FromDriver_Omni_RadialCamera_"></a> FromDriver\(RadialCamera\)

<xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref> の現在値から設定を取り込みます。

```csharp
public static RadialSettings FromDriver(RadialCamera driver)
```

#### 引数（Parameters）

`driver` [RadialCamera](Omni.RadialCamera.md)

取り込み元のドライバ。nullの場合は既定値を返します。

#### 戻り値（Returns）

 [RadialSettings](Omni.RadialSettings.md)

取り込んだ設定。

### <a id="Omni_RadialSettings_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_RadialSettings_ToString"></a> ToString\(\)

```csharp
public override string ToString()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_RadialSettings_TryGetLog2Scale_Omni_Logical_Scalar__System_Single__"></a> TryGetLog2Scale\(in Scalar, out float\)

ワープによる等方スケール倍率（描画距離 / 論理距離）を求めます。
distanceが0の場合は、そのカーブの原点極限を返します。

```csharp
public bool TryGetLog2Scale(in Scalar distance, out float log2Scale)
```

#### 引数（Parameters）

`distance` [Scalar](Omni.Logical.Scalar.md)

ワープ中心からの非負で有限な距離。

`log2Scale` [float](https://learn.microsoft.com/dotnet/api/system.single)

有限なスケール倍率のlog2。失敗時は0。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

算出に成功した場合はtrue。

### <a id="Omni_RadialSettings_TryMap_Omni_Logical_Vector3__Unity_Mathematics_float3__"></a> TryMap\(in Vector3, out float3\)

ワープ中心からの相対位置を、描画空間の相対位置へ写像します。
方向は保存され、距離のみが再写像されます（シェーダーの<code>RadialWarp()</code>と同一）。

```csharp
public bool TryMap(in Vector3 relativePosition, out float3 mappedPosition)
```

#### 引数（Parameters）

`relativePosition` [Vector3](Omni.Logical.Vector3.md)

ワープ中心からの相対位置。

`mappedPosition` float3

写像後の相対位置。失敗時はゼロ。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

入出力がすべて有限であればtrue。

### <a id="Omni_RadialSettings_TryMapDistance_Omni_Logical_Scalar__System_Single__"></a> TryMapDistance\(in Scalar, out float\)

距離のみをスカラーとして写像します。<xref href="Omni.RadialSettings.TryMap(Omni.Logical.Vector3%40%2cUnity.Mathematics.float3%40)" data-throw-if-not-resolved="false"></xref> と同じカーブを、
+X方向の1点を通して評価するため、ベクトル版と必ず一致します。

```csharp
public bool TryMapDistance(in Scalar distance, out float mappedDistance)
```

#### 引数（Parameters）

`distance` [Scalar](Omni.Logical.Scalar.md)

ワープ中心からの非負で有限な距離。

`mappedDistance` [float](https://learn.microsoft.com/dotnet/api/system.single)

写像後の距離（符号付き）。失敗時は0。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

写像に成功した場合はtrue。

### <a id="Omni_RadialSettings_TryProject_Omni_Logical_Vector3__Unity_Mathematics_float3__System_Single__"></a> TryProject\(in Vector3, out float3, out float\)

相対位置を写像し、同時に等方スケール倍率のlog2も返します。

<p>
<xref href="Omni.RadialSettings.TryMap(Omni.Logical.Vector3%40%2cUnity.Mathematics.float3%40)" data-throw-if-not-resolved="false"></xref> と <xref href="Omni.RadialSettings.TryGetLog2Scale(Omni.Logical.Scalar%40%2cSystem.Single%40)" data-throw-if-not-resolved="false"></xref> を別々に呼ぶと写像を
2回行うことになるため、描画のホットパス（オブジェクトごとに毎フレーム）は
こちらを使います。log2倍率はLogical距離から直接求めます。
</p>

```csharp
public bool TryProject(in Vector3 relativePosition, out float3 mappedPosition, out float log2Scale)
```

#### 引数（Parameters）

`relativePosition` [Vector3](Omni.Logical.Vector3.md)

ワープ中心からの相対位置。

`mappedPosition` float3

写像後の相対位置。失敗時はゼロ。

`log2Scale` [float](https://learn.microsoft.com/dotnet/api/system.single)

等方スケール倍率のlog2。失敗時は0。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

写像と倍率の算出に成功した場合はtrue。

### <a id="Omni_RadialSettings_TryUnmap_Unity_Mathematics_float3__Omni_Logical_Vector3__"></a> TryUnmap\(in float3, out Vector3\)

描画空間の相対位置を、ワープ中心からの論理的な相対位置へ逆写像します。
<xref href="Omni.RadialSettings.TryMap(Omni.Logical.Vector3%40%2cUnity.Mathematics.float3%40)" data-throw-if-not-resolved="false"></xref> の逆変換です。

```csharp
public bool TryUnmap(in float3 mappedPosition, out Vector3 relativePosition)
```

#### 引数（Parameters）

`mappedPosition` float3

描画空間でのワープ中心からの相対位置。

`relativePosition` [Vector3](Omni.Logical.Vector3.md)

逆写像後の相対位置。失敗時はゼロ。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

入出力がすべて有限であればtrue。

### <a id="Omni_RadialSettings_TryUnmapDistance_System_Single_Omni_Logical_Scalar__"></a> TryUnmapDistance\(float, out Scalar\)

描画距離を論理距離へスカラーで逆写像します。<xref href="Omni.RadialSettings.TryUnmap(Unity.Mathematics.float3%40%2cOmni.Logical.Vector3%40)" data-throw-if-not-resolved="false"></xref>と同じカーブを
+X方向の1点を通して評価します。<xref href="Omni.RadialGlobalRenderSystem" data-throw-if-not-resolved="false"></xref>の
カリング錐台near/far逆写像と、Inspectorの「Logical Near Clip」表示が共有します。

```csharp
public bool TryUnmapDistance(float mappedDistance, out Scalar distance)
```

#### 引数（Parameters）

`mappedDistance` [float](https://learn.microsoft.com/dotnet/api/system.single)

非負で有限な描画距離。

`distance` [Scalar](Omni.Logical.Scalar.md)

逆写像後の論理距離。失敗時は入力値のまま。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

逆写像に成功した場合はtrue。
