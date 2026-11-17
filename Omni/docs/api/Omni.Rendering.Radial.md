# <a id="Omni_Rendering_Radial"></a> Namespace Omni.Rendering.Radial

### クラス（Classes）

 [BakeData](Omni.Rendering.Radial.BakeData.md)

### 構造体（Structs）

 [Aabb](Omni.Rendering.Radial.Aabb.md)

Logical AABBをUnityシリアライザで保持するためのラッパーです。

 [BakeEntry](Omni.Rendering.Radial.BakeEntry.md)

Rendererごとのカメラ非依存ベイク結果です。

 [DrawTransform](Omni.Rendering.Radial.DrawTransform.md)

1台のRadialカメラから見た、1オブジェクトの一時的な表示変換です。
Componentではなく、Scene/Prefabへシリアライズされません。

 [FarFieldGroup](Omni.Rendering.Radial.FarFieldGroup.md)

空間的に近接する静的遠景Rendererのグループです。

 [Frustum](Omni.Rendering.Radial.Frustum.md)

Logical座標系で解釈するカメラ錐台です。巨大な絶対float座標を使わず、
<xref href="Omni.Rendering.Radial.Frustum.Origin" data-throw-if-not-resolved="false"></xref>と方向・投影値だけでBRGの安全な入力を表します。
SaturnシーンのMesoリングセル判定で使用します。

 [GpuFrame](Omni.Rendering.Radial.GpuFrame.md)

BRG専用シェーダーとCPUカリングが共有する、カメラ相対Radial GPU frameです。
この値は<xref href="UnityEngine.Shader.SetGlobalFloat(System.Int32%2cSystem.Single)" data-throw-if-not-resolved="false"></xref>から再取得せず、
<xref href="Omni.Rendering.Radial.ViewSnapshot" data-throw-if-not-resolved="false"></xref>を経由してカメラ別に受け渡します。
SaturnシーンのMesoリングBRG描画で使用します。

 [Position3](Omni.Rendering.Radial.Position3.md)

Logical位置をUnityシリアライザで保持するためのラッパーです。

 [Vector3](Omni.Rendering.Radial.Vector3.md)

Logical差分ベクトルをUnityシリアライザで保持するためのラッパーです。

 [ViewSnapshot](Omni.Rendering.Radial.ViewSnapshot.md)

1回のカメラ描画に対応する不変Radialビュー状態です。
BRGは<xref href="Omni.RadialViewRegistry" data-throw-if-not-resolved="false"></xref>からこの値を取得し、Shader.SetGlobal*を
正本として参照しません。SaturnシーンのMesoリングBRG描画で使用します。

### 列挙型（Enums）

 [BakeTier](Omni.Rendering.Radial.BakeTier.md)

距離帯の分類です。

 [ViewKind](Omni.Rendering.Radial.ViewKind.md)

Radial描画のビュー種別です。SaturnのBRG v1は<xref href="Omni.Rendering.Radial.ViewKind.Camera" data-throw-if-not-resolved="false"></xref>だけを描画対象にし、
それ以外はカリングを省略するfail-open経路へ渡します。
