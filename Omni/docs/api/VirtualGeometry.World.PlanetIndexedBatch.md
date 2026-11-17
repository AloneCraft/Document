# <a id="VirtualGeometry_World_PlanetIndexedBatch"></a> Class PlanetIndexedBatch

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

1 Camera・1 Layerの共有index描画資源。頂点poolとcluster boundsはLayerから借り、この所有者は解放しない。
RenderGraphへは同じbufferを1回だけimportし、cull書込み→draw読取りの依存を明示する必要がある。

```csharp
public sealed class PlanetIndexedBatch : IDisposable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetIndexedBatch](VirtualGeometry.World.PlanetIndexedBatch.md)

#### 実装するインターフェース（Implements）

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetIndexedBatch__ctor_System_Int32_System_Int32_System_Int32_System_Int64_"></a> PlanetIndexedBatch\(int, int, int, long\)

```csharp
public PlanetIndexedBatch(int n, int poolCapacity, int selectedCapacity, long maximumStorageBufferBytes)
```

#### 引数（Parameters）

`n` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`poolCapacity` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`selectedCapacity` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`maximumStorageBufferBytes` [long](https://learn.microsoft.com/dotnet/api/system.int64)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetIndexedBatch_Arguments"></a> Arguments

```csharp
public GraphicsBuffer Arguments { get; }
```

#### 値（Property Value）

 GraphicsBuffer

### <a id="VirtualGeometry_World_PlanetIndexedBatch_CellRecords"></a> CellRecords

```csharp
public GraphicsBuffer CellRecords { get; }
```

#### 値（Property Value）

 GraphicsBuffer

### <a id="VirtualGeometry_World_PlanetIndexedBatch_CollectDrawDiagnostics"></a> CollectDrawDiagnostics

診断を明示指定したForward batchだけが読む。prepassは有効にしない。

```csharp
public bool CollectDrawDiagnostics { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetIndexedBatch_DrawDiagnosticsError"></a> DrawDiagnosticsError

空なら直近の読取りに失敗なし。古い成功sampleのframeは更新しない。

```csharp
public string DrawDiagnosticsError { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualGeometry_World_PlanetIndexedBatch_DummyTerrainStorage"></a> DummyTerrainStorage

```csharp
public GraphicsBuffer DummyTerrainStorage { get; }
```

#### 値（Property Value）

 GraphicsBuffer

### <a id="VirtualGeometry_World_PlanetIndexedBatch_DummyTerrainWords"></a> DummyTerrainWords

```csharp
public GraphicsBuffer DummyTerrainWords { get; }
```

#### 値（Property Value）

 GraphicsBuffer

### <a id="VirtualGeometry_World_PlanetIndexedBatch_GridIndices"></a> GridIndices

```csharp
public GraphicsBuffer GridIndices { get; }
```

#### 値（Property Value）

 GraphicsBuffer

### <a id="VirtualGeometry_World_PlanetIndexedBatch_LastDrawDiagnostics"></a> LastDrawDiagnostics

```csharp
public PlanetIndexedDrawDiagnostics LastDrawDiagnostics { get; }
```

#### 値（Property Value）

 [PlanetIndexedDrawDiagnostics](VirtualGeometry.World.PlanetIndexedDrawDiagnostics.md)

### <a id="VirtualGeometry_World_PlanetIndexedBatch_OwnedBufferBytes"></a> OwnedBufferBytes

```csharp
public long OwnedBufferBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualGeometry_World_PlanetIndexedBatch_PoolCapacity"></a> PoolCapacity

```csharp
public int PoolCapacity { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetIndexedBatch_SelectedCapacity"></a> SelectedCapacity

```csharp
public int SelectedCapacity { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetIndexedBatch_SelectedCount"></a> SelectedCount

```csharp
public int SelectedCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetIndexedBatch_SelectedSlots"></a> SelectedSlots

```csharp
public GraphicsBuffer SelectedSlots { get; }
```

#### 値（Property Value）

 GraphicsBuffer

### <a id="VirtualGeometry_World_PlanetIndexedBatch_SkirtIndices"></a> SkirtIndices

```csharp
public GraphicsBuffer SkirtIndices { get; }
```

#### 値（Property Value）

 GraphicsBuffer

### <a id="VirtualGeometry_World_PlanetIndexedBatch_SkirtVisibleBase"></a> SkirtVisibleBase

```csharp
public int SkirtVisibleBase { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetIndexedBatch_Topology"></a> Topology

```csharp
public PlanetClusterTopology Topology { get; }
```

#### 値（Property Value）

 [PlanetClusterTopology](VirtualGeometry.World.PlanetClusterTopology.md)

### <a id="VirtualGeometry_World_PlanetIndexedBatch_VisibleClusters"></a> VisibleClusters

```csharp
public GraphicsBuffer VisibleClusters { get; }
```

#### 値（Property Value）

 GraphicsBuffer

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetIndexedBatch_Dispose"></a> Dispose\(\)

```csharp
public void Dispose()
```

### <a id="VirtualGeometry_World_PlanetIndexedBatch_MaximumSelectedCells_System_Int32_System_Int64_"></a> MaximumSelectedCells\(int, long\)

単一bindingの上限。頂点pool等の別の制約と合わせて、選択側の上限を決める。

```csharp
public static int MaximumSelectedCells(int n, long maximumStorageBufferBytes)
```

#### 引数（Parameters）

`n` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`maximumStorageBufferBytes` [long](https://learn.microsoft.com/dotnet/api/system.int64)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetIndexedBatch_Upload_System_Int32___System_Int32_VirtualGeometry_World_PlanetClusterRecord___"></a> Upload\(int\[\], int, PlanetClusterRecord\[\]\)

Graph記録前の入力転送。重複slotは候補数の上限保証を壊すため拒否する。

```csharp
public void Upload(int[] selected, int count, PlanetClusterRecord[] records)
```

#### 引数（Parameters）

`selected` [int](https://learn.microsoft.com/dotnet/api/system.int32)\[\]

`count` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`records` [PlanetClusterRecord](VirtualGeometry.World.PlanetClusterRecord.md)\[\]

### <a id="VirtualGeometry_World_PlanetIndexedBatch_UploadFrom_VirtualGeometry_World_PlanetIndexedBatch_"></a> UploadFrom\(PlanetIndexedBatch\)

prepass等の独立bufferへ同じ確定済み入力を送る。重複検査/gatherを二度行わず、GPU書込み先は共有しない。

```csharp
public void UploadFrom(PlanetIndexedBatch source)
```

#### 引数（Parameters）

`source` [PlanetIndexedBatch](VirtualGeometry.World.PlanetIndexedBatch.md)
