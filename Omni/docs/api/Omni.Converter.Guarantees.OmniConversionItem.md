# <a id="Omni_Converter_Guarantees_OmniConversionItem"></a> Class OmniConversionItem

Namespace: [Omni.Converter.Guarantees](Omni.Converter.Guarantees.md)  
Assembly: Omni.Converter.dll  

保証表の対象として分類した元です。<xref href="Omni.Converter.Guarantees.OmniConversionItem.Item" data-throw-if-not-resolved="false"></xref> は判定の鍵（元の資産パス）、<xref href="Omni.Converter.Guarantees.OmniConversionItem.RowItem" data-throw-if-not-resolved="false"></xref> は保証表の行の鍵です。
<xref href="Omni.Converter.Guarantees.OmniConversionItem.UnitSources" data-throw-if-not-resolved="false"></xref> は1回の変換で一緒に生成する元（TerrainLit は4本の閉包）です。

```csharp
public sealed class OmniConversionItem
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniConversionItem](Omni.Converter.Guarantees.OmniConversionItem.md)

## コンストラクター（Constructors）

### <a id="Omni_Converter_Guarantees_OmniConversionItem__ctor_System_String_System_String_Omni_Converter_Guarantees_OmniConversionFamily_System_Collections_Generic_IReadOnlyList_System_String__System_String_"></a> OmniConversionItem\(string, string, OmniConversionFamily, IReadOnlyList<string\>, string\)

```csharp
public OmniConversionItem(string item, string rowItem, OmniConversionFamily family, IReadOnlyList<string> unitSources, string knownSourceRuleId)
```

#### 引数（Parameters）

`item` [string](https://learn.microsoft.com/dotnet/api/system.string)

`rowItem` [string](https://learn.microsoft.com/dotnet/api/system.string)

`family` [OmniConversionFamily](Omni.Converter.Guarantees.OmniConversionFamily.md)

`unitSources` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

`knownSourceRuleId` [string](https://learn.microsoft.com/dotnet/api/system.string)

## プロパティ（Properties）

### <a id="Omni_Converter_Guarantees_OmniConversionItem_Family"></a> Family

```csharp
public OmniConversionFamily Family { get; }
```

#### 値（Property Value）

 [OmniConversionFamily](Omni.Converter.Guarantees.OmniConversionFamily.md)

### <a id="Omni_Converter_Guarantees_OmniConversionItem_Item"></a> Item

```csharp
public string Item { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniConversionItem_KnownSourceRuleId"></a> KnownSourceRuleId

```csharp
public string KnownSourceRuleId { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniConversionItem_RowItem"></a> RowItem

```csharp
public string RowItem { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniConversionItem_UnitSources"></a> UnitSources

```csharp
public IReadOnlyList<string> UnitSources { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>
