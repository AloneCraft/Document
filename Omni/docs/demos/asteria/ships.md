# 船と宇宙の構造物

**結論**：移民船、着陸艇、主星を囲む集光板の群れ（スウォーム）、送電の中継を描く部品たちです。
どれも「画面でどれくらいの大きさに見えるか」や「どれくらい近いか」で、描くか描かないかを切り替えます。

## 大きさで描き方を変える

<figure class="caption">
<svg class="fig" viewBox="0 0 720 200" width="720" role="img" aria-label="画面での大きさで段を切り替える">
  <line x1="40" y1="120" x2="680" y2="120" class="ink" stroke-width="2"/>
  <text x="360" y="190" text-anchor="middle" font-size="13">画面での大きさ（画素）→ 大きいほど近い</text>
  <rect x="40" y="60" width="180" height="50" rx="8" class="c" stroke-width="2"/>
  <text x="130" y="90" text-anchor="middle" font-size="14">段 0：描かない</text>
  <rect x="250" y="60" width="200" height="50" rx="8" class="a" stroke-width="2"/>
  <text x="350" y="90" text-anchor="middle" font-size="14">段 1：粗い形（LOD2）</text>
  <rect x="480" y="60" width="200" height="50" rx="8" class="b" stroke-width="2"/>
  <text x="580" y="90" text-anchor="middle" font-size="14">段 2：細かい形（LOD1）</text>
  <text x="235" y="145" text-anchor="middle" font-size="12">切り替え</text>
  <text x="465" y="145" text-anchor="middle" font-size="12">切り替え</text>
</svg>
<figcaption>移民船の例。新しい段を先に登録してから古い段を外すので、切り替えの瞬間に船が消えません。</figcaption>
</figure>

## 部品の一覧

| 部品 | 付いている所 | 何を描くか | 切り替えの決まり |
|---|---|---|---|
| `AsteriaColonyShip` | `ColonyShip` | 移民船ハルカ（全長 197 m） | 画面での大きさで段 0〜2 |
| `AsteriaLander` | `Lander` | 着陸艇（全長 18 m） | 物語が毎フレーム位置を与える。噴射が 0 なら登録を外す |
| `AsteriaSwarm` | `Swarm` | 主星を囲む 4,000 枚の集光板 | 近い板だけ登録。登録と解除の距離をずらして行ったり来たりしない |
| `AsteriaRelay` | `Relay` | 主星の方向 231 万 km にある送電の中継板と、北極へのビームの管 | 6,000 万 m 以内で登録、9,000 万 m を超えたら解除 |

## 各部品の補足

### AsteriaColonyShip（移民船）

- Mesh は、Editor の道具 `AsteriaShipBaker` が前もって焼いた資産です（実行中に作るのではありません）。
- 項目 `m_Levels` に、段ごとの Mesh と材質を入れます。2 段より少ないと止まります。
- 画面での大きさは Omni の `VirtualObjectSelector.ProjectedPixels` で求めます。

### AsteriaLander（着陸艇）

- 形は `AsteriaLanderModel` が計算で作ります。
- 物語の監督が `Place(位置, 回転, 機首の赤熱, 噴射, 逆噴射)` を呼んで動かします。
- 赤熱や噴射の強さは、シェーダー共通の変数 `_AsteriaLanderGlow` で材質に伝えます。

### AsteriaSwarm（スウォーム）

- 主星の向き × 軌道の半径（1.48 AU）の所に、板を並べます。
- BRG は、登録した後に親が動いても追いかけません。そのため、主星の向きが変わったら板を外して付け直します。

### AsteriaRelay（中継）

- 遠すぎる間は登録しません。近づいたときだけ描きます。

!!! tip "「登録」とは"
    ここでの「登録」は、Omni の Scene BRG（[描く道筋](../../basics/rendering-paths.md)）に
    「この Mesh を描いて」と頼むことです。登録を外せば、Mesh があっても描かれません。
    遠くの物を登録しないことで、GPU の仕事を減らしています。
