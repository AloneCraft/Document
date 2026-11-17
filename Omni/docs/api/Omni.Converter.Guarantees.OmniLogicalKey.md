# <a id="Omni_Converter_Guarantees_OmniLogicalKey"></a> Class OmniLogicalKey

Namespace: [Omni.Converter.Guarantees](Omni.Converter.Guarantees.md)  
Assembly: Omni.Converter.dll  

資産パスを、機械や配置によらない指紋の鍵にします。
パッケージは <code>@hash</code> の無い論理パス、本体は <code>omni:</code>、生成物は <code>Assets/Radial/</code> のまま、
それ以外の <code>Assets/</code> は基準のフォルダからの相対（<code>asset:</code>）です。小文字化はしません。

```csharp
public static class OmniLogicalKey
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniLogicalKey](Omni.Converter.Guarantees.OmniLogicalKey.md)

## フィールド（Fields）

### <a id="Omni_Converter_Guarantees_OmniLogicalKey_AssetPrefix"></a> AssetPrefix

```csharp
public const string AssetPrefix = "asset:"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniLogicalKey_GeneratedPrefix"></a> GeneratedPrefix

```csharp
public const string GeneratedPrefix = "Assets/Radial/"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniLogicalKey_OmniPrefix"></a> OmniPrefix

```csharp
public const string OmniPrefix = "omni:"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniLogicalKey_ProjectPrefix"></a> ProjectPrefix

利用者の <code>Assets/</code> のファイルの鍵の接頭辞です。自作 Shader の確認済みの表は、同じプロジェクトの中で
共有するものなので、プロジェクト相対のパスをそのまま鍵にします（標準の Shader の指紋では使いません）。

```csharp
public const string ProjectPrefix = "project:"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Converter_Guarantees_OmniLogicalKey_TryFromAssetPath_System_String_System_String_System_String__System_String__"></a> TryFromAssetPath\(string, string, out string, out string\)

```csharp
public static bool TryFromAssetPath(string assetPath, string assetRelativeBase, out string key, out string error)
```

#### 引数（Parameters）

`assetPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`assetRelativeBase` [string](https://learn.microsoft.com/dotnet/api/system.string)

`key` [string](https://learn.microsoft.com/dotnet/api/system.string)

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_Guarantees_OmniLogicalKey_TryFromAssetPath_System_String_System_String_System_Boolean_System_String__System_String__"></a> TryFromAssetPath\(string, string, bool, out string, out string\)

```csharp
public static bool TryFromAssetPath(string assetPath, string assetRelativeBase, bool allowProjectAssets, out string key, out string error)
```

#### 引数（Parameters）

`assetPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`assetRelativeBase` [string](https://learn.microsoft.com/dotnet/api/system.string)

`allowProjectAssets` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

true のとき、基準が無い <code>Assets/</code> のパスを <xref href="Omni.Converter.Guarantees.OmniLogicalKey.ProjectPrefix" data-throw-if-not-resolved="false"></xref> 付きの鍵にします。

`key` [string](https://learn.microsoft.com/dotnet/api/system.string)

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
