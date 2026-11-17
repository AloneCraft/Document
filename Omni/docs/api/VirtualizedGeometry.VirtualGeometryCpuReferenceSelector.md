# <a id="VirtualizedGeometry_VirtualGeometryCpuReferenceSelector"></a> Class VirtualGeometryCpuReferenceSelector

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

GPU の階層選択(<code>VirtualGeometrySelect.compute</code>)と同じ誤差式・細分化の規則・streaming の feedback の規則を持つ CPU の参照実装。
GPU の描画の選択には使わない。GPU の選択と同じ cut になること、cut に穴も重なりも無いことを、テストがこの実装で確かめる。
テストのほかには、archive の接続(VirtualGeometryConnection)が、CPU で cut を求めるのに段ごとの方式を使う。
細分化の方式(<xref href="VirtualizedGeometry.VirtualGeometryRefineMode" data-throw-if-not-resolved="false"></xref>)は GPU と同じ 3 つを持つ。

```csharp
public static class VirtualGeometryCpuReferenceSelector
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryCpuReferenceSelector](VirtualizedGeometry.VirtualGeometryCpuReferenceSelector.md)

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometryCpuReferenceSelector_CalculateScreenError_VirtualizedGeometry_VirtualGeometryHierarchyNode_VirtualizedGeometry_VirtualGeometryLodSelectionContext_"></a> CalculateScreenError\(VirtualGeometryHierarchyNode, VirtualGeometryLodSelectionContext\)

```csharp
public static float CalculateScreenError(VirtualGeometryHierarchyNode node, VirtualGeometryLodSelectionContext context)
```

#### 引数（Parameters）

`node` [VirtualGeometryHierarchyNode](VirtualizedGeometry.VirtualGeometryHierarchyNode.md)

`context` [VirtualGeometryLodSelectionContext](VirtualizedGeometry.VirtualGeometryLodSelectionContext.md)

#### 戻り値（Returns）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryCpuReferenceSelector_Select_VirtualizedGeometry_VirtualGeometryPage_VirtualizedGeometry_VirtualGeometryLodSelectionContext_System_Func_System_UInt32_System_Boolean__System_Collections_Generic_ISet_System_Int32__VirtualizedGeometry_VirtualGeometryRefineMode_"></a> Select\(VirtualGeometryPage, VirtualGeometryLodSelectionContext, Func<uint, bool\>, ISet<int\>, VirtualGeometryRefineMode\)

groupのDAGから、画面に描くclusterの集合(cut)を決める。GPUの階層選択(RefineGroups と SelectClusters)と同じ規則。
「このgroupの出力を使わず、入力(1段細かい表現)へ細分化するか」(refine)を group ごとに決め、cluster は「消費者がrefineしている ∧ 生産者がrefineしていない」ときに描く。
<xref href="VirtualizedGeometry.VirtualGeometryRefineMode.Chained" data-throw-if-not-resolved="false"></xref>: groupを粗い段から細かい段へ順に見て、refine(g) = 到達している ∧ 誤差が閾値を超える ∧ 入力を出力するgroupのpageがすべて常駐している。
到達している = gの出力clusterを入力に取るgroup(消費者)がすべてrefineしている(最粗のgroupは常に到達している)。
<xref href="VirtualizedGeometry.VirtualGeometryRefineMode.Independent" data-throw-if-not-resolved="false"></xref> と <xref href="VirtualizedGeometry.VirtualGeometryRefineMode.IndependentWithHysteresis" data-throw-if-not-resolved="false"></xref>: refine(g) = 誤差が閾値を超える ∧ ready(g)。
ready(g) = 入力を出力するgroupのpageがすべて常駐 ∧ 消費者がすべて ready(GPU では CPU が常駐から求めて常駐 buffer の後半に載せる値)。
誤差が単調(親は子の 1.25 倍以上)なら、どの方式でも閉包が成り立ち、穴も重なりも出ない。Independent はヒステリシスを使わない。

```csharp
public static VirtualGeometryLodSelectionResult Select(VirtualGeometryPage page, VirtualGeometryLodSelectionContext context, Func<uint, bool> isPageResident, ISet<int> previouslyRefined, VirtualGeometryRefineMode mode = VirtualGeometryRefineMode.Chained)
```

#### 引数（Parameters）

`page` [VirtualGeometryPage](VirtualizedGeometry.VirtualGeometryPage.md)

`context` [VirtualGeometryLodSelectionContext](VirtualizedGeometry.VirtualGeometryLodSelectionContext.md)

`isPageResident` [Func](https://learn.microsoft.com/dotnet/api/system.func\-2)<[uint](https://learn.microsoft.com/dotnet/api/system.uint32), [bool](https://learn.microsoft.com/dotnet/api/system.boolean)\>

`previouslyRefined` [ISet](https://learn.microsoft.com/dotnet/api/system.collections.generic.iset\-1)<[int](https://learn.microsoft.com/dotnet/api/system.int32)\>

`mode` [VirtualGeometryRefineMode](VirtualizedGeometry.VirtualGeometryRefineMode.md)

#### 戻り値（Returns）

 [VirtualGeometryLodSelectionResult](VirtualizedGeometry.VirtualGeometryLodSelectionResult.md)
