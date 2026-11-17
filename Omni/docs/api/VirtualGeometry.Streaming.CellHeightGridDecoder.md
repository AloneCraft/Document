# <a id="VirtualGeometry_Streaming_CellHeightGridDecoder"></a> Class CellHeightGridDecoder

Namespace: [VirtualGeometry.Streaming](VirtualGeometry.Streaming.md)  
Assembly: Omni.VirtualGeometry.Streaming.dll  

種別 <xref href="VirtualGeometry.Streaming.CellHeightGridCodec.Kind" data-throw-if-not-resolved="false"></xref> の展開器。

```csharp
public sealed class CellHeightGridDecoder : IPayloadDecoder
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[CellHeightGridDecoder](VirtualGeometry.Streaming.CellHeightGridDecoder.md)

#### 実装するインターフェース（Implements）

[IPayloadDecoder](Omni.Streaming.IPayloadDecoder.md)

## プロパティ（Properties）

### <a id="VirtualGeometry_Streaming_CellHeightGridDecoder_Kind"></a> Kind

```csharp
public ushort Kind { get; }
```

#### 値（Property Value）

 [ushort](https://learn.microsoft.com/dotnet/api/system.uint16)

## メソッド（Methods）

### <a id="VirtualGeometry_Streaming_CellHeightGridDecoder_Decode_System_ReadOnlyMemory_System_Byte__Omni_Streaming_StreamKey__"></a> Decode\(ReadOnlyMemory<byte\>, in StreamKey\)

encoded は展開の間だけ有効(保持しない)。失敗は例外で知らせる(その中身は再試行しても同じ結果なので、host は再試行しない)。

```csharp
public IDecodedPayload Decode(ReadOnlyMemory<byte> encoded, in StreamKey key)
```

#### 引数（Parameters）

`encoded` [ReadOnlyMemory](https://learn.microsoft.com/dotnet/api/system.readonlymemory\-1)<[byte](https://learn.microsoft.com/dotnet/api/system.byte)\>

`key` [StreamKey](Omni.Streaming.StreamKey.md)

#### 戻り値（Returns）

 [IDecodedPayload](Omni.Streaming.IDecodedPayload.md)

### <a id="VirtualGeometry_Streaming_CellHeightGridDecoder_EstimateDecodedSize_System_Int32_"></a> EstimateDecodedSize\(int\)

展開後の大きさの見積もり(メモリ予算の判断に使う。厳密でなくてよい)。

```csharp
public long EstimateDecodedSize(int encodedLength)
```

#### 引数（Parameters）

`encodedLength` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)
