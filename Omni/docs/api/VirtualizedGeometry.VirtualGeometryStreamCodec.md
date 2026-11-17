# <a id="VirtualizedGeometry_VirtualGeometryStreamCodec"></a> Class VirtualGeometryStreamCodec

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

v3のmetadataを先に検証し、payloadをpage単位で独立検証する。

```csharp
public static class VirtualGeometryStreamCodec
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryStreamCodec](VirtualizedGeometry.VirtualGeometryStreamCodec.md)

## フィールド（Fields）

### <a id="VirtualizedGeometry_VirtualGeometryStreamCodec_ConnectedVersion"></a> ConnectedVersion

```csharp
public const uint ConnectedVersion = 7
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualizedGeometry_VirtualGeometryStreamCodec_HeaderBytes"></a> HeaderBytes

```csharp
public const int HeaderBytes = 96
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryStreamCodec_Version"></a> Version

```csharp
public const uint Version = 6
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometryStreamCodec_DecodePayload_System_Byte___VirtualizedGeometry_VirtualGeometryPageDescriptor_VirtualizedGeometry_VirtualGeometryStreamMetadata_"></a> DecodePayload\(byte\[\], VirtualGeometryPageDescriptor, VirtualGeometryStreamMetadata\)

archiveの版に合わせてpageを復号する。v7はboundsから独立した接続格子を使う。

```csharp
public static VirtualGeometryPagePayload DecodePayload(byte[] bytes, VirtualGeometryPageDescriptor descriptor, VirtualGeometryStreamMetadata metadata)
```

#### 引数（Parameters）

`bytes` [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\]

`descriptor` [VirtualGeometryPageDescriptor](VirtualizedGeometry.VirtualGeometryPageDescriptor.md)

`metadata` [VirtualGeometryStreamMetadata](VirtualizedGeometry.VirtualGeometryStreamMetadata.md)

#### 戻り値（Returns）

 [VirtualGeometryPagePayload](VirtualizedGeometry.VirtualGeometryPagePayload.md)

### <a id="VirtualizedGeometry_VirtualGeometryStreamCodec_DecodePayload_System_Byte___VirtualizedGeometry_VirtualGeometryPageDescriptor_"></a> DecodePayload\(byte\[\], VirtualGeometryPageDescriptor\)

版 4(頂点と index を生のまま並べた形)の page を復号する。

```csharp
public static VirtualGeometryPagePayload DecodePayload(byte[] bytes, VirtualGeometryPageDescriptor descriptor)
```

#### 引数（Parameters）

`bytes` [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\]

`descriptor` [VirtualGeometryPageDescriptor](VirtualizedGeometry.VirtualGeometryPageDescriptor.md)

#### 戻り値（Returns）

 [VirtualGeometryPagePayload](VirtualizedGeometry.VirtualGeometryPagePayload.md)

### <a id="VirtualizedGeometry_VirtualGeometryStreamCodec_IsSupportedVersion_System_UInt32_"></a> IsSupportedVersion\(uint\)

読める版。4 は頂点(32 byte)と index(32 bit)を生のまま並べた形。

```csharp
public static bool IsSupportedVersion(uint version)
```

#### 引数（Parameters）

`version` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryStreamCodec_ReadAll_System_Byte___"></a> ReadAll\(byte\[\]\)

```csharp
public static VirtualGeometryPage ReadAll(byte[] bytes)
```

#### 引数（Parameters）

`bytes` [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\]

#### 戻り値（Returns）

 [VirtualGeometryPage](VirtualizedGeometry.VirtualGeometryPage.md)

### <a id="VirtualizedGeometry_VirtualGeometryStreamCodec_ReadMetadata_System_IO_Stream_System_Int64_"></a> ReadMetadata\(Stream, long\)

```csharp
public static VirtualGeometryStreamMetadata ReadMetadata(Stream stream, long fileLength = -1)
```

#### 引数（Parameters）

`stream` [Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)

`fileLength` [long](https://learn.microsoft.com/dotnet/api/system.int64)

archive 全体の長さ。stream が先頭の metadata だけのとき(HTTP の Range で取った場合)に渡す。省略すると stream の長さ。

#### 戻り値（Returns）

 [VirtualGeometryStreamMetadata](VirtualizedGeometry.VirtualGeometryStreamMetadata.md)

### <a id="VirtualizedGeometry_VirtualGeometryStreamCodec_Write_VirtualizedGeometry_VirtualGeometryPage_"></a> Write\(VirtualGeometryPage\)

```csharp
public static byte[] Write(VirtualGeometryPage source)
```

#### 引数（Parameters）

`source` [VirtualGeometryPage](VirtualizedGeometry.VirtualGeometryPage.md)

#### 戻り値（Returns）

 [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\]
