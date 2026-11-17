# <a id="Omni_Converter_Guarantees_OmniFingerprintEntry"></a> Struct OmniFingerprintEntry

Namespace: [Omni.Converter.Guarantees](Omni.Converter.Guarantees.md)  
Assembly: Omni.Converter.dll  

```csharp
public readonly struct OmniFingerprintEntry : IEquatable<OmniFingerprintEntry>
```

#### 実装するインターフェース（Implements）

[IEquatable<OmniFingerprintEntry\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1)

## コンストラクター（Constructors）

### <a id="Omni_Converter_Guarantees_OmniFingerprintEntry__ctor_Omni_Converter_Guarantees_OmniFingerprintEntryKind_System_String_System_String_"></a> OmniFingerprintEntry\(OmniFingerprintEntryKind, string, string\)

```csharp
public OmniFingerprintEntry(OmniFingerprintEntryKind kind, string key, string hash)
```

#### 引数（Parameters）

`kind` [OmniFingerprintEntryKind](Omni.Converter.Guarantees.OmniFingerprintEntryKind.md)

`key` [string](https://learn.microsoft.com/dotnet/api/system.string)

`hash` [string](https://learn.microsoft.com/dotnet/api/system.string)

## フィールド（Fields）

### <a id="Omni_Converter_Guarantees_OmniFingerprintEntry_Hash"></a> Hash

```csharp
public readonly string Hash
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniFingerprintEntry_Key"></a> Key

```csharp
public readonly string Key
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniFingerprintEntry_Kind"></a> Kind

```csharp
public readonly OmniFingerprintEntryKind Kind
```

#### 値（Field Value）

 [OmniFingerprintEntryKind](Omni.Converter.Guarantees.OmniFingerprintEntryKind.md)

## メソッド（Methods）

### <a id="Omni_Converter_Guarantees_OmniFingerprintEntry_Equals_Omni_Converter_Guarantees_OmniFingerprintEntry_"></a> Equals\(OmniFingerprintEntry\)

```csharp
public bool Equals(OmniFingerprintEntry other)
```

#### 引数（Parameters）

`other` [OmniFingerprintEntry](Omni.Converter.Guarantees.OmniFingerprintEntry.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_Guarantees_OmniFingerprintEntry_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object obj)
```

#### 引数（Parameters）

`obj` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_Guarantees_OmniFingerprintEntry_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)
