# <a id="Omni_Localization_OmniPoParser"></a> Class OmniPoParser

Namespace: [Omni.Localization](Omni.Localization.md)  
Assembly: Radial.Runtime.dll  

gettext .po形式の必要最小サブセットを読むパーサです。
msgctxt/msgid/msgstrの複数行連結とエスケープ(\n \t \" \\)、
#, fuzzyと#~(廃止エントリ)のスキップに対応します。複数形(msgid_plural/msgstr[N])は非対応です。

```csharp
public static class OmniPoParser
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniPoParser](Omni.Localization.OmniPoParser.md)

## フィールド（Fields）

### <a id="Omni_Localization_OmniPoParser_ContextSeparator"></a> ContextSeparator

```csharp
public const string ContextSeparator = "\u0004"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Localization_OmniPoParser_Escape_System_String_"></a> Escape\(string\)

Escape()の逆変換です。Parse()が読めるリテラル1行分の中身を組み立てます。

```csharp
public static string Escape(string value)
```

#### 引数（Parameters）

`value` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Localization_OmniPoParser_Parse_System_String_"></a> Parse\(string\)

(context+ContextSeparator+id、contextが無ければid) → msgstr の辞書です。
<xref href="Omni.Localization.OmniL10n.Tr(System.String)" data-throw-if-not-resolved="false"></xref>/<xref href="Omni.Localization.OmniL10n.TrCtx(System.String%2cSystem.String)" data-throw-if-not-resolved="false"></xref>のキー解決と一致させます。

```csharp
public static Dictionary<string, string> Parse(string text)
```

#### 引数（Parameters）

`text` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary\-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Localization_OmniPoParser_ParseEntries_System_String_"></a> ParseEntries\(string\)

msgctxt/msgid/msgstrを分離したまま列挙します。カタログの書き戻し(マージツール)向けです。

```csharp
public static IEnumerable<OmniPoParser.Entry> ParseEntries(string text)
```

#### 引数（Parameters）

`text` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<[OmniPoParser](Omni.Localization.OmniPoParser.md).[Entry](Omni.Localization.OmniPoParser.Entry.md)\>
