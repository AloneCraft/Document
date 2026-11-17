# <a id="VirtualGeometry_World_PlanetGpuChildren"></a> Struct PlanetGpuChildren

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

```csharp
public readonly struct PlanetGpuChildren
```

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetGpuChildren_InvalidMask"></a> InvalidMask

```csharp
public readonly uint InvalidMask
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualGeometry_World_PlanetGpuChildren_MissingMask"></a> MissingMask

```csharp
public readonly uint MissingMask
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualGeometry_World_PlanetGpuChildren_RequestMask"></a> RequestMask

```csharp
public readonly uint RequestMask
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualGeometry_World_PlanetGpuChildren_Slot0"></a> Slot0

```csharp
public readonly uint Slot0
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualGeometry_World_PlanetGpuChildren_Slot1"></a> Slot1

```csharp
public readonly uint Slot1
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualGeometry_World_PlanetGpuChildren_Slot2"></a> Slot2

```csharp
public readonly uint Slot2
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualGeometry_World_PlanetGpuChildren_Slot3"></a> Slot3

```csharp
public readonly uint Slot3
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetGpuChildren_AllReady"></a> AllReady

```csharp
public bool AllReady { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetGpuChildren_Decide_VirtualGeometry_World_PlanetGpuResidency_System_Int32_System_Int32_System_Boolean_System_Boolean_"></a> Decide\(PlanetGpuResidency, int, int, bool, bool\)

```csharp
public PlanetGpuSplitDecision Decide(PlanetGpuResidency parentState, int level, int maximumLevel, bool budgetAllows, bool seamsAllow)
```

#### 引数（Parameters）

`parentState` [PlanetGpuResidency](VirtualGeometry.World.PlanetGpuResidency.md)

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`maximumLevel` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`budgetAllows` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`seamsAllow` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [PlanetGpuSplitDecision](VirtualGeometry.World.PlanetGpuSplitDecision.md)

### <a id="VirtualGeometry_World_PlanetGpuChildren_Inspect_VirtualGeometry_World_PlanetGpuResidencyTable_VirtualGeometry_World_PlanetGpuKey_System_UInt32_System_ReadOnlySpan_System_UInt32__"></a> Inspect\(PlanetGpuResidencyTable, PlanetGpuKey, uint, ReadOnlySpan<uint\>\)

```csharp
public static PlanetGpuChildren Inspect(PlanetGpuResidencyTable table, PlanetGpuKey parent, uint epoch, ReadOnlySpan<uint> generations)
```

#### 引数（Parameters）

`table` [PlanetGpuResidencyTable](VirtualGeometry.World.PlanetGpuResidencyTable.md)

`parent` [PlanetGpuKey](VirtualGeometry.World.PlanetGpuKey.md)

`epoch` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`generations` [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[uint](https://learn.microsoft.com/dotnet/api/system.uint32)\>

#### 戻り値（Returns）

 [PlanetGpuChildren](VirtualGeometry.World.PlanetGpuChildren.md)
