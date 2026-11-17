# <a id="Omni_Editor_Diagnostics_OmniObservationEnvironment"></a> Struct OmniObservationEnvironment

Namespace: [Omni.Editor.Diagnostics](Omni.Editor.Diagnostics.md)  
Assembly: Omni.Editor.dll  

前提の判定に使う Editor 環境の値です。実 Editor からは
<xref href="Omni.Editor.Diagnostics.OmniObservationEnvironmentReader" data-throw-if-not-resolved="false"></xref> が読み、テストは偽の値を直接作ります。

```csharp
[Serializable]
public struct OmniObservationEnvironment
```

## フィールド（Fields）

### <a id="Omni_Editor_Diagnostics_OmniObservationEnvironment_activeScenePath"></a> activeScenePath

active Scene の path です。無題の Scene は "&lt;untitled&gt;" です。

```csharp
public string activeScenePath
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniObservationEnvironment_dirtyScenePaths"></a> dirtyScenePaths

```csharp
public string[] dirtyScenePaths
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)\[\]

### <a id="Omni_Editor_Diagnostics_OmniObservationEnvironment_floatingWindowsOverSceneView"></a> floatingWindowsOverSceneView

遮蔽を読んだときだけ意味を持ちます。Scene View に重なる浮いたウィンドウの "Type(rect)" で、診断用です。
Scene View と重なるだけでは測定した画素を遮ったとは言えないので、前提にはしません（測定領域との重なりは
<xref href="Omni.Editor.Diagnostics.OmniObservationPreconditions.EvaluateRegionOcclusion(System.String%2cUnityEngine.RectInt%2cSystem.Collections.Generic.IReadOnlyList%7bOmni.Editor.Diagnostics.OmniScreenOccluder%7d)" data-throw-if-not-resolved="false"></xref> で判定します）。

```csharp
public string[] floatingWindowsOverSceneView
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)\[\]

### <a id="Omni_Editor_Diagnostics_OmniObservationEnvironment_foreground"></a> foreground

```csharp
public OmniForegroundState foreground
```

#### 値（Field Value）

 [OmniForegroundState](Omni.Editor.Diagnostics.OmniForegroundState.md)

### <a id="Omni_Editor_Diagnostics_OmniObservationEnvironment_foregroundLossCount"></a> foregroundLossCount

```csharp
public int foregroundLossCount
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Diagnostics_OmniObservationEnvironment_hasSceneView"></a> hasSceneView

```csharp
public bool hasSceneView
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_OmniObservationEnvironment_isCompiling"></a> isCompiling

```csharp
public bool isCompiling
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_OmniObservationEnvironment_isPlaying"></a> isPlaying

```csharp
public bool isPlaying
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_OmniObservationEnvironment_isPlayingOrWillChangePlaymode"></a> isPlayingOrWillChangePlaymode

```csharp
public bool isPlayingOrWillChangePlaymode
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_OmniObservationEnvironment_isUpdating"></a> isUpdating

```csharp
public bool isUpdating
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_OmniObservationEnvironment_loadedScenePaths"></a> loadedScenePaths

```csharp
public string[] loadedScenePaths
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)\[\]

### <a id="Omni_Editor_Diagnostics_OmniObservationEnvironment_omniOverlayExpanded"></a> omniOverlayExpanded

遮蔽を読んだときだけ意味を持ちます。Omni Overlay が表示かつ展開されていれば true です。

```csharp
public bool omniOverlayExpanded
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_OmniObservationEnvironment_refreshPending"></a> refreshPending

自動化の入口だけが知る値です。Reader は false を入れます。

```csharp
public bool refreshPending
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_OmniObservationEnvironment_scriptCompilationFailed"></a> scriptCompilationFailed

```csharp
public bool scriptCompilationFailed
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_OmniObservationEnvironment_testRunActive"></a> testRunActive

自動化の入口だけが知る値です。Reader は false を入れます。

```csharp
public bool testRunActive
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
