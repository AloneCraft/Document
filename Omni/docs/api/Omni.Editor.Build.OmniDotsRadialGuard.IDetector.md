# <a id="Omni_Editor_Build_OmniDotsRadialGuard_IDetector"></a> Interface OmniDotsRadialGuard.IDetector

Namespace: [Omni.Editor.Build](Omni.Editor.Build.md)  
Assembly: Omni.Editor.dll  

Scene内とEditor WorldのDOTSコンテンツを数えます。

```csharp
public interface OmniDotsRadialGuard.IDetector
```

## メソッド（Methods）

### <a id="Omni_Editor_Build_OmniDotsRadialGuard_IDetector_CountEntitiesGraphicsEntities"></a> CountEntitiesGraphicsEntities\(\)

現在のWorldにあるEntities Graphicsの描画Entityを数えます。

```csharp
int CountEntitiesGraphicsEntities()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Build_OmniDotsRadialGuard_IDetector_CountSubScenes_UnityEngine_SceneManagement_Scene_"></a> CountSubScenes\(Scene\)

Scene内のSubSceneを数えます。

```csharp
int CountSubScenes(Scene scene)
```

#### 引数（Parameters）

`scene` Scene

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)
