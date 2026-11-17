# <a id="Omni_Streaming_AsyncLocalContentStore"></a> Class AsyncLocalContentStore

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

MemoryStoreはHost所有thread、diskはI/O workerだけが操作する。cacheの失敗はmissとして回復する。

```csharp
public sealed class AsyncLocalContentStore : IContentStore, IAsyncContentStore
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[AsyncLocalContentStore](Omni.Streaming.AsyncLocalContentStore.md)

#### 実装するインターフェース（Implements）

[IContentStore](Omni.Streaming.IContentStore.md), 
[IAsyncContentStore](Omni.Streaming.IAsyncContentStore.md)

## コンストラクター（Constructors）

### <a id="Omni_Streaming_AsyncLocalContentStore__ctor_Omni_Streaming_MemoryStore_Omni_Streaming_IContentStore_Omni_Streaming_LocalIoSession_System_Collections_Generic_IEnumerable_System_Collections_Generic_KeyValuePair_Omni_Streaming_ContentId_System_Int64___"></a> AsyncLocalContentStore\(MemoryStore, IContentStore, LocalIoSession, IEnumerable<KeyValuePair<ContentId, long\>\>\)

```csharp
public AsyncLocalContentStore(MemoryStore memory, IContentStore disk, LocalIoSession session, IEnumerable<KeyValuePair<ContentId, long>> inventory = null)
```

#### 引数（Parameters）

`memory` [MemoryStore](Omni.Streaming.MemoryStore.md)

`disk` [IContentStore](Omni.Streaming.IContentStore.md)

`session` [LocalIoSession](Omni.Streaming.LocalIoSession.md)

`inventory` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<[KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair\-2)<[ContentId](Omni.Streaming.ContentId.md), [long](https://learn.microsoft.com/dotnet/api/system.int64)\>\>

## プロパティ（Properties）

### <a id="Omni_Streaming_AsyncLocalContentStore_PendingReads"></a> PendingReads

```csharp
public int PendingReads { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_AsyncLocalContentStore_RequiresVerification"></a> RequiresVerification

取り出した中身を host が内容 ID で照合する必要があるか(ディスクなど、書き込み後に壊れうる保存先は true)。
host が検証してから入れたデータだけを持つメモリ上のストアは false。照合に失敗した中身は <xref href="Omni.Streaming.IContentStore.Remove(Omni.Streaming.ContentId%40)" data-throw-if-not-resolved="false"></xref> して取り直す。

```csharp
public bool RequiresVerification { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_AsyncLocalContentStore_UsedBytes"></a> UsedBytes

```csharp
public long UsedBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

## メソッド（Methods）

### <a id="Omni_Streaming_AsyncLocalContentStore_BeginRead_Omni_Streaming_ContentId__"></a> BeginRead\(in ContentId\)

```csharp
public IByteRequest BeginRead(in ContentId id)
```

#### 引数（Parameters）

`id` [ContentId](Omni.Streaming.ContentId.md)

#### 戻り値（Returns）

 [IByteRequest](Omni.Streaming.IByteRequest.md)

### <a id="Omni_Streaming_AsyncLocalContentStore_Contains_Omni_Streaming_ContentId__"></a> Contains\(in ContentId\)

```csharp
public bool Contains(in ContentId id)
```

#### 引数（Parameters）

`id` [ContentId](Omni.Streaming.ContentId.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_AsyncLocalContentStore_Pump"></a> Pump\(\)

```csharp
public void Pump()
```

### <a id="Omni_Streaming_AsyncLocalContentStore_Put_Omni_Streaming_ContentId__Omni_Streaming_PooledBuffer_"></a> Put\(in ContentId, PooledBuffer\)

保存する。buffer の参照は呼び手のもので、ストア自身が必要なら Retain する。失敗(容量など)は黙って捨ててよい(キャッシュなので)。

```csharp
public void Put(in ContentId id, PooledBuffer buffer)
```

#### 引数（Parameters）

`id` [ContentId](Omni.Streaming.ContentId.md)

`buffer` [PooledBuffer](Omni.Streaming.PooledBuffer.md)

### <a id="Omni_Streaming_AsyncLocalContentStore_Remove_Omni_Streaming_ContentId__"></a> Remove\(in ContentId\)

消す(壊れた中身の除去など)。無ければ false。取り出し済みのバッファは、持ち主が戻すまで生きる。

```csharp
public bool Remove(in ContentId id)
```

#### 引数（Parameters）

`id` [ContentId](Omni.Streaming.ContentId.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_AsyncLocalContentStore_TryGet_Omni_Streaming_ContentId__Omni_Streaming_PooledBuffer__"></a> TryGet\(in ContentId, out PooledBuffer\)

あれば true。buffer は呼び手が <xref href="Omni.Streaming.PooledBuffer.Release" data-throw-if-not-resolved="false"></xref> する(参照が1つ増えている)。

```csharp
public bool TryGet(in ContentId id, out PooledBuffer buffer)
```

#### 引数（Parameters）

`id` [ContentId](Omni.Streaming.ContentId.md)

`buffer` [PooledBuffer](Omni.Streaming.PooledBuffer.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
