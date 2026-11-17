# <a id="Omni_Streaming_Formats_Bc1"></a> Class Bc1

Namespace: [Omni.Streaming.Formats](Omni.Streaming.Formats.md)  
Assembly: Omni.Streaming.Formats.dll  

BC1(DXT1)。4×4 画素を 8 byte に圧縮する GPU 圧縮形式。GPU が圧縮のまま読めるので、届いたタイルを展開せずにテクスチャへ送れる。
符号化は包含箱の両端を色の端点にする簡易な方式(月面のような低彩度の画像向け。4 色モードのみ、アルファなし)。
GPU が BC1 を使えない環境のために、RGBA32 へ展開する復号もある(<xref href="Omni.Streaming.Formats.Bc1.DecodeImage(System.ReadOnlySpan%7bSystem.Byte%7d%2cSystem.Int32%2cSystem.Int32)" data-throw-if-not-resolved="false"></xref>)。

```csharp
public static class Bc1
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[Bc1](Omni.Streaming.Formats.Bc1.md)

## フィールド（Fields）

### <a id="Omni_Streaming_Formats_Bc1_BlockBytes"></a> BlockBytes

```csharp
public const int BlockBytes = 8
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_Streaming_Formats_Bc1_DecodeBlock_System_ReadOnlySpan_System_Byte__System_Span_System_Byte__"></a> DecodeBlock\(ReadOnlySpan<byte\>, Span<byte\>\)

1 ブロックを 16 画素(RGBA、アルファ 255)へ。c0 ≤ c1 の 3 色モードも復号できる。

```csharp
public static void DecodeBlock(ReadOnlySpan<byte> block, Span<byte> rgba)
```

#### 引数（Parameters）

`block` [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[byte](https://learn.microsoft.com/dotnet/api/system.byte)\>

`rgba` [Span](https://learn.microsoft.com/dotnet/api/system.span\-1)<[byte](https://learn.microsoft.com/dotnet/api/system.byte)\>

### <a id="Omni_Streaming_Formats_Bc1_DecodeImage_System_ReadOnlySpan_System_Byte__System_Int32_System_Int32_"></a> DecodeImage\(ReadOnlySpan<byte\>, int, int\)

```csharp
public static byte[] DecodeImage(ReadOnlySpan<byte> blocks, int width, int height)
```

#### 引数（Parameters）

`blocks` [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[byte](https://learn.microsoft.com/dotnet/api/system.byte)\>

`width` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`height` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\]

### <a id="Omni_Streaming_Formats_Bc1_EncodeBlock_System_ReadOnlySpan_System_Byte__System_Span_System_Byte__"></a> EncodeBlock\(ReadOnlySpan<byte\>, Span<byte\>\)

16 画素(RGBA、各 4 byte、行の順)を 1 ブロックへ。

```csharp
public static void EncodeBlock(ReadOnlySpan<byte> rgba, Span<byte> block)
```

#### 引数（Parameters）

`rgba` [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[byte](https://learn.microsoft.com/dotnet/api/system.byte)\>

`block` [Span](https://learn.microsoft.com/dotnet/api/system.span\-1)<[byte](https://learn.microsoft.com/dotnet/api/system.byte)\>

### <a id="Omni_Streaming_Formats_Bc1_EncodeImage_System_Byte___System_Int32_System_Int32_"></a> EncodeImage\(byte\[\], int, int\)

RGBA32(行の順、幅・高さは 4 の倍数)を BC1 のブロック列(ブロックの行の順)へ。

```csharp
public static byte[] EncodeImage(byte[] rgba, int width, int height)
```

#### 引数（Parameters）

`rgba` [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\]

`width` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`height` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\]
