# <a id="Omni_Diagnostics_OmniBenchmarkComparisonResult"></a> Class OmniBenchmarkComparisonResult

Namespace: [Omni.Diagnostics](Omni.Diagnostics.md)  
Assembly: Radial.Runtime.dll  

<xref href="Omni.Diagnostics.OmniBenchmarkComparisonValidator" data-throw-if-not-resolved="false"></xref>が返す、比較可能性と実測比率の
不変スナップショットです。

```csharp
public sealed class OmniBenchmarkComparisonResult
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniBenchmarkComparisonResult](Omni.Diagnostics.OmniBenchmarkComparisonResult.md)

## プロパティ（Properties）

### <a id="Omni_Diagnostics_OmniBenchmarkComparisonResult_CandidateReductionRatio"></a> CandidateReductionRatio

候補判定数の削減率です。比較不能ならNaNです。

```csharp
public double CandidateReductionRatio { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Diagnostics_OmniBenchmarkComparisonResult_FailureReasons"></a> FailureReasons

不合格理由です。合格時は空配列です。

```csharp
public string[] FailureReasons { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)\[\]

### <a id="Omni_Diagnostics_OmniBenchmarkComparisonResult_FrustumCandidateCount"></a> FrustumCandidateCount

FrustumOnlyの候補判定総数です。

```csharp
public long FrustumCandidateCount { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Diagnostics_OmniBenchmarkComparisonResult_FrustumRingCullingP95Ms"></a> FrustumRingCullingP95Ms

FrustumOnlyのリングカリングP95（ms）です。

```csharp
public double FrustumRingCullingP95Ms { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Diagnostics_OmniBenchmarkComparisonResult_FrustumWorkingSetCounterName"></a> FrustumWorkingSetCounterName

FrustumOnly側で使用したworking-set write counter名です。

```csharp
public string FrustumWorkingSetCounterName { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Diagnostics_OmniBenchmarkComparisonResult_FrustumWorkingSetWriteCount"></a> FrustumWorkingSetWriteCount

FrustumOnlyのcandidate working-set write総数です。

```csharp
public long FrustumWorkingSetWriteCount { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Diagnostics_OmniBenchmarkComparisonResult_OmniCandidateCount"></a> OmniCandidateCount

Omniの候補判定総数です。

```csharp
public long OmniCandidateCount { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Diagnostics_OmniBenchmarkComparisonResult_OmniRingCullingP95Ms"></a> OmniRingCullingP95Ms

OmniのリングカリングP95（ms）です。

```csharp
public double OmniRingCullingP95Ms { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Diagnostics_OmniBenchmarkComparisonResult_OmniWorkingSetCounterName"></a> OmniWorkingSetCounterName

Omni側で使用したworking-set write counter名です。

```csharp
public string OmniWorkingSetCounterName { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Diagnostics_OmniBenchmarkComparisonResult_OmniWorkingSetWriteCount"></a> OmniWorkingSetWriteCount

Omniのcandidate working-set write総数です。

```csharp
public long OmniWorkingSetWriteCount { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Diagnostics_OmniBenchmarkComparisonResult_Passed"></a> Passed

すべての計測前提と削減条件を満たす場合にtrueです。

```csharp
public bool Passed { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Diagnostics_OmniBenchmarkComparisonResult_RingCullingP95ImprovementRatio"></a> RingCullingP95ImprovementRatio

リングカリングP95の短縮率です。比較不能ならNaNです。

```csharp
public double RingCullingP95ImprovementRatio { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Diagnostics_OmniBenchmarkComparisonResult_WorkingSetWriteReductionRatio"></a> WorkingSetWriteReductionRatio

candidate working-set writeの削減率です。比較不能ならNaNです。

```csharp
public double WorkingSetWriteReductionRatio { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)
