# <a id="VirtualGeometry_World_PlanetGpuHeightBasis"></a> Class PlanetGpuHeightBasis

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

元データの寿命から独立した係数。係数は各々の中心高さとの差を表す。

```csharp
public sealed class PlanetGpuHeightBasis
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetGpuHeightBasis](VirtualGeometry.World.PlanetGpuHeightBasis.md)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetGpuHeightBasis__ctor_System_Double_System_Double_VirtualGeometry_World_PlanetGpuCubicPatch___VirtualGeometry_World_PlanetGpuCubicPatch___"></a> PlanetGpuHeightBasis\(double, double, PlanetGpuCubicPatch\[\], PlanetGpuCubicPatch\[\]\)

```csharp
public PlanetGpuHeightBasis(double geometryCenter, double shadingCenter, PlanetGpuCubicPatch[] geometryPatches = null, PlanetGpuCubicPatch[] shadingPatches = null)
```

#### 引数（Parameters）

`geometryCenter` [double](https://learn.microsoft.com/dotnet/api/system.double)

`shadingCenter` [double](https://learn.microsoft.com/dotnet/api/system.double)

`geometryPatches` [PlanetGpuCubicPatch](VirtualGeometry.World.PlanetGpuCubicPatch.md)\[\]

`shadingPatches` [PlanetGpuCubicPatch](VirtualGeometry.World.PlanetGpuCubicPatch.md)\[\]

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetGpuHeightBasis_GeometryCenter"></a> GeometryCenter

```csharp
public double GeometryCenter { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetGpuHeightBasis_GeometryPatches"></a> GeometryPatches

```csharp
public ReadOnlySpan<PlanetGpuCubicPatch> GeometryPatches { get; }
```

#### 値（Property Value）

 [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[PlanetGpuCubicPatch](VirtualGeometry.World.PlanetGpuCubicPatch.md)\>

### <a id="VirtualGeometry_World_PlanetGpuHeightBasis_ShadingCenter"></a> ShadingCenter

```csharp
public double ShadingCenter { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetGpuHeightBasis_ShadingPatches"></a> ShadingPatches

```csharp
public ReadOnlySpan<PlanetGpuCubicPatch> ShadingPatches { get; }
```

#### 値（Property Value）

 [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[PlanetGpuCubicPatch](VirtualGeometry.World.PlanetGpuCubicPatch.md)\>
