# <a id="VirtualizedGeometry_Editor"></a> Namespace VirtualizedGeometry.Editor

### クラス（Classes）

 [MeshOptimizerSimplifier](VirtualizedGeometry.Editor.MeshOptimizerSimplifier.md)

meshoptimizer v1.1を決定的なEditor変換だけに使用する薄い境界。

 [VirtualGeometryBuildInclusion](VirtualizedGeometry.Editor.VirtualGeometryBuildInclusion.md)

Playerへ収録するarchive集合とEditor専用native依存の禁止境界。

 [VirtualGeometryBuildOutput](VirtualizedGeometry.Editor.VirtualGeometryBuildOutput.md)

 [VirtualGeometryBuildSettings](VirtualizedGeometry.Editor.VirtualGeometryBuildSettings.md)

クラスタ化、共通位置量子化、境界保持階層を制御する変換設定。

 [VirtualGeometryBuilder](VirtualizedGeometry.Editor.VirtualGeometryBuilder.md)

入力を検査し、共有頂点を維持したクラスタと原子的な境界保持LOD階層へ変換する。

 [VirtualGeometryMeshInput](VirtualizedGeometry.Editor.VirtualGeometryMeshInput.md)

Meshから抽出した、Unityオブジェクト寿命に依存しない変換入力。

 [VirtualGeometryProxyBuilder](VirtualizedGeometry.Editor.VirtualGeometryProxyBuilder.md)

fallback/影/物理/選択用の低密度Meshを階層から生成し、元Mesh参照を残さない。
rootから単一子の段を降りた、group束ねで1 nodeへまとまった段を使う。最粗root(1 cluster以下)では影やcolliderが粗すぎるため。

 [VirtualGeometryRendererSetup](VirtualizedGeometry.Editor.VirtualGeometryRendererSetup.md)

URP の Renderer に、Virtual Geometry の専用描画(<xref href="VirtualizedGeometry.VirtualGeometryRenderFeature" data-throw-if-not-resolved="false"></xref>)を追加する。

 [VirtualGeometryShaderConversion](VirtualizedGeometry.Editor.VirtualGeometryShaderConversion.md)

変換結果。失敗時はErrorに理由を入れ、Sourceはnullにする。

 [VirtualGeometryShaderImporter](VirtualizedGeometry.Editor.VirtualGeometryShaderImporter.md)

Virtual Geometry Shader(.vgshader)。参照先shader(.shader / Shader Graph)から、元の全passとVG用forward passを持つShaderを生成する。
Materialのshaderにこれを選ぶと、同じMaterialで通常Mesh・Proxy・影とVG描画の両方に使える。参照先を編集すると再生成される。

 [VirtualGeometryShaderSource](VirtualizedGeometry.Editor.VirtualGeometryShaderSource.md)

URPのShaderLabソースから、元の全passに「頂点入力だけをVGのbufferへ差し替えたpass」を加えたソースを作る。
fragment処理・keyword・Propertiesは元shaderのものをそのまま使うため、Materialの見た目は通常Meshと同じになる。
必須はUniversalPipelineのforward pass(UniversalForward/UniversalForwardOnly/LightModeなし)。同じSubShaderにDepthOnly・DepthNormals(無ければDepthNormalsOnly)・
ShadowCasterがあれば、それぞれもVG版にする(prepassと影にVGの面を描くため。pass名は<xref href="VirtualizedGeometry.VirtualGeometryMaterials" data-throw-if-not-resolved="false"></xref>)。
追加のpassを変換できないときは、そのpassだけ作らない(<xref href="VirtualizedGeometry.Editor.VirtualGeometryShaderConversion.Warnings" data-throw-if-not-resolved="false"></xref>)。Deferred専用・BRP・HDRP・tessellation/geometry stageは扱わない。

### 構造体（Structs）

 [MeshOptimizerSimplifyResult](VirtualizedGeometry.Editor.MeshOptimizerSimplifyResult.md)

 [VirtualGeometryBuildDiagnostic](VirtualizedGeometry.Editor.VirtualGeometryBuildDiagnostic.md)

### 列挙型（Enums）

 [VirtualGeometryDiagnosticSeverity](VirtualizedGeometry.Editor.VirtualGeometryDiagnosticSeverity.md)
