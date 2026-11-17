# <a id="Omni_Streaming_IClock"></a> Interface IClock

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

時刻の供給元(テストでは仮想時計に替える)。

```csharp
public interface IClock
```

## プロパティ（Properties）

### <a id="Omni_Streaming_IClock_Ticks"></a> Ticks

```csharp
long Ticks { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Streaming_IClock_TicksPerSecond"></a> TicksPerSecond

```csharp
long TicksPerSecond { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)
