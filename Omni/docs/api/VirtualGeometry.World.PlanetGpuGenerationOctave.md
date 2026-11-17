# <a id="VirtualGeometry_World_PlanetGpuGenerationOctave"></a> Struct PlanetGpuGenerationOctave

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

1 octaveの64 bit latticeと中心端数。中心値はCPUが別に保持し、GPUは変化分だけを生成する。

```csharp
public struct PlanetGpuGenerationOctave
```

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetGpuGenerationOctave_FractionAmplitude"></a> FractionAmplitude

```csharp
public Vector4 FractionAmplitude
```

#### 値（Field Value）

 Vector4

### <a id="VirtualGeometry_World_PlanetGpuGenerationOctave_Parameters"></a> Parameters

```csharp
public Vector4 Parameters
```

#### 値（Field Value）

 Vector4

### <a id="VirtualGeometry_World_PlanetGpuGenerationOctave_Stride"></a> Stride

```csharp
public const int Stride = 64
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetGpuGenerationOctave_XY"></a> XY

```csharp
public uint4 XY
```

#### 値（Field Value）

 uint4

### <a id="VirtualGeometry_World_PlanetGpuGenerationOctave_ZSeedFlags"></a> ZSeedFlags

```csharp
public uint4 ZSeedFlags
```

#### 値（Field Value）

 uint4

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetGpuGenerationOctave_TryCreate_VirtualGeometry_World_PlanetAmplifiedHeightProvider_System_Int32_System_Double_System_Double_System_Double_System_Double_System_UInt32_VirtualGeometry_World_PlanetGpuGenerationOctave__System_Double__"></a> TryCreate\(PlanetAmplifiedHeightProvider, int, double, double, double, double, uint, out PlanetGpuGenerationOctave, out double\)

flagsのbit0=形、bit1=陰影。帯域で消えるoctave、非有限値、範囲外はfalse。

```csharp
public static bool TryCreate(PlanetAmplifiedHeightProvider layer, int octave, double ux, double uy, double uz, double spacing, uint flags, out PlanetGpuGenerationOctave result, out double centerHeight)
```

#### 引数（Parameters）

`layer` [PlanetAmplifiedHeightProvider](VirtualGeometry.World.PlanetAmplifiedHeightProvider.md)

`octave` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`ux` [double](https://learn.microsoft.com/dotnet/api/system.double)

`uy` [double](https://learn.microsoft.com/dotnet/api/system.double)

`uz` [double](https://learn.microsoft.com/dotnet/api/system.double)

`spacing` [double](https://learn.microsoft.com/dotnet/api/system.double)

`flags` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`result` [PlanetGpuGenerationOctave](VirtualGeometry.World.PlanetGpuGenerationOctave.md)

`centerHeight` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
