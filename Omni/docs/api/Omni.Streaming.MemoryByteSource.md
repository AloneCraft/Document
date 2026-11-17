# <a id="Omni_Streaming_MemoryByteSource"></a> Class MemoryByteSource

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

メモリ上のコンテナ(Container は登録順の番号)から範囲を返す取得元。事前に読み込んだデータの一括利用(プリロード)・テスト・合成データ用。

```csharp
public sealed class MemoryByteSource : IByteSource
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[MemoryByteSource](Omni.Streaming.MemoryByteSource.md)

#### 実装するインターフェース（Implements）

[IByteSource](Omni.Streaming.IByteSource.md)

## プロパティ（Properties）

### <a id="Omni_Streaming_MemoryByteSource_Info"></a> Info

```csharp
public ByteSourceInfo Info { get; }
```

#### 値（Property Value）

 [ByteSourceInfo](Omni.Streaming.ByteSourceInfo.md)

## メソッド（Methods）

### <a id="Omni_Streaming_MemoryByteSource_Add_System_ReadOnlyMemory_System_Byte__"></a> Add\(ReadOnlyMemory<byte\>\)

コンテナを追加し、その番号を返す。

```csharp
public int Add(ReadOnlyMemory<byte> data)
```

#### 引数（Parameters）

`data` [ReadOnlyMemory](https://learn.microsoft.com/dotnet/api/system.readonlymemory\-1)<[byte](https://learn.microsoft.com/dotnet/api/system.byte)\>

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_MemoryByteSource_Begin_Omni_Streaming_ByteLocation__Omni_Streaming_BufferPool_"></a> Begin\(in ByteLocation, BufferPool\)

location の範囲の取得を始める。結果のバッファは pool から借りる。始められないときは例外ではなく、完了済みの失敗を返してもよい。

```csharp
public IByteRequest Begin(in ByteLocation location, BufferPool pool)
```

#### 引数（Parameters）

`location` [ByteLocation](Omni.Streaming.ByteLocation.md)

`pool` [BufferPool](Omni.Streaming.BufferPool.md)

#### 戻り値（Returns）

 [IByteRequest](Omni.Streaming.IByteRequest.md)
