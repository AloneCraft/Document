# <a id="VirtualizedGeometry_VirtualGeometryCluster"></a> Struct VirtualGeometryCluster

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

1クラスタの描画範囲。階層の置換単位はVirtualGeometryHierarchyNode(group)が保持する。
<xref href="VirtualizedGeometry.VirtualGeometryCluster.Parent" data-throw-if-not-resolved="false"></xref> はこのclusterを入力に取るgroup(消費者。最粗のgroupのclusterは -1)、<xref href="VirtualizedGeometry.VirtualGeometryCluster.ChildStart" data-throw-if-not-resolved="false"></xref> はこのclusterを出力するgroup(生産者)のnode index。

```csharp
[Serializable]
public struct VirtualGeometryCluster
```

## フィールド（Fields）

### <a id="VirtualizedGeometry_VirtualGeometryCluster_BoundsCenter"></a> BoundsCenter

```csharp
public Vector3 BoundsCenter
```

#### 値（Field Value）

 Vector3

### <a id="VirtualizedGeometry_VirtualGeometryCluster_BoundsRadius"></a> BoundsRadius

```csharp
public float BoundsRadius
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryCluster_ChildCount"></a> ChildCount

```csharp
public uint ChildCount
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualizedGeometry_VirtualGeometryCluster_ChildStart"></a> ChildStart

```csharp
public uint ChildStart
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualizedGeometry_VirtualGeometryCluster_FirstIndex"></a> FirstIndex

```csharp
public uint FirstIndex
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualizedGeometry_VirtualGeometryCluster_GeometricError"></a> GeometricError

```csharp
public float GeometricError
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryCluster_IndexCount"></a> IndexCount

```csharp
public uint IndexCount
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualizedGeometry_VirtualGeometryCluster_MaterialSlot"></a> MaterialSlot

```csharp
public uint MaterialSlot
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualizedGeometry_VirtualGeometryCluster_PageId"></a> PageId

```csharp
public uint PageId
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualizedGeometry_VirtualGeometryCluster_Parent"></a> Parent

```csharp
public int Parent
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryCluster_Stride"></a> Stride

```csharp
public const int Stride = 48
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)
