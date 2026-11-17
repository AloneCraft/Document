# <a id="Omni_Streaming_IAsyncContentStore"></a> Interface IAsyncContentStore

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

任意の非同期cache読込。完了までPendingを維持し、null結果だけをcache missとする。

```csharp
public interface IAsyncContentStore
```

## プロパティ（Properties）

### <a id="Omni_Streaming_IAsyncContentStore_PendingReads"></a> PendingReads

```csharp
int PendingReads { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_Streaming_IAsyncContentStore_BeginRead_Omni_Streaming_ContentId__"></a> BeginRead\(in ContentId\)

```csharp
IByteRequest BeginRead(in ContentId id)
```

#### 引数（Parameters）

`id` [ContentId](Omni.Streaming.ContentId.md)

#### 戻り値（Returns）

 [IByteRequest](Omni.Streaming.IByteRequest.md)

### <a id="Omni_Streaming_IAsyncContentStore_Pump"></a> Pump\(\)

```csharp
void Pump()
```
