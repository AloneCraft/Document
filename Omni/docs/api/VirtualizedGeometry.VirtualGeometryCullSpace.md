# <a id="VirtualizedGeometry_VirtualGeometryCullSpace"></a> Struct VirtualGeometryCullSpace

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

cluster の cull を行う空間。world とは限らない(Omni の対数描画では、カメラ相対の物理空間)。
カメラの位置・視錐台の6平面・HZB 用の ViewProjection はすべてこの空間で表す。

```csharp
public readonly struct VirtualGeometryCullSpace
```

## コンストラクター（Constructors）

### <a id="VirtualizedGeometry_VirtualGeometryCullSpace__ctor_UnityEngine_Vector3_UnityEngine_Plane___UnityEngine_Matrix4x4_System_Single_System_Boolean_"></a> VirtualGeometryCullSpace\(Vector3, Plane\[\], Matrix4x4, float, bool\)

```csharp
public VirtualGeometryCullSpace(Vector3 cameraPosition, Plane[] planes, Matrix4x4 viewProjection, float nearPlane, bool occlusionAllowed)
```

#### 引数（Parameters）

`cameraPosition` Vector3

`planes` Plane\[\]

`viewProjection` Matrix4x4

`nearPlane` [float](https://learn.microsoft.com/dotnet/api/system.single)

`occlusionAllowed` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## フィールド（Fields）

### <a id="VirtualizedGeometry_VirtualGeometryCullSpace_CameraPosition"></a> CameraPosition

```csharp
public readonly Vector3 CameraPosition
```

#### 値（Field Value）

 Vector3

### <a id="VirtualizedGeometry_VirtualGeometryCullSpace_NearPlane"></a> NearPlane

```csharp
public readonly float NearPlane
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryCullSpace_OcclusionAllowed"></a> OcclusionAllowed

HZB の遮蔽判定を使ってよいか。深度が ViewProjection と同じ写像でないとき(対数描画など)は false。

```csharp
public readonly bool OcclusionAllowed
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryCullSpace_Planes"></a> Planes

```csharp
public readonly Plane[] Planes
```

#### 値（Field Value）

 Plane\[\]

### <a id="VirtualizedGeometry_VirtualGeometryCullSpace_ViewProjection"></a> ViewProjection

```csharp
public readonly Matrix4x4 ViewProjection
```

#### 値（Field Value）

 Matrix4x4
