# <a id="VirtualGeometry_World_PlanetGpuSelectionView"></a> Class PlanetGpuSelectionView

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

1 roundの有限なview定数。planesと写像の値は送信時に固定し、別viewの再利用で混ぜない。

```csharp
public sealed class PlanetGpuSelectionView
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetGpuSelectionView](VirtualGeometry.World.PlanetGpuSelectionView.md)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetGpuSelectionView__ctor_VirtualGeometry_World_PlanetCellSelector_VirtualGeometry_World_PlanetSelectionView__"></a> PlanetGpuSelectionView\(PlanetCellSelector, in PlanetSelectionView\)

```csharp
public PlanetGpuSelectionView(PlanetCellSelector selector, in PlanetSelectionView view)
```

#### 引数（Parameters）

`selector` [PlanetCellSelector](VirtualGeometry.World.PlanetCellSelector.md)

`view` [PlanetSelectionView](VirtualGeometry.World.PlanetSelectionView.md)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetGpuSelectionView_ErrorMetric"></a> ErrorMetric

```csharp
public PlanetErrorMetric ErrorMetric { get; }
```

#### 値（Property Value）

 [PlanetErrorMetric](VirtualGeometry.World.PlanetErrorMetric.md)

### <a id="VirtualGeometry_World_PlanetGpuSelectionView_Hysteresis"></a> Hysteresis

```csharp
public float Hysteresis { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetGpuSelectionView_MinimumGrazingSine"></a> MinimumGrazingSine

```csharp
public float MinimumGrazingSine { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetGpuSelectionView_TargetPixels"></a> TargetPixels

```csharp
public float TargetPixels { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)
