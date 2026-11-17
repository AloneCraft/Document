# <a id="VirtualGeometry_World_PlanetCellMeshBuilder"></a> Class PlanetCellMeshBuilder

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

惑星の Cell 1 つ分の頂点(<xref href="VirtualizedGeometry.VirtualGeometryGridLayout" data-throw-if-not-resolved="false"></xref> の配置)を、高さの正本(<xref href="VirtualGeometry.World.IPlanetHeightProvider" data-throw-if-not-resolved="false"></xref>)から CPU で作る。
GPU は作った頂点をそのまま写すので、描く頂点と CPU の配列(接地の問い合わせ <xref href="VirtualGeometry.World.PlanetTerrainContact" data-throw-if-not-resolved="false"></xref> が使う)は bit 単位で同じになる。
位置は Cell の原点(<xref href="VirtualGeometry.World.PlanetCellFrame.Origin" data-throw-if-not-resolved="false"></xref>、Logical)からの相対位置で、double で求めてから float にする:
球面上の点は、中心の正接(Logical から double)と格子の角度の差から R·(p/|p| − p0/|p0|) を差だけで求め(大きな値どうしを引かない)、
高さ h と原点の持ち上げ H を足して sphere + h·n − H·u0(n は頂点の方向、u0 は Cell の中心の方向)にする。
誤差は R·2^-52 程度(月で 4×10^-10 m、地球で 1.4×10^-9 m)で、R が 10^9 m を超える天体には向かない(GPU 生成の Layer を使う)。
法線は格子の外の 1 周を含めた中心差分。陰影用の高さを持つ供給元(<xref href="VirtualGeometry.World.IPlanetShadingHeightProvider" data-throw-if-not-resolved="false"></xref>)は、その高さで法線を求める。
高さの入口は 2 つ: <xref href="VirtualGeometry.World.PlanetCellMeshBuilder.Build(VirtualGeometry.World.PlanetCellFrame%40%2cSystem.Double%2cVirtualGeometry.World.IPlanetHeightProvider%2cSystem.Double%2cSystem.Single%2cUnityEngine.Vector4%2cVirtualizedGeometry.VirtualGeometryPackedVertex%5b%5d%2cSystem.Int32%2cUnityEngine.Vector4%40%2cSystem.Double%40%2cSystem.Double%40%2cSystem.Threading.CancellationToken)" data-throw-if-not-resolved="false"></xref>(供給元を格子の各点でサンプルする)と <xref href="VirtualGeometry.World.PlanetCellMeshBuilder.BuildFromHeights(VirtualGeometry.World.PlanetCellFrame%40%2cSystem.Double%2cSystem.ReadOnlySpan%7bSystem.Double%7d%2cSystem.ReadOnlySpan%7bSystem.Double%7d%2cSystem.Single%2cUnityEngine.Vector4%2cVirtualizedGeometry.VirtualGeometryPackedVertex%5b%5d%2cSystem.Int32%2cUnityEngine.Vector4%40%2cSystem.Double%40%2cSystem.Double%40)" data-throw-if-not-resolved="false"></xref>(格子の各点の高さを配列で受け取る。
ストリーミングで届いた高さ、焼いた高さなど)。同じ高さを渡せば、2 つの結果は bit 単位で一致する。

```csharp
public sealed class PlanetCellMeshBuilder
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetCellMeshBuilder](VirtualGeometry.World.PlanetCellMeshBuilder.md)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetCellMeshBuilder__ctor_System_Int32_"></a> PlanetCellMeshBuilder\(int\)

```csharp
public PlanetCellMeshBuilder(int cellQuads)
```

#### 引数（Parameters）

`cellQuads` [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetCellMeshBuilder_CellQuads"></a> CellQuads

```csharp
public int CellQuads { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetCellMeshBuilder_LastAssembleTicks"></a> LastAssembleTicks

```csharp
public long LastAssembleTicks { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualGeometry_World_PlanetCellMeshBuilder_LastGridTicks"></a> LastGridTicks

```csharp
public long LastGridTicks { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualGeometry_World_PlanetCellMeshBuilder_LastSampleTicks"></a> LastSampleTicks

```csharp
public long LastSampleTicks { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualGeometry_World_PlanetCellMeshBuilder_LastSamples"></a> LastSamples

直近の <xref href="VirtualGeometry.World.PlanetCellMeshBuilder.Build(VirtualGeometry.World.PlanetCellFrame%40%2cSystem.Double%2cVirtualGeometry.World.IPlanetHeightProvider%2cSystem.Double%2cSystem.Single%2cUnityEngine.Vector4%2cVirtualizedGeometry.VirtualGeometryPackedVertex%5b%5d%2cSystem.Int32%2cUnityEngine.Vector4%40%2cSystem.Double%40%2cSystem.Double%40%2cSystem.Threading.CancellationToken)" data-throw-if-not-resolved="false"></xref> が求めた高さの数(診断用)。

```csharp
public int LastSamples { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetCellMeshBuilder_MeasureTimings"></a> MeasureTimings

計測専用。高さサンプルと純粋な格子/組立の時間を混ぜない。

```csharp
public bool MeasureTimings { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetCellMeshBuilder_RingSide"></a> RingSide

格子の1辺の点の数(外の 1 周を含む、cellQuads+3)。<xref href="VirtualGeometry.World.PlanetCellMeshBuilder.BuildFromHeights(VirtualGeometry.World.PlanetCellFrame%40%2cSystem.Double%2cSystem.ReadOnlySpan%7bSystem.Double%7d%2cSystem.ReadOnlySpan%7bSystem.Double%7d%2cSystem.Single%2cUnityEngine.Vector4%2cVirtualizedGeometry.VirtualGeometryPackedVertex%5b%5d%2cSystem.Int32%2cUnityEngine.Vector4%40%2cSystem.Double%40%2cSystem.Double%40)" data-throw-if-not-resolved="false"></xref> の高さの配列は RingSide² 個(行 j、列 i の順に j·RingSide+i)。

```csharp
public int RingSide { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetCellMeshBuilder_SlotVertexCount"></a> SlotVertexCount

1 Cell の頂点数(grid と 4 辺の skirt)。

```csharp
public int SlotVertexCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetCellMeshBuilder_UsePreparedSampling"></a> UsePreparedSampling

```csharp
public bool UsePreparedSampling { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetCellMeshBuilder_Build_VirtualGeometry_World_PlanetCellFrame__System_Double_VirtualGeometry_World_IPlanetHeightProvider_System_Double_System_Single_UnityEngine_Vector4_VirtualizedGeometry_VirtualGeometryPackedVertex___System_Int32_UnityEngine_Vector4__System_Double__System_Double__System_Threading_CancellationToken_"></a> Build\(in PlanetCellFrame, double, IPlanetHeightProvider, double, float, Vector4, VirtualGeometryPackedVertex\[\], int, out Vector4, out double, out double, CancellationToken\)

Cell の頂点を vertices[offset..offset+<xref href="VirtualGeometry.World.PlanetCellMeshBuilder.SlotVertexCount" data-throw-if-not-resolved="false"></xref>) に書く。spacing は帯域制限に使うメッシュの間隔(この階層の quad の弧長)。
skirtDepth は 4 辺の skirt を下げる距離、faceRange は UV。bounds は Cell の原点からの中心 xyz と半径 w。
高さが有限でなければ false(その Cell は描かない)。

```csharp
public bool Build(in PlanetCellFrame frame, double radius, IPlanetHeightProvider heights, double spacing, float skirtDepth, Vector4 faceRange, VirtualGeometryPackedVertex[] vertices, int offset, out Vector4 bounds, out double minimumHeight, out double maximumHeight, CancellationToken cancellation = default)
```

#### 引数（Parameters）

`frame` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

`radius` [double](https://learn.microsoft.com/dotnet/api/system.double)

`heights` [IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

`spacing` [double](https://learn.microsoft.com/dotnet/api/system.double)

`skirtDepth` [float](https://learn.microsoft.com/dotnet/api/system.single)

`faceRange` Vector4

`vertices` [VirtualGeometryPackedVertex](VirtualizedGeometry.VirtualGeometryPackedVertex.md)\[\]

`offset` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`bounds` Vector4

`minimumHeight` [double](https://learn.microsoft.com/dotnet/api/system.double)

`maximumHeight` [double](https://learn.microsoft.com/dotnet/api/system.double)

`cancellation` [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetCellMeshBuilder_BuildFromHeights_VirtualGeometry_World_PlanetCellFrame__System_Double_System_ReadOnlySpan_System_Double__System_ReadOnlySpan_System_Double__System_Single_UnityEngine_Vector4_VirtualizedGeometry_VirtualGeometryPackedVertex___System_Int32_UnityEngine_Vector4__System_Double__System_Double__"></a> BuildFromHeights\(in PlanetCellFrame, double, ReadOnlySpan<double\>, ReadOnlySpan<double\>, float, Vector4, VirtualGeometryPackedVertex\[\], int, out Vector4, out double, out double\)

<xref href="VirtualGeometry.World.PlanetCellMeshBuilder.Build(VirtualGeometry.World.PlanetCellFrame%40%2cSystem.Double%2cVirtualGeometry.World.IPlanetHeightProvider%2cSystem.Double%2cSystem.Single%2cUnityEngine.Vector4%2cVirtualizedGeometry.VirtualGeometryPackedVertex%5b%5d%2cSystem.Int32%2cUnityEngine.Vector4%40%2cSystem.Double%40%2cSystem.Double%40%2cSystem.Threading.CancellationToken)" data-throw-if-not-resolved="false"></xref> と同じ頂点を、格子の各点の高さを配列で受け取って作る。heights は RingSide² 個(行 j、列 i の順に j·RingSide+i。
点の方向は <xref href="VirtualGeometry.World.PlanetCellMeshBuilder.GridDirections(VirtualGeometry.World.PlanetCellFrame%40%2cSystem.Double%2cSystem.Double%5b%5d%2cSystem.Double%5b%5d%2cSystem.Double%5b%5d)" data-throw-if-not-resolved="false"></xref> と同じ)。shadingHeights は法線に使う別の高さ(空なら heights で法線を求める)。
高さが有限でなければ false。

```csharp
public bool BuildFromHeights(in PlanetCellFrame frame, double radius, ReadOnlySpan<double> heights, ReadOnlySpan<double> shadingHeights, float skirtDepth, Vector4 faceRange, VirtualGeometryPackedVertex[] vertices, int offset, out Vector4 bounds, out double minimumHeight, out double maximumHeight)
```

#### 引数（Parameters）

`frame` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

`radius` [double](https://learn.microsoft.com/dotnet/api/system.double)

`heights` [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[double](https://learn.microsoft.com/dotnet/api/system.double)\>

`shadingHeights` [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[double](https://learn.microsoft.com/dotnet/api/system.double)\>

`skirtDepth` [float](https://learn.microsoft.com/dotnet/api/system.single)

`faceRange` Vector4

`vertices` [VirtualGeometryPackedVertex](VirtualizedGeometry.VirtualGeometryPackedVertex.md)\[\]

`offset` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`bounds` Vector4

`minimumHeight` [double](https://learn.microsoft.com/dotnet/api/system.double)

`maximumHeight` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetCellMeshBuilder_CenterDirection_VirtualGeometry_World_PlanetCellFrame__System_Double__System_Double__System_Double__"></a> CenterDirection\(in PlanetCellFrame, out double, out double, out double\)

Cell の中心の外向きの単位方向(double)。

```csharp
public static void CenterDirection(in PlanetCellFrame frame, out double x, out double y, out double z)
```

#### 引数（Parameters）

`frame` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

`x` [double](https://learn.microsoft.com/dotnet/api/system.double)

`y` [double](https://learn.microsoft.com/dotnet/api/system.double)

`z` [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetCellMeshBuilder_CenterHeight_VirtualGeometry_World_PlanetCellFrame__VirtualGeometry_World_IPlanetHeightProvider_System_Double_"></a> CenterHeight\(in PlanetCellFrame, IPlanetHeightProvider, double\)

Cell の中心の方向の地表の高さ(帯域制限あり)。原点を持ち上げる高さの判定に使う。

```csharp
public static double CenterHeight(in PlanetCellFrame frame, IPlanetHeightProvider heights, double spacing)
```

#### 引数（Parameters）

`frame` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

`heights` [IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

`spacing` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetCellMeshBuilder_GridDirections_VirtualGeometry_World_PlanetCellFrame__System_Double_System_Double___System_Double___System_Double___"></a> GridDirections\(in PlanetCellFrame, double, double\[\], double\[\], double\[\]\)

Cell の格子(外の 1 周を含む RingSide²)の各点の単位方向を x・y・z に書く(<xref href="VirtualGeometry.World.PlanetCellMeshBuilder.Build(VirtualGeometry.World.PlanetCellFrame%40%2cSystem.Double%2cVirtualGeometry.World.IPlanetHeightProvider%2cSystem.Double%2cSystem.Single%2cUnityEngine.Vector4%2cVirtualizedGeometry.VirtualGeometryPackedVertex%5b%5d%2cSystem.Int32%2cUnityEngine.Vector4%40%2cSystem.Double%40%2cSystem.Double%40%2cSystem.Threading.CancellationToken)" data-throw-if-not-resolved="false"></xref> が高さを問い合わせる方向と同じ値)。
高さを焼く側が、実行時と同じ点で高さを求めるために使う。

```csharp
public void GridDirections(in PlanetCellFrame frame, double radius, double[] x, double[] y, double[] z)
```

#### 引数（Parameters）

`frame` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

`radius` [double](https://learn.microsoft.com/dotnet/api/system.double)

`x` [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]

`y` [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]

`z` [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]

### <a id="VirtualGeometry_World_PlanetCellMeshBuilder_PrepareNativeInputs_VirtualGeometry_World_PlanetCellFrame__System_Double_VirtualGeometry_World_IPlanetHeightProvider_System_Double_System_Threading_CancellationToken_"></a> PrepareNativeInputs\(in PlanetCellFrame, double, IPlanetHeightProvider, double, CancellationToken\)

managed供給元の基底だけをworkerで取得し、noiseと組立の数値計算をJobへ渡す。

```csharp
public PlanetNativeHeightInputs PrepareNativeInputs(in PlanetCellFrame frame, double radius, IPlanetHeightProvider heights, double spacing, CancellationToken cancellation = default)
```

#### 引数（Parameters）

`frame` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

`radius` [double](https://learn.microsoft.com/dotnet/api/system.double)

`heights` [IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

`spacing` [double](https://learn.microsoft.com/dotnet/api/system.double)

`cancellation` [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)

#### 戻り値（Returns）

 [PlanetNativeHeightInputs](VirtualGeometry.World.PlanetNativeHeightInputs.md)

### <a id="VirtualGeometry_World_PlanetCellMeshBuilder_SpherePoint_VirtualGeometry_World_PlanetCellFrame__System_Int32_System_Double_System_Double_System_Double_System_Double__System_Double__System_Double__System_Double__System_Double__System_Double__"></a> SpherePoint\(in PlanetCellFrame, int, double, double, double, out double, out double, out double, out double, out double, out double\)

Cell の格子の (a, b)(−1〜N+1)の、半径 R の球面上の点の、球面上の原点(<xref href="VirtualGeometry.World.PlanetCellFrame.SphereOrigin" data-throw-if-not-resolved="false"></xref>)からの相対位置と単位方向(double)。

```csharp
public static void SpherePoint(in PlanetCellFrame frame, int cellQuads, double radius, double a, double b, out double rx, out double ry, out double rz, out double dirX, out double dirY, out double dirZ)
```

#### 引数（Parameters）

`frame` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

`cellQuads` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`radius` [double](https://learn.microsoft.com/dotnet/api/system.double)

`a` [double](https://learn.microsoft.com/dotnet/api/system.double)

`b` [double](https://learn.microsoft.com/dotnet/api/system.double)

`rx` [double](https://learn.microsoft.com/dotnet/api/system.double)

`ry` [double](https://learn.microsoft.com/dotnet/api/system.double)

`rz` [double](https://learn.microsoft.com/dotnet/api/system.double)

`dirX` [double](https://learn.microsoft.com/dotnet/api/system.double)

`dirY` [double](https://learn.microsoft.com/dotnet/api/system.double)

`dirZ` [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetCellMeshBuilder_TangentOffset_System_Double_System_Double_"></a> TangentOffset\(double, double\)

tan(a0+δ)−tan(a0) を、tan(a0)=x0 と δ から差だけで求める(double)。

```csharp
public static double TangentOffset(double x0, double delta)
```

#### 引数（Parameters）

`x0` [double](https://learn.microsoft.com/dotnet/api/system.double)

`delta` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)
