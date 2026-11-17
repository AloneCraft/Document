# <a id="Omni_Converter_OmniMaterialShaderSwitchService_Plan"></a> Class OmniMaterialShaderSwitchService.Plan

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

```csharp
public sealed class OmniMaterialShaderSwitchService.Plan
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniMaterialShaderSwitchService.Plan](Omni.Converter.OmniMaterialShaderSwitchService.Plan.md)

## フィールド（Fields）

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_Plan_AlreadyRadialMaterials"></a> AlreadyRadialMaterials

```csharp
public readonly List<Material> AlreadyRadialMaterials
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<Material\>

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_Plan_BuiltInItems"></a> BuiltInItems

```csharp
public readonly List<OmniMaterialShaderSwitchService.BuiltInPlanItem> BuiltInItems
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[OmniMaterialShaderSwitchService](Omni.Converter.OmniMaterialShaderSwitchService.md).[BuiltInPlanItem](Omni.Converter.OmniMaterialShaderSwitchService.BuiltInPlanItem.md)\>

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_Plan_DiagnosticItems"></a> DiagnosticItems

```csharp
public readonly List<OmniMaterialShaderSwitchService.DiagnosticPlanItem> DiagnosticItems
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[OmniMaterialShaderSwitchService](Omni.Converter.OmniMaterialShaderSwitchService.md).[DiagnosticPlanItem](Omni.Converter.OmniMaterialShaderSwitchService.DiagnosticPlanItem.md)\>

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_Plan_ExemptMaterials"></a> ExemptMaterials

Radialの変換対象にしない標準URP Shader(URPの2D Shader)の材質です。何も変えません。

```csharp
public readonly List<Material> ExemptMaterials
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<Material\>

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_Plan_HardIssues"></a> HardIssues

```csharp
public readonly List<string> HardIssues
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_Plan_InvestigatedScopes"></a> InvestigatedScopes

```csharp
public readonly List<string> InvestigatedScopes
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_Plan_Issues"></a> Issues

```csharp
public readonly List<string> Issues
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_Plan_Items"></a> Items

```csharp
public readonly List<OmniMaterialShaderSwitchService.PlanItem> Items
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[OmniMaterialShaderSwitchService](Omni.Converter.OmniMaterialShaderSwitchService.md).[PlanItem](Omni.Converter.OmniMaterialShaderSwitchService.PlanItem.md)\>

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_Plan_LoadedUsageLocations"></a> LoadedUsageLocations

```csharp
public readonly List<string> LoadedUsageLocations
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_Plan_ProblemMaterials"></a> ProblemMaterials

```csharp
public readonly HashSet<Material> ProblemMaterials
```

#### 値（Field Value）

 [HashSet](https://learn.microsoft.com/dotnet/api/system.collections.generic.hashset\-1)<Material\>

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_Plan_SharedUsages"></a> SharedUsages

```csharp
public readonly List<string> SharedUsages
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_Plan_UninvestigatedScopes"></a> UninvestigatedScopes

```csharp
public readonly List<string> UninvestigatedScopes
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_Plan_UsageLocations"></a> UsageLocations

```csharp
public readonly List<string> UsageLocations
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

## プロパティ（Properties）

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_Plan_IsApplicable"></a> IsApplicable

```csharp
public bool IsApplicable { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
