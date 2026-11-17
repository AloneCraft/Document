# <a id="VirtualGeometry_World_PlanetHeightTerrainSource"></a> Class PlanetHeightTerrainSource

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

高さの正本(<xref href="VirtualGeometry.World.IPlanetHeightProvider" data-throw-if-not-resolved="false"></xref>、CPU の double)から惑星の地形を作る。既定はCPU生成(<xref href="VirtualGeometry.World.PlanetCellMeshBuilder" data-throw-if-not-resolved="false"></xref>)、
対応する入力と明示的なshader指定があれば非接地のN=8/16をGPU生成する。接地はCPU生成を維持し、描く頂点と接地の三角形のbit一致を保つ。
CPU の時間は frame ごとの予算(<xref href="VirtualGeometry.World.PlanetHeightTerrainSource.BuildMillisecondsPerFrame" data-throw-if-not-resolved="false"></xref>)で区切り、間に合わない Cell は次の frame へ送る(親を描き続ける)。
CPU生成のboundsはCPUで求め、GPU生成は非同期の結果と世代を検査してから公開する。
Cell の選択・退避・配置は <xref href="VirtualGeometry.World.PlanetLayerSource" data-throw-if-not-resolved="false"></xref>。高さの供給元は <xref href="VirtualGeometry.World.PlanetHeightTerrainSource.Configure(VirtualGeometry.World.IPlanetHeightProvider%2cSystem.Single%2cSystem.Int32%2cSystem.Single)" data-throw-if-not-resolved="false"></xref> で渡す(Scene には保存しない)。

```csharp
[ExecuteAlways]
public sealed class PlanetHeightTerrainSource : PlanetLayerSource, IPlanetCellResidency, INavigationBoundsSource
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[VirtualGeometryClusterSource](VirtualizedGeometry.VirtualGeometryClusterSource.md) ← 
[PlanetLayerSource](VirtualGeometry.World.PlanetLayerSource.md) ← 
[PlanetHeightTerrainSource](VirtualGeometry.World.PlanetHeightTerrainSource.md)

#### 実装するインターフェース（Implements）

[IPlanetCellResidency](VirtualGeometry.World.IPlanetCellResidency.md), 
INavigationBoundsSource

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_ActiveWorkerRequests"></a> ActiveWorkerRequests

```csharp
public static long ActiveWorkerRequests { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_BuildMillisecondsPerFrame"></a> BuildMillisecondsPerFrame

1 frame に Cell の頂点を CPU で作る時間の上限(ミリ秒)。少なくとも 1 Cell は作る。

```csharp
public float BuildMillisecondsPerFrame { get; set; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_BuiltCells"></a> BuiltCells

CPU で作った Cell の累計と、直近の frame に作った数・かかった時間(診断用)。

```csharp
public int BuiltCells { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_CanUseBurstJobs"></a> CanUseBurstJobs

```csharp
public static bool CanUseBurstJobs { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_CancelledWorkerCells"></a> CancelledWorkerCells

```csharp
public long CancelledWorkerCells { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_CellHeights"></a> CellHeights

Cell の格子の高さを外から受け取る供給元。設定した Cell(<xref href="VirtualGeometry.World.PlanetCellHeightStatus.Ready" data-throw-if-not-resolved="false"></xref>)は <xref href="VirtualGeometry.World.PlanetCellMeshBuilder.BuildFromHeights(VirtualGeometry.World.PlanetCellFrame%40%2cSystem.Double%2cSystem.ReadOnlySpan%7bSystem.Double%7d%2cSystem.ReadOnlySpan%7bSystem.Double%7d%2cSystem.Single%2cUnityEngine.Vector4%2cVirtualizedGeometry.VirtualGeometryPackedVertex%5b%5d%2cSystem.Int32%2cUnityEngine.Vector4%40%2cSystem.Double%40%2cSystem.Double%40)" data-throw-if-not-resolved="false"></xref> で作り、
<xref href="VirtualGeometry.World.PlanetCellHeightStatus.NotProvided" data-throw-if-not-resolved="false"></xref> の Cell は従来どおり <xref href="VirtualGeometry.World.PlanetHeightTerrainSource.Heights" data-throw-if-not-resolved="false"></xref> から作る。Pending・Unavailable の Cell は作らない
(選択は親を描き続ける)。有効なまま変えた場合は作り直す。null で解除。

```csharp
public IPlanetCellHeightSource CellHeights { get; set; }
```

#### 値（Property Value）

 [IPlanetCellHeightSource](VirtualGeometry.World.IPlanetCellHeightSource.md)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_CellProperties"></a> CellProperties

Cell の draw の MaterialPropertyBlock に、shader が使う値を足す口(<xref href="VirtualGeometry.World.IPlanetCellPropertySource" data-throw-if-not-resolved="false"></xref>)。標準の値(_PlanetCellUp など)の後に呼ばれる。null で解除。

```csharp
public IPlanetCellPropertySource CellProperties { get; set; }
```

#### 値（Property Value）

 [IPlanetCellPropertySource](VirtualGeometry.World.IPlanetCellPropertySource.md)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_CellsFromHeightSource"></a> CellsFromHeightSource

格子の高さを供給元から受け取って作った Cell の累計(診断用)。

```csharp
public int CellsFromHeightSource { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_CellsInFlight"></a> CellsInFlight

ワーカーで作っている Cell の数（診断用）。

```csharp
public int CellsInFlight { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_CpuBuildBackend"></a> CpuBuildBackend

配列の組立と既知の増幅noiseのbackend。managed基底の取得はworkerに残す。

```csharp
public PlanetCpuBuildBackend CpuBuildBackend { get; set; }
```

#### 値（Property Value）

 [PlanetCpuBuildBackend](VirtualGeometry.World.PlanetCpuBuildBackend.md)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_ExactTerrainSlots"></a> ExactTerrainSlots

同時に32 Bで保持できるslotの上限。root6個も含む。変更するとpoolを作り直す。

```csharp
public int ExactTerrainSlots { get; set; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_ExactTerrainStorageCapacity"></a> ExactTerrainStorageCapacity

```csharp
protected override int ExactTerrainStorageCapacity { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_FailedCells"></a> FailedCells

入力を作れず(高さが有限でない)描けなかった Cell の累計(0 が正常)。

```csharp
public int FailedCells { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_FramePreparationCompleted"></a> FramePreparationCompleted

```csharp
public int FramePreparationCompleted { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_FramePreparationFailures"></a> FramePreparationFailures

```csharp
public int FramePreparationFailures { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_GenerationDiagnosticsEnabled"></a> GenerationDiagnosticsEnabled

SolarSystemの画像なしP0計測。値はこのinstanceでの累計、worker 実行区間の累計はwall時間と別。

```csharp
public bool GenerationDiagnosticsEnabled { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_GeometryGridQuads"></a> GeometryGridQuads

選択・pool・生成で共通の格子。既存Layerは64、CPU高さの地形だけ移行時に変更できる。

```csharp
protected override int GeometryGridQuads { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_GpuBuiltCells"></a> GpuBuiltCells

```csharp
public int GpuBuiltCells { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_GpuFailedCells"></a> GpuFailedCells

```csharp
public int GpuFailedCells { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_GpuFallbackInputs"></a> GpuFallbackInputs

```csharp
public int GpuFallbackInputs { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_GpuGenerationReason"></a> GpuGenerationReason

```csharp
public string GpuGenerationReason { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_GpuGenerationShader"></a> GpuGenerationShader

明示指定でGPU生成を使う。N=8/16と対応した高さ供給元のみ。変更時は旧poolを完了まで保持して作り直す。

```csharp
public ComputeShader GpuGenerationShader { get; set; }
```

#### 値（Property Value）

 ComputeShader

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_GpuPendingInputs"></a> GpuPendingInputs

```csharp
public int GpuPendingInputs { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_GpuSubmittedCells"></a> GpuSubmittedCells

```csharp
public int GpuSubmittedCells { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_GridQuads"></a> GridQuads

1 slotの格子(8/16/64 quad)。keyのlevelは変えない。同じ間隔には64→8でlevel+3が必要。変更時はpoolと接地cacheを作り直す。

```csharp
public int GridQuads { get; set; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_HeightShiftThreshold"></a> HeightShiftThreshold

中心の方向の地表の高さの絶対値がこれ以上の Cell は、原点を地表の高さまで持ち上げる。0 なら全ての Cell を持ち上げる(地面すれすれ・mm 以下の精度が要るとき。
持ち上げない Cell は、頂点が数百 m の高さ成分を float で持つので、刻みが 0.03〜0.06 mm になる)。Cell を作る前に設定する。

```csharp
public float HeightShiftThreshold { get; set; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_Heights"></a> Heights

```csharp
public IPlanetHeightProvider Heights { get; }
```

#### 値（Property Value）

 [IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_LastFrameBuildMilliseconds"></a> LastFrameBuildMilliseconds

```csharp
public float LastFrameBuildMilliseconds { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_LastFrameBuiltCells"></a> LastFrameBuiltCells

```csharp
public int LastFrameBuiltCells { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_LastGpuGenerationFailure"></a> LastGpuGenerationFailure

```csharp
public string LastGpuGenerationFailure { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_NativeAdmissionWaits"></a> NativeAdmissionWaits

```csharp
public int NativeAdmissionWaits { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_NativeBurstCompleted"></a> NativeBurstCompleted

```csharp
public int NativeBurstCompleted { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_NativeCompleted"></a> NativeCompleted

```csharp
public int NativeCompleted { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_NativeDiscarded"></a> NativeDiscarded

```csharp
public int NativeDiscarded { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_NativeProviderSubmitted"></a> NativeProviderSubmitted

```csharp
public int NativeProviderSubmitted { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_NativeRecoveryMilliseconds"></a> NativeRecoveryMilliseconds

```csharp
public double NativeRecoveryMilliseconds { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_NativeSubmitted"></a> NativeSubmitted

```csharp
public int NativeSubmitted { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_PackedTerrain"></a> PackedTerrain

N=8/16の共有indexで12 B poolを明示指定する。接地/CPUアンカーの頂点は元の32 Bで保持する。

```csharp
public bool PackedTerrain { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_QueuedWorkerCells"></a> QueuedWorkerCells

```csharp
public int QueuedWorkerCells { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_Radius"></a> Radius

惑星の半径 R(高さ 0 の球面。Cell の原点はこの球面から <xref href="VirtualGeometry.World.PlanetCellFrame.HeightShift" data-throw-if-not-resolved="false"></xref> だけ持ち上げた点)。

```csharp
public override float Radius { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_SelectionAmplitude"></a> SelectionAmplitude

頂点が半径 R から離れうる最大の距離(選択の bounds に含める)。

```csharp
protected override float SelectionAmplitude { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_SupportsIndexedTerrain"></a> SupportsIndexedTerrain

```csharp
protected override bool SupportsIndexedTerrain { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_UnavailableCells"></a> UnavailableCells

格子の高さの供給元(<xref href="VirtualGeometry.World.PlanetHeightTerrainSource.CellHeights" data-throw-if-not-resolved="false"></xref>)が Unavailable を返し、作らなかった Cell の問い合わせの累計(frame ごとに数える)。

```csharp
public int UnavailableCells { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_UseAsyncFramePreparation"></a> UseAsyncFramePreparation

```csharp
public bool UseAsyncFramePreparation { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_UseLocalHeightBounds"></a> UseLocalHeightBounds

```csharp
public bool UseLocalHeightBounds { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_UsePackedTerrainStorage"></a> UsePackedTerrainStorage

```csharp
protected override bool UsePackedTerrainStorage { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_UsePreparedSampling"></a> UsePreparedSampling

```csharp
public bool UsePreparedSampling { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_UsesWorkers"></a> UsesWorkers

Cell をワーカースレッドで作るか。

```csharp
public bool UsesWorkers { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_WorkerCount"></a> WorkerCount

Cell の高さを同時に計算するワーカーの数。高さの計算(1 Cell で数十 ms のことがある)が生成の速さを決めるので、
視点が速く近づく場面では、この数が足りないと細かい Cell が遅れて、粗い地形のまま表示される。

```csharp
public int WorkerCount { get; set; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_BeginRequestFramePreparation_System_Collections_Generic_IReadOnlyList_System_Collections_Generic_KeyValuePair_VirtualGeometry_World_PlanetCellKey_System_Single___System_Int32_"></a> BeginRequestFramePreparation\(IReadOnlyList<KeyValuePair<PlanetCellKey, float\>\>, int\)

```csharp
protected override void BeginRequestFramePreparation(IReadOnlyList<KeyValuePair<PlanetCellKey, float>> requests, int limit)
```

#### 引数（Parameters）

`requests` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair\-2)<[PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md), [float](https://learn.microsoft.com/dotnet/api/system.single)\>\>

`limit` [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_Configure_VirtualGeometry_World_IPlanetHeightProvider_System_Single_System_Int32_System_Single_"></a> Configure\(IPlanetHeightProvider, float, int, float\)

高さの供給元・半径・選択の設定を決める。有効なまま変えた場合は作り直す。heights が null なら高さ 0 の球。
供給元は同じ引数に常に同じ値を返すこと(作り直した Cell と接地の計算が一致する前提)。

```csharp
public void Configure(IPlanetHeightProvider heights, float radius, int maximumLevel, float targetPixels)
```

#### 引数（Parameters）

`heights` [IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

`radius` [float](https://learn.microsoft.com/dotnet/api/system.single)

`maximumLevel` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`targetPixels` [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_GenerateSlots_System_Collections_Generic_IReadOnlyList_System_Int32__"></a> GenerateSlots\(IReadOnlyList<int\>\)

生成を予約したslotを、<xref href="VirtualizedGeometry.VirtualGeometryClusterSource.StoreSlot(System.Int32%2cVirtualizedGeometry.VirtualGeometryPackedVertex%5b%5d)" data-throw-if-not-resolved="false"></xref>でuploadするか、GPUのleaseを取得して完了後に公開する。

```csharp
protected override void GenerateSlots(IReadOnlyList<int> slots)
```

#### 引数（Parameters）

`slots` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[int](https://learn.microsoft.com/dotnet/api/system.int32)\>

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_GenerationTimingCsv"></a> GenerationTimingCsv\(\)

```csharp
public string GenerationTimingCsv()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_IsGenerationInputReady_System_Int32_"></a> IsGenerationInputReady\(int\)

slot の生成の入力が揃っているか(既定は true)。揃っていない slot は生成を次の frame へ送る。

```csharp
protected override bool IsGenerationInputReady(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_OnDisable"></a> OnDisable\(\)

```csharp
protected override void OnDisable()
```

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_OnEnable"></a> OnEnable\(\)

```csharp
protected override void OnEnable()
```

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_PrepareGenerationInputs_System_Collections_Generic_IReadOnlyList_System_Int32__"></a> PrepareGenerationInputs\(IReadOnlyList<int\>\)

生成を待っている slot(要求の順)の、生成の入力を CPU で用意する(頂点を CPU で作る供給元。既定は何もしない)。
生成の直前、frame に 1 回だけ呼ぶ。用意できた slot は <xref href="VirtualizedGeometry.VirtualGeometryClusterSource.IsGenerationInputReady(System.Int32)" data-throw-if-not-resolved="false"></xref> が true を返すこと。

```csharp
protected override void PrepareGenerationInputs(IReadOnlyList<int> pendingSlots)
```

#### 引数（Parameters）

`pendingSlots` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[int](https://learn.microsoft.com/dotnet/api/system.int32)\>

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_TerrainSlotFaceRange_System_Int32_"></a> TerrainSlotFaceRange\(int\)

```csharp
protected override Vector4 TerrainSlotFaceRange(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 Vector4

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_TryBuildContactTerrain_Omni_Logical_Vector3__System_Single_System_Int32_VirtualGeometry_World_PlanetTriangleSoup_"></a> TryBuildContactTerrain\(in Vector3, float, int, PlanetTriangleSoup\)

接地の計算に使う地形の三角形を作る。点 point(惑星のローカル座標、Logical)のまわり半径 footprint の円板に掛かる階層 level の Cell を、
描く Cell と同じ値で CPU で作り、三角形(skirt を除く。VirtualGeometryGridLayout と同じ分割)を terrain に足す。
頂点は point からの相対位置(m、double): Cell の原点 − point を Logical で引いてから double にし、描く float の頂点を足す。
描く三角形と同じにするには、同じ領域を <xref href="VirtualGeometry.World.PlanetLayerSource.SetContactRegions(System.Collections.Generic.IReadOnlyList%7bVirtualGeometry.World.PlanetContactRegion%7d%2cSystem.Boolean)" data-throw-if-not-resolved="false"></xref> で登録しておくこと。

```csharp
public bool TryBuildContactTerrain(in Vector3 point, float footprint, int level, PlanetTriangleSoup terrain)
```

#### 引数（Parameters）

`point` Vector3

`footprint` [float](https://learn.microsoft.com/dotnet/api/system.single)

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`terrain` [PlanetTriangleSoup](VirtualGeometry.World.PlanetTriangleSoup.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_TryCellHeightRange_VirtualGeometry_World_PlanetCellFrame__System_Double__System_Double__"></a> TryCellHeightRange\(in PlanetCellFrame, out double, out double\)

```csharp
protected override bool TryCellHeightRange(in PlanetCellFrame frame, out double minimum, out double maximum)
```

#### 引数（Parameters）

`frame` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

`minimum` [double](https://learn.microsoft.com/dotnet/api/system.double)

`maximum` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_TryCellHeightShift_VirtualGeometry_World_PlanetCellFrame__System_Single__"></a> TryCellHeightShift\(in PlanetCellFrame, out float\)

Cell の原点を半径 R の球面から外向きに持ち上げる高さ(m)。頂点は持ち上げた原点からの相対位置になり、起伏の大きな天体でも高さ方向の成分が小さく保たれる。
同じ Cell には常に同じ値を返すこと。既定は 0(持ち上げない)。sphereFrame は持ち上げていない Cell の値(<xref href="VirtualGeometry.World.PlanetCellFrame.SphereOrigin" data-throw-if-not-resolved="false"></xref> など)。

```csharp
protected override bool TryCellHeightShift(in PlanetCellFrame sphereFrame, out float shift)
```

#### 引数（Parameters）

`sphereFrame` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

`shift` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_TryGetRequestFrame_VirtualGeometry_World_PlanetCellKey__VirtualGeometry_World_PlanetCellFrame__"></a> TryGetRequestFrame\(in PlanetCellKey, out PlanetCellFrame\)

```csharp
protected override bool TryGetRequestFrame(in PlanetCellKey key, out PlanetCellFrame frame)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

`frame` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_TrySampleHeight_Omni_Logical_Vector3__System_Double__"></a> TrySampleHeight\(in Vector3, out double\)

点 point(惑星のローカル座標、Logical)の真下(中心からの方向)の地表の高さ(帯域制限なし、R からの高さ、m)。
接地には使わない(描く三角形は帯域制限した高さで、三角形の内側は線形補間なので)。見積もり・検証用。

```csharp
public bool TrySampleHeight(in Vector3 point, out double height)
```

#### 引数（Parameters）

`point` Vector3

`height` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_TrySampleMeshHeight_Omni_Logical_Vector3__System_Int32_System_Boolean_System_Double__"></a> TrySampleMeshHeight\(in Vector3, int, bool, out double\)

指定levelの描画と同じ頂点の三角形から高さを求める。生成済みを要求する場合は、接地領域を登録してから呼ぶ。
入力待ちをReadyへ置き換えず、全帯域のTrySampleHeightとは明示的に分離する。

```csharp
public bool TrySampleMeshHeight(in Vector3 point, int level, bool requireResident, out double height)
```

#### 引数（Parameters）

`point` Vector3

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`requireResident` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`height` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetHeightTerrainSource_WriteCellProperties_UnityEngine_MaterialPropertyBlock_System_Int32_VirtualGeometry_World_PlanetCellFrame__"></a> WriteCellProperties\(MaterialPropertyBlock, int, in PlanetCellFrame\)

Cell の draw の MaterialPropertyBlock に、この Layer の shader が使う値を書く(配置が書く値の後に呼ぶ)。
_PlanetCellUp: xyz=Cell の原点の外向きの単位方向(object 空間)、w=Cell の原点の惑星の中心からの距離(R+HeightShift)。
_PlanetCellQuad: x=この階層の quad の弧長。
_PlanetCellRef: xyz=Cell の原点 − 基準点(<xref href="VirtualGeometry.World.PlanetLayerSource.SetReferencePoint(Omni.Logical.Vector3%40)" data-throw-if-not-resolved="false"></xref>)を Logical で引いてから float にしたもの(object 空間)、w=基準点があれば 1。
派生クラスは base を呼んでから、自分の値を足す。

```csharp
protected override void WriteCellProperties(MaterialPropertyBlock block, int slot, in PlanetCellFrame frame)
```

#### 引数（Parameters）

`block` MaterialPropertyBlock

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`frame` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)
