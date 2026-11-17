# <a id="Omni_Converter_RadialVfxBackend"></a> Class RadialVfxBackend

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

VFX Graph の Radial 対応の状態を、実際に描画に使われるシェーダーで判定する Editor の窓口です。

<p>
パッチは <xref href="Omni.Converter.RadialVfxImportHook" data-throw-if-not-resolved="false"></xref> が取り込みのたびに、全ての VFX の表示用シェーダーへ当てます
（VFX Graph 17.6 では、以前の外部化した .vfxshader と manifest の方式は使われていませんでした）。
この窓口は、フックが入っていることと、各 VFX 資産の描画シェーダーがパッチの目印（<xref href="Omni.Converter.RadialVfxShaderPatcher.SentinelProperty" data-throw-if-not-resolved="false"></xref>）を
公開していることを確かめます。パッチ無しのシェーダーは Unity が Properties を公開しないので、目印の有無で判別できます。
古い（パッチ前に取り込まれた）資産は <xref href="Omni.Converter.RadialVfxBackend.GenerateForLoadedScenes(System.String%40)" data-throw-if-not-resolved="false"></xref> / <xref href="Omni.Converter.RadialVfxBackend.GenerateForAssetPaths(System.Collections.Generic.IEnumerable%7bSystem.String%7d%2cSystem.String%40)" data-throw-if-not-resolved="false"></xref>
で取り込み直します。待機中に自動で取り込み直すのは、使う VFX（<xref href="Omni.Converter.RadialVfxUsage" data-throw-if-not-resolved="false"></xref>）だけです
（<xref href="Omni.Converter.RadialVfxAssetPostprocessor" data-throw-if-not-resolved="false"></xref>）。
</p>

```csharp
public static class RadialVfxBackend
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialVfxBackend](Omni.Converter.RadialVfxBackend.md)

## メソッド（Methods）

### <a id="Omni_Converter_RadialVfxBackend_CollectLoadedSceneAssetPaths"></a> CollectLoadedSceneAssetPaths\(\)

読み込み中の Scene（切替の対象）が参照する VFX 資産のパス（パスの順）。

```csharp
public static IReadOnlyList<string> CollectLoadedSceneAssetPaths()
```

#### 戻り値（Returns）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Converter_RadialVfxBackend_CountPatchedShaders_UnityEngine_VFX_VisualEffectAsset_System_Int32__System_Int32__"></a> CountPatchedShaders\(VisualEffectAsset, out int, out int\)

VFX 資産の描画シェーダーの数と、そのうちパッチの目印を公開している数。描画シェーダーを持たない資産（描画の出力が無い）は 0/0 です。

```csharp
public static void CountPatchedShaders(VisualEffectAsset asset, out int renderShaders, out int patchedShaders)
```

#### 引数（Parameters）

`asset` VisualEffectAsset

`renderShaders` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`patchedShaders` [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Converter_RadialVfxBackend_GenerateForAssetPaths_System_Collections_Generic_IEnumerable_System_String__System_String__"></a> GenerateForAssetPaths\(IEnumerable<string\>, out string\)

指定した VFX 資産のうち、パッチの無い資産を取り込み直します。

```csharp
public static bool GenerateForAssetPaths(IEnumerable<string> assetPaths, out string error)
```

#### 引数（Parameters）

`assetPaths` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_RadialVfxBackend_GenerateForLoadedScenes_System_String__"></a> GenerateForLoadedScenes\(out string\)

読み込み中の Scene が参照する VFX のうち、パッチの無い資産を取り込み直します。

```csharp
public static bool GenerateForLoadedScenes(out string error)
```

#### 引数（Parameters）

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_RadialVfxBackend_IsManagedRuntimeMaterial_UnityEngine_Renderer_UnityEngine_Material_"></a> IsManagedRuntimeMaterial\(Renderer, Material\)

```csharp
public static bool IsManagedRuntimeMaterial(Renderer renderer, Material material)
```

#### 引数（Parameters）

`renderer` Renderer

`material` Material

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_RadialVfxBackend_IsVfxRenderer_UnityEngine_Renderer_"></a> IsVfxRenderer\(Renderer\)

```csharp
public static bool IsVfxRenderer(Renderer renderer)
```

#### 引数（Parameters）

`renderer` Renderer

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_RadialVfxBackend_ScanAssetPaths_System_Collections_Generic_IEnumerable_System_String__"></a> ScanAssetPaths\(IEnumerable<string\>\)

指定した VFX 資産の状態（Build の対象など）。

```csharp
public static RadialVfxSceneState ScanAssetPaths(IEnumerable<string> assetPaths)
```

#### 引数（Parameters）

`assetPaths` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

#### 戻り値（Returns）

 [RadialVfxSceneState](Omni.Converter.RadialVfxSceneState.md)

### <a id="Omni_Converter_RadialVfxBackend_ScanLoadedScenes"></a> ScanLoadedScenes\(\)

読み込み中の Scene（切替の対象）が参照する VFX の状態。

```csharp
public static RadialVfxSceneState ScanLoadedScenes()
```

#### 戻り値（Returns）

 [RadialVfxSceneState](Omni.Converter.RadialVfxSceneState.md)
