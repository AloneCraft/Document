# <a id="VirtualizedGeometry_VirtualGeometryHierarchyNode"></a> Struct VirtualGeometryHierarchyNode

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

階層のgroup。入力clusterを束ねて外周を固定して簡略化し、出力cluster(<xref href="VirtualizedGeometry.VirtualGeometryHierarchyNode.FirstCluster" data-throw-if-not-resolved="false"></xref>、<xref href="VirtualizedGeometry.VirtualGeometryHierarchyNode.ClusterCount" data-throw-if-not-resolved="false"></xref>)を作る。
出力clusterは次の段で別のgroupへ振り分けられるので、groupの関係は木ではなくDAGになる。
<xref href="VirtualizedGeometry.VirtualGeometryHierarchyNode.GeometricError" data-throw-if-not-resolved="false"></xref> と bounds は出力(簡略化後)のもので、入力のgroupより単調に大きく、入力のgroupの球を含む。
<xref href="VirtualizedGeometry.VirtualGeometryHierarchyNode.FirstChild" data-throw-if-not-resolved="false"></xref>、<xref href="VirtualizedGeometry.VirtualGeometryHierarchyNode.ChildCount" data-throw-if-not-resolved="false"></xref> は、入力clusterを出力しているgroup(生産者)のindexが並ぶ <xref href="VirtualizedGeometry.VirtualGeometryPage.GroupLinks" data-throw-if-not-resolved="false"></xref> の範囲。
段0のgroupは入力を持たず(ChildCount=0)、leaf cluster 1つを出力する。<xref href="VirtualizedGeometry.VirtualGeometryHierarchyNode.LeafStart" data-throw-if-not-resolved="false"></xref>、<xref href="VirtualizedGeometry.VirtualGeometryHierarchyNode.LeafCount" data-throw-if-not-resolved="false"></xref> は使わない。

```csharp
[Serializable]
public struct VirtualGeometryHierarchyNode
```

## フィールド（Fields）

### <a id="VirtualizedGeometry_VirtualGeometryHierarchyNode_BoundsCenter"></a> BoundsCenter

```csharp
public Vector3 BoundsCenter
```

#### 値（Field Value）

 Vector3

### <a id="VirtualizedGeometry_VirtualGeometryHierarchyNode_BoundsRadius"></a> BoundsRadius

```csharp
public float BoundsRadius
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryHierarchyNode_ChildCount"></a> ChildCount

```csharp
public uint ChildCount
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualizedGeometry_VirtualGeometryHierarchyNode_ClusterCount"></a> ClusterCount

```csharp
public uint ClusterCount
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualizedGeometry_VirtualGeometryHierarchyNode_FirstChild"></a> FirstChild

```csharp
public uint FirstChild
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualizedGeometry_VirtualGeometryHierarchyNode_FirstCluster"></a> FirstCluster

```csharp
public uint FirstCluster
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualizedGeometry_VirtualGeometryHierarchyNode_GeometricError"></a> GeometricError

```csharp
public float GeometricError
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryHierarchyNode_LeafCount"></a> LeafCount

```csharp
public uint LeafCount
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualizedGeometry_VirtualGeometryHierarchyNode_LeafStart"></a> LeafStart

```csharp
public uint LeafStart
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualizedGeometry_VirtualGeometryHierarchyNode_Level"></a> Level

```csharp
public uint Level
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualizedGeometry_VirtualGeometryHierarchyNode_MaterialSlot"></a> MaterialSlot

```csharp
public uint MaterialSlot
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualizedGeometry_VirtualGeometryHierarchyNode_PageId"></a> PageId

```csharp
public uint PageId
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualizedGeometry_VirtualGeometryHierarchyNode_Reserved0"></a> Reserved0

```csharp
public uint Reserved0
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualizedGeometry_VirtualGeometryHierarchyNode_Reserved1"></a> Reserved1

```csharp
public uint Reserved1
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualizedGeometry_VirtualGeometryHierarchyNode_Stride"></a> Stride

```csharp
public const int Stride = 64
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)
