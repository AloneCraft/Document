# <a id="VirtualGeometry_World_PlanetGpuResidencyBuilder"></a> Class PlanetGpuResidencyBuilder

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

1つのGPU表向けのCPU差分producer。pool回収やfenceの所有者ではない。複数GPU複製には別のack/journalが必要。

```csharp
public sealed class PlanetGpuResidencyBuilder
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetGpuResidencyBuilder](VirtualGeometry.World.PlanetGpuResidencyBuilder.md)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetGpuResidencyBuilder__ctor_System_Int32_System_Int32_System_UInt32_"></a> PlanetGpuResidencyBuilder\(int, int, uint\)

```csharp
public PlanetGpuResidencyBuilder(int capacity, int poolCapacity, uint epoch)
```

#### 引数（Parameters）

`capacity` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`poolCapacity` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`epoch` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetGpuResidencyBuilder_Capacity"></a> Capacity

```csharp
public int Capacity { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetGpuResidencyBuilder_Count"></a> Count

```csharp
public int Count { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetGpuResidencyBuilder_MaximumProbeLength"></a> MaximumProbeLength

```csharp
public int MaximumProbeLength { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetGpuResidencyBuilder_Acknowledge_VirtualGeometry_World_PlanetGpuTablePatch_"></a> Acknowledge\(PlanetGpuTablePatch\)

転送先への適用が確定した同じrevisionだけをackする。古いackは未転送の変更を消さない。

```csharp
public bool Acknowledge(PlanetGpuTablePatch patch)
```

#### 引数（Parameters）

`patch` [PlanetGpuTablePatch](VirtualGeometry.World.PlanetGpuTablePatch.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetGpuResidencyBuilder_BuildPatch"></a> BuildPatch\(\)

```csharp
public PlanetGpuTablePatch BuildPatch()
```

#### 戻り値（Returns）

 [PlanetGpuTablePatch](VirtualGeometry.World.PlanetGpuTablePatch.md)

### <a id="VirtualGeometry_World_PlanetGpuResidencyBuilder_Remove_VirtualGeometry_World_PlanetGpuKey_"></a> Remove\(PlanetGpuKey\)

```csharp
public bool Remove(PlanetGpuKey key)
```

#### 引数（Parameters）

`key` [PlanetGpuKey](VirtualGeometry.World.PlanetGpuKey.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetGpuResidencyBuilder_TryGet_VirtualGeometry_World_PlanetGpuKey_VirtualGeometry_World_PlanetGpuResidentEntry__"></a> TryGet\(PlanetGpuKey, out PlanetGpuResidentEntry\)

```csharp
public bool TryGet(PlanetGpuKey key, out PlanetGpuResidentEntry entry)
```

#### 引数（Parameters）

`key` [PlanetGpuKey](VirtualGeometry.World.PlanetGpuKey.md)

`entry` [PlanetGpuResidentEntry](VirtualGeometry.World.PlanetGpuResidentEntry.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetGpuResidencyBuilder_Upsert_VirtualGeometry_World_PlanetGpuResidentEntry_"></a> Upsert\(PlanetGpuResidentEntry\)

```csharp
public PlanetGpuTableUpdate Upsert(PlanetGpuResidentEntry value)
```

#### 引数（Parameters）

`value` [PlanetGpuResidentEntry](VirtualGeometry.World.PlanetGpuResidentEntry.md)

#### 戻り値（Returns）

 [PlanetGpuTableUpdate](VirtualGeometry.World.PlanetGpuTableUpdate.md)
