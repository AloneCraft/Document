# <a id="Omni_BatchRendering_RadialSceneBatchRendererExclusion"></a> Class RadialSceneBatchRendererExclusion

Namespace: [Omni.BatchRendering](Omni.BatchRendering.md)  
Assembly: Omni.BatchRendering.Runtime.dll  

外部のMaterialPropertyBlockを維持するScene Renderer（Animatorがmaterialのプロパティを書くもの等）を
Scene BRGの自動所有から除外し、通常のOmni Radial MeshRenderer経路へ残します。

```csharp
[ExecuteAlways]
[DisallowMultipleComponent]
public sealed class RadialSceneBatchRendererExclusion : MonoBehaviour
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[RadialSceneBatchRendererExclusion](Omni.BatchRendering.RadialSceneBatchRendererExclusion.md)

## メソッド（Methods）

### <a id="Omni_BatchRendering_RadialSceneBatchRendererExclusion_RegisterExternalMaterialOwnership_System_Func_UnityEngine_Material_System_Boolean__"></a> RegisterExternalMaterialOwnership\(Func<Material, bool\>\)

検証などが所有するMaterialを製品用Scene BRGから除外する判定を登録します。
Editor側の所有権判定をRuntime assemblyへ逆向き参照せず渡す境界です。

```csharp
public static void RegisterExternalMaterialOwnership(Func<Material, bool> ownership)
```

#### 引数（Parameters）

`ownership` [Func](https://learn.microsoft.com/dotnet/api/system.func\-2)<Material, [bool](https://learn.microsoft.com/dotnet/api/system.boolean)\>

### <a id="Omni_BatchRendering_RadialSceneBatchRendererExclusion_RegisterUnmappedSceneMaterial_System_Func_UnityEngine_MeshRenderer_System_Int32_UnityEngine_Material_System_Boolean__"></a> RegisterUnmappedSceneMaterial\(Func<MeshRenderer, int, Material, bool\>\)

正本（永続Material）へ戻せないScene Materialを判定する関数を登録します（Editor側が登録）。
スクリプトがEditモードで作った照明ごとの複製などはsidecarを作れないため、そのRendererだけ
Scene BRGから外して通常の描画へ残します。Play準備全体を止めないためです。

```csharp
public static void RegisterUnmappedSceneMaterial(Func<MeshRenderer, int, Material, bool> predicate)
```

#### 引数（Parameters）

`predicate` [Func](https://learn.microsoft.com/dotnet/api/system.func\-4)<MeshRenderer, [int](https://learn.microsoft.com/dotnet/api/system.int32), Material, [bool](https://learn.microsoft.com/dotnet/api/system.boolean)\>
