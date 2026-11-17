# <a id="Omni_Editor_Manager_MaterialEntry"></a> Class MaterialEntry

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

1つの実Materialアセットに対応するスキャン結果です。

```csharp
public sealed class MaterialEntry
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[MaterialEntry](Omni.Editor.Manager.MaterialEntry.md)

## フィールド（Fields）

### <a id="Omni_Editor_Manager_MaterialEntry_AppliedInScene"></a> AppliedInScene

```csharp
public bool AppliedInScene
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_MaterialEntry_ExclusionDetail"></a> ExclusionDetail

```csharp
public string ExclusionDetail
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_MaterialEntry_GenerationOrigin"></a> GenerationOrigin

```csharp
public string GenerationOrigin
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_MaterialEntry_IsNativeRadial"></a> IsNativeRadial

最初からRadialのMaterialです（UB-009）。Shader自身が対数契約を実装し、台帳にも標準版にも
対応しないため、標準へ戻す対象ではありません。<xref href="Omni.Editor.Manager.MaterialEntry.RestoreDetail" data-throw-if-not-resolved="false"></xref> が設定される条件と同じです。

```csharp
public bool IsNativeRadial
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_MaterialEntry_OmniMaterial"></a> OmniMaterial

```csharp
public Material OmniMaterial
```

#### 値（Field Value）

 Material

### <a id="Omni_Editor_Manager_MaterialEntry_OmniPath"></a> OmniPath

```csharp
public string OmniPath
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_MaterialEntry_ProblemDetail"></a> ProblemDetail

```csharp
public string ProblemDetail
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_MaterialEntry_RadialShaderPath"></a> RadialShaderPath

```csharp
public string RadialShaderPath
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_MaterialEntry_RadialState"></a> RadialState

```csharp
public RadialVersionState RadialState
```

#### 値（Field Value）

 [RadialVersionState](Omni.Editor.Manager.RadialVersionState.md)

### <a id="Omni_Editor_Manager_MaterialEntry_RestoreDetail"></a> RestoreDetail

```csharp
public string RestoreDetail
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_MaterialEntry_SceneUsageCount"></a> SceneUsageCount

```csharp
public int SceneUsageCount
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Manager_MaterialEntry_ShaderName"></a> ShaderName

```csharp
public string ShaderName
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_MaterialEntry_ShaderUsage"></a> ShaderUsage

```csharp
public MaterialShaderUsageKind ShaderUsage
```

#### 値（Field Value）

 [MaterialShaderUsageKind](Omni.Editor.Manager.MaterialShaderUsageKind.md)

### <a id="Omni_Editor_Manager_MaterialEntry_SourceMaterial"></a> SourceMaterial

```csharp
public Material SourceMaterial
```

#### 値（Field Value）

 Material

### <a id="Omni_Editor_Manager_MaterialEntry_SourcePath"></a> SourcePath

```csharp
public string SourcePath
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_MaterialEntry_SourceShaderPath"></a> SourceShaderPath

```csharp
public string SourceShaderPath
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_MaterialEntry_Status"></a> Status

```csharp
public MaterialStatus Status
```

#### 値（Field Value）

 [MaterialStatus](Omni.Editor.Manager.MaterialStatus.md)

### <a id="Omni_Editor_Manager_MaterialEntry_UsageLocations"></a> UsageLocations

```csharp
public readonly List<string> UsageLocations
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

## プロパティ（Properties）

### <a id="Omni_Editor_Manager_MaterialEntry_HasProblem"></a> HasProblem

```csharp
public bool HasProblem { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_MaterialEntry_IsExcluded"></a> IsExcluded

```csharp
public bool IsExcluded { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_MaterialEntry_NeedsPreparation"></a> NeedsPreparation

```csharp
public bool NeedsPreparation { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
