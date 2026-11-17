# <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSource"></a> Class OmniAiPromptSource

Namespace: [Omni.Editor.Manager.AiConversion](Omni.Editor.Manager.AiConversion.md)  
Assembly: Omni.Manager.dll  

<code>Documentation/CustomShaderAiPrompt.md</code> のプロンプトを、目印の間から取り出して節に分けます（プロンプトの単一の正本）。
目印は 3 組あります: 本体 <code>omni:ai-prompt</code>、Manager が足す節 <code>omni:ai-prompt-manager</code>、実験的な振り分け <code>omni:ai-prompt-experimental</code>。
各目印の間の <code>````text</code> で囲んだ内側が本文で、最上位の <code># </code> 見出しで節に分けます。
読み込めない・形が崩れているときは例外ではなく理由を返します（呼び出し側はコピーを無効にして理由を出す）。

```csharp
public sealed class OmniAiPromptSource
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniAiPromptSource](Omni.Editor.Manager.AiConversion.OmniAiPromptSource.md)

## フィールド（Fields）

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSource_ExperimentalRegion"></a> ExperimentalRegion

```csharp
public const string ExperimentalRegion = "omni:ai-prompt-experimental"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSource_InvariantsBulletPrefix"></a> InvariantsBulletPrefix

対象の節の中で、そのまま使う「不変にするもの」の項目の先頭。

```csharp
public const string InvariantsBulletPrefix = "- 不変にするもの"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSource_MainRegion"></a> MainRegion

```csharp
public const string MainRegion = "omni:ai-prompt"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSource_ManagerRegion"></a> ManagerRegion

```csharp
public const string ManagerRegion = "omni:ai-prompt-manager"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSource_RelativePath"></a> RelativePath

```csharp
public const string RelativePath = "Documentation/CustomShaderAiPrompt.md"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSource_SectionAgentWork"></a> SectionAgentWork

```csharp
public const string SectionAgentWork = "エージェントとして作業するとき"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSource_SectionChatAnswer"></a> SectionChatAnswer

```csharp
public const string SectionChatAnswer = "チャットで答えるとき"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSource_SectionExperimentalRoute"></a> SectionExperimentalRoute

```csharp
public const string SectionExperimentalRoute = "実験的な振り分けI"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSource_SectionForbidden"></a> SectionForbidden

```csharp
public const string SectionForbidden = "してはいけないこと"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSource_SectionGraphDirect"></a> SectionGraphDirect

```csharp
public const string SectionGraphDirect = "Shader Graphを直接編集するとき"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSource_SectionGraphManual"></a> SectionGraphManual

```csharp
public const string SectionGraphManual = "Shader Graphの手順書"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSource_SectionGraphViewFix"></a> SectionGraphViewFix

```csharp
public const string SectionGraphViewFix = "Shader Graphの視線の直し方"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSource_SectionOutput"></a> SectionOutput

```csharp
public const string SectionOutput = "出力の形式"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSource_SectionResultJson"></a> SectionResultJson

```csharp
public const string SectionResultJson = "結果JSONの形式"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSource_SectionRouting"></a> SectionRouting

```csharp
public const string SectionRouting = "状況別の振り分け"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSource_SectionRules"></a> SectionRules

```csharp
public const string SectionRules = "守る規則"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSource_SectionTarget"></a> SectionTarget

```csharp
public const string SectionTarget = "対象"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## プロパティ（Properties）

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSource_ExperimentalSections"></a> ExperimentalSections

```csharp
public IReadOnlyList<OmniAiPromptSection> ExperimentalSections { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[OmniAiPromptSection](Omni.Editor.Manager.AiConversion.OmniAiPromptSection.md)\>

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSource_MainSections"></a> MainSections

```csharp
public IReadOnlyList<OmniAiPromptSection> MainSections { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[OmniAiPromptSection](Omni.Editor.Manager.AiConversion.OmniAiPromptSection.md)\>

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSource_ManagerSections"></a> ManagerSections

```csharp
public IReadOnlyList<OmniAiPromptSection> ManagerSections { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[OmniAiPromptSection](Omni.Editor.Manager.AiConversion.OmniAiPromptSection.md)\>

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSource_Preamble"></a> Preamble

本体の前文（最初の見出しの前。役割の説明）。

```csharp
public string Preamble { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSource_Experimental_System_String_"></a> Experimental\(string\)

実験的な振り分けの節。無ければ null。

```csharp
public OmniAiPromptSection Experimental(string title)
```

#### 引数（Parameters）

`title` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [OmniAiPromptSection](Omni.Editor.Manager.AiConversion.OmniAiPromptSection.md)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSource_InvariantsBullet"></a> InvariantsBullet\(\)

「対象」の節にある「不変にするもの」の項目（次の項目の前まで）。

```csharp
public string InvariantsBullet()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSource_Main_System_String_"></a> Main\(string\)

本体の節。無ければ null。

```csharp
public OmniAiPromptSection Main(string title)
```

#### 引数（Parameters）

`title` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [OmniAiPromptSection](Omni.Editor.Manager.AiConversion.OmniAiPromptSection.md)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSource_Manager_System_String_"></a> Manager\(string\)

Manager が足す節。無ければ null。

```csharp
public OmniAiPromptSection Manager(string title)
```

#### 引数（Parameters）

`title` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [OmniAiPromptSection](Omni.Editor.Manager.AiConversion.OmniAiPromptSection.md)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSource_TryLoad_Omni_Editor_Manager_AiConversion_OmniAiPromptSource__System_String__"></a> TryLoad\(out OmniAiPromptSource, out string\)

製品の置き場（開発: Assets/Omni、UPM: Packages/com.omni.rendering）から読む。

```csharp
public static bool TryLoad(out OmniAiPromptSource source, out string error)
```

#### 引数（Parameters）

`source` [OmniAiPromptSource](Omni.Editor.Manager.AiConversion.OmniAiPromptSource.md)

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSource_TryLoadFile_System_String_Omni_Editor_Manager_AiConversion_OmniAiPromptSource__System_String__"></a> TryLoadFile\(string, out OmniAiPromptSource, out string\)

```csharp
public static bool TryLoadFile(string absolutePath, out OmniAiPromptSource source, out string error)
```

#### 引数（Parameters）

`absolutePath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`source` [OmniAiPromptSource](Omni.Editor.Manager.AiConversion.OmniAiPromptSource.md)

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSource_TryParse_System_String_Omni_Editor_Manager_AiConversion_OmniAiPromptSource__System_String__"></a> TryParse\(string, out OmniAiPromptSource, out string\)

文書の全文から取り出す（テストからも使う）。

```csharp
public static bool TryParse(string markdown, out OmniAiPromptSource source, out string error)
```

#### 引数（Parameters）

`markdown` [string](https://learn.microsoft.com/dotnet/api/system.string)

`source` [OmniAiPromptSource](Omni.Editor.Manager.AiConversion.OmniAiPromptSource.md)

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
