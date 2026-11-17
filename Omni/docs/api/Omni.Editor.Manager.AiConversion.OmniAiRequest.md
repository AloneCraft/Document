# <a id="Omni_Editor_Manager_AiConversion_OmniAiRequest"></a> Class OmniAiRequest

Namespace: [Omni.Editor.Manager.AiConversion](Omni.Editor.Manager.AiConversion.md)  
Assembly: Omni.Manager.dll  

AI への依頼の記録（<code>request.json</code>）です。依頼のたびに上書きします。

```csharp
[Serializable]
public sealed class OmniAiRequest
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniAiRequest](Omni.Editor.Manager.AiConversion.OmniAiRequest.md)

## フィールド（Fields）

### <a id="Omni_Editor_Manager_AiConversion_OmniAiRequest_GraphDirect"></a> GraphDirect

```csharp
public const string GraphDirect = "direct"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiRequest_GraphManual"></a> GraphManual

```csharp
public const string GraphManual = "manual"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiRequest_ModeAgent"></a> ModeAgent

```csharp
public const string ModeAgent = "agent"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiRequest_ModeChat"></a> ModeChat

```csharp
public const string ModeChat = "chat"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiRequest_SchemaId"></a> SchemaId

```csharp
public const string SchemaId = "omni.ai-request/1"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiRequest_attempt"></a> attempt

試行回数（1 始まり）。

```csharp
public int attempt
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiRequest_createdUtc"></a> createdUtc

依頼した時刻（UTC、ISO 8601 の往復形式）。

```csharp
public string createdUtc
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiRequest_experimental"></a> experimental

```csharp
public bool experimental
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiRequest_graphMode"></a> graphMode

Shader Graph の作業の形。"direct" か "manual"（ShaderLab のときは空）。

```csharp
public string graphMode
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiRequest_mode"></a> mode

"chat" か "agent"。

```csharp
public string mode
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiRequest_schema"></a> schema

```csharp
public string schema
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiRequest_source"></a> source

対象 Shader のプロジェクト相対パス。

```csharp
public string source
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiRequest_sourceFingerprintAtRequest"></a> sourceFingerprintAtRequest

依頼したときの元の指紋。

```csharp
public string sourceFingerprintAtRequest
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiRequest_watchedPaths"></a> watchedPaths

保存を見張るプロジェクト相対パス。

```csharp
public List<string> watchedPaths
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>
