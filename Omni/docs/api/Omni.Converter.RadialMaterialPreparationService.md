# <a id="Omni_Converter_RadialMaterialPreparationService"></a> Class RadialMaterialPreparationService

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

元MaterialからRadial ShaderとRadial Materialを確保する共通Editorサービスです。
Manager UIとScene BRGの双方が同じ生成順序を利用し、検証だけの呼び出しとは分離します。

```csharp
public static class RadialMaterialPreparationService
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialMaterialPreparationService](Omni.Converter.RadialMaterialPreparationService.md)

## メソッド（Methods）

### <a id="Omni_Converter_RadialMaterialPreparationService_IsShaderPatchExcluded_UnityEngine_Shader_"></a> IsShaderPatchExcluded\(Shader\)

名前ではなく、登録済みのPass解析が変換不要を証明した場合だけtrueです。

```csharp
public static bool IsShaderPatchExcluded(Shader shader)
```

#### 引数（Parameters）

`shader` Shader

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_RadialMaterialPreparationService_RegisterShaderGenerator_System_Func_System_String_System_String__"></a> RegisterShaderGenerator\(Func<string, string\>\)

上位のShaderパッチャを登録します。ConverterからManager assemblyを参照しないための
依存性逆転境界で、Unity domain reloadごとにManagerが登録します。

```csharp
public static void RegisterShaderGenerator(Func<string, string> generator)
```

#### 引数（Parameters）

`generator` [Func](https://learn.microsoft.com/dotnet/api/system.func\-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [string](https://learn.microsoft.com/dotnet/api/system.string)\>

元ShaderのAsset pathを受け、生成先pathを返す関数です。

### <a id="Omni_Converter_RadialMaterialPreparationService_RegisterShaderPatchExclusion_System_Func_System_String_System_Boolean__"></a> RegisterShaderPatchExclusion\(Func<string, bool\>\)

全描画Passが変換不要であることを解析する上位パッチャの判定を登録します。

```csharp
public static void RegisterShaderPatchExclusion(Func<string, bool> exclusion)
```

#### 引数（Parameters）

`exclusion` [Func](https://learn.microsoft.com/dotnet/api/system.func\-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [bool](https://learn.microsoft.com/dotnet/api/system.boolean)\>

### <a id="Omni_Converter_RadialMaterialPreparationService_TryEnsure_UnityEngine_Material_System_Boolean_UnityEngine_Material__System_Boolean__System_String__"></a> TryEnsure\(Material, bool, out Material, out bool, out string\)

元Materialに対応するRadial Materialを、Shader生成後に確保します。

```csharp
public static bool TryEnsure(Material source, bool regenerateShader, out Material generated, out bool changed, out string reason)
```

#### 引数（Parameters）

`source` Material

SceneまたはManagerが保持する永続元Materialです。

`regenerateShader` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

既存Shaderも現在のパッチャで更新する場合はtrueです。

`generated` Material

確保済みRadial Materialです。元からRadialの場合はsource自身です。

`changed` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

生成物の作成、移行、または再生成を行った場合はtrueです。

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

失敗時の一次原因です。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

Radial契約を満たすMaterialを確保できた場合はtrueです。

### <a id="Omni_Converter_RadialMaterialPreparationService_TryEnsureRadialShader_UnityEngine_Material_UnityEngine_Shader__System_Boolean__System_Boolean__System_String__"></a> TryEnsureRadialShader\(Material, out Shader, out bool, out bool, out string\)

元Materialを描くRadial Shaderだけを確保します。Radial Materialの写し（<code>Assets/Radial/Project</code> など）は作りません。

<p>
Scene BRGのsidecarは元Materialの値を写し、ShaderだけをRadial ShaderのBRG版にするので、写しを使いません。
以前のScene BRGは<xref href="Omni.Converter.RadialMaterialPreparationService.TryEnsure(UnityEngine.Material%2cSystem.Boolean%2cUnityEngine.Material%40%2cSystem.Boolean%40%2cSystem.String%40)" data-throw-if-not-resolved="false"></xref>で写しを作り、そのShaderを読んでいました。対数への切替は元Materialの
Shaderを直接差し替えるので写しを作らず、標準へ戻した直後の自動準備だけが全Materialの写しを1件ずつ作って
取り込んでいました（URP 3DサンプルのTerminalでRefresh 71回、34.6秒）。
</p>

```csharp
public static bool TryEnsureRadialShader(Material source, out Shader radialShader, out bool changed, out bool generationFailed, out string reason)
```

#### 引数（Parameters）

`source` Material

SceneまたはManagerが保持する永続元Materialです。

`radialShader` Shader

元MaterialのRadial Shaderです。元からRadialならそのShaderです。

`changed` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

Shaderを生成した場合はtrueです。

`generationFailed` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

生成器を呼んで出力が無かった場合はtrueです。同じ元Shaderと同じ変換器では同じ結果になります
（生成器はそのたびにConsoleへ理由を出すので、自動の呼出し側が同じ入力で繰り返さないための印です）。

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

失敗時の一次原因です。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

Radial契約を満たすShaderを確保できた場合はtrueです。

### <a id="Omni_Converter_RadialMaterialPreparationService_TryResolveRadialShader_UnityEngine_Shader_System_Boolean_UnityEngine_Shader__System_Boolean__System_String__"></a> TryResolveRadialShader\(Shader, bool, out Shader, out bool, out string\)

標準URPのShader（手書き、Terrainの閉包、Decal Graph）は、利用者の環境に生成した対数版（OmniShaderCatalogResolver）から、
それ以外（Shader Graph、ユーザーShader）は明示的な生成器から、置換先を解決します。生成は<code class="paramref">allowUserGeneration</code>が
trueのとき（対数への切替の準備の段）だけ行います。

```csharp
public static bool TryResolveRadialShader(Shader source, bool allowUserGeneration, out Shader radialShader, out bool changed, out string reason)
```

#### 引数（Parameters）

`source` Shader

`allowUserGeneration` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`radialShader` Shader

`changed` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
