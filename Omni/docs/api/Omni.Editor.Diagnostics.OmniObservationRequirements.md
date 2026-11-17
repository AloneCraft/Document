# <a id="Omni_Editor_Diagnostics_OmniObservationRequirements"></a> Struct OmniObservationRequirements

Namespace: [Omni.Editor.Diagnostics](Omni.Editor.Diagnostics.md)  
Assembly: Omni.Editor.dll  

観測を始める前に満たすべき前提です。

```csharp
[Serializable]
public struct OmniObservationRequirements
```

## フィールド（Fields）

### <a id="Omni_Editor_Diagnostics_OmniObservationRequirements_allowPlayMode"></a> allowPlayMode

```csharp
public bool allowPlayMode
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_OmniObservationRequirements_expectedScenePaths"></a> expectedScenePaths

読み込まれているべき Scene の path の集合です。null なら照合しません。空配列は何も読み込まれて
いないことを要求します。

```csharp
public string[] expectedScenePaths
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)\[\]

### <a id="Omni_Editor_Diagnostics_OmniObservationRequirements_requireCleanScenes"></a> requireCleanScenes

```csharp
public bool requireCleanScenes
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_OmniObservationRequirements_requireForeground"></a> requireForeground

```csharp
public bool requireForeground
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_OmniObservationRequirements_requireNoOcclusion"></a> requireNoOcclusion

Omni Overlay が展開されていないことを要求します。浮いたウィンドウは測定領域が分かる観測者が
<xref href="Omni.Editor.Diagnostics.OmniObservationPreconditions.EvaluateRegionOcclusion(System.String%2cUnityEngine.RectInt%2cSystem.Collections.Generic.IReadOnlyList%7bOmni.Editor.Diagnostics.OmniScreenOccluder%7d)" data-throw-if-not-resolved="false"></xref> で判定します。

```csharp
public bool requireNoOcclusion
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_OmniObservationRequirements_requireSceneView"></a> requireSceneView

```csharp
public bool requireSceneView
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
