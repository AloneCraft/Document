# <a id="Omni_Editor_Manager"></a> Namespace Omni.Editor.Manager

### 名前空間（Namespaces）

 [Omni.Editor.Manager.AiConversion](Omni.Editor.Manager.AiConversion.md)

### クラス（Classes）

 [BakeTab](Omni.Editor.Manager.BakeTab.md)

Radial ベイク（<xref href="Omni.Editor.Manager.RadialBaker" data-throw-if-not-resolved="false"></xref>）を実行し、現在のシーンのベイク状態を表示するタブです。

 [RadialOrphanGeneratedAssetSweeper.Item](Omni.Editor.Manager.RadialOrphanGeneratedAssetSweeper.Item.md)

 [MaterialEntry](Omni.Editor.Manager.MaterialEntry.md)

1つの実Materialアセットに対応するスキャン結果です。

 [MaterialScanExclusion](Omni.Editor.Manager.MaterialScanExclusion.md)

Project走査から除外した読取専用または埋込みMaterialです。

 [MaterialsTab](Omni.Editor.Manager.MaterialsTab.md)

Materialタブは切替対象の診断と対応関係を表示します。
生成・適用・復元は上部の標準／対数統合切替だけが行います。

 [OmniCameraScanner](Omni.Editor.Manager.OmniCameraScanner.md)

シーン内カメラのスキャンと診断を行うクラスです。

 [OmniFullPass](Omni.Editor.Manager.OmniFullPass.md)

TerminalSceneを対象に、生成・配線・マテリアル適用・保存・描画確認までを一括実行します。

 [OmniIssue](Omni.Editor.Manager.OmniIssue.md)

Omni Manager が検出した単一の問題を表します。

 [OmniManagerUserSettings](Omni.Editor.Manager.OmniManagerUserSettings.md)

Omni Manager のユーザー個別設定です。EditorPrefs に保存されます。

 [OmniManagerWindow](Omni.Editor.Manager.OmniManagerWindow.md)

Omni プロジェクト全体を管理する統合 Editor ウィンドウです。

<p>
マテリアルの Radial 変換・シーン適用・復元・検証を一箇所で行えます。
従来の <code>Converter</code> メニュー群を統合した UI です。
</p>

 [OmniMaterialGenerator](Omni.Editor.Manager.OmniMaterialGenerator.md)

Omni マテリアルの生成を管理します。<xref href="Omni.Converter.RadialMaterialConverter" data-throw-if-not-resolved="false"></xref> のラッパーです。

 [OmniMaterialReplacer](Omni.Editor.Manager.OmniMaterialReplacer.md)

シーン内MaterialのShader切替・復元を管理します。<xref href="Omni.Converter.RadialMaterialApplier" data-throw-if-not-resolved="false"></xref> のラッパーです。

 [OmniMaterialScanner](Omni.Editor.Manager.OmniMaterialScanner.md)

Projectまたは全ロード済みSceneから、実Materialアセット単位の共通解析結果を作ります。
GUI描画中には呼ばず、Managerの遅延更新からのみ実行します。

 [OmniProductDemo](Omni.Editor.Manager.OmniProductDemo.md)

製品デモ(Build Settingsの先頭に置くScene)です。2026-09-25のユーザー判断で、受入(P11 WebGPU、P12 DX12)を通った
Earth to Moon 2へ切り替え、2026-09-30に旧Earth to Moonを削除して、EarthToMoonの名前へ改めました。

 [OmniRegenerateAll](Omni.Editor.Manager.OmniRegenerateAll.md)

プロジェクト全体（Assets/ 配下の全シーン・全マテリアル）を対象に、
Omni ラッパーシェーダー／マテリアルを再生成します。
RadialInject.hlsl の CBUFFER 配置修正など、生成テンプレート側の変更を
既存の生成済みアセットへ反映するために使います。

 [OmniRenderingModeAutoApply](Omni.Editor.Manager.OmniRenderingModeAutoApply.md)

対数が記録されている間、Editorで開いたSceneのCameraへ <xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref> を付けて有効にします。

<p>
Undoへ記録せず、Sceneを未保存（dirty）にもしません。開くたびに保存を求めないためと、
未保存のSceneがあるとテストが始まらないためです。PlayとPlayer Buildでは
<xref href="Omni.Editor.Manager.OmniRenderingModeSceneProcessor" data-throw-if-not-resolved="false"></xref> が毎回付け直すので、保存されなくても困りません。
</p>
<p>
付けるのはMaterialが対数のSceneだけです（<xref href="Omni.Editor.Manager.OmniCameraScanner.IsSceneMaterialsRadial(UnityEngine.SceneManagement.Scene)" data-throw-if-not-resolved="false"></xref>）。
標準のMaterialのSceneは標準のまま表示します。
自動で付けた分はSceneファイルへ保存しません。新しく付けたComponentは
<xref href="UnityEngine.HideFlags.DontSaveInEditor" data-throw-if-not-resolved="false"></xref> にし、保存済みの無効なRadialCameraを有効にした分は
保存の直前に無効へ戻して保存後に有効へ戻します。Omni自身がScene参照を書き換えて保存するとき
（Project範囲の切替）に、自動付与まで書き込まれて標準へ戻しても残る不具合がありました。
記録が対数でなくなったら、自動で付けた分を外します。
</p>

 [OmniRenderingModeSettings](Omni.Editor.Manager.OmniRenderingModeSettings.md)

統合切替で選んだ描画方式（対数／標準）をプロジェクトに記録します。

<p>
Cameraへの <xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref> 付与はSceneの変更なので、保存しないまま開き直す、
別のSceneを開く、Player Buildする、のいずれでも失われます。対数を選んだ記録を残し、
Sceneを開いたとき、Playを始めたとき、Player Buildのときに付け直します
（<xref href="Omni.Editor.Manager.OmniRenderingModeAutoApply" data-throw-if-not-resolved="false"></xref>、<xref href="Omni.Editor.Manager.OmniRenderingModeSceneProcessor" data-throw-if-not-resolved="false"></xref>）。
</p>
<p>
標準は自動で外しません。RadialCameraを有効にして保存したデモSceneを壊さないためです。
記録が無いとき（未設定）も何もしません。
</p>

 [OmniRepairDanglingMaterials](Omni.Editor.Manager.OmniRepairDanglingMaterials.md)

シーン内の壊れたマテリアル参照（PrefabInstanceのオーバーライドが実体の無いGUIDを
指しているケース）を、プレハブ本来のデフォルトマテリアルへ安全に戻します。

<p>
2026-08-01、<code>Assets/Radial/</code> を削除して再生成した際にGUIDが変わり、
TerminalScene.unity の "Center Floor Trim" 等、約20オブジェクト・約120箇所の
マテリアル参照が永久にダングリングした事故の復旧手段として用意した。
</p>
<p>
<xref href="UnityEditor.PrefabUtility.RevertPropertyOverride(UnityEditor.SerializedProperty%2cUnityEditor.InteractionMode)" data-throw-if-not-resolved="false"></xref> は使いません。多段ネストした
プレハブ（内側のプレハブ自身の既定値と外側のプレハブインスタンス側のオーバーライドが
別々の階層に記録されている場合）では、処理対象ではない兄弟インスタンスのスロットを
巻き添えで空にすることが実際に確認されています（詳細は
<xref href="Omni.Converter.RadialSceneMaterialState.Revert(System.Boolean)" data-throw-if-not-resolved="false"></xref> 直下のコメント参照）。同じ理由で
本クラスも <xref href="UnityEditor.PrefabUtility.GetCorrespondingObjectFromSource%60%601(%60%600)" data-throw-if-not-resolved="false"></xref> でプレハブ側の
実効デフォルト値を読み、<xref href="UnityEngine.Renderer.sharedMaterials" data-throw-if-not-resolved="false"></xref> への通常の配列代入で
書き戻します。
</p>

 [OmniSceneScanner](Omni.Editor.Manager.OmniSceneScanner.md)

シーン全体の Omni 関連情報を収集します。

 [OmniShaderDiagnosticWindow](Omni.Editor.Manager.OmniShaderDiagnosticWindow.md)

選択Shaderの診断、オフライン文書、AI修正promptを一つの画面にまとめます。

 [OmniShaderErrorChecker](Omni.Editor.Manager.OmniShaderErrorChecker.md)

<code>Assets/Radial/</code> 配下の生成シェーダーを走査し、コンパイルエラーを検出します。

<p>
生成物が壊れたときの最も分かりやすい症状は「マテリアルがマゼンタになる」ことですが、
変換対象が SRP パッケージ全体（URP だけで 20 シェーダー）に広がると、
4 シーンを目視で確認する運用では取りこぼします。ここでコード側から確実に検出します。
</p>
<p>
逆に「コンパイルは通るがレンダーステートが欠落して静かに見た目が壊れる」類の破綻は
原理的にここでは検出できません。それは <xref href="Omni.Editor.Manager.OmniShaderGenerator" data-throw-if-not-resolved="false"></xref> が
原文を複製する方式を採ることで、そもそも発生させない設計になっています。
</p>

 [OmniShaderGenerator](Omni.Editor.Manager.OmniShaderGenerator.md)

元シェーダーを<b>そのまま複製し、テキストで最小限だけパッチ</b>して Radial 対応版を生成します。

<p>
さらに昔の実装は HLSL ブロックを正規表現で抽出して別ファイルへ出し、シェーダー本体を
組み立て直していました。その方式は <code>Blend [_SrcBlend][_DstBlend]</code> のような SubShader
レベルのレンダーステート、Pass の <code>Name</code> / <code>LightMode</code> タグ、相対 include を
落としてしまい、生成物が壊れます。複製＋パッチなら原文の構造がそのまま残るため、
これらの取りこぼしが原理的に発生しません。
</p>
<p>
パッチの当て方は<b>正規表現から構文解析へ移行済み</b>です。ShaderLab の構造は
<xref href="Omni.Editor.Manager.ShaderLab.ShaderLabParser" data-throw-if-not-resolved="false"></xref> が、頂点フックの挿入位置は
<xref href="Omni.Editor.Manager.Hlsl.HlslIncludeGraph" data-throw-if-not-resolved="false"></xref> が決めます。
なぜ HLSL パーサーを導入しないのか、その前提が崩れる条件、対応できないシェーダーが
出たときの手順は <xref href="Omni.Editor.Manager.Radial.OmniShaderPatcher" data-throw-if-not-resolved="false"></xref> の冒頭コメントにまとめてあります。
<b>ここに正規表現を足して個別対応しないでください。</b>
</p>

 [OmniShaderScanner](Omni.Editor.Manager.OmniShaderScanner.md)

 [OmniTerrainShaderClosureGenerator](Omni.Editor.Manager.OmniTerrainShaderClosureGenerator.md)

URP TerrainLit と、その Add/Base/Basemap・Scene View 選択参照を一括生成します。

<p>
これは <xref href="Omni.Editor.Manager.OmniShaderGenerator" data-throw-if-not-resolved="false"></xref> の通常入口とは分けています。通常入口は Hidden
Shader を拒否する安全契約を持つため、Terrain の依存閉包だけを明示的に許可する方が
ポストプロセスなど全 Hidden Shader を誤変換するより安全です。
</p>
<p>
Galaxy を含む Runtime Scene では直接使いません。Omni Manager の Shader 生成と、
Terrain Material を置換する直前の Editor 経路から呼び出します。
</p>

 [OmniTmpUrpMaterialMigration](Omni.Editor.Manager.OmniTmpUrpMaterialMigration.md)

既存TMP MaterialをGUIDを維持したまま公式URP原本へ移行し、Omni Managerの
共通経路でRadial版を生成します。GUID参照のため全Scene/Prefabへ一括波及し、
Active Sceneでは表示モードに依存せず、BRG Manifestが解決できるURP
Authoring正本へ即時同期します。Radial生成物はsidecarとして使用します。

 [OmniValidator](Omni.Editor.Manager.OmniValidator.md)

プロジェクトとシーンの Omni 関連問題を検出します。

 [RadialOrphanGeneratedAssetSweeper.Plan](Omni.Editor.Manager.RadialOrphanGeneratedAssetSweeper.Plan.md)

 [ProjectMaterialScanResult](Omni.Editor.Manager.ProjectMaterialScanResult.md)

書換え可能なProject Materialと、除外理由を分離した走査結果です。

 [RadialBaker](Omni.Editor.Manager.RadialBaker.md)

Radial ワープのカメラ非依存な静的データ（<xref href="Omni.Rendering.Radial.BakeData" data-throw-if-not-resolved="false"></xref>）を生成する
Editor ツールです。運用感は Unity の Lightmap ベイクに準じます
（明示実行 → ディスクへアセット保存 → シーン/ワープ設定の変更で再ベイクが要る）。

<p>
ここでベイクするのはカメラ非依存の静的な材料だけです。ワープ後の座標そのものは
保存しません（カメラは毎フレーム動くため、保存してもカメラが動いた瞬間に無効になります）。
</p>

 [RadialOrphanGeneratedAssetSweeper](Omni.Editor.Manager.RadialOrphanGeneratedAssetSweeper.md)

元のShader／Materialが消えた <code>Assets/Radial</code> の生成物（孤児）を、対数レンダリングへの
切替完了後にOSのごみ箱へ移します。

 [RadialRenderingSwitch](Omni.Editor.Manager.RadialRenderingSwitch.md)

「Unityレンダリング / Radialレンダリング」の統合切替です。

<p>
マテリアル設定・シェーダー設定・ベイク設定・カメラへの <xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref> 付与は、
「Radial で見るか Unity 標準で見るか」という 1 つの意思決定の各側面であり、個別に
操作する意味がありません（シェーダー生成はマテリアル生成が内部で自動的に呼ぶため、
独立項目にする意味自体が無い）。このクラスが単一の入口になります。
</p>
<p>
マテリアル部分の実行エンジンは <xref href="Omni.Converter.RadialMaterialApplier" data-throw-if-not-resolved="false"></xref> /
<xref href="Omni.Converter.RadialSceneMaterialState" data-throw-if-not-resolved="false"></xref>（前段で作った、シーン実データから毎回状態を
数え直す仕組み）をそのまま再利用します。ここで新たに持つ状態はありません。
</p>

 [RadialOrphanGeneratedAssetSweeper.Result](Omni.Editor.Manager.RadialOrphanGeneratedAssetSweeper.Result.md)

 [SceneBrgTab](Omni.Editor.Manager.SceneBrgTab.md)

ロード済みSceneのScene BRG sidecar準備状態を表示し、利用者が再確認・再生成を
要求するタブです。生成は <xref href="Omni.Editor.BatchRendering.RadialSceneBrgEditorIntegration" data-throw-if-not-resolved="false"></xref> が次の安全な
Editor更新で行い、このタブのOnGUIは結果を読むだけです。

 [ShaderEntry](Omni.Editor.Manager.ShaderEntry.md)

 [ShadersTab](Omni.Editor.Manager.ShadersTab.md)

 [TerrainShaderClosureResult](Omni.Editor.Manager.TerrainShaderClosureResult.md)

TerrainLit の依存 Shader 閉包を生成した結果です。

<p>
この型は Editor 専用です。Runtime の Terrain や Material を変更せず、呼び出し側が
<xref href="Omni.Editor.Manager.TerrainShaderClosureResult.IsReady" data-throw-if-not-resolved="false"></xref> を確認してから置換をコミットするための診断値だけを返します。
</p>

### 構造体（Structs）

 [MaterialRenderingComposition](Omni.Editor.Manager.MaterialRenderingComposition.md)

選択範囲内の一意なMaterialへ現在設定されているShaderの構成です。
Camera、VFX、Renderer準備状態は切替検証の責務であり、この表示状態へ混ぜません。

 [RadialRenderingSwitch.RadialRenderingSwitchResult](Omni.Editor.Manager.RadialRenderingSwitch.RadialRenderingSwitchResult.md)

 [OmniSceneScanner.SceneSummary](Omni.Editor.Manager.OmniSceneScanner.SceneSummary.md)

シーンスキャン結果のサマリーです。

 [OmniShaderErrorChecker.ShaderError](Omni.Editor.Manager.OmniShaderErrorChecker.ShaderError.md)

1 シェーダー分の検出結果です。

 [RadialRenderingSwitch.State](Omni.Editor.Manager.RadialRenderingSwitch.State.md)

ラジオボタンの表示状態です。

### インターフェース（Interfaces）

 [IOmniManagerTab](Omni.Editor.Manager.IOmniManagerTab.md)

Omni Manager のタブが実装すべきインターフェースです。
新規タブを追加するときはこれを実装し、<code>OmniManagerWindow.s_Tabs</code> に追加してください。

### 列挙型（Enums）

 [RadialOrphanGeneratedAssetSweeper.Decision](Omni.Editor.Manager.RadialOrphanGeneratedAssetSweeper.Decision.md)

 [RadialRenderingSwitch.FailureStage](Omni.Editor.Manager.RadialRenderingSwitch.FailureStage.md)

 [IssueCategory](Omni.Editor.Manager.IssueCategory.md)

問題のカテゴリです。

 [IssueSeverity](Omni.Editor.Manager.IssueSeverity.md)

問題の重大度です。

 [RadialOrphanGeneratedAssetSweeper.Kind](Omni.Editor.Manager.RadialOrphanGeneratedAssetSweeper.Kind.md)

 [MaterialScanScope](Omni.Editor.Manager.MaterialScanScope.md)

Omni Manager上部のMaterial切替で使用する走査範囲です。

 [MaterialShaderUsageKind](Omni.Editor.Manager.MaterialShaderUsageKind.md)

現在Materialへ割り当てられているShaderの区分です。

 [MaterialStatus](Omni.Editor.Manager.MaterialStatus.md)

旧UIとの互換性を保つMaterial生成状態です。

 [RadialBakeStaleReason](Omni.Editor.Manager.RadialBakeStaleReason.md)

<xref href="Omni.Editor.Manager.RadialBaker.IsBakeStale(UnityEngine.SceneManagement.Scene%2cOmni.RadialCamera%2cOmni.Editor.Manager.RadialBakeStaleReason%40%2cSystem.String%40)" data-throw-if-not-resolved="false"></xref>が返す陳腐化理由の分類です。
表示文言（多言語対応）とは切り離し、呼び出し側が文字列内容に依存せず分岐できるようにします。

 [RadialVersionState](Omni.Editor.Manager.RadialVersionState.md)

現在Materialに対する対数版Shaderの状態です。

 [OmniRenderingModeSettings.RenderingMode](Omni.Editor.Manager.OmniRenderingModeSettings.RenderingMode.md)

 [RadialRenderingSwitch.RenderingMode](Omni.Editor.Manager.RadialRenderingSwitch.RenderingMode.md)

 [ShaderKind](Omni.Editor.Manager.ShaderKind.md)

 [ShaderStatus](Omni.Editor.Manager.ShaderStatus.md)

 [RadialRenderingSwitch.SwitchOutcome](Omni.Editor.Manager.RadialRenderingSwitch.SwitchOutcome.md)

 [TerrainShaderClosureStatus](Omni.Editor.Manager.TerrainShaderClosureStatus.md)

Terrain Shader 依存閉包の失敗理由です。
