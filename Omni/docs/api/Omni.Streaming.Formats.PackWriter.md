# <a id="Omni_Streaming_Formats_PackWriter"></a> Class PackWriter

Namespace: [Omni.Streaming.Formats](Omni.Streaming.Formats.md)  
Assembly: Omni.Streaming.Formats.dll  

pack を書く。マスは ID(<xref href="Omni.Streaming.Formats.TileId" data-throw-if-not-resolved="false"></xref>)の昇順に <xref href="Omni.Streaming.Formats.PackWriter.AddTile(System.Int32%2cSystem.UInt32%2cSystem.UInt32%2cSystem.ReadOnlySpan%7bSystem.Byte%7d)" data-throw-if-not-resolved="false"></xref> する(Hilbert 順で並ぶので、近いマスの中身が本体の中でも連続する)。
同じ中身は1回だけ保存し、ID が連続して同じ中身を指すマスは1項目にまとめる。

```csharp
public sealed class PackWriter
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PackWriter](Omni.Streaming.Formats.PackWriter.md)

## コンストラクター（Constructors）

### <a id="Omni_Streaming_Formats_PackWriter__ctor_Omni_Streaming_Formats_PackWriterOptions_"></a> PackWriter\(PackWriterOptions\)

```csharp
public PackWriter(PackWriterOptions options)
```

#### 引数（Parameters）

`options` [PackWriterOptions](Omni.Streaming.Formats.PackWriterOptions.md)

## プロパティ（Properties）

### <a id="Omni_Streaming_Formats_PackWriter_TileCountSoFar"></a> TileCountSoFar

```csharp
public int TileCountSoFar { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_Streaming_Formats_PackWriter_AddTile_System_Int32_System_UInt32_System_UInt32_System_ReadOnlySpan_System_Byte__"></a> AddTile\(int, uint, uint, ReadOnlySpan<byte\>\)

```csharp
public void AddTile(int level, uint x, uint y, ReadOnlySpan<byte> content)
```

#### 引数（Parameters）

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`x` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`y` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`content` [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[byte](https://learn.microsoft.com/dotnet/api/system.byte)\>

### <a id="Omni_Streaming_Formats_PackWriter_AddTile_System_Int32_System_UInt32_System_UInt32_System_ReadOnlySpan_System_Byte__System_UInt16_"></a> AddTile\(int, uint, uint, ReadOnlySpan<byte\>, ushort\)

```csharp
public void AddTile(int level, uint x, uint y, ReadOnlySpan<byte> content, ushort kind)
```

#### 引数（Parameters）

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`x` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`y` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`content` [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[byte](https://learn.microsoft.com/dotnet/api/system.byte)\>

`kind` [ushort](https://learn.microsoft.com/dotnet/api/system.uint16)

### <a id="Omni_Streaming_Formats_PackWriter_Finish_System_IO_Stream_"></a> Finish\(Stream\)

```csharp
public PackWriteResult Finish(Stream output)
```

#### 引数（Parameters）

`output` [Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)

#### 戻り値（Returns）

 [PackWriteResult](Omni.Streaming.Formats.PackWriteResult.md)
