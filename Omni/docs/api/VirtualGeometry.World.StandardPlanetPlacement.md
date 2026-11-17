# <a id="VirtualGeometry_World_StandardPlanetPlacement"></a> Class StandardPlanetPlacement

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

Unity の world 空間に惑星を置く(float の精度で足りる大きさに限る)。

```csharp
public sealed class StandardPlanetPlacement : IPlanetPlacement
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[StandardPlanetPlacement](VirtualGeometry.World.StandardPlanetPlacement.md)

#### 実装するインターフェース（Implements）

[IPlanetPlacement](VirtualGeometry.World.IPlanetPlacement.md)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_StandardPlanetPlacement_UsesProperties"></a> UsesProperties

Cell ごとの MaterialPropertyBlock を使うか。

```csharp
public bool UsesProperties { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="VirtualGeometry_World_StandardPlanetPlacement_Describe_VirtualGeometry_World_PlanetPlacementFrame__VirtualGeometry_World_PlanetCellFrame__UnityEngine_Matrix4x4__UnityEngine_Matrix4x4__UnityEngine_MaterialPropertyBlock_"></a> Describe\(in PlanetPlacementFrame, in PlanetCellFrame, out Matrix4x4, out Matrix4x4, MaterialPropertyBlock\)

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

### <a id="VirtualGeometry_World_StandardPlanetPlacement_TryBeginFrame_VirtualizedGeometry_VirtualGeometryClusterView__UnityEngine_Transform_VirtualGeometry_World_PlanetPlacementFrame__"></a> TryBeginFrame\(in VirtualGeometryClusterView, Transform, out PlanetPlacementFrame\)

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
