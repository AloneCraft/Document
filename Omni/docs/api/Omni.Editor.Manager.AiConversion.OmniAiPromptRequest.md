# <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptRequest"></a> Class OmniAiPromptRequest

Namespace: [Omni.Editor.Manager.AiConversion](Omni.Editor.Manager.AiConversion.md)  
Assembly: Omni.Manager.dll  

プロンプトを組み立てるための事実です。閉包の収集（<code>OmniShaderLabClosureCollector.Collect</code>）と、本文・失敗の取得は呼び出し側が行います。

```csharp
public sealed class OmniAiPromptRequest
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniAiPromptRequest](Omni.Editor.Manager.AiConversion.OmniAiPromptRequest.md)

## フィールド（Fields）

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptRequest_Attempt"></a> Attempt

この依頼の試行回数（1 始まり）。

```csharp
public int Attempt
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptRequest_ExperimentalDeferred"></a> ExperimentalDeferred

実験的な振り分け I（Deferred 専用の Shader に UniversalForward Pass を足す）を有効にするか。

```csharp
public bool ExperimentalDeferred
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptRequest_GraphMode"></a> GraphMode

Shader Graph の作業の形（"direct"＝直接編集、"manual"＝手順書）。チャット用は常に手順書になります。

```csharp
public string GraphMode
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptRequest_GraphSummary"></a> GraphSummary

Shader Graph のノード要約（呼び出し側が作る。JSON 全文は入れない）。

```csharp
public string GraphSummary
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptRequest_IsGraph"></a> IsGraph

```csharp
public bool IsGraph
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptRequest_Judge"></a> Judge

最新の機械判定。失敗の段・Pass・検出行をプロンプトに入れます。

```csharp
public OmniJudgeReport Judge
```

#### 値（Field Value）

 [OmniJudgeReport](Omni.Editor.Manager.AiConversion.OmniJudgeReport.md)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptRequest_OwnedFiles"></a> OwnedFiles

対象と、それが届く自作ファイルの閉包（対象を含む）。AI に見せてよいかは <xref href="Omni.Editor.Manager.AiConversion.OmniAiPromptBuilder.IsAiVisible(System.String)" data-throw-if-not-resolved="false"></xref> で絞ります。

```csharp
public List<OmniAiOwnedFile> OwnedFiles
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[OmniAiOwnedFile](Omni.Editor.Manager.AiConversion.OmniAiOwnedFile.md)\>

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptRequest_PreviousResult"></a> PreviousResult

前回の AI の結果。2 回目以降に入れます。

```csharp
public OmniAiConversionResult PreviousResult
```

#### 値（Field Value）

 [OmniAiConversionResult](Omni.Editor.Manager.AiConversion.OmniAiConversionResult.md)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptRequest_Purpose"></a> Purpose

「私の目的」の文。空なら既定の文。

```csharp
public string Purpose
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptRequest_ResultJsonPath"></a> ResultJsonPath

結果 JSON の書き先（プロジェクト相対、/ 区切り）。エージェント用で使う。

```csharp
public string ResultJsonPath
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptRequest_ShaderName"></a> ShaderName

対象の Shader 名（"Custom/Foo" など）。分からなければ空。

```csharp
public string ShaderName
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptRequest_SourcePath"></a> SourcePath

対象 Shader のプロジェクト相対パス。

```csharp
public string SourcePath
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptRequest_UnityVersion"></a> UnityVersion

Unity の版（"6000.6.4f1" など）。<xref href="Omni.Editor.Manager.AiConversion.OmniAiPromptBuilder.DetectVersions(System.String%40%2cSystem.String%40)" data-throw-if-not-resolved="false"></xref> で取れる。

```csharp
public string UnityVersion
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptRequest_UrpVersion"></a> UrpVersion

URP の版（"17.6.0" など）。

```csharp
public string UrpVersion
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
