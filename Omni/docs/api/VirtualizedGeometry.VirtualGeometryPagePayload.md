# <a id="VirtualizedGeometry_VirtualGeometryPagePayload"></a> Class VirtualGeometryPagePayload

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

GPU転送に使用する単一page。配列の所有者はstreaming controller。

```csharp
public sealed class VirtualGeometryPagePayload
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryPagePayload](VirtualizedGeometry.VirtualGeometryPagePayload.md)

## コンストラクター（Constructors）

### <a id="VirtualizedGeometry_VirtualGeometryPagePayload__ctor_VirtualizedGeometry_VirtualGeometryPackedVertex___System_UInt32___"></a> VirtualGeometryPagePayload\(VirtualGeometryPackedVertex\[\], uint\[\]\)

```csharp
public VirtualGeometryPagePayload(VirtualGeometryPackedVertex[] vertices, uint[] indices)
```

#### 引数（Parameters）

`vertices` [VirtualGeometryPackedVertex](VirtualizedGeometry.VirtualGeometryPackedVertex.md)\[\]

`indices` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]

### <a id="VirtualizedGeometry_VirtualGeometryPagePayload__ctor_System_UInt32___"></a> VirtualGeometryPagePayload\(uint\[\]\)

```csharp
public VirtualGeometryPagePayload(uint[] words)
```

#### 引数（Parameters）

`words` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]

## プロパティ（Properties）

### <a id="VirtualizedGeometry_VirtualGeometryPagePayload_ByteCount"></a> ByteCount

```csharp
public int ByteCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryPagePayload_Indices"></a> Indices

```csharp
public uint[] Indices { get; }
```

#### 値（Property Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]

### <a id="VirtualizedGeometry_VirtualGeometryPagePayload_Vertices"></a> Vertices

```csharp
public VirtualGeometryPackedVertex[] Vertices { get; }
```

#### 値（Property Value）

 [VirtualGeometryPackedVertex](VirtualizedGeometry.VirtualGeometryPackedVertex.md)\[\]

### <a id="VirtualizedGeometry_VirtualGeometryPagePayload_Words"></a> Words

符号化したままの page(版 6 の page を GPU の pool へそのまま置く形)。これがあるとき、Vertices と Indices は空。

```csharp
public uint[] Words { get; }
```

#### 値（Property Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]
