# <a id="Omni_Logical_IRenderPoseProvider"></a> Interface IRenderPoseProvider

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

CameraCombinationVerificationのTMPラベルなど、カメラごとに論理姿勢が変わるRendererへ
Transformを書き戻さず描画姿勢を供給するインターフェースです。

```csharp
public interface IRenderPoseProvider
```

## メソッド（Methods）

### <a id="Omni_Logical_IRenderPoseProvider_TryGetRenderPose_UnityEngine_Camera_Omni_Logical_SceneViewRenderContext__Omni_Logical_RenderPose__"></a> TryGetRenderPose\(Camera, in SceneViewRenderContext, out RenderPose\)

指定カメラの描画中に使う論理姿勢を返します。

```csharp
bool TryGetRenderPose(Camera camera, in SceneViewRenderContext context, out RenderPose pose)
```

#### 引数（Parameters）

`camera` Camera

現在描画中のカメラです。

`context` [SceneViewRenderContext](Omni.Logical.SceneViewRenderContext.md)

GPU描画時に凍結されたScene View論理コンテキストです。

`pose` [RenderPose](Omni.Logical.RenderPose.md)

Transformへ書き戻さない論理描画姿勢です。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
