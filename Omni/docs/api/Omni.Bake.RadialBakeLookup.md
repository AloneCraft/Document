# <a id="Omni_Bake_RadialBakeLookup"></a> Class RadialBakeLookup

Namespace: [Omni.Bake](Omni.Bake.md)  
Assembly: Radial.Runtime.dll  

シーンから <xref href="Omni.Bake.RadialBakeBinding" data-throw-if-not-resolved="false"></xref> を探す共通ヘルパーです。
<code>RadialCullingSystem</code>（第2層カリング）と <code>RadialFarFieldCache</code>（遠景キャッシュ）の
両方が同じ探索ロジックを必要とするため、ここに切り出します。

```csharp
public static class RadialBakeLookup
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialBakeLookup](Omni.Bake.RadialBakeLookup.md)

## メソッド（Methods）

### <a id="Omni_Bake_RadialBakeLookup_TryFindBinding_UnityEngine_SceneManagement_Scene_Omni_Bake_RadialBakeBinding__"></a> TryFindBinding\(Scene, out RadialBakeBinding\)

シーンのルートGameObject群から <xref href="Omni.Bake.RadialBakeBinding" data-throw-if-not-resolved="false"></xref> を探します。
ベイクデータ（<xref href="Omni.Bake.RadialBakeBinding.Data" data-throw-if-not-resolved="false"></xref>）を持たないものは見つからなかった扱いにします。

```csharp
public static bool TryFindBinding(Scene scene, out RadialBakeBinding binding)
```

#### 引数（Parameters）

`scene` Scene

`binding` [RadialBakeBinding](Omni.Bake.RadialBakeBinding.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
