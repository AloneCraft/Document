# <a id="Omni_Converter_UnityAssetPathResolver"></a> Class UnityAssetPathResolver

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

Unity の論理アセットパスを、ファイル API で使える実体パスへ解決します。

<p>
Registry / built-in package はプロジェクト直下の <code>Packages/</code> に実ファイルを
持たず、<code>Library/PackageCache</code> に実体が置かれます。ハッシュ付き cache 名を
推測せず、<xref href="UnityEditor.PackageManager.PackageInfo.resolvedPath" data-throw-if-not-resolved="false"></xref> を使います。
</p>

```csharp
public static class UnityAssetPathResolver
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[UnityAssetPathResolver](Omni.Converter.UnityAssetPathResolver.md)

## メソッド（Methods）

### <a id="Omni_Converter_UnityAssetPathResolver_GetFullPath_System_String_"></a> GetFullPath\(string\)

論理アセットパスを実体パスへ解決します。通常の Assets パスはそのまま返し、
物理的に存在しない Packages パスだけ Package Manager の解決済みパスへ置換します。

```csharp
public static string GetFullPath(string logicalPath)
```

#### 引数（Parameters）

`logicalPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
