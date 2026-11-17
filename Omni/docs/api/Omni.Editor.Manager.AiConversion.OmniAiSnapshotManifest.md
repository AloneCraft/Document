# <a id="Omni_Editor_Manager_AiConversion_OmniAiSnapshotManifest"></a> Class OmniAiSnapshotManifest

Namespace: [Omni.Editor.Manager.AiConversion](Omni.Editor.Manager.AiConversion.md)  
Assembly: Omni.Manager.dll  

依頼時の退避の一覧（<code>snapshots/&lt;attempt&gt;/manifest.json</code>）です。

```csharp
[Serializable]
public sealed class OmniAiSnapshotManifest
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniAiSnapshotManifest](Omni.Editor.Manager.AiConversion.OmniAiSnapshotManifest.md)

## フィールド（Fields）

### <a id="Omni_Editor_Manager_AiConversion_OmniAiSnapshotManifest_Absent"></a> Absent

```csharp
public const string Absent = "absent"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiSnapshotManifest_SchemaId"></a> SchemaId

```csharp
public const string SchemaId = "omni.ai-snapshot/1"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiSnapshotManifest_afterAi"></a> afterAi

AI が作業を終えた時点の状態（<xref href="Omni.Editor.Manager.AiConversion.OmniAiConversionStore.RecordAiOutput(System.String%2cSystem.Int32%2cSystem.Collections.Generic.IEnumerable%7bSystem.String%7d%2cSystem.Boolean)" data-throw-if-not-resolved="false"></xref> が記録）。人が後で直したかの検出に使う。

```csharp
public List<OmniAiSnapshotEntry> afterAi
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[OmniAiSnapshotEntry](Omni.Editor.Manager.AiConversion.OmniAiSnapshotEntry.md)\>

### <a id="Omni_Editor_Manager_AiConversion_OmniAiSnapshotManifest_afterAiRecorded"></a> afterAiRecorded

```csharp
public bool afterAiRecorded
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiSnapshotManifest_attempt"></a> attempt

```csharp
public int attempt
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiSnapshotManifest_createdUtc"></a> createdUtc

```csharp
public string createdUtc
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiSnapshotManifest_files"></a> files

依頼時点の状態（退避の対象）。

```csharp
public List<OmniAiSnapshotEntry> files
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[OmniAiSnapshotEntry](Omni.Editor.Manager.AiConversion.OmniAiSnapshotEntry.md)\>

### <a id="Omni_Editor_Manager_AiConversion_OmniAiSnapshotManifest_schema"></a> schema

```csharp
public string schema
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
