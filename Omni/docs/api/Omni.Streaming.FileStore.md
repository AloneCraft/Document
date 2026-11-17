# <a id="Omni_Streaming_FileStore"></a> Class FileStore

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

ディスク(またはブラウザの IndexedDB を背にしたファイルシステム)上の内容ストア。中身は内容 ID を名前にしたファイルで、
書き込みは一時ファイルに書いてから名前を付け替える(途中で止まっても壊れたファイルを名乗らない)。
合計バイト数が予算を超えたら、使われていない古いファイルから消す。起動時にディレクトリを1回数え上げて索引を作る。
書き込み後に壊れうる保存先なので <xref href="Omni.Streaming.FileStore.RequiresVerification" data-throw-if-not-resolved="false"></xref> は true(host が取り出し時に ID を照合する)。
保存の失敗(容量不足・書き込み禁止など)は黙って捨てる(キャッシュなので)。<xref href="Omni.Streaming.FileStore.Failures" data-throw-if-not-resolved="false"></xref> で数える。

```csharp
public sealed class FileStore : IContentStore
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[FileStore](Omni.Streaming.FileStore.md)

#### 実装するインターフェース（Implements）

[IContentStore](Omni.Streaming.IContentStore.md)

## コンストラクター（Constructors）

### <a id="Omni_Streaming_FileStore__ctor_System_String_System_Int64_Omni_Streaming_BufferPool_System_Action_Omni_Streaming_StreamingTraceContext_"></a> FileStore\(string, long, BufferPool, Action, StreamingTraceContext\)

```csharp
public FileStore(string directory, long budgetBytes, BufferPool pool, Action changed = null, StreamingTraceContext diagnostics = null)
```

#### 引数（Parameters）

`directory` [string](https://learn.microsoft.com/dotnet/api/system.string)

`budgetBytes` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`pool` [BufferPool](Omni.Streaming.BufferPool.md)

`changed` [Action](https://learn.microsoft.com/dotnet/api/system.action)

ファイルを書いた・消した後に呼ぶ(WebGL でファイルシステムの保存を促す、など。呼び手が間引く)。

`diagnostics` [StreamingTraceContext](Omni.Streaming.StreamingTraceContext.md)

## プロパティ（Properties）

### <a id="Omni_Streaming_FileStore_Count"></a> Count

```csharp
public int Count { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_FileStore_Diagnostics"></a> Diagnostics

```csharp
public StreamingTraceContext Diagnostics { get; set; }
```

#### 値（Property Value）

 [StreamingTraceContext](Omni.Streaming.StreamingTraceContext.md)

### <a id="Omni_Streaming_FileStore_DirectoryPath"></a> DirectoryPath

```csharp
public string DirectoryPath { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Streaming_FileStore_Evictions"></a> Evictions

```csharp
public long Evictions { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Streaming_FileStore_Failures"></a> Failures

```csharp
public long Failures { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Streaming_FileStore_RequiresVerification"></a> RequiresVerification

取り出した中身を host が内容 ID で照合する必要があるか(ディスクなど、書き込み後に壊れうる保存先は true)。
host が検証してから入れたデータだけを持つメモリ上のストアは false。照合に失敗した中身は <xref href="Omni.Streaming.IContentStore.Remove(Omni.Streaming.ContentId%40)" data-throw-if-not-resolved="false"></xref> して取り直す。

```csharp
public bool RequiresVerification { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_FileStore_UsedBytes"></a> UsedBytes

```csharp
public long UsedBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

## メソッド（Methods）

### <a id="Omni_Streaming_FileStore_Clear"></a> Clear\(\)

全部消す(試験台の「ストアを空にする」など)。消した数を返す。

```csharp
public int Clear()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_FileStore_Contains_Omni_Streaming_ContentId__"></a> Contains\(in ContentId\)

```csharp
public bool Contains(in ContentId id)
```

#### 引数（Parameters）

`id` [ContentId](Omni.Streaming.ContentId.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_FileStore_Put_Omni_Streaming_ContentId__Omni_Streaming_PooledBuffer_"></a> Put\(in ContentId, PooledBuffer\)

保存する。buffer の参照は呼び手のもので、ストア自身が必要なら Retain する。失敗(容量など)は黙って捨ててよい(キャッシュなので)。

```csharp
public void Put(in ContentId id, PooledBuffer buffer)
```

#### 引数（Parameters）

`id` [ContentId](Omni.Streaming.ContentId.md)

`buffer` [PooledBuffer](Omni.Streaming.PooledBuffer.md)

### <a id="Omni_Streaming_FileStore_Remove_Omni_Streaming_ContentId__"></a> Remove\(in ContentId\)

消す(壊れた中身の除去など)。無ければ false。取り出し済みのバッファは、持ち主が戻すまで生きる。

```csharp
public bool Remove(in ContentId id)
```

#### 引数（Parameters）

`id` [ContentId](Omni.Streaming.ContentId.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_FileStore_SnapshotInventory"></a> SnapshotInventory\(\)

worker開始前に取得する索引snapshot。以後のdisk操作は同じworkerだけが行う。

```csharp
public List<KeyValuePair<ContentId, long>> SnapshotInventory()
```

#### 戻り値（Returns）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair\-2)<[ContentId](Omni.Streaming.ContentId.md), [long](https://learn.microsoft.com/dotnet/api/system.int64)\>\>

### <a id="Omni_Streaming_FileStore_TryGet_Omni_Streaming_ContentId__Omni_Streaming_PooledBuffer__"></a> TryGet\(in ContentId, out PooledBuffer\)

あれば true。buffer は呼び手が <xref href="Omni.Streaming.PooledBuffer.Release" data-throw-if-not-resolved="false"></xref> する(参照が1つ増えている)。

```csharp
public bool TryGet(in ContentId id, out PooledBuffer buffer)
```

#### 引数（Parameters）

`id` [ContentId](Omni.Streaming.ContentId.md)

`buffer` [PooledBuffer](Omni.Streaming.PooledBuffer.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
