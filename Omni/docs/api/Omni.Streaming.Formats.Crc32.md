# <a id="Omni_Streaming_Formats_Crc32"></a> Class Crc32

Namespace: [Omni.Streaming.Formats](Omni.Streaming.Formats.md)  
Assembly: Omni.Streaming.Formats.dll  

CRC-32(IEEE 802.3)。ディレクトリページの破損検出に使う。

```csharp
public static class Crc32
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[Crc32](Omni.Streaming.Formats.Crc32.md)

## メソッド（Methods）

### <a id="Omni_Streaming_Formats_Crc32_Compute_System_ReadOnlySpan_System_Byte__"></a> Compute\(ReadOnlySpan<byte\>\)

```csharp
public static uint Compute(ReadOnlySpan<byte> data)
```

#### 引数（Parameters）

`data` [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[byte](https://learn.microsoft.com/dotnet/api/system.byte)\>

#### 戻り値（Returns）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)
