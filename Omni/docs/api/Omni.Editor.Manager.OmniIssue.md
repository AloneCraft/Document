# <a id="Omni_Editor_Manager_OmniIssue"></a> Class OmniIssue

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

Omni Manager が検出した単一の問題を表します。

```csharp
public class OmniIssue
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniIssue](Omni.Editor.Manager.OmniIssue.md)

## フィールド（Fields）

### <a id="Omni_Editor_Manager_OmniIssue_Category"></a> Category

```csharp
public IssueCategory Category
```

#### 値（Field Value）

 [IssueCategory](Omni.Editor.Manager.IssueCategory.md)

### <a id="Omni_Editor_Manager_OmniIssue_Description"></a> Description

```csharp
public string Description
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_OmniIssue_IsFixable"></a> IsFixable

```csharp
public bool IsFixable
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_OmniIssue_RecommendedFix"></a> RecommendedFix

```csharp
public string RecommendedFix
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_OmniIssue_Severity"></a> Severity

```csharp
public IssueSeverity Severity
```

#### 値（Field Value）

 [IssueSeverity](Omni.Editor.Manager.IssueSeverity.md)

### <a id="Omni_Editor_Manager_OmniIssue_TargetAssetPath"></a> TargetAssetPath

```csharp
public string TargetAssetPath
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_OmniIssue_TargetObjectId"></a> TargetObjectId

```csharp
public GlobalObjectId TargetObjectId
```

#### 値（Field Value）

 GlobalObjectId

## プロパティ（Properties）

### <a id="Omni_Editor_Manager_OmniIssue_SeverityLabel"></a> SeverityLabel

```csharp
public string SeverityLabel { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
