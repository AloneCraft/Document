# <a id="Omni_Streaming_IStreamingDiagnostics"></a> Interface IStreamingDiagnostics

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

任意の計測先。呼出しはHostを単独所有するthread上。実装は例外を投げず、I/Oしない。

```csharp
public interface IStreamingDiagnostics
```

## メソッド（Methods）

### <a id="Omni_Streaming_IStreamingDiagnostics_Begin_Omni_Streaming_StreamingPhase_"></a> Begin\(StreamingPhase\)

```csharp
void Begin(StreamingPhase phase)
```

#### 引数（Parameters）

`phase` [StreamingPhase](Omni.Streaming.StreamingPhase.md)

### <a id="Omni_Streaming_IStreamingDiagnostics_End_Omni_Streaming_StreamingTraceEvent__"></a> End\(in StreamingTraceEvent\)

```csharp
void End(in StreamingTraceEvent sample)
```

#### 引数（Parameters）

`sample` [StreamingTraceEvent](Omni.Streaming.StreamingTraceEvent.md)

### <a id="Omni_Streaming_IStreamingDiagnostics_Record_Omni_Streaming_StreamingTraceEvent__"></a> Record\(in StreamingTraceEvent\)

```csharp
void Record(in StreamingTraceEvent sample)
```

#### 引数（Parameters）

`sample` [StreamingTraceEvent](Omni.Streaming.StreamingTraceEvent.md)
