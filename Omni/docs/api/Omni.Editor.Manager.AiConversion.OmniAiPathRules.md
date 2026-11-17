# <a id="Omni_Editor_Manager_AiConversion_OmniAiPathRules"></a> Class OmniAiPathRules

Namespace: [Omni.Editor.Manager.AiConversion](Omni.Editor.Manager.AiConversion.md)  
Assembly: Omni.Manager.dll  

AI が返す・Manager が扱うプロジェクト相対パスの規則です。

```csharp
public static class OmniAiPathRules
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniAiPathRules](Omni.Editor.Manager.AiConversion.OmniAiPathRules.md)

## フィールド（Fields）

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPathRules_AllowedNewFileExtensions"></a> AllowedNewFileExtensions

新しいファイルとして許す拡張子（対象と同じフォルダ）。

```csharp
public static readonly string[] AllowedNewFileExtensions
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)\[\]

## メソッド（Methods）

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPathRules_AreSame_System_String_System_String_"></a> AreSame\(string, string\)

```csharp
public static bool AreSame(string a, string b)
```

#### 引数（Parameters）

`a` [string](https://learn.microsoft.com/dotnet/api/system.string)

`b` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPathRules_DirectoryOf_System_String_"></a> DirectoryOf\(string\)

```csharp
public static string DirectoryOf(string normalizedPath)
```

#### 引数（Parameters）

`normalizedPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPathRules_IsNewFileNextToSource_System_String_System_String_"></a> IsNewFileNextToSource\(string, string\)

対象 Shader と同じフォルダにある、許可した拡張子の新しいファイルか（対象の下位フォルダや親フォルダは不可）。
既存か新規かは見ない（許可の範囲の判定だけ）。.meta は不可。

```csharp
public static bool IsNewFileNextToSource(string path, string source)
```

#### 引数（Parameters）

`path` [string](https://learn.microsoft.com/dotnet/api/system.string)

`source` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPathRules_IsSafeProjectRelative_System_String_System_String__"></a> IsSafeProjectRelative\(string, out string\)

プロジェクト相対パスとして安全か。空、絶対パス（/ 始まり、ドライブ名、UNC）、バックスラッシュ、<code>..</code>、
制御文字を含むものは拒否します。

```csharp
public static bool IsSafeProjectRelative(string path, out string problem)
```

#### 引数（Parameters）

`path` [string](https://learn.microsoft.com/dotnet/api/system.string)

`problem` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiPathRules_Normalize_System_String_"></a> Normalize\(string\)

区切りを / にそろえ、先頭の ./ を外します。

```csharp
public static string Normalize(string path)
```

#### 引数（Parameters）

`path` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
