# <a id="Omni_Localization_OmniL10n"></a> Class OmniL10n

Namespace: [Omni.Localization](Omni.Localization.md)  
Assembly: Radial.Runtime.dll  

Omni独自のgettext方式ローカライズAPIです。カタログは<code>Assets/Omni/Core/Localization~/&lt;locale&gt;.po</code>から
Editor専用に読み込みます。フォルダ名の<code>~</code>は、.poをUnityの翻訳機能（LocalizationImporter）に取り込ませないためです（取り込ませるとpackageで「will not be compiled」のエラーになります）。Playerビルドにはカタログを含めず、Tr()はmsgid(英語原文)をそのまま返します。

```csharp
public static class OmniL10n
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniL10n](Omni.Localization.OmniL10n.md)

## 補足（Remarks）

UnityEditor.L10nをそのまま使わない理由は、対応言語がEditorの言語(ja/ko/zh-hans/zh-hant等)に固定されており
任意言語へスケールアウトできないためです。方式(英語msgid・gettext .po・Tr() API)はUnity純正パッケージ
(Timeline/Memory Profiler等)に倣いつつ、カタログ探索とロケール解決だけ独自実装します。

## プロパティ（Properties）

### <a id="Omni_Localization_OmniL10n_AvailableLocales"></a> AvailableLocales

選択可能なロケールコード一覧です。"en"(msgidの言語なのでカタログ不要)は常に含み、
それ以外は<code>Assets/Omni/Core/Localization~/*.po</code>から見つかったものです。

```csharp
public static IReadOnlyList<string> AvailableLocales { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Localization_OmniL10n_CurrentLocale"></a> CurrentLocale

現在解決されているロケールコードです("ja"/"en"/"fr"等)。カタログが無ければ"en"相当です。

```csharp
public static string CurrentLocale { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Localization_OmniL10n_IsJapaneseEnvironment"></a> IsJapaneseEnvironment\(\)

デモHUDの起動言語に使う「日本語環境か」です。Editorでは(Play中も)Omniの表示言語＝Editorの言語に追従し、
Playerでは実行環境(OS)の言語に従います。Web(WebGPU)は英語のみなので常にfalseです。

```csharp
public static bool IsJapaneseEnvironment()
```

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Localization_OmniL10n_NativeLanguageName_System_String_"></a> NativeLanguageName\(string\)

言語選択メニュー表示用に、ロケールコードをその言語自身の表記で返します。未知のコードはそのまま返します。

```csharp
public static string NativeLanguageName(string locale)
```

#### 引数（Parameters）

`locale` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Localization_OmniL10n_Reload"></a> Reload\(\)

カタログを破棄して再読込します。手動で.poを編集した後の反映に使います。

```csharp
public static void Reload()
```

### <a id="Omni_Localization_OmniL10n_SetLocale_System_String_"></a> SetLocale\(string\)

表示言語を明示的に上書きします。空文字は「自動(Editor言語に追従)」を意味します。

```csharp
public static void SetLocale(string locale)
```

#### 引数（Parameters）

`locale` [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Localization_OmniL10n_Tr_System_String_"></a> Tr\(string\)

msgid(英語原文)を現在ロケールへ翻訳します。訳が無ければmsgidをそのまま返します。

```csharp
public static string Tr(string source)
```

#### 引数（Parameters）

`source` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Localization_OmniL10n_Tr_System_String_System_Object___"></a> Tr\(string, params object\[\]\)

Tr(source)を書式文字列として使い、argsを埋め込みます。

```csharp
public static string Tr(string source, params object[] args)
```

#### 引数（Parameters）

`source` [string](https://learn.microsoft.com/dotnet/api/system.string)

`args` [object](https://learn.microsoft.com/dotnet/api/system.object)\[\]

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Localization_OmniL10n_TrContent_System_String_System_String_"></a> TrContent\(string, string\)

ラベルとツールチップの両方を翻訳したGUIContentを返します。

```csharp
public static GUIContent TrContent(string label, string tooltip = null)
```

#### 引数（Parameters）

`label` [string](https://learn.microsoft.com/dotnet/api/system.string)

`tooltip` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 GUIContent

### <a id="Omni_Localization_OmniL10n_TrCtx_System_String_System_String_"></a> TrCtx\(string, string\)

同じ英語原文でも文脈によって訳が異なる場合に使います(gettextのmsgctxtに相当)。

```csharp
public static string TrCtx(string context, string source)
```

#### 引数（Parameters）

`context` [string](https://learn.microsoft.com/dotnet/api/system.string)

`source` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Localization_OmniL10n_Changed"></a> Changed

```csharp
public static event Action Changed
```

#### 型（Event Type）

 [Action](https://learn.microsoft.com/dotnet/api/system.action)
