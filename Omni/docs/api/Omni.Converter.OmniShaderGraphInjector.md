# <a id="Omni_Converter_OmniShaderGraphInjector"></a> Class OmniShaderGraphInjector

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

.shadergraph ファイルに <code>RadialKeepObjectPosition</code> Custom Function Node と
camera-relative <code>_RadialGlobal_*</code> schemaを所有範囲内で自動注入・更新します。
VertexDescription はObject座標を保持したままにし、Absolute World → Object の
float round-trip をGraph経路へ作りません。

```csharp
public static class OmniShaderGraphInjector
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniShaderGraphInjector](Omni.Converter.OmniShaderGraphInjector.md)

## メソッド（Methods）

### <a id="Omni_Converter_OmniShaderGraphInjector_InjectRadialWarp_System_String_"></a> InjectRadialWarp\(string\)

変換先のShaderGraphへ現在のRadial schemaを注入します。既存の注入があれば、
注入器が所有するproperty/node/edgeだけを置き換えます。

```csharp
public static void InjectRadialWarp(string shaderGraphPath)
```

#### 引数（Parameters）

`shaderGraphPath` [string](https://learn.microsoft.com/dotnet/api/system.string)
