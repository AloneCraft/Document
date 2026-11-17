# <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceStateContract"></a> Class GalaxyAcceptanceStateContract

Namespace: [Omni.Editor.Diagnostics](Omni.Editor.Diagnostics.md)  
Assembly: Omni.Editor.dll  

受入ランナーとEditorコマンドが共有する純粋な契約判定です。

```csharp
public static class GalaxyAcceptanceStateContract
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[GalaxyAcceptanceStateContract](Omni.Editor.Diagnostics.GalaxyAcceptanceStateContract.md)

## フィールド（Fields）

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceStateContract_CurrentSchemaVersion"></a> CurrentSchemaVersion

```csharp
public const int CurrentSchemaVersion = 2
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceStateContract_ClassifyFailure_System_String_"></a> ClassifyFailure\(string\)

ランナーの例外・タイムアウト文字列を安定した分類へ写像します。
明示的な接頭辞を優先し、未知の失敗は製品へ誤分類せず基盤側へ倒します。

```csharp
public static GalaxyAcceptanceFailureClass ClassifyFailure(string failure)
```

#### 引数（Parameters）

`failure` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [GalaxyAcceptanceFailureClass](Omni.Editor.Diagnostics.GalaxyAcceptanceFailureClass.md)

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceStateContract_Deserialize_System_String_"></a> Deserialize\(string\)

```csharp
public static GalaxyAcceptanceEditorSnapshot Deserialize(string json)
```

#### 引数（Parameters）

`json` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [GalaxyAcceptanceEditorSnapshot](Omni.Editor.Diagnostics.GalaxyAcceptanceEditorSnapshot.md)

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceStateContract_Serialize_Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_"></a> Serialize\(GalaxyAcceptanceEditorSnapshot\)

```csharp
public static string Serialize(GalaxyAcceptanceEditorSnapshot snapshot)
```

#### 引数（Parameters）

`snapshot` [GalaxyAcceptanceEditorSnapshot](Omni.Editor.Diagnostics.GalaxyAcceptanceEditorSnapshot.md)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceStateContract_ToWireString_Omni_Editor_Diagnostics_GalaxyAcceptanceFailureClass_"></a> ToWireString\(GalaxyAcceptanceFailureClass\)

```csharp
public static string ToWireString(GalaxyAcceptanceFailureClass value)
```

#### 引数（Parameters）

`value` [GalaxyAcceptanceFailureClass](Omni.Editor.Diagnostics.GalaxyAcceptanceFailureClass.md)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceStateContract_TryParseWireString_System_String_Omni_Editor_Diagnostics_GalaxyAcceptanceFailureClass__"></a> TryParseWireString\(string, out GalaxyAcceptanceFailureClass\)

```csharp
public static bool TryParseWireString(string value, out GalaxyAcceptanceFailureClass result)
```

#### 引数（Parameters）

`value` [string](https://learn.microsoft.com/dotnet/api/system.string)

`result` [GalaxyAcceptanceFailureClass](Omni.Editor.Diagnostics.GalaxyAcceptanceFailureClass.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceStateContract_TryReadFile_System_String_Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot__System_String__"></a> TryReadFile\(string, out GalaxyAcceptanceEditorSnapshot, out string\)

```csharp
public static bool TryReadFile(string path, out GalaxyAcceptanceEditorSnapshot snapshot, out string reason)
```

#### 引数（Parameters）

`path` [string](https://learn.microsoft.com/dotnet/api/system.string)

`snapshot` [GalaxyAcceptanceEditorSnapshot](Omni.Editor.Diagnostics.GalaxyAcceptanceEditorSnapshot.md)

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_GalaxyAcceptanceStateContract_TryValidate_Omni_Editor_Diagnostics_GalaxyAcceptanceEditorSnapshot_Omni_Editor_Diagnostics_GalaxyAcceptanceFailureClass__System_String__"></a> TryValidate\(GalaxyAcceptanceEditorSnapshot, out GalaxyAcceptanceFailureClass, out string\)

実入力を開始できるEditor状態か検証します。
dirty/再生中/コンパイル中/更新中は、製品不具合と混同しないよう
専用セッション要求として停止します。

```csharp
public static bool TryValidate(GalaxyAcceptanceEditorSnapshot snapshot, out GalaxyAcceptanceFailureClass failureClass, out string reason)
```

#### 引数（Parameters）

`snapshot` [GalaxyAcceptanceEditorSnapshot](Omni.Editor.Diagnostics.GalaxyAcceptanceEditorSnapshot.md)

`failureClass` [GalaxyAcceptanceFailureClass](Omni.Editor.Diagnostics.GalaxyAcceptanceFailureClass.md)

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
