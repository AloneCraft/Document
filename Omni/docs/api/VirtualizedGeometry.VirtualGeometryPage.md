# <a id="VirtualizedGeometry_VirtualGeometryPage"></a> Class VirtualGeometryPage

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

検証済みページのCPU表現。ランタイムは必要ページだけをこの単位で読み込む。

```csharp
public sealed class VirtualGeometryPage
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryPage](VirtualizedGeometry.VirtualGeometryPage.md)

## コンストラクター（Constructors）

### <a id="VirtualizedGeometry_VirtualGeometryPage__ctor_VirtualizedGeometry_VirtualGeometryPackedVertex___System_UInt32___VirtualizedGeometry_VirtualGeometryCluster___System_Int32_UnityEngine_Bounds_"></a> VirtualGeometryPage\(VirtualGeometryPackedVertex\[\], uint\[\], VirtualGeometryCluster\[\], int, Bounds\)

```csharp
public VirtualGeometryPage(VirtualGeometryPackedVertex[] vertices, uint[] indices, VirtualGeometryCluster[] clusters, int materialCount, Bounds bounds)
```

#### 引数（Parameters）

`vertices` [VirtualGeometryPackedVertex](VirtualizedGeometry.VirtualGeometryPackedVertex.md)\[\]

`indices` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]

`clusters` [VirtualGeometryCluster](VirtualizedGeometry.VirtualGeometryCluster.md)\[\]

`materialCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`bounds` Bounds

### <a id="VirtualizedGeometry_VirtualGeometryPage__ctor_VirtualizedGeometry_VirtualGeometryPackedVertex___System_UInt32___VirtualizedGeometry_VirtualGeometryCluster___VirtualizedGeometry_VirtualGeometryHierarchyNode___System_UInt32___System_UInt32___System_Int32_UnityEngine_Bounds_VirtualizedGeometry_VirtualGeometryConnection_"></a> VirtualGeometryPage\(VirtualGeometryPackedVertex\[\], uint\[\], VirtualGeometryCluster\[\], VirtualGeometryHierarchyNode\[\], uint\[\], uint\[\], int, Bounds, VirtualGeometryConnection\)

```csharp
public VirtualGeometryPage(VirtualGeometryPackedVertex[] vertices, uint[] indices, VirtualGeometryCluster[] clusters, VirtualGeometryHierarchyNode[] nodes, uint[] groupLinks, uint[] rootNodeIndices, int materialCount, Bounds bounds, VirtualGeometryConnection connection = null)
```

#### 引数（Parameters）

`vertices` [VirtualGeometryPackedVertex](VirtualizedGeometry.VirtualGeometryPackedVertex.md)\[\]

`indices` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]

`clusters` [VirtualGeometryCluster](VirtualizedGeometry.VirtualGeometryCluster.md)\[\]

`nodes` [VirtualGeometryHierarchyNode](VirtualizedGeometry.VirtualGeometryHierarchyNode.md)\[\]

`groupLinks` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]

`rootNodeIndices` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]

`materialCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`bounds` Bounds

`connection` [VirtualGeometryConnection](VirtualizedGeometry.VirtualGeometryConnection.md)

## プロパティ（Properties）

### <a id="VirtualizedGeometry_VirtualGeometryPage_Bounds"></a> Bounds

```csharp
public Bounds Bounds { get; }
```

#### 値（Property Value）

 Bounds

### <a id="VirtualizedGeometry_VirtualGeometryPage_Clusters"></a> Clusters

```csharp
public VirtualGeometryCluster[] Clusters { get; }
```

#### 値（Property Value）

 [VirtualGeometryCluster](VirtualizedGeometry.VirtualGeometryCluster.md)\[\]

### <a id="VirtualizedGeometry_VirtualGeometryPage_Connection"></a> Connection

独立archive接続の正本。存在するときはstream codec v7で保存する。

```csharp
public VirtualGeometryConnection Connection { get; }
```

#### 値（Property Value）

 [VirtualGeometryConnection](VirtualizedGeometry.VirtualGeometryConnection.md)

### <a id="VirtualizedGeometry_VirtualGeometryPage_GroupLinks"></a> GroupLinks

各groupの入力を出力しているgroup(生産者)のindex。nodeの <code>FirstChild</code>、<code>ChildCount</code> がこの配列の範囲を指す。

```csharp
public uint[] GroupLinks { get; }
```

#### 値（Property Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]

### <a id="VirtualizedGeometry_VirtualGeometryPage_Indices"></a> Indices

```csharp
public uint[] Indices { get; }
```

#### 値（Property Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]

### <a id="VirtualizedGeometry_VirtualGeometryPage_MaterialCount"></a> MaterialCount

```csharp
public int MaterialCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryPage_Nodes"></a> Nodes

```csharp
public VirtualGeometryHierarchyNode[] Nodes { get; }
```

#### 値（Property Value）

 [VirtualGeometryHierarchyNode](VirtualizedGeometry.VirtualGeometryHierarchyNode.md)\[\]

### <a id="VirtualizedGeometry_VirtualGeometryPage_RootNodeIndices"></a> RootNodeIndices

```csharp
public uint[] RootNodeIndices { get; }
```

#### 値（Property Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]

### <a id="VirtualizedGeometry_VirtualGeometryPage_Vertices"></a> Vertices

```csharp
public VirtualGeometryPackedVertex[] Vertices { get; }
```

#### 値（Property Value）

 [VirtualGeometryPackedVertex](VirtualizedGeometry.VirtualGeometryPackedVertex.md)\[\]
