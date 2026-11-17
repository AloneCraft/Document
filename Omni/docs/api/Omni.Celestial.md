# <a id="Omni_Celestial"></a> Namespace Omni.Celestial

### クラス（Classes）

 [CelestialBodyAuthoring](Omni.Celestial.CelestialBodyAuthoring.md)

<xref href="Omni.Celestial.CelestialCatalogAsset" data-throw-if-not-resolved="false"></xref>に直列化する1天体分のAuthoring値です。
数値はfloatではなく10進文字列で保持し、Snapshot化時に幾何量は
<xref href="Omni.Logical.Scalar" data-throw-if-not-resolved="false"></xref>、質量は<xref href="Omni.Units.Mass" data-throw-if-not-resolved="false"></xref>へ検証付きで
変換します。これによりInspectorの表示精度やカルチャ差で物理定数を失いません。

 [CelestialCatalogAsset](Omni.Celestial.CelestialCatalogAsset.md)

天体の物理定数を保持する唯一のAuthoring Source of Truthです。

<p>
SaturnやGalaxyのPrefab・Scene・描画用データは半径、質量、軌道を複製してはなりません。
起動時には必ず<xref href="Omni.Celestial.CelestialCatalogAsset.TryCreateSnapshot(Omni.Celestial.CelestialCatalogSnapshot%40%2cOmni.Celestial.CelestialCatalogValidationResult%40)" data-throw-if-not-resolved="false"></xref>で検証済みの
<xref href="Omni.Celestial.CelestialCatalogSnapshot" data-throw-if-not-resolved="false"></xref>へ変換してから利用してください。
</p>

 [CelestialCatalogRuntime](Omni.Celestial.CelestialCatalogRuntime.md)

Resourcesに置いた共有CelestialCatalogAssetを、検証済み不変Snapshotとして提供します。
GalaxyとSaturnは同じAuthoring assetを参照し、物理定数を個別の静的表へ複製しません。

 [CelestialCatalogSnapshot](Omni.Celestial.CelestialCatalogSnapshot.md)

<xref href="Omni.Celestial.CelestialCatalogAsset" data-throw-if-not-resolved="false"></xref>から一度だけ生成する、検証済みの読み取り専用カタログです。
Unity Objectを含まず、同じAuthoring内容から必ず同じ<xref href="Omni.Celestial.CelestialCatalogSnapshot.Fingerprint" data-throw-if-not-resolved="false"></xref>を生成します。

 [CelestialCatalogValidationResult](Omni.Celestial.CelestialCatalogValidationResult.md)

カタログ検証の不変結果です。エラー配列は外部から変更できません。

 [SaturnRingSnapshotProvider](Omni.Celestial.SaturnRingSnapshotProvider.md)

Resourcesに置いた唯一のSaturnリングAuthoring assetから不変物理Snapshotを読みます。
GalaxyはSaturn Runtimeの具体型を参照せず、このproviderを通じてリング寸法を取得します。
Authoring assetとその型は開発環境（Saturn Legacy Scenario）にだけあり、配布物には含みません。
無い環境では<xref href="Omni.Celestial.SaturnRingSnapshotProvider.TryGetSnapshot(Omni.Celestial.SaturnRingSnapshot%40%2cSystem.String%40)" data-throw-if-not-resolved="false"></xref>が理由付きでfalseを返します。

 [SchwarzschildLensTable](Omni.Celestial.SchwarzschildLensTable.md)

シュヴァルツシルト時空の光線が、半径 r の点から無限遠まで進む間に中心のまわりを回る角度 Δφ の表（単位は Rs = 1）。
ブラックホールのそばの点（例: 降着円盤の粒子）の見かけの位置を求めるのに使います: 点と観測者が中心から見て角 ψ だけ
離れているとき、Δφ = ψ となる光線が一次像、Δφ = 2π − ψ が中心の裏を回る二次像です。
GPU では、表を半径の行ごとに二分探索して Δφ − asin(b/D) = 目標の角（D は観測者の距離）となる b を求め、
観測者から見た光の向き（中心から asin(b/D) だけ傾いた向き）を作ります。
光線の軌道の式 (du/dφ)² = 1/b² − u² + u³（u = 1/r）を数値積分します。
横軸 s ∈ [0, 1) は光線を1本の単調な列に並べたもの: 前半は外向きに出る光線（衝突パラメーター b を 0 から、半径 r で
接線方向になる b_t = r/√(1 − 1/r) まで）、後半は一度内向きに進み、近点を回ってから出る光線（b を b_t から光子球の
b_c = 3√3/2 まで）。Δφ は s とともに単調に増え、s → 1 で発散します（光子球をまわる光）。
縦軸は r ∈ [RMin, RMax]。テクスチャ（RGHalf）: R = Δφ、G = b。

### 構造体（Structs）

 [CelestialBodySnapshot](Omni.Celestial.CelestialBodySnapshot.md)

1天体分の、検証済みで不変なカタログ値です。

 [CelestialCatalogValidationIssue](Omni.Celestial.CelestialCatalogValidationIssue.md)

1件のカタログ検証エラーです。<xref href="Omni.Celestial.CelestialCatalogValidationIssue.BodyIndex" data-throw-if-not-resolved="false"></xref>が-1の場合はカタログ全体のエラーです。

 [CelestialOrbitalElements](Omni.Celestial.CelestialOrbitalElements.md)

天体の不変な軌道要素です。中心天体を持たない場合は<xref href="Omni.Celestial.CelestialOrbitalElements.IsDefined" data-throw-if-not-resolved="false"></xref>がfalseです。

 [CelestialPhysicalConstants](Omni.Celestial.CelestialPhysicalConstants.md)

1天体の不変な物理定数です。幾何量は<xref href="Omni.Logical.Scalar" data-throw-if-not-resolved="false"></xref>、
質量は桁域の異なる<xref href="Omni.Units.Mass" data-throw-if-not-resolved="false"></xref>で保持します。

 [SaturnRingSnapshot](Omni.Celestial.SaturnRingSnapshot.md)

Saturnリングの物理寸法だけを表す、Unity Objectを含まない不変値です。
Authoringの唯一の正本は、<xref href="Omni.Celestial.ISaturnRingDefinitionSource" data-throw-if-not-resolved="false"></xref>を実装する
既存のSaturnRingDefinitionAssetです。Galaxyはその型に依存せず、この値だけを読みます。

### インターフェース（Interfaces）

 [ISaturnRingDefinitionSource](Omni.Celestial.ISaturnRingDefinitionSource.md)

Saturn RuntimeのAuthoring assetをCelestial層へ中立的に公開する境界です。
Galaxyは具体的なSaturn型ではなく、このinterface経由で不変物理Snapshotを取得します。

### 列挙型（Enums）

 [CelestialCatalogValidationCode](Omni.Celestial.CelestialCatalogValidationCode.md)

天体カタログを不変Snapshotへ変換する前に検出した不正値の種別です。
