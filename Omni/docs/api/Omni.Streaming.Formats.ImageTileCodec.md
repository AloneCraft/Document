# <a id="Omni_Streaming_Formats_ImageTileCodec"></a> Class ImageTileCodec

Namespace: [Omni.Streaming.Formats](Omni.Streaming.Formats.md)  
Assembly: Omni.Streaming.Formats.dll  

画像タイルの中身の形式 "IMT1": [0..4) "IMT1"、[4..6) 幅、[6..8) 高さ、[8] 形式、[9..12) 予備、以降は画素のデータ(形式のまま)。

```csharp
public static class ImageTileCodec
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[ImageTileCodec](Omni.Streaming.Formats.ImageTileCodec.md)

## フィールド（Fields）

### <a id="Omni_Streaming_Formats_ImageTileCodec_Kind"></a> Kind

カタログの項目の種別(<xref href="Omni.Streaming.IPayloadDecoder.Kind" data-throw-if-not-resolved="false"></xref>)。

```csharp
public const ushort Kind = 258
```

#### 値（Field Value）

 [ushort](https://learn.microsoft.com/dotnet/api/system.uint16)

## メソッド（Methods）

### <a id="Omni_Streaming_Formats_ImageTileCodec_Decode_System_ReadOnlySpan_System_Byte__"></a> Decode\(ReadOnlySpan<byte\>\)

```csharp
public static ImageTile Decode(ReadOnlySpan<byte> bytes)
```

#### 引数（Parameters）

`bytes` [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[byte](https://learn.microsoft.com/dotnet/api/system.byte)\>

#### 戻り値（Returns）

 [ImageTile](Omni.Streaming.Formats.ImageTile.md)

### <a id="Omni_Streaming_Formats_ImageTileCodec_Encode_System_Int32_System_Int32_Omni_Streaming_Formats_ImageTileFormat_System_Byte___"></a> Encode\(int, int, ImageTileFormat, byte\[\]\)

```csharp
public static byte[] Encode(int width, int height, ImageTileFormat format, byte[] data)
```

#### 引数（Parameters）

`width` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`height` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`format` [ImageTileFormat](Omni.Streaming.Formats.ImageTileFormat.md)

`data` [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\]

#### 戻り値（Returns）

 [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\]
