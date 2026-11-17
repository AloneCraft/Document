# <a id="Omni_Editor_BatchRendering"></a> Namespace Omni.Editor.BatchRendering

### クラス（Classes）

 [OmniAdaptiveProbeVolumeSpaceAuthoring](Omni.Editor.BatchRendering.OmniAdaptiveProbeVolumeSpaceAuthoring.md)

URP APVのworldOffsetと、同じ表示RootにあるLight Probe空間契約を一括構成します。
APVの公式offsetが表現できる有限な平行移動だけを受け入れます。

 [OmniLightProbeSpaceAuthoring](Omni.Editor.BatchRendering.OmniLightProbeSpaceAuthoring.md)

表示RootへLight Probe空間の明示契約を一貫して構成するEditor authoring境界です。
自動保存やBRG rebuildの直接要求は行わず、Space自身の変更通知へ委ねます。

 [RadialSceneBrgEditorIntegration](Omni.Editor.BatchRendering.RadialSceneBrgEditorIntegration.md)

Scene BRGのEditor通知集約、sidecar生成、Build検証を管理します。

 [RadialSceneBrgPreparationFailure](Omni.Editor.BatchRendering.RadialSceneBrgPreparationFailure.md)

sidecar準備の失敗内容です。原因のMaterial、Shader、段階、影響先を保持します。

 [RadialSceneBrgPreparationReport](Omni.Editor.BatchRendering.RadialSceneBrgPreparationReport.md)

1回のsidecar準備の結果です。

 [RadialSceneBrgPreparationStatus](Omni.Editor.BatchRendering.RadialSceneBrgPreparationStatus.md)

準備状態を利用者向けの分類へ変換します。

 [RadialSceneResidentCacheDiagnostics](Omni.Editor.BatchRendering.RadialSceneResidentCacheDiagnostics.md)

外部Editor自動化からResident cacheだけをA/B計測するための狭い診断入口です。
Runtimeの内部cache型や公開APIは露出しません。

### 列挙型（Enums）

 [RadialSceneBrgPreparationScope](Omni.Editor.BatchRendering.RadialSceneBrgPreparationScope.md)

準備の対象範囲です。

 [RadialSceneBrgPreparationStage](Omni.Editor.BatchRendering.RadialSceneBrgPreparationStage.md)

Scene BRG sidecar準備が止まった段階です。

 [RadialSceneBrgPreparationTrigger](Omni.Editor.BatchRendering.RadialSceneBrgPreparationTrigger.md)

準備を開始した契機です。

 [RadialSceneBrgReadiness](Omni.Editor.BatchRendering.RadialSceneBrgReadiness.md)

ロード済みSceneのBRG描画準備を利用者へ示す分類です。
