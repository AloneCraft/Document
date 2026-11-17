# 考え方

## 目指すもの

> Unity で「大きさ」を、設計の制約でなくす。

陽子（原子の芯の粒）から、観測できる宇宙の端までを、
**1 つの Scene・1 台のカメラ・いつもの Unity の作り方のまま**、置けて、見えて、ゲームとして出せるようにすることが、最終の目標です。

<figure class="caption">
<svg class="fig" viewBox="0 0 720 150" width="720" role="img" aria-label="陽子から宇宙まで">
  <line x1="40" y1="80" x2="680" y2="80" class="ink" stroke-width="2"/>
  <g font-size="12" text-anchor="middle">
    <circle cx="40" cy="80" r="5" class="fa"/><text x="40" y="60">陽子</text><text x="40" y="108">10⁻¹⁵ m</text>
    <circle cx="190" cy="80" r="5" class="fa"/><text x="190" y="60">人</text><text x="190" y="108">1 m</text>
    <circle cx="300" cy="80" r="5" class="fa"/><text x="300" y="60">地球</text><text x="300" y="108">10⁷ m</text>
    <circle cx="380" cy="80" r="5" class="fa"/><text x="380" y="60">太陽系</text><text x="380" y="108">10¹³ m</text>
    <circle cx="520" cy="80" r="5" class="fa"/><text x="520" y="60">銀河</text><text x="520" y="108">10²¹ m</text>
    <circle cx="680" cy="80" r="5" class="fa"/><text x="680" y="60">宇宙</text><text x="680" y="108">10²⁷ m</text>
  </g>
  <text x="360" y="140" text-anchor="middle" font-size="13" class="muted">およそ 42 桁の違いを、1 つの Scene に置く</text>
</svg>
</figure>

## 6 つの約束

| 約束 | 中身 | 関係するページ |
|---|---|---|
| ① Logical が正本 | 位置の本当の値は Logical が持つ。途中で `float` に落とさない | [Logical](../basics/logical.md) |
| ② Fail Closed | 正しく描けない組み合わせは、それらしい絵を出さずに止める | [照明と「止める」考え方](../basics/lighting.md) |
| ③ どこでも同じ決まり | ふつうの描画と Radial、Scene View と Game View と Player、Legacy と BRG は、同じ空間の決まりを守る。片方だけ正しく見えても合格にしない | [描く道筋](../basics/rendering-paths.md) |
| ④ いつでも標準へ戻せる | 変換は利用者の資産を壊さない。元の Material・GUID・Scene の参照を保つ | [シェーダーの変換](../basics/shader-conversion.md) |
| ⑤ 観測を偽らない | 「当たった・外れた・確かめられなかった」を区別する | [クリックで選ぶ](../basics/picking.md) |
| ⑥ 買った人が自分で確かめられる | 確かめるための Scene（検証 Hub）を製品に入れる | — |

## 「広さ」は妥協し、「正しさ」は妥協しない

Omni が一番大切にしているのは「この絵は正しい」と信じられることです。
宇宙の大きさでは、少しのずれが大きな間違いになり、しかも原因を追いかけるのがとても難しいからです。

そこで、

- **対応する範囲は狭くてよい**（Unity の版、描き方、ビルド先などを絞る）。
- ただし**対応すると言った範囲では必ず正しく**、
- **対応しない範囲では必ず止まる**。

という方針をとっています。

| 妥協するもの（広さ） | 妥協しないもの（正しさ） |
|---|---|
| 対応する Unity の版（0.1 は 6000.6 だけ） | Logical の値を正本にすること |
| 描き方（URP の Forward / Forward+ だけ） | 間違った絵を出さないこと |
| ビルド先（Windows の Direct3D 12 と WebGPU） | 標準へ戻せること |
| すべてのシェーダーの自動変換 | 観測を偽らないこと |
| 性能（まず正しさ、速さは後で測る） | |
| 物理や当たり判定などの遊びの仕組み | |

## Unity の中にとどまる

Omni は自分でゲームエンジンを作りません。Unity と URP の上で動く拡張です。
そのため、Unity の普通の作り方（Scene、Prefab、Material、Shader Graph など）をそのまま使えます。
その代わり、Unity や URP の変化の影響を強く受けます（[良いところ・苦手なところ](pros-cons.md)）。
