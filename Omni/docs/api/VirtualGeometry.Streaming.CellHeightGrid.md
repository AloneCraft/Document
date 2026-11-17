# <a id="VirtualGeometry_Streaming_CellHeightGrid"></a> Class CellHeightGrid

Namespace: [VirtualGeometry.Streaming](VirtualGeometry.Streaming.md)  
Assembly: Omni.VirtualGeometry.Streaming.dll  

Cell の格子の高さ(外の 1 周を含む side×side、<xref href="VirtualGeometry.World.PlanetCellMeshBuilder.RingSide" data-throw-if-not-resolved="false"></xref>)を、共通の固定量子化(step メートル刻みの int16)で
持つ展開済みの中身。隣り合う Cell の共有する格子点は同じ高さ(同じ整数)になるので、継ぎ目で割れない。

```csharp
public sealed class CellHeightGrid : IDecodedPayload, IDisposable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[CellHeightGrid](VirtualGeometry.Streaming.CellHeightGrid.md)

#### 実装するインターフェース（Implements）

[IDecodedPayload](Omni.Streaming.IDecodedPayload.md), 
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_Streaming_CellHeightGrid__ctor_System_Int32_System_Single_System_Int16___System_Int16___"></a> CellHeightGrid\(int, float, short\[\], short\[\]\)

```csharp
public CellHeightGrid(int side, float step, short[] heights, short[] shading)
```

#### 引数（Parameters）

`side` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`step` [float](https://learn.microsoft.com/dotnet/api/system.single)

`heights` [short](https://learn.microsoft.com/dotnet/api/system.int16)\[\]

`shading` [short](https://learn.microsoft.com/dotnet/api/system.int16)\[\]

## フィールド（Fields）

### <a id="VirtualGeometry_Streaming_CellHeightGrid_Heights"></a> Heights

```csharp
public readonly short[] Heights
```

#### 値（Field Value）

 [short](https://learn.microsoft.com/dotnet/api/system.int16)\[\]

### <a id="VirtualGeometry_Streaming_CellHeightGrid_Shading"></a> Shading

法線に使う別の高さ(無ければ null)。

```csharp
public readonly short[] Shading
```

#### 値（Field Value）

 [short](https://learn.microsoft.com/dotnet/api/system.int16)\[\]

### <a id="VirtualGeometry_Streaming_CellHeightGrid_Side"></a> Side

```csharp
public readonly int Side
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_Streaming_CellHeightGrid_Step"></a> Step

```csharp
public readonly float Step
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

## プロパティ（Properties）

### <a id="VirtualGeometry_Streaming_CellHeightGrid_ByteSize"></a> ByteSize

```csharp
public long ByteSize { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualGeometry_Streaming_CellHeightGrid_HasShading"></a> HasShading

```csharp
public bool HasShading { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="VirtualGeometry_Streaming_CellHeightGrid_CopyTo_System_Double___System_Double___"></a> CopyTo\(double\[\], double\[\]\)

メートルの高さへ戻して配列に書く(shading は、持たなければ書かない)。

```csharp
public void CopyTo(double[] heights, double[] shading)
```

#### 引数（Parameters）

`heights` [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]

`shading` [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]

### <a id="VirtualGeometry_Streaming_CellHeightGrid_Dispose"></a> Dispose\(\)

```csharp
public void Dispose()
```
