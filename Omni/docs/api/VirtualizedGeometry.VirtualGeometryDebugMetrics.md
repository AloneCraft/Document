# <a id="VirtualizedGeometry_VirtualGeometryDebugMetrics"></a> Class VirtualGeometryDebugMetrics

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

VG Statsで同じassetを複数配置してもunique bytesを二重に数えない。

```csharp
public static class VirtualGeometryDebugMetrics
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryDebugMetrics](VirtualizedGeometry.VirtualGeometryDebugMetrics.md)

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometryDebugMetrics_Aggregate_System_Collections_Generic_IEnumerable_VirtualizedGeometry_VirtualGeometryInstanceMetrics__"></a> Aggregate\(IEnumerable<VirtualGeometryInstanceMetrics\>\)

```csharp
public static VirtualGeometryInstanceMetrics Aggregate(IEnumerable<VirtualGeometryInstanceMetrics> instances)
```

#### 引数（Parameters）

`instances` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<[VirtualGeometryInstanceMetrics](VirtualizedGeometry.VirtualGeometryInstanceMetrics.md)\>

#### 戻り値（Returns）

 [VirtualGeometryInstanceMetrics](VirtualizedGeometry.VirtualGeometryInstanceMetrics.md)
