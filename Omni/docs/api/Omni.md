# <a id="Omni"></a> Namespace Omni

### 名前空間（Namespaces）

 [Omni.Bake](Omni.Bake.md)

 [Omni.BatchRendering](Omni.BatchRendering.md)

 [Omni.Celestial](Omni.Celestial.md)

 [Omni.Converter](Omni.Converter.md)

 [Omni.Core](Omni.Core.md)

 [Omni.Diagnostics](Omni.Diagnostics.md)

 [Omni.Editor](Omni.Editor.md)

 [Omni.Lighting](Omni.Lighting.md)

 [Omni.Localization](Omni.Localization.md)

 [Omni.Logical](Omni.Logical.md)

 [Omni.Observer](Omni.Observer.md)

 [Omni.Rendering](Omni.Rendering.md)

 [Omni.Streaming](Omni.Streaming.md)

 [Omni.Units](Omni.Units.md)

 [Omni.VersionedConversion](Omni.VersionedConversion.md)

 [Omni.VirtualObject](Omni.VirtualObject.md)

### クラス（Classes）

 [RadialTerrainVegetationBinding.DetailMeshPair](Omni.RadialTerrainVegetationBinding.DetailMeshPair.md)

 [ExternalDrawPaths](Omni.ExternalDrawPaths.md)

GPU駆動の独自drawなど、Omniが収集するRenderer・Terrain・BRGの外にある描画経路の公開入口です。
外部経路は独自のcamera packet writerを持たず、ここへ要件を登録します。

 [RadialTerrainVegetationBinding.MaterialPair](Omni.RadialTerrainVegetationBinding.MaterialPair.md)

 [OmniFacePlaneCapability](Omni.OmniFacePlaneCapability.md)

交点方式(面と視線の交点。三角形の 3 頂点の値を画素で読む)を、この環境で使えるかと、使えない理由を返します。

<p>
生成シェーダーは交点方式の SubShader を先に置き、使えない環境では Unity が自動で次の SubShader(奥行き対数補間)を選びます。
奥行き対数補間では、とても長い三角形を視点の近くで見ると、奥行きが崩れることがあります(D05)。
自動で切り替わるので目では分かりにくく、理由を Console(1 回だけ)と検証 Scene の画面に出します。
視点の近くの被覆の欠け(D06)は、どの環境でも <xref href="Omni.OmniNearPatch" data-throw-if-not-resolved="false"></xref>(CPU)が補います。
2026-11-14 までは Geometry Shader も使っていたが、OmniNearPatch に置き換えて外した
(Docs/refactoring-designs/20261114-0400-cpu-near-patch-long-triangles.md)。
</p>

 [OmniHudTooltip](Omni.OmniHudTooltip.md)

実行時の UI Toolkit の HUD で、要素の <xref href="UnityEngine.UIElements.VisualElement.tooltip" data-throw-if-not-resolved="false"></xref> をマウスオーバーで出す。
実行時のパネルは tooltip を自動では出さない（Editor のパネルだけ）ので、HUD の root へ <xref href="Omni.OmniHudTooltip.Attach(UnityEngine.UIElements.VisualElement%2cSystem.Single%2cSystem.Int32%2cSystem.Func%7bSystem.Single%7d)" data-throw-if-not-resolved="false"></xref> を 1 回呼ぶ。
ボタンなどには <code>button.tooltip = "説明"</code> を設定するだけ。説明の板は root の最前面の浮いたラベル（ポインタを受けず、レイアウトに影響しない）。
文字は呼び出し側が渡した言語のまま（この部品は言語を持たない）。HUD を作り直す（root が替わる）ときは、新しい root へ Attach し直す。

 [OmniHudTooltipLogic](Omni.OmniHudTooltipLogic.md)

<xref href="Omni.OmniHudTooltip" data-throw-if-not-resolved="false"></xref> の、UI Toolkit の実体に依らない部分（探索・置き位置・表示の状態）。EditMode で試せる。

 [OmniHudTooltipTracker](Omni.OmniHudTooltipTracker.md)

説明を出す・消すタイミング。ホバーした説明の文字（空なら無し）と時刻を渡し、<xref href="Omni.OmniHudTooltipTracker.Tick(System.Single)" data-throw-if-not-resolved="false"></xref> で今出すべきかを得る。
説明の無い所から有る所へ入ると遅れ後に出る。出ている間に別の説明へ移ると、遅れなしですぐ切り替わる。押した後は、その要素を離れるまで出さない。

 [OmniNearPatch](Omni.OmniNearPatch.md)

とても長い三角形(世界の辺が <xref href="Omni.OmniNearPatch.LongEdge" data-throw-if-not-resolved="false"></xref> を超える)を持つ物に付けます。描くたびに、視点を中心とした箱
(一辺 2 × <xref href="Omni.OmniNearPatch.Reach" data-throw-if-not-resolved="false"></xref>)に入る部分を CPU が double で切り出し、視点を原点にした小さな Mesh として描きます。
float の頂点ではラスタの被覆が本当の三角形から外れ、視点の近くで欠ける(D06 の段 3)のを補います。
元の物はそのまま描きます(同じ面なので重なっても同じ見え方)。
設計: Docs/refactoring-designs/20261114-0400-cpu-near-patch-long-triangles.md

<p>
三角形は Editor で写して保存します(<xref href="Omni.OmniNearPatch.Bake" data-throw-if-not-resolved="false"></xref>)。Player で Mesh の Read/Write が無くても動きます。
LogicalTransform の Inspector で大きな倍率を入れると、自動で付きます。
</p>

 [OmniProductPaths](Omni.OmniProductPaths.md)

Omni本体の置き場所を1か所で解決します。開発プロジェクトでは<code>Assets/Omni/Core</code>、利用者のプロジェクトでは
UPMの<code>Packages/com.omni.rendering</code>です。本体の資産パスをコードや生成シェーダーへ書くときは、
文字列の直書きではなく<xref href="Omni.OmniProductPaths.Combine(System.String)" data-throw-if-not-resolved="false"></xref>を通します。Playerでは資産パスを使わないので
開発時の値のままです。

 [OmniRuntimeShaderLookupAttribute](Omni.OmniRuntimeShaderLookupAttribute.md)

このアセンブリが Player の実行時に <code>Shader.Find</code> で名前から探す Shader を宣言します。
名前で探す Shader は Scene の依存に現れないので、開発用ビルドの Shader 間引きが外さないよう、
探すコードを持つアセンブリ自身が理由つきで宣言します（製品が他のアセンブリの Shader 名を持たないため）。

 [OmniVirtualShadowClipmap](Omni.OmniVirtualShadowClipmap.md)

仮想シャドウマップの段(クリップマップ)。光の向きの正射影で、基準点を中心に段を重ねる。各段はページの格子に合わせた窓(PagesPerAxis² ページ)を持つ。

<p>
座標: 基準点(warp center。Radial を使わない Camera ではカメラ)の Unity の座標を double で受け取り、光の座標の格子番号の整数部と端数を CPU で求める。
GPU は「端数 + 基準点からの相対位置 ÷ テクセル」だけを float で足す(巨大な値どうしを float で引かない)。
ページの番号は Unity の座標に固定した格子の番号なので、Unity の座標の原点が動かない限り、フレームをまたいで同じページを使い回せる。
</p>

 [OmniVirtualShadowDynamicCaster](Omni.OmniVirtualShadowDynamicCaster.md)

仮想シャドウマップ(OmniVirtualShadowsFeature)へ「この物は動く・形が変わる」と知らせる部品。

<p>
仮想シャドウマップは、描いたページを使い回す。動く物・形が変わる物の影は、その物の範囲に重なるページだけを描き直す必要がある。
この部品を付けた物(と子)の、影を落とす Renderer の範囲が動いたら、前の範囲と今の範囲に重なるページが「古い」になり、すぐ描き直される。
位置は変わらないが中身が変わる物(メッシュを作り直した等)は、<xref href="Omni.OmniVirtualShadowDynamicCaster.MarkChanged" data-throw-if-not-resolved="false"></xref> を呼ぶ。
</p>

付けていない動く物の影は、順番の描き直し(Feature の「描き直すページの数」)で数秒遅れて追いつく。

 [OmniVirtualShadowPageCache](Omni.OmniVirtualShadowPageCache.md)

仮想シャドウマップの物理ページの割り当て。ページの番号は Unity の座標に固定した格子(段・X・Y)で、物理ページ(スロット)へ対応させる。

<p>
1 フレーム: 画面が要るページの印(GPU のビット列。要求したときの窓の相対位置)を受け取り、まだ無いページを数え、
1 フレームの上限まで割り当てて描くページの一覧を作る。粗い段から先に割り当てる(どの画素にも早く何かの影が出るように)。
置き場が足りなければ、しばらく要求されていないページから外す(LRU)。今のフレームで要求されたページは外さない。
</p>

光の向きが変わったときは、描いたページを「古い」として残しながら描き直す(<xref href="Omni.OmniVirtualShadowPageCache.MarkAllStale" data-throw-if-not-resolved="false"></xref>)。
Unity の座標の原点が動いたときは、番号の意味が変わるので全部捨てる(<xref href="Omni.OmniVirtualShadowPageCache.Clear" data-throw-if-not-resolved="false"></xref>)。

 [OmniVirtualShadowTiles](Omni.OmniVirtualShadowTiles.md)

仮想シャドウマップの、このフレームに描くページを「タイル」(同じ段の、ページの格子で TilePages × TilePages の区画)にまとめる。

<p>
ページごとに影を落とす物を描くと、描画の回数がページ数に比例する(起動直後は数千ページ)。タイルごとに 1 回だけ作業用の深度へ描き、
要るページだけを置き場へ写すと、描画の回数はタイル数になる。同じ段のページはテクセルの大きさが同じなので、1 つの正射影で描ける。
</p>

 [OmniVirtualShadowsFeature](Omni.OmniVirtualShadowsFeature.md)

主光源(Directional)の仮想シャドウマップ(Docs/Plans/VirtualShadowMaps.md)。結果は URP の画面空間の影(_ScreenSpaceShadowmapTexture、_MAIN_LIGHT_SHADOWS_SCREEN)へ書くので、
URP Lit・Omni の生成シェーダー・画面空間の影を受け取る自前のシェーダーは変えずに受け取れる。

<p>
1 フレーム: (1) 光の向き・カメラの位置から段の窓を決める。(2) 前のフレームまでの要求の読み戻しから、まだ無いページを割り当て、その範囲の正射影で影を落とす物を物理ページの置き場へ描く。
(3) 深度の前段の後に、画素ごとに要るページの印を付け(読み戻す)、段とページを引いて画面空間の影を書く。(4) 透明物の前でキーワードを戻す。
</p>

使えないとき(ランダム書き込みが無い・WebGPU・主光源が無い・影なし)は何もしない(URP のカスケード影のまま)。理由を 1 回だけ警告する。
対象は Game の主カメラ(Camera.main)だけ(置き場を 1 つにするため)。それ以外のカメラは URP のカスケード影のまま。

 [OmniVirtualShadowsSceneSwitch](Omni.OmniVirtualShadowsSceneSwitch.md)

この部品がある Scene では、Renderer の仮想シャドウマップ(OmniVirtualShadowsFeature)を、既定が無効でも使う。
全ての Scene で使うときは Feature の「全ての Scene で使う」をオンにする。

 [RadialCamera](Omni.RadialCamera.md)

カメラに付与し、RadialGlobal 対数ワープのパラメータを保持するデータホルダです。
写像は Smooth Log（S = 1）だけで、曲線・S・線形半径の設定はありません（<xref href="Omni.RadialSettings" data-throw-if-not-resolved="false"></xref>）。
設定は論理 Near／Far Clip だけで、View Scale M は <code>Camera の Near ÷ nearClip</code> で決まります。
実際の適用は <xref href="Omni.RadialGlobalRenderSystem" data-throw-if-not-resolved="false"></xref> が
beginCameraRendering でカメラごとに、登録済み Renderer の MaterialPropertyBlock へ
書き込みます（旧: 本コンポーネントが Shader.SetGlobal* でグローバル設定）。
グローバルは SRP Batcher（UnityPerMaterial CBUFFER）に無視され、かつ複数カメラで
競合するため MaterialPropertyBlock 方式へ移行しています。

 [RadialCameraToggle](Omni.RadialCameraToggle.md)

Play中に <xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref> の有効／無効を切り替え、同じ視点で標準描画と対数描画を
見比べるためのコンポーネントです。RadialCameraを持つCameraへ付けて使います。

 [RadialCullingBoundsBuilder](Omni.RadialCullingBoundsBuilder.md)

Logical AABB を GPU の Radial 写像後にも必ず包む、Unity 標準カリング用のワールド Bounds を構築します。
Galaxy と Saturn の通常 MeshRenderer 経路で使い、BRG の独自カリングには使いません。

 [RadialCullingSystem](Omni.RadialCullingSystem.md)

ベイク済みのLogical AABB（<xref href="Omni.Rendering.Radial.BakeEntry" data-throw-if-not-resolved="false"></xref>）を使い、near/far方向の
放射距離をLogical正本で判定してカリングする「第2層」です。

<p>
<xref href="Omni.RadialGlobalRenderSystem" data-throw-if-not-resolved="false"></xref> のUnity cullingMatrix 補正（第1層）は保守的broad phaseに限定し、
こちらがベイク済みLogical AABBと現在のLogicalカメラ位置から真の放射距離レンジを求める権威値です。
錐台の側面4平面の判定はワープ不変（レイ上の移動は角度を変えない）なので Unity標準の
カリング（第1層で補正済みの cullingMatrix を使う）にそのまま任せ、
このシステムは near/far のみを <xref href="UnityEngine.Renderer.forceRenderingOff" data-throw-if-not-resolved="false"></xref> で追加カリングします。
</p>
<p>
対象は「静的（<xref href="Omni.Rendering.Radial.BakeEntry.IsStatic" data-throw-if-not-resolved="false"></xref>）」なベイク済みEntryのみです。
動的オブジェクトはベイク時のLogical AABBが現在の実位置と一致する保証が無いため対象外とし、
Unityの保守的broad phaseにのみ委ねます。
</p>
<p>
<xref href="UnityEngine.Renderer.forceRenderingOff" data-throw-if-not-resolved="false"></xref> はカメラ非依存のグローバルなフラグです。
本システムは <xref href="Omni.RadialGlobalRenderSystem" data-throw-if-not-resolved="false"></xref> と同じ前提（1フレーム内でカメラは順次描画され、
同時にアクティブなのは1台）の上で、カメラごとの beginCameraRendering 直前に毎回評価し直すことで
正しく機能します。この前提が崩れる状況（Play モード中に Game カメラと Scene View が同一フレーム内で
両方描画されるなど）では、<xref href="Omni.RadialWarpSource.ApplyShellCulling" data-throw-if-not-resolved="false"></xref> が false のカメラに
<xref href="Omni.RadialCullingSystem.ApplyShellCulling(UnityEngine.Camera%2cOmni.RadialCamera)" data-throw-if-not-resolved="false"></xref> を呼ばせず、代わりに <xref href="Omni.RadialCullingSystem.ClearAll" data-throw-if-not-resolved="false"></xref> を呼ばせます。
</p>
<p>
<xref href="Omni.RadialCullingSystem.ApplyShellCulling(UnityEngine.Camera%2cOmni.RadialCamera)" data-throw-if-not-resolved="false"></xref> と <xref href="Omni.RadialCullingSystem.ClearAll" data-throw-if-not-resolved="false"></xref> は非対称です。前者は
<code>forceRenderingOff = true</code> を含むため、権限の無いカメラが呼ぶと他カメラで見えるべき物が
消えます（fail-closed、危険）。後者は <code>false</code> しか書かないため、権限の無いカメラが呼んでも
実害はありません（fail-open、安全）。呼び出し側（RadialGlobalRenderSystem）はこの非対称性に
従い、権限の無いカメラには常に <xref href="Omni.RadialCullingSystem.ClearAll" data-throw-if-not-resolved="false"></xref> 側を呼ばせます
（前フレームの通常カメラの判定がそのまま残ることを防ぎます）。
</p>

 [RadialFarFieldCache](Omni.RadialFarFieldCache.md)

遠景（<xref href="Omni.Rendering.Radial.BakeEntry.FarFieldGroup" data-throw-if-not-resolved="false"></xref> が割り当てられた静的Renderer群）の
ワープパラメータMPB更新を、カメラが十分動くまで省略するキャッシュです。

<p>
ThresholdLinearLog で <code>d &gt;&gt; R</code> のとき <code>mapped(d) = R + S・log2(d/R)</code> であり、
カメラが δ 動いたときの写像距離の変化は概ね <code>S・δ/(d・ln2)</code>、角度の変化は概ね <code>δ/d</code> です。
十分遠い対象ではワープ後の描画はカメラ移動に対してほぼ不変になるため、<code>RadialBaker</code> が
ベイク時に許容角度誤差εから求めた無効化半径
<code>δmax = ε・dMin</code>（<xref href="Omni.Rendering.Radial.FarFieldGroup.InvalidationDistance" data-throw-if-not-resolved="false"></xref>）の範囲内であれば、
前回書き込んだMPB値をそのまま使い回してよいとみなします。
</p>
<p>
<xref href="Omni.RadialGlobalRenderSystem" data-throw-if-not-resolved="false"></xref> が対象Rendererを1つずつ処理する際、このキャッシュへ
「このRendererは今フレームMPB更新をスキップしてよいか」を問い合わせます。
</p>

 [RadialGlobalRenderSystem](Omni.RadialGlobalRenderSystem.md)

RadialGlobal対数ワープのcamera共有packetと、Logical/特殊Renderer用の精密
MaterialPropertyBlockを配布する描画システムです。ordinary opaque MeshRendererは
unity_ObjectToWorldを使う共有経路へ移し、CameraごとのRenderer走査を行いません。

対象 Renderer は「RadialGlobal シェーダーのマテリアルを持つ Renderer」を
自動収集します（マーカーコンポーネント不要）。シーン読み込み・Hierarchy 変更・
初回に再スキャンし、通常フレームでは既存の収集結果を使い回します。

<xref href="UnityEngine.Terrain" data-throw-if-not-resolved="false"></xref> は <xref href="UnityEngine.Renderer" data-throw-if-not-resolved="false"></xref> ではなく <xref href="UnityEngine.Behaviour" data-throw-if-not-resolved="false"></xref> 派生の
ため上記の走査には原理的に掛かりません。そこで Terrain だけは別に収集し、
<xref href="UnityEngine.Terrain.SetSplatMaterialPropertyBlock(UnityEngine.MaterialPropertyBlock)" data-throw-if-not-resolved="false"></xref>（Terrain 版の MPB API）へ
まったく同じ値を書き込みます。判定は Renderer と共通の <xref href="Omni.RadialGlobalRenderSystem.IsRadialMaterial(UnityEngine.Material)" data-throw-if-not-resolved="false"></xref> です。

かつては <xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref> / RadialGlobalEditorDriver が
Shader.SetGlobal* でグローバル設定していましたが、当該 uniform が
UnityPerMaterial CBUFFER 内にあると SRP Batcher がマテリアル値を優先して
無視され、かつグローバルは複数カメラ（Game/Scene 同時）で「最後に書いた
カメラが勝つ」共有状態になります。MaterialPropertyBlock は Unity が
beginCameraRendering → DrawRenderers のカメラごとの記録時に読み取るため、
カメラごとに正しくスコープされます。

 [RadialGlobalWarpSourceRegistry](Omni.RadialGlobalWarpSourceRegistry.md)

「どのカメラを描画するか」と「どこを中心にワープするか」を分離するための
カメラ単位のレジストリです。

<p>
<xref href="Omni.RadialGlobalRenderSystem" data-throw-if-not-resolved="false"></xref> は通常、描画中カメラ自身の
<xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref> をワープ元にします。観察カメラのように
「カメラAの投影を適用した世界を、カメラBから外部観察する」場合は、観察カメラ自身に
ドライバを持たせず、本レジストリで観察カメラと投影中心ドライバを対応付けます
（<code>Omni.Observer.RadialObserverRig</code> が利用します）。
</p>
<p>
観察カメラにドライバを持たせない点が重要です。共有 Unity Transform を書き換える
システムはどれも <code>camera.GetComponent&lt;RadialCamera&gt;()</code> を要求し、
本レジストリを参照しません。したがって観察カメラはそれらの対象外となり、
「観察用の Unity 座標を共有 Transform へ書き込まない」ことが構造的に保証されます。
</p>
<p>
登録時にはワープ元のほかに、カメラ単位の <xref href="Omni.Logical.SceneViewRenderContext" data-throw-if-not-resolved="false"></xref>
の供給元を渡せます。Editor の Scene View は <xref href="Omni.RadialGlobalRenderSystem.SceneViewContextProvider" data-throw-if-not-resolved="false"></xref>
でこれを供給しますが、Game／Player の観察カメラにはそれが無いため、同じ契約
（仮想論理視点と比較モード）をここから渡します。
</p>
<p>
既存の <xref href="Omni.RadialGlobalRenderSystem.SceneViewDriverProvider" data-throw-if-not-resolved="false"></xref>（単一スロット）は
変更しません。本レジストリは解決順序の中間に入り、登録の無いカメラでは
従来どおり Provider が呼ばれます。
</p>

 [RadialIdentityWarp](Omni.RadialIdentityWarp.md)

同じGameObjectのRendererまたはTerrainだけを、Radial Shaderのまま対数写像を恒等にして描画します。

 [RadialLightProxy](Omni.RadialLightProxy.md)

安全域の外にある Spot／Point Light の Unity Transform を、描画する Camera ごとの camera 相対位置へ置きます。

<p>
URP の追加ライトの位置・範囲・影行列は、Light の Unity Transform から作られます。Logical 位置が巨大な光の
Unity Transform は代理値（原点）になるため、そのままでは範囲外として照明にも影にも寄与しません。
この Component は、描画の直前に「光の Logical 位置 - Camera の Logical 位置」を有限値にして、native Camera
の位置（安全域外では原点 proxy）へ足した位置を、所有権つきの表示用代理位置として設定します。
ユーザーの Transform を外から書き換えず、<xref href="Omni.Logical.Transform" data-throw-if-not-resolved="false"></xref> の単一書き手の制約を守ります。
</p>
<p>
安全域内の光には何もしません。複数 Camera では、描画する Camera ごとに値を書き直します。
</p>

 [RadialMaterialContract](Omni.RadialMaterialContract.md)

MaterialのShaderが、OmniのRadial変換の契約（<code>_RadialGlobal_UseRadialTransform</code>）を宣言しているかを判定します。

 [RadialPhysicalBounds](Omni.RadialPhysicalBounds.md)

Rendererの物理（Radialで圧縮する前）のworld Boundsを返します。
Radial有効中の <xref href="UnityEngine.Renderer.bounds" data-throw-if-not-resolved="false"></xref> は、描画するCameraごとに <xref href="Omni.RadialRendererBoundsRegistry" data-throw-if-not-resolved="false"></xref> が
カリング用の保守Boundsへ書き換えるため、物理の位置関係（交差、包含、可視判定、画面上の大きさ）には使えません。
直前に描いたCamera次第で物理から離れた値になります。

 [RadialRendererBoundsRegistry](Omni.RadialRendererBoundsRegistry.md)

Radial描画用の保守BoundsをRendererへ適用し、Camera間では再利用しながら
現viewで触られなかった対象だけを元のBoundsへ戻すRegistryです。
Galaxy、Gardenなど通常MeshRendererのUnity標準カリング経路で使い、BRGは扱いません。

 [RadialShellPolicy](Omni.RadialShellPolicy.md)

Radial near/farシェルのfail-open判定規約です。
SaturnシーンのMesoリングBRG Jobは、距離算出に失敗したセルを
<xref href="Omni.RadialShellRelation.Indeterminate" data-throw-if-not-resolved="false"></xref>として本規約へ渡します。

 [RadialSwitchExcludedCamera](Omni.RadialSwitchExcludedCamera.md)

この Camera(と子の Camera)を、対数への切り替えの対象から外す目印です。付けた Camera には RadialCamera が付かず、
標準の Unity のまま描きます。標準の Unity と Omni を同じ Scene で並べて比べる検証 Scene(Functions/Basics)などで使います。

 [RadialTerrainPatchRegistry](Omni.RadialTerrainPatchRegistry.md)

TerrainDataを正本として、Radial描画に使う非保存MeshRenderer patchを管理します。

<p>
これはGalaxy/Saturn等のSceneへコンポーネントを保存しないRuntime registryです。Native Terrainを
隠すのは全patchを構築できた<xref href="Omni.RadialTerrainBackendState.Ready" data-throw-if-not-resolved="false"></xref>後だけで、構築失敗・
解除・Scene境界では必ず元の<xref href="UnityEngine.Terrain.drawHeightmap" data-throw-if-not-resolved="false"></xref>へ戻します。
</p>
<p>
写像しないCameraが描く間は、patchを壊さずに隠して元の表示へ戻します
（<xref href="Omni.RadialTerrainPatchRegistry.HideForCamera(UnityEngine.Terrain)" data-throw-if-not-resolved="false"></xref>／<xref href="Omni.RadialTerrainPatchRegistry.ShowAfterCamera(UnityEngine.Terrain)" data-throw-if-not-resolved="false"></xref>）。写像するCameraと交互に描いても作り直しません。
</p>
<p>
現段階は33×33相当の固定LOD 0を提供する安全な土台です。カメラ依存quadtree選択は、
呼び出し側がpatch一覧をカメラ別に利用できるようになってから追加します。
</p>

 [RadialTerrainVegetationBackend](Omni.RadialTerrainVegetationBackend.md)

TerrainDataを正本に保ち、非保存の植生描画（木・mesh detail）だけを組み立てます。
組み立てられない木のprototypeやdetailは、そのprototypeだけをFail Closedで外して診断へ記録し、
他の植生は描画します（1つの非対応素材で全植生が消えないようにするため）。

 [RadialTerrainVegetationBinding](Omni.RadialTerrainVegetationBinding.md)

元の地形・Prefab・Materialを変更せず、植生用の生成MaterialをSceneへ保持します。

 [RadialVfxRendererRegistry](Omni.RadialVfxRendererRegistry.md)

VFXRendererの所属だけをtarget refresh時に記録し、Camera/Repaint hot pathで
Scene走査を行わず最新native BoundsをRadial world Boundsへ変換します。
Boundsの所有・復元自体は共通RadialRendererBoundsRegistryへ委譲します。

 [RadialViewRegistry](Omni.RadialViewRegistry.md)

カメラ描画ごとの不変<xref href="Omni.Rendering.Radial.ViewSnapshot" data-throw-if-not-resolved="false"></xref>を、Unity 6000の
<xref href="UnityEngine.EntityId" data-throw-if-not-resolved="false"></xref> viewIDで管理するレジストリです。BRGのculling callbackは
<code>context.viewID.GetEntityId()</code>で得た値から本レジストリを読むため、
Shader.SetGlobal*をカメラ状態の正本にしません。SaturnシーンのMesoリングBRG描画で使用します。

### 構造体（Structs）

 [RadialRendererBoundsRegistry.Diagnostics](Omni.RadialRendererBoundsRegistry.Diagnostics.md)

Bounds Registryの累積処理量と直近viewの処理量です。

 [RadialVfxRendererRegistry.Diagnostics](Omni.RadialVfxRendererRegistry.Diagnostics.md)

 [OmniVirtualShadowClipmap.Level](Omni.OmniVirtualShadowClipmap.Level.md)

1 段の状態。

 [OmniVirtualShadowSettings](Omni.OmniVirtualShadowSettings.md)

仮想シャドウマップの数値(Docs/Plans/VirtualShadowMaps.md)。

 [OmniVirtualShadowStatistics](Omni.OmniVirtualShadowStatistics.md)

仮想シャドウマップの 1 フレームの状態(診断用)。

 [OmniVirtualShadowPageCache.PageKey](Omni.OmniVirtualShadowPageCache.PageKey.md)

ページの番号(段と Unity の座標に固定した格子の X・Y)。

 [RadialCullingBoundsResult](Omni.RadialCullingBoundsResult.md)

1 Renderer・1 カメラ描画スコープに対する標準カリング用 Bounds の不変結果です。

 [RadialSettings](Omni.RadialSettings.md)

Radial（対数）ワープのパラメータ一式です。

<p>
写像は Smooth Log ひとつだけです: <code>F(d) = S·log2(1 + d·M/S)</code>、S = <xref href="Omni.RadialSettings.RadialScale" data-throw-if-not-resolved="false"></xref> = 1（定数）。
線形域（ThresholdLinearLog）や曲線・S の選択は持ちません。近くがほぼ恒等（一様な拡大）になる構成では、
写像の扱いの誤りが近景で見えず、描画の不具合を見つけられないためです（2026-10-04 の判断）。
調整できるのは View Scale M（<code>Camera の Near ÷ 論理 near</code>）だけで、曲がり始めは論理距離で約 1/M です。
</p>
<xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref> の該当フィールドから取り込み、GPU頂点ワープ
（<code>Omni/RadialGlobalLit</code> シェーダーのOmni Radial写像）と
CPU側のTransform書き換えが同一のカーブを共有するための単一の正本です。
RuntimeのCPU写像は、この型のLogical演算を正本とします。

 [RadialTerrainPatchDiagnostics](Omni.RadialTerrainPatchDiagnostics.md)

<xref href="Omni.RadialTerrainPatchRegistry" data-throw-if-not-resolved="false"></xref> の読み取り専用診断値です。
Omni Manager/ValidatorがTerrainDataを変更せずにbackendの状態を表示するために使います。

 [RadialWarpSource](Omni.RadialWarpSource.md)

あるカメラのワープ元（<xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref>）と、それを適用してよい範囲を
まとめて表します。

<p>
適用範囲を <code>ApplyCullingMatrixOverride</code> と <code>ApplyShellCulling</code> の
2 段に分けているのは、両者の安全性がまったく違うためです。
<code>camera.cullingMatrix</code> は Unity がカメラごとに保持するプロパティなので、
ワープ中心が描画中カメラ自身の位置と一致してさえいれば、誰が上書きしても
他のカメラには影響しません。一方 <code>Renderer.forceRenderingOff</code> は
カメラに紐付かないグローバルなフラグで、「1 フレーム内でカメラは順次描画され、
同時にアクティブなのは 1 台」という前提の上でしか安全に使えません
（<xref href="Omni.RadialCullingSystem" data-throw-if-not-resolved="false"></xref> 参照）。Play モード中は Game カメラと
Scene View が同一フレーム内で両方描画されるためこの前提が崩れるので、
シェルカリングだけは「権限を持つカメラ」に限定します。
</p>
<p>
<code>ApplyShellCulling</code> は <code>ApplyCullingMatrixOverride</code> の部分集合です
（シェルカリングを適用してよいなら cullingMatrix の上書きも必ず妥当）。
呼び出し側が矛盾した組み合わせを作れないよう、生成はファクトリメソッド経由に限定しています。
</p>

 [OmniVirtualShadowPageCache.RenderRequest](Omni.OmniVirtualShadowPageCache.RenderRequest.md)

このフレームに描くページ。

 [ShadowVector2d](Omni.ShadowVector2d.md)

double の 2 次元ベクトル。

 [ShadowVector3d](Omni.ShadowVector3d.md)

double の 3 次元ベクトル(仮想シャドウマップの CPU の計算用)。

 [OmniVirtualShadowTiles.Tile](Omni.OmniVirtualShadowTiles.Tile.md)

タイル。X・Y はタイルの格子の番号(ページの番号 ÷ TilePages の切り捨て)。Start から Count 個が、並べ替えた一覧の中のこのタイルのページ。

### 列挙型（Enums）

 [ExternalDrawRequirements](Omni.ExternalDrawRequirements.md)

Renderer収集外の外部描画経路が、Omniのcamera準備へ参加するときに宣言する要件です。

 [RadialCullingBoundsFailure](Omni.RadialCullingBoundsFailure.md)

保守 Bounds を厳密に構築できなかった理由です。診断画面では原因別の件数集計に使います。

 [RadialCullingBoundsStatus](Omni.RadialCullingBoundsStatus.md)

Radial 頂点ワープ後の Renderer 候補を Unity 標準カリングへ渡すための結果状態です。

 [RadialShellRelation](Omni.RadialShellRelation.md)

2つの論理シェル境界の比較結果です。<xref href="Omni.RadialShellRelation.Indeterminate" data-throw-if-not-resolved="false"></xref>は演算失敗・
overflow・非有限入力を表し、描画判定では必ず可視側へ倒します。

 [RadialTerrainBackendState](Omni.RadialTerrainBackendState.md)

Radial描画用Terrainパッチbackendのライフサイクル状態です。
TerrainDataは常に正本であり、この状態は非保存の描画派生物だけを表します。

 [ViewportVetoKind](Omni.ViewportVetoKind.md)

Scene Viewの高精度（仮想）ビューポートを使えない理由の種類です。
UIはこの種類から利用者へ対処（対数レンダリングへの切替など）を案内します。
