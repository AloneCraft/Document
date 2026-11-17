# <a id="Omni_Converter_Guarantees_OmniConversionGuaranteeTable"></a> Class OmniConversionGuaranteeTable

Namespace: [Omni.Converter.Guarantees](Omni.Converter.Guarantees.md)  
Assembly: Omni.Converter.dll  

変換保証表（<code>OmniConversionGuarantees.json</code>）です。検証した Unity と元・出力・約束の版の指紋の組を行に持ちます。
本体の根からの相対パスで持ち、File IO で読みます（Resources には置きません）。表が1か所でも壊れていれば全体を使わず、
どの項目も保証済みにしません（Fail Closed）。

```csharp
public sealed class OmniConversionGuaranteeTable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniConversionGuaranteeTable](Omni.Converter.Guarantees.OmniConversionGuaranteeTable.md)

## フィールド（Fields）

### <a id="Omni_Converter_Guarantees_OmniConversionGuaranteeTable_RelativePath"></a> RelativePath

```csharp
public const string RelativePath = "Converter/Guarantees/OmniConversionGuarantees.json"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniConversionGuaranteeTable_Schema"></a> Schema

```csharp
public const string Schema = "omni-conversion-guarantees/1"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## プロパティ（Properties）

### <a id="Omni_Converter_Guarantees_OmniConversionGuaranteeTable_Error"></a> Error

無効な理由です。有効なら null です。

```csharp
public string Error { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniConversionGuaranteeTable_Exclusions"></a> Exclusions

```csharp
public IReadOnlyList<OmniConversionGuaranteeTable.Exclusion> Exclusions { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[OmniConversionGuaranteeTable](Omni.Converter.Guarantees.OmniConversionGuaranteeTable.md).[Exclusion](Omni.Converter.Guarantees.OmniConversionGuaranteeTable.Exclusion.md)\>

### <a id="Omni_Converter_Guarantees_OmniConversionGuaranteeTable_Files"></a> Files

```csharp
public IReadOnlyList<OmniConversionGuaranteeTable.FileEntry> Files { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[OmniConversionGuaranteeTable](Omni.Converter.Guarantees.OmniConversionGuaranteeTable.md).[FileEntry](Omni.Converter.Guarantees.OmniConversionGuaranteeTable.FileEntry.md)\>

### <a id="Omni_Converter_Guarantees_OmniConversionGuaranteeTable_IsValid"></a> IsValid

```csharp
public bool IsValid { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_Guarantees_OmniConversionGuaranteeTable_Rows"></a> Rows

```csharp
public IReadOnlyList<OmniConversionGuaranteeTable.Row> Rows { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[OmniConversionGuaranteeTable](Omni.Converter.Guarantees.OmniConversionGuaranteeTable.md).[Row](Omni.Converter.Guarantees.OmniConversionGuaranteeTable.Row.md)\>

## メソッド（Methods）

### <a id="Omni_Converter_Guarantees_OmniConversionGuaranteeTable_FilesFor_Omni_Converter_Guarantees_OmniConversionFamily_"></a> FilesFor\(OmniConversionFamily\)

系統の「違うファイル」の比較に使う、鍵 → 指紋です。

```csharp
public IReadOnlyDictionary<string, string> FilesFor(OmniConversionFamily f)
```

#### 引数（Parameters）

`f` [OmniConversionFamily](Omni.Converter.Guarantees.OmniConversionFamily.md)

#### 戻り値（Returns）

 [IReadOnlyDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlydictionary\-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Converter_Guarantees_OmniConversionGuaranteeTable_HasRowIgnoringContract_Omni_Converter_Guarantees_OmniConversionFamily_System_String_System_String_System_String_"></a> HasRowIgnoringContract\(OmniConversionFamily, string, string, string\)

```csharp
public bool HasRowIgnoringContract(OmniConversionFamily f, string item, string rule, string source)
```

#### 引数（Parameters）

`f` [OmniConversionFamily](Omni.Converter.Guarantees.OmniConversionFamily.md)

`item` [string](https://learn.microsoft.com/dotnet/api/system.string)

`rule` [string](https://learn.microsoft.com/dotnet/api/system.string)

`source` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_Guarantees_OmniConversionGuaranteeTable_LoadShipped"></a> LoadShipped\(\)

同梱の表を読みます。ファイルの（長さ, 更新時刻）と登録済みの規約が前回と同じなら、前回の結果を返します。
読めない・壊れているときも null にせず、無効な表を返します。

```csharp
public static OmniConversionGuaranteeTable LoadShipped()
```

#### 戻り値（Returns）

 [OmniConversionGuaranteeTable](Omni.Converter.Guarantees.OmniConversionGuaranteeTable.md)

### <a id="Omni_Converter_Guarantees_OmniConversionGuaranteeTable_TryFindRow_Omni_Converter_Guarantees_OmniConversionFamily_System_String_System_String_System_String_System_String_Omni_Converter_Guarantees_OmniConversionGuaranteeTable_Row__"></a> TryFindRow\(OmniConversionFamily, string, string, string, string, out Row\)

```csharp
public bool TryFindRow(OmniConversionFamily f, string item, string rule, string contract, string source, out OmniConversionGuaranteeTable.Row row)
```

#### 引数（Parameters）

`f` [OmniConversionFamily](Omni.Converter.Guarantees.OmniConversionFamily.md)

`item` [string](https://learn.microsoft.com/dotnet/api/system.string)

`rule` [string](https://learn.microsoft.com/dotnet/api/system.string)

`contract` [string](https://learn.microsoft.com/dotnet/api/system.string)

`source` [string](https://learn.microsoft.com/dotnet/api/system.string)

`row` [OmniConversionGuaranteeTable](Omni.Converter.Guarantees.OmniConversionGuaranteeTable.md).[Row](Omni.Converter.Guarantees.OmniConversionGuaranteeTable.Row.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_Guarantees_OmniConversionGuaranteeTable_TryGetExclusion_Omni_Converter_Guarantees_OmniConversionFamily_System_String_System_String_System_String__"></a> TryGetExclusion\(OmniConversionFamily, string, string, out string\)

```csharp
public bool TryGetExclusion(OmniConversionFamily f, string item, string rule, out string reason)
```

#### 引数（Parameters）

`f` [OmniConversionFamily](Omni.Converter.Guarantees.OmniConversionFamily.md)

`item` [string](https://learn.microsoft.com/dotnet/api/system.string)

`rule` [string](https://learn.microsoft.com/dotnet/api/system.string)

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_Guarantees_OmniConversionGuaranteeTable_VerifiedUnityFor_Omni_Converter_Guarantees_OmniConversionFamily_"></a> VerifiedUnityFor\(OmniConversionFamily\)

系統の行が検証された Unity の版です。行が無ければ null、版が複数あれば Ordinal 順に「, 」でつなぎます。

```csharp
public string VerifiedUnityFor(OmniConversionFamily f)
```

#### 引数（Parameters）

`f` [OmniConversionFamily](Omni.Converter.Guarantees.OmniConversionFamily.md)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
