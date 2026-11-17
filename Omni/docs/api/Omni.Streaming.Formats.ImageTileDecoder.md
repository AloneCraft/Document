# <a id="Omni_Streaming_Formats_ImageTileDecoder"></a> Class ImageTileDecoder

Namespace: [Omni.Streaming.Formats](Omni.Streaming.Formats.md)  
Assembly: Omni.Streaming.Formats.dll  

種別 <xref href="Omni.Streaming.Formats.ImageTileCodec.Kind" data-throw-if-not-resolved="false"></xref> の展開器。

```csharp
public sealed class ImageTileDecoder : IPayloadDecoder
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[ImageTileDecoder](Omni.Streaming.Formats.ImageTileDecoder.md)

#### 実装するインターフェース（Implements）

[IPayloadDecoder](Omni.Streaming.IPayloadDecoder.md)

## コンストラクター（Constructors）

### <a id="Omni_Streaming_Formats_ImageTileDecoder__ctor_System_Int32_"></a> ImageTileDecoder\(int\)

```csharp
public ImageTileDecoder(int estimatedPixels = 16384)
```

#### 引数（Parameters）

`estimatedPixels` [int](https://learn.microsoft.com/dotnet/api/system.int32)

1 タイルの画素数の見積もり(メモリ予算の判断用。既定は 128×128)。

## プロパティ（Properties）

### <a id="Omni_Streaming_Formats_ImageTileDecoder_Kind"></a> Kind

```csharp
public ushort Kind { get; }
```

#### 値（Property Value）

 [ushort](https://learn.microsoft.com/dotnet/api/system.uint16)

## メソッド（Methods）

### <a id="Omni_Streaming_Formats_ImageTileDecoder_Decode_System_ReadOnlyMemory_System_Byte__Omni_Streaming_StreamKey__"></a> Decode\(ReadOnlyMemory<byte\>, in StreamKey\)

encoded は展開の間だけ有効(保持しない)。失敗は例外で知らせる(その中身は再試行しても同じ結果なので、host は再試行しない)。

```csharp
public IDecodedPayload Decode(ReadOnlyMemory<byte> encoded, in StreamKey key)
```

#### 引数（Parameters）

`encoded` [ReadOnlyMemory](https://learn.microsoft.com/dotnet/api/system.readonlymemory\-1)<[byte](https://learn.microsoft.com/dotnet/api/system.byte)\>

`key` [StreamKey](Omni.Streaming.StreamKey.md)

#### 戻り値（Returns）

 [IDecodedPayload](Omni.Streaming.IDecodedPayload.md)

### <a id="Omni_Streaming_Formats_ImageTileDecoder_EstimateDecodedSize_System_Int32_"></a> EstimateDecodedSize\(int\)

展開後の大きさの見積もり(メモリ予算の判断に使う。厳密でなくてよい)。

```csharp
public long EstimateDecodedSize(int encodedLength)
```

#### 引数（Parameters）

`encodedLength` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)
