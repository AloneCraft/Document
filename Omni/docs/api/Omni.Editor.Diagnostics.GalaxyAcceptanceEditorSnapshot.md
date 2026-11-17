# <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot"></a> Class GalaxyAcceptanceEditorSnapshot

Namespace: [Omni.Editor.Diagnostics](Omni.Editor.Diagnostics.md)  
Assembly: Omni.Editor.dll  

受入前に記録するEditor状態のシリアライズ可能なスナップショットです。
Scene/Selection/SceneView以外の設定も同じ復元単位へ含め、失敗時にGalaxyを
強制的に開き直すことを禁止します。

```csharp
[Serializable]
public sealed class GalaxyAcceptanceEditorSnapshot
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[GalaxyAcceptanceEditorSnapshot](Omni.Editor.Diagnostics.GalaxyAcceptanceEditorSnapshot.md)

## フィールド（Fields）

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_activeSceneDirty"></a> activeSceneDirty

```csharp
public bool activeSceneDirty
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_activeScenePath"></a> activeScenePath

```csharp
public string activeScenePath
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_brgEnabled"></a> brgEnabled

```csharp
public bool brgEnabled
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_cullingEnabled"></a> cullingEnabled

```csharp
public bool cullingEnabled
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_cursorX"></a> cursorX

```csharp
public int cursorX
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_cursorY"></a> cursorY

```csharp
public int cursorY
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_foregroundWindowHandle"></a> foregroundWindowHandle

```csharp
public long foregroundWindowHandle
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_graphicsApis"></a> graphicsApis

```csharp
public string[] graphicsApis
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)\[\]

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_graphicsDeviceType"></a> graphicsDeviceType

```csharp
public string graphicsDeviceType
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_hasCursorPosition"></a> hasCursorPosition

```csharp
public bool hasCursorPosition
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_hasForegroundWindow"></a> hasForegroundWindow

```csharp
public bool hasForegroundWindow
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_hasSceneViewRadialState"></a> hasSceneViewRadialState

```csharp
public bool hasSceneViewRadialState
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_isCompiling"></a> isCompiling

```csharp
public bool isCompiling
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_isPlaying"></a> isPlaying

```csharp
public bool isPlaying
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_isUpdating"></a> isUpdating

```csharp
public bool isUpdating
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_logicalSceneViewPivotX"></a> logicalSceneViewPivotX

```csharp
public ulong[] logicalSceneViewPivotX
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)\[\]

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_logicalSceneViewPivotY"></a> logicalSceneViewPivotY

```csharp
public ulong[] logicalSceneViewPivotY
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)\[\]

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_logicalSceneViewPivotZ"></a> logicalSceneViewPivotZ

```csharp
public ulong[] logicalSceneViewPivotZ
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)\[\]

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_navigatorOverlayVisible"></a> navigatorOverlayVisible

```csharp
public bool navigatorOverlayVisible
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_qualityName"></a> qualityName

```csharp
public string qualityName
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_renderingMode"></a> renderingMode

```csharp
public string renderingMode
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_sceneSetup"></a> sceneSetup

```csharp
public GalaxyAcceptanceSceneSetupSnapshot[] sceneSetup
```

#### 値（Field Value）

 [GalaxyAcceptanceSceneSetupSnapshot](Omni.Editor.Diagnostics.GalaxyAcceptanceSceneSetupSnapshot.md)\[\]

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_sceneViewExploreFromSceneView"></a> sceneViewExploreFromSceneView

```csharp
public bool sceneViewExploreFromSceneView
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_sceneViewIn2D"></a> sceneViewIn2D

```csharp
public bool sceneViewIn2D
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_sceneViewOrthographic"></a> sceneViewOrthographic

```csharp
public bool sceneViewOrthographic
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_sceneViewPivot"></a> sceneViewPivot

```csharp
public Vector3 sceneViewPivot
```

#### 値（Field Value）

 Vector3

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_sceneViewRadialCameraGlobalObjectId"></a> sceneViewRadialCameraGlobalObjectId

```csharp
public string sceneViewRadialCameraGlobalObjectId
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_sceneViewRotation"></a> sceneViewRotation

```csharp
public Quaternion sceneViewRotation
```

#### 値（Field Value）

 Quaternion

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_sceneViewRotationLocked"></a> sceneViewRotationLocked

```csharp
public bool sceneViewRotationLocked
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_sceneViewSize"></a> sceneViewSize

```csharp
public float sceneViewSize
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_sceneViews"></a> sceneViews

```csharp
public GalaxyAcceptanceSceneViewSnapshot[] sceneViews
```

#### 値（Field Value）

 [GalaxyAcceptanceSceneViewSnapshot](Omni.Editor.Diagnostics.GalaxyAcceptanceSceneViewSnapshot.md)\[\]

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_schemaVersion"></a> schemaVersion

```csharp
public int schemaVersion
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_selectionGlobalObjectIds"></a> selectionGlobalObjectIds

```csharp
public string[] selectionGlobalObjectIds
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)\[\]

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_useDefaultGraphicsApis"></a> useDefaultGraphicsApis

```csharp
public bool useDefaultGraphicsApis
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
