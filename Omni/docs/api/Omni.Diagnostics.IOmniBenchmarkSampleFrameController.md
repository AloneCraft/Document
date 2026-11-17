# <a id="Omni_Diagnostics_IOmniBenchmarkSampleFrameController"></a> Interface IOmniBenchmarkSampleFrameController

Namespace: [Omni.Diagnostics](Omni.Diagnostics.md)  
Assembly: Radial.Runtime.dll  

採取フレームの開始境界で、シーン側の累積診断値を差分計測用に固定する任意契約です。

```csharp
public interface IOmniBenchmarkSampleFrameController
```

## 補足（Remarks）

RunnerはSequence Driverを呼んだ直後にこのメソッドを一度だけ呼び、EndOfFrameの
<xref href="Omni.Diagnostics.IOmniBenchmarkSceneController.CaptureBenchmarkCounters" data-throw-if-not-resolved="false"></xref>までを一標本とします。

## メソッド（Methods）

### <a id="Omni_Diagnostics_IOmniBenchmarkSampleFrameController_BeginBenchmarkSampleFrame"></a> BeginBenchmarkSampleFrame\(\)

次の一採取フレームのカウンター基準値を固定します。

```csharp
void BeginBenchmarkSampleFrame()
```
