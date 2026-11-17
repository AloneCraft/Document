# <a id="VirtualGeometry_World_PlanetGpuAnchor"></a> Struct PlanetGpuAnchor

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

G2の精度検証用アンカー。sphere原点をLogicalでcamera相対にし、子以下の差だけをfloatで求める。

```csharp
public struct PlanetGpuAnchor
```

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetGpuAnchor_FromCamera"></a> FromCamera

```csharp
public Vector4 FromCamera
```

#### 値（Field Value）

 Vector4

### <a id="VirtualGeometry_World_PlanetGpuAnchor_Key"></a> Key

```csharp
public PlanetGpuKey Key
```

#### 値（Field Value）

 [PlanetGpuKey](VirtualGeometry.World.PlanetGpuKey.md)

### <a id="VirtualGeometry_World_PlanetGpuAnchor_MaximumDescendantDepth"></a> MaximumDescendantDepth

```csharp
public const int MaximumDescendantDepth = 10
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetGpuAnchor_Stride"></a> Stride

```csharp
public const int Stride = 64
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetGpuAnchor_TangentRadiusAngle"></a> TangentRadiusAngle

```csharp
public Vector4 TangentRadiusAngle
```

#### 値（Field Value）

 Vector4

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetGpuAnchor_TryCenter_VirtualGeometry_World_PlanetGpuKey_UnityEngine_Vector3__UnityEngine_Vector3__UnityEngine_Vector3__"></a> TryCenter\(PlanetGpuKey, out Vector3, out Vector3, out Vector3\)

```csharp
public bool TryCenter(PlanetGpuKey child, out Vector3 sphereOffset, out Vector3 direction, out Vector3 fromCamera)
```

#### 引数（Parameters）

`child` [PlanetGpuKey](VirtualGeometry.World.PlanetGpuKey.md)

`sphereOffset` Vector3

`direction` Vector3

`fromCamera` Vector3

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetGpuAnchor_TryCreate_VirtualGeometry_World_PlanetCellFrame__System_Single_Omni_Logical_Vector3__VirtualGeometry_World_PlanetGpuAnchor__"></a> TryCreate\(in PlanetCellFrame, float, in Vector3, out PlanetGpuAnchor\)

```csharp
public static bool TryCreate(in PlanetCellFrame frame, float radius, in Vector3 camera, out PlanetGpuAnchor anchor)
```

#### 引数（Parameters）

`frame` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

`radius` [float](https://learn.microsoft.com/dotnet/api/system.single)

`camera` Vector3

`anchor` [PlanetGpuAnchor](VirtualGeometry.World.PlanetGpuAnchor.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
