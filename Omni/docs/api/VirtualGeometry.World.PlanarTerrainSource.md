# <a id="VirtualGeometry_World_PlanarTerrainSource"></a> Class PlanarTerrainSource

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

平らな地面の Layer。一辺 <xref href="VirtualGeometry.World.PlanarTerrainSource.Extent" data-throw-if-not-resolved="false"></xref> の正方形の平面(局所座標の XZ、原点が正方形の中心、法線 +Y)を、
球と同じ Cell の四分木(<xref href="VirtualGeometry.World.PlanetCellSelector.CreatePlane(System.Single%2cSystem.Single%2cSystem.Int32%2cSystem.Int32%2cSystem.Single)" data-throw-if-not-resolved="false"></xref>)で分け、選んだ Cell ごとに、共有の単位格子(<xref href="VirtualGeometry.World.PlanarGridPage" data-throw-if-not-resolved="false"></xref>)の instance を
メッシュ版 VG の描画(<xref href="VirtualizedGeometry.VirtualGeometryRenderFeature" data-throw-if-not-resolved="false"></xref>)へ渡す。Cell の頂点は単位格子に Cell の大きさを掛けたもの(<xref href="VirtualizedGeometry.VirtualGeometryDrawPlacement.VertexScale" data-throw-if-not-resolved="false"></xref>)で、
頂点を Cell ごとに生成・保持しない(球は <xref href="VirtualGeometry.World.PlanetLayerSource" data-throw-if-not-resolved="false"></xref>。頂点を Cell ごとに持つ)。
Cell の原点は Logical で正確に求め(<xref href="VirtualGeometry.World.PlanetCellFrame.TryCreatePlane(VirtualGeometry.World.PlanetCellKey%40%2cOmni.Logical.Scalar%40%2cVirtualGeometry.World.PlanetCellFrame%40)" data-throw-if-not-resolved="false"></xref>)、頂点は Cell の原点からの相対位置なので、
平面が大きくても(Extent が 2^25 m でも)、Cell の中の頂点の精度は Cell の大きさに比例する。
置く空間は <xref href="VirtualGeometry.World.IPlanetPlacement" data-throw-if-not-resolved="false"></xref>(OnEnable の時に同じ GameObject にある実装。無い、または無効なら Unity の world 空間)。
材質は .vgshader 由来の VG pass を持つもの。単位格子の uv は Cell ごとに [0,1] で、Cell の面上の位置にはならない(shader が頂点の uv を使わない前提)。

```csharp
[ExecuteAlways]
public sealed class PlanarTerrainSource : MonoBehaviour, IPlanetCellResidency, INavigationBoundsSource
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[PlanarTerrainSource](VirtualGeometry.World.PlanarTerrainSource.md)

#### 実装するインターフェース（Implements）

[IPlanetCellResidency](VirtualGeometry.World.IPlanetCellResidency.md), 
INavigationBoundsSource

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanarTerrainSource_CellQuads"></a> CellQuads

```csharp
public const int CellQuads = 64
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanarTerrainSource_DefaultExtent"></a> DefaultExtent

既定の一辺(2^25 m。float で quad の長さまで正確に表せる 2 のべき乗)。

```csharp
public const float DefaultExtent = 33554432
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanarTerrainSource_GpuMaximumLevel"></a> GpuMaximumLevel

選べる最大の階層。Cell の中心の値を Logical で正確に作れる範囲(<xref href="VirtualGeometry.World.PlanetCellFrame.MaximumLevel" data-throw-if-not-resolved="false"></xref>)。

```csharp
public const int GpuMaximumLevel = 94
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanarTerrainSource_SelectedCellBudgetFraction"></a> SelectedCellBudgetFraction

1 回の選択で選ぶ Cell の数の上限を、<code>poolCapacity</code> のこの割合にする。

```csharp
public const float SelectedCellBudgetFraction = 0.2
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanarTerrainSource_EnableFrustumCulling"></a> EnableFrustumCulling

```csharp
public bool EnableFrustumCulling { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanarTerrainSource_EnableOcclusionCulling"></a> EnableOcclusionCulling

```csharp
public bool EnableOcclusionCulling { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanarTerrainSource_Extent"></a> Extent

平面の一辺(m)。

```csharp
public float Extent { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanarTerrainSource_LastDescribeFailedCells"></a> LastDescribeFailedCells

```csharp
public int LastDescribeFailedCells { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanarTerrainSource_LastDrawnCells"></a> LastDrawnCells

```csharp
public int LastDrawnCells { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanarTerrainSource_LastError"></a> LastError

共有の単位格子の準備が失敗した理由(正常なら null)。

```csharp
public string LastError { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualGeometry_World_PlanarTerrainSource_LastNotReadyCells"></a> LastNotReadyCells

直近の選択で、描けなかった Cell の数(配置を作れなかった Cell。単位格子は常に準備済み)。

```csharp
public int LastNotReadyCells { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanarTerrainSource_LastPrepareMilliseconds"></a> LastPrepareMilliseconds

```csharp
public float LastPrepareMilliseconds { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanarTerrainSource_LastProjectionScale"></a> LastProjectionScale

```csharp
public float LastProjectionScale { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanarTerrainSource_LastSelectFrame"></a> LastSelectFrame

```csharp
public int LastSelectFrame { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanarTerrainSource_LastSelectMilliseconds"></a> LastSelectMilliseconds

```csharp
public float LastSelectMilliseconds { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanarTerrainSource_LastSelected"></a> LastSelected

直近の選択で選んだ Cell(最後に選択した camera の分)。

```csharp
public IReadOnlyList<PlanetCellKey> LastSelected { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)\>

### <a id="VirtualGeometry_World_PlanarTerrainSource_Material"></a> Material

```csharp
public Material Material { get; set; }
```

#### 値（Property Value）

 Material

### <a id="VirtualGeometry_World_PlanarTerrainSource_MaximumLevel"></a> MaximumLevel

```csharp
public int MaximumLevel { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanarTerrainSource_PendingGeneration"></a> PendingGeneration

頂点を Cell ごとに生成しないので、待つ生成は常に 0(診断用の互換)。

```csharp
public int PendingGeneration { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanarTerrainSource_Selector"></a> Selector

```csharp
public PlanetCellSelector Selector { get; }
```

#### 値（Property Value）

 [PlanetCellSelector](VirtualGeometry.World.PlanetCellSelector.md)

### <a id="VirtualGeometry_World_PlanarTerrainSource_TargetPixels"></a> TargetPixels

```csharp
public float TargetPixels { get; set; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanarTerrainSource_UsesStandardPlacement"></a> UsesStandardPlacement

この GameObject に有効な配置が無く、Unity の world 空間の既定の配置を使っているか(診断用。選択の frame ごとに決まる)。

```csharp
public bool UsesStandardPlacement { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanarTerrainSource_ClearReferencePoint"></a> ClearReferencePoint\(\)

```csharp
public void ClearReferencePoint()
```

### <a id="VirtualGeometry_World_PlanarTerrainSource_Configure_System_Single_System_Int32_System_Single_"></a> Configure\(float, int, float\)

形の設定を変える。有効なまま変えた場合は無効化して作り直す。

```csharp
public void Configure(float extent, int maximumLevel, float targetPixels)
```

#### 引数（Parameters）

`extent` [float](https://learn.microsoft.com/dotnet/api/system.single)

`maximumLevel` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`targetPixels` [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanarTerrainSource_DescribeSelectedLevels"></a> DescribeSelectedLevels\(\)

直近の選択の、階層ごとの数（"階層:数" をコンマで）。

```csharp
public string DescribeSelectedLevels()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualGeometry_World_PlanarTerrainSource_RequestCullReadbackForDiagnostics_UnityEngine_Camera_System_Action_System_UInt32____"></a> RequestCullReadbackForDiagnostics\(Camera, Action<uint\[\]\>\)

検証用。camera の選択 batch が直近に数えた GPU cull の結果(全 Cell の合計)を非同期で読む。値は候補・Frustum 棄却・HZB 棄却・可視の cluster 数と、残り 2 つ(index の数、draw 数、この形式では 0)。
読めなければ null を渡す。

```csharp
public void RequestCullReadbackForDiagnostics(Camera camera, Action<uint[]> callback)
```

#### 引数（Parameters）

`camera` Camera

`callback` [Action](https://learn.microsoft.com/dotnet/api/system.action\-1)<[uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]\>

### <a id="VirtualGeometry_World_PlanarTerrainSource_SetReferencePoint_Omni_Logical_Vector3__"></a> SetReferencePoint\(in Vector3\)

基準点(平面のローカル座標、Logical)を決める。shader は Cell の原点からの差を、基準点からの差(_PlanetCellRef)として受け取れる。
基準点の近くの模様(目盛りなど)を、面の大きさによらず mm の精度で描くために使う。

```csharp
public void SetReferencePoint(in Vector3 planeLocalPoint)
```

#### 引数（Parameters）

`planeLocalPoint` Vector3

### <a id="VirtualGeometry_World_PlanarTerrainSource_TryGetNavigationLocalBounds_UnityEngine_Bounds__"></a> TryGetNavigationLocalBounds\(out Bounds\)

局所座標の XZ に一辺 <xref href="VirtualGeometry.World.PlanarTerrainSource.Extent" data-throw-if-not-resolved="false"></xref> の正方形(原点が中心)。高さは 0。

```csharp
public bool TryGetNavigationLocalBounds(out Bounds localBounds)
```

#### 引数（Parameters）

`localBounds` Bounds

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanarTerrainSource_UnsupportedReason_UnityEngine_Camera_"></a> UnsupportedReason\(Camera\)

この camera で描けない理由。描けるなら null。

```csharp
public string UnsupportedReason(Camera camera)
```

#### 引数（Parameters）

`camera` Camera

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
