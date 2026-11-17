# <a id="Omni_VersionedConversion_UnityPackageObservation"></a> Class UnityPackageObservation

Namespace: [Omni.VersionedConversion](Omni.VersionedConversion.md)  
Assembly: Omni.VersionedConversion.dll  

URP 固有の型へ参照せず、Package Manager の解決結果を記録します。

```csharp
public static class UnityPackageObservation
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[UnityPackageObservation](Omni.VersionedConversion.UnityPackageObservation.md)

## メソッド（Methods）

### <a id="Omni_VersionedConversion_UnityPackageObservation_TryObserve_System_Collections_Generic_IEnumerable_System_String__System_String__System_String__System_Collections_Generic_IReadOnlyList_Omni_VersionedConversion_UnityPackageObservation_ObservedPackage___System_String__"></a> TryObserve\(IEnumerable<string\>, out string, out string, out IReadOnlyList<ObservedPackage\>, out string\)

呼出し元は対象パッケージの安定した共有読み取りを確保してください。

```csharp
public static bool TryObserve(IEnumerable<string> requiredNames, out string editorVersion, out string editorRevision, out IReadOnlyList<UnityPackageObservation.ObservedPackage> observed, out string reason)
```

#### 引数（Parameters）

`requiredNames` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

`editorVersion` [string](https://learn.microsoft.com/dotnet/api/system.string)

`editorRevision` [string](https://learn.microsoft.com/dotnet/api/system.string)

`observed` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[UnityPackageObservation](Omni.VersionedConversion.UnityPackageObservation.md).[ObservedPackage](Omni.VersionedConversion.UnityPackageObservation.ObservedPackage.md)\>

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
