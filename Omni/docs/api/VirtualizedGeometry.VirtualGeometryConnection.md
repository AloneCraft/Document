# <a id="VirtualizedGeometry_VirtualGeometryConnection"></a> Class VirtualGeometryConnection

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

汎用meshの共通局所格子と、全生成LODで保持する明示境界。Logical原点はFrameIdの外側で保持する。

```csharp
public sealed class VirtualGeometryConnection
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryConnection](VirtualizedGeometry.VirtualGeometryConnection.md)

## コンストラクター（Constructors）

### <a id="VirtualizedGeometry_VirtualGeometryConnection__ctor_System_String_UnityEngine_Vector3_UnityEngine_Vector3_System_Int32_System_Single_System_Int32_VirtualizedGeometry_VirtualGeometryConnectionBoundary___"></a> VirtualGeometryConnection\(string, Vector3, Vector3, int, float, int, params VirtualGeometryConnectionBoundary\[\]\)

```csharp
public VirtualGeometryConnection(string frameId, Vector3 minimum, Vector3 extent, int builderBits, float maximumStep, int maximumRootTriangles, params VirtualGeometryConnectionBoundary[] boundaries)
```

#### 引数（Parameters）

`frameId` [string](https://learn.microsoft.com/dotnet/api/system.string)

`minimum` Vector3

`extent` Vector3

`builderBits` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`maximumStep` [float](https://learn.microsoft.com/dotnet/api/system.single)

`maximumRootTriangles` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`boundaries` [VirtualGeometryConnectionBoundary](VirtualizedGeometry.VirtualGeometryConnectionBoundary.md)\[\]

## プロパティ（Properties）

### <a id="VirtualizedGeometry_VirtualGeometryConnection_BoundaryCount"></a> BoundaryCount

```csharp
public int BoundaryCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryConnection_BuilderBits"></a> BuilderBits

```csharp
public int BuilderBits { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryConnection_Extent"></a> Extent

```csharp
public Vector3 Extent { get; }
```

#### 値（Property Value）

 Vector3

### <a id="VirtualizedGeometry_VirtualGeometryConnection_FrameId"></a> FrameId

```csharp
public string FrameId { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualizedGeometry_VirtualGeometryConnection_MaximumRootTriangles"></a> MaximumRootTriangles

```csharp
public int MaximumRootTriangles { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryConnection_MaximumStep"></a> MaximumStep

```csharp
public float MaximumStep { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryConnection_Minimum"></a> Minimum

```csharp
public Vector3 Minimum { get; }
```

#### 値（Property Value）

 Vector3

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometryConnection_Boundary_System_Int32_"></a> Boundary\(int\)

```csharp
public VirtualGeometryConnectionBoundary Boundary(int index)
```

#### 引数（Parameters）

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [VirtualGeometryConnectionBoundary](VirtualizedGeometry.VirtualGeometryConnectionBoundary.md)

### <a id="VirtualizedGeometry_VirtualGeometryConnection_Contains_UnityEngine_Vector3_"></a> Contains\(Vector3\)

```csharp
public bool Contains(Vector3 point)
```

#### 引数（Parameters）

`point` Vector3

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryConnection_Same_UnityEngine_Vector3_UnityEngine_Vector3_"></a> Same\(Vector3, Vector3\)

Vector3の近似演算子を使わず、保存するfloatのbitを比較する。

```csharp
public static bool Same(Vector3 a, Vector3 b)
```

#### 引数（Parameters）

`a` Vector3

`b` Vector3

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryConnection_SameFrame_VirtualizedGeometry_VirtualGeometryConnection_"></a> SameFrame\(VirtualGeometryConnection\)

```csharp
public bool SameFrame(VirtualGeometryConnection other)
```

#### 引数（Parameters）

`other` [VirtualGeometryConnection](VirtualizedGeometry.VirtualGeometryConnection.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryConnection_ValidateInput_UnityEngine_Vector3___System_Int32_____"></a> ValidateInput\(Vector3\[\], int\[\]\[\]\)

canonical入力と実在する外周有向辺を検査する。UVなどで分かれた同位置頂点は幾何的に数える。

```csharp
public void ValidateInput(Vector3[] positions, int[][] submeshes)
```

#### 引数（Parameters）

`positions` Vector3\[\]

`submeshes` [int](https://learn.microsoft.com/dotnet/api/system.int32)\[\]\[\]

### <a id="VirtualizedGeometry_VirtualGeometryConnection_ValidateRepresentation_VirtualizedGeometry_VirtualGeometryPackedVertex___System_UInt32___System_UInt32___"></a> ValidateRepresentation\(VirtualGeometryPackedVertex\[\], uint\[\], uint\[\]\)

固定頂点だけでなく、接続辺の向きと出現数を検査する。nullのbeforeは完全表現の外周検査。

```csharp
public void ValidateRepresentation(VirtualGeometryPackedVertex[] vertices, uint[] before, uint[] after)
```

#### 引数（Parameters）

`vertices` [VirtualGeometryPackedVertex](VirtualizedGeometry.VirtualGeometryPackedVertex.md)\[\]

`before` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]

`after` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]
