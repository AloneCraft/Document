# <a id="Omni_RadialFarFieldCache"></a> Class RadialFarFieldCache

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

遠景（<xref href="Omni.Rendering.Radial.BakeEntry.FarFieldGroup" data-throw-if-not-resolved="false"></xref> が割り当てられた静的Renderer群）の
ワープパラメータMPB更新を、カメラが十分動くまで省略するキャッシュです。

<p>
ThresholdLinearLog で <code>d &gt;&gt; R</code> のとき <code>mapped(d) = R + S・log2(d/R)</code> であり、
カメラが δ 動いたときの写像距離の変化は概ね <code>S・δ/(d・ln2)</code>、角度の変化は概ね <code>δ/d</code> です。
十分遠い対象ではワープ後の描画はカメラ移動に対してほぼ不変になるため、<code>RadialBaker</code> が
ベイク時に許容角度誤差εから求めた無効化半径
<code>δmax = ε・dMin</code>（<xref href="Omni.Rendering.Radial.FarFieldGroup.InvalidationDistance" data-throw-if-not-resolved="false"></xref>）の範囲内であれば、
前回書き込んだMPB値をそのまま使い回してよいとみなします。
</p>
<p>
<xref href="Omni.RadialGlobalRenderSystem" data-throw-if-not-resolved="false"></xref> が対象Rendererを1つずつ処理する際、このキャッシュへ
「このRendererは今フレームMPB更新をスキップしてよいか」を問い合わせます。
</p>

```csharp
public static class RadialFarFieldCache
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialFarFieldCache](Omni.RadialFarFieldCache.md)

## メソッド（Methods）

### <a id="Omni_RadialFarFieldCache_ClearAll"></a> ClearAll\(\)

シーン変更時などにキャッシュを破棄します。

```csharp
public static void ClearAll()
```

### <a id="Omni_RadialFarFieldCache_InvalidateAll"></a> InvalidateAll\(\)

索引は保持したままキャッシュ済みの値だけを捨てます（<xref href="Omni.RadialFarFieldCache.ClearAll" data-throw-if-not-resolved="false"></xref> と違い
ベイクの逆引きを作り直しません）。ワープ一時停止の切り替えなど、
「次フレームに必ず全 Renderer へ配布し直したい」ときに使います。

```csharp
public static void InvalidateAll()
```

### <a id="Omni_RadialFarFieldCache_MakeCurveKey_System_Single_System_Single_System_Single_System_Single_"></a> MakeCurveKey\(float, float, float, float\)

カーブ形状の指紋を作ります。位置（CameraPos / PrevCameraPos）は含めません
—— 位置は無効化半径の判定が担当し、毎フレーム変わる PrevCameraPos を
含めるとキャッシュが常に無効になって存在意義が消えるためです。

```csharp
public static int MakeCurveKey(float radialScale, float mode, float linearRadius, float log2ViewScale)
```

#### 引数（Parameters）

`radialScale` [float](https://learn.microsoft.com/dotnet/api/system.single)

`mode` [float](https://learn.microsoft.com/dotnet/api/system.single)

`linearRadius` [float](https://learn.microsoft.com/dotnet/api/system.single)

`log2ViewScale` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_RadialFarFieldCache_MarkApplied_UnityEngine_Renderer_"></a> MarkApplied\(Renderer\)

MPBを実際に書き込んだRendererを記録します。<xref href="Omni.RadialFarFieldCache.ShouldSkipUpdate(UnityEngine.Renderer%2cOmni.Logical.Position3%40%2cUnityEngine.Camera%2cOmni.RadialCamera%2cSystem.Int32)" data-throw-if-not-resolved="false"></xref>とは別に呼ぶことで、
グループ更新の初回値が一部のRendererだけへ届く問題を防ぎます。

```csharp
public static void MarkApplied(Renderer renderer)
```

#### 引数（Parameters）

`renderer` Renderer

### <a id="Omni_RadialFarFieldCache_ShouldSkipUpdate_UnityEngine_Renderer_Omni_Logical_Position3__UnityEngine_Camera_Omni_RadialCamera_System_Int32_"></a> ShouldSkipUpdate\(Renderer, in Position3, Camera, RadialCamera, int\)

このRendererについて、今フレームの _RadialGlobal_* MPB更新を省略してよいか判定します。
無効化半径を超えて動いていた場合は、この呼び出し自体がキャッシュ位置を更新します
（＝「再計算した」ことになり、以後 δmax 以内は再びスキップ対象になります）。

```csharp
public static bool ShouldSkipUpdate(Renderer renderer, in Position3 cameraPosition, Camera camera, RadialCamera driver, int curveKey)
```

#### 引数（Parameters）

`renderer` Renderer

`cameraPosition` [Position3](Omni.Logical.Position3.md)

`camera` Camera

描画中のカメラ。

`driver` [RadialCamera](Omni.RadialCamera.md)

ワープ中心を提供している基準カメラ（<xref href="Omni.RadialWarpSource.Driver" data-throw-if-not-resolved="false"></xref>）。
描画中カメラ（<code class="paramref">camera</code>）が同じでも基準カメラが切り替わることは
あるため（例: Scene View で基準カメラを切り替える）、別途キーに含めます。

`curveKey` [int](https://learn.microsoft.com/dotnet/api/system.int32)

ワープカーブ形状の指紋（<xref href="Omni.RadialFarFieldCache.MakeCurveKey(System.Single%2cSystem.Single%2cSystem.Single%2cSystem.Single)" data-throw-if-not-resolved="false"></xref>）。位置以外のパラメータが
変わったことを検出するために要ります。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
