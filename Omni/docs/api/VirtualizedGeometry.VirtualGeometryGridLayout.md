# <a id="VirtualizedGeometry_VirtualGeometryGridLayout"></a> Class VirtualGeometryGridLayout

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

実行時生成clusterの1 slot(cell)の頂点とclusterの配置。全slotが同じ配置を使い、index値はslot内の頂点番号。
頂点はgrid((N+1)×(N+1)、行優先 v=y*(N+1)+x)の後に、4辺のskirt(辺ごとにN+1個。辺0:y=0、1:x=N、2:y=N、3:x=0、辺に沿ってx・yの増える順)を置く。
clusterはM×M quadの格子で、cell境界に接するclusterは、その辺のskirt(両面)も含む。
供給元はgridのu(x方向)・v(y方向)を、外向き法線がcross(v,u)になる向きで置く(Unityの左手系で時計回りが表)。

```csharp
public sealed class VirtualGeometryGridLayout
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryGridLayout](VirtualizedGeometry.VirtualGeometryGridLayout.md)

## コンストラクター（Constructors）

### <a id="VirtualizedGeometry_VirtualGeometryGridLayout__ctor_System_Int32_System_Int32_"></a> VirtualGeometryGridLayout\(int, int\)

```csharp
public VirtualGeometryGridLayout(int cellQuads, int clusterQuads)
```

#### 引数（Parameters）

`cellQuads` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`clusterQuads` [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="VirtualizedGeometry_VirtualGeometryGridLayout_CellQuads"></a> CellQuads

```csharp
public int CellQuads { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryGridLayout_ClusterQuads"></a> ClusterQuads

```csharp
public int ClusterQuads { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryGridLayout_GridVertexCount"></a> GridVertexCount

```csharp
public int GridVertexCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryGridLayout_SlotClusterCount"></a> SlotClusterCount

```csharp
public int SlotClusterCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryGridLayout_SlotIndexCount"></a> SlotIndexCount

```csharp
public int SlotIndexCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryGridLayout_SlotVertexCount"></a> SlotVertexCount

```csharp
public int SlotVertexCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometryGridLayout_EdgeGrid_System_Int32_System_Int32_"></a> EdgeGrid\(int, int\)

辺edgeのt番目に対応するgrid頂点。

```csharp
public uint EdgeGrid(int edge, int t)
```

#### 引数（Parameters）

`edge` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`t` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualizedGeometry_VirtualGeometryGridLayout_Grid_System_Int32_System_Int32_"></a> Grid\(int, int\)

grid頂点(x,y)のslot内番号。

```csharp
public uint Grid(int x, int y)
```

#### 引数（Parameters）

`x` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`y` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualizedGeometry_VirtualGeometryGridLayout_Skirt_System_Int32_System_Int32_"></a> Skirt\(int, int\)

辺edgeのt番目のskirt頂点のslot内番号。

```csharp
public uint Skirt(int edge, int t)
```

#### 引数（Parameters）

`edge` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`t` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)
