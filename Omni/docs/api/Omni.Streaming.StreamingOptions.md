# <a id="Omni_Streaming_StreamingOptions"></a> Class StreamingOptions

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

host の値で決める設定。ランタイムの定数にしない: 既定値は <xref href="Omni.Streaming.StreamingOptions.Default" data-throw-if-not-resolved="false"></xref> が出し、すべて上書きできる
(プラットフォームごとの既定は、Unity 側がプラットフォームの能力から作って渡す)。

```csharp
public sealed class StreamingOptions
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[StreamingOptions](Omni.Streaming.StreamingOptions.md)

## フィールド（Fields）

### <a id="Omni_Streaming_StreamingOptions_CancelGraceTicks"></a> CancelGraceTicks

関心から外れた取得中の要求を取り消すまでの Tick 数(関心の一瞬の揺れで取り消さないため)。

```csharp
public int CancelGraceTicks
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_StreamingOptions_DecodedMemoryBudget"></a> DecodedMemoryBudget

展開済みの中身の合計バイト数の予算。使われていないものを古い順に追い出す。

```csharp
public long DecodedMemoryBudget
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Streaming_StreamingOptions_MaximumCandidatesPerTick"></a> MaximumCandidatesPerTick

1回の Tick が取得を始めるために見る、優先度の高い候補の数の上限。

```csharp
public int MaximumCandidatesPerTick
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_StreamingOptions_MaximumCoalesceGap"></a> MaximumCoalesceGap

隣り合う範囲を1回の取得にまとめる許容の隙間(byte)。0 は隙間なしだけ。まとめるのは範囲取得ができる取得元だけ。

```csharp
public int MaximumCoalesceGap
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_StreamingOptions_MaximumCoalescedBytes"></a> MaximumCoalescedBytes

1回にまとめる取得の最大バイト数。

```csharp
public int MaximumCoalescedBytes
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_StreamingOptions_MaximumInFlightBytes"></a> MaximumInFlightBytes

取得中のバイト数の上限(0 は無制限)。1件も進んでいないときは、1件が上限を超えても始める。

```csharp
public long MaximumInFlightBytes
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Streaming_StreamingOptions_MaximumInFlightRequests"></a> MaximumInFlightRequests

同時に進める取得の数(取得元の希望と小さい方を使う)。

```csharp
public int MaximumInFlightRequests
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_StreamingOptions_MaximumRetries"></a> MaximumRetries

取得の失敗を再試行する回数(最初の1回を除く)。

```csharp
public int MaximumRetries
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_StreamingOptions_RecordRetentionTicks"></a> RecordRetentionTicks

この Tick 数、関心にも常駐にも無い記録(Absent・Failed・Unavailable・Unknown)を捨てる。

```csharp
public int RecordRetentionTicks
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_StreamingOptions_RetryInitialSeconds"></a> RetryInitialSeconds

```csharp
public double RetryInitialSeconds
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Streaming_StreamingOptions_RetryMaximumSeconds"></a> RetryMaximumSeconds

```csharp
public double RetryMaximumSeconds
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Streaming_StreamingOptions_UnavailableRecheckSeconds"></a> UnavailableRecheckSeconds

カタログが Unavailable のキーを問い合わせ直す間隔。

```csharp
public double UnavailableRecheckSeconds
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Streaming_StreamingOptions_VerifyIntegrity"></a> VerifyIntegrity

取得した中身の ID を計算して照合する(I4)。

```csharp
public bool VerifyIntegrity
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## プロパティ（Properties）

### <a id="Omni_Streaming_StreamingOptions_Default"></a> Default

```csharp
public static StreamingOptions Default { get; }
```

#### 値（Property Value）

 [StreamingOptions](Omni.Streaming.StreamingOptions.md)

## メソッド（Methods）

### <a id="Omni_Streaming_StreamingOptions_Clone"></a> Clone\(\)

```csharp
public StreamingOptions Clone()
```

#### 戻り値（Returns）

 [StreamingOptions](Omni.Streaming.StreamingOptions.md)

### <a id="Omni_Streaming_StreamingOptions_Validate"></a> Validate\(\)

```csharp
public void Validate()
```
