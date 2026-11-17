# <a id="Omni_RadialIdentityWarp"></a> Class RadialIdentityWarp

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

同じGameObjectのRendererまたはTerrainだけを、Radial Shaderのまま対数写像を恒等にして描画します。

```csharp
[ExecuteAlways]
[DisallowMultipleComponent]
public sealed class RadialIdentityWarp : MonoBehaviour
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[RadialIdentityWarp](Omni.RadialIdentityWarp.md)

## 補足（Remarks）

URP本来のShader、Radial恒等、Radial対数を同じCamera・同じフレームで並べて比べる検証用です。
恒等のRendererは実Transformとnative Boundsで描くため、カリングはURPと同じ判定になります。
Scene BRGのInstanceごとに恒等へ切り替える仕組みは無いため、Scene BRGの自動所有から常に外し、
Legacy（RendererごとのMaterialPropertyBlock）経路で描きます。
Terrainは非保存のpatchを作らず、Terrain本来の描画へ恒等の値を渡します。

## メソッド（Methods）

### <a id="Omni_RadialIdentityWarp_IsApplied_UnityEngine_Renderer_"></a> IsApplied\(Renderer\)

有効な印を持つRendererかを返します。

```csharp
public static bool IsApplied(Renderer renderer)
```

#### 引数（Parameters）

`renderer` Renderer

判定するRenderer。nullは対象外です。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_RadialIdentityWarp_IsApplied_UnityEngine_Terrain_"></a> IsApplied\(Terrain\)

有効な印を持つTerrainかを返します。

```csharp
public static bool IsApplied(Terrain terrain)
```

#### 引数（Parameters）

`terrain` Terrain

判定するTerrain。nullは対象外です。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
