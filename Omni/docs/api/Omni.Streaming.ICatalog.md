# <a id="Omni_Streaming_ICatalog"></a> Interface ICatalog

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

キー → 中身の ID・場所・種別・存在を引く。目録を遅延して読む実装は、<xref href="Omni.Streaming.ICatalog.Pump" data-throw-if-not-resolved="false"></xref> で進める。

```csharp
public interface ICatalog
```

## メソッド（Methods）

### <a id="Omni_Streaming_ICatalog_Lookup_Omni_Streaming_StreamKey__Omni_Streaming_CatalogEntry__"></a> Lookup\(in StreamKey, out CatalogEntry\)

```csharp
CatalogLookup Lookup(in StreamKey key, out CatalogEntry entry)
```

#### 引数（Parameters）

`key` [StreamKey](Omni.Streaming.StreamKey.md)

`entry` [CatalogEntry](Omni.Streaming.CatalogEntry.md)

#### 戻り値（Returns）

 [CatalogLookup](Omni.Streaming.CatalogLookup.md)

### <a id="Omni_Streaming_ICatalog_Pump"></a> Pump\(\)

host の Tick ごとに1回。目録の読み込みを進める(何もしない実装でもよい)。

```csharp
void Pump()
```
