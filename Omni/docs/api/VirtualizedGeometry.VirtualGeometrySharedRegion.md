# <a id="VirtualizedGeometry_VirtualGeometrySharedRegion"></a> Class VirtualGeometrySharedRegion

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

一つのpage/LODの明示index。配列を複製して、公開後の供給側による書換えを防ぐ。

```csharp
public sealed class VirtualGeometrySharedRegion
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometrySharedRegion](VirtualizedGeometry.VirtualGeometrySharedRegion.md)

## コンストラクター（Constructors）

### <a id="VirtualizedGeometry_VirtualGeometrySharedRegion__ctor_System_String_System_Int32_System_Boolean_System_Boolean_VirtualizedGeometry_VirtualGeometrySharedVertex___System_UInt32___"></a> VirtualGeometrySharedRegion\(string, int, bool, bool, VirtualGeometrySharedVertex\[\], uint\[\]\)

```csharp
public VirtualGeometrySharedRegion(string pageId, int lod, bool ready, bool cancelled, VirtualGeometrySharedVertex[] vertices, uint[] indices)
```

#### 引数（Parameters）

`pageId` [string](https://learn.microsoft.com/dotnet/api/system.string)

`lod` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`ready` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`cancelled` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`vertices` [VirtualGeometrySharedVertex](VirtualizedGeometry.VirtualGeometrySharedVertex.md)\[\]

`indices` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]

## プロパティ（Properties）

### <a id="VirtualizedGeometry_VirtualGeometrySharedRegion_Cancelled"></a> Cancelled

```csharp
public bool Cancelled { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometrySharedRegion_IndexCount"></a> IndexCount

```csharp
public int IndexCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometrySharedRegion_Lod"></a> Lod

```csharp
public int Lod { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometrySharedRegion_PageId"></a> PageId

```csharp
public string PageId { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualizedGeometry_VirtualGeometrySharedRegion_Ready"></a> Ready

```csharp
public bool Ready { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometrySharedRegion_VertexCount"></a> VertexCount

```csharp
public int VertexCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)
