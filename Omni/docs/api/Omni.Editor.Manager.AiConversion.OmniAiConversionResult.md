# <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionResult"></a> Class OmniAiConversionResult

Namespace: [Omni.Editor.Manager.AiConversion](Omni.Editor.Manager.AiConversion.md)  
Assembly: Omni.Manager.dll  

AI が返す結果 JSON（<code>omni.ai-conversion-result/1</code>）です。エージェントは決まったパスへ書き、チャットは Manager の貼り付け欄に貼ります。
取り込み前に <xref href="Omni.Editor.Manager.AiConversion.OmniAiConversionResult.TryValidate(Omni.Editor.Manager.AiConversion.OmniAiConversionResult%2cSystem.String%2cSystem.Collections.Generic.IEnumerable%7bSystem.String%7d%2cSystem.String%40%2cSystem.Int32%2cSystem.Boolean)" data-throw-if-not-resolved="false"></xref> で検査します（source 不一致、危険なパス、許可範囲外のファイル、規則欠けは拒否）。

```csharp
[Serializable]
public sealed class OmniAiConversionResult
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniAiConversionResult](Omni.Editor.Manager.AiConversion.OmniAiConversionResult.md)

## フィールド（Fields）

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionResult_ActionModified"></a> ActionModified

```csharp
public const string ActionModified = "modified"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionResult_ActionNone"></a> ActionNone

```csharp
public const string ActionNone = "none"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionResult_MaxJsonChars"></a> MaxJsonChars

```csharp
public const int MaxJsonChars = 1048576
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionResult_RuleCount"></a> RuleCount

```csharp
public const int RuleCount = 14
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionResult_SchemaId"></a> SchemaId

```csharp
public const string SchemaId = "omni.ai-conversion-result/1"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionResult_action"></a> action

```csharp
public string action
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionResult_attempt"></a> attempt

```csharp
public int attempt
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionResult_experimental"></a> experimental

```csharp
public bool experimental
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionResult_graph"></a> graph

```csharp
public OmniAiGraphInfo graph
```

#### 値（Field Value）

 [OmniAiGraphInfo](Omni.Editor.Manager.AiConversion.OmniAiGraphInfo.md)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionResult_humanDecisions"></a> humanDecisions

```csharp
public List<OmniAiHumanDecision> humanDecisions
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[OmniAiHumanDecision](Omni.Editor.Manager.AiConversion.OmniAiHumanDecision.md)\>

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionResult_modifiedFiles"></a> modifiedFiles

```csharp
public List<string> modifiedFiles
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionResult_route"></a> route

```csharp
public string route
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionResult_routeReason"></a> routeReason

```csharp
public string routeReason
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionResult_rules"></a> rules

```csharp
public List<OmniAiRuleResult> rules
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[OmniAiRuleResult](Omni.Editor.Manager.AiConversion.OmniAiRuleResult.md)\>

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionResult_schema"></a> schema

```csharp
public string schema
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionResult_source"></a> source

```csharp
public string source
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionResult_unverified"></a> unverified

```csharp
public List<string> unverified
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

## プロパティ（Properties）

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionResult_EffectiveAction"></a> EffectiveAction

<xref href="Omni.Editor.Manager.AiConversion.OmniAiConversionState" data-throw-if-not-resolved="false"></xref> へ渡す action です。Shader Graph の手順書（action が "none" で手順がある）は、
「対応不可」ではなく人が手順を行うのを待っている状態なので "modified" として扱います。

```csharp
public string EffectiveAction { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionResult_HasManualSteps"></a> HasManualSteps

Shader Graph の手順書として、人が行う手順を持っているか。

```csharp
public bool HasManualSteps { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionResult_FirstFailedRule"></a> FirstFailedRule\(\)

結果が FAIL と答えた最初の規則。無ければ null。

```csharp
public OmniAiRuleResult FirstFailedRule()
```

#### 戻り値（Returns）

 [OmniAiRuleResult](Omni.Editor.Manager.AiConversion.OmniAiRuleResult.md)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionResult_ToJson"></a> ToJson\(\)

```csharp
public string ToJson()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionResult_TryExtract_System_String_Omni_Editor_Manager_AiConversion_OmniAiConversionResult__System_String__"></a> TryExtract\(string, out OmniAiConversionResult, out string\)

貼り付けられた文章から結果 JSON を取り出します。```json で囲んだブロックを（複数あれば後ろから）先に試し、
無ければ最初の <code>{</code> から最後の <code>}</code> までを試します。形式の検査（<xref href="Omni.Editor.Manager.AiConversion.OmniAiConversionResult.TryValidate(Omni.Editor.Manager.AiConversion.OmniAiConversionResult%2cSystem.String%2cSystem.Collections.Generic.IEnumerable%7bSystem.String%7d%2cSystem.String%40%2cSystem.Int32%2cSystem.Boolean)" data-throw-if-not-resolved="false"></xref>）はしません。

```csharp
public static bool TryExtract(string pastedText, out OmniAiConversionResult result, out string error)
```

#### 引数（Parameters）

`pastedText` [string](https://learn.microsoft.com/dotnet/api/system.string)

`result` [OmniAiConversionResult](Omni.Editor.Manager.AiConversion.OmniAiConversionResult.md)

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionResult_TryValidate_Omni_Editor_Manager_AiConversion_OmniAiConversionResult_System_String_System_Collections_Generic_IEnumerable_System_String__System_String__System_Int32_System_Boolean_"></a> TryValidate\(OmniAiConversionResult, string, IEnumerable<string\>, out string, int, bool\)

取り込んでよい結果かを検査します。

```csharp
public static bool TryValidate(OmniAiConversionResult result, string expectedSource, IEnumerable<string> allowedFiles, out string error, int expectedAttempt = 0, bool allowRouteI = true)
```

#### 引数（Parameters）

`result` [OmniAiConversionResult](Omni.Editor.Manager.AiConversion.OmniAiConversionResult.md)

`expectedSource` [string](https://learn.microsoft.com/dotnet/api/system.string)

依頼した対象のプロジェクト相対パス。

`allowedFiles` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

依頼が変更を許したプロジェクト相対パス。対象と同じフォルダの新しい .shader／.hlsl／.shadergraph も許す。

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

`expectedAttempt` [int](https://learn.microsoft.com/dotnet/api/system.int32)

依頼の試行回数。0 なら比べない。

`allowRouteI` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

実験的な振り分け I を許すか（実験的機能が有効な依頼のみ）。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
