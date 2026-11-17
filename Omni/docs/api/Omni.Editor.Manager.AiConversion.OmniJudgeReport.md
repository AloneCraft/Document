# <a id="Omni_Editor_Manager_AiConversion_OmniJudgeReport"></a> Class OmniJudgeReport

Namespace: [Omni.Editor.Manager.AiConversion](Omni.Editor.Manager.AiConversion.md)  
Assembly: Omni.Manager.dll  

自作 Shader 1 本の機械判定の結果です。judge.json にそのまま保存します。

```csharp
[Serializable]
public sealed class OmniJudgeReport
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniJudgeReport](Omni.Editor.Manager.AiConversion.OmniJudgeReport.md)

## フィールド（Fields）

### <a id="Omni_Editor_Manager_AiConversion_OmniJudgeReport_KindGraph"></a> KindGraph

```csharp
public const string KindGraph = "graph"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniJudgeReport_KindShaderLab"></a> KindShaderLab

```csharp
public const string KindShaderLab = "shaderlab"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniJudgeReport_SchemaId"></a> SchemaId

```csharp
public const string SchemaId = "omni.judge/1"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniJudgeReport_compile"></a> compile

```csharp
public List<OmniJudgeCompileMessage> compile
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[OmniJudgeCompileMessage](Omni.Editor.Manager.AiConversion.OmniJudgeCompileMessage.md)\>

### <a id="Omni_Editor_Manager_AiConversion_OmniJudgeReport_firstFailure"></a> firstFailure

```csharp
public string firstFailure
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniJudgeReport_kind"></a> kind

```csharp
public string kind
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniJudgeReport_outputFingerprint"></a> outputFingerprint

```csharp
public string outputFingerprint
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniJudgeReport_passed"></a> passed

```csharp
public bool passed
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_AiConversion_OmniJudgeReport_passes"></a> passes

```csharp
public List<OmniJudgePass> passes
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[OmniJudgePass](Omni.Editor.Manager.AiConversion.OmniJudgePass.md)\>

### <a id="Omni_Editor_Manager_AiConversion_OmniJudgeReport_schema"></a> schema

```csharp
public string schema
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniJudgeReport_silent"></a> silent

```csharp
public List<OmniJudgeSilentHit> silent
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[OmniJudgeSilentHit](Omni.Editor.Manager.AiConversion.OmniJudgeSilentHit.md)\>

### <a id="Omni_Editor_Manager_AiConversion_OmniJudgeReport_source"></a> source

```csharp
public string source
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniJudgeReport_sourceFingerprint"></a> sourceFingerprint

```csharp
public string sourceFingerprint
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniJudgeReport_stages"></a> stages

```csharp
public List<OmniJudgeStage> stages
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[OmniJudgeStage](Omni.Editor.Manager.AiConversion.OmniJudgeStage.md)\>
