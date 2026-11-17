# <a id="VirtualGeometry_World_IPlanetGpuHeightInputSource"></a> Interface IPlanetGpuHeightInputSource

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

ノイズを足す前の高さを、halo付きの三次係数へ写す供給元。Sceneや惑星の種類には依存しない。

```csharp
public interface IPlanetGpuHeightInputSource : IPlanetHeightProvider
```

#### 実装するインターフェース（Implements）

[IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

## メソッド（Methods）

### <a id="VirtualGeometry_World_IPlanetGpuHeightInputSource_PrepareGpuHeightInput_VirtualGeometry_World_PlanetCellFrame__System_Int32_System_Double_System_Int32_VirtualGeometry_World_PlanetGpuHeightBasis__System_String__"></a> PrepareGpuHeightInput\(in PlanetCellFrame, int, double, int, out PlanetGpuHeightBasis, out string\)

```csharp
PlanetGpuHeightInputStatus PrepareGpuHeightInput(in PlanetCellFrame frame, int gridQuads, double spacingMeters, int maximumPatches, out PlanetGpuHeightBasis input, out string reason)
```

#### 引数（Parameters）

`frame` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

`gridQuads` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`spacingMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

`maximumPatches` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`input` [PlanetGpuHeightBasis](VirtualGeometry.World.PlanetGpuHeightBasis.md)

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [PlanetGpuHeightInputStatus](VirtualGeometry.World.PlanetGpuHeightInputStatus.md)
