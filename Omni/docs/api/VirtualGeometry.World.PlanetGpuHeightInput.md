# <a id="VirtualGeometry_World_PlanetGpuHeightInput"></a> Class PlanetGpuHeightInput

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

1 Cellの中心差・係数・octave。CPUの頂点全体を作らず、GPU生成へ入力する。

```csharp
public sealed class PlanetGpuHeightInput
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetGpuHeightInput](VirtualGeometry.World.PlanetGpuHeightInput.md)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetGpuHeightInput_Basis"></a> Basis

```csharp
public PlanetGpuHeightBasis Basis { get; }
```

#### 値（Property Value）

 [PlanetGpuHeightBasis](VirtualGeometry.World.PlanetGpuHeightBasis.md)

### <a id="VirtualGeometry_World_PlanetGpuHeightInput_GeometryCenter"></a> GeometryCenter

```csharp
public double GeometryCenter { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetGpuHeightInput_Octaves"></a> Octaves

```csharp
public ReadOnlySpan<PlanetGpuGenerationOctave> Octaves { get; }
```

#### 値（Property Value）

 [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[PlanetGpuGenerationOctave](VirtualGeometry.World.PlanetGpuGenerationOctave.md)\>

### <a id="VirtualGeometry_World_PlanetGpuHeightInput_ShadingCenter"></a> ShadingCenter

```csharp
public double ShadingCenter { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetGpuHeightInput_Prepare_VirtualGeometry_World_IPlanetHeightProvider_VirtualGeometry_World_PlanetCellFrame__System_Single_System_Int32_System_Double_System_Int32_System_Int32_VirtualGeometry_World_PlanetGpuHeightInput__System_String__"></a> Prepare\(IPlanetHeightProvider, in PlanetCellFrame, float, int, double, int, int, out PlanetGpuHeightInput, out string\)

形だけのノイズと、陰影にも入るノイズをCPUの供給元と同じ順序で区別する。

```csharp
public static PlanetGpuHeightInputStatus Prepare(IPlanetHeightProvider provider, in PlanetCellFrame frame, float radius, int n, double spacing, int maximumPatches, int maximumOctaves, out PlanetGpuHeightInput input, out string reason)
```

#### 引数（Parameters）

`provider` [IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

`frame` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

`radius` [float](https://learn.microsoft.com/dotnet/api/system.single)

`n` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`spacing` [double](https://learn.microsoft.com/dotnet/api/system.double)

`maximumPatches` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`maximumOctaves` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`input` [PlanetGpuHeightInput](VirtualGeometry.World.PlanetGpuHeightInput.md)

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [PlanetGpuHeightInputStatus](VirtualGeometry.World.PlanetGpuHeightInputStatus.md)
