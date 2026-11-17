# <a id="Omni_Editor_Manager_AiConversion_OmniAiPrompt"></a> Class OmniAiPrompt

Namespace: [Omni.Editor.Manager.AiConversion](Omni.Editor.Manager.AiConversion.md)  
Assembly: Omni.Manager.dll  

組み立てたプロンプトと、コピー前に利用者へ見せる情報です。

```csharp
public sealed class OmniAiPrompt
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniAiPrompt](Omni.Editor.Manager.AiConversion.OmniAiPrompt.md)

## フィールド（Fields）

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPrompt_ContentBytes"></a> ContentBytes

チャット用: 入れたファイル本文の合計（UTF-8 のバイト数）。

```csharp
public long ContentBytes
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPrompt_Error"></a> Error

失敗の理由（<xref href="Omni.Editor.Manager.AiConversion.OmniAiPrompt.Success" data-throw-if-not-resolved="false"></xref> が false のとき。ローカライズ済み）。

```csharp
public string Error
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPrompt_ExcludedFiles"></a> ExcludedFiles

AI に見せてはいけない場所のため、除いたファイル（Packages の非埋め込み、Omni 本体、Assets/Radial など）。

```csharp
public readonly List<string> ExcludedFiles
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPrompt_IncludedFiles"></a> IncludedFiles

プロンプトに入れた（エージェント用では「変更してよい」と示した）ファイル。順序は対象が先頭。

```csharp
public readonly List<string> IncludedFiles
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPrompt_Success"></a> Success

```csharp
public bool Success
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPrompt_Text"></a> Text

```csharp
public string Text
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPrompt_Warnings"></a> Warnings

コピー前に利用者へ見せる注意（大きさ、個人情報らしき文字列など）。

```csharp
public readonly List<string> Warnings
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

## プロパティ（Properties）

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPrompt_EditableFiles"></a> EditableFiles

結果 JSON の modifiedFiles に許す範囲（<xref href="Omni.Editor.Manager.AiConversion.OmniAiPrompt.IncludedFiles" data-throw-if-not-resolved="false"></xref> と同じ）。

```csharp
public IReadOnlyList<string> EditableFiles { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>
