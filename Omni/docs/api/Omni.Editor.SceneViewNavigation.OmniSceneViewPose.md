# <a id="Omni_Editor_SceneViewNavigation_OmniSceneViewPose"></a> Class OmniSceneViewPose

Namespace: [Omni.Editor.SceneViewNavigation](Omni.Editor.SceneViewNavigation.md)  
Assembly: Omni.Editor.dll  

Scene View 専用の論理 eye 操作。Scene と Main Camera は変更しません。

```csharp
[InitializeOnLoad]
public static class OmniSceneViewPose
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniSceneViewPose](Omni.Editor.SceneViewNavigation.OmniSceneViewPose.md)

## メソッド（Methods）

### <a id="Omni_Editor_SceneViewNavigation_OmniSceneViewPose_TryCapture_UnityEditor_SceneView_Omni_Editor_SceneViewNavigation_OmniSceneViewPose_Snapshot__"></a> TryCapture\(SceneView, out Snapshot\)

既存 viewport の raw Position3 と Unity 回転を取得します。

```csharp
public static bool TryCapture(SceneView view, out OmniSceneViewPose.Snapshot pose)
```

#### 引数（Parameters）

`view` SceneView

`pose` [OmniSceneViewPose](Omni.Editor.SceneViewNavigation.OmniSceneViewPose.md).[Snapshot](Omni.Editor.SceneViewNavigation.OmniSceneViewPose.Snapshot.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_SceneViewNavigation_OmniSceneViewPose_TryMove_Omni_Editor_SceneViewNavigation_OmniSceneViewPose_Snapshot__Omni_Logical_Position3__UnityEngine_Quaternion_"></a> TryMove\(in Snapshot, in Position3, Quaternion\)

同じ View/camera/Scene へ raw eye と有限回転を適用します。

```csharp
public static bool TryMove(in OmniSceneViewPose.Snapshot owner, in Position3 eye, Quaternion rotation)
```

#### 引数（Parameters）

`owner` [OmniSceneViewPose](Omni.Editor.SceneViewNavigation.OmniSceneViewPose.md).[Snapshot](Omni.Editor.SceneViewNavigation.OmniSceneViewPose.Snapshot.md)

`eye` Position3

`rotation` Quaternion

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
