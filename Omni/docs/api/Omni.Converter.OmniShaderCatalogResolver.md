# <a id="Omni_Converter_OmniShaderCatalogResolver"></a> Class OmniShaderCatalogResolver

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

標準URP Shaderと、その対数（Radial）版の対応を、利用者の環境の生成物から解決します。
対応は<xref href="Omni.Converter.OmniStandardUrpSources" data-throw-if-not-resolved="false"></xref>の確定一覧と出力先の規則（<xref href="Omni.Converter.RadialMaterialConverter.GetOmniOutputPath(System.String)" data-throw-if-not-resolved="false"></xref>）で
決まり、同梱の目録は使いません。生成物が無ければ「まだ生成していない」として解決を断ります
（生成は対数への切替の準備の段が行います）。名前一致だけの推測を行わないため、
同名のユーザーShaderを誤変換しません。

```csharp
public static class OmniShaderCatalogResolver
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniShaderCatalogResolver](Omni.Converter.OmniShaderCatalogResolver.md)

## プロパティ（Properties）

### <a id="Omni_Converter_OmniShaderCatalogResolver_SourcePaths"></a> SourcePaths

対数版を生成する標準URP Shader（手書き13、Terrainの閉包4、Decal Graph）の資産パスです。

```csharp
public static IReadOnlyCollection<string> SourcePaths { get; }
```

#### 値（Property Value）

 [IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

## メソッド（Methods）

### <a id="Omni_Converter_OmniShaderCatalogResolver_IsBundledOmniShader_UnityEngine_Shader_"></a> IsBundledOmniShader\(Shader\)

指定Shaderが、標準URP Shaderから生成した対数Shaderならtrueを返します。

```csharp
public static bool IsBundledOmniShader(Shader shader)
```

#### 引数（Parameters）

`shader` Shader

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniShaderCatalogResolver_TryResolve_UnityEngine_Shader_UnityEngine_Shader__System_String__"></a> TryResolve\(Shader, out Shader, out string\)

元Shaderの実参照に対応する、利用者の環境で生成した対数Shaderを返します。

```csharp
public static bool TryResolve(Shader source, out Shader omniShader, out string reason)
```

#### 引数（Parameters）

`source` Shader

`omniShader` Shader

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniShaderCatalogResolver_TryResolveConflictingOmniName_UnityEngine_Shader_UnityEngine_Shader__UnityEngine_Shader__"></a> TryResolveConflictingOmniName\(Shader, out Shader, out Shader\)

生成した対数Shaderと同じ内部名を持つものの、規定の出力先のShaderとは異なるShaderを検出します。
名前一致を変換成功とみなさず、旧生成物や別GUIDの複製を明示的に拒否するための境界です。

```csharp
public static bool TryResolveConflictingOmniName(Shader shader, out Shader sourceShader, out Shader expectedOmniShader)
```

#### 引数（Parameters）

`shader` Shader

Materialが現在参照しているShaderです。nullは競合なしです。

`sourceShader` Shader

競合名に対応する元Shaderです。検出できない場合はnullです。

`expectedOmniShader` Shader

規定の出力先にある正規の対数Shaderです。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

内部名は一致するが実参照が異なる場合はtrueです。

### <a id="Omni_Converter_OmniShaderCatalogResolver_TryResolveSource_UnityEngine_Shader_UnityEngine_Shader__System_String__"></a> TryResolveSource\(Shader, out Shader, out string\)

生成した対数Shaderの実参照から対応する標準Shaderを返します。

```csharp
public static bool TryResolveSource(Shader omniShader, out Shader sourceShader, out string reason)
```

#### 引数（Parameters）

`omniShader` Shader

`sourceShader` Shader

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
