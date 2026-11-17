# <a id="Omni_VersionedConversion_IVersionedShaderConverter"></a> Interface IVersionedShaderConverter

Namespace: [Omni.VersionedConversion](Omni.VersionedConversion.md)  
Assembly: Omni.VersionedConversion.dll  

URP シェーダー本文の版別変換を表します。ファイルの書込みは行いません。

```csharp
public interface IVersionedShaderConverter
```

## メソッド（Methods）

### <a id="Omni_VersionedConversion_IVersionedShaderConverter_Patch_System_String_System_String_System_String_Omni_VersionedConversion_IShaderSourceAccess_"></a> Patch\(string, string, string, IShaderSourceAccess\)

```csharp
ShaderConversionResult Patch(string source, string sourcePath, string uniqueShaderName, IShaderSourceAccess sources)
```

#### 引数（Parameters）

`source` [string](https://learn.microsoft.com/dotnet/api/system.string)

`sourcePath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`uniqueShaderName` [string](https://learn.microsoft.com/dotnet/api/system.string)

`sources` [IShaderSourceAccess](Omni.VersionedConversion.IShaderSourceAccess.md)

#### 戻り値（Returns）

 [ShaderConversionResult](Omni.VersionedConversion.ShaderConversionResult.md)
