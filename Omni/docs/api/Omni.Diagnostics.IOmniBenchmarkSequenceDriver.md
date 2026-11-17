# <a id="Omni_Diagnostics_IOmniBenchmarkSequenceDriver"></a> Interface IOmniBenchmarkSequenceDriver

Namespace: [Omni.Diagnostics](Omni.Diagnostics.md)  
Assembly: Radial.Runtime.dll  

固定SequenceTimeまたはStreamingの時刻列を、採取フレーム単位で適用する任意契約です。

```csharp
public interface IOmniBenchmarkSequenceDriver
```

## 補足（Remarks）

時刻適用はRunnerが採取フレーム開始時にだけ要求します。実装はseekとして評価し、音声などの
前進副作用を発火してはいけません。

## メソッド（Methods）

### <a id="Omni_Diagnostics_IOmniBenchmarkSequenceDriver_TryDriveBenchmarkSequence_Omni_Diagnostics_OmniBenchmarkRequest_System_Int32_System_Int32_System_Double__System_String__"></a> TryDriveBenchmarkSequence\(OmniBenchmarkRequest, int, int, out double, out string\)

指定標本のSequenceTimeをSceneへ適用します。

```csharp
bool TryDriveBenchmarkSequence(OmniBenchmarkRequest request, int sampleIndex, int sampleCount, out double sequenceTimeSeconds, out string rejectionReason)
```

#### 引数（Parameters）

`request` [OmniBenchmarkRequest](Omni.Diagnostics.OmniBenchmarkRequest.md)

開始前に固定したベンチマーク要求です。

`sampleIndex` [int](https://learn.microsoft.com/dotnet/api/system.int32)

0始まりの採取標本番号です。

`sampleCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

採取予定総数。1以上です。

`sequenceTimeSeconds` [double](https://learn.microsoft.com/dotnet/api/system.double)

実際に適用できた有限のSequenceTime（秒）です。

`rejectionReason` [string](https://learn.microsoft.com/dotnet/api/system.string)

適用不能な場合の機械可読な理由。成功時は空文字列です。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

指定時刻を安全に適用できた場合はtrueです。
