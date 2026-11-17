# <a id="VirtualGeometry_World_PlanetCellSelector"></a> Class PlanetCellSelector

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

カメラから見て描く Cell を選ぶ。6つの root から深さ優先で辿り、次の順に決める。
1. bounds で、視錐台と地平線の外なら描かない。bounds は、生成済みの Cell なら実際の頂点から求めたもの、
   無ければ解析的なもの(半径 R±Hmax で Cell を囲む球。惑星全体の高さの幅を含むので大きい)。
2. 画面上の quad の大きさ(弧長×投影÷距離)がしきい値を超え、最大階層より浅ければ細分化を望む。
   しきい値は前の frame に細分化していた Cell では (1−ヒステリシス) 倍、それ以外は (1+ヒステリシス) 倍。
3. 子4つがすべて生成済みなら子へ進み、そうでなければ自分を描いて子の生成を要求する(親は子が揃うまで描き続ける)。
4. 2:1 制約: 隣が2段以上細かい Cell は細分化する(子が揃っていなければ、描いたまま要求だけ出す)。
root が生成済みでなければ、その面は描かない(穴を見せない)。
bounds の中心は Cell の原点(Logical)からの相対位置で持ち、カメラとの差は Logical で取る。

```csharp
public sealed class PlanetCellSelector
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetCellSelector](VirtualGeometry.World.PlanetCellSelector.md)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetCellSelector__ctor_System_Single_System_Single_System_Int32_System_Int32_System_Single_VirtualGeometry_World_PlanetHeightShiftProvider_"></a> PlanetCellSelector\(float, float, int, int, float, PlanetHeightShiftProvider\)

```csharp
public PlanetCellSelector(float radius, float heightAmplitude, int cellQuads, int maximumLevel, float skirtQuads, PlanetHeightShiftProvider heightShift = null)
```

#### 引数（Parameters）

`radius` [float](https://learn.microsoft.com/dotnet/api/system.single)

`heightAmplitude` [float](https://learn.microsoft.com/dotnet/api/system.single)

`cellQuads` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`maximumLevel` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`skirtQuads` [float](https://learn.microsoft.com/dotnet/api/system.single)

`heightShift` [PlanetHeightShiftProvider](VirtualGeometry.World.PlanetHeightShiftProvider.md)

Cell の原点を持ち上げる高さの供給元。null なら持ち上げない(原点は半径 R の球面上)。

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetCellSelector_FrameBoundsLevel"></a> FrameBoundsLevel

この階層から、解析的な bounds を <xref href="VirtualGeometry.World.PlanetCellSelector.FrameBounds(VirtualGeometry.World.PlanetCellKey%40%2cUnityEngine.Vector3%40%2cSystem.Single%40)" data-throw-if-not-resolved="false"></xref> で求める(面の座標の float では角が潰れるため)。

```csharp
public const int FrameBoundsLevel = 14
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetCellSelector_PlaneFace"></a> PlaneFace

平面の root の面(<xref href="VirtualGeometry.World.CubeSphere" data-throw-if-not-resolved="false"></xref> の +Y の面と同じ向き: X が +x、Y が +z、法線 +Y)。

```csharp
public const int PlaneFace = 2
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetCellSelector_CellQuads"></a> CellQuads

```csharp
public int CellQuads { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetCellSelector_ContactRegions"></a> ContactRegions

接地の領域(<xref href="VirtualGeometry.World.PlanetContactRegion" data-throw-if-not-resolved="false"></xref>)。領域に掛かる Cell は、画面の誤差によらず、ちょうど領域の階層まで細かくし、それより細かくしない
(2:1 の均しでも細かくしない。隣との段差は skirt が隠す)。null なら無し。

```csharp
public IReadOnlyList<PlanetContactRegion> ContactRegions { get; set; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[PlanetContactRegion](VirtualGeometry.World.PlanetContactRegion.md)\>

### <a id="VirtualGeometry_World_PlanetCellSelector_ErrorMetric"></a> ErrorMetric

誤差の定義。既定は <xref href="VirtualGeometry.World.PlanetErrorMetric.QuadSize" data-throw-if-not-resolved="false"></xref>(従来どおり)。

```csharp
public PlanetErrorMetric ErrorMetric { get; set; }
```

#### 値（Property Value）

 [PlanetErrorMetric](VirtualGeometry.World.PlanetErrorMetric.md)

### <a id="VirtualGeometry_World_PlanetCellSelector_Extent"></a> Extent

平面の一辺(m)。球では 0。

```csharp
public float Extent { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetCellSelector_HeightAmplitude"></a> HeightAmplitude

```csharp
public float HeightAmplitude { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetCellSelector_HeightRange"></a> HeightRange

```csharp
public PlanetHeightRangeProvider HeightRange { get; set; }
```

#### 値（Property Value）

 [PlanetHeightRangeProvider](VirtualGeometry.World.PlanetHeightRangeProvider.md)

### <a id="VirtualGeometry_World_PlanetCellSelector_Hysteresis"></a> Hysteresis

```csharp
public float Hysteresis { get; set; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetCellSelector_IsPlane"></a> IsPlane

平面の選択か(球の選択なら false)。

```csharp
public bool IsPlane { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetCellSelector_LastBudgetLimitedRefinements"></a> LastBudgetLimitedRefinements

直近の選択で、葉数予算のため細分化できなかった枝数。

```csharp
public int LastBudgetLimitedRefinements { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetCellSelector_LogicalRadius"></a> LogicalRadius

```csharp
public Scalar LogicalRadius { get; }
```

#### 値（Property Value）

 Scalar

### <a id="VirtualGeometry_World_PlanetCellSelector_MaximumLevel"></a> MaximumLevel

```csharp
public int MaximumLevel { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetCellSelector_MaximumSelectedCells"></a> MaximumSelectedCells

1 回の選択で選ぶ Cell（葉）の数の上限（0 は無制限）。細分化は、これを超えるなら行わず（その Cell を描いて子を要求しない）、必要な Cell の集合が pool の容量を超えて
細分化の要求が割り当てられないまま固まるのを避ける（WebGPU の pool は 935 スロットで、平面の遠方が階層 7 で固まった: README の WebGPU の節）。
接地の領域の細分化には掛けない（精度の約束のため）。選択済みと積んだ Cell の数に、この Cell を 4 つの子へ替える分を足して数える。

```csharp
public int MaximumSelectedCells { get; set; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetCellSelector_MinimumGrazingSine"></a> MinimumGrazingSine

<xref href="VirtualGeometry.World.PlanetErrorMetric.ProjectedArea" data-throw-if-not-resolved="false"></xref> で、視線と地面のなす角の正弦の下限。1 なら <xref href="VirtualGeometry.World.PlanetErrorMetric.QuadSize" data-throw-if-not-resolved="false"></xref> と同じ。

```csharp
public float MinimumGrazingSine { get; set; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetCellSelector_ProceduralSourceMeters"></a> ProceduralSourceMeters

手続き細部の元データ間隔(m)。0なら従来の画面誤差だけを使う。

```csharp
public float ProceduralSourceMeters { get; set; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetCellSelector_Radius"></a> Radius

```csharp
public float Radius { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetCellSelector_SkirtQuads"></a> SkirtQuads

skirt を quad の弧長の何倍だけ下げるか。bounds に含める。

```csharp
public float SkirtQuads { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetCellSelector_TargetPixels"></a> TargetPixels

画面上の quad の大きさの目標(px)。

```csharp
public float TargetPixels { get; set; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetCellSelector_Bounds_VirtualGeometry_World_PlanetCellKey__UnityEngine_Vector3__System_Single__"></a> Bounds\(in PlanetCellKey, out Vector3, out float\)

Cell の解析的な bounds。中心は Cell の原点からの相対位置。粗い階層は <xref href="VirtualGeometry.World.PlanetCellSelector.SampledBounds(VirtualGeometry.World.PlanetCellKey%40%2cUnityEngine.Vector3%40%2cSystem.Single%40)" data-throw-if-not-resolved="false"></xref>、細かい階層は <xref href="VirtualGeometry.World.PlanetCellSelector.FrameBounds(VirtualGeometry.World.PlanetCellKey%40%2cUnityEngine.Vector3%40%2cSystem.Single%40)" data-throw-if-not-resolved="false"></xref>。

```csharp
public void Bounds(in PlanetCellKey key, out Vector3 offset, out float radius)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

`offset` Vector3

`radius` [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetCellSelector_CreatePlane_System_Single_System_Single_System_Int32_System_Int32_System_Single_"></a> CreatePlane\(float, float, int, int, float\)

一辺 extent(m)の正方形の平面を、球の代わりに分ける選択。root は 1 つ(<xref href="VirtualGeometry.World.PlanetCellSelector.PlaneFace" data-throw-if-not-resolved="false"></xref>)で、局所座標の XZ の原点が正方形の中心。
球と違い、地平線で落とさず、Cell の原点は持ち上げず、1 quad の長さは extent·2^-L/N。<xref href="VirtualGeometry.World.PlanetCellSelector.Radius" data-throw-if-not-resolved="false"></xref> は extent の半分(正方形に外接しない、大きさの目安)。
平面の root の縁の <xref href="VirtualGeometry.World.PlanetCellKey.Neighbor(System.Int32)" data-throw-if-not-resolved="false"></xref> は別の面の Key を返すが、その Key は選ばれないので 2:1 の均しには影響しない。

```csharp
public static PlanetCellSelector CreatePlane(float extent, float heightAmplitude, int cellQuads, int maximumLevel, float skirtQuads)
```

#### 引数（Parameters）

`extent` [float](https://learn.microsoft.com/dotnet/api/system.single)

`heightAmplitude` [float](https://learn.microsoft.com/dotnet/api/system.single)

`cellQuads` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`maximumLevel` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`skirtQuads` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [PlanetCellSelector](VirtualGeometry.World.PlanetCellSelector.md)

### <a id="VirtualGeometry_World_PlanetCellSelector_FaceRange_VirtualGeometry_World_PlanetCellKey__System_Single__System_Single__System_Single__"></a> FaceRange\(in PlanetCellKey, out float, out float, out float\)

Cell の面の座標の範囲(s0、t0、size)。float なので細かい階層では潰れる(形には使わない)。

```csharp
public static void FaceRange(in PlanetCellKey key, out float s0, out float t0, out float size)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

`s0` [float](https://learn.microsoft.com/dotnet/api/system.single)

`t0` [float](https://learn.microsoft.com/dotnet/api/system.single)

`size` [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetCellSelector_Frame_VirtualGeometry_World_PlanetCellKey__"></a> Frame\(in PlanetCellKey\)

Cell の中心の値。原点は、高さの供給元があれば地表の高さまで持ち上げた点、無ければ半径 R の球面上の点。求めた値は覚えておく。
持ち上げる高さが有限でない、または |高さ| ≥ R のときは持ち上げない。

```csharp
public PlanetCellFrame Frame(in PlanetCellKey key)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

#### 戻り値（Returns）

 [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

### <a id="VirtualGeometry_World_PlanetCellSelector_FrameBounds_VirtualGeometry_World_PlanetCellKey__UnityEngine_Vector3__System_Single__"></a> FrameBounds\(in PlanetCellKey, out Vector3, out float\)

中心を Cell の原点の方向に置き、半径を角度の幅から保守的に見積もる。細かい階層用。
等角写像では、Cell の中心から角・辺の中点までの角度は面の角度の幅 (π/2)·2^-L の最大 0.816 倍(面の角の Cell。
面の中央では √2/2 倍)なので、0.85 倍で見込む。

```csharp
public void FrameBounds(in PlanetCellKey key, out Vector3 offset, out float radius)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

`offset` Vector3

`radius` [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetCellSelector_FromCamera_VirtualGeometry_World_PlanetSelectionView__VirtualGeometry_World_PlanetCellKey__UnityEngine_Vector3_"></a> FromCamera\(in PlanetSelectionView, in PlanetCellKey, Vector3\)

Cell の原点(地表の高さまで持ち上げた点)からの相対位置 offset の点の、カメラからの相対位置(惑星のローカル座標の向き)。

```csharp
public Vector3 FromCamera(in PlanetSelectionView view, in PlanetCellKey key, Vector3 offset)
```

#### 引数（Parameters）

`view` [PlanetSelectionView](VirtualGeometry.World.PlanetSelectionView.md)

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

`offset` Vector3

#### 戻り値（Returns）

 Vector3

### <a id="VirtualGeometry_World_PlanetCellSelector_IsCulled_VirtualGeometry_World_PlanetSelectionView__UnityEngine_Vector3_System_Single_"></a> IsCulled\(in PlanetSelectionView, Vector3, float\)

視錐台の外、または惑星の地平線の向こうにあるか。center はカメラからの相対位置。

```csharp
public bool IsCulled(in PlanetSelectionView view, Vector3 center, float radius)
```

#### 引数（Parameters）

`view` [PlanetSelectionView](VirtualGeometry.World.PlanetSelectionView.md)

`center` Vector3

`radius` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetCellSelector_OriginFromCamera_VirtualGeometry_World_PlanetSelectionView__VirtualGeometry_World_PlanetCellKey__"></a> OriginFromCamera\(in PlanetSelectionView, in PlanetCellKey\)

Cell の原点のカメラからの相対位置(<xref href="VirtualGeometry.World.PlanetCellSelector.Select(VirtualGeometry.World.PlanetSelectionView%40%2cVirtualGeometry.World.IPlanetCellResidency%2cSystem.Collections.Generic.ISet%7bVirtualGeometry.World.PlanetCellKey%7d%2cSystem.Collections.Generic.List%7bVirtualGeometry.World.PlanetCellKey%7d%2cSystem.Collections.Generic.ISet%7bVirtualGeometry.World.PlanetCellKey%7d)" data-throw-if-not-resolved="false"></xref> を呼んだ後の同じ frame で、速い経路で求める。geomorph の寄せる割合の計算用)。

```csharp
public Vector3 OriginFromCamera(in PlanetSelectionView view, in PlanetCellKey key)
```

#### 引数（Parameters）

`view` [PlanetSelectionView](VirtualGeometry.World.PlanetSelectionView.md)

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

#### 戻り値（Returns）

 Vector3

### <a id="VirtualGeometry_World_PlanetCellSelector_PlaneBounds_VirtualGeometry_World_PlanetCellKey__UnityEngine_Vector3__System_Single__"></a> PlaneBounds\(in PlanetCellKey, out Vector3, out float\)

平面の Cell の bounds。Cell の原点(平面上の中心)から、高さの幅(−skirt〜+振幅)の中間を中心にして、一辺 size の正方形と高さの幅を囲む球。

```csharp
public void PlaneBounds(in PlanetCellKey key, out Vector3 offset, out float radius)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

`offset` Vector3

`radius` [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetCellSelector_PointScreenError_VirtualGeometry_World_PlanetSelectionView__System_Int32_UnityEngine_Vector3_UnityEngine_Vector3_"></a> PointScreenError\(in PlanetSelectionView, int, Vector3, Vector3\)

同じ地表点を共有するCellのmorph用の誤差。surfaceNormalはその点の単位球面法線。
E2でも親Cell中心の法線を使わず、同じ点・同じ階層なら同じ誤差になる。

```csharp
public float PointScreenError(in PlanetSelectionView view, int level, Vector3 center, Vector3 surfaceNormal)
```

#### 引数（Parameters）

`view` [PlanetSelectionView](VirtualGeometry.World.PlanetSelectionView.md)

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`center` Vector3

`surfaceNormal` Vector3

#### 戻り値（Returns）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetCellSelector_QuadArc_System_Int32_"></a> QuadArc\(int\)

この階層の1 quad の弧長(面の中央の値。等角写像なので面の中でほぼ一定)。親の半分。平面では 1 quad の長さ。

```csharp
public float QuadArc(int level)
```

#### 引数（Parameters）

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetCellSelector_ResolveTargetPixels_System_Single_System_Int32_"></a> ResolveTargetPixels\(float, int\)

元の1画素が1〜2画素へ拡大する間、形状の目標間隔を段階的に狭める。

```csharp
public float ResolveTargetPixels(float error, int level)
```

#### 引数（Parameters）

`error` [float](https://learn.microsoft.com/dotnet/api/system.single)

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetCellSelector_SampledBounds_VirtualGeometry_World_PlanetCellKey__UnityEngine_Vector3__System_Single__"></a> SampledBounds\(in PlanetCellKey, out Vector3, out float\)

面の座標(float)の角・辺の中点・中心を、半径 R−Hmax−skirt と R+Hmax の両方で囲み、標本点の間で球面が外へふくらむ分(sagitta)を足す。
粗い階層用(Cell が大きいので、惑星のローカル座標の float で原点との差を取っても誤差は Cell より十分小さい)。

```csharp
public void SampledBounds(in PlanetCellKey key, out Vector3 offset, out float radius)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

`offset` Vector3

`radius` [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetCellSelector_ScreenError_VirtualGeometry_World_PlanetSelectionView__VirtualGeometry_World_PlanetCellKey__UnityEngine_Vector3_System_Single_"></a> ScreenError\(in PlanetSelectionView, in PlanetCellKey, Vector3, float\)

画面上の誤差(px)。<xref href="VirtualGeometry.World.PlanetCellSelector.ErrorMetric" data-throw-if-not-resolved="false"></xref> が <xref href="VirtualGeometry.World.PlanetErrorMetric.QuadSize" data-throw-if-not-resolved="false"></xref> なら quad の一辺、
<xref href="VirtualGeometry.World.PlanetErrorMetric.ProjectedArea" data-throw-if-not-resolved="false"></xref> なら、一辺に sqrt(視線と地面のなす角の正弦)を掛けた値(斜めに見る地面の奥行き方向の縮みを、半分だけ見込む)。

```csharp
public float ScreenError(in PlanetSelectionView view, in PlanetCellKey key, Vector3 center, float radius)
```

#### 引数（Parameters）

`view` [PlanetSelectionView](VirtualGeometry.World.PlanetSelectionView.md)

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

`center` Vector3

`radius` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetCellSelector_ScreenError_VirtualGeometry_World_PlanetSelectionView__System_Int32_UnityEngine_Vector3_System_Single_"></a> ScreenError\(in PlanetSelectionView, int, Vector3, float\)

画面上の quad の大きさ(px)。center はカメラからの相対位置。

```csharp
public float ScreenError(in PlanetSelectionView view, int level, Vector3 center, float radius)
```

#### 引数（Parameters）

`view` [PlanetSelectionView](VirtualGeometry.World.PlanetSelectionView.md)

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`center` Vector3

`radius` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetCellSelector_Select_VirtualGeometry_World_PlanetSelectionView__VirtualGeometry_World_IPlanetCellResidency_System_Collections_Generic_ISet_VirtualGeometry_World_PlanetCellKey__System_Collections_Generic_List_VirtualGeometry_World_PlanetCellKey__System_Collections_Generic_ISet_VirtualGeometry_World_PlanetCellKey__"></a> Select\(in PlanetSelectionView, IPlanetCellResidency, ISet<PlanetCellKey\>, List<PlanetCellKey\>, ISet<PlanetCellKey\>\)

描く Cell を output に入れる。refined には今回細分化した Cell が入る(次の frame の previouslyRefined に渡す)。

```csharp
public void Select(in PlanetSelectionView view, IPlanetCellResidency residency, ISet<PlanetCellKey> previouslyRefined, List<PlanetCellKey> output, ISet<PlanetCellKey> refined)
```

#### 引数（Parameters）

`view` [PlanetSelectionView](VirtualGeometry.World.PlanetSelectionView.md)

`residency` [IPlanetCellResidency](VirtualGeometry.World.IPlanetCellResidency.md)

`previouslyRefined` [ISet](https://learn.microsoft.com/dotnet/api/system.collections.generic.iset\-1)<[PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)\>

`output` [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)\>

`refined` [ISet](https://learn.microsoft.com/dotnet/api/system.collections.generic.iset\-1)<[PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)\>

### <a id="VirtualGeometry_World_PlanetCellSelector_SetResidentFrame_VirtualGeometry_World_PlanetCellFrame__"></a> SetResidentFrame\(in PlanetCellFrame\)

予測選択へ、生成に実際に使ったCell原点を同期する。boundsと原点の基準がずれないよう差分cacheも失効する。

```csharp
public void SetResidentFrame(in PlanetCellFrame frame)
```

#### 引数（Parameters）

`frame` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

### <a id="VirtualGeometry_World_PlanetCellSelector_SkirtDepth_System_Int32_"></a> SkirtDepth\(int\)

skirt の深さ。

```csharp
public float SkirtDepth(int level)
```

#### 引数（Parameters）

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [float](https://learn.microsoft.com/dotnet/api/system.single)
