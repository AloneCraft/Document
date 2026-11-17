# <a id="Omni_Streaming_Formats_PackSetCatalog"></a> Class PackSetCatalog

Namespace: [Omni.Streaming.Formats](Omni.Streaming.Formats.md)  
Assembly: Omni.Streaming.Formats.dll  

面ごとに分けた pack(層×面で1ファイル)を、キーの層と面で引き分ける。登録の無い(層, 面)は Unavailable(取得手段が無い)。
面を指定しない pack(<xref href="Omni.Streaming.Formats.PackHeader.AnyFace" data-throw-if-not-resolved="false"></xref>)は、face に −1 で登録する。

```csharp
public sealed class PackSetCatalog : ICatalog
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PackSetCatalog](Omni.Streaming.Formats.PackSetCatalog.md)

#### 実装するインターフェース（Implements）

[ICatalog](Omni.Streaming.ICatalog.md)

## メソッド（Methods）

### <a id="Omni_Streaming_Formats_PackSetCatalog_Add_System_UInt32_System_Int32_Omni_Streaming_ICatalog_"></a> Add\(uint, int, ICatalog\)

```csharp
public void Add(uint layer, int face, ICatalog catalog)
```

#### 引数（Parameters）

`layer` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`face` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`catalog` [ICatalog](Omni.Streaming.ICatalog.md)

### <a id="Omni_Streaming_Formats_PackSetCatalog_Lookup_Omni_Streaming_StreamKey__Omni_Streaming_CatalogEntry__"></a> Lookup\(in StreamKey, out CatalogEntry\)

```csharp
public CatalogLookup Lookup(in StreamKey key, out CatalogEntry entry)
```

#### 引数（Parameters）

`key` [StreamKey](Omni.Streaming.StreamKey.md)

`entry` [CatalogEntry](Omni.Streaming.CatalogEntry.md)

#### 戻り値（Returns）

 [CatalogLookup](Omni.Streaming.CatalogLookup.md)

### <a id="Omni_Streaming_Formats_PackSetCatalog_Pump"></a> Pump\(\)

host の Tick ごとに1回。目録の読み込みを進める(何もしない実装でもよい)。

```csharp
public void Pump()
```
