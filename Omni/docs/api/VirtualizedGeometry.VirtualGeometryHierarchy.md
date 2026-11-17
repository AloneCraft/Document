# <a id="VirtualizedGeometry_VirtualGeometryHierarchy"></a> Class VirtualGeometryHierarchy

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

階層から導く共通規則。変換時のProxy生成と、streamingの常駐page決定で同じ段を使う。

```csharp
public static class VirtualGeometryHierarchy
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryHierarchy](VirtualizedGeometry.VirtualGeometryHierarchy.md)

## フィールド（Fields）

### <a id="VirtualizedGeometry_VirtualGeometryHierarchy_ChunkSize"></a> ChunkSize

1 つの chunk(GPU の 1 thread group)が受け持つ group の数。

```csharp
public const int ChunkSize = 64
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometryHierarchy_BuildGroupChunks_VirtualizedGeometry_VirtualGeometryHierarchyNode___System_UInt32___System_Int32___System_UInt32___"></a> BuildGroupChunks\(VirtualGeometryHierarchyNode\[\], uint\[\], int\[\], uint\[\]\)

階層(BVH)の中間の段。段 1 以上の group(<xref href="VirtualizedGeometry.VirtualGeometryHierarchy.SortByLevel(VirtualizedGeometry.VirtualGeometryHierarchyNode%5b%5d%2cSystem.Int32%5b%5d%40)" data-throw-if-not-resolved="false"></xref> の starts[1] 以降)を、段の中で Morton 順(中心の空間の並び)に並べ替え、<xref href="VirtualizedGeometry.VirtualGeometryHierarchy.ChunkSize" data-throw-if-not-resolved="false"></xref> 個ずつの chunk にして、
chunk ごとに「members の境界の球を含む球」と「members の誤差の最大」を作る(float4 を 2 つずつ: 中心 xyz・半径、誤差の最大・0・0・0)。
GPU は chunk の誤差の最大を、球の手前の端までの距離で割った値(members の画面上の誤差の上限)が閾値以下なら、chunk の group を 1 つずつ判定せずに戻る。
同じ段の group の判定は互いに独立なので、並べ替えても結果は変わらない。root(material の階層の根)を含む chunk は、誤差の最大を float.MaxValue にして、必ず判定させる。

```csharp
public static Vector4[] BuildGroupChunks(VirtualGeometryHierarchyNode[] nodes, uint[] sorted, int[] starts, uint[] roots)
```

#### 引数（Parameters）

`nodes` [VirtualGeometryHierarchyNode](VirtualizedGeometry.VirtualGeometryHierarchyNode.md)\[\]

`sorted` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]

`starts` [int](https://learn.microsoft.com/dotnet/api/system.int32)\[\]

`roots` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]

#### 戻り値（Returns）

 Vector4\[\]

### <a id="VirtualizedGeometry_VirtualGeometryHierarchy_MaximumLevel_VirtualizedGeometry_VirtualGeometryHierarchyNode___"></a> MaximumLevel\(VirtualGeometryHierarchyNode\[\]\)

groupの段(Level)の最大値。GPUの階層選択は、この段から0へ向かって1段ずつ細分化の可否を決める。

```csharp
public static int MaximumLevel(VirtualGeometryHierarchyNode[] nodes)
```

#### 引数（Parameters）

`nodes` [VirtualGeometryHierarchyNode](VirtualizedGeometry.VirtualGeometryHierarchyNode.md)\[\]

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryHierarchy_ProxyNode_VirtualizedGeometry_VirtualGeometryHierarchyNode___System_UInt32_"></a> ProxyNode\(VirtualGeometryHierarchyNode\[\], uint\)

低密度Proxy(影・fallback)に使うgroup。最粗のgroup(root)の出力。

```csharp
public static uint ProxyNode(VirtualGeometryHierarchyNode[] nodes, uint root)
```

#### 引数（Parameters）

`nodes` [VirtualGeometryHierarchyNode](VirtualizedGeometry.VirtualGeometryHierarchyNode.md)\[\]

`root` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

#### 戻り値（Returns）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualizedGeometry_VirtualGeometryHierarchy_SortByLevel_VirtualizedGeometry_VirtualGeometryHierarchyNode___System_Int32____"></a> SortByLevel\(VirtualGeometryHierarchyNode\[\], out int\[\]\)

groupのindexを、段(Level)の昇順(同じ段ではindexの昇順)に並べた配列と、各段の先頭の位置(長さ MaximumLevel+2。段 L は starts[L] から starts[L+1] の手前まで)。
GPUの階層選択は、段ごとに、その段のgroupだけを並列に処理する。

```csharp
public static uint[] SortByLevel(VirtualGeometryHierarchyNode[] nodes, out int[] starts)
```

#### 引数（Parameters）

`nodes` [VirtualGeometryHierarchyNode](VirtualizedGeometry.VirtualGeometryHierarchyNode.md)\[\]

`starts` [int](https://learn.microsoft.com/dotnet/api/system.int32)\[\]

#### 戻り値（Returns）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]
