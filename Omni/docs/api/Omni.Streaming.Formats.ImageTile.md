# <a id="Omni_Streaming_Formats_ImageTile"></a> Class ImageTile

Namespace: [Omni.Streaming.Formats](Omni.Streaming.Formats.md)  
Assembly: Omni.Streaming.Formats.dll  

展開済みの画像タイル(幅×高さの画素)。<xref href="Omni.Streaming.Formats.ImageTile.Data" data-throw-if-not-resolved="false"></xref> は <xref href="Omni.Streaming.Formats.ImageTile.Format" data-throw-if-not-resolved="false"></xref> のまま(BC1 ならブロック列)。

```csharp
public sealed class ImageTile : IDecodedPayload, IDisposable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[ImageTile](Omni.Streaming.Formats.ImageTile.md)

#### 実装するインターフェース（Implements）

[IDecodedPayload](Omni.Streaming.IDecodedPayload.md), 
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

## コンストラクター（Constructors）

### <a id="Omni_Streaming_Formats_ImageTile__ctor_System_Int32_System_Int32_Omni_Streaming_Formats_ImageTileFormat_System_Byte___"></a> ImageTile\(int, int, ImageTileFormat, byte\[\]\)

```csharp
public ImageTile(int width, int height, ImageTileFormat format, byte[] data)
```

#### 引数（Parameters）

`width` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`height` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`format` [ImageTileFormat](Omni.Streaming.Formats.ImageTileFormat.md)

`data` [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\]

## フィールド（Fields）

### <a id="Omni_Streaming_Formats_ImageTile_Data"></a> Data

```csharp
public readonly byte[] Data
```

#### 値（Field Value）

 [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\]

### <a id="Omni_Streaming_Formats_ImageTile_Format"></a> Format

```csharp
public readonly ImageTileFormat Format
```

#### 値（Field Value）

 [ImageTileFormat](Omni.Streaming.Formats.ImageTileFormat.md)

### <a id="Omni_Streaming_Formats_ImageTile_Height"></a> Height

```csharp
public readonly int Height
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_Formats_ImageTile_Width"></a> Width

```csharp
public readonly int Width
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="Omni_Streaming_Formats_ImageTile_ByteSize"></a> ByteSize

```csharp
public long ByteSize { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

## メソッド（Methods）

### <a id="Omni_Streaming_Formats_ImageTile_Dispose"></a> Dispose\(\)

```csharp
public void Dispose()
```

### <a id="Omni_Streaming_Formats_ImageTile_ExpectedBytes_System_Int32_System_Int32_Omni_Streaming_Formats_ImageTileFormat_"></a> ExpectedBytes\(int, int, ImageTileFormat\)

```csharp
public static int ExpectedBytes(int width, int height, ImageTileFormat format)
```

#### 引数（Parameters）

`width` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`height` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`format` [ImageTileFormat](Omni.Streaming.Formats.ImageTileFormat.md)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_Formats_ImageTile_ToRgba32"></a> ToRgba32\(\)

RGBA32 の画素列(BC1 なら復号する)。

```csharp
public byte[] ToRgba32()
```

#### 戻り値（Returns）

 [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\]
