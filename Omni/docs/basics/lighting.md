# 照明と「止める」考え方

**結論**：Radial では、画面に描く位置（縮めた位置）と、光の計算に使う位置（本当の位置）が違います。
Omni は、この 2 つを混ぜないように気をつけています。
正しく照らせないときは、**それらしい絵を出さずに止めます**。これを **Fail Closed** と呼びます。

## 困りごと：縮めた位置で光を計算すると、間違う

Radial は遠くの物を手前に寄せて描きます。
もし「寄せた後の位置」で光や影を計算すると、

- ライトからの距離が変わり、明るさが変わる。
- 影の向きや長さが変わる。
- 鏡のような反射がずれる。

といった、**本当とは違う照明**になります。しかも、ぱっと見ではもっともらしく見えてしまいます。

<figure class="caption">
<svg class="fig" viewBox="0 0 720 240" width="720" role="img" aria-label="描く位置と光の計算に使う位置を分ける">
  <rect x="20" y="20" width="320" height="200" rx="12" class="b" stroke-width="2"/>
  <text x="180" y="50" text-anchor="middle" font-size="16" font-weight="700">画面に描く位置</text>
  <text x="180" y="72" text-anchor="middle" font-size="13" class="muted">Radial で縮めた位置</text>
  <text x="180" y="120" text-anchor="middle" font-size="14">どこに見えるか</text>
  <text x="180" y="145" text-anchor="middle" font-size="14">どちらが手前か</text>
  <rect x="380" y="20" width="320" height="200" rx="12" class="a" stroke-width="2"/>
  <text x="540" y="50" text-anchor="middle" font-size="16" font-weight="700">光の計算に使う位置</text>
  <text x="540" y="72" text-anchor="middle" font-size="13" class="muted">本当の位置（Physical Lighting Data）</text>
  <text x="540" y="120" text-anchor="middle" font-size="14">明るさ・影・反射</text>
  <text x="540" y="145" text-anchor="middle" font-size="14">ライトからの距離</text>
  <text x="360" y="200" text-anchor="middle" font-size="22" class="fc">≠</text>
</svg>
<figcaption>2 つの位置を分けて持ち、それぞれの計算に正しい方を使います。</figcaption>
</figure>

## Omni の直し方

- シェーダーには、描く位置とは別に、**本当の位置の情報**（Physical Lighting Data）を渡します。
- 光・影・反射は、その本当の位置で計算します。
  - 影：影を落とす側も受ける側も、同じ本当の位置を使います。
  - 反射：視線の向きを画面の点ごとに計算し直します。
- 本当の位置を渡せない描き方では、**照明を出さずに止めます**（Fail Closed）。

## Fail Closed とは

「失敗したら、閉じた（安全な）側に倒す」という意味です。
電気のブレーカーが、危ないときに電気を止めるのと同じ考え方です。

| 場面 | Omni がすること |
|---|---|
| 本当の位置を渡せない照明の描き方 | 照明を出さない |
| URP の SSAO（画面の陰影）をそのまま使うと間違う | 補正していないものは使わない |
| Deferred の Renderer がある | ビルドを止める（Forward と Forward+ だけ対応） |
| 変換できないシェーダー | 斜線の診断表示にする |

!!! question "なぜ、それらしい絵を出さないの？"
    もっともらしい絵が出ていると、間違いに誰も気づきません。
    はっきり止まれば、原因を探して直せます。Omni は「広さ」は妥協しても「正しさ」は妥協しない、という方針です。

## 照明に関わる部品

焼き込んだ照明を、動かした場所でも正しく読むための部品があります。
詳しくは [照明の空間をそろえる部品](lighting-spaces.md)、手順は [使い方](../guides/light-probe-space.md) を見てください。

| 部品 | 役割 | 付ける場所 |
|---|---|---|
| `OmniLightProbeSpace` ＋ `OmniLightProbeSpaceRequirement` | Light Probe（焼き込んだ周りの明るさ）を、焼いた場所に戻して読む（Scene BRG の物だけ） | 表示の Root（動かす部屋の親） |
| `OmniAdaptiveProbeVolumeSpace` ＋ `OmniAdaptiveProbeVolumeSpaceRequirement` | APV（自動で並ぶ Light Probe）を、焼いた場所に戻して読む（位置のずれだけ） | 同じ表示の Root（Volume も付ける） |
| `OmniLightingSpace` | Logical の正確な住所と、焼き込み用の小さな空間の位置を行き来する（今は開発用の Lightmap と検証 Scene だけ） | 照明の検証用の物 |

!!! warning "つまずきやすい点"
    - Lightmap・Light Probe・Reflection Probe は、原点の近く（安全域 1 万 m の内側）で焼いてください。
      Unity の焼き込みは `float` の位置で計算するためです。
    - URP の Forward では、点光源とスポットライトが BRG の物に当たりません。Forward+ を勧めます。

## Earth デモの照明はさらに特別

Earth デモは、URP のライトで地表を照らしていません。
空の部品 `EarthSkyRenderer` が計算した「大気を通った太陽の光」の値を、地表・岩・木のシェーダーが読んで明るさを決めます。
その値が無いときは、地表を**黒で描きます**（ここでも Fail Closed）。
詳しくは [EarthSkyRenderer](../demos/earth/sky.md) を見てください。
