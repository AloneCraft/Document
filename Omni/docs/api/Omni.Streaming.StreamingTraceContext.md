# <a id="Omni_Streaming_StreamingTraceContext"></a> Class StreamingTraceContext

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

1Hostの診断識別子と入れ子。Hostと同じ所有threadだけが操作する。

```csharp
public sealed class StreamingTraceContext
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[StreamingTraceContext](Omni.Streaming.StreamingTraceContext.md)

## コンストラクター（Constructors）

### <a id="Omni_Streaming_StreamingTraceContext__ctor_Omni_Streaming_IStreamingDiagnostics_"></a> StreamingTraceContext\(IStreamingDiagnostics\)

```csharp
public StreamingTraceContext(IStreamingDiagnostics sink)
```

#### 引数（Parameters）

`sink` [IStreamingDiagnostics](Omni.Streaming.IStreamingDiagnostics.md)

## フィールド（Fields）

### <a id="Omni_Streaming_StreamingTraceContext_Generation"></a> Generation

```csharp
public long Generation
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Streaming_StreamingTraceContext_HostId"></a> HostId

```csharp
public readonly long HostId
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Streaming_StreamingTraceContext_Owner"></a> Owner

0=先行準備、1=通常。引継ぎ完了後の所有threadで切り替える。

```csharp
public int Owner
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_StreamingTraceContext_Tick"></a> Tick

```csharp
public long Tick
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

## メソッド（Methods）

### <a id="Omni_Streaming_StreamingTraceContext_Fork"></a> Fork\(\)

別thread用の診断context。Host識別子は同じで、入れ子の可変状態を共有しない。

```csharp
public StreamingTraceContext Fork()
```

#### 戻り値（Returns）

 [StreamingTraceContext](Omni.Streaming.StreamingTraceContext.md)

### <a id="Omni_Streaming_StreamingTraceContext_Measure_Omni_Streaming_StreamingPhase_Omni_Streaming_StreamKey_Omni_Streaming_ContentId_System_Int32_Omni_Streaming_ByteLocation_"></a> Measure\(StreamingPhase, StreamKey, ContentId, int, ByteLocation\)

```csharp
public StreamingTraceContext.Scope Measure(StreamingPhase phase, StreamKey key = default, ContentId content = default, int bytes = 0, ByteLocation location = default)
```

#### 引数（Parameters）

`phase` [StreamingPhase](Omni.Streaming.StreamingPhase.md)

`key` [StreamKey](Omni.Streaming.StreamKey.md)

`content` [ContentId](Omni.Streaming.ContentId.md)

`bytes` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`location` [ByteLocation](Omni.Streaming.ByteLocation.md)

#### 戻り値（Returns）

 [StreamingTraceContext](Omni.Streaming.StreamingTraceContext.md).[Scope](Omni.Streaming.StreamingTraceContext.Scope.md)

### <a id="Omni_Streaming_StreamingTraceContext_RecordInterval_Omni_Streaming_StreamingPhase_System_Int64_System_Int64_Omni_Streaming_ContentId_System_Int32_Omni_Streaming_ByteLocation_"></a> RecordInterval\(StreamingPhase, long, long, ContentId, int, ByteLocation\)

非同期要求の待ち区間。Profiler実行時間へは加算せず、共通時刻のCSVへ記録する。

```csharp
public void RecordInterval(StreamingPhase phase, long start, long end, ContentId content, int bytes, ByteLocation location)
```

#### 引数（Parameters）

`phase` [StreamingPhase](Omni.Streaming.StreamingPhase.md)

`start` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`end` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`content` [ContentId](Omni.Streaming.ContentId.md)

`bytes` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`location` [ByteLocation](Omni.Streaming.ByteLocation.md)
