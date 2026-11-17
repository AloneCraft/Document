# <a id="VirtualGeometry_World"></a> Namespace VirtualGeometry.World

### クラス（Classes）

 [CubeSphere](VirtualGeometry.World.CubeSphere.md)

cube-sphere の面の軸と、面の座標から球面の方向への写像(等角写像)。
面 f の点は n + a·u + b·v(a、b は −1〜1)。外向き法線は cross(v,u)=n になる向きに u・v を選ぶ
(VirtualGeometryGridLayout の三角形が外から時計回りに見える向き)。
面の番号: 0:+X、1:−X、2:+Y、3:−Y、4:+Z、5:−Z。

 [PlanarTerrainSource](VirtualGeometry.World.PlanarTerrainSource.md)

平らな地面の Layer。一辺 <xref href="VirtualGeometry.World.PlanarTerrainSource.Extent" data-throw-if-not-resolved="false"></xref> の正方形の平面(局所座標の XZ、原点が正方形の中心、法線 +Y)を、
球と同じ Cell の四分木(<xref href="VirtualGeometry.World.PlanetCellSelector.CreatePlane(System.Single%2cSystem.Single%2cSystem.Int32%2cSystem.Int32%2cSystem.Single)" data-throw-if-not-resolved="false"></xref>)で分け、選んだ Cell ごとに、共有の単位格子(<xref href="VirtualGeometry.World.PlanarGridPage" data-throw-if-not-resolved="false"></xref>)の instance を
メッシュ版 VG の描画(<xref href="VirtualizedGeometry.VirtualGeometryRenderFeature" data-throw-if-not-resolved="false"></xref>)へ渡す。Cell の頂点は単位格子に Cell の大きさを掛けたもの(<xref href="VirtualizedGeometry.VirtualGeometryDrawPlacement.VertexScale" data-throw-if-not-resolved="false"></xref>)で、
頂点を Cell ごとに生成・保持しない(球は <xref href="VirtualGeometry.World.PlanetLayerSource" data-throw-if-not-resolved="false"></xref>。頂点を Cell ごとに持つ)。
Cell の原点は Logical で正確に求め(<xref href="VirtualGeometry.World.PlanetCellFrame.TryCreatePlane(VirtualGeometry.World.PlanetCellKey%40%2cOmni.Logical.Scalar%40%2cVirtualGeometry.World.PlanetCellFrame%40)" data-throw-if-not-resolved="false"></xref>)、頂点は Cell の原点からの相対位置なので、
平面が大きくても(Extent が 2^25 m でも)、Cell の中の頂点の精度は Cell の大きさに比例する。
置く空間は <xref href="VirtualGeometry.World.IPlanetPlacement" data-throw-if-not-resolved="false"></xref>(OnEnable の時に同じ GameObject にある実装。無い、または無効なら Unity の world 空間)。
材質は .vgshader 由来の VG pass を持つもの。単位格子の uv は Cell ごとに [0,1] で、Cell の面上の位置にはならない(shader が頂点の uv を使わない前提)。

 [PlanetAmplifiedHeightProvider](VirtualGeometry.World.PlanetAmplifiedHeightProvider.md)

基の高さ(実データなど)に、その帯域より短い波長の細部を足す(増幅)。細部は 3 次元の gradient noise の octave の和で、
遮断波長 <xref href="VirtualGeometry.World.PlanetAmplifiedHeightProvider.CutoffWavelengthMeters" data-throw-if-not-resolved="false"></xref> の octave の振幅が <xref href="VirtualGeometry.World.PlanetAmplifiedHeightProvider.CutoffAmplitudeMeters" data-throw-if-not-resolved="false"></xref>、波長が半分になるごとに振幅が 2^−H 倍
(H は Hurst 指数 <xref href="VirtualGeometry.World.PlanetAmplifiedHeightProvider.Hurst" data-throw-if-not-resolved="false"></xref>。月の表面の粗さは 0.8〜0.9 程度)。最も短い波長は <xref href="VirtualGeometry.World.PlanetAmplifiedHeightProvider.MinimumWavelengthMeters" data-throw-if-not-resolved="false"></xref>。
帯域制限: 波長 λ の octave の重みは、λ がメッシュの間隔の 4 倍以上で 1、2 倍以下で 0、その間は滑らかにつなぐ(細かい Cell ほど octave が増える)。
noise は球面上の点 R·方向 の座標で評価し、格子の番号は 64 ビットの整数で持つ(半径 10^9 m・波長 1 mm でも番号が潰れない)。

 [PlanetAxisMappedHeightProvider](VirtualGeometry.World.PlanetAxisMappedHeightProvider.md)

天体のローカル座標の向きの決め方が、高さの供給元(inner)の決め方と違うときに、方向を回してから inner へ聞く。
inner の方向 = (dot(d, xRow), dot(d, yRow), dot(d, zRow))。行は互いに直交する単位ベクトル(回転)であること。
例: 北極 +Z・経度 0 が +Y・東経 90 度が +X の天体座標から、<xref href="VirtualGeometry.World.PlanetEquirectangularHeightProvider" data-throw-if-not-resolved="false"></xref>(北極 +Y・経度 0 が +X・東経 90 度が +Z)へ聞くには
<xref href="VirtualGeometry.World.PlanetAxisMappedHeightProvider.ZNorthYPrimeMeridianToEquirectangular(VirtualGeometry.World.IPlanetHeightProvider)" data-throw-if-not-resolved="false"></xref>。

 [PlanetCellDrawBudget](VirtualGeometry.World.PlanetCellDrawBudget.md)

惑星・平面の Cell を VG で描くときの、選ぶ Cell の数の上限(<xref href="VirtualGeometry.World.PlanetCellSelector.MaximumSelectedCells" data-throw-if-not-resolved="false"></xref>)と、描画の容量の対応。
描く Cell は階層選択で簡略化されず(<xref href="VirtualGeometry.World.PlanarGridPage" data-throw-if-not-resolved="false"></xref>)、1 Cell が <xref href="VirtualGeometry.World.PlanarGridPage.IndicesPerCell" data-throw-if-not-resolved="false"></xref> 個の可視 index を要る。
描画の共有 buffer(<xref href="VirtualizedGeometry.VirtualGeometrySelectionBatch" data-throw-if-not-resolved="false"></xref>)の容量は固定で、超えた cluster は黙って捨てられ、画面に穴(背景の黒)が開く
(2026-10-23: 既定の容量 16 Mi index は約 607 Cell。Moon の TargetPixels 4 は 611 Cell で境界、3 は 930 Cell で約 5 %、2 は 1796 Cell で 36 % が欠けた)。
選択の上限と容量を別々に決めると、上限の方が大きいときに穴が開くので、ここで一緒に決める:
選択の上限から、選びうる Cell の数の最大(<xref href="VirtualGeometry.World.PlanetCellDrawBudget.MaximumSelectableCells(System.Int32%2cSystem.Int32)" data-throw-if-not-resolved="false"></xref>)を求め、描画の容量をそれ以上にする。
機器の上限(<xref href="VirtualGeometry.World.PlanetCellDrawBudget.VisibleIndexLimit" data-throw-if-not-resolved="false"></xref>)を超えるときは、描画の容量を上限にして、選択の上限を下げる(粗い親を描き続ける。穴にはしない)。

 [PlanetCellLocator](VirtualGeometry.World.PlanetCellLocator.md)

方向から Cell を探す(double の精度。階層 50 程度まで区別できる)。

 [PlanetCellMeshBuilder](VirtualGeometry.World.PlanetCellMeshBuilder.md)

惑星の Cell 1 つ分の頂点(<xref href="VirtualizedGeometry.VirtualGeometryGridLayout" data-throw-if-not-resolved="false"></xref> の配置)を、高さの正本(<xref href="VirtualGeometry.World.IPlanetHeightProvider" data-throw-if-not-resolved="false"></xref>)から CPU で作る。
GPU は作った頂点をそのまま写すので、描く頂点と CPU の配列(接地の問い合わせ <xref href="VirtualGeometry.World.PlanetTerrainContact" data-throw-if-not-resolved="false"></xref> が使う)は bit 単位で同じになる。
位置は Cell の原点(<xref href="VirtualGeometry.World.PlanetCellFrame.Origin" data-throw-if-not-resolved="false"></xref>、Logical)からの相対位置で、double で求めてから float にする:
球面上の点は、中心の正接(Logical から double)と格子の角度の差から R·(p/|p| − p0/|p0|) を差だけで求め(大きな値どうしを引かない)、
高さ h と原点の持ち上げ H を足して sphere + h·n − H·u0(n は頂点の方向、u0 は Cell の中心の方向)にする。
誤差は R·2^-52 程度(月で 4×10^-10 m、地球で 1.4×10^-9 m)で、R が 10^9 m を超える天体には向かない(GPU 生成の Layer を使う)。
法線は格子の外の 1 周を含めた中心差分。陰影用の高さを持つ供給元(<xref href="VirtualGeometry.World.IPlanetShadingHeightProvider" data-throw-if-not-resolved="false"></xref>)は、その高さで法線を求める。
高さの入口は 2 つ: <xref href="VirtualGeometry.World.PlanetCellMeshBuilder.Build(VirtualGeometry.World.PlanetCellFrame%40%2cSystem.Double%2cVirtualGeometry.World.IPlanetHeightProvider%2cSystem.Double%2cSystem.Single%2cUnityEngine.Vector4%2cVirtualizedGeometry.VirtualGeometryPackedVertex%5b%5d%2cSystem.Int32%2cUnityEngine.Vector4%40%2cSystem.Double%40%2cSystem.Double%40%2cSystem.Threading.CancellationToken)" data-throw-if-not-resolved="false"></xref>(供給元を格子の各点でサンプルする)と <xref href="VirtualGeometry.World.PlanetCellMeshBuilder.BuildFromHeights(VirtualGeometry.World.PlanetCellFrame%40%2cSystem.Double%2cSystem.ReadOnlySpan%7bSystem.Double%7d%2cSystem.ReadOnlySpan%7bSystem.Double%7d%2cSystem.Single%2cUnityEngine.Vector4%2cVirtualizedGeometry.VirtualGeometryPackedVertex%5b%5d%2cSystem.Int32%2cUnityEngine.Vector4%40%2cSystem.Double%40%2cSystem.Double%40)" data-throw-if-not-resolved="false"></xref>(格子の各点の高さを配列で受け取る。
ストリーミングで届いた高さ、焼いた高さなど)。同じ高さを渡せば、2 つの結果は bit 単位で一致する。

 [PlanetCellMorph](VirtualGeometry.World.PlanetCellMorph.md)

階層の境目で細かさが跳ばないよう、Cell の頂点を親(1 つ粗い階層)の面へ連続的に寄せる(geomorph)ための、CPU 側の純関数。
頂点 shader(<code>Shaders/PlanetMorph.hlsl</code>)が同じ規則で、4 隅の寄せる割合 m(0 = 自分の形、1 = 親の面)を格子で双線形に補間し、位置と法線を寄せる。
設計: <code>Docs/Plans/VirtualGeometryNaniteMigration.md</code> §2.3.4。

 [PlanetCellNativeBuild](VirtualGeometry.World.PlanetCellNativeBuild.md)

1 CellのNative入出力とhandleの所有者。通常回収は完了確認後、取消はRetireへ渡す。

 [PlanetCellSelector](VirtualGeometry.World.PlanetCellSelector.md)

カメラから見て描く Cell を選ぶ。6つの root から深さ優先で辿り、次の順に決める。
1. bounds で、視錐台と地平線の外なら描かない。bounds は、生成済みの Cell なら実際の頂点から求めたもの、
   無ければ解析的なもの(半径 R±Hmax で Cell を囲む球。惑星全体の高さの幅を含むので大きい)。
2. 画面上の quad の大きさ(弧長×投影÷距離)がしきい値を超え、最大階層より浅ければ細分化を望む。
   しきい値は前の frame に細分化していた Cell では (1−ヒステリシス) 倍、それ以外は (1+ヒステリシス) 倍。
3. 子4つがすべて生成済みなら子へ進み、そうでなければ自分を描いて子の生成を要求する(親は子が揃うまで描き続ける)。
4. 2:1 制約: 隣が2段以上細かい Cell は細分化する(子が揃っていなければ、描いたまま要求だけ出す)。
root が生成済みでなければ、その面は描かない(穴を見せない)。
bounds の中心は Cell の原点(Logical)からの相対位置で持ち、カメラとの差は Logical で取る。

 [PlanetClusterTopology](VirtualGeometry.World.PlanetClusterTopology.md)

8×8格子と8 quadの両面skirtを、共有indexからCellの頂点配置へ写すCPU参照。

 [PlanetCraterField](VirtualGeometry.World.PlanetCraterField.md)

天体全体の生成クレーターの場(CPU の正本。GPU 版は Shaders/PlanetCraters.hlsl で、同じ定義)。

<p>
置き方: 段ごとに天体の中心に固定した 3 次元の格子(1 辺 4dMin)を置き、各マスの中央半分に候補の点 q を 1 つ置く。q の基準球からの高さ |q| − R が
[−マス/2, マス/2) のときだけクレーターにする(基準球を通るマスの層 1 枚分なので、面積あたりの数は 1 マスあたりの期待値 ÷ マス²)。
中心は q の真下の基準球の点。高さによらず基準球の方向で置くので、地形の高さが変わってもクレーターは滑らない。
画素に届くのは各軸で近い側の 2 マス(2×2×2)。半径は dMin 未満、ゆがみを含む影響半径は 2.25r 未満で、調べないマスの候補は面に沿って 2.24dMin より遠い。
</p>
<p>
分布: 直径 [dMin, 2dMin) の数は Gault(1970)の平衡分布 N(&gt;D)=10^-1.1 D^-2(個/m²)。<xref href="VirtualGeometry.World.PlanetCraterSettings.EquilibriumLimitMeters" data-throw-if-not-resolved="false"></xref> より大きい段は生成分布。
古さ: 新しい約 5%(深さ/直径 0.15〜0.2、縁と内側の段差)、中くらい約 25%(0.06〜0.15)、古い約 70%(0.015〜0.06、縁のない、裾の広いなだらかな窪み)。
形: 楕円(長短比 1〜1.15、面積を保つ)とふちの緩い欠け(3 つ山、±5%)。
</p>

状態を持たないので、複数のスレッドから呼べる。

 [PlanetCraterHeightProvider](VirtualGeometry.World.PlanetCraterHeightProvider.md)

高さの層: 内側の高さに、生成クレーター(<xref href="VirtualGeometry.World.PlanetCraterField" data-throw-if-not-resolved="false"></xref>)の凹みを足す。地形メッシュ・接地・岩はこれを使う。
凹みはメッシュ間隔で帯域制限する(直径がメッシュ間隔の 6〜12 倍の間で入れていく)。細かいクレーターは shader の陰影だけ(PlanetCraters.hlsl)。
陰影は二重にしない: 頂点法線の高さ(<xref href="VirtualGeometry.World.PlanetCraterHeightProvider.SampleShadingHeightMeters(System.Double%2cSystem.Double%2cSystem.Double%2cSystem.Double)" data-throw-if-not-resolved="false"></xref>)にはクレーターを入れない。
間隔 0(接地・岩)は最も細かいメッシュの間隔として扱い、接地と描かれる最も細かい地表を一致させる。

 [PlanetCraterShadingSource](VirtualGeometry.World.PlanetCraterShadingSource.md)

生成クレーターの陰影(Shaders/PlanetCraters.hlsl の VGPlanetCraters)へ、Cell ごとの値を書く。内側の値(色タイル・色のゆらぎなど)を先に書く。
値は Cell の球面上の原点(R·中心の方向)の、段 0 の格子番号(48 ビット)と端数、シード、置かない範囲(Cell の原点からの相対位置)。並びは hlsl の冒頭の契約と同じ。

 [PlanetDetailBandSuppression](VirtualGeometry.World.PlanetDetailBandSuppression.md)

実データの範囲(<xref href="VirtualGeometry.World.IPlanetRealDataRegion" data-throw-if-not-resolved="false"></xref>)で、増幅の細部(<xref href="VirtualGeometry.World.PlanetAmplifiedHeightProvider" data-throw-if-not-resolved="false"></xref> の鎖)のうち、
実データが表せる長い波長の octave を引く(本物の起伏の上に偽の起伏を二重に足さない)。範囲の外では元の高さそのまま。
波長 λ の octave を引く割合は、範囲の重み × smoothstep((λ − 実データの波長) / 実データの波長)(λ が実データの波長の 2 倍以上で全部引く)。
増幅の部品そのものは変えない(GPU 生成と前もって帯域を選ぶ経路は増幅の部品を直接ほどくため)。

 [PlanetEquirectangularHeightProvider](VirtualGeometry.World.PlanetEquirectangularHeightProvider.md)

正距円筒(緯度経度)の格子の標高(m)を、方向から求める供給元(<xref href="VirtualGeometry.World.IPlanetHeightProvider" data-throw-if-not-resolved="false"></xref>)。
格子は北の行から南へ、経度 −180° の列から東へ、画素の中心が格子点(LOLA などの全球の地図の並び)。
方向の規約: +Y が北極、+X が経度 0°、+Z が経度 +90°(経度 = atan2(z, x)、緯度 = asin(y))。別の規約の天体は、呼び出し側で軸を入れ替える。
帯域制限: 格子を 2×2 ずつ平均した mip を作り、メッシュの間隔が赤道の 1 画素より広いときは、間隔に合う 2 つの mip を補間する
(粗い Cell が細かい起伏を拾って遠景がちらつかない。間隔 0 は元の格子の双線形補間)。
値は呼び出し側が持つ配列から作り(コピーする)、作った後は変えない。スレッドから同時に呼んでよい。

 [PlanetFallbackHeightProvider](VirtualGeometry.World.PlanetFallbackHeightProvider.md)

主の供給元が答えられない(NaN)方向だけ、予備の供給元で答える(読み込みを待つ間の接地・岩の問い合わせ用)。
VG の Cell を作る供給元には使わないこと(届いていない場所を偽の高さで作らないため)。

 [PlanetGpuCubicHeight](VirtualGeometry.World.PlanetGpuCubicHeight.md)

固定64 quad配列へ依存せず、量子化したsource格子からGPU用のimmutableな係数をコピーする。

 [PlanetGpuFrontier](VirtualGeometry.World.PlanetGpuFrontier.md)

分割1回の安定したprefix/scatterのCPU参照。誤差評価・継ぎ目処理・frame controllerは含まない。

 [PlanetGpuFrontierResult](VirtualGeometry.World.PlanetGpuFrontierResult.md)

 [PlanetGpuGenerationDispatch](VirtualGeometry.World.PlanetGpuGenerationDispatch.md)

1 batchの入力を所有し、同じgraphics queueの生成→readback後にだけslot所有者へ結果を渡す。

 [PlanetGpuGenerationLeases](VirtualGeometry.World.PlanetGpuGenerationLeases.md)

惑星GPU生成のslot書込み所有権。完了はGPU fence/readbackの後だけ渡す。
この型自身はGPU完了を観測せず、描画readyの変更やbufferの解放もしない。

 [PlanetGpuHeightBasis](VirtualGeometry.World.PlanetGpuHeightBasis.md)

元データの寿命から独立した係数。係数は各々の中心高さとの差を表す。

 [PlanetGpuHeightInput](VirtualGeometry.World.PlanetGpuHeightInput.md)

1 Cellの中心差・係数・octave。CPUの頂点全体を作らず、GPU生成へ入力する。

 [PlanetGpuNoiseDelta](VirtualGeometry.World.PlanetGpuNoiseDelta.md)

GPU生成用のfloat演算参照。中心のノイズ値を引かず、lattice境界で分けた値の差を積分する。

 [PlanetGpuResidencyBuilder](VirtualGeometry.World.PlanetGpuResidencyBuilder.md)

1つのGPU表向けのCPU差分producer。pool回収やfenceの所有者ではない。複数GPU複製には別のack/journalが必要。

 [PlanetGpuResidencyMirror](VirtualGeometry.World.PlanetGpuResidencyMirror.md)

consumerごとに実Layerのresident/ready差分を保持する。1つの読取りが終わるまでGPU表を書き換えない。

 [PlanetGpuResidencyTable](VirtualGeometry.World.PlanetGpuResidencyTable.md)

GPU常駐確認用のimmutable snapshotのCPU参照。毎frameの全再構築には使わない。

 [PlanetGpuSelectionRound](VirtualGeometry.World.PlanetGpuSelectionRound.md)

GPU誤差判定と子への交換結果。拒否時は前の準備済みcutを維持する。

 [PlanetGpuSelectionRoundInput](VirtualGeometry.World.PlanetGpuSelectionRoundInput.md)

重複/祖先子孫の重なりを検査した1 round入力。全cutの最終controllerではない。

 [PlanetGpuSelectionView](VirtualGeometry.World.PlanetGpuSelectionView.md)

1 roundの有限なview定数。planesと写像の値は送信時に固定し、別viewの再利用で混ぜない。

 [PlanetGpuTablePatch](VirtualGeometry.World.PlanetGpuTablePatch.md)

確定したrevisionの転送データ。作成後にproducerが更新しても内容は変わらない。

 [PlanetGradientNoise](VirtualGeometry.World.PlanetGradientNoise.md)

3 次元の gradient noise(Perlin 型、quintic の補間)。格子の番号は 64 ビットの整数(床関数)、端数は double。値の範囲は ±<xref href="VirtualGeometry.World.PlanetGradientNoise.MaximumMagnitude" data-throw-if-not-resolved="false"></xref>。
hash は uint の演算だけ(GPU へ移すときも同じ値になる)。

 [PlanetHeightBounds](VirtualGeometry.World.PlanetHeightBounds.md)

 [PlanetHeightClearance](VirtualGeometry.World.PlanetHeightClearance.md)

描画と同じ高さの正本(<xref href="VirtualGeometry.World.IPlanetHeightProvider" data-throw-if-not-resolved="false"></xref>)から、天体のローカル位置(m)と地面との距離を求め、地面より上へ保つ。
位置・半径・余裕はメートル。spacingMeters は高さを聞く網目の間隔(0 は全帯域)。高さが NaN(届いていない)なら例外にする(偽の地面で判定しない)。

 [PlanetHeightTerrainSource](VirtualGeometry.World.PlanetHeightTerrainSource.md)

高さの正本(<xref href="VirtualGeometry.World.IPlanetHeightProvider" data-throw-if-not-resolved="false"></xref>、CPU の double)から惑星の地形を作る。既定はCPU生成(<xref href="VirtualGeometry.World.PlanetCellMeshBuilder" data-throw-if-not-resolved="false"></xref>)、
対応する入力と明示的なshader指定があれば非接地のN=8/16をGPU生成する。接地はCPU生成を維持し、描く頂点と接地の三角形のbit一致を保つ。
CPU の時間は frame ごとの予算(<xref href="VirtualGeometry.World.PlanetHeightTerrainSource.BuildMillisecondsPerFrame" data-throw-if-not-resolved="false"></xref>)で区切り、間に合わない Cell は次の frame へ送る(親を描き続ける)。
CPU生成のboundsはCPUで求め、GPU生成は非同期の結果と世代を検査してから公開する。
Cell の選択・退避・配置は <xref href="VirtualGeometry.World.PlanetLayerSource" data-throw-if-not-resolved="false"></xref>。高さの供給元は <xref href="VirtualGeometry.World.PlanetHeightTerrainSource.Configure(VirtualGeometry.World.IPlanetHeightProvider%2cSystem.Single%2cSystem.Int32%2cSystem.Single)" data-throw-if-not-resolved="false"></xref> で渡す(Scene には保存しない)。

 [PlanetIndexedBatch](VirtualGeometry.World.PlanetIndexedBatch.md)

1 Camera・1 Layerの共有index描画資源。頂点poolとcluster boundsはLayerから借り、この所有者は解放しない。
RenderGraphへは同じbufferを1回だけimportし、cull書込み→draw読取りの依存を明示する必要がある。

 [PlanetIndexedGraph](VirtualGeometry.World.PlanetIndexedGraph.md)

共有index描画のGraph部分。placement・材質・lightingは呼び出し元の既存契約で準備する。

 [PlanetLayerSource](VirtualGeometry.World.PlanetLayerSource.md)

球の地形を、cube-sphere の Cell ごとの instance として VG のメッシュ経路で描く共通部分(派生は <xref href="VirtualGeometry.World.PlanetHeightTerrainSource" data-throw-if-not-resolved="false"></xref>)。惑星の中心はこの GameObject の原点。
Cell の選択は <xref href="VirtualGeometry.World.PlanetCellSelector" data-throw-if-not-resolved="false"></xref>、頂点の生成は派生クラスが CPU で行い、Cell の頂点の pool(<xref href="VirtualizedGeometry.VirtualGeometryClusterSource" data-throw-if-not-resolved="false"></xref>)の slot へ書く。
Cell と pool の slot の対応を持ち、pool が足りないときは使っていない Cell を下(葉)から退避する。
頂点は Cell の原点(Cell の中心の方向の地表の高さの点、惑星のローカル座標。<xref href="VirtualGeometry.World.PlanetCellFrame.Origin" data-throw-if-not-resolved="false"></xref>)からの相対位置で持ち、Cell ごとに draw する。
惑星を置く空間は <xref href="VirtualGeometry.World.IPlanetPlacement" data-throw-if-not-resolved="false"></xref> が決める(OnEnable の時に同じ GameObject にある実装。無い、または無効なら Unity の world 空間)。
Cell の原点と GPU に渡す値は Logical 精度で求める(<xref href="VirtualGeometry.World.PlanetCellFrame" data-throw-if-not-resolved="false"></xref>)。頂点の誤差は惑星の大きさではなく Cell の大きさに比例する。

 [PlanetLayeredHeightProvider](VirtualGeometry.World.PlanetLayeredHeightProvider.md)

基の高さ(natural)の上に、書き換えの層を順に重ねる。層の式は前から順に合成する(後の層が前の層の結果を書き換える)。
陰影用の高さ(<xref href="VirtualGeometry.World.IPlanetShadingHeightProvider" data-throw-if-not-resolved="false"></xref>)は、基の陰影用の高さへ同じ式を掛ける。
基は複数のスレッドから同時に呼べること(層も状態を持たないこと)。

 [PlanetLocalHeightOverride](VirtualGeometry.World.PlanetLocalHeightOverride.md)

中心の方向と東の方向で決まる局所の長方形(東・北の弧長、m)を書き換える層。縁の feather の幅で滑らかに元へ戻す(縁の傾きは 0)。
sample は東・北の弧長(m)からその場所の高さ(m)を返す関数で、寿命中に変わらず、複数のスレッドから同時に呼べること。

 [PlanetLodBudgetController](VirtualGeometry.World.PlanetLodBudgetController.md)

Layer全体の閾値倍率だけを調整する。選択cutや接地、pool容量を直接変更しない。

 [PlanetMeshGeometrySource](VirtualGeometry.World.PlanetMeshGeometrySource.md)

惑星固有の格子・標高を、汎用VGの局所mesh/page producerへ変換する。選択・退避・描画は所有しない。

 [PlanetMeshSurfaceSampler](VirtualGeometry.World.PlanetMeshSurfaceSampler.md)

描画と同じfloat頂点・三角形から、指定方向の地表高を求める。全帯域の高さ場の直接評価を接地の代用にしない。
Moon/OldMoon の視点と、手続きメッシュproducerの接地問い合わせで使用する。

 [PlanetNativeHeightInputs](VirtualGeometry.World.PlanetNativeHeightInputs.md)

workerが作り終えた基底標高と不変の増幅係数。Native領域の所有はmainのleaseへ渡す。

 [PlanetNoiseColorSource](VirtualGeometry.World.PlanetNoiseColorSource.md)

地表の色のゆらぎ(色画像の 1 画素より細かい帯域の零平均の変動)の、Cell ごとの格子原点を書く(shader は Shaders/PlanetSurfaceColor.hlsl の VGApplyColorNoise)。
内側の値(色タイルなど)を先に書いてから、_VGColorNoiseInfo と _VGColorNoiseA〜D を書く。各 octave は独立した格子原点を 48bit で符号化する
(粗い格子の float の端数を何百万倍にも拡大しない)。SolarSystem・EarthToMoon が同じ部品を使う。

 [PlanetNoiseLattice](VirtualGeometry.World.PlanetNoiseLattice.md)

GPU 版の <xref href="VirtualGeometry.World.PlanetGradientNoise" data-throw-if-not-resolved="false"></xref>(Shaders/PlanetGradientNoise.hlsl)へ渡す Cell ごとの値を作る。
メッシュは波長が quad の 4 倍より短い octave を落とす(<xref href="VirtualGeometry.World.PlanetAmplifiedHeightProvider.BandWeight(System.Double%2cSystem.Double)" data-throw-if-not-resolved="false"></xref>)ので、shader がその分を画素ごとに同じ関数で足す。
惑星の座標 ÷ 波長は 10^9 周期に達し float では位相が潰れるため、Cell の球面上の原点(R·中心の方向)の格子番号と端数を、
shader が足す最初の octave(波長が quad の <xref href="VirtualGeometry.World.PlanetNoiseLattice.CoarsestQuads" data-throw-if-not-resolved="false"></xref> 倍より短いもの)について double で求める。細かい octave は shader が 2 倍を正確に繰り返して作る。
値の並びは hlsl の冒頭の契約と同じ(1 層 4 つの Vector4)。格子番号は 48 ビットの 2 の補数を 24 ビットずつ float で渡す(float で正確に表せる)。

 [PlanetNoiseShadingSource](VirtualGeometry.World.PlanetNoiseShadingSource.md)

形は元の高さを保ち、手続きの細部の陰影を画素側へ分離する。Cell の階層では陰影の帯域を変えない。

 [PlanetPackedTerrainCodec](VirtualGeometry.World.PlanetPackedTerrainCodec.md)

12 Bの形式を検証するCPU参照。GPU pool/生成への接続は別途行う。

 [PlanetPreparedHeightSampler](VirtualGeometry.World.PlanetPreparedHeightSampler.md)

1 Cell で不変の帯域を一度だけ選び、形と陰影で同じ基底・noise を再評価しない。演算順と採用 octave は元の供給元と同じ。

 [PlanetSharedVertexCatalog](VirtualGeometry.World.PlanetSharedVertexCatalog.md)

惑星固有の正本keyを汎用ID/Logical位置へ供給する。高さ未準備の頂点は登録しない。

 [PlanetTerrainContact](VirtualGeometry.World.PlanetTerrainContact.md)

物体の三角形メッシュを方向 d へまっすぐ動かしたとき、地形の三角形メッシュに初めて触れる距離を厳密に求める(どちらも描く三角形そのもの)。
区分的に平らな面どうしの最初の接触は、(1) 物体の頂点と地形の面、(2) 地形の頂点と物体の面、(3) 物体の辺と地形の辺 のどれかで起きるので、
それぞれの距離の最小値が答えになる(凹んだ形、斜面、細かい起伏でも成り立つ。球を真上から置くときの斜面の食い込み r(√(1+s²)−1) も無い)。
速くするため、d に垂直な面へ写した 2 次元の格子で候補を絞る。また、物体の最も低い点から、地形の高さの幅より上にある部分は触れようがないので除く。
入力は倍精度で、呼び出し側が同じ基準点からの相対位置にそろえる(地形の頂点は Cell の原点との Logical の差 + 描く float の頂点)。

 [PlanetTerrainGenerationMarkers](VirtualGeometry.World.PlanetTerrainGenerationMarkers.md)

Profiler TimelineとSolarSystemの画像なし集計が共用する処理境界。待機時間は別の要求台帳で計る。

 [PlanetTerrainVertexPool](VirtualGeometry.World.PlanetTerrainVertexPool.md)

惑星の共有index用の混合pool。接地のCPU正本を保持し、保護から外れた32 B領域を再利用する。

 [PlanetTriangleSoup](VirtualGeometry.World.PlanetTriangleSoup.md)

三角形の集まり(頂点と、3 つずつの頂点番号)。

 [PlanetZeroHeightProvider](VirtualGeometry.World.PlanetZeroHeightProvider.md)

どこも高さ 0 の球。

 [StandardPlanetPlacement](VirtualGeometry.World.StandardPlanetPlacement.md)

Unity の world 空間に惑星を置く(float の精度で足りる大きさに限る)。

### 構造体（Structs）

 [PlanetCraterField.Crater](VirtualGeometry.World.PlanetCraterField.Crater.md)

1 つのクレーター。中心は基準球の点(天体の中心からの位置、m)。

 [PlanetCellBuildFrame](VirtualGeometry.World.PlanetCellBuildFrame.md)

Logical原本は所有者に残し、数値Jobへ渡す有限成分だけを固定する。

 [PlanetCellBurstJob](VirtualGeometry.World.PlanetCellBurstJob.md)

Burst経路。managed fallbackで実行された結果を計測から識別できる。

 [PlanetCellBurstKernel](VirtualGeometry.World.PlanetCellBurstKernel.md)

高さ配列からの計算専用。全Native領域は外側のleaseが所有する。

 [PlanetCellCoordinate](VirtualGeometry.World.PlanetCellCoordinate.md)

cube-sphere の1つの面の上の、Cell の格子番号(0〜2^階層−1)。96ビットの符号なし整数。
10^20 m の天体を 1mm まで分けると約77段になり、64ビットでは足りないため。

 [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

Cell の中心の値を Logical 精度(Omni の Q95.96 固定小数点)で持つ。
頂点は Cell の原点からの相対量だけを float で持ち、float にすると精度が足りない値(中心の正接、Cell の原点、ノイズの格子の基点)はここで求める。
中心の角度は π·n/2^(L+2)(n=2x+1−2^L)で、n/2^(L+2) を固定小数点で正確に作るので、階層は <xref href="VirtualGeometry.World.PlanetCellFrame.MaximumLevel" data-throw-if-not-resolved="false"></xref> までに限る。
Cell の原点(<xref href="VirtualGeometry.World.PlanetCellFrame.Origin" data-throw-if-not-resolved="false"></xref>)は、中心の方向の地表の高さ(<xref href="VirtualGeometry.World.PlanetCellFrame.HeightShift" data-throw-if-not-resolved="false"></xref>)だけ半径 R の球面から持ち上げた点。
頂点の高さ方向の成分が地形の起伏ぶんの大きさになるので、起伏が数 km あっても float の刻みが mm を超えない。
ノイズの格子・波の位相・実データの方向など、高さ 0 の球面で定義する値は <xref href="VirtualGeometry.World.PlanetCellFrame.SphereOrigin" data-throw-if-not-resolved="false"></xref> から求める(持ち上げた原点から求めると、隣の Cell と食い違う)。

 [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

cube-sphere の四分木の1つの Cell(面、階層、格子番号)。

 [PlanetCellManagedJob](VirtualGeometry.World.PlanetCellManagedJob.md)

同じNative入出力でBurstだけを除いた対照。

 [PlanetCellNativeResult](VirtualGeometry.World.PlanetCellNativeResult.md)

 [PlanetClusterRecord](VirtualGeometry.World.PlanetClusterRecord.md)

CameraごとのCell配置。64 byte。C#とHLSLは4つのfloat4で配置を共有する。

 [PlanetContactRegion](VirtualGeometry.World.PlanetContactRegion.md)

接地の領域。惑星のローカル座標の点 <xref href="VirtualGeometry.World.PlanetContactRegion.Point" data-throw-if-not-resolved="false"></xref>(Logical)のまわり半径 <xref href="VirtualGeometry.World.PlanetContactRegion.Radius" data-throw-if-not-resolved="false"></xref>(m)に掛かる Cell を、
描くときにちょうど階層 <xref href="VirtualGeometry.World.PlanetContactRegion.Level" data-throw-if-not-resolved="false"></xref> にする(<xref href="VirtualGeometry.World.PlanetLayerSource.SetContactRegions(System.Collections.Generic.IReadOnlyList%7bVirtualGeometry.World.PlanetContactRegion%7d%2cSystem.Boolean)" data-throw-if-not-resolved="false"></xref>)。

 [PlanetContactResult](VirtualGeometry.World.PlanetContactResult.md)

接地の結果。

 [PlanetCraterKeepOut](VirtualGeometry.World.PlanetCraterKeepOut.md)

生成クレーターを置かない範囲。中心(天体の単位方向)から半径 RadiusMeters の円の中に中心がある、直径 MinimumDiameterMeters 以上のクレーターを置かない。
IncludeInfluence なら、クレーターの影響半径(2r)も半径に足す(施設の周りに凹みを届かせない)。実データで分かる大きさを実データの範囲に二重に足さないためにも使う。

 [PlanetCraterSettings](VirtualGeometry.World.PlanetCraterSettings.md)

生成クレーターの分布の値(天体ごと。同じ天体はどのデモでも同じ値)。
段 0 が最も大きい(最小直径 = 最も小さい段の最小直径 × 2^(段の数 − 1))。各段の最小直径 dMin の 3 次元の格子(1 辺 4dMin)に候補を 1 つ置く。

 [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

倍精度の 3 次元ベクトル(接地の計算用)。

 [PlanetDrawableCutReadiness](VirtualGeometry.World.PlanetDrawableCutReadiness.md)

 [PlanetGpuAnchor](VirtualGeometry.World.PlanetGpuAnchor.md)

G2の精度検証用アンカー。sphere原点をLogicalでcamera相対にし、子以下の差だけをfloatで求める。

 [PlanetGpuChildren](VirtualGeometry.World.PlanetGpuChildren.md)

 [PlanetGpuCubicPatch](VirtualGeometry.World.PlanetGpuCubicPatch.md)

整数の格子範囲と、Cell中心からの格子差で評価する高さの三次係数。定数項は基準高さからの差。

 [PlanetGpuFrontierNode](VirtualGeometry.World.PlanetGpuFrontierNode.md)

 [PlanetGpuGenerationLease](VirtualGeometry.World.PlanetGpuGenerationLease.md)

CPUの所有権。GPU完了の世代確認に加え、同じ割当で再試行した古いcallbackを識別する。

 [PlanetGpuGenerationOctave](VirtualGeometry.World.PlanetGpuGenerationOctave.md)

1 octaveの64 bit latticeと中心端数。中心値はCPUが別に保持し、GPUは変化分だけを生成する。

 [PlanetGpuGenerationResult](VirtualGeometry.World.PlanetGpuGenerationResult.md)

Identity=(slot,version,status,poolEpoch)。HeightRange.zwはdispatchSerialの下位/上位16 bitを正確なfloat整数で返す。

 [PlanetGpuGenerationTask](VirtualGeometry.World.PlanetGpuGenerationTask.md)

1 slotのGPU生成。patchの高さはbasis中心からの差、height.y/zは全高さ中心とHeightShiftとの差。

 [PlanetGpuKey](VirtualGeometry.World.PlanetGpuKey.md)

structured buffer用の96 bit×2座標。演算は32 bit wordで行い、floatへ変換しない。

 [PlanetGpuPackedCompletion](VirtualGeometry.World.PlanetGpuPackedCompletion.md)

生成resultと圧縮recordを同じreadbackで返す。slot表全体は読み戻さない。

 [PlanetGpuResidentEntry](VirtualGeometry.World.PlanetGpuResidentEntry.md)

 [PlanetGpuResidentPatchEntry](VirtualGeometry.World.PlanetGpuResidentPatchEntry.md)

 [PlanetGpuResidentProbeResult](VirtualGeometry.World.PlanetGpuResidentProbeResult.md)

GPU選択が読むsnapshotの照合結果。現在の描画cutの公開許可ではない。

 [PlanetGpuSelectionDecision](VirtualGeometry.World.PlanetGpuSelectionDecision.md)

GPUが求めた画素誤差と分割hint。Visible=falseのnodeも被覆のため親として候補に残る。

 [PlanetGpuSelectionSample](VirtualGeometry.World.PlanetGpuSelectionSample.md)

Logicalの差を取った後のcamera相対bounds。Displayの結果は移行中はCPUから渡す。

 [PlanetGpuSplitRequest](VirtualGeometry.World.PlanetGpuSplitRequest.md)

 [PlanetHeightBlend](VirtualGeometry.World.PlanetHeightBlend.md)

基の高さへ掛ける重ね書きの式(基の重み・足す高さ・岩を置く重み)。高さ = <xref href="VirtualGeometry.World.PlanetHeightBlend.NaturalWeight" data-throw-if-not-resolved="false"></xref> × 基の高さ + <xref href="VirtualGeometry.World.PlanetHeightBlend.OffsetHeightMeters" data-throw-if-not-resolved="false"></xref>。

 [PlanetHeightNoiseLayer](VirtualGeometry.World.PlanetHeightNoiseLayer.md)

 [PlanetHeightNoiseOctave](VirtualGeometry.World.PlanetHeightNoiseOctave.md)

 [PlanetIndexedDrawDiagnostics](VirtualGeometry.World.PlanetIndexedDrawDiagnostics.md)

CameraのForwardへ提出した三角形数。画素被覆やGPU時間とは別の、frame付き非同期sample。

 [PlanetLodBudgetSample](VirtualGeometry.World.PlanetLodBudgetSample.md)

各値は測定値/予算。nullは未取得で、0の余裕とは扱わない。

 [PlanetPackedTerrainBounds](VirtualGeometry.World.PlanetPackedTerrainBounds.md)

slot相対の量子化領域。絶対惑星座標には使わない。

 [PlanetPackedTerrainVertex](VirtualGeometry.World.PlanetPackedTerrainVertex.md)

位置unorm16×3、八面体法線unorm16×2、補助flag16 bit。UVは格子から復元する。

 [PlanetPlacementFrame](VirtualGeometry.World.PlanetPlacementFrame.md)

camera ごとに、惑星をどの空間に置いて選択・cull・描画するかの値。

 [PlanetPredictionResult](VirtualGeometry.World.PlanetPredictionResult.md)

描画を変更しない先読み結果。必須経路では選択上限と予約容量不足を区別する。

 [PlanetSelectionView](VirtualGeometry.World.PlanetSelectionView.md)

選択に使う視点。カメラの位置は惑星のローカル座標の Logical で持ち、Cell との差を Logical で取ってから float にする
(惑星が大きくても、カメラの近くの小さな Cell の判定が潰れない)。
cull 空間での Cell の位置は CameraCull + LocalToCull·(Cell − カメラ)(LocalToCull は線形部分だけを使う)。

 [PlanetSharedVertexKey](VirtualGeometry.World.PlanetSharedVertexKey.md)

面IDを含まない、等角cubeのdyadic標本。面境界・角・異LODの同じ点は同じkeyへ正規化する。

 [PlanetTerrainStorageRecord](VirtualGeometry.World.PlanetTerrainStorageRecord.md)

logical slotから12 B/元の32 Bの物理word領域へ写す。範囲はCell局所、UVは格子から復元する。

### インターフェース（Interfaces）

 [IPlanetAnchorPropertySource](VirtualGeometry.World.IPlanetAnchorPropertySource.md)

指定Cellを描画アンカーとして、その原点からの相対頂点すべてに同じpropertyを使える供給元。
CellのLOD・タイル番号で表面の意味を変えず、shaderがアンカー相対位置から連続な値を復元すること。
per-Cell texture/tileは、この契約を実装せず既存描画または個別のrecord adapterを使う。

 [IPlanetCellHeightBoundsSource](VirtualGeometry.World.IPlanetCellHeightBoundsSource.md)

 [IPlanetCellHeightSource](VirtualGeometry.World.IPlanetCellHeightSource.md)

Cell の格子の高さを、高さの供給元(<xref href="VirtualGeometry.World.IPlanetHeightProvider" data-throw-if-not-resolved="false"></xref>をサンプルする代わりに、外から渡す口。
ストリーミングで届いた高さ、焼いた高さ、サーバーが計算した高さなどを、Cell の頂点に使う(<xref href="VirtualGeometry.World.PlanetCellMeshBuilder.BuildFromHeights(VirtualGeometry.World.PlanetCellFrame%40%2cSystem.Double%2cSystem.ReadOnlySpan%7bSystem.Double%7d%2cSystem.ReadOnlySpan%7bSystem.Double%7d%2cSystem.Single%2cUnityEngine.Vector4%2cVirtualizedGeometry.VirtualGeometryPackedVertex%5b%5d%2cSystem.Int32%2cUnityEngine.Vector4%40%2cSystem.Double%40%2cSystem.Double%40)" data-throw-if-not-resolved="false"></xref>)。
main thread から呼ばれる。同じ Cell には、Ready になった後は常に同じ高さを返すこと(作り直した Cell と接地の三角形が一致する前提)。

 [IPlanetCellPropertySource](VirtualGeometry.World.IPlanetCellPropertySource.md)

Cell の draw の MaterialPropertyBlock に、Layer の shader が使う値を外から足す口(Cell ごとの色のタイルの番号など)。
<xref href="VirtualGeometry.World.PlanetHeightTerrainSource.CellProperties" data-throw-if-not-resolved="false"></xref> に設定すると、Cell ごとの標準の値(_PlanetCellUp など)の後に呼ばれる。main thread から、
描く Cell ごとに毎 frame 呼ばれる(重い処理を入れない)。

 [IPlanetCellResidency](VirtualGeometry.World.IPlanetCellResidency.md)

Cell の生成と描画の状態を、選択から問い合わせる口。

 [IPlanetDisplayMapping](VirtualGeometry.World.IPlanetDisplayMapping.md)

Radial で圧縮した描画空間での、Cell の見え方（<xref href="VirtualGeometry.World.PlanetCellSelector" data-throw-if-not-resolved="false"></xref> が誤差と cull に使う）。
実距離の画面上の大きさは、圧縮した空間を別のカメラ（俯瞰）から見るときには合わない。

 [IPlanetGpuHeightInputSource](VirtualGeometry.World.IPlanetGpuHeightInputSource.md)

ノイズを足す前の高さを、halo付きの三次係数へ写す供給元。Sceneや惑星の種類には依存しない。

 [IPlanetGridHeightSource](VirtualGeometry.World.IPlanetGridHeightSource.md)

Cellの物理的な範囲と格子の分解能を分け、N=8/16/64のhalo全体を供給する契約。

 [IPlanetHeightBoundsSource](VirtualGeometry.World.IPlanetHeightBoundsSource.md)

main threadの選択用。取得やdecodeを行わず、現在保証できる高さの範囲だけを返す。

 [IPlanetHeightOverride](VirtualGeometry.World.IPlanetHeightOverride.md)

天体の一部だけ高さを書き換える層(局所の実測、施設の地ならし、島など)。内容を変えたら <xref href="VirtualGeometry.World.IPlanetHeightOverride.CacheIdentity" data-throw-if-not-resolved="false"></xref> も変えること。
方向は天体のローカル座標の単位ベクトル。複数のスレッドから同時に呼ばれるので、状態を変えないこと。

 [IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

惑星の地表の高さ(半径 R の球面からの高さ、m)の正本を CPU で返す。<xref href="VirtualGeometry.World.PlanetHeightTerrainSource" data-throw-if-not-resolved="false"></xref> は Cell の頂点をこの値で作り、
描く頂点と接地の問い合わせ(<xref href="VirtualGeometry.World.PlanetTerrainContact" data-throw-if-not-resolved="false"></xref>)が同じ値を使う(GPU に別の式を持たない)。
方向は惑星のローカル座標の単位ベクトル。spacingMeters はメッシュの間隔(この間隔で表せない短い波長を落とす帯域制限。0 は全帯域)。
同じ引数には常に同じ値を返すこと(Cell を作り直しても形が変わらない前提)。呼び出しは main thread から。

 [IPlanetPlacement](VirtualGeometry.World.IPlanetPlacement.md)

惑星を置く座標系。既定(<xref href="VirtualGeometry.World.StandardPlanetPlacement" data-throw-if-not-resolved="false"></xref>)は Unity の world 空間で、惑星の GameObject の行列を使う。
Omni の対数描画では、惑星の位置を Logical で持ち、カメラ相対の物理空間で cull し、Cell ごとに Omni の物体の値を書く実装を使う
(VirtualGeometry.Omni の OmniPlanetPlacement。惑星と同じ GameObject に付けると <xref href="VirtualGeometry.World.PlanetLayerSource" data-throw-if-not-resolved="false"></xref> が使う)。
呼び出しは camera ごとに TryBeginFrame → Describe(Cell の数だけ)の順で、同じ camera の中で入れ子にならない。

 [IPlanetRealDataRegion](VirtualGeometry.World.IPlanetRealDataRegion.md)

実データの細かさを知らせる層。その範囲では、実データが表せる長い波長の手続きの細部を足さない(<xref href="VirtualGeometry.World.PlanetDetailBandSuppression" data-throw-if-not-resolved="false"></xref>)。

 [IPlanetShadingHeightProvider](VirtualGeometry.World.IPlanetShadingHeightProvider.md)

頂点の法線に、形とは別の高さを使う供給元(形には入れるが、陰影は画素ごとに別に付ける細部を、法線へ二重に入れないため)。
実装しない供給元では、法線も形と同じ高さから求める。

 [IThreadSafePlanetHeightProvider](VirtualGeometry.World.IThreadSafePlanetHeightProvider.md)

複数のスレッドから同時に呼べる高さの供給元（呼び出しが状態を変えない）。<xref href="VirtualGeometry.World.PlanetHeightTerrainSource" data-throw-if-not-resolved="false"></xref> は、これを実装する供給元の Cell をワーカースレッドで作る
（WebGL などスレッドを使えない環境では main thread で、frame の予算内で作る）。

### 列挙型（Enums）

 [PlanetCellHeightStatus](VirtualGeometry.World.PlanetCellHeightStatus.md)

 [PlanetCpuBuildBackend](VirtualGeometry.World.PlanetCpuBuildBackend.md)

 [PlanetErrorMetric](VirtualGeometry.World.PlanetErrorMetric.md)

Cell の細かさを決める誤差の定義(Docs/Plans/VirtualGeometryNaniteMigration.md の E1 / E2)。

 [PlanetGpuFrontierStatus](VirtualGeometry.World.PlanetGpuFrontierStatus.md)

 [PlanetGpuGenerationCompletion](VirtualGeometry.World.PlanetGpuGenerationCompletion.md)

GPU書込み完了後に、生成要求の所有者が実行する遷移。

 [PlanetGpuHeightInputStatus](VirtualGeometry.World.PlanetGpuHeightInputStatus.md)

入力待ちと未対応を区別する。Pendingでは偽の高さや別の供給元へ置き換えない。

 [PlanetGpuResidency](VirtualGeometry.World.PlanetGpuResidency.md)

 [PlanetGpuSelectionControl](VirtualGeometry.World.PlanetGpuSelectionControl.md)

 [PlanetGpuSplitDecision](VirtualGeometry.World.PlanetGpuSplitDecision.md)

 [PlanetGpuSplitHint](VirtualGeometry.World.PlanetGpuSplitHint.md)

 [PlanetGpuTableUpdate](VirtualGeometry.World.PlanetGpuTableUpdate.md)

 [PlanetLodBudgetMode](VirtualGeometry.World.PlanetLodBudgetMode.md)

 [PlanetLodBudgetSignals](VirtualGeometry.World.PlanetLodBudgetSignals.md)

### デリゲート（Delegates）

 [PlanetSharedVertexCatalog.HeightQuery](VirtualGeometry.World.PlanetSharedVertexCatalog.HeightQuery.md)

 [PlanetHeightRangeProvider](VirtualGeometry.World.PlanetHeightRangeProvider.md)

 [PlanetHeightShiftProvider](VirtualGeometry.World.PlanetHeightShiftProvider.md)

Cell の原点を半径 R の球面から外向きに持ち上げる高さ(m)を返す。sphereFrame は持ち上げていない Cell の値。
同じ Cell には常に同じ値を返すこと(選択の bounds と、生成した頂点の基準が一致する前提)。false または 0 なら持ち上げない。
