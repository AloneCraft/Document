# <a id="Omni_Converter_OmniRadialExemptShaders"></a> Class OmniRadialExemptShaders

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

Radialへ変換しないと決めた標準URP Shaderの一覧です(2026-09-30の判断)。
URPの2D Shader(Sprite／Mesh2D／Sprite Mask)はフォークを持たず、カタログにも登録しません。
カタログは「標準→Radial」の対なので、Radial側が空の登録は未登録扱いになり、診断表示とPlayer Buildの中止を招くためです。
名前やタグでの推測はせず、パッケージ内の正確なパスだけで判定します。
実行時の扱いは変わりません。<code>Omni.Logical.Transform</code>の下にある間はRadialのカメラで安全側に非表示になり、外にあれば標準描画です。
モバイル向けのTextMesh Pro Shader（<code>TextMeshPro/Mobile/*</code>とその派生）も対象外です。Omni 0.1.xはモバイルを
対象にしないためで、デスクトップ向けにはURP用のShader Graph（TMP_SDF-URP Lit/Unlit）を変換します。

```csharp
public static class OmniRadialExemptShaders
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniRadialExemptShaders](Omni.Converter.OmniRadialExemptShaders.md)

## プロパティ（Properties）

### <a id="Omni_Converter_OmniRadialExemptShaders_MobileTextMeshProPaths"></a> MobileTextMeshProPaths

変換対象にしない、モバイル向けTextMesh Pro Shaderのアセットパスです。

```csharp
public static IReadOnlyList<string> MobileTextMeshProPaths { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Converter_OmniRadialExemptShaders_Paths"></a> Paths

変換対象にしない標準URP Shaderのアセットパスです。

```csharp
public static IReadOnlyList<string> Paths { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

## メソッド（Methods）

### <a id="Omni_Converter_OmniRadialExemptShaders_IsExempt_UnityEngine_Shader_"></a> IsExempt\(Shader\)

Shaderの実参照が、変換対象にしない標準URP Shaderならtrueを返します。

```csharp
public static bool IsExempt(Shader shader)
```

#### 引数（Parameters）

`shader` Shader

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniRadialExemptShaders_IsExemptPath_System_String_"></a> IsExemptPath\(string\)

Shaderのアセットパスが、変換対象にしない標準URP Shaderならtrueを返します。

```csharp
public static bool IsExemptPath(string shaderPath)
```

#### 引数（Parameters）

`shaderPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
