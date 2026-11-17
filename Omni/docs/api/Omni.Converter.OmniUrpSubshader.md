# <a id="Omni_Converter_OmniUrpSubshader"></a> Class OmniUrpSubshader

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

URPで使われるSubShader（RenderPipelineタグがUniversalPipelineか無し）のPassとタグを読みます。

<p>
Material.passCount／GetPassName／FindPass／GetTag と Shader.passCount は、Shader.globalRenderPipeline に合う
SubShaderを見ます。この値はURPが一度描画するまで空なので、起動直後の自動処理、batchmode、CIでは
代替SubShaderやFallback Shaderの情報になり、URP用のPassやタグが見えません。
</p>

```csharp
public static class OmniUrpSubshader
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniUrpSubshader](Omni.Converter.OmniUrpSubshader.md)

## メソッド（Methods）

### <a id="Omni_Converter_OmniUrpSubshader_FindPass_UnityEngine_Shader_System_String_"></a> FindPass\(Shader, string\)

URP用SubShader内のPassの番号です。無ければ -1 です。

```csharp
public static int FindPass(Shader shader, string passName)
```

#### 引数（Parameters）

`shader` Shader

`passName` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Converter_OmniUrpSubshader_PassNames_UnityEngine_Shader_"></a> PassNames\(Shader\)

URP用SubShaderのPass名です。無ければ空の配列です。

```csharp
public static string[] PassNames(Shader shader)
```

#### 引数（Parameters）

`shader` Shader

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)\[\]

### <a id="Omni_Converter_OmniUrpSubshader_Tag_UnityEngine_Shader_System_String_System_String_"></a> Tag\(Shader, string, string\)

URP用SubShaderのタグの値です（Material.GetTag の searchFallbacks:false に相当）。

```csharp
public static string Tag(Shader shader, string tagName, string defaultValue)
```

#### 引数（Parameters）

`shader` Shader

`tagName` [string](https://learn.microsoft.com/dotnet/api/system.string)

`defaultValue` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniUrpSubshader_TryGet_UnityEngine_Shader_UnityEditor_ShaderData_Subshader__"></a> TryGet\(Shader, out Subshader\)

URPが選ぶSubShader（最初の、URP向けかパイプライン指定の無いもの）を返します。

```csharp
public static bool TryGet(Shader shader, out ShaderData.Subshader subshader)
```

#### 引数（Parameters）

`shader` Shader

`subshader` ShaderData.Subshader

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniUrpSubshader_TryGetIndex_UnityEngine_Shader_System_Int32__"></a> TryGetIndex\(Shader, out int\)

URPが選ぶSubShaderの番号を返します。<xref href="UnityEngine.Rendering.PassIdentifier" data-throw-if-not-resolved="false"></xref>
（<code>ShaderUtil.GetPassKeywords(Shader, in PassIdentifier, ShaderType)</code> など）に使います。

```csharp
public static bool TryGetIndex(Shader shader, out int index)
```

#### 引数（Parameters）

`shader` Shader

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
