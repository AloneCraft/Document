# <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSection"></a> Class OmniAiPromptSection

Namespace: [Omni.Editor.Manager.AiConversion](Omni.Editor.Manager.AiConversion.md)  
Assembly: Omni.Manager.dll  

プロンプトの 1 つの節（最上位の <code># 見出し</code> から次の見出しの前まで）。

```csharp
public sealed class OmniAiPromptSection
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniAiPromptSection](Omni.Editor.Manager.AiConversion.OmniAiPromptSection.md)

## コンストラクター（Constructors）

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSection__ctor_System_String_System_String_"></a> OmniAiPromptSection\(string, string\)

```csharp
public OmniAiPromptSection(string title, string body)
```

#### 引数（Parameters）

`title` [string](https://learn.microsoft.com/dotnet/api/system.string)

`body` [string](https://learn.microsoft.com/dotnet/api/system.string)

## プロパティ（Properties）

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSection_Body"></a> Body

見出しの行を除く本文（前後の空行は除く、改行は LF）。

```csharp
public string Body { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSection_Name"></a> Name

見出しの名前。全角の括弧の開き（の前の部分で、括弧の中の補足を除く。節の検索はこの名前で行う。

```csharp
public string Name { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSection_Title"></a> Title

見出しの全文（<code># </code> を除く）。前文（最初の見出しの前）は空文字。

```csharp
public string Title { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptSection_ToText"></a> ToText\(\)

見出し付きの全文。前文は本文だけ。

```csharp
public string ToText()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
