# <a id="Omni_VersionedConversion_PackageIdentity"></a> Class PackageIdentity

Namespace: [Omni.VersionedConversion](Omni.VersionedConversion.md)  
Assembly: Omni.VersionedConversion.dll  

変換器を選ぶための、パッケージの版と解決済み内容の識別情報です。

```csharp
public sealed class PackageIdentity
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PackageIdentity](Omni.VersionedConversion.PackageIdentity.md)

## コンストラクター（Constructors）

### <a id="Omni_VersionedConversion_PackageIdentity__ctor_System_String_System_String_System_String_"></a> PackageIdentity\(string, string, string\)

```csharp
public PackageIdentity(string name, string version, string contentSha256)
```

#### 引数（Parameters）

`name` [string](https://learn.microsoft.com/dotnet/api/system.string)

`version` [string](https://learn.microsoft.com/dotnet/api/system.string)

`contentSha256` [string](https://learn.microsoft.com/dotnet/api/system.string)

## プロパティ（Properties）

### <a id="Omni_VersionedConversion_PackageIdentity_ContentSha256"></a> ContentSha256

```csharp
public string ContentSha256 { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_VersionedConversion_PackageIdentity_Name"></a> Name

```csharp
public string Name { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_VersionedConversion_PackageIdentity_Version"></a> Version

```csharp
public string Version { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
