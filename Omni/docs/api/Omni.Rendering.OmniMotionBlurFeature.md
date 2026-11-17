# <a id="Omni_Rendering_OmniMotionBlurFeature"></a> Class OmniMotionBlurFeature

Namespace: [Omni.Rendering](Omni.Rendering.md)  
Assembly: Radial.Runtime.dll  

奥行きを見るモーションブラー(<xref href="Omni.Rendering.OmniMotionBlur" data-throw-if-not-resolved="false"></xref> の Volume 設定が有効なカメラだけ)。
ポストエフェクトの前に、付けたマテリアル(Fullscreen の Shader Graph、URP 標準の深度の書き方)を 1 回の全画面処理で描く。
Graph へは、元の色を _BlitTexture、動きを _MotionVectorTexture、深度を _CameraDepthTexture、強さ・上限・標本数を _BlurSettings で渡す。
Radial のときは、Omni の切り替え(Renderer Feature が持つマテリアルも対象)が変換した Graph へ差し替える。
マテリアルが無いときは何もしない。URP の Motion Blur と同じく Game の Camera だけで働く。

```csharp
public sealed class OmniMotionBlurFeature : ScriptableRendererFeature, IDisposable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
ScriptableObject ← 
ScriptableRendererFeature ← 
[OmniMotionBlurFeature](Omni.Rendering.OmniMotionBlurFeature.md)

#### 実装するインターフェース（Implements）

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

## フィールド（Fields）

### <a id="Omni_Rendering_OmniMotionBlurFeature_DebugClamp"></a> DebugClamp

```csharp
public const float DebugClamp = 0.05
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Rendering_OmniMotionBlurFeature_DebugExaggerate"></a> DebugExaggerate

確認用の強調(Editor のメニューから切り替える)。オンの間は Volume の値の代わりに、強さ 1(1 フレームの動きの全長)と
最大の長さ画面の 5%、標本数 16 を使う。製品の見た目には使わない。

```csharp
public static bool DebugExaggerate
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Rendering_OmniMotionBlurFeature_DebugIntensity"></a> DebugIntensity

```csharp
public const float DebugIntensity = 1
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Rendering_OmniMotionBlurFeature_DebugReplacementShader"></a> DebugReplacementShader

確認用の差し替え(Editor の自動操作から設定する)。null でなければ、付けたマテリアルの代わりにこの Fullscreen の Shader Graph で描く
(変換前と変換後の Graph を見比べるときなど)。製品の見た目には使わない。

```csharp
public static Shader DebugReplacementShader
```

#### 値（Field Value）

 Shader

### <a id="Omni_Rendering_OmniMotionBlurFeature_DebugSamples"></a> DebugSamples

```csharp
public const int DebugSamples = 16
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_Rendering_OmniMotionBlurFeature_AddRenderPasses_UnityEngine_Rendering_Universal_ScriptableRenderer_UnityEngine_Rendering_Universal_RenderingData__"></a> AddRenderPasses\(ScriptableRenderer, ref RenderingData\)

```csharp
public override void AddRenderPasses(ScriptableRenderer renderer, ref RenderingData renderingData)
```

#### 引数（Parameters）

`renderer` ScriptableRenderer

`renderingData` RenderingData

### <a id="Omni_Rendering_OmniMotionBlurFeature_Create"></a> Create\(\)

```csharp
public override void Create()
```

### <a id="Omni_Rendering_OmniMotionBlurFeature_Dispose_System_Boolean_"></a> Dispose\(bool\)

```csharp
protected override void Dispose(bool disposing)
```

#### 引数（Parameters）

`disposing` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
