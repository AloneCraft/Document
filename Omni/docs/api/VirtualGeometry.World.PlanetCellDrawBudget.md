# <a id="VirtualGeometry_World_PlanetCellDrawBudget"></a> Class PlanetCellDrawBudget

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

惑星・平面の Cell を VG で描くときの、選ぶ Cell の数の上限(<xref href="VirtualGeometry.World.PlanetCellSelector.MaximumSelectedCells" data-throw-if-not-resolved="false"></xref>)と、描画の容量の対応。
描く Cell は階層選択で簡略化されず(<xref href="VirtualGeometry.World.PlanarGridPage" data-throw-if-not-resolved="false"></xref>)、1 Cell が <xref href="VirtualGeometry.World.PlanarGridPage.IndicesPerCell" data-throw-if-not-resolved="false"></xref> 個の可視 index を要る。
描画の共有 buffer(<xref href="VirtualizedGeometry.VirtualGeometrySelectionBatch" data-throw-if-not-resolved="false"></xref>)の容量は固定で、超えた cluster は黙って捨てられ、画面に穴(背景の黒)が開く
(2026-10-23: 既定の容量 16 Mi index は約 607 Cell。Moon の TargetPixels 4 は 611 Cell で境界、3 は 930 Cell で約 5 %、2 は 1796 Cell で 36 % が欠けた)。
選択の上限と容量を別々に決めると、上限の方が大きいときに穴が開くので、ここで一緒に決める:
選択の上限から、選びうる Cell の数の最大(<xref href="VirtualGeometry.World.PlanetCellDrawBudget.MaximumSelectableCells(System.Int32%2cSystem.Int32)" data-throw-if-not-resolved="false"></xref>)を求め、描画の容量をそれ以上にする。
機器の上限(<xref href="VirtualGeometry.World.PlanetCellDrawBudget.VisibleIndexLimit" data-throw-if-not-resolved="false"></xref>)を超えるときは、描画の容量を上限にして、選択の上限を下げる(粗い親を描き続ける。穴にはしない)。

```csharp
public static class PlanetCellDrawBudget
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetCellDrawBudget](VirtualGeometry.World.PlanetCellDrawBudget.md)

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetCellDrawBudget_DesktopVisibleIndexLimit"></a> DesktopVisibleIndexLimit

WebGPU 以外の可視 index の容量の上限(index の数。256 Mi = 1 GiB)。

```csharp
public const int DesktopVisibleIndexLimit = 268435456
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetCellDrawBudget_ClampSelectionBudget_System_Int32_System_Int32_System_Int32_"></a> ClampSelectionBudget\(int, int, int\)

選択の上限を、描ける Cell の数(<xref href="VirtualGeometry.World.PlanetCellDrawBudget.MaximumDrawableCells(System.Int32%2cVirtualizedGeometry.VirtualGeometryGridLayout)" data-throw-if-not-resolved="false"></xref>)に収まる最大の値に下げる(収まっていれば selectionBudget のまま)。最小は 16。

```csharp
public static int ClampSelectionBudget(int selectionBudget, int visibleIndexLimit, int contactCells = 0)
```

#### 引数（Parameters）

`selectionBudget` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`visibleIndexLimit` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`contactCells` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetCellDrawBudget_MaximumDrawableCells_System_Int32_"></a> MaximumDrawableCells\(int\)

1 回に描ける Cell の数の上限(可視 index の容量 visibleIndexLimit と、可視 cluster の一覧の容量から)。

```csharp
public static int MaximumDrawableCells(int visibleIndexLimit)
```

#### 引数（Parameters）

`visibleIndexLimit` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetCellDrawBudget_MaximumSelectableCells_System_Int32_System_Int32_"></a> MaximumSelectableCells\(int, int\)

選択の上限 selectionBudget のとき、1 回の選択が選びうる Cell の数の最大。細分化の本体は上限、バランスの補正は上限の 1.25 倍まで、
接地の領域の Cell(contactCells 個。上限の対象外。精度の約束のため)はその外。

```csharp
public static int MaximumSelectableCells(int selectionBudget, int contactCells = 0)
```

#### 引数（Parameters）

`selectionBudget` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`contactCells` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetCellDrawBudget_RequiredVisibleIndices_System_Int32_System_Int32_"></a> RequiredVisibleIndices\(int, int\)

選択の上限 selectionBudget の選択を、穴なく描くのに要る可視 index の容量(int の上限で打ち切る)。

```csharp
public static int RequiredVisibleIndices(int selectionBudget, int contactCells = 0)
```

#### 引数（Parameters）

`selectionBudget` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`contactCells` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetCellDrawBudget_VisibleIndexLimit"></a> VisibleIndexLimit\(\)

この機器で使える可視 index の容量の上限(index の数)。

```csharp
public static int VisibleIndexLimit()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetCellDrawBudget_VisibleIndicesFor_System_Int64_"></a> VisibleIndicesFor\(long\)

cells 個の Cell を全部描くのに要る可視 index の数。

```csharp
public static long VisibleIndicesFor(long cells)
```

#### 引数（Parameters）

`cells` [long](https://learn.microsoft.com/dotnet/api/system.int64)

#### 戻り値（Returns）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)
