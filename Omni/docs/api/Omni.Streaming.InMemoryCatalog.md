# <a id="Omni_Streaming_InMemoryCatalog"></a> Class InMemoryCatalog

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

メモリ上のカタログ(テスト・合成データ・小さなデータ用)。登録したキーは Found、<xref href="Omni.Streaming.InMemoryCatalog.MarkAbsent(Omni.Streaming.StreamKey%40)" data-throw-if-not-resolved="false"></xref> したキーは Absent、
それ以外は <xref href="Omni.Streaming.InMemoryCatalog.UnknownKeys" data-throw-if-not-resolved="false"></xref> の答え(既定は Absent: このカタログが全体の正本という扱い)。
<xref href="Omni.Streaming.InMemoryCatalog.PendingPumps" data-throw-if-not-resolved="false"></xref> 回の Pump が終わるまで、全キーが Pending を返す(目録の遅延読み込みの再現)。

```csharp
public sealed class InMemoryCatalog : ICatalog
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[InMemoryCatalog](Omni.Streaming.InMemoryCatalog.md)

#### 実装するインターフェース（Implements）

[ICatalog](Omni.Streaming.ICatalog.md)

## フィールド（Fields）

### <a id="Omni_Streaming_InMemoryCatalog_PendingPumps"></a> PendingPumps

```csharp
public int PendingPumps
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_InMemoryCatalog_UnknownKeys"></a> UnknownKeys

```csharp
public CatalogLookup UnknownKeys
```

#### 値（Field Value）

 [CatalogLookup](Omni.Streaming.CatalogLookup.md)

## プロパティ（Properties）

### <a id="Omni_Streaming_InMemoryCatalog_LookupCount"></a> LookupCount

```csharp
public int LookupCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_InMemoryCatalog_PumpCount"></a> PumpCount

```csharp
public int PumpCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_Streaming_InMemoryCatalog_Add_Omni_Streaming_StreamKey__Omni_Streaming_CatalogEntry__"></a> Add\(in StreamKey, in CatalogEntry\)

```csharp
public void Add(in StreamKey key, in CatalogEntry entry)
```

#### 引数（Parameters）

`key` [StreamKey](Omni.Streaming.StreamKey.md)

`entry` [CatalogEntry](Omni.Streaming.CatalogEntry.md)

### <a id="Omni_Streaming_InMemoryCatalog_Lookup_Omni_Streaming_StreamKey__Omni_Streaming_CatalogEntry__"></a> Lookup\(in StreamKey, out CatalogEntry\)

```csharp
public CatalogLookup Lookup(in StreamKey key, out CatalogEntry entry)
```

#### 引数（Parameters）

`key` [StreamKey](Omni.Streaming.StreamKey.md)

`entry` [CatalogEntry](Omni.Streaming.CatalogEntry.md)

#### 戻り値（Returns）

 [CatalogLookup](Omni.Streaming.CatalogLookup.md)

### <a id="Omni_Streaming_InMemoryCatalog_MarkAbsent_Omni_Streaming_StreamKey__"></a> MarkAbsent\(in StreamKey\)

```csharp
public void MarkAbsent(in StreamKey key)
```

#### 引数（Parameters）

`key` [StreamKey](Omni.Streaming.StreamKey.md)

### <a id="Omni_Streaming_InMemoryCatalog_Pump"></a> Pump\(\)

host の Tick ごとに1回。目録の読み込みを進める(何もしない実装でもよい)。

```csharp
public void Pump()
```

### <a id="Omni_Streaming_InMemoryCatalog_Remove_Omni_Streaming_StreamKey__"></a> Remove\(in StreamKey\)

```csharp
public bool Remove(in StreamKey key)
```

#### 引数（Parameters）

`key` [StreamKey](Omni.Streaming.StreamKey.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
