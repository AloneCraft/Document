# <a id="Omni_Converter_OmniBuiltInToUrpUpgrade"></a> Class OmniBuiltInToUrpUpgrade

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

Built-in RP専用のParticle Shaderを、URPのMaterial Upgrader（Unity標準）でURPのShaderへ移してから
Omniの対数変換へ渡すための入口です。Omniは変換表を持たず、Shaderの対応とPropertyの写し方は
URPのUpgraderに任せます。元のMaterialは書き換えず、呼び出し側が作る管理Materialの写しにだけ適用します。
範囲はParticle系に限ります（Legacy Shaders等は未対応のまま診断表示にします）。

```csharp
public static class OmniBuiltInToUrpUpgrade
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniBuiltInToUrpUpgrade](Omni.Converter.OmniBuiltInToUrpUpgrade.md)

## メソッド（Methods）

### <a id="Omni_Converter_OmniBuiltInToUrpUpgrade_Apply_UnityEngine_Material_UnityEditor_Rendering_MaterialUpgrader_"></a> Apply\(Material, MaterialUpgrader\)

管理Materialの写しをURPのShaderへ移します。移せなければ例外にして、半端な状態を残しません。

```csharp
public static void Apply(Material managed, MaterialUpgrader upgrader)
```

#### 引数（Parameters）

`managed` Material

`upgrader` MaterialUpgrader

### <a id="Omni_Converter_OmniBuiltInToUrpUpgrade_TryFind_UnityEngine_Shader_UnityEditor_Rendering_MaterialUpgrader__UnityEngine_Shader__System_String__"></a> TryFind\(Shader, out MaterialUpgrader, out Shader, out string\)

URPのUpgraderでURPのShaderへ移せるBuilt-inのShaderなら、そのUpgraderと対数Shaderを返します。

```csharp
public static bool TryFind(Shader builtIn, out MaterialUpgrader upgrader, out Shader omniTarget, out string reason)
```

#### 引数（Parameters）

`builtIn` Shader

`upgrader` MaterialUpgrader

`omniTarget` Shader

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
