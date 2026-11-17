# <a id="Omni_Logical_PoseBakeSampler"></a> Class PoseBakeSampler

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Omni.Sequencer.Runtime.dll  

```csharp
[MovedFrom(true, "Omni.Sequencer", null, "LogicalPoseBakeSampler")]
public static class PoseBakeSampler
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PoseBakeSampler](Omni.Logical.PoseBakeSampler.md)

## メソッド（Methods）

### <a id="Omni_Logical_PoseBakeSampler_TryFractionTo_System_Double_Omni_Logical_Scalar__"></a> TryFractionTo\(double, out Scalar\)

時刻由来の無次元比率をLogicalScalarへ取り込みます。

<p>
doubleを単精度1回で受けると仮数が24ビットに落ち、1/60秒区間の内側が
6e-8刻みになります。上位floatと残差floatの2回に分けて取り込むことで
48ビット相当の分解能を保ちます。ここで扱うのは時刻の比率であって
空間量ではないため、doubleを入力に取ることは空間double APIには当たりません。
</p>

```csharp
public static bool TryFractionTo(double fraction, out Scalar result)
```

#### 引数（Parameters）

`fraction` [double](https://learn.microsoft.com/dotnet/api/system.double)

0〜1の比率。

`result` Scalar

Logical化した比率。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_PoseBakeSampler_TryResolveSample_Omni_Logical_PoseBake_System_Double_System_Int32__System_Int32__Omni_Logical_Scalar__Omni_Logical_PoseBakeRejection__"></a> TryResolveSample\(PoseBake, double, out int, out int, out Scalar, out PoseBakeRejection\)

時刻から、前後のサンプル索引と区間内の比率を求めます。

<p>
範囲外の時刻は棄却せずに端のサンプルへクランプします。演出の末尾や
浮動小数の丸めでわずかに範囲を出た瞬間だけリアルタイム経路へ切り替わると、
そこで絵が跳ねます。範囲外は「端で止まる」方が破綻しません。
</p>

```csharp
public static bool TryResolveSample(PoseBake bake, double timeSeconds, out int index, out int nextIndex, out Scalar fraction, out PoseBakeRejection rejection)
```

#### 引数（Parameters）

`bake` [PoseBake](Omni.Logical.PoseBake.md)

ベイクデータ。

`timeSeconds` [double](https://learn.microsoft.com/dotnet/api/system.double)

評価する時刻（秒）。

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

区間の開始サンプル索引。

`nextIndex` [int](https://learn.microsoft.com/dotnet/api/system.int32)

区間の終了サンプル索引。末尾では<code class="paramref">index</code>と同じです。

`fraction` Scalar

区間内の比率(0〜1)をLogical化したもの。

`rejection` [PoseBakeRejection](Omni.Logical.PoseBakeRejection.md)

失敗した場合の理由。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_PoseBakeSampler_TrySampleClipRange_Omni_Logical_PoseBakeChannel_System_Int32_System_Int32_System_Single_System_Single__System_Single__"></a> TrySampleClipRange\(PoseBakeChannel, int, int, float, out float, out float\)

前後サンプルのクリップ範囲を補間します。近クリップは対数的に変化するため、
線形ではなく対数で補間します（数十桁を線形に補間すると手前側が潰れます）。

```csharp
public static bool TrySampleClipRange(PoseBakeChannel channel, int index, int nextIndex, float fraction, out float nearClip, out float farClip)
```

#### 引数（Parameters）

`channel` [PoseBakeChannel](Omni.Logical.PoseBakeChannel.md)

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`nextIndex` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`fraction` [float](https://learn.microsoft.com/dotnet/api/system.single)

`nearClip` [float](https://learn.microsoft.com/dotnet/api/system.single)

`farClip` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_PoseBakeSampler_TrySampleDistance_Omni_Logical_PoseBakeChannel_System_Int32_System_Int32_Omni_Logical_Scalar__Omni_Logical_Scalar__"></a> TrySampleDistance\(PoseBakeChannel, int, int, in Scalar, out Scalar\)

前後サンプルのカメラ距離を補間します。

```csharp
public static bool TrySampleDistance(PoseBakeChannel channel, int index, int nextIndex, in Scalar fraction, out Scalar value)
```

#### 引数（Parameters）

`channel` [PoseBakeChannel](Omni.Logical.PoseBakeChannel.md)

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`nextIndex` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`fraction` Scalar

`value` Scalar

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_PoseBakeSampler_TrySampleFieldOfView_Omni_Logical_PoseBakeChannel_System_Int32_System_Int32_System_Single_System_Single__"></a> TrySampleFieldOfView\(PoseBakeChannel, int, int, float, out float\)

前後サンプルの画角を補間します。画角は空間量ではないのでfloatのまま扱います。

```csharp
public static bool TrySampleFieldOfView(PoseBakeChannel channel, int index, int nextIndex, float fraction, out float value)
```

#### 引数（Parameters）

`channel` [PoseBakeChannel](Omni.Logical.PoseBakeChannel.md)

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`nextIndex` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`fraction` [float](https://learn.microsoft.com/dotnet/api/system.single)

`value` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_PoseBakeSampler_TrySampleLightShading_Omni_Logical_PoseBakeChannel_System_Int32_System_Int32_System_Single_System_Single__UnityEngine_Color__"></a> TrySampleLightShading\(PoseBakeChannel, int, int, float, out float, out Color\)

前後サンプルの光の強さ・色を補間します。

```csharp
public static bool TrySampleLightShading(PoseBakeChannel channel, int index, int nextIndex, float fraction, out float intensity, out Color color)
```

#### 引数（Parameters）

`channel` [PoseBakeChannel](Omni.Logical.PoseBakeChannel.md)

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`nextIndex` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`fraction` [float](https://learn.microsoft.com/dotnet/api/system.single)

`intensity` [float](https://learn.microsoft.com/dotnet/api/system.single)

`color` Color

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_PoseBakeSampler_TrySampleLookOffset_Omni_Logical_PoseBakeChannel_System_Int32_System_Int32_Omni_Logical_Scalar__Omni_Logical_Vector3__"></a> TrySampleLookOffset\(PoseBakeChannel, int, int, in Scalar, out Vector3\)

前後サンプルの注視点Logicalオフセットを補間します。

```csharp
public static bool TrySampleLookOffset(PoseBakeChannel channel, int index, int nextIndex, in Scalar fraction, out Vector3 value)
```

#### 引数（Parameters）

`channel` [PoseBakeChannel](Omni.Logical.PoseBakeChannel.md)

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`nextIndex` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`fraction` Scalar

`value` Vector3

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_PoseBakeSampler_TrySamplePosition_Omni_Logical_PoseBakeChannel_System_Int32_System_Int32_Omni_Logical_Scalar__Omni_Logical_Position3__"></a> TrySamplePosition\(PoseBakeChannel, int, int, in Scalar, out Position3\)

前後サンプルの位置を補間します。

```csharp
public static bool TrySamplePosition(PoseBakeChannel channel, int index, int nextIndex, in Scalar fraction, out Position3 value)
```

#### 引数（Parameters）

`channel` [PoseBakeChannel](Omni.Logical.PoseBakeChannel.md)

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`nextIndex` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`fraction` Scalar

`value` Position3

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_PoseBakeSampler_TrySampleRotation_Omni_Logical_PoseBakeChannel_System_Int32_System_Int32_Omni_Logical_Scalar__Omni_Logical_Quaternion__"></a> TrySampleRotation\(PoseBakeChannel, int, int, in Scalar, out Quaternion\)

前後サンプルの回転を補間します。

```csharp
public static bool TrySampleRotation(PoseBakeChannel channel, int index, int nextIndex, in Scalar fraction, out Quaternion value)
```

#### 引数（Parameters）

`channel` [PoseBakeChannel](Omni.Logical.PoseBakeChannel.md)

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`nextIndex` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`fraction` Scalar

`value` Quaternion

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
