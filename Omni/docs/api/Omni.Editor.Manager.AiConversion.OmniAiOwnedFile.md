# <a id="Omni_Editor_Manager_AiConversion_OmniAiOwnedFile"></a> Class OmniAiOwnedFile

Namespace: [Omni.Editor.Manager.AiConversion](Omni.Editor.Manager.AiConversion.md)  
Assembly: Omni.Manager.dll  

プロンプトに入れる自作 Shader の 1 ファイル。チャット用は本文（<xref href="Omni.Editor.Manager.AiConversion.OmniAiOwnedFile.Content" data-throw-if-not-resolved="false"></xref>）が要り、エージェント用はパスだけを使います。

```csharp
public sealed class OmniAiOwnedFile
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniAiOwnedFile](Omni.Editor.Manager.AiConversion.OmniAiOwnedFile.md)

## コンストラクター（Constructors）

### <a id="Omni_Editor_Manager_AiConversion_OmniAiOwnedFile__ctor_System_String_System_String_"></a> OmniAiOwnedFile\(string, string\)

```csharp
public OmniAiOwnedFile(string path, string content = null)
```

#### 引数（Parameters）

`path` [string](https://learn.microsoft.com/dotnet/api/system.string)

`content` [string](https://learn.microsoft.com/dotnet/api/system.string)

## プロパティ（Properties）

### <a id="Omni_Editor_Manager_AiConversion_OmniAiOwnedFile_Content"></a> Content

```csharp
public string Content { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiOwnedFile_Path"></a> Path

プロジェクト相対パス（/ 区切り）。

```csharp
public string Path { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
