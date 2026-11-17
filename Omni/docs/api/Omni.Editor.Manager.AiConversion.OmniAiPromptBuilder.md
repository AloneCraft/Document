# <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptBuilder"></a> Class OmniAiPromptBuilder

Namespace: [Omni.Editor.Manager.AiConversion](Omni.Editor.Manager.AiConversion.md)  
Assembly: Omni.Manager.dll  

AI 変換依頼のプロンプトを組み立てます。単一の正本は <code>Documentation/CustomShaderAiPrompt.md</code>（<xref href="Omni.Editor.Manager.AiConversion.OmniAiPromptSource" data-throw-if-not-resolved="false"></xref>）で、
「守る規則」「状況別の振り分け」「してはいけないこと」「出力の形式」と結果 JSON の節はそこから取ります。
「対象」「今回の状況」「Omni が機械判定する条件」「ヒント」とファイル本文は、依頼ごとにここで組み立てます（日本語のみ）。

```csharp
public static class OmniAiPromptBuilder
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniAiPromptBuilder](Omni.Editor.Manager.AiConversion.OmniAiPromptBuilder.md)

## フィールド（Fields）

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptBuilder_ChatSizeWarningBytes"></a> ChatSizeWarningBytes

チャット用に埋め込む本文の合計がこれを超えたら警告する（バイト）。

```csharp
public const int ChatSizeWarningBytes = 204800
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptBuilder_BuildAgent_Omni_Editor_Manager_AiConversion_OmniAiPromptRequest_"></a> BuildAgent\(OmniAiPromptRequest\)

```csharp
public static OmniAiPrompt BuildAgent(OmniAiPromptRequest request)
```

#### 引数（Parameters）

`request` [OmniAiPromptRequest](Omni.Editor.Manager.AiConversion.OmniAiPromptRequest.md)

#### 戻り値（Returns）

 [OmniAiPrompt](Omni.Editor.Manager.AiConversion.OmniAiPrompt.md)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptBuilder_BuildAgent_Omni_Editor_Manager_AiConversion_OmniAiPromptRequest_Omni_Editor_Manager_AiConversion_OmniAiPromptSource_"></a> BuildAgent\(OmniAiPromptRequest, OmniAiPromptSource\)

```csharp
public static OmniAiPrompt BuildAgent(OmniAiPromptRequest request, OmniAiPromptSource source)
```

#### 引数（Parameters）

`request` [OmniAiPromptRequest](Omni.Editor.Manager.AiConversion.OmniAiPromptRequest.md)

`source` [OmniAiPromptSource](Omni.Editor.Manager.AiConversion.OmniAiPromptSource.md)

#### 戻り値（Returns）

 [OmniAiPrompt](Omni.Editor.Manager.AiConversion.OmniAiPrompt.md)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptBuilder_BuildChat_Omni_Editor_Manager_AiConversion_OmniAiPromptRequest_"></a> BuildChat\(OmniAiPromptRequest\)

```csharp
public static OmniAiPrompt BuildChat(OmniAiPromptRequest request)
```

#### 引数（Parameters）

`request` [OmniAiPromptRequest](Omni.Editor.Manager.AiConversion.OmniAiPromptRequest.md)

#### 戻り値（Returns）

 [OmniAiPrompt](Omni.Editor.Manager.AiConversion.OmniAiPrompt.md)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptBuilder_BuildChat_Omni_Editor_Manager_AiConversion_OmniAiPromptRequest_Omni_Editor_Manager_AiConversion_OmniAiPromptSource_"></a> BuildChat\(OmniAiPromptRequest, OmniAiPromptSource\)

```csharp
public static OmniAiPrompt BuildChat(OmniAiPromptRequest request, OmniAiPromptSource source)
```

#### 引数（Parameters）

`request` [OmniAiPromptRequest](Omni.Editor.Manager.AiConversion.OmniAiPromptRequest.md)

`source` [OmniAiPromptSource](Omni.Editor.Manager.AiConversion.OmniAiPromptSource.md)

#### 戻り値（Returns）

 [OmniAiPrompt](Omni.Editor.Manager.AiConversion.OmniAiPrompt.md)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptBuilder_BuildHints_System_Boolean_"></a> BuildHints\(bool\)

「ヒント」の節の本文（見出しを除く）。変換器の定義から生成するので、定義が変われば自動で変わります。

```csharp
public static string BuildHints(bool isGraph)
```

#### 引数（Parameters）

`isGraph` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptBuilder_BuildMachineConditions_System_Boolean_"></a> BuildMachineConditions\(bool\)

「Omni が機械判定する条件」の節の本文（見出しを除く）。

```csharp
public static string BuildMachineConditions(bool isGraph)
```

#### 引数（Parameters）

`isGraph` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptBuilder_DetectVersions_System_String__System_String__"></a> DetectVersions\(out string, out string\)

Unity と URP の版を取ります（取れなければ空）。

```csharp
public static void DetectVersions(out string unityVersion, out string urpVersion)
```

#### 引数（Parameters）

`unityVersion` [string](https://learn.microsoft.com/dotnet/api/system.string)

`urpVersion` [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptBuilder_FindPersonalMarkers_System_String_"></a> FindPersonalMarkers\(string\)

個人のパスや利用者名らしき文字列を探します（ドライブ名つきの絶対パス、Users／home 配下、実行中の利用者名）。

```csharp
public static IReadOnlyList<string> FindPersonalMarkers(string text)
```

#### 引数（Parameters）

`text` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPromptBuilder_IsAiVisible_System_String_"></a> IsAiVisible\(string\)

AI に見せてよいパスか。プロジェクト相対の <code>Assets/</code> と <code>Packages/</code> のうち、埋め込み／ローカル package 以外の Packages、
Omni 本体（<xref href="Omni.OmniProductPaths.IsUnder(System.String%2cSystem.String)" data-throw-if-not-resolved="false"></xref>）、<code>Assets/Radial</code>（生成物）、.meta を除きます。

```csharp
public static bool IsAiVisible(string path)
```

#### 引数（Parameters）

`path` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
