# <a id="Omni_Editor_Build"></a> Namespace Omni.Editor.Build

### クラス（Classes）

 [OmniBuildShaderClosure](Omni.Editor.Build.OmniBuildShaderClosure.md)

Player に残す Shader を、資産（パス）と理由で求めた結果です。名前は表示にだけ使います。
理由: scene、pipeline（対象ビルドの URP 資産・Renderer と、グローバル設定のうち Player に入る設定が直接参照する Shader）、
brg-sidecar、dependency / usepass / fallback（ShaderLab の宣言を辿ったもの）、runtime-lookup、extra。
元 ↔ Radial の対応は使わない。Player 側に元 ↔ Radial の切り替えは無いので、対応する Shader は残さない（変換の版の確認は、ビルドの前の準備 <code>OmniRadialBuildPreparation</code> の変換保証が行う）。

 [OmniBuildShaderRequest](Omni.Editor.Build.OmniBuildShaderRequest.md)

Player 用に残す Shader の集合を計算する入力です（<xref href="Omni.Editor.Build.OmniBuildShaderClosure.Compute(Omni.Editor.Build.OmniBuildShaderRequest)" data-throw-if-not-resolved="false"></xref>）。

 [OmniBuildShaderScope](Omni.Editor.Build.OmniBuildShaderScope.md)

開発用の Player ビルド（回帰、EarthToMoon、SolarSystem）の間だけ、Scene とパイプラインが使わない Shader の
variant を外します。残す Shader の計算は <xref href="Omni.Editor.Build.OmniBuildShaderClosure" data-throw-if-not-resolved="false"></xref> が行い、この型は
<code>IPreprocessShaders</code>（<xref href="Omni.Editor.Build.OmniBuildShaderStripper" data-throw-if-not-resolved="false"></xref>）を有効にして、外した数を記録するだけです。
製品の Player ビルドには適用しません（利用者のコードが実行時に探す Shader を落とす危険があるため）。

 [OmniDotsRadialGuard](Omni.Editor.Build.OmniDotsRadialGuard.md)

Omni 0.1 はDOTS／Entities Graphicsの描画を対数（Radial）レンダリングの対象にしません。
対数切替とPlayer Buildの前に、DOTSコンテンツを検出したら理由を示して停止します。

 [OmniForwardPlusOnlyBuildScope](Omni.Editor.Build.OmniForwardPlusOnlyBuildScope.md)

Forward+ しか使わない開発用の Player ビルド（EarthToMoon、SolarSystem のデモ）の間だけ、ビルドに入る URP 資産の
Forward の Renderer を Forward+ に切り替えます。URP は資産の Renderer に1つでも Forward があると、Lit 系の
ForwardLit に Forward 用の組合せ（<code>_CLUSTER_LIGHT_LOOP</code> なし）を残すので、Forward+ だけなら約 4分の1 になります。
ビルドする Scene のカメラが Forward の Renderer を使っていたら、見た目が変わるので切り替えずに止めます。
製品と回帰 Player は Forward と Forward+ の両方を対象にするので使いません。Dispose で元の設定へ戻して保存します。
戻せない Renderer があれば、戻せた分を戻してから LogError と <xref href="System.InvalidOperationException" data-throw-if-not-resolved="false"></xref> でビルドを失敗させます
（黙って飛ばすと、Renderer が Forward+ のまま残る）。

 [OmniRadialBuildPreparation](Omni.Editor.Build.OmniRadialBuildPreparation.md)

Player Buildの前に、対数（Radial）版の標準URP Shaderが利用者の環境に揃っていることを保証します。
標準URP Shaderの対数版は同梱せず、対数への切替の準備の段で<code>Assets/Radial</code>（追跡しない）へ生成するため、
新しく取得したプロジェクトやCIの作業ツリーでは、ビルドの前に生成が要ります。

 [OmniRuntimeShaderLookups](Omni.Editor.Build.OmniRuntimeShaderLookups.md)

読み込み済みのアセンブリが <xref href="Omni.OmniRuntimeShaderLookupAttribute" data-throw-if-not-resolved="false"></xref> で宣言した、実行時に
<code>Shader.Find</code> で名前から探す Shader の一覧です。開発用ビルドの Shader 間引き（<xref href="Omni.Editor.Build.OmniBuildShaderScope" data-throw-if-not-resolved="false"></xref>）が
これを残します。宣言は探すコードを持つアセンブリ自身が持つので、製品は他のアセンブリの Shader 名を持ちません。
コード中の <code>Shader.Find("...")</code> の文字列が、そのアセンブリの宣言に含まれることは、テストが検査します。

 [OmniVirtualShadowVariantsBuildScope](Omni.Editor.Build.OmniVirtualShadowVariantsBuildScope.md)

仮想シャドウマップ（<xref href="Omni.OmniVirtualShadowsFeature" data-throw-if-not-resolved="false"></xref>）を使う Player ビルドの間だけ、画面空間の影を受ける Shader の組合せ
（<code>_MAIN_LIGHT_SHADOWS_SCREEN</code>）を Player に残します。

<p>
仮想シャドウマップは、結果を URP の画面空間の影のテクスチャへ書き、標準の受け手（URP Lit・Radial Lit）にはこのキーワードで受けさせます。
URP は、ビルドに入る URP 資産の Renderer のどれにも有効な URP の ScreenSpaceShadows Feature が無いと、この組合せを Player から外します
（ShaderBuildPreprocessor・ShaderScriptableStripper）。外れると、仮想シャドウマップが働く間、標準の受け手が正しく描かれません
（2026-11-12、EarthToMoon の Windows Player で施設と乗り物が青一色になった。Editor は組合せをその場で作るので起きない）。
</p>
<p>
そこで、有効な ScreenSpaceShadows Feature だけを持つ Renderer を作り、ビルドの間だけ URP 資産の Renderer の一覧の末尾へ足します。
この Renderer はどのカメラも使わないので、実行時の描画は変わりません（URP の画面空間の影のパスは走りません）。
Dispose で一覧から外し、作った Renderer を消します。仮想シャドウマップの Feature が無い URP 資産と、もともと ScreenSpaceShadows を
持つ URP 資産は触りません。
</p>

### 構造体（Structs）

 [OmniRuntimeShaderLookups.Lookup](Omni.Editor.Build.OmniRuntimeShaderLookups.Lookup.md)

実行時に名前で探す Shader 1件。

### インターフェース（Interfaces）

 [OmniDotsRadialGuard.IDetector](Omni.Editor.Build.OmniDotsRadialGuard.IDetector.md)

Scene内とEditor WorldのDOTSコンテンツを数えます。

 [OmniDotsRadialGuard.IMaterialOwner](Omni.Editor.Build.OmniDotsRadialGuard.IMaterialOwner.md)

実行時にコードでEntityを作る所有者です。対数の切替の対象にするMaterialを報告し、切替後の作り直しを受けます。

### 列挙型（Enums）

 [OmniBuildShaderClosure.Decision](Omni.Editor.Build.OmniBuildShaderClosure.Decision.md)

Shader の扱い。
