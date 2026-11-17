# <a id="Omni_Diagnostics"></a> Namespace Omni.Diagnostics

### クラス（Classes）

 [OmniBenchmarkComparisonResult](Omni.Diagnostics.OmniBenchmarkComparisonResult.md)

<xref href="Omni.Diagnostics.OmniBenchmarkComparisonValidator" data-throw-if-not-resolved="false"></xref>が返す、比較可能性と実測比率の
不変スナップショットです。

 [OmniBenchmarkComparisonValidator](Omni.Diagnostics.OmniBenchmarkComparisonValidator.md)

Saturn Large ResidentのFrustumOnly/Omni計測JSONを、同一コンテンツ・同一環境の
比較として成立させられるか判定します。

 [OmniGalaxyPerformanceComparison](Omni.Diagnostics.OmniGalaxyPerformanceComparison.md)

Galaxy Player の 300 warm-up + 1,000 sample を、同一環境の baseline と比較する
専用ゲートです。既存の Saturn 用 600 sample 比較器とは契約を分離します。

 [OmniGalaxyPerformanceComparisonResult](Omni.Diagnostics.OmniGalaxyPerformanceComparisonResult.md)

 [OmniGalaxyPerformanceReport](Omni.Diagnostics.OmniGalaxyPerformanceReport.md)

 [OmniGpuImageMetrics](Omni.Diagnostics.OmniGpuImageMetrics.md)

実GPU比較で共通利用する、割り当てを発生させない画素統計です。
mask が false の画素は背景・UIとして比較から除外します。

 [OmniPerformanceBenchmarkRunner](Omni.Diagnostics.OmniPerformanceBenchmarkRunner.md)

コマンドラインで明示したPlayerだけで動作し、フレーム時間とOmniマーカーをJSONへ保存します。

 [OmniPerformanceMarkers](Omni.Diagnostics.OmniPerformanceMarkers.md)

Logical、Radial、Galaxyのホットパスで共有する低オーバーヘッドのProfilerマーカーです。

### 構造体（Structs）

 [OmniBenchmarkCounters](Omni.Diagnostics.OmniBenchmarkCounters.md)

シーンが各採取フレームで返す、累積ではないカリング・描画カウンターです。

 [OmniBenchmarkRequest](Omni.Diagnostics.OmniBenchmarkRequest.md)

Runnerが計測開始前にシーンへ一度だけ渡す、不変のベンチマーク要求です。

 [OmniBenchmarkSceneDescriptor](Omni.Diagnostics.OmniBenchmarkSceneDescriptor.md)

シーンが確定した描画backendと比較可能性をRunnerへ返す不変の記述子です。

 [OmniGpuImageMetricResult](Omni.Diagnostics.OmniGpuImageMetricResult.md)

### インターフェース（Interfaces）

 [IOmniBenchmarkCompletionController](Omni.Diagnostics.IOmniBenchmarkCompletionController.md)

ベンチマークの完走・中断・Runner破棄時に、Scene固有の一時構成を復帰する任意契約です。

 [IOmniBenchmarkDescriptorProvider](Omni.Diagnostics.IOmniBenchmarkDescriptorProvider.md)

warmup後や採取フレームの開始時に、実際に成立している描画backendと比較可能性を再取得する任意契約です。

 [IOmniBenchmarkSampleFrameController](Omni.Diagnostics.IOmniBenchmarkSampleFrameController.md)

採取フレームの開始境界で、シーン側の累積診断値を差分計測用に固定する任意契約です。

 [IOmniBenchmarkSceneController](Omni.Diagnostics.IOmniBenchmarkSceneController.md)

Benchmark Runnerからシーン固有の設定・実測カウンターを取得する公開契約です。

 [IOmniBenchmarkSequenceDriver](Omni.Diagnostics.IOmniBenchmarkSequenceDriver.md)

固定SequenceTimeまたはStreamingの時刻列を、採取フレーム単位で適用する任意契約です。

### 列挙型（Enums）

 [OmniBenchmarkCullingMode](Omni.Diagnostics.OmniBenchmarkCullingMode.md)

ベンチマーク中に適用する粒子カリング方式を表します。

 [OmniBenchmarkKind](Omni.Diagnostics.OmniBenchmarkKind.md)

性能計測が対象とするコンテンツ種別を表します。

 [OmniBenchmarkResidencyMode](Omni.Diagnostics.OmniBenchmarkResidencyMode.md)

ベンチマーク中に適用する粒子常駐方式を表します。
