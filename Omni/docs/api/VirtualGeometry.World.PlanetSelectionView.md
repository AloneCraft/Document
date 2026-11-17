# <a id="VirtualGeometry_World_PlanetSelectionView"></a> Struct PlanetSelectionView

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

選択に使う視点。カメラの位置は惑星のローカル座標の Logical で持ち、Cell との差を Logical で取ってから float にする
(惑星が大きくても、カメラの近くの小さな Cell の判定が潰れない)。
cull 空間での Cell の位置は CameraCull + LocalToCull·(Cell − カメラ)(LocalToCull は線形部分だけを使う)。

```csharp
public readonly struct PlanetSelectionView
```

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetSelectionView__ctor_Omni_Logical_Vector3__Omni_Logical_Scalar__UnityEngine_Matrix4x4_UnityEngine_Vector3_System_Single_UnityEngine_Plane___System_Single_System_Single_System_Boolean_System_Boolean_VirtualGeometry_World_IPlanetDisplayMapping_"></a> PlanetSelectionView\(in Vector3, in Scalar, Matrix4x4, Vector3, float, Plane\[\], float, float, bool, bool, IPlanetDisplayMapping\)

```csharp
public PlanetSelectionView(in Vector3 cameraLocal, in Scalar radius, Matrix4x4 localToCull, Vector3 cameraCull, float maximumScale, Plane[] cullPlanes, float projectionScale, float nearPlane, bool orthographic, bool horizonCulling, IPlanetDisplayMapping display = null)
```

#### 引数（Parameters）

`cameraLocal` Vector3

`radius` Scalar

`localToCull` Matrix4x4

`cameraCull` Vector3

`maximumScale` [float](https://learn.microsoft.com/dotnet/api/system.single)

`cullPlanes` Plane\[\]

`projectionScale` [float](https://learn.microsoft.com/dotnet/api/system.single)

`nearPlane` [float](https://learn.microsoft.com/dotnet/api/system.single)

`orthographic` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`horizonCulling` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`display` [IPlanetDisplayMapping](VirtualGeometry.World.IPlanetDisplayMapping.md)

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetSelectionView_CameraAltitude"></a> CameraAltitude

カメラの、惑星の半径 R からの高さ(|CameraLocal|−R を Logical で求めたもの)。

```csharp
public readonly float CameraAltitude
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetSelectionView_CameraCull"></a> CameraCull

```csharp
public readonly Vector3 CameraCull
```

#### 値（Field Value）

 Vector3

### <a id="VirtualGeometry_World_PlanetSelectionView_CameraLocal"></a> CameraLocal

```csharp
public readonly Vector3 CameraLocal
```

#### 値（Field Value）

 Vector3

### <a id="VirtualGeometry_World_PlanetSelectionView_CullPlanes"></a> CullPlanes

cull 空間の視錐台の6平面。null なら視錐台で落とさない。

```csharp
public readonly Plane[] CullPlanes
```

#### 値（Field Value）

 Plane\[\]

### <a id="VirtualGeometry_World_PlanetSelectionView_Display"></a> Display

描画空間の写像（<xref href="VirtualGeometry.World.PlanetPlacementFrame.Display" data-throw-if-not-resolved="false"></xref>）。null なら実距離と実際の視錐台で選ぶ。

```csharp
public readonly IPlanetDisplayMapping Display
```

#### 値（Field Value）

 [IPlanetDisplayMapping](VirtualGeometry.World.IPlanetDisplayMapping.md)

### <a id="VirtualGeometry_World_PlanetSelectionView_HorizonCulling"></a> HorizonCulling

```csharp
public readonly bool HorizonCulling
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetSelectionView_LocalToCull"></a> LocalToCull

```csharp
public readonly Matrix4x4 LocalToCull
```

#### 値（Field Value）

 Matrix4x4

### <a id="VirtualGeometry_World_PlanetSelectionView_MaximumScale"></a> MaximumScale

```csharp
public readonly float MaximumScale
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetSelectionView_NearPlane"></a> NearPlane

```csharp
public readonly float NearPlane
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetSelectionView_Orthographic"></a> Orthographic

```csharp
public readonly bool Orthographic
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetSelectionView_ProjectionScale"></a> ProjectionScale

```csharp
public readonly float ProjectionScale
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)
