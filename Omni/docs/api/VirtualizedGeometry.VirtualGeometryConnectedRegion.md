# <a id="VirtualizedGeometry_VirtualGeometryConnectedRegion"></a> Class VirtualGeometryConnectedRegion

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

同じpageと境界パターンの準備済み三角形。LODは公開cutが決める。配列は供給元が所有し、公開後は変更しない。

```csharp
public sealed class VirtualGeometryConnectedRegion
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryConnectedRegion](VirtualizedGeometry.VirtualGeometryConnectedRegion.md)

## コンストラクター（Constructors）

### <a id="VirtualizedGeometry_VirtualGeometryConnectedRegion__ctor_System_Int32_System_Object_VirtualizedGeometry_VirtualGeometryPage_VirtualizedGeometry_VirtualGeometryVertexConnection___System_UInt32___System_Single_System_Int32_"></a> VirtualGeometryConnectedRegion\(int, object, VirtualGeometryPage, VirtualGeometryVertexConnection\[\], uint\[\], float, int\)

```csharp
public VirtualGeometryConnectedRegion(int group, object pattern, VirtualGeometryPage topology, VirtualGeometryVertexConnection[] connections, uint[] triangleIndices, float boundsPadding, int detailLevel = 0)
```

#### 引数（Parameters）

`group` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`pattern` [object](https://learn.microsoft.com/dotnet/api/system.object)

`topology` [VirtualGeometryPage](VirtualizedGeometry.VirtualGeometryPage.md)

`connections` [VirtualGeometryVertexConnection](VirtualizedGeometry.VirtualGeometryVertexConnection.md)\[\]

`triangleIndices` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]

`boundsPadding` [float](https://learn.microsoft.com/dotnet/api/system.single)

`detailLevel` [int](https://learn.microsoft.com/dotnet/api/system.int32)

## フィールド（Fields）

### <a id="VirtualizedGeometry_VirtualGeometryConnectedRegion_BoundsPadding"></a> BoundsPadding

```csharp
public readonly float BoundsPadding
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryConnectedRegion_Connections"></a> Connections

```csharp
public readonly VirtualGeometryVertexConnection[] Connections
```

#### 値（Field Value）

 [VirtualGeometryVertexConnection](VirtualizedGeometry.VirtualGeometryVertexConnection.md)\[\]

### <a id="VirtualizedGeometry_VirtualGeometryConnectedRegion_DetailLevel"></a> DetailLevel

```csharp
public readonly int DetailLevel
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryConnectedRegion_Group"></a> Group

```csharp
public readonly int Group
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryConnectedRegion_Pattern"></a> Pattern

```csharp
public readonly object Pattern
```

#### 値（Field Value）

 [object](https://learn.microsoft.com/dotnet/api/system.object)

### <a id="VirtualizedGeometry_VirtualGeometryConnectedRegion_Topology"></a> Topology

```csharp
public readonly VirtualGeometryPage Topology
```

#### 値（Field Value）

 [VirtualGeometryPage](VirtualizedGeometry.VirtualGeometryPage.md)

### <a id="VirtualizedGeometry_VirtualGeometryConnectedRegion_TriangleIndices"></a> TriangleIndices

```csharp
public readonly uint[] TriangleIndices
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]
