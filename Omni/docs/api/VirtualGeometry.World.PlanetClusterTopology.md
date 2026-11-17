# <a id="VirtualGeometry_World_PlanetClusterTopology"></a> Class PlanetClusterTopology

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

8×8格子と8 quadの両面skirtを、共有indexからCellの頂点配置へ写すCPU参照。

```csharp
public sealed class PlanetClusterTopology
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetClusterTopology](VirtualGeometry.World.PlanetClusterTopology.md)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetClusterTopology__ctor_System_Int32_"></a> PlanetClusterTopology\(int\)

```csharp
public PlanetClusterTopology(int cellQuads)
```

#### 引数（Parameters）

`cellQuads` [int](https://learn.microsoft.com/dotnet/api/system.int32)

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetClusterTopology_ClusterQuads"></a> ClusterQuads

```csharp
public const int ClusterQuads = 8
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetClusterTopology_GridIndexCount"></a> GridIndexCount

```csharp
public const int GridIndexCount = 384
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetClusterTopology_GridVertices"></a> GridVertices

```csharp
public const int GridVertices = 81
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetClusterTopology_SkirtIndexCount"></a> SkirtIndexCount

```csharp
public const int SkirtIndexCount = 96
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetClusterTopology_SkirtVertices"></a> SkirtVertices

```csharp
public const int SkirtVertices = 18
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetClusterTopology_CellQuads"></a> CellQuads

```csharp
public int CellQuads { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetClusterTopology_ClusterCount"></a> ClusterCount

```csharp
public int ClusterCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetClusterTopology_ClustersPerSide"></a> ClustersPerSide

```csharp
public int ClustersPerSide { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetClusterTopology_GridClusterCount"></a> GridClusterCount

```csharp
public int GridClusterCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetClusterTopology_SlotVertexCount"></a> SlotVertexCount

```csharp
public int SlotVertexCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetClusterTopology_CreateGridIndices"></a> CreateGridIndices\(\)

```csharp
public static ushort[] CreateGridIndices()
```

#### 戻り値（Returns）

 [ushort](https://learn.microsoft.com/dotnet/api/system.uint16)\[\]

### <a id="VirtualGeometry_World_PlanetClusterTopology_CreateSkirtIndices"></a> CreateSkirtIndices\(\)

```csharp
public static ushort[] CreateSkirtIndices()
```

#### 戻り値（Returns）

 [ushort](https://learn.microsoft.com/dotnet/api/system.uint16)\[\]

### <a id="VirtualGeometry_World_PlanetClusterTopology_SlotVertex_System_Int32_System_UInt32_"></a> SlotVertex\(int, uint\)

PlanarGridPageと同じ並び。格子が先、続いて辺0〜3のskirt。

```csharp
public uint SlotVertex(int cluster, uint localVertex)
```

#### 引数（Parameters）

`cluster` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`localVertex` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

#### 戻り値（Returns）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)
