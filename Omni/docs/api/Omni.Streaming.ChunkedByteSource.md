# <a id="Omni_Streaming_ChunkedByteSource"></a> Class ChunkedByteSource

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

大きい論理packの範囲readを、最大4MiBの独立ファイルへ変換する。Unity不要の本体。
同じchunkの同時取得を共有し、hash照合後だけ公開する。Unityのmain threadからpollする。

```csharp
public sealed class ChunkedByteSource : IByteSource, IDisposable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[ChunkedByteSource](Omni.Streaming.ChunkedByteSource.md)

#### 実装するインターフェース（Implements）

[IByteSource](Omni.Streaming.IByteSource.md), 
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

## コンストラクター（Constructors）

### <a id="Omni_Streaming_ChunkedByteSource__ctor_Omni_Streaming_IByteSource_System_Collections_Generic_IReadOnlyList_Omni_Streaming_ContentChunk__Omni_Streaming_BufferPool_System_Int64_System_Int32_"></a> ChunkedByteSource\(IByteSource, IReadOnlyList<ContentChunk\>, BufferPool, long, int\)

```csharp
public ChunkedByteSource(IByteSource inner, IReadOnlyList<ContentChunk> chunks, BufferPool chunkPool, long cacheBudgetBytes = 67108864, int maximumConcurrency = 4)
```

#### 引数（Parameters）

`inner` [IByteSource](Omni.Streaming.IByteSource.md)

`chunks` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[ContentChunk](Omni.Streaming.ContentChunk.md)\>

`chunkPool` [BufferPool](Omni.Streaming.BufferPool.md)

`cacheBudgetBytes` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`maximumConcurrency` [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="Omni_Streaming_ChunkedByteSource_CachedBytes"></a> CachedBytes

```csharp
public long CachedBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Streaming_ChunkedByteSource_DownloadedBytes"></a> DownloadedBytes

```csharp
public long DownloadedBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Streaming_ChunkedByteSource_FetchCount"></a> FetchCount

```csharp
public long FetchCount { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Streaming_ChunkedByteSource_InFlight"></a> InFlight

```csharp
public int InFlight { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_ChunkedByteSource_Info"></a> Info

```csharp
public ByteSourceInfo Info { get; }
```

#### 値（Property Value）

 [ByteSourceInfo](Omni.Streaming.ByteSourceInfo.md)

## メソッド（Methods）

### <a id="Omni_Streaming_ChunkedByteSource_Add_System_Int64_System_Int32_System_Collections_Generic_IReadOnlyList_System_Int32__"></a> Add\(long, int, IReadOnlyList<int\>\)

論理packを登録する。先頭からchunkSizeずつ、末尾だけ短い形を厳密に照合する。

```csharp
public int Add(long length, int chunkSize, IReadOnlyList<int> chunkIndices)
```

#### 引数（Parameters）

`length` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`chunkSize` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`chunkIndices` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[int](https://learn.microsoft.com/dotnet/api/system.int32)\>

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_ChunkedByteSource_Begin_Omni_Streaming_ByteLocation__Omni_Streaming_BufferPool_"></a> Begin\(in ByteLocation, BufferPool\)

location の範囲の取得を始める。結果のバッファは pool から借りる。始められないときは例外ではなく、完了済みの失敗を返してもよい。

```csharp
public IByteRequest Begin(in ByteLocation location, BufferPool pool)
```

#### 引数（Parameters）

`location` [ByteLocation](Omni.Streaming.ByteLocation.md)

`pool` [BufferPool](Omni.Streaming.BufferPool.md)

#### 戻り値（Returns）

 [IByteRequest](Omni.Streaming.IByteRequest.md)

### <a id="Omni_Streaming_ChunkedByteSource_Dispose"></a> Dispose\(\)

```csharp
public void Dispose()
```
