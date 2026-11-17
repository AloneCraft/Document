# <a id="VirtualGeometry_Omni_OmniPlanetPlacement"></a> Class OmniPlanetPlacement

Namespace: [VirtualGeometry.Omni](VirtualGeometry.Omni.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

面(惑星)を Omni の Logical 座標に置き、Radial 対数描画で描く <xref href="VirtualGeometry.World.IPlanetPlacement" data-throw-if-not-resolved="false"></xref>。
面の GameObject(<xref href="VirtualGeometry.World.PlanarTerrainSource" data-throw-if-not-resolved="false"></xref> など <xref href="VirtualGeometry.World.PlanetLayerSource" data-throw-if-not-resolved="false"></xref> と同じもの)に Omni の Logical.Transform と一緒に付ける。
位置の正本は Logical で、float にするのは eye からの相対差にした後だけ。
cull は eye を原点とする world 軸の物理空間で行い、HZB は使わない(深度が対数写像のため)。
Cell ごとに、Omni が precise な Renderer に書くのと同じ物体ごとの値を MaterialPropertyBlock へ書く。
material には Omni の Radial shader を元にした .vgshader を使う。

```csharp
[ExecuteAlways]
[DisallowMultipleComponent]
public sealed class OmniPlanetPlacement : MonoBehaviour, IPlanetPlacement
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[OmniPlanetPlacement](VirtualGeometry.Omni.OmniPlanetPlacement.md)

#### 実装するインターフェース（Implements）

[IPlanetPlacement](VirtualGeometry.World.IPlanetPlacement.md)

## プロパティ（Properties）

### <a id="VirtualGeometry_Omni_OmniPlanetPlacement_LastCullState"></a> LastCullState

最後の frame の、視錐台での絞り込み（cull）の状態（診断用）。CanUseConeCulling が false だと、側面の平面を使わず全面を通す（fail-open）。

```csharp
public string LastCullState { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualGeometry_Omni_OmniPlanetPlacement_LastFailure"></a> LastFailure

最後に描けなかった理由(描けた frame では null)。

```csharp
public string LastFailure { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualGeometry_Omni_OmniPlanetPlacement_UsesProperties"></a> UsesProperties

Cell ごとの MaterialPropertyBlock を使うか。

```csharp
public bool UsesProperties { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="VirtualGeometry_Omni_OmniPlanetPlacement_Describe_VirtualGeometry_World_PlanetPlacementFrame__VirtualGeometry_World_PlanetCellFrame__UnityEngine_Matrix4x4__UnityEngine_Matrix4x4__UnityEngine_MaterialPropertyBlock_"></a> Describe\(in PlanetPlacementFrame, in PlanetCellFrame, out Matrix4x4, out Matrix4x4, MaterialPropertyBlock\)

Cell の draw の値。頂点は Cell の原点(cell.Origin = 半径 R の球面上の点を cell.HeightShift だけ外向きに持ち上げた点、惑星のローカル座標、Logical 精度)からの相対位置で書かれている。
properties は UsesProperties が true のときだけ渡る。値を作れないときは false(この Cell を描かない)。

```csharp
public bool Describe(in PlanetPlacementFrame frame, in PlanetCellFrame cell, out Matrix4x4 objectToWorld, out Matrix4x4 objectToCull, MaterialPropertyBlock properties)
```

#### 引数（Parameters）

`frame` [PlanetPlacementFrame](VirtualGeometry.World.PlanetPlacementFrame.md)

`cell` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

`objectToWorld` Matrix4x4

`objectToCull` Matrix4x4

`properties` MaterialPropertyBlock

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_Omni_OmniPlanetPlacement_TryBeginFrame_VirtualizedGeometry_VirtualGeometryClusterView__UnityEngine_Transform_VirtualGeometry_World_PlanetPlacementFrame__"></a> TryBeginFrame\(in VirtualGeometryClusterView, Transform, out PlanetPlacementFrame\)

この camera で描くための値を作る。描けないときは false(この camera では惑星を描かない)。

```csharp
public bool TryBeginFrame(in VirtualGeometryClusterView view, Transform planet, out PlanetPlacementFrame frame)
```

#### 引数（Parameters）

`view` [VirtualGeometryClusterView](VirtualizedGeometry.VirtualGeometryClusterView.md)

`planet` Transform

`frame` [PlanetPlacementFrame](VirtualGeometry.World.PlanetPlacementFrame.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
