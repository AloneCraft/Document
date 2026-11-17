# <a id="VirtualGeometry_Streaming_CellTileCache"></a> Class CellTileCache

Namespace: [VirtualGeometry.Streaming](VirtualGeometry.Streaming.md)  
Assembly: Omni.VirtualGeometry.Streaming.dll  

届いた画像タイル(<xref href="Omni.Streaming.Formats.ImageTile" data-throw-if-not-resolved="false"></xref>)を GPU の <xref href="UnityEngine.Texture2DArray" data-throw-if-not-resolved="false"></xref> の slice に置くキャッシュ。slice は最近使った順(frame の番号)で再利用する。
GPU が BC1 を使えるときは BC1 のまま置き(展開しない)、使えないときは RGBA32 へ展開して置く。mip は持たない
(Cell は画面の密度に合わせて選ばれるので、タイルは拡大して使う)。sRGB の画像として扱う。

```csharp
public sealed class CellTileCache : IDisposable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[CellTileCache](VirtualGeometry.Streaming.CellTileCache.md)

#### 実装するインターフェース（Implements）

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_Streaming_CellTileCache__ctor_System_Int32_System_Int32_System_Boolean_"></a> CellTileCache\(int, int, bool\)

```csharp
public CellTileCache(int capacity, int tileSize, bool allowBc1 = true)
```

#### 引数（Parameters）

`capacity` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`tileSize` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`allowBc1` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## プロパティ（Properties）

### <a id="VirtualGeometry_Streaming_CellTileCache_Capacity"></a> Capacity

```csharp
public int Capacity { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_Streaming_CellTileCache_Count"></a> Count

```csharp
public int Count { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_Streaming_CellTileCache_Evictions"></a> Evictions

```csharp
public long Evictions { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualGeometry_Streaming_CellTileCache_HasFreeSlice"></a> HasFreeSlice

```csharp
public bool HasFreeSlice { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_Streaming_CellTileCache_IsBc1"></a> IsBc1

```csharp
public bool IsBc1 { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_Streaming_CellTileCache_Rejected"></a> Rejected

```csharp
public long Rejected { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualGeometry_Streaming_CellTileCache_RequiredReservationTemporarilyBlocked"></a> RequiredReservationTemporarilyBlocked

```csharp
public bool RequiredReservationTemporarilyBlocked { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_Streaming_CellTileCache_Texture"></a> Texture

```csharp
public Texture2DArray Texture { get; }
```

#### 値（Property Value）

 Texture2DArray

### <a id="VirtualGeometry_Streaming_CellTileCache_TileSize"></a> TileSize

```csharp
public int TileSize { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_Streaming_CellTileCache_Uploads"></a> Uploads

```csharp
public long Uploads { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

## メソッド（Methods）

### <a id="VirtualGeometry_Streaming_CellTileCache_Apply"></a> Apply\(\)

置いたタイルを GPU へ送る(1 frame に 1 回)。

```csharp
public void Apply()
```

### <a id="VirtualGeometry_Streaming_CellTileCache_CanStorePrediction_System_Int32_"></a> CanStorePrediction\(int\)

```csharp
public bool CanStorePrediction(int frame)
```

#### 引数（Parameters）

`frame` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_Streaming_CellTileCache_CancelRequiredReservation"></a> CancelRequiredReservation\(\)

予約解除後も、直近の描画・uploadの保護期間は維持する。

```csharp
public void CancelRequiredReservation()
```

### <a id="VirtualGeometry_Streaming_CellTileCache_Contains_Omni_Streaming_StreamKey__"></a> Contains\(in StreamKey\)

先読みは空きsliceだけ使い、現在の表示を追い出さない。

```csharp
public bool Contains(in StreamKey key)
```

#### 引数（Parameters）

`key` [StreamKey](Omni.Streaming.StreamKey.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_Streaming_CellTileCache_Dispose"></a> Dispose\(\)

```csharp
public void Dispose()
```

### <a id="VirtualGeometry_Streaming_CellTileCache_IsUploaded_System_Int32_"></a> IsUploaded\(int\)

slice の中身が GPU に送られている(<xref href="VirtualGeometry.Streaming.CellTileCache.Apply" data-throw-if-not-resolved="false"></xref> 済み)なら true。

```csharp
public bool IsUploaded(int slice)
```

#### 引数（Parameters）

`slice` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_Streaming_CellTileCache_ReleaseUnusedPrediction_Omni_Streaming_StreamKey__System_Int32_"></a> ReleaseUnusedPrediction\(in StreamKey, int\)

使われなくなった予測sliceだけを返す。直近の描画に触れたsliceは維持する。

```csharp
public bool ReleaseUnusedPrediction(in StreamKey key, int frame)
```

#### 引数（Parameters）

`key` [StreamKey](Omni.Streaming.StreamKey.md)

`frame` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_Streaming_CellTileCache_Store_Omni_Streaming_StreamKey__Omni_Streaming_Formats_ImageTile_System_Int32_"></a> Store\(in StreamKey, ImageTile, int\)

タイルを slice に置く(すでにあればその slice)。いっぱいなら、この frame に使っていない最も古い slice を再利用する。
全部この frame に使われているか、大きさが合わなければ −1(置かない)。

```csharp
public int Store(in StreamKey key, ImageTile tile, int frame)
```

#### 引数（Parameters）

`key` [StreamKey](Omni.Streaming.StreamKey.md)

`tile` [ImageTile](Omni.Streaming.Formats.ImageTile.md)

`frame` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_Streaming_CellTileCache_TryGetSlice_Omni_Streaming_StreamKey__System_Int32_System_Int32__"></a> TryGetSlice\(in StreamKey, int, out int\)

key のタイルが、GPU から読める slice にあれば true(使った frame を記録する)。
<xref href="VirtualGeometry.Streaming.CellTileCache.Store(Omni.Streaming.StreamKey%40%2cOmni.Streaming.Formats.ImageTile%2cSystem.Int32)" data-throw-if-not-resolved="false"></xref> で置いただけの slice(<xref href="VirtualGeometry.Streaming.CellTileCache.Apply" data-throw-if-not-resolved="false"></xref> の前)は false を返す: Store は描画の最中に走り、Apply は描画の後なので、
置いた frame の描画に slice を渡すと、その Cell は中身が空(黒)の slice を 1 frame だけ読んでしまう。次の frame(Apply の後)から使える。

```csharp
public bool TryGetSlice(in StreamKey key, int frame, out int slice)
```

#### 引数（Parameters）

`key` [StreamKey](Omni.Streaming.StreamKey.md)

`frame` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`slice` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_Streaming_CellTileCache_TryReserveRequired_System_Collections_Generic_IReadOnlyCollection_Omni_Streaming_StreamKey__System_Int32_"></a> TryReserveRequired\(IReadOnlyCollection<StreamKey\>, int\)

直近の移動に必要な色の集合を一括予約する。表示中・upload中のsliceを保護し、失敗時は前の予約を維持する。

```csharp
public bool TryReserveRequired(IReadOnlyCollection<StreamKey> keys, int frame)
```

#### 引数（Parameters）

`keys` [IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection\-1)<[StreamKey](Omni.Streaming.StreamKey.md)\>

`frame` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
