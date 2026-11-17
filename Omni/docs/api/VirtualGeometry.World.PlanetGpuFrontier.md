# <a id="VirtualGeometry_World_PlanetGpuFrontier"></a> Class PlanetGpuFrontier

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

分割1回の安定したprefix/scatterのCPU参照。誤差評価・継ぎ目処理・frame controllerは含まない。

```csharp
public static class PlanetGpuFrontier
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetGpuFrontier](VirtualGeometry.World.PlanetGpuFrontier.md)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetGpuFrontier_Expand_System_Collections_Generic_IReadOnlyList_VirtualGeometry_World_PlanetGpuFrontierNode__System_Collections_Generic_IReadOnlyList_VirtualGeometry_World_PlanetGpuSplitHint__VirtualGeometry_World_PlanetGpuResidencyTable_System_UInt32_System_ReadOnlySpan_System_UInt32__System_Int32_System_Int32_System_Int32_System_Int32_System_Int32_"></a> Expand\(IReadOnlyList<PlanetGpuFrontierNode\>, IReadOnlyList<PlanetGpuSplitHint\>, PlanetGpuResidencyTable, uint, ReadOnlySpan<uint\>, int, int, int, int, int\)

```csharp
public static PlanetGpuFrontierResult Expand(IReadOnlyList<PlanetGpuFrontierNode> input, IReadOnlyList<PlanetGpuSplitHint> hints, PlanetGpuResidencyTable table, uint epoch, ReadOnlySpan<uint> ready, int budget, int outputCapacity, int requestCapacity, int anchorCount, int maximumLevel = 94)
```

#### 引数（Parameters）

`input` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[PlanetGpuFrontierNode](VirtualGeometry.World.PlanetGpuFrontierNode.md)\>

`hints` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[PlanetGpuSplitHint](VirtualGeometry.World.PlanetGpuSplitHint.md)\>

`table` [PlanetGpuResidencyTable](VirtualGeometry.World.PlanetGpuResidencyTable.md)

`epoch` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`ready` [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[uint](https://learn.microsoft.com/dotnet/api/system.uint32)\>

`budget` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`outputCapacity` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`requestCapacity` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`anchorCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`maximumLevel` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [PlanetGpuFrontierResult](VirtualGeometry.World.PlanetGpuFrontierResult.md)
