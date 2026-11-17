# <a id="Omni_Rendering"></a> Namespace Omni.Rendering

### 名前空間（Namespaces）

 [Omni.Rendering.Radial](Omni.Rendering.Radial.md)

### クラス（Classes）

 [OmniMotionBlur](Omni.Rendering.OmniMotionBlur.md)

奥行きを見るモーションブラーの Volume 設定(<xref href="Omni.Rendering.OmniMotionBlurFeature" data-throw-if-not-resolved="false"></xref> が読む)。
URP の <xref href="UnityEngine.Rendering.Universal.MotionBlur" data-throw-if-not-resolved="false"></xref> は手前と奥を区別せずに混ぜるため、速く流れる背景がほとんど動かない手前の物の色を拾い、縁の外へもやが出る。
これを使う Volume では、URP の Motion Blur を併用しない(二重にぼかさない)。強さ・上限・品質の意味は URP の Motion Blur と同じ。

 [OmniMotionBlurFeature](Omni.Rendering.OmniMotionBlurFeature.md)

奥行きを見るモーションブラー(<xref href="Omni.Rendering.OmniMotionBlur" data-throw-if-not-resolved="false"></xref> の Volume 設定が有効なカメラだけ)。
ポストエフェクトの前に、付けたマテリアル(Fullscreen の Shader Graph、URP 標準の深度の書き方)を 1 回の全画面処理で描く。
Graph へは、元の色を _BlitTexture、動きを _MotionVectorTexture、深度を _CameraDepthTexture、強さ・上限・標本数を _BlurSettings で渡す。
Radial のときは、Omni の切り替え(Renderer Feature が持つマテリアルも対象)が変換した Graph へ差し替える。
マテリアルが無いときは何もしない。URP の Motion Blur と同じく Game の Camera だけで働く。
