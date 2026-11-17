# <a id="Omni_Diagnostics_OmniPerformanceBenchmarkRunner"></a> Class OmniPerformanceBenchmarkRunner

Namespace: [Omni.Diagnostics](Omni.Diagnostics.md)  
Assembly: Radial.Runtime.dll  

コマンドラインで明示したPlayerだけで動作し、フレーム時間とOmniマーカーをJSONへ保存します。

```csharp
[DisallowMultipleComponent]
public sealed class OmniPerformanceBenchmarkRunner : MonoBehaviour
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[OmniPerformanceBenchmarkRunner](Omni.Diagnostics.OmniPerformanceBenchmarkRunner.md)

## 補足（Remarks）

通常のPlayerでは<code>-omni-benchmark</code>がないためGameObject、Recorder、ファイル出力を
一切作りません。計測を有効にする例は
<code>-omni-benchmark -omni-benchmark-scene Galaxy -omni-benchmark-warmup 120 -omni-benchmark-frames 600 -omni-benchmark-quit</code>です。

## メソッド（Methods）

### <a id="Omni_Diagnostics_OmniPerformanceBenchmarkRunner_IsAutoQuitRequested_System_Collections_Generic_IReadOnlyList_System_String__"></a> IsAutoQuitRequested\(IReadOnlyList<string\>\)

自動終了スイッチがあるかを返します。

```csharp
public static bool IsAutoQuitRequested(IReadOnlyList<string> arguments)
```

#### 引数（Parameters）

`arguments` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

実行ファイル名を含むコマンドライン引数。nullならfalse。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

<code>-omni-benchmark-quit</code>が完全一致で含まれる場合のみtrue。

### <a id="Omni_Diagnostics_OmniPerformanceBenchmarkRunner_IsBenchmarkComplete_System_Int32_System_Int32_System_Boolean_System_Boolean_System_Boolean_"></a> IsBenchmarkComplete\(int, int, bool, bool, bool\)

サンプル、FrameTiming、Recorder、実行品質の必須条件を満たす場合だけ完走と判定します。

```csharp
public static bool IsBenchmarkComplete(int requestedSampleFrames, int collectedSampleFrames, bool hasRequiredFrameTiming, bool hasRequiredRecorders, bool hasExpectedRuntimeConfiguration)
```

#### 引数（Parameters）

`requestedSampleFrames` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`collectedSampleFrames` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`hasRequiredFrameTiming` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`hasRequiredRecorders` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`hasExpectedRuntimeConfiguration` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Diagnostics_OmniPerformanceBenchmarkRunner_IsBenchmarkRequested_System_Collections_Generic_IReadOnlyList_System_String__"></a> IsBenchmarkRequested\(IReadOnlyList<string\>\)

コマンドラインに性能計測の明示スイッチがあるかを返します。

```csharp
public static bool IsBenchmarkRequested(IReadOnlyList<string> arguments)
```

#### 引数（Parameters）

`arguments` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

実行ファイル名を含むコマンドライン引数。nullならfalse。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

<code>-omni-benchmark</code>が完全一致で含まれる場合のみtrue。

### <a id="Omni_Diagnostics_OmniPerformanceBenchmarkRunner_IsValidForComparison_System_Boolean_Omni_Diagnostics_OmniBenchmarkRequest_Omni_Diagnostics_OmniBenchmarkSceneDescriptor_"></a> IsValidForComparison\(bool, OmniBenchmarkRequest, OmniBenchmarkSceneDescriptor\)

完走済みの測定値が、固定コンテンツと比較可能backendを使う正規比較として利用できるかを返します。

```csharp
public static bool IsValidForComparison(bool isBenchmarkComplete, OmniBenchmarkRequest request, OmniBenchmarkSceneDescriptor descriptor)
```

#### 引数（Parameters）

`isBenchmarkComplete` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

必須の測定契約を満たして完走した場合はtrueです。

`request` [OmniBenchmarkRequest](Omni.Diagnostics.OmniBenchmarkRequest.md)

計測開始前に固定した要求です。

`descriptor` [OmniBenchmarkSceneDescriptor](Omni.Diagnostics.OmniBenchmarkSceneDescriptor.md)

Scene Controllerが返した実backend記述子です。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

比較可能な結果ならtrueです。

### <a id="Omni_Diagnostics_OmniPerformanceBenchmarkRunner_RequiresEffectiveSequenceDriver_Omni_Diagnostics_OmniBenchmarkRequest_"></a> RequiresEffectiveSequenceDriver\(OmniBenchmarkRequest\)

要求した比較が実時刻の適用を必要とする場合にtrueを返します。

```csharp
public static bool RequiresEffectiveSequenceDriver(OmniBenchmarkRequest request)
```

#### 引数（Parameters）

`request` [OmniBenchmarkRequest](Omni.Diagnostics.OmniBenchmarkRequest.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Diagnostics_OmniPerformanceBenchmarkRunner_ShouldCaptureAtEndOfFrame_System_Boolean_System_Int32_System_Boolean_"></a> ShouldCaptureAtEndOfFrame\(bool, int, bool\)

描画後の採取条件を満たすかを返します。

```csharp
public static bool ShouldCaptureAtEndOfFrame(bool initialized, int warmupFramesRemaining, bool recordersStarted)
```

#### 引数（Parameters）

`initialized` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

Runnerが初期化済みならtrue。

`warmupFramesRemaining` [int](https://learn.microsoft.com/dotnet/api/system.int32)

残りウォームアップフレーム数。

`recordersStarted` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

Profiler Recorderを開始済みならtrue。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

描画後に一件採取してよい場合はtrue。

### <a id="Omni_Diagnostics_OmniPerformanceBenchmarkRunner_TryResolveRequestedSampleSequenceTime_Omni_Diagnostics_OmniBenchmarkRequest_System_Int32_System_Int32_System_Double__"></a> TryResolveRequestedSampleSequenceTime\(OmniBenchmarkRequest, int, int, out double\)

固定時刻または明示Streaming範囲から、指定した採取標本の時刻を決定します。

```csharp
public static bool TryResolveRequestedSampleSequenceTime(OmniBenchmarkRequest request, int sampleIndex, int sampleCount, out double sequenceTimeSeconds)
```

#### 引数（Parameters）

`request` [OmniBenchmarkRequest](Omni.Diagnostics.OmniBenchmarkRequest.md)

開始前に固定したベンチマーク要求です。

`sampleIndex` [int](https://learn.microsoft.com/dotnet/api/system.int32)

0始まりの採取標本番号です。

`sampleCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

採取予定総数。1以上を渡します。

`sequenceTimeSeconds` [double](https://learn.microsoft.com/dotnet/api/system.double)

成功時の有限な評価時刻（秒）です。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

要求自身が時刻を明示している場合はtrueです。既定時刻はScene固有Driverが決めます。
