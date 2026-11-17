# <a id="Omni_Streaming_Formats_PackCatalog"></a> Class PackCatalog

Namespace: [Omni.Streaming.Formats](Omni.Streaming.Formats.md)  
Assembly: Omni.Streaming.Formats.dll  

pack(.otp)を引くカタログ。目録は遅延して読む: 先頭(ヘッダー+根の目録+付随情報)を1回取得し、キーを引くときに必要な葉のページだけを取得する。
答えられない間は Pending を返し、<xref href="Omni.Streaming.Formats.PackCatalog.Pump" data-throw-if-not-resolved="false"></xref> が取得を進める。ページの取得に失敗したら再試行し、使い切ると一定時間 Unavailable を返す。
面・層・階層の範囲が合わないキーは Absent(この pack に無い)。目録の項目が無いキーも Absent(= 平坦などで親から導けるマス)。

```csharp
public sealed class PackCatalog : ICatalog
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PackCatalog](Omni.Streaming.Formats.PackCatalog.md)

#### 実装するインターフェース（Implements）

[ICatalog](Omni.Streaming.ICatalog.md)

## コンストラクター（Constructors）

### <a id="Omni_Streaming_Formats_PackCatalog__ctor_Omni_Streaming_IByteSource_Omni_Streaming_BufferPool_System_Int32_System_Int64_Omni_Streaming_IClock_System_Int32_System_Int32_System_Int32_System_Double_System_Double_"></a> PackCatalog\(IByteSource, BufferPool, int, long, IClock, int, int, int, double, double\)

```csharp
public PackCatalog(IByteSource source, BufferPool pool, int container, long knownLength = -1, IClock clock = null, int maximumCachedPages = 64, int maximumConcurrentFetches = 4, int maximumAttempts = 4, double retrySeconds = 0.5, double failedCooldownSeconds = 10)
```

#### 引数（Parameters）

`source` [IByteSource](Omni.Streaming.IByteSource.md)

`pool` [BufferPool](Omni.Streaming.BufferPool.md)

`container` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`knownLength` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`clock` [IClock](Omni.Streaming.IClock.md)

`maximumCachedPages` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`maximumConcurrentFetches` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`maximumAttempts` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`retrySeconds` [double](https://learn.microsoft.com/dotnet/api/system.double)

`failedCooldownSeconds` [double](https://learn.microsoft.com/dotnet/api/system.double)

## プロパティ（Properties）

### <a id="Omni_Streaming_Formats_PackCatalog_CachedPages"></a> CachedPages

```csharp
public int CachedPages { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_Formats_PackCatalog_Error"></a> Error

```csharp
public string Error { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Streaming_Formats_PackCatalog_Header"></a> Header

State が Ready のときだけ有効。

```csharp
public PackHeader Header { get; }
```

#### 値（Property Value）

 [PackHeader](Omni.Streaming.Formats.PackHeader.md)

### <a id="Omni_Streaming_Formats_PackCatalog_Metadata"></a> Metadata

```csharp
public IReadOnlyDictionary<string, string> Metadata { get; }
```

#### 値（Property Value）

 [IReadOnlyDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlydictionary\-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Streaming_Formats_PackCatalog_PageFetches"></a> PageFetches

```csharp
public int PageFetches { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_Formats_PackCatalog_State"></a> State

```csharp
public PackCatalog.InitState State { get; }
```

#### 値（Property Value）

 [PackCatalog](Omni.Streaming.Formats.PackCatalog.md).[InitState](Omni.Streaming.Formats.PackCatalog.InitState.md)

## メソッド（Methods）

### <a id="Omni_Streaming_Formats_PackCatalog_Lookup_Omni_Streaming_StreamKey__Omni_Streaming_CatalogEntry__"></a> Lookup\(in StreamKey, out CatalogEntry\)

```csharp
public CatalogLookup Lookup(in StreamKey key, out CatalogEntry entry)
```

#### 引数（Parameters）

`key` [StreamKey](Omni.Streaming.StreamKey.md)

`entry` [CatalogEntry](Omni.Streaming.CatalogEntry.md)

#### 戻り値（Returns）

 [CatalogLookup](Omni.Streaming.CatalogLookup.md)

### <a id="Omni_Streaming_Formats_PackCatalog_Pump"></a> Pump\(\)

host の Tick ごとに1回。目録の読み込みを進める(何もしない実装でもよい)。

```csharp
public void Pump()
```
