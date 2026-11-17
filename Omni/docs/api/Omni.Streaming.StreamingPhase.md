# <a id="Omni_Streaming_StreamingPhase"></a> Enum StreamingPhase

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

Unity非依存のStreaming処理区間。値はCSVの対応表にも保存する。

```csharp
public enum StreamingPhase
```

## フィールド（Fields）

`BeginFetch = 6` 

`CacheRead = 16` 

`CacheScan = 19` 

`CacheTrim = 18` 

`CacheWrite = 17` 

`Catalog = 1` 

`Decode = 12` 

`DecodeReady = 10` 

`EvaluateWanted = 4` 

`Evict = 13` 

`IoAdmissionWait = 20` 

`IoQueueWait = 21` 

`IoRecoveryWait = 22` 

`LocalRead = 15` 

`MergeInterests = 2` 

`NotifyInterest = 3` 

`PollTransfers = 7` 

`Prune = 14` 

`ScheduleFetches = 5` 

`StoreGet = 11` 

`StorePut = 9` 

`Tick = 0` 

`Verify = 8`
