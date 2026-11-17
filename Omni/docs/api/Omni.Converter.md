# <a id="Omni_Converter"></a> Namespace Omni.Converter

### 名前空間（Namespaces）

 [Omni.Converter.Guarantees](Omni.Converter.Guarantees.md)

### クラス（Classes）

 [OmniMaterialShaderSwitchService.BuiltInPlanItem](Omni.Converter.OmniMaterialShaderSwitchService.BuiltInPlanItem.md)

 [OmniMaterialShaderMappingStore.BuiltInReplacement](Omni.Converter.OmniMaterialShaderMappingStore.BuiltInReplacement.md)

 [OmniMaterialShaderSwitchService.DiagnosticPlanItem](Omni.Converter.OmniMaterialShaderSwitchService.DiagnosticPlanItem.md)

 [OmniMaterialShaderMappingStore.DiagnosticReplacement](Omni.Converter.OmniMaterialShaderMappingStore.DiagnosticReplacement.md)

 [OmniRadialGraphWarningAcknowledgements.Entry](Omni.Converter.OmniRadialGraphWarningAcknowledgements.Entry.md)

確認済みの Graph と、記録したときの内容の指紋です。

 [OmniCustomShaderConversionConfirmations.Entry](Omni.Converter.OmniCustomShaderConversionConfirmations.Entry.md)

確認済みの記録と、承認した検出です。

 [OmniRadialShaderSubstitutes.Entry](Omni.Converter.OmniRadialShaderSubstitutes.Entry.md)

元のShaderと代わりのShaderの組です。

 [OmniMaterialShaderMappingStore.Entry](Omni.Converter.OmniMaterialShaderMappingStore.Entry.md)

 [OmniBuildRadialDecision](Omni.Converter.OmniBuildRadialDecision.md)

Player Build 1回分の判定です。

 [OmniBuildRadialScope](Omni.Converter.OmniBuildRadialScope.md)

Player Build が対数（Radial）レンダリングを使うかの判定を 1 か所にまとめます。対数を使わないビルドでは、Omni の
ビルドの準備・検査（Scene BRG、Render Objects の検査、BRG sidecar と manifest、対数版の Shader の準備、variant の予算など）は
何もせず、ビルドに関与しません（2026-10-09 のユーザー判断）。各入口は <xref href="Omni.Converter.OmniBuildRadialScope.IsStandardPlayerBuild(UnityEditor.Build.Reporting.BuildReport)" data-throw-if-not-resolved="false"></xref> が true なら何もせずに戻ります。

 [OmniBuiltInToUrpUpgrade](Omni.Converter.OmniBuiltInToUrpUpgrade.md)

Built-in RP専用のParticle Shaderを、URPのMaterial Upgrader（Unity標準）でURPのShaderへ移してから
Omniの対数変換へ渡すための入口です。Omniは変換表を持たず、Shaderの対応とPropertyの写し方は
URPのUpgraderに任せます。元のMaterialは書き換えず、呼び出し側が作る管理Materialの写しにだけ適用します。
範囲はParticle系に限ります（Legacy Shaders等は未対応のまま診断表示にします）。

 [OmniComparisonAssets](Omni.Converter.OmniComparisonAssets.md)

標準と対数を見比べる比較Sceneと、その元（URP）のMaterialを、全体の標準／対数の切替から守ります。

 [OmniCustomShaderConversionConfirmations](Omni.Converter.OmniCustomShaderConversionConfirmations.md)

自作 Shader（利用者が編集できる .shader／.shadergraph）の AI 変換依頼で、機械判定に合格した結果を利用者が
「確認済み」にした記録と、機械判定の誤検出を「この検出は誤り」と承認した記録を持つ表です。
プロジェクトのアセットなので Git で共有できます（<xref href="Omni.Converter.OmniRadialGraphWarningAcknowledgements" data-throw-if-not-resolved="false"></xref> と同じ作りです）。

<p>
項目は元 Shader と、確認したときの（元の指紋, 出力の指紋）です。元か出力が変わると指紋が合わなくなり、
「確認済み」から「変換済み・未確認」へ戻ります。指紋は <code>OmniSourceFingerprints</code> が取った値を文字列で受け取ります
（この表は指紋の式を知りません）。
</p>
<p>
承認した検出は、検出箇所の指紋の一覧として元 Shader ごとに持ちます。確認済みにする前にも承認できるので、
項目は「確認なしで承認だけ」の状態を取れます。
</p>

 [OmniExternalMaterialSources](Omni.Converter.OmniExternalMaterialSources.md)

外部Material供給元の登録簿です。

 [OmniGeneratedAssetPaths](Omni.Converter.OmniGeneratedAssetPaths.md)

配布物とプロジェクト固有の生成物を分離するための正規パスです。

 [OmniGuidManifest](Omni.Converter.OmniGuidManifest.md)

<code>Assets/Radial/</code> 配下の生成物パス→GUID の対応を記録する、
Unity Assetではないプロジェクト設定マニフェストです。正本は
<code>ProjectSettings/Omni/Generated.manifest.json</code>に置きます。

<p>
<code>Assets/Radial/</code> はディスク上のキャッシュとして丸ごと削除・
再生成できますが、削除後に再生成すると <xref href="UnityEditor.AssetDatabase.CreateAsset(UnityEngine.Object%2cSystem.String)" data-throw-if-not-resolved="false"></xref>
は新しい GUID を発行します。シーンファイルは committed であり、生成物への
参照が GUID で焼き込まれているため、削除→再生成のたびにシーン参照が
永久に壊れる事故が起きていました（2026-08-01 のTerminalScene破損の根本原因）。
</p>
<p>
Unity は、アセットをインポートする前に <code>.meta</code> ファイルが既に存在していれば
そこに書かれた GUID を採用します。このマニフェストは「このパスには過去このGUIDを
割り当てた」という記録を git 管理下に置き、次回生成時に同じ GUID の <code>.meta</code> を
先に書き込むことで、フォルダを丸ごと消して作り直しても GUID が再現されるようにします。
</p>

 [OmniMaterialShaderMappingStore](Omni.Converter.OmniMaterialShaderMappingStore.md)

既存Materialを直接Omni Shaderへ切り替えた履歴を永続化します。
Libraryやstatic状態に依存せず、Editor再起動後も同じMaterialを復元できます。

 [OmniMaterialShaderSwitchService](Omni.Converter.OmniMaterialShaderSwitchService.md)

書込可能なMaterialはShaderを切り替え、読取専用のMaterialは管理用の写しへ参照を切り替えます。
解析と変更を分離し、対象が1件でも不正なら書き込み前に停止します。

 [OmniRadialExemptShaders](Omni.Converter.OmniRadialExemptShaders.md)

Radialへ変換しないと決めた標準URP Shaderの一覧です(2026-09-30の判断)。
URPの2D Shader(Sprite／Mesh2D／Sprite Mask)はフォークを持たず、カタログにも登録しません。
カタログは「標準→Radial」の対なので、Radial側が空の登録は未登録扱いになり、診断表示とPlayer Buildの中止を招くためです。
名前やタグでの推測はせず、パッケージ内の正確なパスだけで判定します。
実行時の扱いは変わりません。<code>Omni.Logical.Transform</code>の下にある間はRadialのカメラで安全側に非表示になり、外にあれば標準描画です。
モバイル向けのTextMesh Pro Shader（<code>TextMeshPro/Mobile/*</code>とその派生）も対象外です。Omni 0.1.xはモバイルを
対象にしないためで、デスクトップ向けにはURP用のShader Graph（TMP_SDF-URP Lit/Unlit）を変換します。

 [OmniRadialGraphWarningAcknowledgements](Omni.Converter.OmniRadialGraphWarningAcknowledgements.md)

Radial へ変換するときに視線の警告（変換器が直せない View Direction などの使い方）が出る Shader Graph のうち、
利用者が手で直した・問題ないと確かめたものを「確認済み」として記録する表です。プロジェクトのアセットなので Git で共有できます。
項目は元の Graph と、記録したときの Graph の内容の指紋です。Graph を変えると指紋が合わなくなり、警告が戻ります。
解除は Omni Manager の Shaders タブ（1 件・すべて）か、このアセットの Inspector（すべて・項目の削除）で行います。

 [OmniRadialOutputMigration](Omni.Converter.OmniRadialOutputMigration.md)

旧配置 <code>Assets/Radial/User/&lt;パッケージ名&gt;/…</code> の Shader・Shader Graph（とその <code>*_Materials</code>）を、
現在の規則 <code>Assets/Radial/Packages/&lt;パッケージ名&gt;/…</code>（<xref href="Omni.Converter.RadialMaterialConverter.GetOmniOutputPath(System.String)" data-throw-if-not-resolved="false"></xref>）へ
<b>移動</b>します。

 [OmniRadialShaderSubstitutes](Omni.Converter.OmniRadialShaderSubstitutes.md)

Omniが変換できないShader（固定機能やBuilt-in専用など）の代わりに、利用者が用意したURPの
Shaderを変換元として登録する表です。元のShaderとファイルは変えず、元のShaderを使うMaterialを
Radialへ切り替えるときだけ、代わりのShaderから生成したRadial版を使います。標準へ戻すと元のShaderへ戻ります。
代わりのShaderは元のShaderの全Propertyを同じ名前・同じ型で宣言し、URPのShaderとして通常の
検証（OmniShaderPipelineValidator）を通らなければなりません。どちらかを満たさなければ変換しません。

 [OmniShaderCatalogResolver](Omni.Converter.OmniShaderCatalogResolver.md)

標準URP Shaderと、その対数（Radial）版の対応を、利用者の環境の生成物から解決します。
対応は<xref href="Omni.Converter.OmniStandardUrpSources" data-throw-if-not-resolved="false"></xref>の確定一覧と出力先の規則（<xref href="Omni.Converter.RadialMaterialConverter.GetOmniOutputPath(System.String)" data-throw-if-not-resolved="false"></xref>）で
決まり、同梱の目録は使いません。生成物が無ければ「まだ生成していない」として解決を断ります
（生成は対数への切替の準備の段が行います）。名前一致だけの推測を行わないため、
同名のユーザーShaderを誤変換しません。

 [OmniShaderGraphInjector](Omni.Converter.OmniShaderGraphInjector.md)

.shadergraph ファイルに <code>RadialKeepObjectPosition</code> Custom Function Node と
camera-relative <code>_RadialGlobal_*</code> schemaを所有範囲内で自動注入・更新します。
VertexDescription はObject座標を保持したままにし、Absolute World → Object の
float round-trip をGraph経路へ作りません。

 [OmniShaderGraphLegacyUpgrader](Omni.Converter.OmniShaderGraphLegacyUpgrader.md)

Shader Graph 10 より前の形式（Master Node の形式。<code>m_SerializedProperties</code> と <code>JSONnodeData</code> を持ち、Target が無い）の Graph を、
Shader Graph の取り込みと同じ方法で今の形式（MultiJson、Target と SubTarget）へ上げます。

<p>
Unity は旧形式の Graph を取り込むたびに、メモリの上だけで今の形式へ上げています（<code>ShaderGraphImporter</code>:
<code>new GraphData { messageManager, assetGuid }</code> → <code>MultiJson.Deserialize</code> → <code>OnEnable</code> → <code>ValidateGraph</code>）。
Omni の注入器は今の形式だけを読むので、注入の前に同じ処理を通し、<code>MultiJson.Serialize</code> で書き出します。
例: URP 同梱の AutodeskInteractive（FBX の取り込みで自動的に割り当てられる）は旧形式です。
</p>
<p>
上げるたびに、Shader Graph は全ての Object へ新しい乱数の Id（<code>m_ObjectId</code>）を振り、書き出す順序もその乱数に引きずられます。
そのため、同じ入力から毎回別のバイト列ができ、生成物の指紋（変換保証）が決まらなくなります。
上げた結果は <xref href="Omni.Converter.OmniShaderGraphLegacyUpgrader.TryCanonicalizeObjectIds(System.String%2cSystem.String%40%2cSystem.String%40)" data-throw-if-not-resolved="false"></xref> で、Id と書き出しの順序を内容だけから決まる形にそろえます。
</p>
<p>Shader Graph の内部の型は C# の反射で使います。見つからない版では理由を返して止めます（Fail Closed）。</p>

 [OmniShaderIncludePaths](Omni.Converter.OmniShaderIncludePaths.md)

ShaderLab／HLSL の <code>#include</code> のパスを扱います。本体のシェーダーは置き場所に依存しないよう、
同じ本体の中の HLSL を含むファイルからの相対パスで include します。本体のシェーダーの本文を別の場所
（例: <code>Assets/Radial/BRG/Shaders</code> の sidecar）へ写すときは、相対パスが解決できなくなるので、
元のファイルの位置を基準にした資産パスへ直してから写します。

 [OmniStandardUrpSources](Omni.Converter.OmniStandardUrpSources.md)

Radial版を作るURP同梱の標準Shaderの確定一覧です。利用者の環境で、対数への切替の準備の段に生成します
（同梱カタログを製造していた頃と同じ変換規則。TerrainLitは4本の閉包）。

 [OmniSwitchActivity](Omni.Converter.OmniSwitchActivity.md)

描画切替の最中に、進捗バーと段階ごとの所要時間を出します。
切替は1回の同期処理で数分かかることがあり、その間ウィンドウは再描画されないため、
固まっていないことを進捗バーで示します。途中までの適用は安全でないため、キャンセルは用意しません。
入れ子の呼び出しは最も外側の <xref href="Omni.Converter.OmniSwitchActivity.Begin(System.String)" data-throw-if-not-resolved="false"></xref> / <xref href="Omni.Converter.OmniSwitchActivity.End" data-throw-if-not-resolved="false"></xref> だけが表示とログを担当します。

 [OmniUrpSubshader](Omni.Converter.OmniUrpSubshader.md)

URPで使われるSubShader（RenderPipelineタグがUniversalPipelineか無し）のPassとタグを読みます。

<p>
Material.passCount／GetPassName／FindPass／GetTag と Shader.passCount は、Shader.globalRenderPipeline に合う
SubShaderを見ます。この値はURPが一度描画するまで空なので、起動直後の自動処理、batchmode、CIでは
代替SubShaderやFallback Shaderの情報になり、URP用のPassやタグが見えません。
</p>

 [OmniMaterialShaderMappingStore.PassState](Omni.Converter.OmniMaterialShaderMappingStore.PassState.md)

 [OmniMaterialShaderSwitchService.Plan](Omni.Converter.OmniMaterialShaderSwitchService.Plan.md)

 [OmniMaterialShaderSwitchService.PlanItem](Omni.Converter.OmniMaterialShaderSwitchService.PlanItem.md)

 [RadialMaterialApplier](Omni.Converter.RadialMaterialApplier.md)

シーン内の永続Materialを事前解析し、参照を維持したままShaderをOmni版へ切り替える、
または永続台帳から元へ戻すEditorツールです。旧生成Materialを参照するSceneの復元も
互換経路として維持します。

 [RadialMaterialConverter](Omni.Converter.RadialMaterialConverter.md)

シーン内のマテリアル・シェーダーを走査し、Radial対応版へ一括変換する Editor ツールです。

<p>
変換後アセットは <code>Assets/Radial/</code> 配下に集約されます。
標準URP Shaderは同梱カタログの検証済みShaderへ差し替えます。
ユーザーShaderGraphは <code>.shadergraph</code> を複製し、
<code>_RadialGlobal_*</code> プロパティを注入します。
</p>

 [RadialMaterialPreparationService](Omni.Converter.RadialMaterialPreparationService.md)

元MaterialからRadial ShaderとRadial Materialを確保する共通Editorサービスです。
Manager UIとScene BRGの双方が同じ生成順序を利用し、検証だけの呼び出しとは分離します。

 [RadialOrphanSourceRestorer](Omni.Converter.RadialOrphanSourceRestorer.md)

元アセットが削除された生成マテリアル（孤児）から、元マテリアルを作り直します。

 [RadialSceneMaterialState](Omni.Converter.RadialSceneMaterialState.md)

シーン内の Renderer / Terrain / DecalProjector を走査して、適用・復元の可否を判断します。

 [RadialSourceResolver](Omni.Converter.RadialSourceResolver.md)

生成マテリアル → 元マテリアルの逆引きです。「いつでも元に戻せる」の土台。

<p>
解決は 3 段で、<b>先勝ち・フォールスルー禁止</b>です。どれも駄目なら null を返し、
呼び出し側が理由を報告できるようにします（黙って別のものを返しません）。
</p>
<ol><li><b>マニフェストの GUID + localId</b> …… 正規経路。リネーム・移動に耐えます</li><li><b>マニフェストの GUID + 名前</b> …… DCC 側で作り直して localId が動いた場合</li><li><b>パス規則からの逆算</b> …… 逆引き未記録（v1 マニフェスト）のエントリの救済のみ</li></ol>
<p>
3 は<b>推測</b>であり、これだけに頼っていたのが従来の弱点でした。
バックフィル（<code>Backfill Source Ids</code>）を一度流せば
ほとんどのエントリが 1 で解決するようになります。
</p>

 [RadialSwitchSceneScope](Omni.Converter.RadialSwitchSceneScope.md)

統合切替（標準／対数）が走査・変更するSceneを一時的に限定します。限定していない間は、
従来どおりロード済みの全Sceneが対象です。ほかのSceneを開いたまま特定のSceneだけを
切り替える検証（Radialの生成物は追跡せず、保存済みSceneは標準状態）で使います。

 [RadialVfxBackend](Omni.Converter.RadialVfxBackend.md)

VFX Graph の Radial 対応の状態を、実際に描画に使われるシェーダーで判定する Editor の窓口です。

<p>
パッチは <xref href="Omni.Converter.RadialVfxImportHook" data-throw-if-not-resolved="false"></xref> が取り込みのたびに、全ての VFX の表示用シェーダーへ当てます
（VFX Graph 17.6 では、以前の外部化した .vfxshader と manifest の方式は使われていませんでした）。
この窓口は、フックが入っていることと、各 VFX 資産の描画シェーダーがパッチの目印（<xref href="Omni.Converter.RadialVfxShaderPatcher.SentinelProperty" data-throw-if-not-resolved="false"></xref>）を
公開していることを確かめます。パッチ無しのシェーダーは Unity が Properties を公開しないので、目印の有無で判別できます。
古い（パッチ前に取り込まれた）資産は <xref href="Omni.Converter.RadialVfxBackend.GenerateForLoadedScenes(System.String%40)" data-throw-if-not-resolved="false"></xref> / <xref href="Omni.Converter.RadialVfxBackend.GenerateForAssetPaths(System.Collections.Generic.IEnumerable%7bSystem.String%7d%2cSystem.String%40)" data-throw-if-not-resolved="false"></xref>
で取り込み直します。待機中に自動で取り込み直すのは、使う VFX（<xref href="Omni.Converter.RadialVfxUsage" data-throw-if-not-resolved="false"></xref>）だけです
（<xref href="Omni.Converter.RadialVfxAssetPostprocessor" data-throw-if-not-resolved="false"></xref>）。
</p>

 [RadialVfxImportHook](Omni.Converter.RadialVfxImportHook.md)

VFX Graph の取り込みで生成される表示用シェーダーへ、取り込みのたびに Radial のパッチ（<xref href="Omni.Converter.RadialVfxShaderPatcher" data-throw-if-not-resolved="false"></xref>）を当てます。

<p>
VFX Graph 17.6 は、ネイティブの取り込み処理から <code>VisualEffectResource.onCompileResource</code>（グラフを編集中は
<code>onEarlyGetAuthoringCompileData</code>）を呼び、グラフから生成したシェーダーのソースを <code>VisualEffectAssetDesc.shaderSourceDesc</code>
で直接返します。外部化したシェーダーのファイルを読み戻す仕組みは無く、以前の「外部化の設定を有効にして取り込み直す」方式では
パッチ済みのシェーダーが使われていませんでした（2026-10-04 に確認）。そこで、この2つのコールバックを包み、返るソースに
その場でパッチを当てます。生成物のファイルは作りません。
</p>
<p>
コールバックは internal なので、リフレクションと式木で包みます（C# のデリゲートを差し替えるだけで、ネイティブの関数は呼びません）。
見つからない版では <xref href="Omni.Converter.RadialVfxImportHook.Fault" data-throw-if-not-resolved="false"></xref> に理由を残し、<xref href="Omni.Converter.RadialVfxBackend" data-throw-if-not-resolved="false"></xref> が Faulted として報告します（Fail Closed）。
注入シェーダー（<xref href="Omni.Converter.RadialVfxImportHook.InjectDirectory" data-throw-if-not-resolved="false"></xref> の HLSL）と patcher の版から作る custom dependency を全ての VFX の取り込みに登録するので、
どちらかを変えると、全ての VFX が取り込み直されます。
</p>

 [RadialVfxShaderPatcher](Omni.Converter.RadialVfxShaderPatcher.md)

外部化VFX presentation shaderへRadial描画フックを冪等注入します。

 [UnityAssetPathResolver](Omni.Converter.UnityAssetPathResolver.md)

Unity の論理アセットパスを、ファイル API で使える実体パスへ解決します。

<p>
Registry / built-in package はプロジェクト直下の <code>Packages/</code> に実ファイルを
持たず、<code>Library/PackageCache</code> に実体が置かれます。ハッシュ付き cache 名を
推測せず、<xref href="UnityEditor.PackageManager.PackageInfo.resolvedPath" data-throw-if-not-resolved="false"></xref> を使います。
</p>

 [VfxGraphAuthoring](Omni.Converter.VfxGraphAuthoring.md)

VFX Graph の資産（<code>.vfx</code>）を、コードから空の状態で組み立て直します（Editor 専用）。

<p>
流れ: 空のグラフの YAML を書く → 取り込む → グラフを空にする → <xref href="Omni.Converter.VfxGraphBuilder" data-throw-if-not-resolved="false"></xref> で組む → 書き出す → 取り込み直す。
既存の <code>.vfx</code> は <code>.meta</code>（GUID）を保ったまま上書きするので、Scene や Profile の参照は変わりません。
取り込みのたびに <xref href="Omni.Converter.RadialVfxImportHook" data-throw-if-not-resolved="false"></xref> が表示用シェーダーへ Radial のパッチを当てます。
</p>
<p>
VFX Graph の編集 API は internal なので反射で使います。型やメンバーが見つからない版では、組み立てを始める前に
<xref href="Omni.Converter.VfxGraphAuthoring.CheckEnvironment(System.String%40)" data-throw-if-not-resolved="false"></xref> が理由を返し、<xref href="Omni.Converter.VfxGraphAuthoring.Author(System.String%2cSystem.Action%7bOmni.Converter.VfxGraphBuilder%7d%2cSystem.Boolean)" data-throw-if-not-resolved="false"></xref> は例外で止めます（途中まで作った資産を残しません）。
組み立ての途中で設定名や slot が見つからないときも、名前と候補を含む例外で止めます。
</p>

 [VfxGraphBuilder](Omni.Converter.VfxGraphBuilder.md)

VFX Graph のグラフを組み立てる薄い層です（<xref href="Omni.Converter.VfxGraphAuthoring.Author(System.String%2cSystem.Action%7bOmni.Converter.VfxGraphBuilder%7d%2cSystem.Boolean)" data-throw-if-not-resolved="false"></xref> が渡します）。
Context・Block・Operator・公開パラメーターを型名と設定名で作り、slot を名前で繋ぎます。
返す値は VFX Graph の internal のモデルなので、このクラスのメソッドにだけ渡してください。
型・設定・slot が見つからないときは、名前と候補を含む例外で止めます。

### 構造体（Structs）

 [RadialSourceResolver.BackfillResult](Omni.Converter.RadialSourceResolver.BackfillResult.md)

マニフェストの逆引き情報（v2 で追加）が空のエントリを、パス規則から埋めます。
埋まらないものは<b>空のまま残し、削除も再生成強制もしません</b>。

 [OmniSceneRadialClassification](Omni.Converter.OmniSceneRadialClassification.md)

Scene 1つの判定と、その理由です。

 [RadialVfxShaderPatcher.PatchResult](Omni.Converter.RadialVfxShaderPatcher.PatchResult.md)

 [RadialOrphanSourceRestorer.Plan](Omni.Converter.RadialOrphanSourceRestorer.Plan.md)

1件分の復元計画です。

 [RadialSceneState](Omni.Converter.RadialSceneState.md)

シーンの「Radial マテリアル適用状態」を<b>シーンの実データから</b>数えた結果です。

<p>
以前は UI 側の非シリアライズ bool 1 個で適用状態を覚えていたため、
ドメインリロードのたびに「元に戻す」ボタンが押せなくなり、
同時に一覧も 0 件になって「放射マテリアル」も押せない、という詰みが起きていました。
状態は毎回シーンから数え直すこと。覚えないのが正解です。
</p>

 [RadialVfxSceneState](Omni.Converter.RadialVfxSceneState.md)

 [OmniMaterialShaderSwitchService.Result](Omni.Converter.OmniMaterialShaderSwitchService.Result.md)

 [OmniRadialOutputMigration.Result](Omni.Converter.OmniRadialOutputMigration.Result.md)

移行の結果です。

 [RadialSceneMaterialState.RevertResult](Omni.Converter.RadialSceneMaterialState.RevertResult.md)

 [OmniGuidManifest.SaveResult](Omni.Converter.OmniGuidManifest.SaveResult.md)

### インターフェース（Interfaces）

 [IOmniExternalMaterialSource](Omni.Converter.IOmniExternalMaterialSource.md)

ロード済みSceneのRenderer・Terrain・Decal Projectorからは見えない永続Materialを供給します。
閉じたSubSceneの依存Materialや、実行時にコードでEntityを作る所有者のMaterialが当たります。
供給元は<code>Register</code>で登録します（Converterは供給元のassemblyを参照しません）。

### 列挙型（Enums）

 [OmniSceneRadialUsage](Omni.Converter.OmniSceneRadialUsage.md)

Scene 1つが対数（Radial）レンダリングを使うかの判定です。

 [RadialSourceResolver.PathRuleSourceProbe](Omni.Converter.RadialSourceResolver.PathRuleSourceProbe.md)

パス規則で元アセットを探した結果です。

 [RadialVfxBackendState](Omni.Converter.RadialVfxBackendState.md)

 [OmniMaterialShaderSwitchService.ReferenceScope](Omni.Converter.OmniMaterialShaderSwitchService.ReferenceScope.md)

 [OmniGuidManifest.SaveFailureKind](Omni.Converter.OmniGuidManifest.SaveFailureKind.md)

 [OmniGuidManifest.SaveIntent](Omni.Converter.OmniGuidManifest.SaveIntent.md)

 [OmniGuidManifest.SaveStatus](Omni.Converter.OmniGuidManifest.SaveStatus.md)

 [OmniRadialGraphWarningAcknowledgements.State](Omni.Converter.OmniRadialGraphWarningAcknowledgements.State.md)

Graph の確認済みの状態です。

 [OmniCustomShaderConversionConfirmations.State](Omni.Converter.OmniCustomShaderConversionConfirmations.State.md)

確認済みの状態です。
