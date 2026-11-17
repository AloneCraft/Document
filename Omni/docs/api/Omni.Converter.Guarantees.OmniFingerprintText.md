# <a id="Omni_Converter_Guarantees_OmniFingerprintText"></a> Class OmniFingerprintText

Namespace: [Omni.Converter.Guarantees](Omni.Converter.Guarantees.md)  
Assembly: Omni.Converter.dll  

変換保証の指紋に使う本文の正規化と SHA-256 です。

<p>
改行と BOM だけを揃えます。Git の改行の変換や編集器の BOM で、同じ内容の指紋が変わらないようにするためです。
それ以上の正規化（空白・大小文字）はしません。変換器が見る本文の違いを指紋が見落とさないためです。
</p>

```csharp
public static class OmniFingerprintText
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniFingerprintText](Omni.Converter.Guarantees.OmniFingerprintText.md)

## フィールド（Fields）

### <a id="Omni_Converter_Guarantees_OmniFingerprintText_Algorithm"></a> Algorithm

```csharp
public const string Algorithm = "omni-fp/1"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniFingerprintText_OmniRootToken"></a> OmniRootToken

```csharp
public const string OmniRootToken = "{omni}/"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Converter_Guarantees_OmniFingerprintText_HashText_System_String_"></a> HashText\(string\)

```csharp
public static string HashText(string text)
```

#### 引数（Parameters）

`text` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniFingerprintText_Normalize_System_String_"></a> Normalize\(string\)

```csharp
public static string Normalize(string text)
```

#### 引数（Parameters）

`text` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniFingerprintText_TryHashFile_System_String_System_Boolean_System_String__System_String__"></a> TryHashFile\(string, bool, out string, out string\)

```csharp
public static bool TryHashFile(string fullPath, bool replaceOmniRoot, out string hash, out string error)
```

#### 引数（Parameters）

`fullPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`replaceOmniRoot` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`hash` [string](https://learn.microsoft.com/dotnet/api/system.string)

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_Guarantees_OmniFingerprintText_TryNormalizeOmniRoot_System_String_System_String_System_String__"></a> TryNormalizeOmniRoot\(string, string, out string\)

本文に入った本体の根（開発では <code>Assets/Omni</code>、配布では <code>Packages/com.omni.rendering</code>）を
<xref href="Omni.Converter.Guarantees.OmniFingerprintText.OmniRootToken" data-throw-if-not-resolved="false"></xref> へ置き換えます。生成物は根の資産パスを本文へ書くため、置き換えないと
開発環境と配布物で同じ変換の指紋が一致しません。

```csharp
public static bool TryNormalizeOmniRoot(string normalizedText, string omniRoot, out string result)
```

#### 引数（Parameters）

`normalizedText` [string](https://learn.microsoft.com/dotnet/api/system.string)

`omniRoot` [string](https://learn.microsoft.com/dotnet/api/system.string)

`result` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
