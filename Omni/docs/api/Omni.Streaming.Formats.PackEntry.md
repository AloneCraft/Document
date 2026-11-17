# <a id="Omni_Streaming_Formats_PackEntry"></a> Struct PackEntry

Namespace: [Omni.Streaming.Formats](Omni.Streaming.Formats.md)  
Assembly: Omni.Streaming.Formats.dll  

葉の目録の1項目(48 byte): ID が TileId から RunLength 個連続するマスが、同じ中身(Offset・Length は本体の先頭から)を指す
(平坦なマスなど同一の中身を1つにまとめる)。中身の ID は取得後の照合に使う。

```csharp
public readonly struct PackEntry
```

## コンストラクター（Constructors）

### <a id="Omni_Streaming_Formats_PackEntry__ctor_System_UInt64_System_UInt32_System_UInt32_System_UInt64_Omni_Streaming_ContentId_System_UInt16_System_UInt16_"></a> PackEntry\(ulong, uint, uint, ulong, ContentId, ushort, ushort\)

```csharp
public PackEntry(ulong tileId, uint runLength, uint length, ulong offset, ContentId content, ushort kind, ushort flags = 0)
```

#### 引数（Parameters）

`tileId` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

`runLength` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`length` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`offset` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

`content` [ContentId](Omni.Streaming.ContentId.md)

`kind` [ushort](https://learn.microsoft.com/dotnet/api/system.uint16)

`flags` [ushort](https://learn.microsoft.com/dotnet/api/system.uint16)

## フィールド（Fields）

### <a id="Omni_Streaming_Formats_PackEntry_Content"></a> Content

```csharp
public readonly ContentId Content
```

#### 値（Field Value）

 [ContentId](Omni.Streaming.ContentId.md)

### <a id="Omni_Streaming_Formats_PackEntry_Flags"></a> Flags

```csharp
public readonly ushort Flags
```

#### 値（Field Value）

 [ushort](https://learn.microsoft.com/dotnet/api/system.uint16)

### <a id="Omni_Streaming_Formats_PackEntry_Kind"></a> Kind

```csharp
public readonly ushort Kind
```

#### 値（Field Value）

 [ushort](https://learn.microsoft.com/dotnet/api/system.uint16)

### <a id="Omni_Streaming_Formats_PackEntry_Length"></a> Length

```csharp
public readonly uint Length
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="Omni_Streaming_Formats_PackEntry_Offset"></a> Offset

```csharp
public readonly ulong Offset
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Streaming_Formats_PackEntry_RunLength"></a> RunLength

```csharp
public readonly uint RunLength
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="Omni_Streaming_Formats_PackEntry_Size"></a> Size

```csharp
public const int Size = 48
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_Formats_PackEntry_TileId"></a> TileId

```csharp
public readonly ulong TileId
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

## メソッド（Methods）

### <a id="Omni_Streaming_Formats_PackEntry_Read_System_ReadOnlySpan_System_Byte__"></a> Read\(ReadOnlySpan<byte\>\)

```csharp
public static PackEntry Read(ReadOnlySpan<byte> b)
```

#### 引数（Parameters）

`b` [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[byte](https://learn.microsoft.com/dotnet/api/system.byte)\>

#### 戻り値（Returns）

 [PackEntry](Omni.Streaming.Formats.PackEntry.md)

### <a id="Omni_Streaming_Formats_PackEntry_Write_System_Span_System_Byte__"></a> Write\(Span<byte\>\)

```csharp
public void Write(Span<byte> b)
```

#### 引数（Parameters）

`b` [Span](https://learn.microsoft.com/dotnet/api/system.span\-1)<[byte](https://learn.microsoft.com/dotnet/api/system.byte)\>
