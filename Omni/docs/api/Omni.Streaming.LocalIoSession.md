# <a id="Omni_Streaming_LocalIoSession"></a> Class LocalIoSession

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

1HostのI/O予約。配列を作る前に予約し、引継ぎ後に通常の上限へ戻す。

```csharp
public sealed class LocalIoSession : IDisposable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[LocalIoSession](Omni.Streaming.LocalIoSession.md)

#### 実装するインターフェース（Implements）

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

## コンストラクター（Constructors）

### <a id="Omni_Streaming_LocalIoSession__ctor_System_Int64_Omni_Streaming_StreamingTraceContext_Omni_Streaming_LocalIoDispatcher_"></a> LocalIoSession\(long, StreamingTraceContext, LocalIoDispatcher\)

```csharp
public LocalIoSession(long byteLimit, StreamingTraceContext diagnostics = null, LocalIoDispatcher dispatcher = null)
```

#### 引数（Parameters）

`byteLimit` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`diagnostics` [StreamingTraceContext](Omni.Streaming.StreamingTraceContext.md)

`dispatcher` [LocalIoDispatcher](Omni.Streaming.LocalIoDispatcher.md)

## フィールド（Fields）

### <a id="Omni_Streaming_LocalIoSession_Diagnostics"></a> Diagnostics

```csharp
public readonly StreamingTraceContext Diagnostics
```

#### 値（Field Value）

 [StreamingTraceContext](Omni.Streaming.StreamingTraceContext.md)

## プロパティ（Properties）

### <a id="Omni_Streaming_LocalIoSession_OutstandingBytes"></a> OutstandingBytes

```csharp
public long OutstandingBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Streaming_LocalIoSession_SkippedWrites"></a> SkippedWrites

```csharp
public long SkippedWrites { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

## メソッド（Methods）

### <a id="Omni_Streaming_LocalIoSession_Dispose"></a> Dispose\(\)

```csharp
public void Dispose()
```

### <a id="Omni_Streaming_LocalIoSession_Pump"></a> Pump\(\)

```csharp
public void Pump()
```

### <a id="Omni_Streaming_LocalIoSession_SetLimit_System_Int64_"></a> SetLimit\(long\)

```csharp
public void SetLimit(long bytes)
```

#### 引数（Parameters）

`bytes` [long](https://learn.microsoft.com/dotnet/api/system.int64)
