# <a id="Omni_Streaming_StreamingHost"></a> Class StreamingHost

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

```csharp
public sealed class StreamingHost : IDisposable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[StreamingHost](Omni.Streaming.StreamingHost.md)

#### 実装するインターフェース（Implements）

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

## コンストラクター（Constructors）

### <a id="Omni_Streaming_StreamingHost__ctor_Omni_Streaming_StreamingHostConfig_"></a> StreamingHost\(StreamingHostConfig\)

```csharp
public StreamingHost(StreamingHostConfig config)
```

#### 引数（Parameters）

`config` [StreamingHostConfig](Omni.Streaming.StreamingHostConfig.md)

## プロパティ（Properties）

### <a id="Omni_Streaming_StreamingHost_CurrentTick"></a> CurrentTick

```csharp
public long CurrentTick { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Streaming_StreamingHost_Diagnostics"></a> Diagnostics

```csharp
public StreamingTraceContext Diagnostics { get; }
```

#### 値（Property Value）

 [StreamingTraceContext](Omni.Streaming.StreamingTraceContext.md)

### <a id="Omni_Streaming_StreamingHost_Options"></a> Options

```csharp
public StreamingOptions Options { get; }
```

#### 値（Property Value）

 [StreamingOptions](Omni.Streaming.StreamingOptions.md)

### <a id="Omni_Streaming_StreamingHost_Store"></a> Store

```csharp
public IContentStore Store { get; }
```

#### 値（Property Value）

 [IContentStore](Omni.Streaming.IContentStore.md)

## メソッド（Methods）

### <a id="Omni_Streaming_StreamingHost_CreateInterest"></a> CreateInterest\(\)

```csharp
public IInterestWriter CreateInterest()
```

#### 戻り値（Returns）

 [IInterestWriter](Omni.Streaming.IInterestWriter.md)

### <a id="Omni_Streaming_StreamingHost_DeliverContent_Omni_Streaming_ContentId__Omni_Streaming_PooledBuffer_"></a> DeliverContent\(in ContentId, PooledBuffer\)

取得元が、host を介さずに中身を送り込んだとき(サーバーが送り込む型)に渡す。ID を照合してストアへ入れる。
buffer の参照は呼び手のもの(ストアが必要なら Retain する)。照合に失敗したら false。

```csharp
public bool DeliverContent(in ContentId id, PooledBuffer buffer)
```

#### 引数（Parameters）

`id` [ContentId](Omni.Streaming.ContentId.md)

`buffer` [PooledBuffer](Omni.Streaming.PooledBuffer.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_StreamingHost_DescribePending_System_Int32_"></a> DescribePending\(int\)

診断用: Pending のキーを(最大 limit 件)説明する。取得中か、展開待ちか、目録の答え待ちか、いつまで欲しがられているか。

```csharp
public List<string> DescribePending(int limit)
```

#### 引数（Parameters）

`limit` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Streaming_StreamingHost_Dispose"></a> Dispose\(\)

終了処理: 進行中の取得を取り消し、展開済みの中身を手放し、宣言を捨てる。借りている lease の中身は、返されるまで生きる。
呼んだ後の Tick・CreateInterest は何もしない/例外にはしない(二重 Dispose も安全)。

```csharp
public void Dispose()
```

### <a id="Omni_Streaming_StreamingHost_GetError_Omni_Streaming_StreamKey__"></a> GetError\(in StreamKey\)

失敗の理由(Failed のキー)。無ければ null。

```csharp
public string GetError(in StreamKey key)
```

#### 引数（Parameters）

`key` [StreamKey](Omni.Streaming.StreamKey.md)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Streaming_StreamingHost_GetState_Omni_Streaming_StreamKey__"></a> GetState\(in StreamKey\)

```csharp
public PayloadState GetState(in StreamKey key)
```

#### 引数（Parameters）

`key` [StreamKey](Omni.Streaming.StreamKey.md)

#### 戻り値（Returns）

 [PayloadState](Omni.Streaming.PayloadState.md)

### <a id="Omni_Streaming_StreamingHost_GetStats"></a> GetStats\(\)

```csharp
public StreamingStats GetStats()
```

#### 戻り値（Returns）

 [StreamingStats](Omni.Streaming.StreamingStats.md)

### <a id="Omni_Streaming_StreamingHost_Invalidate_Omni_Streaming_StreamKey__"></a> Invalidate\(in StreamKey\)

キーの状態を捨てて、次に欲しがられたときに最初からやり直す(データの更新、再試行の上限に達した失敗のやり直し)。
借りている lease の中身は、返されるまで生きる。取得中の要求は、結果が来ても採用しない。

```csharp
public void Invalidate(in StreamKey key)
```

#### 引数（Parameters）

`key` [StreamKey](Omni.Streaming.StreamKey.md)

### <a id="Omni_Streaming_StreamingHost_InvalidateAll"></a> InvalidateAll\(\)

```csharp
public void InvalidateAll()
```

### <a id="Omni_Streaming_StreamingHost_Preload_System_Collections_Generic_IEnumerable_Omni_Streaming_StreamKey__System_Single_"></a> Preload\(IEnumerable<StreamKey\>, float\)

```csharp
public PreloadHandle Preload(IEnumerable<StreamKey> keys, float priority = 0)
```

#### 引数（Parameters）

`keys` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<[StreamKey](Omni.Streaming.StreamKey.md)\>

`priority` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [PreloadHandle](Omni.Streaming.PreloadHandle.md)

### <a id="Omni_Streaming_StreamingHost_SetConcurrency_System_Int32_"></a> SetConcurrency\(int\)

同時に進める取得の数を、実行中に変える(取得元の希望と <xref href="Omni.Streaming.StreamingOptions.MaximumInFlightRequests" data-throw-if-not-resolved="false"></xref> の小さい方)。
進行中の取得は止めない(減らしたときは、減るまで新しく始めない)。

```csharp
public void SetConcurrency(int maximumInFlightRequests)
```

#### 引数（Parameters）

`maximumInFlightRequests` [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_StreamingHost_SetResourceLimits_System_Int64_System_Int64_System_Int32_"></a> SetResourceLimits\(long, long, int\)

Hostを単独所有するthreadで資源上限を変更する。進行中の取得とleaseは保持する。

```csharp
public void SetResourceLimits(long decodedBytes, long inFlightBytes, int requests)
```

#### 引数（Parameters）

`decodedBytes` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`inFlightBytes` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`requests` [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_StreamingHost_Tick_Omni_Streaming_FrameBudget_"></a> Tick\(FrameBudget\)

```csharp
public void Tick(FrameBudget budget)
```

#### 引数（Parameters）

`budget` [FrameBudget](Omni.Streaming.FrameBudget.md)

### <a id="Omni_Streaming_StreamingHost_TryAcquire_Omni_Streaming_StreamKey__Omni_Streaming_PayloadLease__"></a> TryAcquire\(in StreamKey, out PayloadLease\)

展開済み(Resident)なら lease を返す。lease を持つ間、その中身は追い出されない。

```csharp
public bool TryAcquire(in StreamKey key, out PayloadLease lease)
```

#### 引数（Parameters）

`key` [StreamKey](Omni.Streaming.StreamKey.md)

`lease` [PayloadLease](Omni.Streaming.PayloadLease.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_StreamingHost_TryGetInfo_Omni_Streaming_StreamKey__Omni_Streaming_KeyInfo__"></a> TryGetInfo\(in StreamKey, out KeyInfo\)

診断用: キーの詳しい状態。記録が無ければ false(Unknown)。

```csharp
public bool TryGetInfo(in StreamKey key, out KeyInfo info)
```

#### 引数（Parameters）

`key` [StreamKey](Omni.Streaming.StreamKey.md)

`info` [KeyInfo](Omni.Streaming.KeyInfo.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_StreamingHost_InternalError"></a> InternalError

```csharp
public event Action<Exception> InternalError
```

#### 型（Event Type）

 [Action](https://learn.microsoft.com/dotnet/api/system.action\-1)<[Exception](https://learn.microsoft.com/dotnet/api/system.exception)\>

### <a id="Omni_Streaming_StreamingHost_KeyFailed"></a> KeyFailed

```csharp
public event Action<StreamKey, string> KeyFailed
```

#### 型（Event Type）

 [Action](https://learn.microsoft.com/dotnet/api/system.action\-2)<[StreamKey](Omni.Streaming.StreamKey.md), [string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Streaming_StreamingHost_TransferFinished"></a> TransferFinished

```csharp
public event Action<TransferInfo> TransferFinished
```

#### 型（Event Type）

 [Action](https://learn.microsoft.com/dotnet/api/system.action\-1)<[TransferInfo](Omni.Streaming.TransferInfo.md)\>
