# <a id="Omni_Converter_OmniRadialShaderSubstitutes"></a> Class OmniRadialShaderSubstitutes

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

Omniが変換できないShader（固定機能やBuilt-in専用など）の代わりに、利用者が用意したURPの
Shaderを変換元として登録する表です。元のShaderとファイルは変えず、元のShaderを使うMaterialを
Radialへ切り替えるときだけ、代わりのShaderから生成したRadial版を使います。標準へ戻すと元のShaderへ戻ります。
代わりのShaderは元のShaderの全Propertyを同じ名前・同じ型で宣言し、URPのShaderとして通常の
検証（OmniShaderPipelineValidator）を通らなければなりません。どちらかを満たさなければ変換しません。

```csharp
[CreateAssetMenu(menuName = "Omni/Radial Shader Substitutes", fileName = "OmniRadialShaderSubstitutes")]
public sealed class OmniRadialShaderSubstitutes : ScriptableObject
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
ScriptableObject ← 
[OmniRadialShaderSubstitutes](Omni.Converter.OmniRadialShaderSubstitutes.md)

## メソッド（Methods）

### <a id="Omni_Converter_OmniRadialShaderSubstitutes_TryGetSubstitute_UnityEngine_Shader_UnityEngine_Shader__System_String__"></a> TryGetSubstitute\(Shader, out Shader, out string\)

プロジェクトの全登録表から、元のShaderの代わりのShaderを探します。登録が無ければfalseで、reasonは空です。
登録があっても使えない（表どうしの食い違い、Propertyの不一致など）ときはfalseで、reasonに理由を返します。

```csharp
public static bool TryGetSubstitute(Shader source, out Shader substitute, out string reason)
```

#### 引数（Parameters）

`source` Shader

`substitute` Shader

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
