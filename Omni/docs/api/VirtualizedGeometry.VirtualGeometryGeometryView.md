# <a id="VirtualizedGeometry_VirtualGeometryGeometryView"></a> Struct VirtualGeometryGeometryView

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

同じsourceを複数のCameraで選ぶための値。絶対float位置を持たない。

```csharp
public readonly struct VirtualGeometryGeometryView
```

## コンストラクター（Constructors）

### <a id="VirtualizedGeometry_VirtualGeometryGeometryView__ctor_Omni_Logical_Vector3__UnityEngine_Matrix4x4_VirtualizedGeometry_VirtualGeometryCullSpace_System_Single_System_Single_System_Single_System_Boolean_System_Object_"></a> VirtualGeometryGeometryView\(in Vector3, Matrix4x4, VirtualGeometryCullSpace, float, float, float, bool, object\)

```csharp
public VirtualGeometryGeometryView(in Vector3 eye, Matrix4x4 localToCull, VirtualGeometryCullSpace cull, float scale, float projection, float near, bool orthographic, object placementState = null)
```

#### 引数（Parameters）

`eye` Vector3

`localToCull` Matrix4x4

`cull` [VirtualGeometryCullSpace](VirtualizedGeometry.VirtualGeometryCullSpace.md)

`scale` [float](https://learn.microsoft.com/dotnet/api/system.single)

`projection` [float](https://learn.microsoft.com/dotnet/api/system.single)

`near` [float](https://learn.microsoft.com/dotnet/api/system.single)

`orthographic` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`placementState` [object](https://learn.microsoft.com/dotnet/api/system.object)

## フィールド（Fields）

### <a id="VirtualizedGeometry_VirtualGeometryGeometryView_CullSpace"></a> CullSpace

```csharp
public readonly VirtualGeometryCullSpace CullSpace
```

#### 値（Field Value）

 [VirtualGeometryCullSpace](VirtualizedGeometry.VirtualGeometryCullSpace.md)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryView_Eye"></a> Eye

```csharp
public readonly Vector3 Eye
```

#### 値（Field Value）

 Vector3

### <a id="VirtualizedGeometry_VirtualGeometryGeometryView_LocalToCull"></a> LocalToCull

```csharp
public readonly Matrix4x4 LocalToCull
```

#### 値（Field Value）

 Matrix4x4

### <a id="VirtualizedGeometry_VirtualGeometryGeometryView_Near"></a> Near

```csharp
public readonly float Near
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryView_Orthographic"></a> Orthographic

```csharp
public readonly bool Orthographic
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryView_PlacementState"></a> PlacementState

```csharp
public readonly object PlacementState
```

#### 値（Field Value）

 [object](https://learn.microsoft.com/dotnet/api/system.object)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryView_Projection"></a> Projection

```csharp
public readonly float Projection
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryView_Scale"></a> Scale

```csharp
public readonly float Scale
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometryGeometryView_IsVisible_VirtualizedGeometry_VirtualGeometryGeometryGroup__"></a> IsVisible\(in VirtualGeometryGeometryGroup\)

```csharp
public bool IsVisible(in VirtualGeometryGeometryGroup group)
```

#### 引数（Parameters）

`group` [VirtualGeometryGeometryGroup](VirtualizedGeometry.VirtualGeometryGeometryGroup.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryView_ScreenError_VirtualizedGeometry_VirtualGeometryGeometryGroup__"></a> ScreenError\(in VirtualGeometryGeometryGroup\)

```csharp
public float ScreenError(in VirtualGeometryGeometryGroup group)
```

#### 引数（Parameters）

`group` [VirtualGeometryGeometryGroup](VirtualizedGeometry.VirtualGeometryGeometryGroup.md)

#### 戻り値（Returns）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryView_TryBounds_VirtualizedGeometry_VirtualGeometryGeometryGroup__UnityEngine_Vector3__System_Single__"></a> TryBounds\(in VirtualGeometryGeometryGroup, out Vector3, out float\)

```csharp
public bool TryBounds(in VirtualGeometryGeometryGroup group, out Vector3 center, out float radius)
```

#### 引数（Parameters）

`group` [VirtualGeometryGeometryGroup](VirtualizedGeometry.VirtualGeometryGeometryGroup.md)

`center` Vector3

`radius` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
