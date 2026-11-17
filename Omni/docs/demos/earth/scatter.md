# EarthGroundScatter（岩と木）

**一言で**：カメラの近くだけに、岩や木の Mesh をその場で作って地面に置く部品です。
1 つの部品で 3 種類（岩・近くの木・遠くの木）を扱い、Scene には 3 つ置かれています。

| | |
|---|---|
| 付いている所 | `Earth` の子：`GroundScatter`（岩）、`TreeScatter`（近くの木）、`FarTreeScatter`（遠くの木） |
| ファイル | `Assets/Omni/Development/Earth/Runtime/Ground/EarthGroundScatter.cs`（置き方の計算は `EarthGroundScatterModel.cs`） |
| 名前空間 | `Omni.Earth`（アセンブリ `Omni.Earth.Runtime`） |
| いつ動くか | Edit Mode でも動く（`[ExecuteAlways]`。撮影で使うため）。毎フレームの `Update` |

## たとえ：カメラの周りにだけ敷く絨毯

地球全体に岩を置くと、数えきれない数になります。
そこで地球の表面を**約 76 m 四方の区画**に分け、カメラの近くの区画にだけ岩や木を作ります。
カメラが動くと、後ろの区画を片付け、前の区画を作ります。

<figure class="caption">
<svg class="fig" viewBox="0 0 720 320" width="720" role="img" aria-label="カメラの周りの区画だけに岩と木を作る">
  <g class="ln" stroke-width="1">
    <path d="M 40 40 H 680 M 40 80 H 680 M 40 120 H 680 M 40 160 H 680 M 40 200 H 680 M 40 240 H 680 M 40 280 H 680"/>
    <path d="M 40 40 V 280 M 120 40 V 280 M 200 40 V 280 M 280 40 V 280 M 360 40 V 280 M 440 40 V 280 M 520 40 V 280 M 600 40 V 280 M 680 40 V 280"/>
  </g>
  <circle cx="360" cy="160" r="230" class="sb" stroke-width="2" stroke-dasharray="8 6"/>
  <circle cx="360" cy="160" r="110" class="sa" stroke-width="2.5"/>
  <circle cx="360" cy="160" r="60" class="sc" stroke-width="2.5"/>
  <circle cx="360" cy="160" r="9" class="fa"/>
  <text x="372" y="156" font-size="13">カメラ</text>
  <text x="360" y="95" text-anchor="middle" font-size="13">岩</text>
  <text x="360" y="44" text-anchor="middle" font-size="13">近くの木</text>
  <text x="640" y="300" text-anchor="middle" font-size="13">遠くの木（さらに外側）</text>
  <rect x="280" y="120" width="160" height="80" class="c" fill-opacity=".25" stroke-width="0"/>
</svg>
<figcaption>地面を約 76 m の区画（格子）に分け、カメラからの範囲に入る区画だけを作ります。円の大きさは説明用です。</figcaption>
</figure>

## 3 つの種類

| 種類（`kind`） | 置き場所の GameObject | 範囲 | 材質 |
|---|---|---|---|
| `Rocks`（0） | `GroundScatter` | 40〜240 m | `EarthRock.mat` |
| `Trees`（1） | `TreeScatter` | 150〜300 m | `EarthTree.mat`、影に `EarthTreeShadow.mat` |
| `TreesFar`（2） | `FarTreeScatter` | 600〜1,500 m | `EarthTreeFar.mat` |

範囲は「距離」で決め打ちしているのではなく、**画面での大きさ**で決めています。

- 岩：直径 0.8 m の岩が 6 画素に見える距離を、40〜240 m の間に収めた値。
- 近くの木：直径 6 m の樹冠が 6 画素に見える距離を、150〜300 m に収めた値。
- 遠くの木：直径 6 m の樹冠が 2 画素に見える距離を、600〜1,500 m に収めた値。

近くの木と遠くの木は**同じ場所の木**です。近くの木が消える距離で、遠くの木（円錐 1 つの簡単な形）が現れます。
木は、アルプスの実際の標高がある所にだけ置かれます。

## 急に現れない工夫

範囲の端で岩がぱっと現れたり消えたりすると目立ちます。そこで：

1. シェーダーが、範囲の 60〜90% の距離で、岩を**足元の点へ縮めて**消します（`_EarthScatterFade` など）。
2. 区画は、範囲より少し外（1.3 倍）を超えてから片付けます。
3. 片付けるときは、まず描画の登録を外し、30 フレーム後に Mesh を壊します。
4. 1 フレームに作る区画は 2 つまで（遠くの木は 8 つまで）にして、カクつきを抑えます。

## 決まった置き方（決定論）

どの区画に、どんな岩が、どこに置かれるかは、**区画の番号と決まった種（seed）だけ**から計算します。
同じ場所に戻ってくれば、必ず同じ岩が同じ形で置かれます。保存する資産はありません。

- 岩の数は、地形の起伏の強さに比例します。海と海岸には置かず、平地は少なく、山地は多く置きます。
- 岩の形は「少しゆがめた球を、何枚かの平面で切り落とした塊」です。
- 足元の高さは、`EarthSurfaceSetup.Heights`（高さの正本）から取ります。だから地面に埋まったり浮いたりしません。

## Inspector の項目

| 項目 | 意味 |
|---|---|
| `kind` | 種類：0 = 岩、1 = 近くの木、2 = 遠くの木 |
| `material` | 描く材質 |
| `shadowMaterial` | 近くの木の影を描く材質（木だけ） |
| `viewer` | 区画を作る基準のカメラ（1 台だけ） |
| `surface` | `EarthSurfaceSetup`（高さの正本をもらう） |

## 一緒に使う部品

| 部品 | 関係 |
|---|---|
| `Logical Transform`（同じ GameObject。必須） | 区画を Logical の子として置く |
| `EarthSurfaceSetup` | 地面の高さを借りる |
| `EarthSkyRenderer` | 目の位置（`TryGetEye`）を借りる |
| Scene BRG（`RadialBatchRendererRegistry`） | 作った Mesh を登録して、まとめて描いてもらう |

!!! warning "つまずきやすい点"
    - 作った区画は Scene に保存されません（`HideFlags.DontSave`）。Scene を見ても岩の GameObject はありません。
    - **岩は影を落としません**（太陽の Light は影なし）。足元の暗がりはシェーダーで似せています。
    - 区画を作るのは `viewer` の 1 台のカメラの周りだけです。Scene View で別の場所を見ても、そこには岩がありません。
    - カメラが地面から高く離れると、全部片付けます。
