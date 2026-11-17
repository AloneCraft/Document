# <a id="VirtualizedGeometry_VirtualGeometryCulling"></a> Class VirtualGeometryCulling

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

GPU cullingと同じ保守規則をテスト可能なCPU関数として定義する。

```csharp
public static class VirtualGeometryCulling
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryCulling](VirtualizedGeometry.VirtualGeometryCulling.md)

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometryCulling_IsOccludedDepth_System_Single_System_Single_System_Boolean_System_Single_"></a> IsOccludedDepth\(float, float, bool, float\)

```csharp
public static bool IsOccludedDepth(float objectNearestDepth, float hzbFarthestDepth, bool reversedZ, float bias)
```

#### 引数（Parameters）

`objectNearestDepth` [float](https://learn.microsoft.com/dotnet/api/system.single)

`hzbFarthestDepth` [float](https://learn.microsoft.com/dotnet/api/system.single)

`reversedZ` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`bias` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryCulling_IsSphereInsideFrustum_UnityEngine_Vector3_System_Single_UnityEngine_Plane___"></a> IsSphereInsideFrustum\(Vector3, float, Plane\[\]\)

```csharp
public static bool IsSphereInsideFrustum(Vector3 center, float radius, Plane[] planes)
```

#### 引数（Parameters）

`center` Vector3

`radius` [float](https://learn.microsoft.com/dotnet/api/system.single)

`planes` Plane\[\]

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryCulling_ReduceDepth_System_Single_System_Single_System_Single_System_Single_System_Boolean_"></a> ReduceDepth\(float, float, float, float, bool\)

```csharp
public static float ReduceDepth(float a, float b, float c, float d, bool reversedZ)
```

#### 引数（Parameters）

`a` [float](https://learn.microsoft.com/dotnet/api/system.single)

`b` [float](https://learn.microsoft.com/dotnet/api/system.single)

`c` [float](https://learn.microsoft.com/dotnet/api/system.single)

`d` [float](https://learn.microsoft.com/dotnet/api/system.single)

`reversedZ` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryCulling_TransformSphere_UnityEngine_Vector3_System_Single_UnityEngine_Matrix4x4_"></a> TransformSphere\(Vector3, float, Matrix4x4\)

```csharp
public static VirtualGeometryWorldSphere TransformSphere(Vector3 localCenter, float localRadius, Matrix4x4 localToWorld)
```

#### 引数（Parameters）

`localCenter` Vector3

`localRadius` [float](https://learn.microsoft.com/dotnet/api/system.single)

`localToWorld` Matrix4x4

#### 戻り値（Returns）

 [VirtualGeometryWorldSphere](VirtualizedGeometry.VirtualGeometryWorldSphere.md)
