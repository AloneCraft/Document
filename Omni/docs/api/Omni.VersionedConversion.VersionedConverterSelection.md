# <a id="Omni_VersionedConversion_VersionedConverterSelection"></a> Class VersionedConverterSelection

Namespace: [Omni.VersionedConversion](Omni.VersionedConversion.md)  
Assembly: Omni.VersionedConversion.dll  

完全に一致する検証済み候補が一つだけの場合に選択します。

```csharp
public static class VersionedConverterSelection
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VersionedConverterSelection](Omni.VersionedConversion.VersionedConverterSelection.md)

## メソッド（Methods）

### <a id="Omni_VersionedConversion_VersionedConverterSelection_TryGetEditorRevision_System_String_System_String_System_String__"></a> TryGetEditorRevision\(string, string, out string\)

Editor の完全版表示から revision を取り出し、版番号も一致させます。

```csharp
public static bool TryGetEditorRevision(string editorVersion, string fullEditorVersion, out string revision)
```

#### 引数（Parameters）

`editorVersion` [string](https://learn.microsoft.com/dotnet/api/system.string)

`fullEditorVersion` [string](https://learn.microsoft.com/dotnet/api/system.string)

`revision` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_VersionedConversion_VersionedConverterSelection_TryGetFolderName_System_String_System_String__"></a> TryGetFolderName\(string, out string\)

例: 6000.6.6f1 を 6.6.6f1 へ変換します。

```csharp
public static bool TryGetFolderName(string editorVersion, out string folderName)
```

#### 引数（Parameters）

`editorVersion` [string](https://learn.microsoft.com/dotnet/api/system.string)

`folderName` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_VersionedConversion_VersionedConverterSelection_TrySelect_System_Collections_Generic_IEnumerable_Omni_VersionedConversion_ConverterCandidate__System_String_System_String_System_Collections_Generic_IEnumerable_Omni_VersionedConversion_PackageIdentity__System_String_Omni_VersionedConversion_ConverterCandidate__System_String__"></a> TrySelect\(IEnumerable<ConverterCandidate\>, string, string, IEnumerable<PackageIdentity\>, string, out ConverterCandidate, out string\)

手動指定がある場合も、同じ Editor と全依存の検査を行います。

```csharp
public static bool TrySelect(IEnumerable<ConverterCandidate> candidates, string editorVersion, string editorRevision, IEnumerable<PackageIdentity> installedPackages, string requestedId, out ConverterCandidate selected, out string reason)
```

#### 引数（Parameters）

`candidates` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<[ConverterCandidate](Omni.VersionedConversion.ConverterCandidate.md)\>

`editorVersion` [string](https://learn.microsoft.com/dotnet/api/system.string)

`editorRevision` [string](https://learn.microsoft.com/dotnet/api/system.string)

`installedPackages` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<[PackageIdentity](Omni.VersionedConversion.PackageIdentity.md)\>

`requestedId` [string](https://learn.microsoft.com/dotnet/api/system.string)

`selected` [ConverterCandidate](Omni.VersionedConversion.ConverterCandidate.md)

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
