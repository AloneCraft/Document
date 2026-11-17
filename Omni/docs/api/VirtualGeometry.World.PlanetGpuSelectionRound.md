# <a id="VirtualGeometry_World_PlanetGpuSelectionRound"></a> Class PlanetGpuSelectionRound

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

GPU誤差判定と子への交換結果。拒否時は前の準備済みcutを維持する。

```csharp
public sealed class PlanetGpuSelectionRound
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetGpuSelectionRound](VirtualGeometry.World.PlanetGpuSelectionRound.md)

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetGpuSelectionRound_Decisions"></a> Decisions

```csharp
public readonly PlanetGpuSelectionDecision[] Decisions
```

#### 値（Field Value）

 [PlanetGpuSelectionDecision](VirtualGeometry.World.PlanetGpuSelectionDecision.md)\[\]

### <a id="VirtualGeometry_World_PlanetGpuSelectionRound_Frontier"></a> Frontier

```csharp
public readonly PlanetGpuFrontierResult Frontier
```

#### 値（Field Value）

 [PlanetGpuFrontierResult](VirtualGeometry.World.PlanetGpuFrontierResult.md)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetGpuSelectionRound_CanPublish"></a> CanPublish

```csharp
public bool CanPublish { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetGpuSelectionRound_RejectionReason"></a> RejectionReason

```csharp
public string RejectionReason { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
