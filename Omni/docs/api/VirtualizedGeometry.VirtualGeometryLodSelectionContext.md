# <a id="VirtualizedGeometry_VirtualGeometryLodSelectionContext"></a> Struct VirtualGeometryLodSelectionContext

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

```csharp
public readonly struct VirtualGeometryLodSelectionContext
```

## コンストラクター（Constructors）

### <a id="VirtualizedGeometry_VirtualGeometryLodSelectionContext__ctor_UnityEngine_Matrix4x4_UnityEngine_Vector3_System_Boolean_System_Single_System_Single_System_Int32_System_Single_System_Single_System_Single_"></a> VirtualGeometryLodSelectionContext\(Matrix4x4, Vector3, bool, float, float, int, float, float, float\)

```csharp
public VirtualGeometryLodSelectionContext(Matrix4x4 objectToWorld, Vector3 cameraPosition, bool orthographic, float verticalFieldOfViewDegrees, float orthographicSize, int pixelHeight, float nearPlane, float targetErrorPixels, float hysteresis)
```

#### 引数（Parameters）

`objectToWorld` Matrix4x4

`cameraPosition` Vector3

`orthographic` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`verticalFieldOfViewDegrees` [float](https://learn.microsoft.com/dotnet/api/system.single)

`orthographicSize` [float](https://learn.microsoft.com/dotnet/api/system.single)

`pixelHeight` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`nearPlane` [float](https://learn.microsoft.com/dotnet/api/system.single)

`targetErrorPixels` [float](https://learn.microsoft.com/dotnet/api/system.single)

`hysteresis` [float](https://learn.microsoft.com/dotnet/api/system.single)

## プロパティ（Properties）

### <a id="VirtualizedGeometry_VirtualGeometryLodSelectionContext_CameraPosition"></a> CameraPosition

```csharp
public Vector3 CameraPosition { get; }
```

#### 値（Property Value）

 Vector3

### <a id="VirtualizedGeometry_VirtualGeometryLodSelectionContext_Hysteresis"></a> Hysteresis

```csharp
public float Hysteresis { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryLodSelectionContext_NearPlane"></a> NearPlane

```csharp
public float NearPlane { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryLodSelectionContext_ObjectToWorld"></a> ObjectToWorld

```csharp
public Matrix4x4 ObjectToWorld { get; }
```

#### 値（Property Value）

 Matrix4x4

### <a id="VirtualizedGeometry_VirtualGeometryLodSelectionContext_Orthographic"></a> Orthographic

```csharp
public bool Orthographic { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryLodSelectionContext_OrthographicSize"></a> OrthographicSize

```csharp
public float OrthographicSize { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryLodSelectionContext_PixelHeight"></a> PixelHeight

```csharp
public int PixelHeight { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryLodSelectionContext_TargetErrorPixels"></a> TargetErrorPixels

```csharp
public float TargetErrorPixels { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryLodSelectionContext_VerticalFieldOfViewDegrees"></a> VerticalFieldOfViewDegrees

```csharp
public float VerticalFieldOfViewDegrees { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)
