# <a id="VirtualizedGeometry_VirtualGeometryStreamMetadata"></a> Class VirtualGeometryStreamMetadata

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

geometryを常駐させず走査できるarchive metadata。

```csharp
public sealed class VirtualGeometryStreamMetadata
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryStreamMetadata](VirtualizedGeometry.VirtualGeometryStreamMetadata.md)

## フィールド（Fields）

### <a id="VirtualizedGeometry_VirtualGeometryStreamMetadata_Bounds"></a> Bounds

```csharp
public Bounds Bounds
```

#### 値（Field Value）

 Bounds

### <a id="VirtualizedGeometry_VirtualGeometryStreamMetadata_Clusters"></a> Clusters

```csharp
public VirtualGeometryCluster[] Clusters
```

#### 値（Field Value）

 [VirtualGeometryCluster](VirtualizedGeometry.VirtualGeometryCluster.md)\[\]

### <a id="VirtualizedGeometry_VirtualGeometryStreamMetadata_Connection"></a> Connection

v7の共通局所格子と接続manifest。v4/v6ではnull。

```csharp
public VirtualGeometryConnection Connection
```

#### 値（Field Value）

 [VirtualGeometryConnection](VirtualizedGeometry.VirtualGeometryConnection.md)

### <a id="VirtualizedGeometry_VirtualGeometryStreamMetadata_FileBytes"></a> FileBytes

```csharp
public long FileBytes
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualizedGeometry_VirtualGeometryStreamMetadata_FormatVersion"></a> FormatVersion

archive の版(4 = 頂点と index を生のまま、6 = cluster ごとの可変幅で、GPU が直接読める語の並び)。

```csharp
public uint FormatVersion
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualizedGeometry_VirtualGeometryStreamMetadata_GroupLinks"></a> GroupLinks

各groupの入力を出力しているgroup(生産者)のindex。nodeの FirstChild、ChildCount がこの配列の範囲を指す。

```csharp
public uint[] GroupLinks
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]

### <a id="VirtualizedGeometry_VirtualGeometryStreamMetadata_MaxPageIndices"></a> MaxPageIndices

```csharp
public int MaxPageIndices
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryStreamMetadata_MaxPageVertices"></a> MaxPageVertices

```csharp
public int MaxPageVertices
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryStreamMetadata_MetadataBytes"></a> MetadataBytes

```csharp
public int MetadataBytes
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryStreamMetadata_Nodes"></a> Nodes

```csharp
public VirtualGeometryHierarchyNode[] Nodes
```

#### 値（Field Value）

 [VirtualGeometryHierarchyNode](VirtualizedGeometry.VirtualGeometryHierarchyNode.md)\[\]

### <a id="VirtualizedGeometry_VirtualGeometryStreamMetadata_Pages"></a> Pages

```csharp
public VirtualGeometryPageDescriptor[] Pages
```

#### 値（Field Value）

 [VirtualGeometryPageDescriptor](VirtualizedGeometry.VirtualGeometryPageDescriptor.md)\[\]

### <a id="VirtualizedGeometry_VirtualGeometryStreamMetadata_Roots"></a> Roots

```csharp
public uint[] Roots
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]

### <a id="VirtualizedGeometry_VirtualGeometryStreamMetadata_UvExtent"></a> UvExtent

```csharp
public float UvExtent
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryStreamMetadata_UvMinimum"></a> UvMinimum

全頂点の UV を含む正方形の範囲(最小と幅)。header の予約領域に書く。幅 0 は「持たない」(古い archive、UV が非有限)で、UV は float のまま GPU へ上げる。

```csharp
public Vector2 UvMinimum
```

#### 値（Field Value）

 Vector2

## プロパティ（Properties）

### <a id="VirtualizedGeometry_VirtualGeometryStreamMetadata_MaxPageBytes"></a> MaxPageBytes

最大のpageの頂点数・添字数を合わせたbytes。どのpageもこの大きさ以下(CPUでの読込と復号の予算の目安)。

```csharp
public int MaxPageBytes { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryStreamMetadata_PackedPool"></a> PackedPool

true なら、page を符号化したまま 1 本の語の配列の pool へ置く(<code>VirtualGeometryPagePayload.Words</code>)。slot の大きさは byte 数の中央値(<xref href="VirtualizedGeometry.VirtualGeometryStreamMetadata.SlotWords" data-throw-if-not-resolved="false"></xref>)で、page が使う slot の数は byte 数で決まる。
false なら、復号した頂点と index を別々の pool へ置く(slot の大きさは頂点数と index 数の中央値)。archive の版 6 だけが true にできる。pool を作る前に決める。

```csharp
public bool PackedPool { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryStreamMetadata_SlotGeometryBytes"></a> SlotGeometryBytes

```csharp
public int SlotGeometryBytes { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryStreamMetadata_SlotIndices"></a> SlotIndices

```csharp
public int SlotIndices { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryStreamMetadata_SlotVertices"></a> SlotVertices

streamingのGPU poolを区切る単位(slot)1つの頂点数・添字数。pageは頂点と添字が入る数だけ連続したslotを使う。
単位はroot以外のpageの中央値にする。最大のpageに合わせると、段ごとに大きくなる上の段のpageのせいで小さなpageまで大きな枠を使い、
予算に入るpage数が大きく減る(地形の例で実データの約38倍の枠が要った)。archiveには書かず、page descriptorから決まる。

```csharp
public int SlotVertices { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryStreamMetadata_SlotWords"></a> SlotWords

packed の pool の slot 1 つの語(4 byte)の数。root 以外の page の byte 数の中央値。

```csharp
public int SlotWords { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryStreamMetadata_TotalPageSlots"></a> TotalPageSlots

全pageを同時に置くのに要るslot数。

```csharp
public long TotalPageSlots { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualizedGeometry_VirtualGeometryStreamMetadata_UniqueGeometryBytes"></a> UniqueGeometryBytes

```csharp
public long UniqueGeometryBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualizedGeometry_VirtualGeometryStreamMetadata_UvPacked"></a> UvPacked

GPU で UV を 16 bit に詰めた頂点(16 byte)にするか。

```csharp
public bool UvPacked { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometryStreamMetadata_GetPositionRange_UnityEngine_Vector3__UnityEngine_Vector3__"></a> GetPositionRange\(out Vector3, out Vector3\)

形状boundsとは独立した復元規約。CPUとGPUへ渡すパラメーターの共通入口。

```csharp
public void GetPositionRange(out Vector3 minimum, out Vector3 extent)
```

#### 引数（Parameters）

`minimum` Vector3

`extent` Vector3

### <a id="VirtualizedGeometry_VirtualGeometryStreamMetadata_PageSlots_System_Int32_"></a> PageSlots\(int\)

pageが使う連続slotの数。

```csharp
public int PageSlots(int page)
```

#### 引数（Parameters）

`page` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)
