# <a id="Omni_Streaming_Formats_PackRootEntry"></a> Struct PackRootEntry

Namespace: [Omni.Streaming.Formats](Omni.Streaming.Formats.md)  
Assembly: Omni.Streaming.Formats.dll  

根の目録の1項目(32 byte): 葉のページの最初の ID、ページの位置(葉の目録の先頭から)、圧縮後の長さ、項目数、CRC-32。

```csharp
public readonly struct PackRootEntry
```

## コンストラクター（Constructors）

### <a id="Omni_Streaming_Formats_PackRootEntry__ctor_System_UInt64_System_UInt64_System_UInt32_System_UInt32_System_UInt32_"></a> PackRootEntry\(ulong, ulong, uint, uint, uint\)

```csharp
public PackRootEntry(ulong firstTileId, ulong pageOffset, uint pageLength, uint entryCount, uint crc)
```

#### 引数（Parameters）

`firstTileId` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

`pageOffset` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

`pageLength` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`entryCount` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`crc` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

## フィールド（Fields）

### <a id="Omni_Streaming_Formats_PackRootEntry_Crc"></a> Crc

```csharp
public readonly uint Crc
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="Omni_Streaming_Formats_PackRootEntry_EntryCount"></a> EntryCount

```csharp
public readonly uint EntryCount
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="Omni_Streaming_Formats_PackRootEntry_FirstTileId"></a> FirstTileId

```csharp
public readonly ulong FirstTileId
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Streaming_Formats_PackRootEntry_PageLength"></a> PageLength

```csharp
public readonly uint PageLength
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="Omni_Streaming_Formats_PackRootEntry_PageOffset"></a> PageOffset

```csharp
public readonly ulong PageOffset
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Streaming_Formats_PackRootEntry_Size"></a> Size

```csharp
public const int Size = 32
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_Streaming_Formats_PackRootEntry_Read_System_ReadOnlySpan_System_Byte__"></a> Read\(ReadOnlySpan<byte\>\)

```csharp
public static PackRootEntry Read(ReadOnlySpan<byte> b)
```

#### 引数（Parameters）

`b` [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[byte](https://learn.microsoft.com/dotnet/api/system.byte)\>

#### 戻り値（Returns）

 [PackRootEntry](Omni.Streaming.Formats.PackRootEntry.md)

### <a id="Omni_Streaming_Formats_PackRootEntry_Write_System_Span_System_Byte__"></a> Write\(Span<byte\>\)

```csharp
public void Write(Span<byte> b)
```

#### 引数（Parameters）

`b` [Span](https://learn.microsoft.com/dotnet/api/system.span\-1)<[byte](https://learn.microsoft.com/dotnet/api/system.byte)\>
