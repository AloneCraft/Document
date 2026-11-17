# <a id="VirtualGeometry_Streaming_StreamedTerrainConnector"></a> Class StreamedTerrainConnector

Namespace: [VirtualGeometry.Streaming](VirtualGeometry.Streaming.md)  
Assembly: Omni.VirtualGeometry.Streaming.dll  

<xref href="VirtualGeometry.World.PlanetHeightTerrainSource" data-throw-if-not-resolved="false"></xref> に <xref href="VirtualGeometry.Streaming.StreamedCellHeightSource" data-throw-if-not-resolved="false"></xref> を接続し、描画の後に関心を宣言する。
host の組み立てと Tick(<code>Omni.Streaming.Unity.StreamingBehaviour</code>)は利用者が行う。
Edit Mode でも動く(Scene に保存されず、利用者が足して接続したときだけ関心を宣言する)。

```csharp
[DefaultExecutionOrder(100)]
[ExecuteAlways]
public sealed class StreamedTerrainConnector : MonoBehaviour
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[StreamedTerrainConnector](VirtualGeometry.Streaming.StreamedTerrainConnector.md)

## プロパティ（Properties）

### <a id="VirtualGeometry_Streaming_StreamedTerrainConnector_Source"></a> Source

```csharp
public StreamedCellHeightSource Source { get; }
```

#### 値（Property Value）

 [StreamedCellHeightSource](VirtualGeometry.Streaming.StreamedCellHeightSource.md)

### <a id="VirtualGeometry_Streaming_StreamedTerrainConnector_Tiles"></a> Tiles

色のタイルの供給元(<xref href="VirtualGeometry.Streaming.StreamedTerrainConnector.ConnectTiles(Omni.Streaming.StreamingHost%2cSystem.UInt32%2cSystem.Int32%2cVirtualGeometry.Streaming.CellTileCache%2cSystem.Int32)" data-throw-if-not-resolved="false"></xref> の後)。

```csharp
public StreamedCellTileSource Tiles { get; }
```

#### 値（Property Value）

 [StreamedCellTileSource](VirtualGeometry.Streaming.StreamedCellTileSource.md)

## メソッド（Methods）

### <a id="VirtualGeometry_Streaming_StreamedTerrainConnector_Connect_VirtualGeometry_World_PlanetHeightTerrainSource_Omni_Streaming_StreamingHost_System_UInt32_System_Int32_"></a> Connect\(PlanetHeightTerrainSource, StreamingHost, uint, int\)

```csharp
public void Connect(PlanetHeightTerrainSource terrain, StreamingHost host, uint layer, int maximumLevel)
```

#### 引数（Parameters）

`terrain` PlanetHeightTerrainSource

`host` [StreamingHost](Omni.Streaming.StreamingHost.md)

`layer` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`maximumLevel` [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_Streaming_StreamedTerrainConnector_Connect_Omni_Streaming_StreamingHost_System_UInt32_System_Int32_"></a> Connect\(StreamingHost, uint, int\)

Moon(汎用版)の汎用mesh供給元へ、Surfaceを生成せず同じ高さstreamを接続する。

```csharp
public void Connect(StreamingHost host, uint layer, int maximumLevel)
```

#### 引数（Parameters）

`host` [StreamingHost](Omni.Streaming.StreamingHost.md)

`layer` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`maximumLevel` [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_Streaming_StreamedTerrainConnector_ConnectTiles_Omni_Streaming_StreamingHost_System_UInt32_System_Int32_VirtualGeometry_Streaming_CellTileCache_System_Int32_"></a> ConnectTiles\(StreamingHost, uint, int, CellTileCache, int\)

Cell ごとの色のタイルを接続する(<xref href="VirtualGeometry.Streaming.StreamedTerrainConnector.Connect(VirtualGeometry.World.PlanetHeightTerrainSource%2cOmni.Streaming.StreamingHost%2cSystem.UInt32%2cSystem.Int32)" data-throw-if-not-resolved="false"></xref> の後)。タイルは cache の slice に置かれ、cache の Texture2DArray が shader の global になる想定。

```csharp
public StreamedCellTileSource ConnectTiles(StreamingHost host, uint layer, int maximumLevel, CellTileCache cache, int border)
```

#### 引数（Parameters）

`host` [StreamingHost](Omni.Streaming.StreamingHost.md)

`layer` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`maximumLevel` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`cache` [CellTileCache](VirtualGeometry.Streaming.CellTileCache.md)

`border` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [StreamedCellTileSource](VirtualGeometry.Streaming.StreamedCellTileSource.md)

### <a id="VirtualGeometry_Streaming_StreamedTerrainConnector_Disconnect"></a> Disconnect\(\)

```csharp
public void Disconnect()
```
