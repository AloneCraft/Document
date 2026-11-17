# <a id="VirtualizedGeometry_VirtualGeometryPageDescriptor"></a> Struct VirtualGeometryPageDescriptor

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

独立I/O範囲とpage-local geometryのサイズ/CRCを保持するv3 descriptor。

```csharp
public struct VirtualGeometryPageDescriptor
```

## フィールド（Fields）

### <a id="VirtualizedGeometry_VirtualGeometryPageDescriptor_ByteCount"></a> ByteCount

archive の中の byte 数(版 6 では符号化した大きさ。4 の倍数)。

```csharp
public int ByteCount
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryPageDescriptor_Crc"></a> Crc

```csharp
public uint Crc
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualizedGeometry_VirtualGeometryPageDescriptor_IndexCount"></a> IndexCount

```csharp
public int IndexCount
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryPageDescriptor_Offset"></a> Offset

```csharp
public long Offset
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualizedGeometry_VirtualGeometryPageDescriptor_Pinned"></a> Pinned

```csharp
public bool Pinned
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryPageDescriptor_VertexCount"></a> VertexCount

復号した page の頂点の数(cluster ごとの頂点を整数で重複排除した後)。

```csharp
public int VertexCount
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="VirtualizedGeometry_VirtualGeometryPageDescriptor_DecodedBytes"></a> DecodedBytes

復号した後の頂点(32 byte)と index(4 byte)の byte 数。CPU のメモリの見積りに使う。

```csharp
public long DecodedBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)
