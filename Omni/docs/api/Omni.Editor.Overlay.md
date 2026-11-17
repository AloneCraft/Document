# <a id="Omni_Editor_Overlay"></a> Namespace Omni.Editor.Overlay

### クラス（Classes）

 [OmniDebugOverlay](Omni.Editor.Overlay.OmniDebugOverlay.md)

有限描画プロキシの状態をScene View単位で確認・上書きする、セッション限定の診断パネルです。

 [OmniManagerOverlayBridge](Omni.Editor.Overlay.OmniManagerOverlayBridge.md)

Scene View の Omni Navigator と Omni Manager ウィンドウの表示状態を仲介します。
アセンブリ循環を避けるため、Manager はウィンドウを登録し、Navigator はこの橋渡しを呼び出します。

 [OmniSceneOverlay](Omni.Editor.Overlay.OmniSceneOverlay.md)

各Scene ViewへOmniの簡易操作を追加するUI Toolkit Overlayです。

<p>
Scene Viewの投影方式（Perspective / Orthographic）に応じて中身を丸ごと切り替えます。
Perspectiveは既存のRadial（3D放射対数）操作一式、Orthographicは
Editor専用の2D対数グリッド表示（<code>Omni.Editor.SceneViewOrtho.OrthoLogGridRenderer</code>）の
トグルだけです。両者は独立した機能で、パラメータを共有しません。
</p>
<p>
ScaleSpaceプロジェクトの同名オーバーレイを移植したものです。
Standard/Radial比較描画は System A（GPU頂点ワープ）のみ移植済みで、実体は
<xref href="Omni.Logical.LinearReferenceMeshRenderer" data-throw-if-not-resolved="false"></xref> にあります。ここはその表示モードを
切り替えるUIだけを持ちます。
</p>
<p>
座標編集とナビゲーションはLogical座標を正本とし、Unityの単精度値は描画・GUI境界でのみ使います。
</p>

 [OmniSettingsOverlay](Omni.Editor.Overlay.OmniSettingsOverlay.md)

たまにしか触らない設定をまとめたScene View パネルです。

<p>
常時表示の「Omni Navigator」（座標・角度・Nav状態など操作系）、読み取り専用の
「Omni Debug」（診断系）とは役割を分け、こちらは対話的なコントロールだけを持ちます。
カリング診断はDebugへ戻し、通常設定だけをこちらへ残します。
描画経路（物体の元Renderer／有限描画プロキシの切替）は常にAuto固定で、設定欄はありません。
</p>
