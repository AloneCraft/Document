# <a id="VirtualGeometry_World_PlanetPlacementFrame"></a> Struct PlanetPlacementFrame

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

camera ごとに、惑星をどの空間に置いて選択・cull・描画するかの値。

```csharp
public readonly struct PlanetPlacementFrame
```

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetPlacementFrame__ctor_Omni_Logical_Vector3__UnityEngine_Matrix4x4_UnityEngine_Vector3_System_Single_VirtualizedGeometry_VirtualGeometryCullSpace_VirtualGeometry_World_IPlanetDisplayMapping_"></a> PlanetPlacementFrame\(in Vector3, Matrix4x4, Vector3, float, VirtualGeometryCullSpace, IPlanetDisplayMapping\)

```csharp
public PlanetPlacementFrame(in Vector3 cameraLocal, Matrix4x4 localToCull, Vector3 cameraCull, float localToCullScale, VirtualGeometryCullSpace cullSpace, IPlanetDisplayMapping display = null)
```

#### 引数（Parameters）

`cameraLocal` Vector3

`localToCull` Matrix4x4

`cameraCull` Vector3

`localToCullScale` [float](https://learn.microsoft.com/dotnet/api/system.single)

`cullSpace` [VirtualGeometryCullSpace](VirtualizedGeometry.VirtualGeometryCullSpace.md)

`display` [IPlanetDisplayMapping](VirtualGeometry.World.IPlanetDisplayMapping.md)

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetPlacementFrame_CameraCull"></a> CameraCull

cull 空間でのカメラの位置。

```csharp
public readonly Vector3 CameraCull
```

#### 値（Field Value）

 Vector3

### <a id="VirtualGeometry_World_PlanetPlacementFrame_CameraLocal"></a> CameraLocal

惑星のローカル座標でのカメラの位置(Logical。Cell の選択に使う)。

```csharp
public readonly Vector3 CameraLocal
```

#### 値（Field Value）

 Vector3

### <a id="VirtualGeometry_World_PlanetPlacementFrame_CullSpace"></a> CullSpace

```csharp
public readonly VirtualGeometryCullSpace CullSpace
```

#### 値（Field Value）

 [VirtualGeometryCullSpace](VirtualizedGeometry.VirtualGeometryCullSpace.md)

### <a id="VirtualGeometry_World_PlanetPlacementFrame_Display"></a> Display

描画空間の写像（Radial で圧縮した空間を別のカメラから見るとき）。null なら、選択は実距離と実際の視錐台で行う。
写像があるカメラは、実距離では画面上の大きさも視錐台も合わないので、<xref href="VirtualGeometry.World.PlanetCellSelector" data-throw-if-not-resolved="false"></xref> は写像後の値で誤差と cull を求める。

```csharp
public readonly IPlanetDisplayMapping Display
```

#### 値（Field Value）

 [IPlanetDisplayMapping](VirtualGeometry.World.IPlanetDisplayMapping.md)

### <a id="VirtualGeometry_World_PlanetPlacementFrame_LocalToCull"></a> LocalToCull

惑星のローカル座標の向きを cull 空間へ写す行列(線形部分だけを使う)。

```csharp
public readonly Matrix4x4 LocalToCull
```

#### 値（Field Value）

 Matrix4x4

### <a id="VirtualGeometry_World_PlanetPlacementFrame_LocalToCullScale"></a> LocalToCullScale

```csharp
public readonly float LocalToCullScale
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)
