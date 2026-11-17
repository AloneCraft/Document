# <a id="Omni_Streaming_StreamingTraceEvent"></a> Struct StreamingTraceEvent

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

区間は共通Stopwatch時刻。親子区間の時間は重複するため加算しない。

```csharp
public readonly struct StreamingTraceEvent
```

## コンストラクター（Constructors）

### <a id="Omni_Streaming_StreamingTraceEvent__ctor_System_Int64_System_Int64_System_Int64_System_Int64_System_Int64_System_Int64_System_Int32_System_Int32_System_Int32_System_Int32_Omni_Streaming_StreamingPhase_Omni_Streaming_StreamKey_Omni_Streaming_ContentId_System_Int32_System_Int64_"></a> StreamingTraceEvent\(long, long, long, long, long, long, int, int, int, int, StreamingPhase, StreamKey, ContentId, int, long\)

```csharp
public StreamingTraceEvent(long host, long generation, long tick, long start, long end, long parent, int thread, int owner, int depth, int bytes, StreamingPhase phase, StreamKey key, ContentId content, int container = 0, long offset = 0)
```

#### 引数（Parameters）

`host` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`generation` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`tick` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`start` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`end` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`parent` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`thread` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`owner` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`depth` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`bytes` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`phase` [StreamingPhase](Omni.Streaming.StreamingPhase.md)

`key` [StreamKey](Omni.Streaming.StreamKey.md)

`content` [ContentId](Omni.Streaming.ContentId.md)

`container` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`offset` [long](https://learn.microsoft.com/dotnet/api/system.int64)

## フィールド（Fields）

### <a id="Omni_Streaming_StreamingTraceEvent_Bytes"></a> Bytes

```csharp
public readonly int Bytes
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_StreamingTraceEvent_Container"></a> Container

```csharp
public readonly int Container
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_StreamingTraceEvent_Content"></a> Content

```csharp
public readonly ContentId Content
```

#### 値（Field Value）

 [ContentId](Omni.Streaming.ContentId.md)

### <a id="Omni_Streaming_StreamingTraceEvent_Depth"></a> Depth

```csharp
public readonly int Depth
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_StreamingTraceEvent_End"></a> End

```csharp
public readonly long End
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Streaming_StreamingTraceEvent_Generation"></a> Generation

```csharp
public readonly long Generation
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Streaming_StreamingTraceEvent_Host"></a> Host

```csharp
public readonly long Host
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Streaming_StreamingTraceEvent_Key"></a> Key

```csharp
public readonly StreamKey Key
```

#### 値（Field Value）

 [StreamKey](Omni.Streaming.StreamKey.md)

### <a id="Omni_Streaming_StreamingTraceEvent_Offset"></a> Offset

```csharp
public readonly long Offset
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Streaming_StreamingTraceEvent_Owner"></a> Owner

```csharp
public readonly int Owner
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_StreamingTraceEvent_Parent"></a> Parent

```csharp
public readonly long Parent
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Streaming_StreamingTraceEvent_Phase"></a> Phase

```csharp
public readonly StreamingPhase Phase
```

#### 値（Field Value）

 [StreamingPhase](Omni.Streaming.StreamingPhase.md)

### <a id="Omni_Streaming_StreamingTraceEvent_Start"></a> Start

```csharp
public readonly long Start
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Streaming_StreamingTraceEvent_Thread"></a> Thread

```csharp
public readonly int Thread
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_StreamingTraceEvent_Tick"></a> Tick

```csharp
public readonly long Tick
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)
