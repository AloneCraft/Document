# <a id="VirtualGeometry_World_IPlanetPlacement"></a> Interface IPlanetPlacement

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

惑星を置く座標系。既定(<xref href="VirtualGeometry.World.StandardPlanetPlacement" data-throw-if-not-resolved="false"></xref>)は Unity の world 空間で、惑星の GameObject の行列を使う。
Omni の対数描画では、惑星の位置を Logical で持ち、カメラ相対の物理空間で cull し、Cell ごとに Omni の物体の値を書く実装を使う
(VirtualGeometry.Omni の OmniPlanetPlacement。惑星と同じ GameObject に付けると <xref href="VirtualGeometry.World.PlanetLayerSource" data-throw-if-not-resolved="false"></xref> が使う)。
呼び出しは camera ごとに TryBeginFrame → Describe(Cell の数だけ)の順で、同じ camera の中で入れ子にならない。

```csharp
public interface IPlanetPlacement
```

## プロパティ（Properties）

### <a id="VirtualGeometry_World_IPlanetPlacement_UsesProperties"></a> UsesProperties

Cell ごとの MaterialPropertyBlock を使うか。

```csharp
bool UsesProperties { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="VirtualGeometry_World_IPlanetPlacement_Describe_VirtualGeometry_World_PlanetPlacementFrame__VirtualGeometry_World_PlanetCellFrame__UnityEngine_Matrix4x4__UnityEngine_Matrix4x4__UnityEngine_MaterialPropertyBlock_"></a> Describe\(in PlanetPlacementFrame, in PlanetCellFrame, out Matrix4x4, out Matrix4x4, MaterialPropertyBlock\)

Cell の draw の値。頂点は Cell の原点(cell.Origin = 半径 R の球面上の点を cell.HeightShift だけ外向きに持ち上げた点、惑星のローカル座標、Logical 精度)からの相対位置で書かれている。
properties は UsesProperties が true のときだけ渡る。値を作れないときは false(この Cell を描かない)。

```csharp
bool Describe(in PlanetPlacementFrame frame, in PlanetCellFrame cell, out Matrix4x4 objectToWorld, out Matrix4x4 objectToCull, MaterialPropertyBlock properties)
```

#### 引数（Parameters）

`frame` [PlanetPlacementFrame](VirtualGeometry.World.PlanetPlacementFrame.md)

`cell` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

`objectToWorld` Matrix4x4

`objectToCull` Matrix4x4

`properties` MaterialPropertyBlock

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_IPlanetPlacement_TryBeginFrame_VirtualizedGeometry_VirtualGeometryClusterView__UnityEngine_Transform_VirtualGeometry_World_PlanetPlacementFrame__"></a> TryBeginFrame\(in VirtualGeometryClusterView, Transform, out PlanetPlacementFrame\)

この camera で描くための値を作る。描けないときは false(この camera では惑星を描かない)。

```csharp
bool TryBeginFrame(in VirtualGeometryClusterView view, Transform planet, out PlanetPlacementFrame frame)
```

#### 引数（Parameters）

`view` [VirtualGeometryClusterView](VirtualizedGeometry.VirtualGeometryClusterView.md)

`planet` Transform

`frame` [PlanetPlacementFrame](VirtualGeometry.World.PlanetPlacementFrame.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
