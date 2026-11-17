# <a id="Omni_VersionedConversion_VersionedConverterCatalog_1"></a> Class VersionedConverterCatalog<T\>

Namespace: [Omni.VersionedConversion](Omni.VersionedConversion.md)  
Assembly: Omni.VersionedConversion.dll  

版別実装を登録し、適合するものが一つだけの場合に取得します。

```csharp
public sealed class VersionedConverterCatalog<T> where T : class
```

#### 型引数（Type Parameters）

`T` 

版別実装が共通入口へ提供する契約。

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VersionedConverterCatalog<T\>](Omni.VersionedConversion.VersionedConverterCatalog\-1.md)

## メソッド（Methods）

### <a id="Omni_VersionedConversion_VersionedConverterCatalog_1_Register_Omni_VersionedConversion_ConverterCandidate__0_"></a> Register\(ConverterCandidate, T\)

登録の寿命は返されたハンドルが所有し、重複登録は選択時に拒否します。

```csharp
public IDisposable Register(ConverterCandidate candidate, T converter)
```

#### 引数（Parameters）

`candidate` [ConverterCandidate](Omni.VersionedConversion.ConverterCandidate.md)

`converter` T

#### 戻り値（Returns）

 [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

### <a id="Omni_VersionedConversion_VersionedConverterCatalog_1_TryResolve_System_String_System_String_System_Collections_Generic_IEnumerable_Omni_VersionedConversion_PackageIdentity__System_String__0__System_String__"></a> TryResolve\(string, string, IEnumerable<PackageIdentity\>, string, out T, out string\)

登録内容と現在の環境を毎回照合し、過去の選択をキャッシュしません。

```csharp
public bool TryResolve(string editorVersion, string editorRevision, IEnumerable<PackageIdentity> installedPackages, string requestedId, out T converter, out string reason)
```

#### 引数（Parameters）

`editorVersion` [string](https://learn.microsoft.com/dotnet/api/system.string)

`editorRevision` [string](https://learn.microsoft.com/dotnet/api/system.string)

`installedPackages` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<[PackageIdentity](Omni.VersionedConversion.PackageIdentity.md)\>

`requestedId` [string](https://learn.microsoft.com/dotnet/api/system.string)

`converter` T

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
