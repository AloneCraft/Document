# <a id="Omni_BatchRendering_RadialBrgRuntimeMaterialCache"></a> Class RadialBrgRuntimeMaterialCache

Namespace: [Omni.BatchRendering](Omni.BatchRendering.md)  
Assembly: Omni.BatchRendering.Runtime.dll  

動的textureを持つ材質を検証済みBRG shaderへ複製し、backendの寿命中所有します。

```csharp
public sealed class RadialBrgRuntimeMaterialCache : IDisposable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialBrgRuntimeMaterialCache](Omni.BatchRendering.RadialBrgRuntimeMaterialCache.md)

#### 実装するインターフェース（Implements）

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

## メソッド（Methods）

### <a id="Omni_BatchRendering_RadialBrgRuntimeMaterialCache_Dispose"></a> Dispose\(\)

複製だけを解放します。元材質とtextureの寿命は変更しません。

```csharp
public void Dispose()
```

### <a id="Omni_BatchRendering_RadialBrgRuntimeMaterialCache_Prune_System_Collections_Generic_ISet_UnityEngine_Material__"></a> Prune\(ISet<Material\>\)

BRG登録解除後に呼び、動的Rendererの削除で使われなくなった複製を解放します。

```csharp
public void Prune(ISet<Material> referenced)
```

#### 引数（Parameters）

`referenced` [ISet](https://learn.microsoft.com/dotnet/api/system.collections.generic.iset\-1)<Material\>

### <a id="Omni_BatchRendering_RadialBrgRuntimeMaterialCache_SyncProperties"></a> SyncProperties\(\)

元Materialへ後から書かれた値を複製へ写します。WashiLightControllerのように毎フレーム強度を
書き換えるProviderでも、BRG描画が生成時点の値に固定されないようにします。

```csharp
public void SyncProperties()
```

### <a id="Omni_BatchRendering_RadialBrgRuntimeMaterialCache_TryResolve_UnityEngine_Material_Omni_BatchRendering_RadialBrgMaterialManifest_UnityEngine_Material__"></a> TryResolve\(Material, RadialBrgMaterialManifest, out Material\)

元shaderの一致だけではBRG適合としません。manifest内の実sidecar shaderへ変換します。

```csharp
public bool TryResolve(Material source, RadialBrgMaterialManifest manifest, out Material material)
```

#### 引数（Parameters）

`source` Material

`manifest` [RadialBrgMaterialManifest](Omni.BatchRendering.RadialBrgMaterialManifest.md)

`material` Material

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_BatchRendering_RadialBrgRuntimeMaterialCache_TryResolveShader_UnityEngine_Material_Omni_BatchRendering_RadialBrgMaterialManifest_UnityEngine_Shader__"></a> TryResolveShader\(Material, RadialBrgMaterialManifest, out Shader\)

実行時Materialを変換できる検証済みsidecar shaderを返します。Play前のEditor検証も同じ規則で判定し、
Editorだけが通してbackendで失敗する食い違いを作りません。

```csharp
public static bool TryResolveShader(Material source, RadialBrgMaterialManifest manifest, out Shader shader)
```

#### 引数（Parameters）

`source` Material

`manifest` [RadialBrgMaterialManifest](Omni.BatchRendering.RadialBrgMaterialManifest.md)

`shader` Shader

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
