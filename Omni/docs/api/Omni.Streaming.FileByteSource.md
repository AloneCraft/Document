# <a id="Omni_Streaming_FileByteSource"></a> Class FileByteSource

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

ファイルから範囲を読む取得元(Container は <xref href="Omni.Streaming.FileByteSource.Add(System.String)" data-throw-if-not-resolved="false"></xref> した順の番号)。読みは呼び出し内で同期的に済ませる
(ローカルの SSD や IndexedDB 上のファイルでは小さな範囲の読みは短い。遅い保存先は別の取得元にする)。

```csharp
public sealed class FileByteSource : IByteSource
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[FileByteSource](Omni.Streaming.FileByteSource.md)

#### 実装するインターフェース（Implements）

[IByteSource](Omni.Streaming.IByteSource.md)

## プロパティ（Properties）

### <a id="Omni_Streaming_FileByteSource_Diagnostics"></a> Diagnostics

```csharp
public StreamingTraceContext Diagnostics { get; set; }
```

#### 値（Property Value）

 [StreamingTraceContext](Omni.Streaming.StreamingTraceContext.md)

### <a id="Omni_Streaming_FileByteSource_Info"></a> Info

```csharp
public ByteSourceInfo Info { get; }
```

#### 値（Property Value）

 [ByteSourceInfo](Omni.Streaming.ByteSourceInfo.md)

## メソッド（Methods）

### <a id="Omni_Streaming_FileByteSource_Add_System_String_"></a> Add\(string\)

```csharp
public int Add(string path)
```

#### 引数（Parameters）

`path` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_FileByteSource_Begin_Omni_Streaming_ByteLocation__Omni_Streaming_BufferPool_"></a> Begin\(in ByteLocation, BufferPool\)

location の範囲の取得を始める。結果のバッファは pool から借りる。始められないときは例外ではなく、完了済みの失敗を返してもよい。

```csharp
public IByteRequest Begin(in ByteLocation location, BufferPool pool)
```

#### 引数（Parameters）

`location` [ByteLocation](Omni.Streaming.ByteLocation.md)

`pool` [BufferPool](Omni.Streaming.BufferPool.md)

#### 戻り値（Returns）

 [IByteRequest](Omni.Streaming.IByteRequest.md)
