# <a id="Omni_Streaming_Formats_PackDirectory"></a> Class PackDirectory

Namespace: [Omni.Streaming.Formats](Omni.Streaming.Formats.md)  
Assembly: Omni.Streaming.Formats.dll  

目録の探索(同期の純関数)。<xref href="Omni.Streaming.Formats.PackCatalog" data-throw-if-not-resolved="false"></xref>(非同期)と <xref href="Omni.Streaming.Formats.PackFile" data-throw-if-not-resolved="false"></xref>(同期)が共有する。

```csharp
public static class PackDirectory
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PackDirectory](Omni.Streaming.Formats.PackDirectory.md)

## メソッド（Methods）

### <a id="Omni_Streaming_Formats_PackDirectory_DecodePage_System_ReadOnlySpan_System_Byte__Omni_Streaming_Formats_PackRootEntry__System_Boolean_"></a> DecodePage\(ReadOnlySpan<byte\>, in PackRootEntry, bool\)

保存されたページ(圧縮されていれば展開する)を検証して、項目列のバイト列にする。

```csharp
public static byte[] DecodePage(ReadOnlySpan<byte> stored, in PackRootEntry entry, bool deflated)
```

#### 引数（Parameters）

`stored` [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[byte](https://learn.microsoft.com/dotnet/api/system.byte)\>

`entry` [PackRootEntry](Omni.Streaming.Formats.PackRootEntry.md)

`deflated` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\]

### <a id="Omni_Streaming_Formats_PackDirectory_FindEntry_System_ReadOnlySpan_System_Byte__System_UInt64_Omni_Streaming_Formats_PackEntry__"></a> FindEntry\(ReadOnlySpan<byte\>, ulong, out PackEntry\)

ページ(展開済みの項目列)から、id を含む項目を探す。

```csharp
public static bool FindEntry(ReadOnlySpan<byte> page, ulong id, out PackEntry entry)
```

#### 引数（Parameters）

`page` [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[byte](https://learn.microsoft.com/dotnet/api/system.byte)\>

`id` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

`entry` [PackEntry](Omni.Streaming.Formats.PackEntry.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_Formats_PackDirectory_FindPage_System_Collections_Generic_IReadOnlyList_Omni_Streaming_Formats_PackRootEntry__System_UInt64_"></a> FindPage\(IReadOnlyList<PackRootEntry\>, ulong\)

根の目録のうち、FirstTileId ≤ id の最後の項目の番号。無ければ −1。

```csharp
public static int FindPage(IReadOnlyList<PackRootEntry> root, ulong id)
```

#### 引数（Parameters）

`root` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[PackRootEntry](Omni.Streaming.Formats.PackRootEntry.md)\>

`id` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_Formats_PackDirectory_ParseMetadata_System_ReadOnlySpan_System_Byte__"></a> ParseMetadata\(ReadOnlySpan<byte\>\)

```csharp
public static Dictionary<string, string> ParseMetadata(ReadOnlySpan<byte> bytes)
```

#### 引数（Parameters）

`bytes` [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[byte](https://learn.microsoft.com/dotnet/api/system.byte)\>

#### 戻り値（Returns）

 [Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary\-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Streaming_Formats_PackDirectory_ParseRoot_System_ReadOnlySpan_System_Byte__System_UInt64_"></a> ParseRoot\(ReadOnlySpan<byte\>, ulong\)

```csharp
public static List<PackRootEntry> ParseRoot(ReadOnlySpan<byte> bytes, ulong count)
```

#### 引数（Parameters）

`bytes` [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[byte](https://learn.microsoft.com/dotnet/api/system.byte)\>

`count` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

#### 戻り値（Returns）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[PackRootEntry](Omni.Streaming.Formats.PackRootEntry.md)\>
