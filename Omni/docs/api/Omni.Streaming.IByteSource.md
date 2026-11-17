# <a id="Omni_Streaming_IByteSource"></a> Interface IByteSource

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

バイト列の取得元(HTTP、ファイル、メモリ、WebSocket、独自 socket など)。

```csharp
public interface IByteSource
```

## プロパティ（Properties）

### <a id="Omni_Streaming_IByteSource_Info"></a> Info

```csharp
ByteSourceInfo Info { get; }
```

#### 値（Property Value）

 [ByteSourceInfo](Omni.Streaming.ByteSourceInfo.md)

## メソッド（Methods）

### <a id="Omni_Streaming_IByteSource_Begin_Omni_Streaming_ByteLocation__Omni_Streaming_BufferPool_"></a> Begin\(in ByteLocation, BufferPool\)

location の範囲の取得を始める。結果のバッファは pool から借りる。始められないときは例外ではなく、完了済みの失敗を返してもよい。

```csharp
IByteRequest Begin(in ByteLocation location, BufferPool pool)
```

#### 引数（Parameters）

`location` [ByteLocation](Omni.Streaming.ByteLocation.md)

`pool` [BufferPool](Omni.Streaming.BufferPool.md)

#### 戻り値（Returns）

 [IByteRequest](Omni.Streaming.IByteRequest.md)
