# <a id="Omni_Streaming_MemoryStore"></a> Class MemoryStore

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

メモリ上の内容ストア。合計バイト数の予算を超えたら、使われていない(最後に触れたのが古い)ものから外す。
外すのはストア自身の参照だけで、利用者が取り出して持っているバッファは、その利用者が戻すまで生きる。

```csharp
public sealed class MemoryStore : IContentStore
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[MemoryStore](Omni.Streaming.MemoryStore.md)

#### 実装するインターフェース（Implements）

[IContentStore](Omni.Streaming.IContentStore.md)

## コンストラクター（Constructors）

### <a id="Omni_Streaming_MemoryStore__ctor_System_Int64_"></a> MemoryStore\(long\)

```csharp
public MemoryStore(long budgetBytes)
```

#### 引数（Parameters）

`budgetBytes` [long](https://learn.microsoft.com/dotnet/api/system.int64)

## プロパティ（Properties）

### <a id="Omni_Streaming_MemoryStore_Count"></a> Count

```csharp
public int Count { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_MemoryStore_Evictions"></a> Evictions

```csharp
public long Evictions { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Streaming_MemoryStore_RequiresVerification"></a> RequiresVerification

取り出した中身を host が内容 ID で照合する必要があるか(ディスクなど、書き込み後に壊れうる保存先は true)。
host が検証してから入れたデータだけを持つメモリ上のストアは false。照合に失敗した中身は <xref href="Omni.Streaming.IContentStore.Remove(Omni.Streaming.ContentId%40)" data-throw-if-not-resolved="false"></xref> して取り直す。

```csharp
public bool RequiresVerification { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_MemoryStore_UsedBytes"></a> UsedBytes

```csharp
public long UsedBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

## メソッド（Methods）

### <a id="Omni_Streaming_MemoryStore_Clear"></a> Clear\(\)

```csharp
public void Clear()
```

### <a id="Omni_Streaming_MemoryStore_Contains_Omni_Streaming_ContentId__"></a> Contains\(in ContentId\)

```csharp
public bool Contains(in ContentId id)
```

#### 引数（Parameters）

`id` [ContentId](Omni.Streaming.ContentId.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_MemoryStore_Put_Omni_Streaming_ContentId__Omni_Streaming_PooledBuffer_"></a> Put\(in ContentId, PooledBuffer\)

保存する。buffer の参照は呼び手のもので、ストア自身が必要なら Retain する。失敗(容量など)は黙って捨ててよい(キャッシュなので)。

```csharp
public void Put(in ContentId id, PooledBuffer buffer)
```

#### 引数（Parameters）

`id` [ContentId](Omni.Streaming.ContentId.md)

`buffer` [PooledBuffer](Omni.Streaming.PooledBuffer.md)

### <a id="Omni_Streaming_MemoryStore_Remove_Omni_Streaming_ContentId__"></a> Remove\(in ContentId\)

消す(壊れた中身の除去など)。無ければ false。取り出し済みのバッファは、持ち主が戻すまで生きる。

```csharp
public bool Remove(in ContentId id)
```

#### 引数（Parameters）

`id` [ContentId](Omni.Streaming.ContentId.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_MemoryStore_SetBudget_System_Int64_"></a> SetBudget\(long\)

所有threadから予算を変更する。既存leaseは維持する。

```csharp
public void SetBudget(long bytes)
```

#### 引数（Parameters）

`bytes` [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Streaming_MemoryStore_TryGet_Omni_Streaming_ContentId__Omni_Streaming_PooledBuffer__"></a> TryGet\(in ContentId, out PooledBuffer\)

あれば true。buffer は呼び手が <xref href="Omni.Streaming.PooledBuffer.Release" data-throw-if-not-resolved="false"></xref> する(参照が1つ増えている)。

```csharp
public bool TryGet(in ContentId id, out PooledBuffer buffer)
```

#### 引数（Parameters）

`id` [ContentId](Omni.Streaming.ContentId.md)

`buffer` [PooledBuffer](Omni.Streaming.PooledBuffer.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
