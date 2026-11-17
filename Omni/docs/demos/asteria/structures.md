# 構造物と都市

**結論**：リング、索（つな）、塔、峡谷、都市、夜の通りなどの「人工物」を作る部品たちです。
どれも**実行中に計算で形を作り**、Scene BRG に登録して描きます。保存する Mesh はありません。

## 共通のしくみ

### 1. 近くだけ作る（区画の出し入れ）

都市や峡谷のように広い物は、カメラの近くの区画だけ Mesh を作ります。
この「区画を作る・登録する・片付ける」を受け持つ共通の部品が `AsteriaTileSet` です（Scene には付かないクラス）。
片付けるときは、まず BRG の登録を外し、30 フレーム後に Mesh を壊します。Earth の [EarthGroundScatter](../earth/scatter.md) と同じ考え方です。

### 2. 遠くはシェーダーが塗る

<figure class="caption">
<svg class="fig" viewBox="0 0 720 230" width="720" role="img" aria-label="近くは Mesh、遠くは地表のシェーダーが模様を塗る">
  <path d="M 20 190 L 700 190" class="sb" stroke-width="3"/>
  <circle cx="60" cy="150" r="9" class="fa"/>
  <text x="60" y="130" text-anchor="middle" font-size="12">カメラ</text>
  <g class="fa" fill-opacity=".8">
    <rect x="100" y="120" width="26" height="70"/><rect x="134" y="95" width="22" height="95"/>
    <rect x="164" y="135" width="30" height="55"/><rect x="202" y="110" width="20" height="80"/>
    <rect x="230" y="140" width="28" height="50"/>
  </g>
  <text x="180" y="215" text-anchor="middle" font-size="13">近く：本物の Mesh（区画ごとに作る）</text>
  <g class="fb">
    <rect x="320" y="182" width="380" height="8" fill-opacity=".6"/>
    <rect x="340" y="184" width="6" height="4"/><rect x="380" y="184" width="6" height="4"/><rect x="420" y="184" width="6" height="4"/>
    <rect x="470" y="184" width="6" height="4"/><rect x="530" y="184" width="6" height="4"/><rect x="600" y="184" width="6" height="4"/>
  </g>
  <text x="510" y="215" text-anchor="middle" font-size="13">遠く：地表のシェーダーが建物と窓の灯りを「模様」として塗る</text>
</svg>
<figcaption>遠くの都市は、Mesh を作らずに地表の色として描きます。`AsteriaCity` などがシェーダー共通の変数に「どこに何があるか」の地図を置きます。</figcaption>
</figure>

### 3. 決まった作り方（決定論）

都市の区画や建物の並びは、決まった種（seed）から毎回同じに作られます。
`AsteriaCity` の都市の計画は、C# の実装と Python の基準の実装で、結果が最後の桁まで一致するように作られています。

### 4. 実行時の材質を知らせる

これらの部品は `IRadialBatchMaterialDependencyProvider` を実装しています。
「実行中に作る Mesh はこの材質で描きます」と、ビルドの前に Omni へ知らせて、BRG 用の材質を用意してもらうためです。

## 部品の一覧

| 部品 | 付いている所 | 何を作るか |
|---|---|---|
| `AsteriaRings` | `Rings` | 惑星を囲む 3 本の軌道リング（A・B・C）。1 度ごとのトラスと軌道都市、約 1,000 個。常に登録したまま |
| `AsteriaRingDetail` | `RingDetail` | リング A の 3 区画だけ、近づくと実物の部材に替える**試験** |
| `AsteriaTether` | `Tether` | 衛星イシュアからリング A へ伸びる索と、その上を走る摺動子 |
| `AsteriaLandmarks` | `Landmarks` | 名所：中央の塔（スパイア）、広場、名所の塔、副塔、発着台と昇降台 |
| `AsteriaCanyon` | `Canyon` | 巨大な峡谷の近景。経路に沿って ±60 km の段、建物は ±30 km |
| `AsteriaLayeredCity` | `LayeredCity` | 何層にも重なった都市の板・柱・建物。カメラから 10 km 以内の 2 km 区画だけ |
| `AsteriaCity` | `City` | 中央都市区の建物・公園・広場・回廊・運河。近くは Mesh、遠くは模様 |
| `AsteriaGroundScatter` | `GroundScatter` | 地面の岩と遺跡。約 78 m の区画ごと |
| `AsteriaStreet` | `Street` | 夜の通り 1 本（床・壁・線の光・反射・アンドロイドとメック） |

すべて Play 中だけ動きます（`Start` で作る）。共通の項目として、ほとんどが `m_Shading`（`AsteriaShading`）と材質、カメラ（`m_Viewer`）を持ちます。

## 主な部品の詳しい説明

### AsteriaLandmarks（名所）

- 名所の塔の地面の中心に、「東・上・北」の向きをそろえた局所の座標（`HeroSite`）を作ります。
- 夜の通り、物語の D2、自由カメラの歩ける範囲は、すべてこの `HeroSite` を基準にしています。
- 副塔は「元の形」と「キットの形」の 2 通りがあり、比べるためにどちらか一方だけを描きます。

### AsteriaCity（都市）

- 寸法表の都市の計画と、Blender で作った建物の部品集（`AsteriaKitCatalog`）から、建物を並べます。
- 遠くの都市のために、窓の灯りの地図などを画像にして、シェーダー共通の変数（`_AsteriaCityPlan`、`_AsteriaCityLights` など）に置きます。
- 部品を壊すときは、これらの変数を黒い画像に戻します。

### AsteriaStreet（夜の通り）

- 通り 1 本を 1 つの **VO**（画面での大きさで描き方を変える物）として扱い、段 0〜2 を出し入れします。
- **ふだんは何も置きません**。`Show()` で置き、`Hide()` で片付けます。物語の D2 と自由カメラの歩行で使います。
- 線の形の光、画面の反射（SSR）、14 体のアンドロイドとメックを置きます。

!!! warning "つまずきやすい点"
    - `AsteriaStreet` は、名所の塔（`HeroSite`）が無いと置けません（例外になります）。
    - アンドロイドたちの向きが確かめられていない（`m_FacingValidated` が false）と、表示しません。
    - Scene ファイルの中で、`Street` の部品が古い名前 `AsteriaStreetStrip` で書かれている所があります。中身は `AsteriaStreet` です（名前を変えた名残）。
    - `AsteriaRings` の材質の数が、寸法表のリングの数と合わないと止まります。
    - `AsteriaGroundScatter` は、立方体球の面の境目では隣の面の区画を作らないので、その帯だけ岩が欠けます（既知の制約）。
