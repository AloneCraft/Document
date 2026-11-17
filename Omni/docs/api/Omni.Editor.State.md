# <a id="Omni_Editor_State"></a> Namespace Omni.Editor.State

### クラス（Classes）

 [OmniViewState](Omni.Editor.State.OmniViewState.md)

1つのScene Viewに属する表示状態です。RadialCamera選択と探索モードは
Scene ViewのEntity IDごとにEditor Sessionへ保存します。

 [OmniViewStateRegistry](Omni.Editor.State.OmniViewStateRegistry.md)

Scene ViewごとのOmni表示状態を管理します。
InstanceIDと弱参照を使用し、破棄済みEditorオブジェクトを保持しません。

### 列挙型（Enums）

 [OmniMeshDisplayMode](Omni.Editor.State.OmniMeshDisplayMode.md)

Standard/Radial 比較表示の表示方式です。

 [OrthoLogGridDataType](Omni.Editor.State.OrthoLogGridDataType.md)

Orthographic対数グリッド（<xref href="Omni.Editor.State.OmniViewState.OrthoLogGridEnabled" data-throw-if-not-resolved="false"></xref>）の画面端が
どのデータ型の表現可能な最大値・最小値に対応するかを選びます（ScaleView_Plan Q節）。

 [SceneViewWarpMode](Omni.Editor.State.SceneViewWarpMode.md)

「基準カメラ」がScene Viewカメラ自身のときに、対数ワープを掛けるかどうかです。
