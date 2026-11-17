# <a id="VirtualGeometry_World_PlanetGpuResidencyTable"></a> Class PlanetGpuResidencyTable

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

GPU常駐確認用のimmutable snapshotのCPU参照。毎frameの全再構築には使わない。

```csharp
public sealed class PlanetGpuResidencyTable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetGpuResidencyTable](VirtualGeometry.World.PlanetGpuResidencyTable.md)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetGpuResidencyTable__ctor_System_Collections_Generic_IReadOnlyList_VirtualGeometry_World_PlanetGpuResidentEntry__System_Int32_System_Int64_"></a> PlanetGpuResidencyTable\(IReadOnlyList<PlanetGpuResidentEntry\>, int, long\)

```csharp
public PlanetGpuResidencyTable(IReadOnlyList<PlanetGpuResidentEntry> residents, int capacity, long maximumBindingBytes = 134217728)
```

#### 引数（Parameters）

`residents` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[PlanetGpuResidentEntry](VirtualGeometry.World.PlanetGpuResidentEntry.md)\>

`capacity` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`maximumBindingBytes` [long](https://learn.microsoft.com/dotnet/api/system.int64)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetGpuResidencyTable_Count"></a> Count

```csharp
public int Count { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetGpuResidencyTable_Entries"></a> Entries

```csharp
public ReadOnlySpan<PlanetGpuResidentEntry> Entries { get; }
```

#### 値（Property Value）

 [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[PlanetGpuResidentEntry](VirtualGeometry.World.PlanetGpuResidentEntry.md)\>

### <a id="VirtualGeometry_World_PlanetGpuResidencyTable_MaximumProbeLength"></a> MaximumProbeLength

```csharp
public int MaximumProbeLength { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetGpuResidencyTable_Lookup_VirtualGeometry_World_PlanetGpuKey_System_UInt32_System_ReadOnlySpan_System_UInt32__VirtualGeometry_World_PlanetGpuResidentEntry__System_Int32__"></a> Lookup\(PlanetGpuKey, uint, ReadOnlySpan<uint\>, out PlanetGpuResidentEntry, out int\)

```csharp
public PlanetGpuResidency Lookup(PlanetGpuKey key, uint epoch, ReadOnlySpan<uint> readyGenerations, out PlanetGpuResidentEntry entry, out int probes)
```

#### 引数（Parameters）

`key` [PlanetGpuKey](VirtualGeometry.World.PlanetGpuKey.md)

`epoch` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`readyGenerations` [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[uint](https://learn.microsoft.com/dotnet/api/system.uint32)\>

`entry` [PlanetGpuResidentEntry](VirtualGeometry.World.PlanetGpuResidentEntry.md)

`probes` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [PlanetGpuResidency](VirtualGeometry.World.PlanetGpuResidency.md)
