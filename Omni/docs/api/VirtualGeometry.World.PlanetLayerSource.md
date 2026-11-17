# <a id="VirtualGeometry_World_PlanetLayerSource"></a> Class PlanetLayerSource

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

球の地形を、cube-sphere の Cell ごとの instance として VG のメッシュ経路で描く共通部分(派生は <xref href="VirtualGeometry.World.PlanetHeightTerrainSource" data-throw-if-not-resolved="false"></xref>)。惑星の中心はこの GameObject の原点。
Cell の選択は <xref href="VirtualGeometry.World.PlanetCellSelector" data-throw-if-not-resolved="false"></xref>、頂点の生成は派生クラスが CPU で行い、Cell の頂点の pool(<xref href="VirtualizedGeometry.VirtualGeometryClusterSource" data-throw-if-not-resolved="false"></xref>)の slot へ書く。
Cell と pool の slot の対応を持ち、pool が足りないときは使っていない Cell を下(葉)から退避する。
頂点は Cell の原点(Cell の中心の方向の地表の高さの点、惑星のローカル座標。<xref href="VirtualGeometry.World.PlanetCellFrame.Origin" data-throw-if-not-resolved="false"></xref>)からの相対位置で持ち、Cell ごとに draw する。
惑星を置く空間は <xref href="VirtualGeometry.World.IPlanetPlacement" data-throw-if-not-resolved="false"></xref> が決める(OnEnable の時に同じ GameObject にある実装。無い、または無効なら Unity の world 空間)。
Cell の原点と GPU に渡す値は Logical 精度で求める(<xref href="VirtualGeometry.World.PlanetCellFrame" data-throw-if-not-resolved="false"></xref>)。頂点の誤差は惑星の大きさではなく Cell の大きさに比例する。

```csharp
[ExecuteAlways]
public abstract class PlanetLayerSource : VirtualGeometryClusterSource, IPlanetCellResidency, INavigationBoundsSource
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[VirtualGeometryClusterSource](VirtualizedGeometry.VirtualGeometryClusterSource.md) ← 
[PlanetLayerSource](VirtualGeometry.World.PlanetLayerSource.md)

#### 派生した型（Derived）

[PlanetHeightTerrainSource](VirtualGeometry.World.PlanetHeightTerrainSource.md)

#### 実装するインターフェース（Implements）

[IPlanetCellResidency](VirtualGeometry.World.IPlanetCellResidency.md), 
INavigationBoundsSource

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetLayerSource_CellQuads"></a> CellQuads

```csharp
public const int CellQuads = 64
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_ClusterQuads"></a> ClusterQuads

```csharp
public const int ClusterQuads = 8
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_GpuMaximumLevel"></a> GpuMaximumLevel

選べる最大の階層。Cell の中心の値を Logical で正確に作れる範囲(<xref href="VirtualGeometry.World.PlanetCellFrame.MaximumLevel" data-throw-if-not-resolved="false"></xref>)。

```csharp
public const int GpuMaximumLevel = 94
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_SelectedCellBudgetFraction"></a> SelectedCellBudgetFraction

slot が足りず、退避できる Cell も無かったために生成できなかった要求の累計。

```csharp
public const float SelectedCellBudgetFraction = 0.2
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetLayerSource_ActiveLodBudgetMode"></a> ActiveLodBudgetMode

```csharp
public PlanetLodBudgetMode ActiveLodBudgetMode { get; }
```

#### 値（Property Value）

 [PlanetLodBudgetMode](VirtualGeometry.World.PlanetLodBudgetMode.md)

### <a id="VirtualGeometry_World_PlanetLayerSource_CameraDiagnostics"></a> CameraDiagnostics

```csharp
public IReadOnlyDictionary<string, string> CameraDiagnostics { get; }
```

#### 値（Property Value）

 [IReadOnlyDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlydictionary\-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="VirtualGeometry_World_PlanetLayerSource_CollectCameraDiagnostics"></a> CollectCameraDiagnostics

true の間、camera ごとの直近の選択の要約（選んだ数、描いた数、まだ描けない数、階層ごとの数）を <xref href="VirtualGeometry.World.PlanetLayerSource.CameraDiagnostics" data-throw-if-not-resolved="false"></xref> に書く（診断用。文字列を作るので既定は false）。

```csharp
public bool CollectCameraDiagnostics { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetLayerSource_CollectDrawDiagnostics"></a> CollectDrawDiagnostics

true の間、数 frame ごとに、描画の共有 buffer が溢れて描けなかった cluster の数(穴になる。0 が正常)を GPU から非同期に読み戻して <xref href="VirtualGeometry.World.PlanetLayerSource.DroppedClusters" data-throw-if-not-resolved="false"></xref> に書き、あれば警告する。
既定は Editor だけ(Player では読み戻さない)。

```csharp
public bool CollectDrawDiagnostics { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetLayerSource_ContactPrefetchEnabled"></a> ContactPrefetchEnabled

```csharp
public bool ContactPrefetchEnabled { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetLayerSource_ContactRegions"></a> ContactRegions

```csharp
public IReadOnlyList<PlanetContactRegion> ContactRegions { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[PlanetContactRegion](VirtualGeometry.World.PlanetContactRegion.md)\>

### <a id="VirtualGeometry_World_PlanetLayerSource_ContactRegionsReady"></a> ContactRegionsReady

接地の領域の Cell と、降りる道（<xref href="VirtualGeometry.World.PlanetLayerSource.SetContactRegions(System.Collections.Generic.IReadOnlyList%7bVirtualGeometry.World.PlanetContactRegion%7d%2cSystem.Boolean)" data-throw-if-not-resolved="false"></xref> の prefetch）がすべて生成済みか。周囲の先読みは含まない。

```csharp
public bool ContactRegionsReady { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetLayerSource_DeepestSelectedLevel"></a> DeepestSelectedLevel

直近の選択で選んだ Cell のうち、最も深い階層(選んだ Cell が無ければ −1)。カメラが近づいたとき、細かい Cell が追いついたかの判定に使う(毎 frame 呼べる)。

```csharp
public int DeepestSelectedLevel { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_DemandedIndices"></a> DemandedIndices

直近の読み戻しの、1 パス目で描こうとした index の数と、描画の共有 buffer の容量(index の数)。

```csharp
public long DemandedIndices { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualGeometry_World_PlanetLayerSource_DrawError"></a> DrawError

描画の準備(材質・GPU 資源)の失敗の理由。正常なら null。

```csharp
public string DrawError { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualGeometry_World_PlanetLayerSource_DrawOverflowReports"></a> DrawOverflowReports

読み戻しで、容量を超えた cluster を見つけた回数(0 が正常)。

```csharp
public int DrawOverflowReports { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_DrawableCutSelection"></a> DrawableCutSelection

```csharp
public IReadOnlyList<PlanetCellKey> DrawableCutSelection { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)\>

### <a id="VirtualGeometry_World_PlanetLayerSource_DroppedClusters"></a> DroppedClusters

直近の読み戻しで、描画の共有 buffer の容量を超えて描かなかった cluster の数(穴になる。0 が正常)。<xref href="VirtualGeometry.World.PlanetLayerSource.CollectDrawDiagnostics" data-throw-if-not-resolved="false"></xref> が true のときだけ更新する。

```csharp
public long DroppedClusters { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualGeometry_World_PlanetLayerSource_EffectiveTargetPixels"></a> EffectiveTargetPixels

```csharp
public float EffectiveTargetPixels { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetLayerSource_ErrorMetric"></a> ErrorMetric

Cell の細かさを決める誤差の定義(E1 / E2。既定は E2 = <xref href="VirtualGeometry.World.PlanetErrorMetric.ProjectedArea" data-throw-if-not-resolved="false"></xref>。<code>Docs/Plans/VirtualGeometryNaniteMigration.md</code>)。起動引数 <code>-vgErrorMetric quad|area</code> が優先する(検証用)。

```csharp
public PlanetErrorMetric ErrorMetric { get; set; }
```

#### 値（Property Value）

 [PlanetErrorMetric](VirtualGeometry.World.PlanetErrorMetric.md)

### <a id="VirtualGeometry_World_PlanetLayerSource_Evictions"></a> Evictions

```csharp
public int Evictions { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_GeometryGridQuads"></a> GeometryGridQuads

選択・pool・生成で共通の格子。既存Layerは64、CPU高さの地形だけ移行時に変更できる。

```csharp
protected virtual int GeometryGridQuads { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_Geomorph"></a> Geomorph

階層の境目の頂点を、親の面へ連続的に寄せる。無効なら従来どおり(階層の境目で細かさが段になる)。起動引数 <code>-vgGeomorph on|off</code> が優先する(検証用)。
材質が落とした octave を shader で戻す補償(Moon の <code>_PlanetCellQuad.x</code>)は、寄せた形を知らない。補償のある材質は、調整が済むまで無効のままにする。

```csharp
public bool Geomorph { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetLayerSource_GpuResidencyConsumerCount"></a> GpuResidencyConsumerCount

```csharp
public int GpuResidencyConsumerCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_GpuResidencyReaders"></a> GpuResidencyReaders

```csharp
public int GpuResidencyReaders { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_GpuResidencyReason"></a> GpuResidencyReason

```csharp
public string GpuResidencyReason { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualGeometry_World_PlanetLayerSource_GpuResidencyStorageBytes"></a> GpuResidencyStorageBytes

```csharp
public long GpuResidencyStorageBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualGeometry_World_PlanetLayerSource_GpuTerrainRecordFallbacks"></a> GpuTerrainRecordFallbacks

```csharp
public long GpuTerrainRecordFallbacks { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualGeometry_World_PlanetLayerSource_GpuTerrainRecordReason"></a> GpuTerrainRecordReason

```csharp
public string GpuTerrainRecordReason { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualGeometry_World_PlanetLayerSource_GpuTerrainRecordings"></a> GpuTerrainRecordings

```csharp
public long GpuTerrainRecordings { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualGeometry_World_PlanetLayerSource_GpuTerrainRecords"></a> GpuTerrainRecords

CPUの準備済みcutをseedし、通常FeatureでGPU record/count描画を使う。全階層のGPU選択は別工程。

```csharp
public bool GpuTerrainRecords { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetLayerSource_IndexedTerrain"></a> IndexedTerrain

対応した材質・property供給元で、共有indexのクラスタinstance描画を使う。移行中は既定無効。

```csharp
public bool IndexedTerrain { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetLayerSource_IndexedTerrainReason"></a> IndexedTerrainReason

```csharp
public string IndexedTerrainReason { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualGeometry_World_PlanetLayerSource_InvalidBounds"></a> InvalidBounds

生成した頂点に NaN または inf があり、実際の bounds を使わなかった Cell の累計(0 が正常)。

```csharp
public int InvalidBounds { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_LastDescribeFailedCells"></a> LastDescribeFailedCells

```csharp
public int LastDescribeFailedCells { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_LastDescribeMilliseconds"></a> LastDescribeMilliseconds

draw の準備のうち、配置(<xref href="VirtualGeometry.World.IPlanetPlacement.Describe(VirtualGeometry.World.PlanetPlacementFrame%40%2cVirtualGeometry.World.PlanetCellFrame%40%2cUnityEngine.Matrix4x4%40%2cUnityEngine.Matrix4x4%40%2cUnityEngine.MaterialPropertyBlock)" data-throw-if-not-resolved="false"></xref>)と、Cell ごとの値(<xref href="VirtualGeometry.World.PlanetLayerSource.WriteCellProperties(UnityEngine.MaterialPropertyBlock%2cSystem.Int32%2cVirtualGeometry.World.PlanetCellFrame%40)" data-throw-if-not-resolved="false"></xref>)の分(ミリ秒、診断用)。

```csharp
public float LastDescribeMilliseconds { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetLayerSource_LastDrawnCells"></a> LastDrawnCells

直近の draw の選択で、draw にした Cell の数(診断用)。

```csharp
public int LastDrawnCells { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_LastFlushMilliseconds"></a> LastFlushMilliseconds

```csharp
public float LastFlushMilliseconds { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetLayerSource_LastGpuResidencyReadyPatchEntries"></a> LastGpuResidencyReadyPatchEntries

```csharp
public int LastGpuResidencyReadyPatchEntries { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_LastGpuResidencyTablePatchEntries"></a> LastGpuResidencyTablePatchEntries

```csharp
public int LastGpuResidencyTablePatchEntries { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_LastMorphedCells"></a> LastMorphedCells

直近の frame で、寄せる割合が 0 でなかった Cell の数と、寄せられなかった(親が無い・接地)Cell の数(診断用)。

```csharp
public int LastMorphedCells { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_LastNotReadyCells"></a> LastNotReadyCells

直近の draw の選択で、選んだ Cell のうち、slot が使えなかった数と、配置が描けなかった数(診断用。どちらも 0 が正常)。

```csharp
public int LastNotReadyCells { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_LastPredictionLatencySeconds"></a> LastPredictionLatencySeconds

```csharp
public double LastPredictionLatencySeconds { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetLayerSource_LastPrepareMilliseconds"></a> LastPrepareMilliseconds

```csharp
public float LastPrepareMilliseconds { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetLayerSource_LastProjectionScale"></a> LastProjectionScale

直近の選択の診断: 射影の倍率（画面の高さ ÷ 2 tan(視野角 ÷ 2)）と、選んだ Cell の階層ごとの数（"階層:数" をコンマで）。

```csharp
public float LastProjectionScale { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetLayerSource_LastPropertiesMilliseconds"></a> LastPropertiesMilliseconds

```csharp
public float LastPropertiesMilliseconds { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetLayerSource_LastSelectFrame"></a> LastSelectFrame

直近の選択の frame 番号（選択が毎 frame 走っているかの診断用）。

```csharp
public int LastSelectFrame { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_LastSelectMilliseconds"></a> LastSelectMilliseconds

直近の draw の選択で、Cell の選択(<xref href="VirtualGeometry.World.PlanetCellSelector.Select(VirtualGeometry.World.PlanetSelectionView%40%2cVirtualGeometry.World.IPlanetCellResidency%2cSystem.Collections.Generic.ISet%7bVirtualGeometry.World.PlanetCellKey%7d%2cSystem.Collections.Generic.List%7bVirtualGeometry.World.PlanetCellKey%7d%2cSystem.Collections.Generic.ISet%7bVirtualGeometry.World.PlanetCellKey%7d)" data-throw-if-not-resolved="false"></xref>)、要求の割り当て、draw の準備にかかった CPU 時間(ミリ秒、診断用)。

```csharp
public float LastSelectMilliseconds { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetLayerSource_LastSelected"></a> LastSelected

直近の選択で選んだ Cell(まだ描けない Cell を含む。描いた数は <xref href="VirtualGeometry.World.PlanetLayerSource.LastDrawnCells" data-throw-if-not-resolved="false"></xref>)。

```csharp
public IReadOnlyList<PlanetCellKey> LastSelected { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)\>

### <a id="VirtualGeometry_World_PlanetLayerSource_LastUnmorphableCells"></a> LastUnmorphableCells

```csharp
public int LastUnmorphableCells { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_LodBudgetMode"></a> LodBudgetMode

既定は固定測定。変更は次のframeの最初の選択で反映する。

```csharp
public PlanetLodBudgetMode LodBudgetMode { get; set; }
```

#### 値（Property Value）

 [PlanetLodBudgetMode](VirtualGeometry.World.PlanetLodBudgetMode.md)

### <a id="VirtualGeometry_World_PlanetLayerSource_LodBudgetMultiplier"></a> LodBudgetMultiplier

```csharp
public float LodBudgetMultiplier { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetLayerSource_MaximumLevel"></a> MaximumLevel

```csharp
public int MaximumLevel { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_PinnedCells"></a> PinnedCells

```csharp
public int PinnedCells { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_PredictedSelection"></a> PredictedSelection

```csharp
public IReadOnlyList<PlanetCellKey> PredictedSelection { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)\>

### <a id="VirtualGeometry_World_PlanetLayerSource_PredictionCapacity"></a> PredictionCapacity

```csharp
public int PredictionCapacity { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_PredictionEnabled"></a> PredictionEnabled

SolarSystem等、明示した利用者だけが予測要求を使う。既存の描画選択には影響しない。

```csharp
public bool PredictionEnabled { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetLayerSource_PredictionLevelsBeyondGenerated"></a> PredictionLevelsBeyondGenerated

先読み(<xref href="VirtualGeometry.World.PlanetLayerSource.Predict(VirtualGeometry.World.PlanetSelectionView%40%2cSystem.Single)" data-throw-if-not-resolved="false"></xref>・<xref href="VirtualGeometry.World.PlanetLayerSource.PredictRequired(VirtualGeometry.World.PlanetSelectionView%40%2cSystem.Single%2cSystem.Boolean)" data-throw-if-not-resolved="false"></xref>)が細分化してよい深さ。負(既定)なら制限なし(理想の cut)。
0 以上なら、生成済みの Cell からこの段数先の Cell までしか選ばない(描画の選択が 1 段ずつ降りるのと同じ形)。
まだ作っていない Cell は、高さの範囲が分からないので起伏の振幅いっぱいの保守的な範囲で選ばれる。カメラが振幅より地表に近いと、
その範囲がカメラを含んで画面誤差が無限になり、最も細かい段まで選んでしまう(EarthToMoon の降下で描画の約 6 倍の Cell)。
深さを限れば、生成済みの Cell の実際の範囲で次の段を決められる。高さの範囲を返せる供給元(UseLocalHeightBounds)では要らない。

```csharp
public int PredictionLevelsBeyondGenerated { get; set; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_PredictionOwnedCells"></a> PredictionOwnedCells

```csharp
public int PredictionOwnedCells { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_ProceduralSourceMeters"></a> ProceduralSourceMeters

元標高画素の間隔。0は手続き細部分割を使わない。

```csharp
public float ProceduralSourceMeters { get; set; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetLayerSource_Radius"></a> Radius

惑星の半径 R(高さ 0 の球面。Cell の原点はこの球面から <xref href="VirtualGeometry.World.PlanetCellFrame.HeightShift" data-throw-if-not-resolved="false"></xref> だけ持ち上げた点)。

```csharp
public abstract float Radius { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetLayerSource_RequiredReservationCells"></a> RequiredReservationCells

SolarSystemの直近経路で、描画・接地とは別に保護した生成用の集合。

```csharp
public int RequiredReservationCells { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_RequiredReservationGeneration"></a> RequiredReservationGeneration

```csharp
public int RequiredReservationGeneration { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_RequiredSelection"></a> RequiredSelection

```csharp
public IReadOnlyCollection<PlanetCellKey> RequiredSelection { get; }
```

#### 値（Property Value）

 [IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection\-1)<[PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)\>

### <a id="VirtualGeometry_World_PlanetLayerSource_SelectedBudgetFraction"></a> SelectedBudgetFraction

1 回の選択で選ぶ Cell の数の上限（pool の slot 数に対する割合）。既定は <xref href="VirtualGeometry.World.PlanetLayerSource.SelectedCellBudgetFraction" data-throw-if-not-resolved="false"></xref>。視錐台で絞れない camera（Radial で eye が warp の中心に無い俯瞰）は
全方向の Cell を選ぶので、上限に達して近くの Cell が粗いままになることがある。その Layer は、pool に余裕のある範囲で上げる。

```csharp
public float SelectedBudgetFraction { get; set; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetLayerSource_SelectionAmplitude"></a> SelectionAmplitude

頂点が半径 R から離れうる最大の距離(選択の bounds に含める)。

```csharp
protected abstract float SelectionAmplitude { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetLayerSource_Selector"></a> Selector

```csharp
public PlanetCellSelector Selector { get; }
```

#### 値（Property Value）

 [PlanetCellSelector](VirtualGeometry.World.PlanetCellSelector.md)

### <a id="VirtualGeometry_World_PlanetLayerSource_StarvedRequests"></a> StarvedRequests

```csharp
public int StarvedRequests { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_SupportsIndexedTerrain"></a> SupportsIndexedTerrain

```csharp
protected virtual bool SupportsIndexedTerrain { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetLayerSource_TargetPixels"></a> TargetPixels

```csharp
public float TargetPixels { get; set; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetLayerSource_UsedSlots"></a> UsedSlots

```csharp
public int UsedSlots { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_UsesStandardPlacement"></a> UsesStandardPlacement

Unity の world 空間の既定の配置(<xref href="VirtualGeometry.World.StandardPlanetPlacement" data-throw-if-not-resolved="false"></xref>)を使っているか(診断用。OnEnable の時に決まる)。

```csharp
public bool UsesStandardPlacement { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetLayerSource_VisibleGenerationFirst"></a> VisibleGenerationFirst

描画中の親子・接地を先に生成し、必須先読みは未生成の祖先から段階的に要求する。

```csharp
public bool VisibleGenerationFirst { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetLayerSource_VisibleGenerationPending"></a> VisibleGenerationPending

直近の全Viewが要求した親子が未完成か。任意の遠方先読みを現在の生成より先に進めない。

```csharp
public bool VisibleGenerationPending { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetLayerSource_VisibleIndexCapacityForDiagnostics"></a> VisibleIndexCapacityForDiagnostics

```csharp
public int VisibleIndexCapacityForDiagnostics { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_VisibleWaitingCells"></a> VisibleWaitingCells

直近の frame に、描画の選択が細かくしたいのに Cell がまだ無くて待った数(重複を含む。診断用)。
0 なら、描画は望む細かさに追いついている。先読みの効果を測るのに使う。

```csharp
public int VisibleWaitingCells { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetLayerSource_BeginRequestFramePreparation_System_Collections_Generic_IReadOnlyList_System_Collections_Generic_KeyValuePair_VirtualGeometry_World_PlanetCellKey_System_Single___System_Int32_"></a> BeginRequestFramePreparation\(IReadOnlyList<KeyValuePair<PlanetCellKey, float\>\>, int\)

```csharp
protected virtual void BeginRequestFramePreparation(IReadOnlyList<KeyValuePair<PlanetCellKey, float>> requests, int limit)
```

#### 引数（Parameters）

`requests` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair\-2)<[PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md), [float](https://learn.microsoft.com/dotnet/api/system.single)\>\>

`limit` [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_CancelPrediction"></a> CancelPrediction\(\)

経路取消・セッション変更。実描画で使う資源は解放せず予測要求だけを失効させる。

```csharp
public void CancelPrediction()
```

### <a id="VirtualGeometry_World_PlanetLayerSource_CancelRequiredPrediction"></a> CancelRequiredPrediction\(\)

経路取消・Camera/地表世代の変更時に必須予約だけを解除する。現在の描画と生成結果は維持する。

```csharp
public void CancelRequiredPrediction()
```

### <a id="VirtualGeometry_World_PlanetLayerSource_ClearReferencePoint"></a> ClearReferencePoint\(\)

```csharp
public void ClearReferencePoint()
```

### <a id="VirtualGeometry_World_PlanetLayerSource_ConfigureSelection_System_Int32_System_Single_"></a> ConfigureSelection\(int, float\)

選択の設定を変える。有効なまま変えた場合は無効化して作り直す。

```csharp
protected void ConfigureSelection(int maximumLevel, float targetPixels)
```

#### 引数（Parameters）

`maximumLevel` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`targetPixels` [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetLayerSource_CreateLayout"></a> CreateLayout\(\)

全slotが使うgridとclusterの配置。poolを作るときに1回だけ読む。

```csharp
protected override VirtualGeometryGridLayout CreateLayout()
```

#### 戻り値（Returns）

 [VirtualGeometryGridLayout](VirtualizedGeometry.VirtualGeometryGridLayout.md)

### <a id="VirtualGeometry_World_PlanetLayerSource_DescribeSelectedLevels"></a> DescribeSelectedLevels\(\)

直近の選択の、階層ごとの数（"階層:数" をコンマで。呼んだ時点の選択結果から数える）。

```csharp
public string DescribeSelectedLevels()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualGeometry_World_PlanetLayerSource_GenerationDemandRank_System_Int32_"></a> GenerationDemandRank\(int\)

0=現在の描画/接地/根、1=必須の次の親子、2=任意先読み、3=失効した要求。

```csharp
protected int GenerationDemandRank(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_GenerationVersion_System_Int32_"></a> GenerationVersion\(int\)

```csharp
protected override int GenerationVersion(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_IsPredictionOnly_VirtualGeometry_World_PlanetCellKey__"></a> IsPredictionOnly\(in PlanetCellKey\)

```csharp
protected bool IsPredictionOnly(in PlanetCellKey key)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetLayerSource_IsReady_VirtualGeometry_World_PlanetCellKey__"></a> IsReady\(in PlanetCellKey\)

頂点が生成済みで描けるか。

```csharp
public bool IsReady(in PlanetCellKey key)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetLayerSource_OnCellDrawn_System_Int32_VirtualGeometry_World_PlanetCellFrame__"></a> OnCellDrawn\(int, in PlanetCellFrame\)

この frame に描く Cell ごとに呼ぶ(時間で動く Layer が作り直しを予約するなど)。既定では何もしない。

```csharp
protected virtual void OnCellDrawn(int slot, in PlanetCellFrame frame)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`frame` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

### <a id="VirtualGeometry_World_PlanetLayerSource_OnDeferredSlotReady_System_Int32_VirtualGeometry_World_PlanetGpuGenerationResult__"></a> OnDeferredSlotReady\(int, in PlanetGpuGenerationResult\)

```csharp
protected override void OnDeferredSlotReady(int slot, in PlanetGpuGenerationResult result)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`result` [PlanetGpuGenerationResult](VirtualGeometry.World.PlanetGpuGenerationResult.md)

### <a id="VirtualGeometry_World_PlanetLayerSource_OnDisable"></a> OnDisable\(\)

```csharp
protected override void OnDisable()
```

### <a id="VirtualGeometry_World_PlanetLayerSource_OnEnable"></a> OnEnable\(\)

```csharp
protected override void OnEnable()
```

### <a id="VirtualGeometry_World_PlanetLayerSource_OnSlotReadinessChanged_System_Int32_"></a> OnSlotReadinessChanged\(int\)

割当中のslotのready変更。GPU選択の差分producerへ通知する。通常の描画はこの通知を待たない。

```csharp
protected override void OnSlotReadinessChanged(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_PollRequired_System_Int32_System_Single_"></a> PollRequired\(int, float\)

既存予約の生成だけを進める。新しいViewの移動許可には必ずPredictRequiredで再検証する。

```csharp
public PlanetPredictionResult PollRequired(int generation, float priority = 1)
```

#### 引数（Parameters）

`generation` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`priority` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [PlanetPredictionResult](VirtualGeometry.World.PlanetPredictionResult.md)

### <a id="VirtualGeometry_World_PlanetLayerSource_Predict_VirtualGeometry_World_PlanetSelectionView__System_Single_"></a> Predict\(in PlanetSelectionView, float\)

将来Viewの必要Cellを調べ、低優先度で生成を予約する。実描画の履歴・選択・診断を変更しない。

```csharp
public PlanetPredictionResult Predict(in PlanetSelectionView view, float priority = 0.25)
```

#### 引数（Parameters）

`view` [PlanetSelectionView](VirtualGeometry.World.PlanetSelectionView.md)

`priority` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [PlanetPredictionResult](VirtualGeometry.World.PlanetPredictionResult.md)

### <a id="VirtualGeometry_World_PlanetLayerSource_PredictRequired_VirtualGeometry_World_PlanetSelectionView__System_Single_System_Boolean_"></a> PredictRequired\(in PlanetSelectionView, float, bool\)

直近の移動先を通常描画と同じ選択予算で評価し、葉と生成に必要な祖先・4兄弟をまとめて予約する。
appendは同じ経路区間の複数Viewを結合するときだけtrue。容量不足なら前の予約を維持し、部分予約しない。

```csharp
public PlanetPredictionResult PredictRequired(in PlanetSelectionView view, float priority = 1, bool append = false)
```

#### 引数（Parameters）

`view` [PlanetSelectionView](VirtualGeometry.World.PlanetSelectionView.md)

`priority` [float](https://learn.microsoft.com/dotnet/api/system.single)

`append` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [PlanetPredictionResult](VirtualGeometry.World.PlanetPredictionResult.md)

### <a id="VirtualGeometry_World_PlanetLayerSource_ProbeDrawableCut_VirtualGeometry_World_PlanetSelectionView__UnityEngine_Camera_"></a> ProbeDrawableCut\(in PlanetSelectionView, Camera\)

既存resident親で覆えるcutだけを読む。要求、Touch、通常Cameraの履歴を変更しない。

```csharp
public PlanetDrawableCutReadiness ProbeDrawableCut(in PlanetSelectionView view, Camera camera = null)
```

#### 引数（Parameters）

`view` [PlanetSelectionView](VirtualGeometry.World.PlanetSelectionView.md)

`camera` Camera

#### 戻り値（Returns）

 [PlanetDrawableCutReadiness](VirtualGeometry.World.PlanetDrawableCutReadiness.md)

### <a id="VirtualGeometry_World_PlanetLayerSource_Rebuild"></a> Rebuild\(\)

有効なら無効化して作り直す(形の設定を変えたとき)。

```csharp
protected void Rebuild()
```

### <a id="VirtualGeometry_World_PlanetLayerSource_ReleaseGpuResidencyConsumer_System_Int32_"></a> ReleaseGpuResidencyConsumer\(int\)

使わなくなったCamera等のconsumerを外す。読取り中の資源はcallbackまで保持する。

```csharp
public void ReleaseGpuResidencyConsumer(int consumer)
```

#### 引数（Parameters）

`consumer` [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_ReportLodBudgetSample_VirtualGeometry_World_PlanetLodBudgetSample__"></a> ReportLodBudgetSample\(in PlanetLodBudgetSample\)

同じLayerの全Cameraの予算をまとめて報告する。最初の選択後の報告は次frameへ持ち越す。欠測はnull。

```csharp
public void ReportLodBudgetSample(in PlanetLodBudgetSample sample)
```

#### 引数（Parameters）

`sample` [PlanetLodBudgetSample](VirtualGeometry.World.PlanetLodBudgetSample.md)

### <a id="VirtualGeometry_World_PlanetLayerSource_Request_VirtualGeometry_World_PlanetCellKey__System_Single_"></a> Request\(in PlanetCellKey, float\)

生成を要求する。priority が大きいほど先に生成する。

```csharp
public void Request(in PlanetCellKey key, float priority)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

`priority` [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetLayerSource_RequiresCpuGeneration_System_Int32_"></a> RequiresCpuGeneration\(int\)

```csharp
protected override bool RequiresCpuGeneration(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetLayerSource_SelectedForCamera_UnityEngine_Camera_"></a> SelectedForCamera\(Camera\)

指定Cameraの直近の選択。別のScene Viewの選択をGame Viewの観測へ混ぜない。

```csharp
public IReadOnlyList<PlanetCellKey> SelectedForCamera(Camera camera)
```

#### 引数（Parameters）

`camera` Camera

#### 戻り値（Returns）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)\>

### <a id="VirtualGeometry_World_PlanetLayerSource_SetContactRegions_System_Collections_Generic_IReadOnlyList_VirtualGeometry_World_PlanetContactRegion__System_Boolean_"></a> SetContactRegions\(IReadOnlyList<PlanetContactRegion\>, bool\)

接地の領域(惑星のローカル座標の点、半径 m、Cell の階層)。領域に掛かる Cell は、描くときにちょうどこの階層まで細かくし、それより細かくしない
(描く三角形が、接地の計算(<xref href="VirtualGeometry.World.PlanetTerrainContact" data-throw-if-not-resolved="false"></xref>)に使った三角形と同じになる)。領域の Cell は毎 frame 使ったことにして退避させない。

```csharp
public void SetContactRegions(IReadOnlyList<PlanetContactRegion> regions, bool prefetch = false)
```

#### 引数（Parameters）

`regions` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[PlanetContactRegion](VirtualGeometry.World.PlanetContactRegion.md)\>

`prefetch` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

true なら、領域の Cell へ降りる道（<xref href="VirtualGeometry.World.PlanetCellLocator.AddDescentPath(VirtualGeometry.World.PlanetCellKey%40%2cSystem.Collections.Generic.HashSet%7bVirtualGeometry.World.PlanetCellKey%7d)" data-throw-if-not-resolved="false"></xref>）も先に生成して残す。
領域が画面に入る前（月が遠く、視錐台の外）でも、入った時点で領域の階層まで降りられる。1 つの領域でおよそ 階層数 × 4 の slot を使う。

### <a id="VirtualGeometry_World_PlanetLayerSource_SetReferencePoint_Omni_Logical_Vector3__"></a> SetReferencePoint\(in Vector3\)

基準点(惑星のローカル座標、Logical)を決める。shader は Cell の原点からの差を、基準点からの差(_PlanetCellRef)として受け取れる。
基準点の近くの模様(目盛りなど)を、惑星の大きさによらず mm の精度で描くために使う。

```csharp
public void SetReferencePoint(in Vector3 planetLocalPoint)
```

#### 引数（Parameters）

`planetLocalPoint` Vector3

### <a id="VirtualGeometry_World_PlanetLayerSource_SetSlotBounds_System_Int32_UnityEngine_Vector4_"></a> SetSlotBounds\(int, Vector4\)

slot の Cell の実際の bounds(Cell の原点からの中心 xyz、半径 w)を設定する。頂点を CPU で作る派生クラスが、生成と同時に設定する
(GPU からの読み戻しを待たない)。

```csharp
protected void SetSlotBounds(int slot, Vector4 bounds)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`bounds` Vector4

### <a id="VirtualGeometry_World_PlanetLayerSource_SkipDraw_System_Int32_"></a> SkipDraw\(int\)

slot の Cell を、この frame は draw にしない(描いても描かなくても画像が変わらないと、派生クラスが保証できるとき true)。
飛ばした Cell は <xref href="VirtualGeometry.World.PlanetLayerSource.OnCellDrawn(System.Int32%2cVirtualGeometry.World.PlanetCellFrame%40)" data-throw-if-not-resolved="false"></xref> も呼ばない。既定は false。

```csharp
protected virtual bool SkipDraw(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetLayerSource_SlotTouchedFrame_System_Int32_"></a> SlotTouchedFrame\(int\)

slot を最後に使った(要求・選択した) frame。生成を待つ slot の優先順位(新しいものから)に使う。

```csharp
protected int SlotTouchedFrame(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_SlotVersion_System_Int32_"></a> SlotVersion\(int\)

slot が今割り当てられている Cell の世代(slot を別の Cell に使い直すと変わる。生成の結果を、作り始めたときの Cell と照合するのに使う)。

```csharp
protected int SlotVersion(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayerSource_Touch_VirtualGeometry_World_PlanetCellKey__"></a> Touch\(in PlanetCellKey\)

この frame で使った(退避しない)。

```csharp
public void Touch(in PlanetCellKey key)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

### <a id="VirtualGeometry_World_PlanetLayerSource_TryCellHeightRange_VirtualGeometry_World_PlanetCellFrame__System_Double__System_Double__"></a> TryCellHeightRange\(in PlanetCellFrame, out double, out double\)

```csharp
protected virtual bool TryCellHeightRange(in PlanetCellFrame frame, out double minimum, out double maximum)
```

#### 引数（Parameters）

`frame` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

`minimum` [double](https://learn.microsoft.com/dotnet/api/system.double)

`maximum` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetLayerSource_TryCellHeightShift_VirtualGeometry_World_PlanetCellFrame__System_Single__"></a> TryCellHeightShift\(in PlanetCellFrame, out float\)

Cell の原点を半径 R の球面から外向きに持ち上げる高さ(m)。頂点は持ち上げた原点からの相対位置になり、起伏の大きな天体でも高さ方向の成分が小さく保たれる。
同じ Cell には常に同じ値を返すこと。既定は 0(持ち上げない)。sphereFrame は持ち上げていない Cell の値(<xref href="VirtualGeometry.World.PlanetCellFrame.SphereOrigin" data-throw-if-not-resolved="false"></xref> など)。

```csharp
protected virtual bool TryCellHeightShift(in PlanetCellFrame sphereFrame, out float shift)
```

#### 引数（Parameters）

`sphereFrame` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

`shift` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetLayerSource_TryGetBounds_VirtualGeometry_World_PlanetCellKey__UnityEngine_Vector3__System_Single__"></a> TryGetBounds\(in PlanetCellKey, out Vector3, out float\)

生成した頂点から求めた実際の bounds。中心は Cell の原点(<xref href="VirtualGeometry.World.PlanetCellFrame.Origin" data-throw-if-not-resolved="false"></xref>、地表の高さまで持ち上げた点)からの相対位置。
まだ無ければ false(解析的な bounds を使う)。

```csharp
public bool TryGetBounds(in PlanetCellKey key, out Vector3 offset, out float radius)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

`offset` Vector3

`radius` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetLayerSource_TryGetIndexedDrawDiagnostics_UnityEngine_Camera_VirtualGeometry_World_PlanetIndexedDrawDiagnostics__System_String__"></a> TryGetIndexedDrawDiagnostics\(Camera, out PlanetIndexedDrawDiagnostics, out string\)

指定CameraのForward描画引数。frame付きの過去sampleで、失敗はerrorで区別する。

```csharp
public bool TryGetIndexedDrawDiagnostics(Camera camera, out PlanetIndexedDrawDiagnostics sample, out string error)
```

#### 引数（Parameters）

`camera` Camera

`sample` [PlanetIndexedDrawDiagnostics](VirtualGeometry.World.PlanetIndexedDrawDiagnostics.md)

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetLayerSource_TryGetNavigationLocalBounds_UnityEngine_Bounds__"></a> TryGetNavigationLocalBounds\(out Bounds\)

Scene View の接近・飛行の基準になる大きさ(Renderer を持たないので宣言する)。既定は、この GameObject の原点を中心にした
半径 R+振幅の球を包む立方体。形が違う派生クラスは上書きする。

```csharp
public virtual bool TryGetNavigationLocalBounds(out Bounds localBounds)
```

#### 引数（Parameters）

`localBounds` Bounds

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetLayerSource_TryGetRequestFrame_VirtualGeometry_World_PlanetCellKey__VirtualGeometry_World_PlanetCellFrame__"></a> TryGetRequestFrame\(in PlanetCellKey, out PlanetCellFrame\)

```csharp
protected virtual bool TryGetRequestFrame(in PlanetCellKey key, out PlanetCellFrame frame)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

`frame` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetLayerSource_TryGetSlotForDiagnostics_VirtualGeometry_World_PlanetCellKey__System_Int32__"></a> TryGetSlotForDiagnostics\(in PlanetCellKey, out int\)

検証用。Cell が割り当てられている slot。

```csharp
protected bool TryGetSlotForDiagnostics(in PlanetCellKey key, out int slot)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetLayerSource_TryGetSlotFrame_System_Int32_VirtualGeometry_World_PlanetCellFrame__"></a> TryGetSlotFrame\(int, out PlanetCellFrame\)

slot が今割り当てられている Cell の中心の値(生成に使う値)。slot が使われていなければ false。

```csharp
protected bool TryGetSlotFrame(int slot, out PlanetCellFrame frame)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`frame` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetLayerSource_TryProbeGpuResidency_System_Int32_System_Collections_Generic_IReadOnlyList_VirtualGeometry_World_PlanetCellKey__System_Action_VirtualGeometry_World_PlanetGpuResidentProbeResult___System_String__System_String__"></a> TryProbeGpuResidency\(int, IReadOnlyList<PlanetCellKey\>, Action<PlanetGpuResidentProbeResult\[\], string\>, out string\)

consumer別のsnapshotでkey/slot/readyを実GPUへ照合する。callbackはsnapshot時点の結果であり、描画cutの公開ではない。
戻り値falseではcallbackを呼ばない。trueでは読取り後に1度呼ぶ。Rebuild/無効化後は結果を取消理由付きで返す。

```csharp
public bool TryProbeGpuResidency(int consumer, IReadOnlyList<PlanetCellKey> queries, Action<PlanetGpuResidentProbeResult[], string> complete, out string reason)
```

#### 引数（Parameters）

`consumer` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`queries` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)\>

`complete` [Action](https://learn.microsoft.com/dotnet/api/system.action\-2)<[PlanetGpuResidentProbeResult](VirtualGeometry.World.PlanetGpuResidentProbeResult.md)\[\], [string](https://learn.microsoft.com/dotnet/api/system.string)\>

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetLayerSource_TryReadbackCellForDiagnostics_VirtualGeometry_World_PlanetCellKey__VirtualizedGeometry_VirtualGeometryPackedVertex____VirtualGeometry_World_PlanetCellFrame__"></a> TryReadbackCellForDiagnostics\(in PlanetCellKey, out VirtualGeometryPackedVertex\[\], out PlanetCellFrame\)

検証用。生成済みの Cell の頂点(Cell の原点からの相対位置)と、Cell の中心の値を返す。

```csharp
public bool TryReadbackCellForDiagnostics(in PlanetCellKey key, out VirtualGeometryPackedVertex[] vertices, out PlanetCellFrame frame)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

`vertices` [VirtualGeometryPackedVertex](VirtualizedGeometry.VirtualGeometryPackedVertex.md)\[\]

`frame` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetLayerSource_TryRefineGpuSelection_System_Int32_System_Collections_Generic_IReadOnlyList_VirtualGeometry_World_PlanetCellKey__System_Collections_Generic_IReadOnlyList_VirtualGeometry_World_PlanetGpuSelectionControl__VirtualGeometry_World_PlanetSelectionView__System_Int32_System_Int32_System_Action_VirtualGeometry_World_PlanetGpuSelectionRound_System_String__System_String__"></a> TryRefineGpuSelection\(int, IReadOnlyList<PlanetCellKey\>, IReadOnlyList<PlanetGpuSelectionControl\>, in PlanetSelectionView, int, int, Action<PlanetGpuSelectionRound, string\>, out string\)

準備済みcutでGPUの誤差判定と分割1回を実行し、不足する子を実Layerへ要求する。
継ぎ目許可はcontrolsで明示する。CPUが準備する相対bounds/Display入力と全候補readbackは移行用で、描画cutは自動で切り替えない。
trueではcallbackを1度呼ぶ。errorまたはCanPublish=falseなら前の準備済みcutを維持する。

```csharp
public bool TryRefineGpuSelection(int consumer, IReadOnlyList<PlanetCellKey> cut, IReadOnlyList<PlanetGpuSelectionControl> controls, in PlanetSelectionView view, int leafBudget, int requestCapacity, Action<PlanetGpuSelectionRound, string> complete, out string reason)
```

#### 引数（Parameters）

`consumer` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`cut` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)\>

`controls` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[PlanetGpuSelectionControl](VirtualGeometry.World.PlanetGpuSelectionControl.md)\>

`view` [PlanetSelectionView](VirtualGeometry.World.PlanetSelectionView.md)

`leafBudget` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`requestCapacity` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`complete` [Action](https://learn.microsoft.com/dotnet/api/system.action\-2)<[PlanetGpuSelectionRound](VirtualGeometry.World.PlanetGpuSelectionRound.md), [string](https://learn.microsoft.com/dotnet/api/system.string)\>

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetLayerSource_WriteCellProperties_UnityEngine_MaterialPropertyBlock_System_Int32_VirtualGeometry_World_PlanetCellFrame__"></a> WriteCellProperties\(MaterialPropertyBlock, int, in PlanetCellFrame\)

Cell の draw の MaterialPropertyBlock に、この Layer の shader が使う値を書く(配置が書く値の後に呼ぶ)。
_PlanetCellUp: xyz=Cell の原点の外向きの単位方向(object 空間)、w=Cell の原点の惑星の中心からの距離(R+HeightShift)。
_PlanetCellQuad: x=この階層の quad の弧長。
_PlanetCellRef: xyz=Cell の原点 − 基準点(<xref href="VirtualGeometry.World.PlanetLayerSource.SetReferencePoint(Omni.Logical.Vector3%40)" data-throw-if-not-resolved="false"></xref>)を Logical で引いてから float にしたもの(object 空間)、w=基準点があれば 1。
派生クラスは base を呼んでから、自分の値を足す。

```csharp
protected virtual void WriteCellProperties(MaterialPropertyBlock block, int slot, in PlanetCellFrame frame)
```

#### 引数（Parameters）

`block` MaterialPropertyBlock

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`frame` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)
