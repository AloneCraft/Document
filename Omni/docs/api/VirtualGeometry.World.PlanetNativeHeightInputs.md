# <a id="VirtualGeometry_World_PlanetNativeHeightInputs"></a> Class PlanetNativeHeightInputs

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

workerが作り終えた基底標高と不変の増幅係数。Native領域の所有はmainのleaseへ渡す。

```csharp
public sealed class PlanetNativeHeightInputs
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetNativeHeightInputs](VirtualGeometry.World.PlanetNativeHeightInputs.md)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetNativeHeightInputs__ctor_System_Double___System_Double___VirtualGeometry_World_PlanetHeightNoiseLayer___VirtualGeometry_World_PlanetHeightNoiseOctave___"></a> PlanetNativeHeightInputs\(double\[\], double\[\], PlanetHeightNoiseLayer\[\], PlanetHeightNoiseOctave\[\]\)

```csharp
public PlanetNativeHeightInputs(double[] heights, double[] shading, PlanetHeightNoiseLayer[] layers, PlanetHeightNoiseOctave[] octaves)
```

#### 引数（Parameters）

`heights` [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]

`shading` [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]

`layers` [PlanetHeightNoiseLayer](VirtualGeometry.World.PlanetHeightNoiseLayer.md)\[\]

`octaves` [PlanetHeightNoiseOctave](VirtualGeometry.World.PlanetHeightNoiseOctave.md)\[\]

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetNativeHeightInputs_Heights"></a> Heights

```csharp
public readonly double[] Heights
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]

### <a id="VirtualGeometry_World_PlanetNativeHeightInputs_Layers"></a> Layers

```csharp
public readonly PlanetHeightNoiseLayer[] Layers
```

#### 値（Field Value）

 [PlanetHeightNoiseLayer](VirtualGeometry.World.PlanetHeightNoiseLayer.md)\[\]

### <a id="VirtualGeometry_World_PlanetNativeHeightInputs_Octaves"></a> Octaves

```csharp
public readonly PlanetHeightNoiseOctave[] Octaves
```

#### 値（Field Value）

 [PlanetHeightNoiseOctave](VirtualGeometry.World.PlanetHeightNoiseOctave.md)\[\]

### <a id="VirtualGeometry_World_PlanetNativeHeightInputs_Shading"></a> Shading

```csharp
public readonly double[] Shading
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]
