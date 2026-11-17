# <a id="Omni_Streaming_Formats_PackHeader"></a> Struct PackHeader

Namespace: [Omni.Streaming.Formats](Omni.Streaming.Formats.md)  
Assembly: Omni.Streaming.Formats.dll  

pack ファイルの先頭(固定 128 byte、little endian)。版 1.0:
[0..4) "OTPK"、[4..6) 主版、[6..8) 副版、[8..12) 機能フラグ(上位16bit = 必須。読み手が知らない必須の機能があれば拒否する)、
[12..16) 層、[16] 面(255 = どの面も)、[17] 最小階層、[18] 最大階層、[20..22) 既定の種別、
[24..32) 掲載したマスの数、[32..40) 目録の項目数、[40..48) 保存した中身の数、
[48..56)+[56..64) 根の目録の位置と長さ、[64..72)+[72..80) 付随情報、[80..88)+[88..96) 葉の目録、[96..104)+[104..112) 中身の本体、
[112..116) 1ページの項目数、[120..124) ヘッダー([0..120))の CRC-32。
並び: ヘッダー、根の目録、付随情報、葉の目録、中身の本体。ヘッダー+根の目録+付随情報が 16 KiB 以内なら、先頭1回の取得で足りる。

```csharp
public readonly struct PackHeader
```

## コンストラクター（Constructors）

### <a id="Omni_Streaming_Formats_PackHeader__ctor_System_UInt32_System_UInt32_System_Byte_System_Byte_System_Byte_System_UInt16_System_UInt64_System_UInt64_System_UInt64_System_UInt64_System_UInt64_System_UInt64_System_UInt64_System_UInt64_System_UInt64_System_UInt64_System_UInt64_System_UInt32_"></a> PackHeader\(uint, uint, byte, byte, byte, ushort, ulong, ulong, ulong, ulong, ulong, ulong, ulong, ulong, ulong, ulong, ulong, uint\)

```csharp
public PackHeader(uint flags, uint layer, byte face, byte minLevel, byte maxLevel, ushort defaultKind, ulong tileCount, ulong entryCount, ulong contentCount, ulong rootOffset, ulong rootLength, ulong metadataOffset, ulong metadataLength, ulong leavesOffset, ulong leavesLength, ulong dataOffset, ulong dataLength, uint pageEntries)
```

#### 引数（Parameters）

`flags` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`layer` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`face` [byte](https://learn.microsoft.com/dotnet/api/system.byte)

`minLevel` [byte](https://learn.microsoft.com/dotnet/api/system.byte)

`maxLevel` [byte](https://learn.microsoft.com/dotnet/api/system.byte)

`defaultKind` [ushort](https://learn.microsoft.com/dotnet/api/system.uint16)

`tileCount` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

`entryCount` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

`contentCount` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

`rootOffset` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

`rootLength` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

`metadataOffset` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

`metadataLength` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

`leavesOffset` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

`leavesLength` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

`dataOffset` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

`dataLength` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

`pageEntries` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

## フィールド（Fields）

### <a id="Omni_Streaming_Formats_PackHeader_AnyFace"></a> AnyFace

```csharp
public const byte AnyFace = 255
```

#### 値（Field Value）

 [byte](https://learn.microsoft.com/dotnet/api/system.byte)

### <a id="Omni_Streaming_Formats_PackHeader_ContentCount"></a> ContentCount

```csharp
public readonly ulong ContentCount
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Streaming_Formats_PackHeader_DataLength"></a> DataLength

```csharp
public readonly ulong DataLength
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Streaming_Formats_PackHeader_DataOffset"></a> DataOffset

```csharp
public readonly ulong DataOffset
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Streaming_Formats_PackHeader_DefaultKind"></a> DefaultKind

```csharp
public readonly ushort DefaultKind
```

#### 値（Field Value）

 [ushort](https://learn.microsoft.com/dotnet/api/system.uint16)

### <a id="Omni_Streaming_Formats_PackHeader_EntryCount"></a> EntryCount

```csharp
public readonly ulong EntryCount
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Streaming_Formats_PackHeader_Face"></a> Face

```csharp
public readonly byte Face
```

#### 値（Field Value）

 [byte](https://learn.microsoft.com/dotnet/api/system.byte)

### <a id="Omni_Streaming_Formats_PackHeader_FirstBlockSize"></a> FirstBlockSize

```csharp
public const int FirstBlockSize = 16384
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_Formats_PackHeader_FlagDirectoriesDeflated"></a> FlagDirectoriesDeflated

```csharp
public const uint FlagDirectoriesDeflated = 1
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="Omni_Streaming_Formats_PackHeader_Flags"></a> Flags

```csharp
public readonly uint Flags
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="Omni_Streaming_Formats_PackHeader_Layer"></a> Layer

```csharp
public readonly uint Layer
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="Omni_Streaming_Formats_PackHeader_LeavesLength"></a> LeavesLength

```csharp
public readonly ulong LeavesLength
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Streaming_Formats_PackHeader_LeavesOffset"></a> LeavesOffset

```csharp
public readonly ulong LeavesOffset
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Streaming_Formats_PackHeader_Major"></a> Major

```csharp
public readonly ushort Major
```

#### 値（Field Value）

 [ushort](https://learn.microsoft.com/dotnet/api/system.uint16)

### <a id="Omni_Streaming_Formats_PackHeader_MajorVersion"></a> MajorVersion

```csharp
public const ushort MajorVersion = 1
```

#### 値（Field Value）

 [ushort](https://learn.microsoft.com/dotnet/api/system.uint16)

### <a id="Omni_Streaming_Formats_PackHeader_MaxLevel"></a> MaxLevel

```csharp
public readonly byte MaxLevel
```

#### 値（Field Value）

 [byte](https://learn.microsoft.com/dotnet/api/system.byte)

### <a id="Omni_Streaming_Formats_PackHeader_MetadataLength"></a> MetadataLength

```csharp
public readonly ulong MetadataLength
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Streaming_Formats_PackHeader_MetadataOffset"></a> MetadataOffset

```csharp
public readonly ulong MetadataOffset
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Streaming_Formats_PackHeader_MinLevel"></a> MinLevel

```csharp
public readonly byte MinLevel
```

#### 値（Field Value）

 [byte](https://learn.microsoft.com/dotnet/api/system.byte)

### <a id="Omni_Streaming_Formats_PackHeader_Minor"></a> Minor

```csharp
public readonly ushort Minor
```

#### 値（Field Value）

 [ushort](https://learn.microsoft.com/dotnet/api/system.uint16)

### <a id="Omni_Streaming_Formats_PackHeader_MinorVersion"></a> MinorVersion

```csharp
public const ushort MinorVersion = 0
```

#### 値（Field Value）

 [ushort](https://learn.microsoft.com/dotnet/api/system.uint16)

### <a id="Omni_Streaming_Formats_PackHeader_PageEntries"></a> PageEntries

```csharp
public readonly uint PageEntries
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="Omni_Streaming_Formats_PackHeader_RootLength"></a> RootLength

```csharp
public readonly ulong RootLength
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Streaming_Formats_PackHeader_RootOffset"></a> RootOffset

```csharp
public readonly ulong RootOffset
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Streaming_Formats_PackHeader_Size"></a> Size

```csharp
public const int Size = 128
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_Formats_PackHeader_SupportedRequiredFlags"></a> SupportedRequiredFlags

```csharp
public const uint SupportedRequiredFlags = 0
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="Omni_Streaming_Formats_PackHeader_TileCount"></a> TileCount

```csharp
public readonly ulong TileCount
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

## プロパティ（Properties）

### <a id="Omni_Streaming_Formats_PackHeader_DirectoriesDeflated"></a> DirectoriesDeflated

```csharp
public bool DirectoriesDeflated { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_Streaming_Formats_PackHeader_Parse_System_ReadOnlySpan_System_Byte__"></a> Parse\(ReadOnlySpan<byte\>\)

```csharp
public static PackHeader Parse(ReadOnlySpan<byte> bytes)
```

#### 引数（Parameters）

`bytes` [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[byte](https://learn.microsoft.com/dotnet/api/system.byte)\>

#### 戻り値（Returns）

 [PackHeader](Omni.Streaming.Formats.PackHeader.md)

### <a id="Omni_Streaming_Formats_PackHeader_Write_System_Span_System_Byte__"></a> Write\(Span<byte\>\)

```csharp
public void Write(Span<byte> b)
```

#### 引数（Parameters）

`b` [Span](https://learn.microsoft.com/dotnet/api/system.span\-1)<[byte](https://learn.microsoft.com/dotnet/api/system.byte)\>
