# <a id="Omni_VersionedConversion_ConverterCandidate"></a> Class ConverterCandidate

Namespace: [Omni.VersionedConversion](Omni.VersionedConversion.md)  
Assembly: Omni.VersionedConversion.dll  

特定の Editor と依存実体に対して検証された変換器の候補です。

```csharp
public sealed class ConverterCandidate
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[ConverterCandidate](Omni.VersionedConversion.ConverterCandidate.md)

## コンストラクター（Constructors）

### <a id="Omni_VersionedConversion_ConverterCandidate__ctor_System_String_System_String_System_String_System_String_System_Boolean_System_Collections_Generic_IEnumerable_Omni_VersionedConversion_PackageIdentity__"></a> ConverterCandidate\(string, string, string, string, bool, IEnumerable<PackageIdentity\>\)

```csharp
public ConverterCandidate(string id, string editorVersion, string editorRevision, string folderName, bool qualified, IEnumerable<PackageIdentity> packages)
```

#### 引数（Parameters）

`id` [string](https://learn.microsoft.com/dotnet/api/system.string)

`editorVersion` [string](https://learn.microsoft.com/dotnet/api/system.string)

`editorRevision` [string](https://learn.microsoft.com/dotnet/api/system.string)

`folderName` [string](https://learn.microsoft.com/dotnet/api/system.string)

`qualified` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`packages` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<[PackageIdentity](Omni.VersionedConversion.PackageIdentity.md)\>

## プロパティ（Properties）

### <a id="Omni_VersionedConversion_ConverterCandidate_EditorRevision"></a> EditorRevision

```csharp
public string EditorRevision { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_VersionedConversion_ConverterCandidate_EditorVersion"></a> EditorVersion

```csharp
public string EditorVersion { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_VersionedConversion_ConverterCandidate_FolderName"></a> FolderName

```csharp
public string FolderName { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_VersionedConversion_ConverterCandidate_Id"></a> Id

```csharp
public string Id { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_VersionedConversion_ConverterCandidate_Packages"></a> Packages

```csharp
public IReadOnlyList<PackageIdentity> Packages { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[PackageIdentity](Omni.VersionedConversion.PackageIdentity.md)\>

### <a id="Omni_VersionedConversion_ConverterCandidate_Qualified"></a> Qualified

```csharp
public bool Qualified { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
