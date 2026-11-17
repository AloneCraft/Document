# <a id="VirtualGeometry_Streaming_StreamedCellTileSource"></a> Class StreamedCellTileSource

Namespace: [VirtualGeometry.Streaming](VirtualGeometry.Streaming.md)  
Assembly: Omni.VirtualGeometry.Streaming.dll  

Cell ごとの色のタイルを、ストリーミング(<xref href="Omni.Streaming.StreamingHost" data-throw-if-not-resolved="false"></xref>)で届けて <xref href="VirtualGeometry.Streaming.CellTileCache" data-throw-if-not-resolved="false"></xref> に置き、Cell の draw の値として渡す
(<xref href="VirtualGeometry.World.IPlanetCellPropertySource" data-throw-if-not-resolved="false"></xref>)。Cell の階層が pack の最大階層を超えるときは、最大階層の祖先のタイルを拡大して使う
(テクセルが画素より大きくなる所。そこから先の細部は shader の手続きの細部が受け持つ)。自分のタイルが届くまでは、届いている最も近い祖先のタイルで描く。
書く値: _PlanetTileSlice.x = slice(タイルが無ければ −1)、_PlanetTileMap = (scaleU, scaleV, offsetU, offsetV)
(面の UV からタイルの UV への変換。タイルの外周の border は隣へのにじみを防ぐ余白)。

```csharp
public sealed class StreamedCellTileSource : IPlanetCellPropertySource, IDisposable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[StreamedCellTileSource](VirtualGeometry.Streaming.StreamedCellTileSource.md)

#### 実装するインターフェース（Implements）

IPlanetCellPropertySource, 
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_Streaming_StreamedCellTileSource__ctor_Omni_Streaming_StreamingHost_System_UInt32_System_Int32_VirtualGeometry_Streaming_CellTileCache_System_Int32_"></a> StreamedCellTileSource\(StreamingHost, uint, int, CellTileCache, int\)

```csharp
public StreamedCellTileSource(StreamingHost host, uint layer, int maximumLevel, CellTileCache cache, int border)
```

#### 引数（Parameters）

`host` [StreamingHost](Omni.Streaming.StreamingHost.md)

`layer` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`maximumLevel` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`cache` [CellTileCache](VirtualGeometry.Streaming.CellTileCache.md)

`border` [int](https://learn.microsoft.com/dotnet/api/system.int32)

## フィールド（Fields）

### <a id="VirtualGeometry_Streaming_StreamedCellTileSource_InterestFrames"></a> InterestFrames

```csharp
public int InterestFrames
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_Streaming_StreamedCellTileSource_LastWrites"></a> LastWrites

診断用: 直近の WriteProperties の結果(Cell → 使ったタイルのキー・slice・変換)。1 Cell 1 件、上限 4096 件。

```csharp
public readonly Dictionary<PlanetCellKey, string> LastWrites
```

#### 値（Field Value）

 [Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary\-2)<PlanetCellKey, [string](https://learn.microsoft.com/dotnet/api/system.string)\>

## プロパティ（Properties）

### <a id="VirtualGeometry_Streaming_StreamedCellTileSource_AncestorTiles"></a> AncestorTiles

```csharp
public long AncestorTiles { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualGeometry_Streaming_StreamedCellTileSource_Cache"></a> Cache

```csharp
public CellTileCache Cache { get; }
```

#### 値（Property Value）

 [CellTileCache](VirtualGeometry.Streaming.CellTileCache.md)

### <a id="VirtualGeometry_Streaming_StreamedCellTileSource_ExactTiles"></a> ExactTiles

```csharp
public long ExactTiles { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualGeometry_Streaming_StreamedCellTileSource_MissingTiles"></a> MissingTiles

```csharp
public long MissingTiles { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualGeometry_Streaming_StreamedCellTileSource_PredictionBudgetLimited"></a> PredictionBudgetLimited

```csharp
public bool PredictionBudgetLimited { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_Streaming_StreamedCellTileSource_RequiredBudgetLimited"></a> RequiredBudgetLimited

```csharp
public bool RequiredBudgetLimited { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_Streaming_StreamedCellTileSource_RequiredCount"></a> RequiredCount

```csharp
public int RequiredCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_Streaming_StreamedCellTileSource_RequiredMissing"></a> RequiredMissing

```csharp
public int RequiredMissing { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_Streaming_StreamedCellTileSource_RequiredRequestedCount"></a> RequiredRequestedCount

```csharp
public int RequiredRequestedCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_Streaming_StreamedCellTileSource_RequiredTemporarilyBlocked"></a> RequiredTemporarilyBlocked

```csharp
public bool RequiredTemporarilyBlocked { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="VirtualGeometry_Streaming_StreamedCellTileSource_CancelPrediction"></a> CancelPrediction\(\)

予測経路の取消。通常の描画要求は維持する。

```csharp
public void CancelPrediction()
```

### <a id="VirtualGeometry_Streaming_StreamedCellTileSource_CancelRequiredPrediction"></a> CancelRequiredPrediction\(\)

Camera・経路・地表セッションの変更時に直近区間の取得とslice保護を解除する。

```csharp
public void CancelRequiredPrediction()
```

### <a id="VirtualGeometry_Streaming_StreamedCellTileSource_CheckDrawableCut_System_Collections_Generic_IReadOnlyList_VirtualGeometry_World_PlanetCellKey__System_Single_"></a> CheckDrawableCut\(IReadOnlyList<PlanetCellKey\>, float\)

通常描画と同じupload済み祖先でcutを覆えるか。最終色解像度は変更しない。

```csharp
public PlanetCellHeightStatus CheckDrawableCut(IReadOnlyList<PlanetCellKey> keys, float priority = 1)
```

#### 引数（Parameters）

`keys` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<PlanetCellKey\>

`priority` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 PlanetCellHeightStatus

### <a id="VirtualGeometry_Streaming_StreamedCellTileSource_Dispose"></a> Dispose\(\)

```csharp
public void Dispose()
```

### <a id="VirtualGeometry_Streaming_StreamedCellTileSource_Predict_VirtualGeometry_World_PlanetCellKey__System_Single_"></a> Predict\(in PlanetCellKey, float\)

描画前の色タイル要求。GPU upload前はPending。予測だけでは表示タイルを追い出さない。

```csharp
public PlanetCellHeightStatus Predict(in PlanetCellKey key, float priority)
```

#### 引数（Parameters）

`key` PlanetCellKey

`priority` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 PlanetCellHeightStatus

### <a id="VirtualGeometry_Streaming_StreamedCellTileSource_PublishInterest_System_Int32_"></a> PublishInterest\(int\)

直近に問い合わせのあった未到着のタイルを宣言し、置いたタイルを GPU へ送る。描画の直後に毎 frame 呼ぶ。

```csharp
public void PublishInterest(int currentFrame)
```

#### 引数（Parameters）

`currentFrame` [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_Streaming_StreamedCellTileSource_RefreshRequired"></a> RefreshRequired\(\)

予約を選び直さず、到着済みpayloadとGPU uploadの完了を確認する。

```csharp
public PlanetCellHeightStatus RefreshRequired()
```

#### 戻り値（Returns）

 PlanetCellHeightStatus

### <a id="VirtualGeometry_Streaming_StreamedCellTileSource_ReserveRequired_System_Collections_Generic_IReadOnlyList_VirtualGeometry_World_PlanetCellKey__System_Single_System_Boolean_"></a> ReserveRequired\(IReadOnlyList<PlanetCellKey\>, float, bool\)

SolarSystemの直近区間で使う色タイルをpackの最大階層へ対応付け、一括予約する。
GPU upload前はPending。appendは複数Viewの結合用で、容量不足なら既存予約を維持する。

```csharp
public PlanetCellHeightStatus ReserveRequired(IReadOnlyList<PlanetCellKey> keys, float priority = 1, bool append = false)
```

#### 引数（Parameters）

`keys` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<PlanetCellKey\>

`priority` [float](https://learn.microsoft.com/dotnet/api/system.single)

`append` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 PlanetCellHeightStatus

### <a id="VirtualGeometry_Streaming_StreamedCellTileSource_WriteProperties_VirtualGeometry_World_PlanetCellKey__System_Single_UnityEngine_MaterialPropertyBlock_"></a> WriteProperties\(in PlanetCellKey, float, MaterialPropertyBlock\)

key の Cell の draw の値を block に書く。priority は大きいほど先に取りたい(まだ届いていない値を要求するときの優先度)。
値が無い間も、shader が見分けられる値(例: 番号 −1)を必ず書くこと(MaterialPropertyBlock は前の Cell の値を残さないが、書かないと shader の既定値になる)。

```csharp
public void WriteProperties(in PlanetCellKey key, float priority, MaterialPropertyBlock block)
```

#### 引数（Parameters）

`key` PlanetCellKey

`priority` [float](https://learn.microsoft.com/dotnet/api/system.single)

`block` MaterialPropertyBlock
