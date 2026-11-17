# <a id="Omni_RadialMaterialContract"></a> Class RadialMaterialContract

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

MaterialのShaderが、OmniのRadial変換の契約（<code>_RadialGlobal_UseRadialTransform</code>）を宣言しているかを判定します。

```csharp
public static class RadialMaterialContract
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialMaterialContract](Omni.RadialMaterialContract.md)

## 補足（Remarks）

<xref href="UnityEngine.Material.HasProperty(System.String)" data-throw-if-not-resolved="false"></xref> はShaderが宣言していない保存済みPropertyにもtrueを返します。
過去の切替の値を残したURPのMaterialをRadial対応と誤認し、Radialの描画対象・Scene BRG・「変換済み」として
扱っていたため、Shaderの宣言で判定します。

## フィールド（Fields）

### <a id="Omni_RadialMaterialContract_UseRadialTransformProperty"></a> UseRadialTransformProperty

Radial変換の契約を表すPropertyの名前です。

```csharp
public const string UseRadialTransformProperty = "_RadialGlobal_UseRadialTransform"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_RadialMaterialContract_ClearCache"></a> ClearCache\(\)

覚えた判定を捨てます。破棄されたShaderを残さないよう、描画対象を集め直すたびに呼びます。

```csharp
public static void ClearCache()
```

### <a id="Omni_RadialMaterialContract_DeclaresRadialTransform_UnityEngine_Material_"></a> DeclaresRadialTransform\(Material\)

MaterialのShaderが契約を宣言しているかを返します。nullは対象外です。

```csharp
public static bool DeclaresRadialTransform(Material material)
```

#### 引数（Parameters）

`material` Material

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_RadialMaterialContract_DeclaresRadialTransform_UnityEngine_Shader_"></a> DeclaresRadialTransform\(Shader\)

Shaderが契約を宣言しているかを返します。nullは対象外です。

```csharp
public static bool DeclaresRadialTransform(Shader shader)
```

#### 引数（Parameters）

`shader` Shader

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
