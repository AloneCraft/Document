# <a id="VirtualizedGeometry_VirtualGeometryClusterView"></a> Struct VirtualGeometryClusterView

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

実行時生成clusterの供給元がcameraごとの選択で受け取る視点の情報。座標はworld空間。

```csharp
public readonly struct VirtualGeometryClusterView
```

## コンストラクター（Constructors）

### <a id="VirtualizedGeometry_VirtualGeometryClusterView__ctor_UnityEngine_Camera_UnityEngine_Vector3_UnityEngine_Plane___System_Single_System_Single_System_Boolean_UnityEngine_Matrix4x4_"></a> VirtualGeometryClusterView\(Camera, Vector3, Plane\[\], float, float, bool, Matrix4x4\)

```csharp
public VirtualGeometryClusterView(Camera camera, Vector3 cameraPosition, Plane[] frustumPlanes, float projectionScale, float nearPlane, bool orthographic, Matrix4x4 viewProjection)
```

#### 引数（Parameters）

`camera` Camera

`cameraPosition` Vector3

`frustumPlanes` Plane\[\]

`projectionScale` [float](https://learn.microsoft.com/dotnet/api/system.single)

`nearPlane` [float](https://learn.microsoft.com/dotnet/api/system.single)

`orthographic` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`viewProjection` Matrix4x4

## フィールド（Fields）

### <a id="VirtualizedGeometry_VirtualGeometryClusterView_Camera"></a> Camera

```csharp
public readonly Camera Camera
```

#### 値（Field Value）

 Camera

### <a id="VirtualizedGeometry_VirtualGeometryClusterView_CameraPosition"></a> CameraPosition

```csharp
public readonly Vector3 CameraPosition
```

#### 値（Field Value）

 Vector3

### <a id="VirtualizedGeometry_VirtualGeometryClusterView_FrustumPlanes"></a> FrustumPlanes

```csharp
public readonly Plane[] FrustumPlanes
```

#### 値（Field Value）

 Plane\[\]

### <a id="VirtualizedGeometry_VirtualGeometryClusterView_NearPlane"></a> NearPlane

```csharp
public readonly float NearPlane
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryClusterView_Orthographic"></a> Orthographic

```csharp
public readonly bool Orthographic
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryClusterView_ProjectionScale"></a> ProjectionScale

透視投影では画面誤差 = world誤差×ProjectionScale/距離。正射影では world誤差×ProjectionScale。

```csharp
public readonly float ProjectionScale
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryClusterView_ViewProjection"></a> ViewProjection

world 空間の GPU 用 ViewProjection(HZB の判定に使う)。

```csharp
public readonly Matrix4x4 ViewProjection
```

#### 値（Field Value）

 Matrix4x4
