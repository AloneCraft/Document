# <a id="Omni_Streaming_IPayloadDecoder"></a> Interface IPayloadDecoder

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

種別ごとの展開器(バイト列 → 利用できる形)。Decode は host の Tick の中(主 thread、frame の予算内)から呼ばれる。

```csharp
public interface IPayloadDecoder
```

## プロパティ（Properties）

### <a id="Omni_Streaming_IPayloadDecoder_Kind"></a> Kind

```csharp
ushort Kind { get; }
```

#### 値（Property Value）

 [ushort](https://learn.microsoft.com/dotnet/api/system.uint16)

## メソッド（Methods）

### <a id="Omni_Streaming_IPayloadDecoder_Decode_System_ReadOnlyMemory_System_Byte__Omni_Streaming_StreamKey__"></a> Decode\(ReadOnlyMemory<byte\>, in StreamKey\)

encoded は展開の間だけ有効(保持しない)。失敗は例外で知らせる(その中身は再試行しても同じ結果なので、host は再試行しない)。

```csharp
IDecodedPayload Decode(ReadOnlyMemory<byte> encoded, in StreamKey key)
```

#### 引数（Parameters）

`encoded` [ReadOnlyMemory](https://learn.microsoft.com/dotnet/api/system.readonlymemory\-1)<[byte](https://learn.microsoft.com/dotnet/api/system.byte)\>

`key` [StreamKey](Omni.Streaming.StreamKey.md)

#### 戻り値（Returns）

 [IDecodedPayload](Omni.Streaming.IDecodedPayload.md)

### <a id="Omni_Streaming_IPayloadDecoder_EstimateDecodedSize_System_Int32_"></a> EstimateDecodedSize\(int\)

展開後の大きさの見積もり(メモリ予算の判断に使う。厳密でなくてよい)。

```csharp
long EstimateDecodedSize(int encodedLength)
```

#### 引数（Parameters）

`encodedLength` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)
