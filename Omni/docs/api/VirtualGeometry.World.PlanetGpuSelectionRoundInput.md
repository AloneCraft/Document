# <a id="VirtualGeometry_World_PlanetGpuSelectionRoundInput"></a> Class PlanetGpuSelectionRoundInput

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

重複/祖先子孫の重なりを検査した1 round入力。全cutの最終controllerではない。

```csharp
public sealed class PlanetGpuSelectionRoundInput
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetGpuSelectionRoundInput](VirtualGeometry.World.PlanetGpuSelectionRoundInput.md)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetGpuSelectionRoundInput__ctor_VirtualGeometry_World_PlanetGpuFrontierNode___VirtualGeometry_World_PlanetGpuSelectionSample___VirtualGeometry_World_PlanetGpuSelectionView_System_Int32_System_Int32_System_Int32_System_Int32_System_Int32_"></a> PlanetGpuSelectionRoundInput\(PlanetGpuFrontierNode\[\], PlanetGpuSelectionSample\[\], PlanetGpuSelectionView, int, int, int, int, int\)

```csharp
public PlanetGpuSelectionRoundInput(PlanetGpuFrontierNode[] nodes, PlanetGpuSelectionSample[] samples, PlanetGpuSelectionView view, int leafBudget, int outputCapacity, int requestCapacity, int anchorCount, int maximumLevel)
```

#### 引数（Parameters）

`nodes` [PlanetGpuFrontierNode](VirtualGeometry.World.PlanetGpuFrontierNode.md)\[\]

`samples` [PlanetGpuSelectionSample](VirtualGeometry.World.PlanetGpuSelectionSample.md)\[\]

`view` [PlanetGpuSelectionView](VirtualGeometry.World.PlanetGpuSelectionView.md)

`leafBudget` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`outputCapacity` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`requestCapacity` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`anchorCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`maximumLevel` [int](https://learn.microsoft.com/dotnet/api/system.int32)

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetGpuSelectionRoundInput_AnchorCount"></a> AnchorCount

```csharp
public readonly int AnchorCount
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetGpuSelectionRoundInput_LeafBudget"></a> LeafBudget

```csharp
public readonly int LeafBudget
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetGpuSelectionRoundInput_MaximumLevel"></a> MaximumLevel

```csharp
public readonly int MaximumLevel
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetGpuSelectionRoundInput_OutputCapacity"></a> OutputCapacity

```csharp
public readonly int OutputCapacity
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetGpuSelectionRoundInput_RequestCapacity"></a> RequestCapacity

```csharp
public readonly int RequestCapacity
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetGpuSelectionRoundInput_View"></a> View

```csharp
public readonly PlanetGpuSelectionView View
```

#### 値（Field Value）

 [PlanetGpuSelectionView](VirtualGeometry.World.PlanetGpuSelectionView.md)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetGpuSelectionRoundInput_Count"></a> Count

```csharp
public int Count { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)
