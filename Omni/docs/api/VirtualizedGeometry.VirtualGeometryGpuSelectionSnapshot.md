# <a id="VirtualizedGeometry_VirtualGeometryGpuSelectionSnapshot"></a> Class VirtualGeometryGpuSelectionSnapshot

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

```csharp
public sealed class VirtualGeometryGpuSelectionSnapshot
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryGpuSelectionSnapshot](VirtualizedGeometry.VirtualGeometryGpuSelectionSnapshot.md)

## プロパティ（Properties）

### <a id="VirtualizedGeometry_VirtualGeometryGpuSelectionSnapshot_Arguments"></a> Arguments

```csharp
public uint[] Arguments { get; }
```

#### 値（Property Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]

### <a id="VirtualizedGeometry_VirtualGeometryGpuSelectionSnapshot_CullingStatistics"></a> CullingStatistics

直近の描画で考慮した数、Frustum棄却数、HZB棄却数、可視数の順。

```csharp
public uint[] CullingStatistics { get; }
```

#### 値（Property Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]

### <a id="VirtualizedGeometry_VirtualGeometryGpuSelectionSnapshot_SelectionFlags"></a> SelectionFlags

```csharp
public uint[] SelectionFlags { get; }
```

#### 値（Property Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]

### <a id="VirtualizedGeometry_VirtualGeometryGpuSelectionSnapshot_VisibleIndices"></a> VisibleIndices

```csharp
public uint[] VisibleIndices { get; }
```

#### 値（Property Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]
