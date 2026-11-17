# <a id="VirtualizedGeometry_IVirtualGeometryPageUploader"></a> Interface IVirtualGeometryPageUploader

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

実GPU転送とstate-machine試験の境界。公開前のpartial slotは描画対象にしない。
slotはpageが使う連続slotの先頭。offsetはそこからの頂点・添字の位置で、pageの全体が連続した範囲に入る。

```csharp
public interface IVirtualGeometryPageUploader
```

## プロパティ（Properties）

### <a id="VirtualizedGeometry_IVirtualGeometryPageUploader_IndexBytes"></a> IndexBytes

GPU に置く index の 1 つの大きさ(byte)。16 bit に詰めるなら 2。転送の予算の数え方に使う。

```csharp
int IndexBytes { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_IVirtualGeometryPageUploader_IndexUploadAlignment"></a> IndexUploadAlignment

index を分けて転送するときの、1 回の個数の単位。16 bit に詰めるなら 2(最後の 1 回を除く)。

```csharp
int IndexUploadAlignment { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="VirtualizedGeometry_IVirtualGeometryPageUploader_Invalidate_System_Int32_"></a> Invalidate\(int\)

```csharp
void Invalidate(int page)
```

#### 引数（Parameters）

`page` [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_IVirtualGeometryPageUploader_Publish_System_Int32_System_Int32_System_Int32_"></a> Publish\(int, int, int\)

```csharp
void Publish(int page, int slot, int generation)
```

#### 引数（Parameters）

`page` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`generation` [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_IVirtualGeometryPageUploader_UploadIndices_System_Int32_System_Int32_System_UInt32___System_Int32_System_Int32_"></a> UploadIndices\(int, int, uint\[\], int, int\)

```csharp
void UploadIndices(int slot, int offset, uint[] indices, int sourceOffset, int count)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`offset` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`indices` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]

`sourceOffset` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`count` [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_IVirtualGeometryPageUploader_UploadVertices_System_Int32_System_Int32_VirtualizedGeometry_VirtualGeometryPackedVertex___System_Int32_System_Int32_"></a> UploadVertices\(int, int, VirtualGeometryPackedVertex\[\], int, int\)

```csharp
void UploadVertices(int slot, int offset, VirtualGeometryPackedVertex[] vertices, int sourceOffset, int count)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`offset` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`vertices` [VirtualGeometryPackedVertex](VirtualizedGeometry.VirtualGeometryPackedVertex.md)\[\]

`sourceOffset` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`count` [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_IVirtualGeometryPageUploader_UploadWords_System_Int32_System_Int32_System_UInt32___System_Int32_System_Int32_"></a> UploadWords\(int, int, uint\[\], int, int\)

符号化した page(<xref href="VirtualizedGeometry.VirtualGeometryPagePayload.Words" data-throw-if-not-resolved="false"></xref>)の語を、slot の先頭からの語の位置 offset へ置く。符号化したまま持つ pool だけ。

```csharp
void UploadWords(int slot, int offset, uint[] words, int sourceOffset, int count)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`offset` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`words` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]

`sourceOffset` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`count` [int](https://learn.microsoft.com/dotnet/api/system.int32)
