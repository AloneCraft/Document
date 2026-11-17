# <a id="Omni_Bake"></a> Namespace Omni.Bake

### クラス（Classes）

 [RadialBakeBinding](Omni.Bake.RadialBakeBinding.md)

シーン内 Renderer の配列を、対応する <xref href="Omni.Rendering.Radial.BakeData" data-throw-if-not-resolved="false"></xref> の
<xref href="Omni.Rendering.Radial.BakeData.Entries" data-throw-if-not-resolved="false"></xref> と同じ並びで保持する橋渡しです。

<p>
GlobalObjectId は Editor 専用でランタイムから引けず、ヒエラルキーパス文字列は
リネームで壊れるため、Unity のシーンローカル参照（コンポーネント経由のオブジェクト参照）で
対応を安定させます。シーンにつき1つ、<code>RadialBaker</code> が生成・更新します。
</p>

 [RadialBakeLookup](Omni.Bake.RadialBakeLookup.md)

シーンから <xref href="Omni.Bake.RadialBakeBinding" data-throw-if-not-resolved="false"></xref> を探す共通ヘルパーです。
<code>RadialCullingSystem</code>（第2層カリング）と <code>RadialFarFieldCache</code>（遠景キャッシュ）の
両方が同じ探索ロジックを必要とするため、ここに切り出します。

 [RadialBakeRegistry](Omni.Bake.RadialBakeRegistry.md)

シーンGUID → <xref href="Omni.Rendering.Radial.BakeData" data-throw-if-not-resolved="false"></xref> の対応表です。プロジェクトに1つ。

<p>
<code>Assets/Radial/Resources/</code> 配下に置き、ランタイムから <xref href="UnityEngine.Resources.Load(System.String)" data-throw-if-not-resolved="false"></xref> で
引けるようにします（<code>[CreateAssetMenu]</code> は使わず、固定パスでロード/生成する
既存の慣習に合わせます）。
</p>
<p>
シーンを開かずにベイク状態を検証したい（<code>OmniValidator</code> の要件）ため、
シーンを開いて <xref href="Omni.Bake.RadialBakeBinding" data-throw-if-not-resolved="false"></xref> を辿る方式ではなく、こちらを正本にします。
</p>

 [RadialBakeSpatialIndexBuilder](Omni.Bake.RadialBakeSpatialIndexBuilder.md)

静的で有効なLogical AABBだけから、入力順に依存しないBVHを構築します。
動的Entryと境界不明Entryは索引へ入れず、後者はFallbackとして可視側に残します。

 [RadialBakeSpatialQuery](Omni.Bake.RadialBakeSpatialQuery.md)

検証済みBake BVHから、静的候補と動的live setを分けて取得します。
古いschema、fingerprint不一致、Binding欠落、構造破損はすべてFailOpenへ倒します。

### 構造体（Structs）

 [RadialBakeSpatialIndex](Omni.Bake.RadialBakeSpatialIndex.md)

<xref href="Omni.Rendering.Radial.BakeData" data-throw-if-not-resolved="false"></xref>に直列化される決定的BVHのペイロードです。
実体はDataの個別配列で保持し、この型はBakerとquery間の不変な受け渡しにだけ使います。

 [RadialBakeSpatialNode](Omni.Bake.RadialBakeSpatialNode.md)

ベイク済み決定的BVHの1ノードです。

 [RadialBakeSpatialQueryContext](Omni.Bake.RadialBakeSpatialQueryContext.md)

refresh境界で完全検証したBake BVHへの非保存参照です。Camera hot pathでは
Binding revisionと配列参照だけを検査し、fingerprint再計算や検証用配列を生成しません。

### インターフェース（Interfaces）

 [IRadialBakeSpatialRelationEvaluator](Omni.Bake.IRadialBakeSpatialRelationEvaluator.md)

Logical AABBと現在の保守的な可視領域との関係を評価します。

### 列挙型（Enums）

 [RadialBakeSpatialAxis](Omni.Bake.RadialBakeSpatialAxis.md)

決定的BVHの分割に使ったLogical軸です。

 [RadialBakeSpatialQueryResult](Omni.Bake.RadialBakeSpatialQueryResult.md)

空間索引queryの成否です。

 [RadialBakeSpatialRelation](Omni.Bake.RadialBakeSpatialRelation.md)

空間ノードと視界との保守的な関係です。<xref href="Omni.Bake.RadialBakeSpatialRelation.Outside" data-throw-if-not-resolved="false"></xref> だけが
対象の除外を許可し、それ以外は可視候補として扱います。
