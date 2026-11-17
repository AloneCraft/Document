# <a id="VirtualGeometry_Streaming_CellHeightGridCodec"></a> Class CellHeightGridCodec

Namespace: [VirtualGeometry.Streaming](VirtualGeometry.Streaming.md)  
Assembly: Omni.VirtualGeometry.Streaming.dll  

格子の高さの中身の形式 "CHT1": [0..4) "CHT1"、[4..6) side、[6..8) 旗(bit0 = 陰影用の高さの面がある)、[8..12) step(float、メートル/整数)、
以降は Deflate した面(高さ、あれば陰影)。1 面は side² 個の int16 で、左の格子点との差(各行の先頭は上の行の先頭との差、最初の点は 0 との差)を
2 byte little endian で並べたもの(差は int16 の剰余で表し、復元は同じ剰余で足すので正確)。滑らかな地形ほど小さな値が並び、Deflate がよく効く。

```csharp
public static class CellHeightGridCodec
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[CellHeightGridCodec](VirtualGeometry.Streaming.CellHeightGridCodec.md)

## フィールド（Fields）

### <a id="VirtualGeometry_Streaming_CellHeightGridCodec_Kind"></a> Kind

カタログの項目の種別(<xref href="Omni.Streaming.IPayloadDecoder.Kind" data-throw-if-not-resolved="false"></xref>)。

```csharp
public const ushort Kind = 257
```

#### 値（Field Value）

 [ushort](https://learn.microsoft.com/dotnet/api/system.uint16)

## メソッド（Methods）

### <a id="VirtualGeometry_Streaming_CellHeightGridCodec_Decode_System_ReadOnlySpan_System_Byte__"></a> Decode\(ReadOnlySpan<byte\>\)

```csharp
public static CellHeightGrid Decode(ReadOnlySpan<byte> data)
```

#### 引数（Parameters）

`data` [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[byte](https://learn.microsoft.com/dotnet/api/system.byte)\>

#### 戻り値（Returns）

 [CellHeightGrid](VirtualGeometry.Streaming.CellHeightGrid.md)

### <a id="VirtualGeometry_Streaming_CellHeightGridCodec_Encode_System_Double___System_Double___System_Int32_System_Single_"></a> Encode\(double\[\], double\[\], int, float\)

```csharp
public static byte[] Encode(double[] heights, double[] shading, int side, float step)
```

#### 引数（Parameters）

`heights` [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]

`shading` [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]

`side` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`step` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\]

### <a id="VirtualGeometry_Streaming_CellHeightGridCodec_Encode_System_Int32_System_Single_System_Int16___System_Int16___"></a> Encode\(int, float, short\[\], short\[\]\)

```csharp
public static byte[] Encode(int side, float step, short[] heights, short[] shading)
```

#### 引数（Parameters）

`side` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`step` [float](https://learn.microsoft.com/dotnet/api/system.single)

`heights` [short](https://learn.microsoft.com/dotnet/api/system.int16)\[\]

`shading` [short](https://learn.microsoft.com/dotnet/api/system.int16)\[\]

#### 戻り値（Returns）

 [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\]

### <a id="VirtualGeometry_Streaming_CellHeightGridCodec_Quantize_System_Double_System_Double_"></a> Quantize\(double, double\)

メートルの高さを step 刻みの整数にする(Round)。int16 に収まらなければ例外(step を大きくする)。

```csharp
public static short Quantize(double meters, double step)
```

#### 引数（Parameters）

`meters` [double](https://learn.microsoft.com/dotnet/api/system.double)

`step` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [short](https://learn.microsoft.com/dotnet/api/system.int16)
