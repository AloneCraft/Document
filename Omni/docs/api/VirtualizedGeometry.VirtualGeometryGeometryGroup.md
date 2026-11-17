# <a id="VirtualizedGeometry_VirtualGeometryGeometryGroup"></a> Struct VirtualGeometryGeometryGroup

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

生成メッシュの安定した局所配置と置換単位。IDはsourceのepoch内で再利用しない。

```csharp
public readonly struct VirtualGeometryGeometryGroup
```

## コンストラクター（Constructors）

### <a id="VirtualizedGeometry_VirtualGeometryGeometryGroup__ctor_System_Int32_System_Int32_System_Int32_Omni_Logical_Vector3__UnityEngine_Vector3_System_Single_System_Single_System_Boolean_"></a> VirtualGeometryGeometryGroup\(int, int, int, in Vector3, Vector3, float, float, bool\)

```csharp
public VirtualGeometryGeometryGroup(int id, int parent, int detailLevel, in Vector3 origin, Vector3 center, float radius, float error, bool canRefine)
```

#### 引数（Parameters）

`id` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`parent` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`detailLevel` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`origin` Vector3

`center` Vector3

`radius` [float](https://learn.microsoft.com/dotnet/api/system.single)

`error` [float](https://learn.microsoft.com/dotnet/api/system.single)

`canRefine` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## フィールド（Fields）

### <a id="VirtualizedGeometry_VirtualGeometryGeometryGroup_BoundsCenter"></a> BoundsCenter

```csharp
public readonly Vector3 BoundsCenter
```

#### 値（Field Value）

 Vector3

### <a id="VirtualizedGeometry_VirtualGeometryGeometryGroup_BoundsRadius"></a> BoundsRadius

```csharp
public readonly float BoundsRadius
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryGroup_CanRefine"></a> CanRefine

```csharp
public readonly bool CanRefine
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryGroup_DetailLevel"></a> DetailLevel

```csharp
public readonly int DetailLevel
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryGroup_GeometricError"></a> GeometricError

```csharp
public readonly float GeometricError
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryGroup_Id"></a> Id

```csharp
public readonly int Id
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryGroup_Origin"></a> Origin

```csharp
public readonly Vector3 Origin
```

#### 値（Field Value）

 Vector3

### <a id="VirtualizedGeometry_VirtualGeometryGeometryGroup_Parent"></a> Parent

```csharp
public readonly int Parent
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)
