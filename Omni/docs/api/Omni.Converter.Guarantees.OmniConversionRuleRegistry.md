# <a id="Omni_Converter_Guarantees_OmniConversionRuleRegistry"></a> Class OmniConversionRuleRegistry

Namespace: [Omni.Converter.Guarantees](Omni.Converter.Guarantees.md)  
Assembly: Omni.Converter.dll  

系統ごとの変換規約の一覧と、元の分類、規約の選び方です。

<p>
規約はコードのデータとして凍結します（保証表が壊れていても、扱える元の範囲と TMP の原本の見分け方が変わらないように）。
範囲より新しい版は一番新しい規約で変換し、良くても「検査のみ合格」にします（決定15）。全ての範囲より古い版、
または引退した規約しか合わない元は「変換不能」です。
</p>

```csharp
public static class OmniConversionRuleRegistry
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniConversionRuleRegistry](Omni.Converter.Guarantees.OmniConversionRuleRegistry.md)

## フィールド（Fields）

### <a id="Omni_Converter_Guarantees_OmniConversionRuleRegistry_GraphRuleId"></a> GraphRuleId

```csharp
public const string GraphRuleId = "UrpGraph.17_6"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniConversionRuleRegistry_TmpRuleId"></a> TmpRuleId

```csharp
public const string TmpRuleId = "Tmp.Ugui2_6"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniConversionRuleRegistry_UrpRuleId"></a> UrpRuleId

```csharp
public const string UrpRuleId = "Urp.17_6"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniConversionRuleRegistry_VfxRowItem"></a> VfxRowItem

```csharp
public const string VfxRowItem = "vfx-templates"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniConversionRuleRegistry_VfxRuleId"></a> VfxRuleId

```csharp
public const string VfxRuleId = "Vfx.17_6"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## プロパティ（Properties）

### <a id="Omni_Converter_Guarantees_OmniConversionRuleRegistry_All"></a> All

```csharp
public static IReadOnlyList<OmniConversionRule> All { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[OmniConversionRule](Omni.Converter.Guarantees.OmniConversionRule.md)\>

## メソッド（Methods）

### <a id="Omni_Converter_Guarantees_OmniConversionRuleRegistry_ForVfxAsset_System_String_"></a> ForVfxAsset\(string\)

```csharp
public static OmniConversionItem ForVfxAsset(string vfxAssetPath)
```

#### 引数（Parameters）

`vfxAssetPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [OmniConversionItem](Omni.Converter.Guarantees.OmniConversionItem.md)

### <a id="Omni_Converter_Guarantees_OmniConversionRuleRegistry_Select_Omni_Converter_Guarantees_OmniConversionItem_"></a> Select\(OmniConversionItem\)

```csharp
public static OmniRuleSelection Select(OmniConversionItem item)
```

#### 引数（Parameters）

`item` [OmniConversionItem](Omni.Converter.Guarantees.OmniConversionItem.md)

#### 戻り値（Returns）

 [OmniRuleSelection](Omni.Converter.Guarantees.OmniRuleSelection.md)

### <a id="Omni_Converter_Guarantees_OmniConversionRuleRegistry_TryClassify_System_String_Omni_Converter_Guarantees_OmniConversionItem__"></a> TryClassify\(string, out OmniConversionItem\)

元の資産パスを、保証表の対象（標準 URP の 17 本と SSAO、Graph 5 本と Decal、TMP の原本）に分類します。
分類できない元は利用者の自作 Shader で、保証の段も警告もありません。

```csharp
public static bool TryClassify(string sourcePath, out OmniConversionItem item)
```

#### 引数（Parameters）

`sourcePath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`item` [OmniConversionItem](Omni.Converter.Guarantees.OmniConversionItem.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_Guarantees_OmniConversionRuleRegistry_TryGet_System_String_Omni_Converter_Guarantees_OmniConversionRule__"></a> TryGet\(string, out OmniConversionRule\)

```csharp
public static bool TryGet(string id, out OmniConversionRule rule)
```

#### 引数（Parameters）

`id` [string](https://learn.microsoft.com/dotnet/api/system.string)

`rule` [OmniConversionRule](Omni.Converter.Guarantees.OmniConversionRule.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
