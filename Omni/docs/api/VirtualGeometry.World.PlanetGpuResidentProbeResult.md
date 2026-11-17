# <a id="VirtualGeometry_World_PlanetGpuResidentProbeResult"></a> Struct PlanetGpuResidentProbeResult

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

GPU選択が読むsnapshotの照合結果。現在の描画cutの公開許可ではない。

```csharp
public struct PlanetGpuResidentProbeResult
```

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetGpuResidentProbeResult_Identity"></a> Identity

```csharp
public uint4 Identity
```

#### 値（Field Value）

 uint4

### <a id="VirtualGeometry_World_PlanetGpuResidentProbeResult_Status"></a> Status

```csharp
public uint4 Status
```

#### 値（Field Value）

 uint4

### <a id="VirtualGeometry_World_PlanetGpuResidentProbeResult_Stride"></a> Stride

```csharp
public const int Stride = 32
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetGpuResidentProbeResult_Generation"></a> Generation

```csharp
public uint Generation { get; }
```

#### 値（Property Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualGeometry_World_PlanetGpuResidentProbeResult_Residency"></a> Residency

```csharp
public PlanetGpuResidency Residency { get; }
```

#### 値（Property Value）

 [PlanetGpuResidency](VirtualGeometry.World.PlanetGpuResidency.md)

### <a id="VirtualGeometry_World_PlanetGpuResidentProbeResult_Slot"></a> Slot

```csharp
public uint Slot { get; }
```

#### 値（Property Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)
