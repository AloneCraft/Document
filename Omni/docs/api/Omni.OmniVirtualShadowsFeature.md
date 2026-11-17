# <a id="Omni_OmniVirtualShadowsFeature"></a> Class OmniVirtualShadowsFeature

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

主光源(Directional)の仮想シャドウマップ(Docs/Plans/VirtualShadowMaps.md)。結果は URP の画面空間の影(_ScreenSpaceShadowmapTexture、_MAIN_LIGHT_SHADOWS_SCREEN)へ書くので、
URP Lit・Omni の生成シェーダー・画面空間の影を受け取る自前のシェーダーは変えずに受け取れる。

<p>
1 フレーム: (1) 光の向き・カメラの位置から段の窓を決める。(2) 前のフレームまでの要求の読み戻しから、まだ無いページを割り当て、その範囲の正射影で影を落とす物を物理ページの置き場へ描く。
(3) 深度の前段の後に、画素ごとに要るページの印を付け(読み戻す)、段とページを引いて画面空間の影を書く。(4) 透明物の前でキーワードを戻す。
</p>

使えないとき(ランダム書き込みが無い・WebGPU・主光源が無い・影なし)は何もしない(URP のカスケード影のまま)。理由を 1 回だけ警告する。
対象は Game の主カメラ(Camera.main)だけ(置き場を 1 つにするため)。それ以外のカメラは URP のカスケード影のまま。

```csharp
[DisallowMultipleRendererFeature("Omni Virtual Shadows")]
public sealed class OmniVirtualShadowsFeature : ScriptableRendererFeature, IDisposable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
ScriptableObject ← 
ScriptableRendererFeature ← 
[OmniVirtualShadowsFeature](Omni.OmniVirtualShadowsFeature.md)

#### 実装するインターフェース（Implements）

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

## フィールド（Fields）

### <a id="Omni_OmniVirtualShadowsFeature_ShaderName"></a> ShaderName

```csharp
public const string ShaderName = "Hidden/Omni/VirtualShadows"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## プロパティ（Properties）

### <a id="Omni_OmniVirtualShadowsFeature_AverageFrameMs"></a> AverageFrameMs

診断用: 直近 60 フレームの平均のフレーム時間(ms)。

```csharp
public static float AverageFrameMs { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_OmniVirtualShadowsFeature_DiagnosticSkip"></a> DiagnosticSkip

検証用: 重さの切り分けのために、処理を個別に止める(ビットの和)。1 = ページの要求(画面を走らせて印を付けるパス)を止める。
2 = ページを描かない(計画はする)。4 = 順番の描き直しと、動く物の描き直しを止める。0 = 通常。

```csharp
public static int DiagnosticSkip { get; set; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_OmniVirtualShadowsFeature_LastStatistics"></a> LastStatistics

診断用: 最後のフレームの状態。

```csharp
public static OmniVirtualShadowStatistics LastStatistics { get; }
```

#### 値（Property Value）

 [OmniVirtualShadowStatistics](Omni.OmniVirtualShadowStatistics.md)

### <a id="Omni_OmniVirtualShadowsFeature_SettleReport"></a> SettleReport

```csharp
public static string SettleReport { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_OmniVirtualShadowsFeature_SuppressForComparison"></a> SuppressForComparison

検証用: true の間は使わない(URP のカスケード影と比べる)。

```csharp
public static bool SuppressForComparison { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_OmniVirtualShadowsFeature_AddRenderPasses_UnityEngine_Rendering_Universal_ScriptableRenderer_UnityEngine_Rendering_Universal_RenderingData__"></a> AddRenderPasses\(ScriptableRenderer, ref RenderingData\)

```csharp
public override void AddRenderPasses(ScriptableRenderer renderer, ref RenderingData renderingData)
```

#### 引数（Parameters）

`renderer` ScriptableRenderer

`renderingData` RenderingData

### <a id="Omni_OmniVirtualShadowsFeature_BeginSettleProbe"></a> BeginSettleProbe\(\)

検証用: ページを全部捨ててから、要求されたページが全部描かれるまでのフレーム数と、その間のいちばん長いフレーム時間を測る。
結果は <xref href="Omni.OmniVirtualShadowsFeature.SettleReport" data-throw-if-not-resolved="false"></xref>(測り終わるまで null)。

```csharp
public static void BeginSettleProbe()
```

### <a id="Omni_OmniVirtualShadowsFeature_ClearStatistics"></a> ClearStatistics\(\)

統計を空にする(検証用。Scene を替えた後、古い値が残らないように)。

```csharp
public static void ClearStatistics()
```

### <a id="Omni_OmniVirtualShadowsFeature_Create"></a> Create\(\)

```csharp
public override void Create()
```

### <a id="Omni_OmniVirtualShadowsFeature_Dispose_System_Boolean_"></a> Dispose\(bool\)

```csharp
protected override void Dispose(bool disposing)
```

#### 引数（Parameters）

`disposing` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_OmniVirtualShadowsFeature_ResetPages"></a> ResetPages\(\)

検証用: 次のフレームで全てのページを捨てて描き直す。

```csharp
public static void ResetPages()
```
