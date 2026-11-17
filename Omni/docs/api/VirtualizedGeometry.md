# <a id="VirtualizedGeometry"></a> Namespace VirtualizedGeometry

### 名前空間（Namespaces）

 [VirtualizedGeometry.Editor](VirtualizedGeometry.Editor.md)

### クラス（Classes）

 [VirtualGeometryReferenceCache<T\>.Lease](VirtualizedGeometry.VirtualGeometryReferenceCache\-1.Lease.md)

 [VirtualGeometryClusterSource](VirtualizedGeometry.VirtualGeometryClusterSource.md)

実行時に Cell(slot)の頂点を作って持つ供給元の基底(球など。頂点が Cell ごとに違う地形)。CPU uploadまたは所有権を持つGPU生成で、pool の頂点 buffer(32 B の頂点を slot ごとに並べる)と、
cluster の bounds の表(layoutの格子と4辺に対応する球をslotごとに並べる)へ書く。描画は、派生クラスがメッシュ版 VG の描画(<xref href="VirtualizedGeometry.VirtualGeometryRenderFeature" data-throw-if-not-resolved="false"></xref>)へ
渡す instance で行う(階層・cull・選択は共通の単位格子の page、頂点と bounds は pool から)。
slot の頂点は frame ごとに 1 回(beginContextRendering)、予算の範囲で生成する。生成済み(ready)の slot だけを描く。

 [VirtualGeometryConnectedCut](VirtualizedGeometry.VirtualGeometryConnectedCut.md)

完全な置換cutを一つの公開単位にする。準備前には旧cutを保持する。

 [VirtualGeometryConnectedPublication](VirtualizedGeometry.VirtualGeometryConnectedPublication.md)

接続集合のCPU公開判定。snapshot使用中のpage寿命は呼出し側が保持する。既存Rendererへ自動接続はしない。

 [VirtualGeometryConnectedRegion](VirtualizedGeometry.VirtualGeometryConnectedRegion.md)

同じpageと境界パターンの準備済み三角形。LODは公開cutが決める。配列は供給元が所有し、公開後は変更しない。

 [VirtualGeometryConnection](VirtualizedGeometry.VirtualGeometryConnection.md)

汎用meshの共通局所格子と、全生成LODで保持する明示境界。Logical原点はFrameIdの外側で保持する。

 [VirtualGeometryConnectionBoundary](VirtualizedGeometry.VirtualGeometryConnectionBoundary.md)

独立archiveが共有する有向の開いた接続鎖。頂点番号はbuild入力、位置は共通local frameの正本。

 [VirtualGeometryCpuReferenceSelector](VirtualizedGeometry.VirtualGeometryCpuReferenceSelector.md)

GPU の階層選択(<code>VirtualGeometrySelect.compute</code>)と同じ誤差式・細分化の規則・streaming の feedback の規則を持つ CPU の参照実装。
GPU の描画の選択には使わない。GPU の選択と同じ cut になること、cut に穴も重なりも無いことを、テストがこの実装で確かめる。
テストのほかには、archive の接続(VirtualGeometryConnection)が、CPU で cut を求めるのに段ごとの方式を使う。
細分化の方式(<xref href="VirtualizedGeometry.VirtualGeometryRefineMode" data-throw-if-not-resolved="false"></xref>)は GPU と同じ 3 つを持つ。

 [VirtualGeometryCulling](VirtualizedGeometry.VirtualGeometryCulling.md)

GPU cullingと同じ保守規則をテスト可能なCPU関数として定義する。

 [VirtualGeometryDebugMetrics](VirtualizedGeometry.VirtualGeometryDebugMetrics.md)

VG Statsで同じassetを複数配置してもunique bytesを二重に数えない。

 [VirtualGeometryDiagnostics](VirtualizedGeometry.VirtualGeometryDiagnostics.md)

明示的に有効化した直前frameのmarker値。未取得のGPU時間はNaNとする。

 [VirtualGeometryFilePageStore](VirtualizedGeometry.VirtualGeometryFilePageStore.md)

指定offset/sizeだけを非同期FileStreamで読む。遅延注入は検証用。

 [VirtualGeometryGeometryCut](VirtualizedGeometry.VirtualGeometryGeometryCut.md)

可変数の置換入力を扱う、手続きsourceのlazyな完全cut。Cameraごとに履歴と出力を保持する。

 [VirtualGeometryGeometryRenderer](VirtualizedGeometry.VirtualGeometryGeometryRenderer.md)

手続きsourceのmeshを、通常VGのpage/pool/cull/drawへ接続する。groupごとにGameObjectを増やさない。
Moon(汎用版)のMoonオブジェクトに付き、MoonStreamingSetupがgeometry producerと材質を設定する。
Edit Mode でも動く(設定した側が Edit Mode で用意したときだけ描く。設定が無ければ何もしない)。

 [VirtualGeometryGpuBudget](VirtualizedGeometry.VirtualGeometryGpuBudget.md)

ビルド済みmeshのGPU geometry(頂点・index の pool)の、全 asset を合わせた上限。asset ごとの予算(<xref href="VirtualizedGeometry.VirtualGeometryStreamingSettings.GpuGeometryBudgetBytes" data-throw-if-not-resolved="false"></xref>)は
asset の数だけ足し合わさるので、種類の多いシーンで VRAM が際限なく増える。作る pool の大きさを、この上限の残りで抑える。
残りが root の page(最小)にも足りないときは作らず(呼び出し側が Proxy へ退避する)、理由を返す。

 [VirtualGeometryGpuSelectionSnapshot](VirtualizedGeometry.VirtualGeometryGpuSelectionSnapshot.md)

 [VirtualGeometryGridLayout](VirtualizedGeometry.VirtualGeometryGridLayout.md)

実行時生成clusterの1 slot(cell)の頂点とclusterの配置。全slotが同じ配置を使い、index値はslot内の頂点番号。
頂点はgrid((N+1)×(N+1)、行優先 v=y*(N+1)+x)の後に、4辺のskirt(辺ごとにN+1個。辺0:y=0、1:x=N、2:y=N、3:x=0、辺に沿ってx・yの増える順)を置く。
clusterはM×M quadの格子で、cell境界に接するclusterは、その辺のskirt(両面)も含む。
供給元はgridのu(x方向)・v(y方向)を、外向き法線がcross(v,u)になる向きで置く(Unityの左手系で時計回りが表)。

 [VirtualGeometryHierarchy](VirtualizedGeometry.VirtualGeometryHierarchy.md)

階層から導く共通規則。変換時のProxy生成と、streamingの常駐page決定で同じ段を使う。

 [VirtualGeometryLodSelectionResult](VirtualizedGeometry.VirtualGeometryLodSelectionResult.md)

 [VirtualGeometryMaterials](VirtualizedGeometry.VirtualGeometryMaterials.md)

地形の Cell とビルド済みメッシュ(<code>VirtualGeometryRenderer</code>)の Material が、VG 描画に使えるかを決める。
Materialのshaderが.vgshader由来でVG pass(<xref href="VirtualizedGeometry.VirtualGeometryMaterials.PassName" data-throw-if-not-resolved="false"></xref>)を持てばそのまま使う。
持たない通常のshaderは、メッシュ版に限り「VirtualGeometry/元shader名」のshader(同梱のURP標準分、または利用者が作った.vgshader)を探し、
内部Materialへpropertyとkeywordを写して使う(<xref href="VirtualizedGeometry.VirtualGeometryMaterials.TryResolve(UnityEngine.Material%2cUnityEngine.Material%40%2cSystem.Int32%40%2cSystem.String%40)" data-throw-if-not-resolved="false"></xref>)。実行時生成の供給元(地形)は.vgshaderのMaterialだけを使う(<xref href="VirtualizedGeometry.VirtualGeometryMaterials.TryResolveSource(UnityEngine.Material%2cUnityEngine.Material%40%2cSystem.Int32%40%2cSystem.String%40)" data-throw-if-not-resolved="false"></xref>)。

 [VirtualGeometryMeshAsset](VirtualizedGeometry.VirtualGeometryMeshAsset.md)

変換済みpageの小さな索引。モデルのInspectorで「Virtual Geometry」を有効にすると、インポート時にモデルのサブアセットとして作られる。
高密度の頂点配列はpage archive(VirtualGeometryPagePaths)に置く。

 [VirtualGeometryNormalMapping](VirtualizedGeometry.VirtualGeometryNormalMapping.md)

格納tangentがないv3向け、三角形の位置差とUV差からtangent/bitangentを作るCPU参照(VirtualGeometryVertexInput.hlslのVGFaceTangentと同じ式)。UV縮退時はfalse。

 [VirtualGeometryPage](VirtualizedGeometry.VirtualGeometryPage.md)

検証済みページのCPU表現。ランタイムは必要ページだけをこの単位で読み込む。

 [VirtualGeometryPageCodec](VirtualizedGeometry.VirtualGeometryPageCodec.md)

バージョン・範囲・CRC・階層不変条件を検証し、破損ページをGPUへ渡さない。

 [VirtualGeometryPagePaths](VirtualizedGeometry.VirtualGeometryPagePaths.md)

page archiveの置き場所を解決する。Editorではモデルのインポート時に生成した変換キャッシュ(Library/VirtualGeometry)を読み、
Playerではbuild時に参照分だけ収録したStreamingAssets/VirtualGeometryを読む。相対パスはどちらも"VirtualGeometry/&lt;名前&gt;.vgpage"。

 [VirtualGeometryPagePayload](VirtualizedGeometry.VirtualGeometryPagePayload.md)

GPU転送に使用する単一page。配列の所有者はstreaming controller。

 [VirtualGeometryProxyOwner](VirtualizedGeometry.VirtualGeometryProxyOwner.md)

VG描画中に影を落とす非表示の子を、元の専用Rendererから回収するための印。

 [VirtualGeometryReferenceCache<T\>](VirtualizedGeometry.VirtualGeometryReferenceCache\-1.md)

共有GPU資源の所有権を参照数とentry世代で管理し、reset後の古いleaseを無効化する。

 [VirtualGeometryRenderFeature](VirtualizedGeometry.VirtualGeometryRenderFeature.md)

VG の描画を URP の RenderGraph へ接続する。描くものは <xref href="VirtualizedGeometry.IVirtualGeometryDrawable" data-throw-if-not-resolved="false"></xref>(ビルド済みメッシュの <xref href="VirtualizedGeometry.VirtualGeometryRenderer" data-throw-if-not-resolved="false"></xref> と、
地形の Cell のように供給元 <xref href="VirtualizedGeometry.IVirtualGeometryDrawableProvider" data-throw-if-not-resolved="false"></xref> が camera ごとに渡す instance)で、どれも同じ階層選択(GPU)と間接描画を通る。
段は 3 つ。
1. prepass の直後(AfterRenderingPrePasses): 供給元の instance を、VG の深度の pass(DepthNormals か DepthOnly)で URP の prepass と同じ出力先へ描く
   (VG の面が SSAO・Decal(DBuffer)・Depth Priming の深度に入る。遮蔽の判定と 2 パス目は無い)。
2. 主光源の影: ビルド済みメッシュの cluster を cascade ごとに選び、ShadowCaster pass で影の texture へ描く。
3. 不透明の後(AfterRenderingOpaques): 階層選択、2 パスの遮蔽(前 frame に見えた cluster を先に描き、その深度の HZB で残りを判定)、forward pass の描画。
細分化の決め方は <xref href="VirtualizedGeometry.VirtualGeometryRenderFeature.RefineMode" data-throw-if-not-resolved="false"></xref>。対応しない camera では描かず、理由を残す(Fail Closed)。

 [VirtualGeometryRenderer](VirtualizedGeometry.VirtualGeometryRenderer.md)

通常のMeshFilter/MeshRendererとVirtual Geometryの描画をつなぐ非表示の部品。モデルのインポートで自動で付き、Inspectorには表示しない。
MeshFilterには低密度の代替Mesh(UE5のFallback Mesh相当)が入り、影・当たり判定・カリング・VGが使えないときの表示を受け持つ。

 [VirtualGeometryReplacement](VirtualizedGeometry.VirtualGeometryReplacement.md)

静的meshのCPU参照と手続きmeshが共有する誤差/ヒステリシス契約。

 [VirtualGeometryScreenSize](VirtualizedGeometry.VirtualGeometryScreenSize.md)

画面上の大きさ（画素）の式の正本。VG の選択（cluster の誤差、Cell の大きさ）と VO の選択（物の見かけの直径）が、この関数を呼ぶ。
同じ意味の式を別の場所に書かない（演算の順序が変わると、float の結果が bit 単位で変わり、選択の境目がずれる）。
線形の画素（<xref href="VirtualizedGeometry.VirtualGeometryScreenSize.LinearPixels(System.Single%2cSystem.Single%2cSystem.Single)" data-throw-if-not-resolved="false"></xref>）と角直径の画素（<xref href="VirtualizedGeometry.VirtualGeometryScreenSize.AngularDiameterPixels(System.Double%2cSystem.Double%2cSystem.Double%2cSystem.Double)" data-throw-if-not-resolved="false"></xref>）は同じ尺度ではない（視野角 70° で前者が約 0.87 倍）。閾値を比べるときは、どちらの画素かをそろえる。

 [VirtualGeometrySharedDrawReceipt](VirtualizedGeometry.VirtualGeometrySharedDrawReceipt.md)

 [VirtualGeometrySharedEdgeSplit](VirtualizedGeometry.VirtualGeometrySharedEdgeSplit.md)

粗い辺の隣接三角形を置き換える。細境界の同じindexを使い、元の面を重ねて残さない。

 [VirtualGeometrySharedRegion](VirtualizedGeometry.VirtualGeometrySharedRegion.md)

一つのpage/LODの明示index。配列を複製して、公開後の供給側による書換えを防ぐ。

 [VirtualGeometrySharedSnapshot](VirtualizedGeometry.VirtualGeometrySharedSnapshot.md)

Immutableなindexと共有slotの所有。retire後も、全Cameraのreceipt完了まで位置を保持する。

 [VirtualGeometrySharedVertexPool](VirtualizedGeometry.VirtualGeometrySharedVertexPool.md)

明示indexを共有位置slotへ結ぶCPU publication host。GPU backendはBeginDraw/Completeのreceiptを実描画完了に結ぶ。
このhost単独ではGPUロードを有効化しない。全てmain threadで使用する。

 [VirtualGeometryStreamCodec](VirtualizedGeometry.VirtualGeometryStreamCodec.md)

v3のmetadataを先に検証し、payloadをpage単位で独立検証する。

 [VirtualGeometryStreamMetadata](VirtualizedGeometry.VirtualGeometryStreamMetadata.md)

geometryを常駐させず走査できるarchive metadata。

 [VirtualGeometryStreamingController](VirtualizedGeometry.VirtualGeometryStreamingController.md)

小容量要求queue、実async I/O、CPU cache、chunk転送、GPU完了後のslot再利用を管理する。
GPU poolはslot(metadataの割り当て単位)に区切り、pageは自分の大きさに要る数だけ連続したslotを使う。root(page 0)は先頭のslotに置く。

 [VirtualGeometryStreamingSettings](VirtualizedGeometry.VirtualGeometryStreamingSettings.md)

M4の独立予算。上限を実行時に自動拡大しない。

 [VirtualGeometryStreamingStatistics](VirtualizedGeometry.VirtualGeometryStreamingStatistics.md)

geometry予算とmetadataを区別したM4実測値。

 [VirtualGeometryTransformSupport](VirtualizedGeometry.VirtualGeometryTransformSupport.md)

max-axis sphere が保守的になる直交TRSだけを専用経路へ渡す。

 [VirtualGeometryWebArchive](VirtualizedGeometry.VirtualGeometryWebArchive.md)

page archive(streaming 形式)の先頭から metadata を取り、streaming の controller を作るための入力を返す。

 [VirtualGeometryWebPageStore](VirtualizedGeometry.VirtualGeometryWebPageStore.md)

WebGL では File を使えない(StreamingAssets は URL)。page archive を HTTP の Range 要求で、必要な page の範囲だけ取る。
サーバーが Range を無視して全体(200)を返す場合は、返ってきた全体から範囲を切り出す。

### 構造体（Structs）

 [VirtualGeometryCluster](VirtualizedGeometry.VirtualGeometryCluster.md)

1クラスタの描画範囲。階層の置換単位はVirtualGeometryHierarchyNode(group)が保持する。
<xref href="VirtualizedGeometry.VirtualGeometryCluster.Parent" data-throw-if-not-resolved="false"></xref> はこのclusterを入力に取るgroup(消費者。最粗のgroupのclusterは -1)、<xref href="VirtualizedGeometry.VirtualGeometryCluster.ChildStart" data-throw-if-not-resolved="false"></xref> はこのclusterを出力するgroup(生産者)のnode index。

 [VirtualGeometryClusterView](VirtualizedGeometry.VirtualGeometryClusterView.md)

実行時生成clusterの供給元がcameraごとの選択で受け取る視点の情報。座標はworld空間。

 [VirtualGeometryCullSpace](VirtualizedGeometry.VirtualGeometryCullSpace.md)

cluster の cull を行う空間。world とは限らない(Omni の対数描画では、カメラ相対の物理空間)。
カメラの位置・視錐台の6平面・HZB 用の ViewProjection はすべてこの空間で表す。

 [VirtualGeometryGeometryGroup](VirtualizedGeometry.VirtualGeometryGeometryGroup.md)

生成メッシュの安定した局所配置と置換単位。IDはsourceのepoch内で再利用しない。

 [VirtualGeometryGeometryView](VirtualizedGeometry.VirtualGeometryGeometryView.md)

同じsourceを複数のCameraで選ぶための値。絶対float位置を持たない。

 [VirtualGeometryHierarchyNode](VirtualizedGeometry.VirtualGeometryHierarchyNode.md)

階層のgroup。入力clusterを束ねて外周を固定して簡略化し、出力cluster(<xref href="VirtualizedGeometry.VirtualGeometryHierarchyNode.FirstCluster" data-throw-if-not-resolved="false"></xref>、<xref href="VirtualizedGeometry.VirtualGeometryHierarchyNode.ClusterCount" data-throw-if-not-resolved="false"></xref>)を作る。
出力clusterは次の段で別のgroupへ振り分けられるので、groupの関係は木ではなくDAGになる。
<xref href="VirtualizedGeometry.VirtualGeometryHierarchyNode.GeometricError" data-throw-if-not-resolved="false"></xref> と bounds は出力(簡略化後)のもので、入力のgroupより単調に大きく、入力のgroupの球を含む。
<xref href="VirtualizedGeometry.VirtualGeometryHierarchyNode.FirstChild" data-throw-if-not-resolved="false"></xref>、<xref href="VirtualizedGeometry.VirtualGeometryHierarchyNode.ChildCount" data-throw-if-not-resolved="false"></xref> は、入力clusterを出力しているgroup(生産者)のindexが並ぶ <xref href="VirtualizedGeometry.VirtualGeometryPage.GroupLinks" data-throw-if-not-resolved="false"></xref> の範囲。
段0のgroupは入力を持たず(ChildCount=0)、leaf cluster 1つを出力する。<xref href="VirtualizedGeometry.VirtualGeometryHierarchyNode.LeafStart" data-throw-if-not-resolved="false"></xref>、<xref href="VirtualizedGeometry.VirtualGeometryHierarchyNode.LeafCount" data-throw-if-not-resolved="false"></xref> は使わない。

 [VirtualGeometryInstanceMetrics](VirtualizedGeometry.VirtualGeometryInstanceMetrics.md)

診断readback由来のinstance計測と共有resource容量を区別する。

 [VirtualGeometryInstancePose](VirtualizedGeometry.VirtualGeometryInstancePose.md)

差し込み口(<xref href="VirtualizedGeometry.IVirtualGeometryInstancePlacement" data-throw-if-not-resolved="false"></xref>)が返す、1 つの camera での姿勢。

 [VirtualGeometryLodSelectionContext](VirtualizedGeometry.VirtualGeometryLodSelectionContext.md)

 [VirtualGeometryMaterialRange](VirtualizedGeometry.VirtualGeometryMaterialRange.md)

 [VirtualGeometryPackedVertex](VirtualizedGeometry.VirtualGeometryPackedVertex.md)

C#とHLSLで共有する頂点(32 byte)。実行時生成clusterの頂点buffer(<xref href="VirtualizedGeometry.VirtualGeometryClusterSource" data-throw-if-not-resolved="false"></xref>)がこの形で持つ。

 [VirtualGeometryPageDescriptor](VirtualizedGeometry.VirtualGeometryPageDescriptor.md)

独立I/O範囲とpage-local geometryのサイズ/CRCを保持するv3 descriptor。

 [VirtualGeometryPageFeedback](VirtualizedGeometry.VirtualGeometryPageFeedback.md)

選択がstreamingへ返すpage単位のfeedback。Missingは不足pageの要求、それ以外は利用中pageの保持。

 [VirtualGeometryRenderDecision](VirtualizedGeometry.VirtualGeometryRenderDecision.md)

カメラ毎のfallback判断。専用geometryと通常Proxyの可視描画を排他的にする。

 [VirtualGeometrySelectionKey](VirtualizedGeometry.VirtualGeometrySelectionKey.md)

同じgeometryを共有しても、instanceとcameraの選択履歴は別keyで保持する。

 [VirtualGeometrySharedAttribute](VirtualizedGeometry.VirtualGeometrySharedAttribute.md)

 [VirtualGeometrySharedLocalTriangle](VirtualizedGeometry.VirtualGeometrySharedLocalTriangle.md)

GPUへ渡したfloat位置と同じ局所三角形。Logical原点は精度を保ったまま別に返す。

 [VirtualGeometrySharedTriangle](VirtualizedGeometry.VirtualGeometrySharedTriangle.md)

接地にも描画にも返す、同じ公開世代の正本三角形。

 [VirtualGeometrySharedVertex](VirtualizedGeometry.VirtualGeometrySharedVertex.md)

 [VirtualGeometrySharedVertexId](VirtualizedGeometry.VirtualGeometrySharedVertexId.md)

Sourceに依存しない正本位置の識別。隣接sourceは同じdomainと番号を合意して供給する。

 [VirtualGeometryVertexConnection](VirtualizedGeometry.VirtualGeometryVertexConnection.md)

局所meshの頂点を、共有Logical正本へ結ぶ供給側の明示参照。追加の接続頂点も同じ契約を使う。

 [VirtualGeometryWorldSphere](VirtualizedGeometry.VirtualGeometryWorldSphere.md)

### インターフェース（Interfaces）

 [IVirtualGeometryCompatibleRenderFeature](VirtualizedGeometry.IVirtualGeometryCompatibleRenderFeature.md)

互換featureはVGより前にgeometryを必要とする場合だけ、VGの描画を止める(通常の描画へ戻す)。

 [IVirtualGeometryConnectedMeshSource](VirtualizedGeometry.IVirtualGeometryConnectedMeshSource.md)

任意meshの接続、局所配置と共通描画原点を供給する口。惑星のface/XY/格子はこの実装側だけが扱う。

 [IVirtualGeometryGeometryResidency](VirtualizedGeometry.IVirtualGeometryGeometryResidency.md)

選択とpage常駐の境界。実装は通常meshと同じStreamingControllerを使用する。

 [IVirtualGeometryGeometrySource](VirtualizedGeometry.IVirtualGeometryGeometrySource.md)

静的/手続きmeshを共通page常駐へ供給する口。面・XY・四分木を共通controllerへ持ち込まない。

 [IVirtualGeometryInstancePlacement](VirtualizedGeometry.IVirtualGeometryInstancePlacement.md)

<xref href="VirtualizedGeometry.VirtualGeometryRenderer" data-throw-if-not-resolved="false"></xref> を、Transform の行列とは別の配置で描くための差し込み口(Omni の Logical 座標と対数描画など)。
同じ GameObject の component が実装する。無ければ、これまでどおり Transform の行列で world 空間に描く。
RenderFeature が camera ごと・frame ごとに、記録中(RenderGraph の記録、main thread)に呼ぶ。
返した姿勢で、LOD の選択と cull(<xref href="VirtualizedGeometry.VirtualGeometryInstancePose.CullSpace" data-throw-if-not-resolved="false"></xref> の空間)と描画(描画行列と MaterialPropertyBlock)を行う。

 [IVirtualGeometryPageStore](VirtualizedGeometry.IVirtualGeometryPageStore.md)

 [IVirtualGeometryPageUploader](VirtualizedGeometry.IVirtualGeometryPageUploader.md)

実GPU転送とstate-machine試験の境界。公開前のpartial slotは描画対象にしない。
slotはpageが使う連続slotの先頭。offsetはそこからの頂点・添字の位置で、pageの全体が連続した範囲に入る。

 [IVirtualGeometryProtectedGroups](VirtualizedGeometry.IVirtualGeometryProtectedGroups.md)

### 列挙型（Enums）

 [VirtualGeometryDebugView](VirtualizedGeometry.VirtualGeometryDebugView.md)

メッシュ版の可視化（デバッグ。Scene overlay・Monitor が選ぶ）。serialized 値を保つため、追加 mode は末尾へ置く。

 [VirtualGeometryPageState](VirtualizedGeometry.VirtualGeometryPageState.md)

 [VirtualGeometryRefineMode](VirtualizedGeometry.VirtualGeometryRefineMode.md)

cluster の DAG の細分化（どの group の出力を描くか）の決め方。値は選択の compute の <code>_VGIndependentCut</code> と同じ。
どの方式でも、cut は閉包を取り、穴も重なりも作らない（CPU 参照 <xref href="VirtualizedGeometry.VirtualGeometryCpuReferenceSelector" data-throw-if-not-resolved="false"></xref> が同じ規則を持つ）。

 [VirtualGeometryStreamingMode](VirtualizedGeometry.VirtualGeometryStreamingMode.md)
