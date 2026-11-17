# <a id="Omni_VirtualObject_ProceduralMeshBuffer"></a> Class ProceduralMeshBuffer

Namespace: [Omni.VirtualObject](Omni.VirtualObject.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

<xref href="Omni.VirtualObject.ProceduralMeshRepresentation" data-throw-if-not-resolved="false"></xref> が集めるメッシュの材料。ビルダーはここへ足していく。

```csharp
public sealed class ProceduralMeshBuffer
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[ProceduralMeshBuffer](Omni.VirtualObject.ProceduralMeshBuffer.md)

## フィールド（Fields）

### <a id="Omni_VirtualObject_ProceduralMeshBuffer_Indices"></a> Indices

頂点番号 3 つで 1 三角形。

```csharp
public readonly List<int> Indices
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[int](https://learn.microsoft.com/dotnet/api/system.int32)\>

### <a id="Omni_VirtualObject_ProceduralMeshBuffer_Normals"></a> Normals

```csharp
public readonly List<Vector3> Normals
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<Vector3\>

### <a id="Omni_VirtualObject_ProceduralMeshBuffer_Uvs"></a> Uvs

```csharp
public readonly List<Vector2> Uvs
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<Vector2\>

### <a id="Omni_VirtualObject_ProceduralMeshBuffer_Vertices"></a> Vertices

```csharp
public readonly List<Vector3> Vertices
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<Vector3\>

## プロパティ（Properties）

### <a id="Omni_VirtualObject_ProceduralMeshBuffer_Bytes"></a> Bytes

CPU 側で持つ大きさ（頂点 32 バイト = 位置 12 + 法線 12 + UV 8、インデックス 4 バイト）。

```csharp
public long Bytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_VirtualObject_ProceduralMeshBuffer_TriangleCount"></a> TriangleCount

```csharp
public int TriangleCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_VirtualObject_ProceduralMeshBuffer_Clear"></a> Clear\(\)

```csharp
public void Clear()
```
