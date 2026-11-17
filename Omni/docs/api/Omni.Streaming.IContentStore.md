# <a id="Omni_Streaming_IContentStore"></a> Interface IContentStore

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

内容 ID でバイト列を保存・取得する(メモリ、ファイルなど)。段を重ねられる(<xref href="Omni.Streaming.TieredStore" data-throw-if-not-resolved="false"></xref>)。

```csharp
public interface IContentStore
```

## プロパティ（Properties）

### <a id="Omni_Streaming_IContentStore_RequiresVerification"></a> RequiresVerification

取り出した中身を host が内容 ID で照合する必要があるか(ディスクなど、書き込み後に壊れうる保存先は true)。
host が検証してから入れたデータだけを持つメモリ上のストアは false。照合に失敗した中身は <xref href="Omni.Streaming.IContentStore.Remove(Omni.Streaming.ContentId%40)" data-throw-if-not-resolved="false"></xref> して取り直す。

```csharp
bool RequiresVerification { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_IContentStore_UsedBytes"></a> UsedBytes

```csharp
long UsedBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

## メソッド（Methods）

### <a id="Omni_Streaming_IContentStore_Contains_Omni_Streaming_ContentId__"></a> Contains\(in ContentId\)

```csharp
bool Contains(in ContentId id)
```

#### 引数（Parameters）

`id` [ContentId](Omni.Streaming.ContentId.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_IContentStore_Put_Omni_Streaming_ContentId__Omni_Streaming_PooledBuffer_"></a> Put\(in ContentId, PooledBuffer\)

保存する。buffer の参照は呼び手のもので、ストア自身が必要なら Retain する。失敗(容量など)は黙って捨ててよい(キャッシュなので)。

```csharp
void Put(in ContentId id, PooledBuffer buffer)
```

#### 引数（Parameters）

`id` [ContentId](Omni.Streaming.ContentId.md)

`buffer` [PooledBuffer](Omni.Streaming.PooledBuffer.md)

### <a id="Omni_Streaming_IContentStore_Remove_Omni_Streaming_ContentId__"></a> Remove\(in ContentId\)

消す(壊れた中身の除去など)。無ければ false。取り出し済みのバッファは、持ち主が戻すまで生きる。

```csharp
bool Remove(in ContentId id)
```

#### 引数（Parameters）

`id` [ContentId](Omni.Streaming.ContentId.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_IContentStore_TryGet_Omni_Streaming_ContentId__Omni_Streaming_PooledBuffer__"></a> TryGet\(in ContentId, out PooledBuffer\)

あれば true。buffer は呼び手が <xref href="Omni.Streaming.PooledBuffer.Release" data-throw-if-not-resolved="false"></xref> する(参照が1つ増えている)。

```csharp
bool TryGet(in ContentId id, out PooledBuffer buffer)
```

#### 引数（Parameters）

`id` [ContentId](Omni.Streaming.ContentId.md)

`buffer` [PooledBuffer](Omni.Streaming.PooledBuffer.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
