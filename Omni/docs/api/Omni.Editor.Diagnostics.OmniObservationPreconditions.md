# <a id="Omni_Editor_Diagnostics_OmniObservationPreconditions"></a> Class OmniObservationPreconditions

Namespace: [Omni.Editor.Diagnostics](Omni.Editor.Diagnostics.md)  
Assembly: Omni.Editor.dll  

観測の前提を判定する純粋関数です。入力は値だけで、静的な状態や Editor の API を読みません。
前提が 1 つでも崩れた観測は、計測が合格でも不合格でも <xref href="Omni.Editor.Diagnostics.OmniObservationOutcome.Unavailable" data-throw-if-not-resolved="false"></xref> です。

```csharp
public static class OmniObservationPreconditions
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniObservationPreconditions](Omni.Editor.Diagnostics.OmniObservationPreconditions.md)

## フィールド（Fields）

### <a id="Omni_Editor_Diagnostics_OmniObservationPreconditions_RenderStartWaitSeconds"></a> RenderStartWaitSeconds

落ち着きの更新を終えた観測が、描画の開始を待つ時間の上限（秒）です。Editor の更新と View の描画は
同じ頻度とは限らないため、更新の回数ではなくこの時間で待ちます。

```csharp
public const double RenderStartWaitSeconds = 5
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

## メソッド（Methods）

### <a id="Omni_Editor_Diagnostics_OmniObservationPreconditions_Aggregate_System_Collections_Generic_IEnumerable_Omni_Editor_Diagnostics_OmniObservationOutcome__"></a> Aggregate\(IEnumerable<OmniObservationOutcome\>\)

独立した複数の観測を集計します。Failed が 1 件でもあれば Failed、無ければ Unavailable が 1 件でも
あれば Unavailable、全件 Passed のときだけ Passed です。0 件の集計は Unavailable です。

```csharp
public static OmniObservationOutcome Aggregate(IEnumerable<OmniObservationOutcome> outcomes)
```

#### 引数（Parameters）

`outcomes` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<[OmniObservationOutcome](Omni.Editor.Diagnostics.OmniObservationOutcome.md)\>

#### 戻り値（Returns）

 [OmniObservationOutcome](Omni.Editor.Diagnostics.OmniObservationOutcome.md)

### <a id="Omni_Editor_Diagnostics_OmniObservationPreconditions_ClassifyTestRun_System_String_Omni_Editor_Diagnostics_OmniTestRunCounts_System_Collections_Generic_IReadOnlyList_System_String__System_Collections_Generic_IReadOnlyList_Omni_Editor_Diagnostics_OmniTestNode__"></a> ClassifyTestRun\(string, OmniTestRunCounts, IReadOnlyList<string\>, IReadOnlyList<OmniTestNode\>\)

テスト実行の結果を分類します。テスト実行は独立した観測の集まりとして扱い、実行されたテストに
不合格があれば、他の理由があっても <xref href="Omni.Editor.Diagnostics.OmniObservationOutcome.Failed" data-throw-if-not-resolved="false"></xref>（理由は併記）です。
不合格が無く理由があれば <xref href="Omni.Editor.Diagnostics.OmniObservationOutcome.Unavailable" data-throw-if-not-resolved="false"></xref> です。

```csharp
public static OmniObservationReport ClassifyTestRun(string observer, OmniTestRunCounts counts, IReadOnlyList<string> requestedFilters, IReadOnlyList<OmniTestNode> nodes)
```

#### 引数（Parameters）

`observer` [string](https://learn.microsoft.com/dotnet/api/system.string)

観測した入口の名前です。

`counts` [OmniTestRunCounts](Omni.Editor.Diagnostics.OmniTestRunCounts.md)

実行全体の集計値です。

`requestedFilters` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

要求したテスト名です。null なら照合しません。

`nodes` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[OmniTestNode](Omni.Editor.Diagnostics.OmniTestNode.md)\>

結果の木の全節点です。

#### 戻り値（Returns）

 [OmniObservationReport](Omni.Editor.Diagnostics.OmniObservationReport.md)

### <a id="Omni_Editor_Diagnostics_OmniObservationPreconditions_ClassifyTestRunWithFilterState_System_String_Omni_Editor_Diagnostics_OmniTestRunCounts_System_Boolean_System_Collections_Generic_IReadOnlyList_System_String__System_Collections_Generic_IReadOnlyList_Omni_Editor_Diagnostics_OmniTestNode__"></a> ClassifyTestRunWithFilterState\(string, OmniTestRunCounts, bool, IReadOnlyList<string\>, IReadOnlyList<OmniTestNode\>\)

要求したテスト名を読めたかを添えてテスト実行を分類します。読めなかった（<code class="paramref">filtersKnown</code> が false）
要求は、全件の実行か名前付きの実行かを区別できません。不合格が無ければ合格にせず、
<xref href="Omni.Editor.Diagnostics.OmniObservationReason.TestFilterStateUnknown" data-throw-if-not-resolved="false"></xref> の Unavailable にします。

```csharp
public static OmniObservationReport ClassifyTestRunWithFilterState(string observer, OmniTestRunCounts counts, bool filtersKnown, IReadOnlyList<string> requestedFilters, IReadOnlyList<OmniTestNode> nodes)
```

#### 引数（Parameters）

`observer` [string](https://learn.microsoft.com/dotnet/api/system.string)

`counts` [OmniTestRunCounts](Omni.Editor.Diagnostics.OmniTestRunCounts.md)

`filtersKnown` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`requestedFilters` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

`nodes` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[OmniTestNode](Omni.Editor.Diagnostics.OmniTestNode.md)\>

#### 戻り値（Returns）

 [OmniObservationReport](Omni.Editor.Diagnostics.OmniObservationReport.md)

### <a id="Omni_Editor_Diagnostics_OmniObservationPreconditions_Combine_Omni_Editor_Diagnostics_OmniObservationReport_System_Boolean_System_String_"></a> Combine\(OmniObservationReport, bool, string\)

前提の報告と計測の合否を合成します。前提が崩れていれば計測の合否によらず Unavailable、
前提が満たされていれば計測の合否がそのまま Passed / Failed になります。判定は前提の報告の結果で行い、
前提の報告として読めないもの（Failed、理由を持つ Passed、既知の理由を持たない Unavailable）は成功側へ
倒さず Failed にします。

```csharp
public static OmniObservationReport Combine(OmniObservationReport preconditions, bool measurementPassed, string measurementDetail)
```

#### 引数（Parameters）

`preconditions` [OmniObservationReport](Omni.Editor.Diagnostics.OmniObservationReport.md)

`measurementPassed` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`measurementDetail` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [OmniObservationReport](Omni.Editor.Diagnostics.OmniObservationReport.md)

### <a id="Omni_Editor_Diagnostics_OmniObservationPreconditions_Evaluate_System_String_Omni_Editor_Diagnostics_OmniObservationEnvironment__Omni_Editor_Diagnostics_OmniObservationRequirements__"></a> Evaluate\(string, in OmniObservationEnvironment, in OmniObservationRequirements\)

Editor 環境の前提を判定します。

```csharp
public static OmniObservationReport Evaluate(string observer, in OmniObservationEnvironment environment, in OmniObservationRequirements requirements)
```

#### 引数（Parameters）

`observer` [string](https://learn.microsoft.com/dotnet/api/system.string)

`environment` [OmniObservationEnvironment](Omni.Editor.Diagnostics.OmniObservationEnvironment.md)

`requirements` [OmniObservationRequirements](Omni.Editor.Diagnostics.OmniObservationRequirements.md)

#### 戻り値（Returns）

 [OmniObservationReport](Omni.Editor.Diagnostics.OmniObservationReport.md)

### <a id="Omni_Editor_Diagnostics_OmniObservationPreconditions_EvaluateControl_System_String_System_Boolean_System_String_"></a> EvaluateControl\(string, bool, string\)

既知の正解を持つ対照が期待どおりだったかを前提として判定します。

```csharp
public static OmniObservationReport EvaluateControl(string observer, bool controlMatchedExpectation, string controlDetail)
```

#### 引数（Parameters）

`observer` [string](https://learn.microsoft.com/dotnet/api/system.string)

`controlMatchedExpectation` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`controlDetail` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [OmniObservationReport](Omni.Editor.Diagnostics.OmniObservationReport.md)

### <a id="Omni_Editor_Diagnostics_OmniObservationPreconditions_EvaluateImage_System_String_Omni_Editor_Diagnostics_OmniImageEvidence__System_Int32_"></a> EvaluateImage\(string, in OmniImageEvidence, int\)

比較型の観測で、画像が比較の証拠になるかを判定します。対象が見えること自体を検査する観測では
この前提を使わず、画素 0 を不合格として扱います。

```csharp
public static OmniObservationReport EvaluateImage(string observer, in OmniImageEvidence evidence, int minimumTargetPixels)
```

#### 引数（Parameters）

`observer` [string](https://learn.microsoft.com/dotnet/api/system.string)

`evidence` [OmniImageEvidence](Omni.Editor.Diagnostics.OmniImageEvidence.md)

`minimumTargetPixels` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [OmniObservationReport](Omni.Editor.Diagnostics.OmniObservationReport.md)

### <a id="Omni_Editor_Diagnostics_OmniObservationPreconditions_EvaluateInputDelivery_System_String_Omni_Editor_Diagnostics_OmniInputDeliveryEvidence__"></a> EvaluateInputDelivery\(string, in OmniInputDeliveryEvidence\)

実入力が Unity に届いたかを判定します。再読み込みで中断した観測は
<xref href="Omni.Editor.Diagnostics.OmniObservationReason.AssemblyReloadInterrupted" data-throw-if-not-resolved="false"></xref>、セッションが他の理由で失われた場合は
無効化の証拠が無いので理由なしの <xref href="Omni.Editor.Diagnostics.OmniObservationOutcome.Failed" data-throw-if-not-resolved="false"></xref> です。セッションが有効なら、
テスト実行の進行（<xref href="Omni.Editor.Diagnostics.OmniObservationReason.TestRunActive" data-throw-if-not-resolved="false"></xref>）、他の自動化の要求の受理
（<xref href="Omni.Editor.Diagnostics.OmniObservationReason.ConcurrentAutomationRequest" data-throw-if-not-resolved="false"></xref>）、期待した入力の 0 件
（<xref href="Omni.Editor.Diagnostics.OmniObservationReason.InputNotDelivered" data-throw-if-not-resolved="false"></xref>）のどれかがあれば Unavailable で、
合成イベントが混ざり得る観測を届いた証拠にしません。

```csharp
public static OmniObservationReport EvaluateInputDelivery(string observer, in OmniInputDeliveryEvidence evidence)
```

#### 引数（Parameters）

`observer` [string](https://learn.microsoft.com/dotnet/api/system.string)

`evidence` [OmniInputDeliveryEvidence](Omni.Editor.Diagnostics.OmniInputDeliveryEvidence.md)

#### 戻り値（Returns）

 [OmniObservationReport](Omni.Editor.Diagnostics.OmniObservationReport.md)

#### 例外（Exceptions）

 [ArgumentOutOfRangeException](https://learn.microsoft.com/dotnet/api/system.argumentoutofrangeexception)

件数が負の場合。

### <a id="Omni_Editor_Diagnostics_OmniObservationPreconditions_EvaluateRegionOcclusion_System_String_UnityEngine_RectInt_System_Collections_Generic_IReadOnlyList_Omni_Editor_Diagnostics_OmniScreenOccluder__"></a> EvaluateRegionOcclusion\(string, RectInt, IReadOnlyList<OmniScreenOccluder\>\)

測定に使った画素の領域に重なる遮蔽物を前提として判定します。<code class="paramref">measuredRegion</code> と
<code class="paramref">occluders</code> の矩形は同じ座標系で渡します。辺が接するだけの遮蔽物と、領域の外の遮蔽物
（Scene View には重なるが測定した画素には重ならない浮いたウィンドウなど）は理由にしません。
領域が空の場合は何も測っていないので理由にしません（全体が隠れて測定量が 0 になり得る観測者は、
画像全体を領域として渡します）。

```csharp
public static OmniObservationReport EvaluateRegionOcclusion(string observer, RectInt measuredRegion, IReadOnlyList<OmniScreenOccluder> occluders)
```

#### 引数（Parameters）

`observer` [string](https://learn.microsoft.com/dotnet/api/system.string)

`measuredRegion` RectInt

`occluders` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[OmniScreenOccluder](Omni.Editor.Diagnostics.OmniScreenOccluder.md)\>

#### 戻り値（Returns）

 [OmniObservationReport](Omni.Editor.Diagnostics.OmniObservationReport.md)

### <a id="Omni_Editor_Diagnostics_OmniObservationPreconditions_EvaluateWindow_System_String_Omni_Editor_Diagnostics_OmniObservationWindowSample__Omni_Editor_Diagnostics_OmniObservationWindowSample__Omni_Editor_Diagnostics_OmniObservationWindowRequirements__"></a> EvaluateWindow\(string, in OmniObservationWindowSample, in OmniObservationWindowSample, in OmniObservationWindowRequirements\)

観測窓の開始と終了の値から、窓の間の前提を判定します。前面は窓の開始の時点では問わず、
窓の間に前面を失っていないこと（喪失回数が同じで、終了時に前面）だけを要求します。
BRG の前進は、描画が進んだことを確かめない窓（<xref href="Omni.Editor.Diagnostics.OmniObservationWindowRequirements.minimumObservedFrames" data-throw-if-not-resolved="false"></xref>
が 0）か、描画も進まなかった窓では前提の崩れ（Unavailable）です。描画が進んだのに BRG の culling が
進まなかった窓は、BRG が描画された View を cull しなかったという製品の失敗の証拠なので、前提の報告ではなく
<xref href="Omni.Editor.Diagnostics.OmniObservationOutcome.Failed" data-throw-if-not-resolved="false"></xref>（理由 <xref href="Omni.Editor.Diagnostics.OmniObservationReason.BrgSequenceDidNotAdvance" data-throw-if-not-resolved="false"></xref>
と他の崩れを併記）を返します。呼び出し側は Failed を前提として記録せず、計測の不合格として扱います。

```csharp
public static OmniObservationReport EvaluateWindow(string observer, in OmniObservationWindowSample begin, in OmniObservationWindowSample end, in OmniObservationWindowRequirements requirements)
```

#### 引数（Parameters）

`observer` [string](https://learn.microsoft.com/dotnet/api/system.string)

`begin` [OmniObservationWindowSample](Omni.Editor.Diagnostics.OmniObservationWindowSample.md)

`end` [OmniObservationWindowSample](Omni.Editor.Diagnostics.OmniObservationWindowSample.md)

`requirements` [OmniObservationWindowRequirements](Omni.Editor.Diagnostics.OmniObservationWindowRequirements.md)

#### 戻り値（Returns）

 [OmniObservationReport](Omni.Editor.Diagnostics.OmniObservationReport.md)

### <a id="Omni_Editor_Diagnostics_OmniObservationPreconditions_HasBrgAdvanced_System_Int32_System_Int32_System_Int32_System_Int32_"></a> HasBrgAdvanced\(int, int, int, int\)

BRG の culling が窓の間に進んだかを返します。同じ backend 世代なら順番が増えたこと、世代が進んだ
なら新しい世代で 1 回以上 culling したことを要求します。世代が戻った場合は false です。

```csharp
public static bool HasBrgAdvanced(int beginGeneration, int beginSequence, int endGeneration, int endSequence)
```

#### 引数（Parameters）

`beginGeneration` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`beginSequence` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`endGeneration` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`endSequence` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_OmniObservationPreconditions_IsFilterMatched_System_String_System_Collections_Generic_IReadOnlyList_Omni_Editor_Diagnostics_OmniTestNode__"></a> IsFilterMatched\(string, IReadOnlyList<OmniTestNode\>\)

テスト名の要求が、結果の木のいずれかの節点の完全名と完全一致し、その配下で 1 件以上のテストが
実行されたかを返します。前方一致は使いません（"FooTests" は "FooTestsExtra" に一致しません）。

```csharp
public static bool IsFilterMatched(string filter, IReadOnlyList<OmniTestNode> nodes)
```

#### 引数（Parameters）

`filter` [string](https://learn.microsoft.com/dotnet/api/system.string)

`nodes` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[OmniTestNode](Omni.Editor.Diagnostics.OmniTestNode.md)\>

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_OmniObservationPreconditions_MeasureImage_UnityEngine_Color32___System_Byte___UnityEngine_Color32_System_Int32_"></a> MeasureImage\(Color32\[\], byte\[\], Color32, int\)

画像の画素を数えます。<code class="paramref">targetMask</code> が null なら mask 無しとして全画素を対象にし、
mask があれば 0 以外の画素だけを対象にします。背景と RGB のいずれかの差が
<code class="paramref">channelThreshold</code> 以上の画素を背景以外と数えます。

```csharp
public static OmniImageEvidence MeasureImage(Color32[] pixels, byte[] targetMask, Color32 background, int channelThreshold)
```

#### 引数（Parameters）

`pixels` Color32\[\]

`targetMask` [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\]

`background` Color32

`channelThreshold` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [OmniImageEvidence](Omni.Editor.Diagnostics.OmniImageEvidence.md)

#### 例外（Exceptions）

 [ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)

pixels が null の場合。

 [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception)

mask と pixels の長さが違う場合。

 [ArgumentOutOfRangeException](https://learn.microsoft.com/dotnet/api/system.argumentoutofrangeexception)

閾値が 1 から 255 の外の場合。

### <a id="Omni_Editor_Diagnostics_OmniObservationPreconditions_Merge_System_String_Omni_Editor_Diagnostics_OmniObservationReport___"></a> Merge\(string, params OmniObservationReport\[\]\)

複数の前提の報告（Passed か Unavailable）を、理由の和集合で 1 つにまとめます。null は読み飛ばします。
環境は最初の報告のものを残します。判定は理由の一覧ではなく各報告の結果で行い、結果と理由が
食い違う報告（理由を持つ Passed、既知の理由を持たない Unavailable）は前提の報告として扱わず拒否します。

```csharp
public static OmniObservationReport Merge(string observer, params OmniObservationReport[] preconditions)
```

#### 引数（Parameters）

`observer` [string](https://learn.microsoft.com/dotnet/api/system.string)

`preconditions` [OmniObservationReport](Omni.Editor.Diagnostics.OmniObservationReport.md)\[\]

#### 戻り値（Returns）

 [OmniObservationReport](Omni.Editor.Diagnostics.OmniObservationReport.md)

#### 例外（Exceptions）

 [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception)

Failed の報告、または結果と理由が食い違う報告を渡した場合。前提の報告は Failed になりません。

### <a id="Omni_Editor_Diagnostics_OmniObservationPreconditions_ShouldWaitForRender_Omni_Editor_Diagnostics_OmniObservationWindowSample__Omni_Editor_Diagnostics_OmniObservationWindowSample__System_Double_System_Double__"></a> ShouldWaitForRender\(in OmniObservationWindowSample, in OmniObservationWindowSample, double, ref double\)

落ち着きの更新を終えた観測で、窓の開始の後の描画がまだ始まっていなければ、期限まで描画を待つかを返します。
最初に待つと決めた時点で <code class="paramref">deadline</code>（0 なら未設定）に期限を入れます。描画が始まっていれば、
または期限を過ぎていれば false で、呼び出し側が <xref href="Omni.Editor.Diagnostics.OmniObservationPreconditions.EvaluateWindow(System.String%2cOmni.Editor.Diagnostics.OmniObservationWindowSample%40%2cOmni.Editor.Diagnostics.OmniObservationWindowSample%40%2cOmni.Editor.Diagnostics.OmniObservationWindowRequirements%40)" data-throw-if-not-resolved="false"></xref> で窓を判定します。

```csharp
public static bool ShouldWaitForRender(in OmniObservationWindowSample begin, in OmniObservationWindowSample end, double now, ref double deadline)
```

#### 引数（Parameters）

`begin` [OmniObservationWindowSample](Omni.Editor.Diagnostics.OmniObservationWindowSample.md)

窓の開始の値です。

`end` [OmniObservationWindowSample](Omni.Editor.Diagnostics.OmniObservationWindowSample.md)

現在の窓の値です。

`now` [double](https://learn.microsoft.com/dotnet/api/system.double)

現在の Editor の時刻です。

`deadline` [double](https://learn.microsoft.com/dotnet/api/system.double)

描画を待つ期限です。窓を開始するたびに 0 へ戻します。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
