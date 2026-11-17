# <a id="Omni_VersionedConversion_PackageContentDigest"></a> Class PackageContentDigest

Namespace: [Omni.VersionedConversion](Omni.VersionedConversion.md)  
Assembly: Omni.VersionedConversion.dll  

解決済みパッケージの全ファイルを、パスと内容の両方で識別します。

```csharp
public static class PackageContentDigest
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PackageContentDigest](Omni.VersionedConversion.PackageContentDigest.md)

## メソッド（Methods）

### <a id="Omni_VersionedConversion_PackageContentDigest_Compute_System_String_"></a> Compute\(string\)

```csharp
public static string Compute(string root)
```

#### 引数（Parameters）

`root` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 補足（Remarks）

呼出し元は検査中にパッケージが変更されないよう共有読み取りを確保してください。
再解析ポイント、ファイルの変更、走査中の追加・削除は失敗として扱います。
