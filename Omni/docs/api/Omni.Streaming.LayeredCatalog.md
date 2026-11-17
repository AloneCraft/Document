# <a id="Omni_Streaming_LayeredCatalog"></a> Class LayeredCatalog

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

層ごとに別のカタログへ振り分ける。登録の無い層は Unavailable(取得手段が無い)。

```csharp
public sealed class LayeredCatalog : ICatalog
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[LayeredCatalog](Omni.Streaming.LayeredCatalog.md)

#### 実装するインターフェース（Implements）

[ICatalog](Omni.Streaming.ICatalog.md)

## メソッド（Methods）

### <a id="Omni_Streaming_LayeredCatalog_Lookup_Omni_Streaming_StreamKey__Omni_Streaming_CatalogEntry__"></a> Lookup\(in StreamKey, out CatalogEntry\)

```csharp
public CatalogLookup Lookup(in StreamKey key, out CatalogEntry entry)
```

#### 引数（Parameters）

`key` [StreamKey](Omni.Streaming.StreamKey.md)

`entry` [CatalogEntry](Omni.Streaming.CatalogEntry.md)

#### 戻り値（Returns）

 [CatalogLookup](Omni.Streaming.CatalogLookup.md)

### <a id="Omni_Streaming_LayeredCatalog_Pump"></a> Pump\(\)

host の Tick ごとに1回。目録の読み込みを進める(何もしない実装でもよい)。

```csharp
public void Pump()
```

### <a id="Omni_Streaming_LayeredCatalog_Remove_System_UInt32_"></a> Remove\(uint\)

```csharp
public bool Remove(uint layer)
```

#### 引数（Parameters）

`layer` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_LayeredCatalog_Set_System_UInt32_Omni_Streaming_ICatalog_"></a> Set\(uint, ICatalog\)

```csharp
public void Set(uint layer, ICatalog catalog)
```

#### 引数（Parameters）

`layer` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`catalog` [ICatalog](Omni.Streaming.ICatalog.md)
