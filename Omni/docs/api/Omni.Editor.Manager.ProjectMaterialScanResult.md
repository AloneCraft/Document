# <a id="Omni_Editor_Manager_ProjectMaterialScanResult"></a> Class ProjectMaterialScanResult

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

書換え可能なProject Materialと、除外理由を分離した走査結果です。

```csharp
public sealed class ProjectMaterialScanResult
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[ProjectMaterialScanResult](Omni.Editor.Manager.ProjectMaterialScanResult.md)

## フィールド（Fields）

### <a id="Omni_Editor_Manager_ProjectMaterialScanResult_Entries"></a> Entries

```csharp
public readonly List<MaterialEntry> Entries
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[MaterialEntry](Omni.Editor.Manager.MaterialEntry.md)\>

### <a id="Omni_Editor_Manager_ProjectMaterialScanResult_Exclusions"></a> Exclusions

```csharp
public readonly List<MaterialScanExclusion> Exclusions
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[MaterialScanExclusion](Omni.Editor.Manager.MaterialScanExclusion.md)\>
