# <a id="Omni_Diagnostics_OmniBenchmarkCounters"></a> Struct OmniBenchmarkCounters

Namespace: [Omni.Diagnostics](Omni.Diagnostics.md)  
Assembly: Radial.Runtime.dll  

シーンが各採取フレームで返す、累積ではないカリング・描画カウンターです。

```csharp
public readonly struct OmniBenchmarkCounters
```

## 補足（Remarks）

実装側はこの値をallocationなしで取得できるようにし、使用しない値は0を返します。
すべての値はそのフレームの実値であり、前フレームから加算してはいけません。

## コンストラクター（Constructors）

### <a id="Omni_Diagnostics_OmniBenchmarkCounters__ctor_System_Int64_System_Int64_System_Int64_System_Int64_System_Int64_System_Int64_System_Int64_System_Int64_System_Int64_System_Int64_"></a> OmniBenchmarkCounters\(long, long, long, long, long, long, long, long, long, long\)

フレーム単位のベンチマークカウンターを作成します。

```csharp
public OmniBenchmarkCounters(long cullingCandidateCount, long frustumVisibleCount, long visibleInstanceCount, long omniRejectedCount, long instanceWriteCount, long drawCommandCount, long epochRebuildCount, long failOpenCount, long staleViewContextCount, long indeterminateShellRelationCount)
```

#### 引数（Parameters）

`cullingCandidateCount` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`frustumVisibleCount` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`visibleInstanceCount` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`omniRejectedCount` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`instanceWriteCount` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`drawCommandCount` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`epochRebuildCount` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`failOpenCount` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`staleViewContextCount` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`indeterminateShellRelationCount` [long](https://learn.microsoft.com/dotnet/api/system.int64)

## プロパティ（Properties）

### <a id="Omni_Diagnostics_OmniBenchmarkCounters_CullingCandidateCount"></a> CullingCandidateCount

詳細判定に渡した候補粒子数です。

```csharp
public long CullingCandidateCount { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Diagnostics_OmniBenchmarkCounters_DrawCommandCount"></a> DrawCommandCount

提出したdraw command数です。

```csharp
public long DrawCommandCount { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Diagnostics_OmniBenchmarkCounters_EpochRebuildCount"></a> EpochRebuildCount

このフレームに完了したepoch索引再構築数です。

```csharp
public long EpochRebuildCount { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Diagnostics_OmniBenchmarkCounters_FailOpenCount"></a> FailOpenCount

非有限値等によりfail-openした判定数です。

```csharp
public long FailOpenCount { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Diagnostics_OmniBenchmarkCounters_FrustumVisibleCount"></a> FrustumVisibleCount

通常の錐台判定を通過した粒子数です。

```csharp
public long FrustumVisibleCount { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Diagnostics_OmniBenchmarkCounters_IndeterminateShellRelationCount"></a> IndeterminateShellRelationCount

shell関係がIndeterminateとなった回数です。

```csharp
public long IndeterminateShellRelationCount { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Diagnostics_OmniBenchmarkCounters_InstanceWriteCount"></a> InstanceWriteCount

カリング候補ワーキングセットへ書き込んだinstance slot数です。最終可視ID数は<xref href="Omni.Diagnostics.OmniBenchmarkCounters.VisibleInstanceCount" data-throw-if-not-resolved="false"></xref>を使います。

```csharp
public long InstanceWriteCount { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Diagnostics_OmniBenchmarkCounters_OmniRejectedCount"></a> OmniRejectedCount

Omni追加判定で除外した粒子数です。

```csharp
public long OmniRejectedCount { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Diagnostics_OmniBenchmarkCounters_StaleViewContextCount"></a> StaleViewContextCount

staleなview contextを検出した回数です。

```csharp
public long StaleViewContextCount { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Diagnostics_OmniBenchmarkCounters_VisibleInstanceCount"></a> VisibleInstanceCount

最終的に可視と判定した粒子数です。

```csharp
public long VisibleInstanceCount { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)
