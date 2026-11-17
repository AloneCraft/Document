# <a id="VirtualGeometry_Streaming_StreamedCellHeightSource"></a> Class StreamedCellHeightSource

Namespace: [VirtualGeometry.Streaming](VirtualGeometry.Streaming.md)  
Assembly: Omni.VirtualGeometry.Streaming.dll  

<xref href="VirtualGeometry.World.IPlanetCellHeightSource" data-throw-if-not-resolved="false"></xref> をストリーミング(<xref href="Omni.Streaming.StreamingHost" data-throw-if-not-resolved="false"></xref>)で満たす。階層が maximumLevel 以下の Cell は、その Cell の格子の高さ
(<xref href="VirtualGeometry.Streaming.CellHeightGrid" data-throw-if-not-resolved="false"></xref>)が常駐したら Ready、届くまで Pending(取得を宣言)。カタログが「無い」(Absent)と答えた Cell と、階層が深い Cell は
NotProvided(高さの供給元 = <xref href="VirtualGeometry.Streaming.StreamedPlanetHeightProvider" data-throw-if-not-resolved="false"></xref> などで作る)。取得に失敗した・取得手段が無い・pack に無い Cell は Unavailable
(作らない。偽の高さで埋めない。pack は階層 0〜MaximumLevel の全 Cell を持つこと)。
階層が深い Cell を問い合わせると、その祖先(階層 MaximumLevel)の格子を手元に確保(pin)し、確保できてから NotProvided を返す
(深い Cell を作る供給元が、同じ格子から補間するため)。届いていなければ Pending。
宣言は <xref href="VirtualGeometry.Streaming.StreamedCellHeightSource.PublishInterest(System.Int32)" data-throw-if-not-resolved="false"></xref> が行う(毎 frame、描画の後に呼ぶ)。直近 <xref href="VirtualGeometry.Streaming.StreamedCellHeightSource.InterestFrames" data-throw-if-not-resolved="false"></xref> frame に問い合わせのあった Cell だけを宣言し続ける。

```csharp
public sealed class StreamedCellHeightSource : IPlanetCellHeightBoundsSource, IPlanetGridHeightSource, IPlanetCellHeightSource, IDisposable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[StreamedCellHeightSource](VirtualGeometry.Streaming.StreamedCellHeightSource.md)

#### 実装するインターフェース（Implements）

IPlanetCellHeightBoundsSource, 
IPlanetGridHeightSource, 
IPlanetCellHeightSource, 
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_Streaming_StreamedCellHeightSource__ctor_Omni_Streaming_StreamingHost_System_UInt32_System_Int32_"></a> StreamedCellHeightSource\(StreamingHost, uint, int\)

```csharp
public StreamedCellHeightSource(StreamingHost host, uint layer, int maximumLevel)
```

#### 引数（Parameters）

`host` [StreamingHost](Omni.Streaming.StreamingHost.md)

`layer` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`maximumLevel` [int](https://learn.microsoft.com/dotnet/api/system.int32)

## フィールド（Fields）

### <a id="VirtualGeometry_Streaming_StreamedCellHeightSource_InterestFrames"></a> InterestFrames

この frame 数より古い問い合わせは、宣言から外す。

```csharp
public int InterestFrames
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_Streaming_StreamedCellHeightSource_MaximumPinned"></a> MaximumPinned

確保する格子の数の上限(超えたら使われていない古いものから手放す)。

```csharp
public int MaximumPinned
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_Streaming_StreamedCellHeightSource_PinFrames"></a> PinFrames

確保(pin)した祖先の格子を、この frame 数使われなければ手放す。

```csharp
public int PinFrames
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="VirtualGeometry_Streaming_StreamedCellHeightSource_Layer"></a> Layer

```csharp
public uint Layer { get; }
```

#### 値（Property Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualGeometry_Streaming_StreamedCellHeightSource_MaximumLevel"></a> MaximumLevel

```csharp
public int MaximumLevel { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_Streaming_StreamedCellHeightSource_PendingQueries"></a> PendingQueries

```csharp
public int PendingQueries { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_Streaming_StreamedCellHeightSource_PinnedCount"></a> PinnedCount

```csharp
public int PinnedCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_Streaming_StreamedCellHeightSource_ReadyQueries"></a> ReadyQueries

```csharp
public int ReadyQueries { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_Streaming_StreamedCellHeightSource_UnavailableQueries"></a> UnavailableQueries

```csharp
public int UnavailableQueries { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="VirtualGeometry_Streaming_StreamedCellHeightSource_Dispose"></a> Dispose\(\)

```csharp
public void Dispose()
```

### <a id="VirtualGeometry_Streaming_StreamedCellHeightSource_GetHeightRange_VirtualGeometry_World_PlanetCellKey__System_Int32_System_Double__System_Double__"></a> GetHeightRange\(in PlanetCellKey, int, out double, out double\)

```csharp
public PlanetCellHeightStatus GetHeightRange(in PlanetCellKey key, int gridQuads, out double minimum, out double maximum)
```

#### 引数（Parameters）

`key` PlanetCellKey

`gridQuads` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`minimum` [double](https://learn.microsoft.com/dotnet/api/system.double)

`maximum` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 PlanetCellHeightStatus

### <a id="VirtualGeometry_Streaming_StreamedCellHeightSource_PredictionStatus_VirtualGeometry_World_PlanetCellKey__"></a> PredictionStatus\(in PlanetCellKey\)

予測Cellの元データの取得失敗を、未到着と区別する。新しい要求やpinは作らない。

```csharp
public PlanetCellHeightStatus PredictionStatus(in PlanetCellKey key)
```

#### 引数（Parameters）

`key` PlanetCellKey

#### 戻り値（Returns）

 PlanetCellHeightStatus

### <a id="VirtualGeometry_Streaming_StreamedCellHeightSource_PublishInterest_System_Int32_"></a> PublishInterest\(int\)

直近に問い合わせのあった未到着の Cell を、ストリーミングの関心として宣言する。frame は単調に増える値(Time.frameCount など)。

```csharp
public void PublishInterest(int currentFrame)
```

#### 引数（Parameters）

`currentFrame` [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_Streaming_StreamedCellHeightSource_RequestGridAt_System_Double_System_Double_System_Double_System_Single_"></a> RequestGridAt\(double, double, double, float\)

単位方向 (x, y, z) の下の、階層 MaximumLevel の格子を確保する(確保済みなら使った frame を更新する)。Cell を作らずに高さを読む利用者
(接地の問い合わせ、カメラの経路の地面など)が、読む前に毎 frame 呼ぶ。確保は Cell を作るときの問い合わせでしか更新されないので、
呼ばないと、作り終えた Cell の下の格子は <xref href="VirtualGeometry.Streaming.StreamedCellHeightSource.PinFrames" data-throw-if-not-resolved="false"></xref> frame 後に手放され、読めなくなる(fps が高いほど早い)。
届いていなければ取得を宣言して Pending。main thread から呼ぶ。

```csharp
public PlanetCellHeightStatus RequestGridAt(double x, double y, double z, float priority)
```

#### 引数（Parameters）

`x` [double](https://learn.microsoft.com/dotnet/api/system.double)

`y` [double](https://learn.microsoft.com/dotnet/api/system.double)

`z` [double](https://learn.microsoft.com/dotnet/api/system.double)

`priority` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 PlanetCellHeightStatus

### <a id="VirtualGeometry_Streaming_StreamedCellHeightSource_TryGetPinned_Omni_Streaming_StreamKey__VirtualGeometry_Streaming_CellHeightGrid__"></a> TryGetPinned\(in StreamKey, out CellHeightGrid\)

確保(pin)してある格子。別 thread から読んでよい(格子は作られた後に変わらない)。

```csharp
public bool TryGetPinned(in StreamKey key, out CellHeightGrid grid)
```

#### 引数（Parameters）

`key` [StreamKey](Omni.Streaming.StreamKey.md)

`grid` [CellHeightGrid](VirtualGeometry.Streaming.CellHeightGrid.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_Streaming_StreamedCellHeightSource_TryGetRingHeights_VirtualGeometry_World_PlanetCellKey__System_Single_System_Double___System_Double___System_Boolean__"></a> TryGetRingHeights\(in PlanetCellKey, float, double\[\], double\[\], out bool\)

key の Cell の格子の高さ(外の 1 周を含む <xref href="VirtualGeometry.World.PlanetCellMeshBuilder.RingSide" data-throw-if-not-resolved="false"></xref>²、行 j・列 i の順に j·RingSide+i)を ringHeights に書く。
陰影用の別の高さを持つなら shadingHeights にも書いて hasShading を true にする(持たなければ false で、書かない)。
priority は大きいほど先に取りたい(Pending を返すときの取得の優先度)。

```csharp
public PlanetCellHeightStatus TryGetRingHeights(in PlanetCellKey key, float priority, double[] ringHeights, double[] shadingHeights, out bool hasShading)
```

#### 引数（Parameters）

`key` PlanetCellKey

`priority` [float](https://learn.microsoft.com/dotnet/api/system.single)

`ringHeights` [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]

`shadingHeights` [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]

`hasShading` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 PlanetCellHeightStatus

### <a id="VirtualGeometry_Streaming_StreamedCellHeightSource_TryGetRingHeights_VirtualGeometry_World_PlanetCellFrame__System_Int32_System_Single_System_Double___System_Double___System_Boolean__"></a> TryGetRingHeights\(in PlanetCellFrame, int, float, double\[\], double\[\], out bool\)

同じquad間隔になる64格子の階層。細かい側は最大階層のpinだけを行い、供給元へ委ねる。

```csharp
public PlanetCellHeightStatus TryGetRingHeights(in PlanetCellFrame frame, int gridQuads, float priority, double[] ringHeights, double[] shadingHeights, out bool hasShading)
```

#### 引数（Parameters）

`frame` PlanetCellFrame

`gridQuads` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`priority` [float](https://learn.microsoft.com/dotnet/api/system.single)

`ringHeights` [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]

`shadingHeights` [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]

`hasShading` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 PlanetCellHeightStatus
