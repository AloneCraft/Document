# <a id="VirtualGeometry_World_PlanetGpuSelectionDecision"></a> Struct PlanetGpuSelectionDecision

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

GPUが求めた画素誤差と分割hint。Visible=falseのnodeも被覆のため親として候補に残る。

```csharp
public struct PlanetGpuSelectionDecision
```

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetGpuSelectionDecision_Error"></a> Error

```csharp
public float Error
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetGpuSelectionDecision_Hint"></a> Hint

```csharp
public uint Hint
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualGeometry_World_PlanetGpuSelectionDecision_Ordinal"></a> Ordinal

```csharp
public uint Ordinal
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualGeometry_World_PlanetGpuSelectionDecision_Stride"></a> Stride

```csharp
public const int Stride = 16
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetGpuSelectionDecision_Visible"></a> Visible

```csharp
public uint Visible
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)
