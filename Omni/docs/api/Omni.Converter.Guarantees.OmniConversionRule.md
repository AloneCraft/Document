# <a id="Omni_Converter_Guarantees_OmniConversionRule"></a> Class OmniConversionRule

Namespace: [Omni.Converter.Guarantees](Omni.Converter.Guarantees.md)  
Assembly: Omni.Converter.dll  

版つきの変換規約です。公開した規約は凍結し、書き換えません（不具合は改訂した規約を足して直します）。

```csharp
public sealed class OmniConversionRule
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniConversionRule](Omni.Converter.Guarantees.OmniConversionRule.md)

## コンストラクター（Constructors）

### <a id="Omni_Converter_Guarantees_OmniConversionRule__ctor_System_String_Omni_Converter_Guarantees_OmniConversionFamily_System_String_System_String_System_String_System_Boolean_System_String_System_String_System_Collections_Generic_IReadOnlyList_System_String__System_Collections_Generic_IReadOnlyDictionary_System_String_System_String__"></a> OmniConversionRule\(string, OmniConversionFamily, string, string, string, bool, string, string, IReadOnlyList<string\>, IReadOnlyDictionary<string, string\>\)

```csharp
public OmniConversionRule(string id, OmniConversionFamily family, string packageName, string minVersion, string maxVersionExclusive, bool retired, string outputFormat, string templateSetId, IReadOnlyList<string> anchors, IReadOnlyDictionary<string, string> knownSources)
```

#### 引数（Parameters）

`id` [string](https://learn.microsoft.com/dotnet/api/system.string)

`family` [OmniConversionFamily](Omni.Converter.Guarantees.OmniConversionFamily.md)

`packageName` [string](https://learn.microsoft.com/dotnet/api/system.string)

`minVersion` [string](https://learn.microsoft.com/dotnet/api/system.string)

`maxVersionExclusive` [string](https://learn.microsoft.com/dotnet/api/system.string)

`retired` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`outputFormat` [string](https://learn.microsoft.com/dotnet/api/system.string)

`templateSetId` [string](https://learn.microsoft.com/dotnet/api/system.string)

`anchors` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

`knownSources` [IReadOnlyDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlydictionary\-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [string](https://learn.microsoft.com/dotnet/api/system.string)\>

## プロパティ（Properties）

### <a id="Omni_Converter_Guarantees_OmniConversionRule_Anchors"></a> Anchors

```csharp
public IReadOnlyList<string> Anchors { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Converter_Guarantees_OmniConversionRule_Family"></a> Family

```csharp
public OmniConversionFamily Family { get; }
```

#### 値（Property Value）

 [OmniConversionFamily](Omni.Converter.Guarantees.OmniConversionFamily.md)

### <a id="Omni_Converter_Guarantees_OmniConversionRule_Id"></a> Id

```csharp
public string Id { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniConversionRule_KnownSources"></a> KnownSources

```csharp
public IReadOnlyDictionary<string, string> KnownSources { get; }
```

#### 値（Property Value）

 [IReadOnlyDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlydictionary\-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Converter_Guarantees_OmniConversionRule_MaxVersionExclusive"></a> MaxVersionExclusive

```csharp
public string MaxVersionExclusive { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniConversionRule_MinVersion"></a> MinVersion

```csharp
public string MinVersion { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniConversionRule_OutputFormat"></a> OutputFormat

```csharp
public string OutputFormat { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniConversionRule_PackageName"></a> PackageName

```csharp
public string PackageName { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniConversionRule_Retired"></a> Retired

```csharp
public bool Retired { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_Guarantees_OmniConversionRule_TemplateSetId"></a> TemplateSetId

```csharp
public string TemplateSetId { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
