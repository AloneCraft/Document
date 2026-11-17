# <a id="VirtualGeometry_Streaming_CubeGridMap"></a> Class CubeGridMap

Namespace: [VirtualGeometry.Streaming](VirtualGeometry.Streaming.md)  
Assembly: Omni.VirtualGeometry.Streaming.dll  

方向 → cube-sphere の面・Cell・格子の座標。Cell の格子点は面の上で等角(角度が格子の番号に比例)に並ぶ
(<xref href="VirtualGeometry.World.PlanetCellMeshBuilder.SpherePoint(VirtualGeometry.World.PlanetCellFrame%40%2cSystem.Int32%2cSystem.Double%2cSystem.Double%2cSystem.Double%2cSystem.Double%40%2cSystem.Double%40%2cSystem.Double%40%2cSystem.Double%40%2cSystem.Double%40%2cSystem.Double%40)" data-throw-if-not-resolved="false"></xref> と同じ規則)ので、方向の面座標の角度 atan(s)、atan(t) を [0, 1] に正規化して 2^level 倍する。

```csharp
public static class CubeGridMap
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[CubeGridMap](VirtualGeometry.Streaming.CubeGridMap.md)

## メソッド（Methods）

### <a id="VirtualGeometry_Streaming_CubeGridMap_DirectionFromCell_System_Int32_System_Int32_System_UInt32_System_UInt32_System_Double_System_Double_System_Double__System_Double__System_Double__"></a> DirectionFromCell\(int, int, uint, uint, double, double, out double, out double, out double\)

面 face・階層 level の Cell (cellX, cellY) の中の位置 (u, v)(Cell を 0〜1 とする。範囲の外も可: 隣の Cell、面の外側へ延ばした位置)の単位方向。
<xref href="VirtualGeometry.Streaming.CubeGridMap.TryExtendedGrid(System.Double%2cSystem.Double%2cSystem.Double%2cSystem.Int32%2cSystem.Int32%2cSystem.Int32%2cSystem.Double%40%2cSystem.Double%40)" data-throw-if-not-resolved="false"></xref> の逆(格子点が面の上で等角に並ぶ規則)。色のタイルを焼くときの画素の位置に使う。

```csharp
public static void DirectionFromCell(int face, int level, uint cellX, uint cellY, double u, double v, out double x, out double y, out double z)
```

#### 引数（Parameters）

`face` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`cellX` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`cellY` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`u` [double](https://learn.microsoft.com/dotnet/api/system.double)

`v` [double](https://learn.microsoft.com/dotnet/api/system.double)

`x` [double](https://learn.microsoft.com/dotnet/api/system.double)

`y` [double](https://learn.microsoft.com/dotnet/api/system.double)

`z` [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_Streaming_CubeGridMap_FacesNearestFirst_System_Double_System_Double_System_Double_System_Int32___"></a> FacesNearestFirst\(double, double, double, int\[\]\)

方向の前側にある面(dot が正)を、近い順に order へ書いて、その数を返す。面の境界・隅の近くの点は、外周 1 周が隣の面へ張り出すので、
元の面の座標(面の外側へ延ばした値)でも引けるよう、全部の候補を順に試す。

```csharp
public static int FacesNearestFirst(double x, double y, double z, int[] order)
```

#### 引数（Parameters）

`x` [double](https://learn.microsoft.com/dotnet/api/system.double)

`y` [double](https://learn.microsoft.com/dotnet/api/system.double)

`z` [double](https://learn.microsoft.com/dotnet/api/system.double)

`order` [int](https://learn.microsoft.com/dotnet/api/system.int32)\[\]

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_Streaming_CubeGridMap_FromDirection_System_Double_System_Double_System_Double_System_Int32_System_Int32_System_Int32__System_UInt32__System_UInt32__System_Double__System_Double__"></a> FromDirection\(double, double, double, int, int, out int, out uint, out uint, out double, out double\)

単位方向 (x, y, z) が階層 level で入る Cell(面・格子 X・Y)と、Cell 内の格子座標 (gu, gv)(0〜cellQuads、格子点の位置を 1 つ 1 とする)。
面の境界の点はどちらの面になってもよい(同じ高さの点)。

```csharp
public static void FromDirection(double x, double y, double z, int level, int cellQuads, out int face, out uint cellX, out uint cellY, out double gu, out double gv)
```

#### 引数（Parameters）

`x` [double](https://learn.microsoft.com/dotnet/api/system.double)

`y` [double](https://learn.microsoft.com/dotnet/api/system.double)

`z` [double](https://learn.microsoft.com/dotnet/api/system.double)

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`cellQuads` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`face` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`cellX` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`cellY` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`gu` [double](https://learn.microsoft.com/dotnet/api/system.double)

`gv` [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_Streaming_CubeGridMap_TryExtendedGrid_System_Double_System_Double_System_Double_System_Int32_System_Int32_System_Int32_System_Double__System_Double__"></a> TryExtendedGrid\(double, double, double, int, int, int, out double, out double\)

方向を指定した面の座標で表した、面の隅からの格子の距離(格子の間隔の単位。階層 level の面全体で 0〜2^level·cellQuads)。
面の外側(面の境界の少し向こう)の点は範囲の外(負、または全体より大きい値)になる。その面から見て後ろ側の方向は false。

```csharp
public static bool TryExtendedGrid(double x, double y, double z, int face, int level, int cellQuads, out double gridU, out double gridV)
```

#### 引数（Parameters）

`x` [double](https://learn.microsoft.com/dotnet/api/system.double)

`y` [double](https://learn.microsoft.com/dotnet/api/system.double)

`z` [double](https://learn.microsoft.com/dotnet/api/system.double)

`face` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`cellQuads` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`gridU` [double](https://learn.microsoft.com/dotnet/api/system.double)

`gridV` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
