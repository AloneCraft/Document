# <a id="Omni_Streaming_QueuedFileByteSource"></a> Class QueuedFileByteSource

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

同期FileByteSourceを単独I/O workerで呼ぶ。Beginとpollではファイルへ触れない。

```csharp
public sealed class QueuedFileByteSource : IByteSource
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[QueuedFileByteSource](Omni.Streaming.QueuedFileByteSource.md)

#### 実装するインターフェース（Implements）

[IByteSource](Omni.Streaming.IByteSource.md)

## コンストラクター（Constructors）

### <a id="Omni_Streaming_QueuedFileByteSource__ctor_Omni_Streaming_IByteSource_Omni_Streaming_LocalIoSession_"></a> QueuedFileByteSource\(IByteSource, LocalIoSession\)

```csharp
public QueuedFileByteSource(IByteSource source, LocalIoSession session)
```

#### 引数（Parameters）

`source` [IByteSource](Omni.Streaming.IByteSource.md)

`session` [LocalIoSession](Omni.Streaming.LocalIoSession.md)

## プロパティ（Properties）

### <a id="Omni_Streaming_QueuedFileByteSource_Info"></a> Info

```csharp
public ByteSourceInfo Info { get; }
```

#### 値（Property Value）

 [ByteSourceInfo](Omni.Streaming.ByteSourceInfo.md)

## メソッド（Methods）

### <a id="Omni_Streaming_QueuedFileByteSource_Begin_Omni_Streaming_ByteLocation__Omni_Streaming_BufferPool_"></a> Begin\(in ByteLocation, BufferPool\)

location の範囲の取得を始める。結果のバッファは pool から借りる。始められないときは例外ではなく、完了済みの失敗を返してもよい。

```csharp
public IByteRequest Begin(in ByteLocation location, BufferPool pool)
```

#### 引数（Parameters）

`location` [ByteLocation](Omni.Streaming.ByteLocation.md)

`pool` [BufferPool](Omni.Streaming.BufferPool.md)

#### 戻り値（Returns）

 [IByteRequest](Omni.Streaming.IByteRequest.md)
