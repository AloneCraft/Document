# <a id="Omni_Converter_Guarantees_OmniFingerprint"></a> Class OmniFingerprint

Namespace: [Omni.Converter.Guarantees](Omni.Converter.Guarantees.md)  
Assembly: Omni.Converter.dll  

行の集合から作る指紋です。行は重複を除いて (種類, 鍵) の Ordinal 順に並べるので、集めた順序に依りません。
文化依存の比較や <xref href="System.Environment.NewLine" data-throw-if-not-resolved="false"></xref> を使わないのは、同じ入力が機械によらず同じ値になるためです。

```csharp
public sealed class OmniFingerprint
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniFingerprint](Omni.Converter.Guarantees.OmniFingerprint.md)

## プロパティ（Properties）

### <a id="Omni_Converter_Guarantees_OmniFingerprint_Entries"></a> Entries

```csharp
public IReadOnlyList<OmniFingerprintEntry> Entries { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[OmniFingerprintEntry](Omni.Converter.Guarantees.OmniFingerprintEntry.md)\>

### <a id="Omni_Converter_Guarantees_OmniFingerprint_Kind"></a> Kind

```csharp
public string Kind { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniFingerprint_Role"></a> Role

```csharp
public string Role { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniFingerprint_Value"></a> Value

```csharp
public string Value { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Converter_Guarantees_OmniFingerprint_TryCompose_System_String_System_String_System_Collections_Generic_IEnumerable_Omni_Converter_Guarantees_OmniFingerprintEntry__Omni_Converter_Guarantees_OmniFingerprint__System_String__"></a> TryCompose\(string, string, IEnumerable<OmniFingerprintEntry\>, out OmniFingerprint, out string\)

```csharp
public static bool TryCompose(string role, string kind, IEnumerable<OmniFingerprintEntry> entries, out OmniFingerprint fingerprint, out string error)
```

#### 引数（Parameters）

`role` [string](https://learn.microsoft.com/dotnet/api/system.string)

`kind` [string](https://learn.microsoft.com/dotnet/api/system.string)

`entries` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<[OmniFingerprintEntry](Omni.Converter.Guarantees.OmniFingerprintEntry.md)\>

`fingerprint` [OmniFingerprint](Omni.Converter.Guarantees.OmniFingerprint.md)

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
