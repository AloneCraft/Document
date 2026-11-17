# <a id="VirtualizedGeometry_VirtualGeometrySharedEdgeSplit"></a> Class VirtualGeometrySharedEdgeSplit

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

粗い辺の隣接三角形を置き換える。細境界の同じindexを使い、元の面を重ねて残さない。

```csharp
public static class VirtualGeometrySharedEdgeSplit
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometrySharedEdgeSplit](VirtualizedGeometry.VirtualGeometrySharedEdgeSplit.md)

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometrySharedEdgeSplit_Replace_System_UInt32___System_UInt32___"></a> Replace\(uint\[\], uint\[\]\)

```csharp
public static uint[] Replace(uint[] indices, uint[] boundary)
```

#### 引数（Parameters）

`indices` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]

`boundary` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]

#### 戻り値（Returns）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]
