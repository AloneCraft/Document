# <a id="VirtualGeometry_World_IPlanetGridHeightSource"></a> Interface IPlanetGridHeightSource

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

Cellの物理的な範囲と格子の分解能を分け、N=8/16/64のhalo全体を供給する契約。

```csharp
public interface IPlanetGridHeightSource : IPlanetCellHeightSource
```

#### 実装するインターフェース（Implements）

[IPlanetCellHeightSource](VirtualGeometry.World.IPlanetCellHeightSource.md)

## メソッド（Methods）

### <a id="VirtualGeometry_World_IPlanetGridHeightSource_TryGetRingHeights_VirtualGeometry_World_PlanetCellFrame__System_Int32_System_Single_System_Double___System_Double___System_Boolean__"></a> TryGetRingHeights\(in PlanetCellFrame, int, float, double\[\], double\[\], out bool\)

```csharp
PlanetCellHeightStatus TryGetRingHeights(in PlanetCellFrame frame, int gridQuads, float priority, double[] ringHeights, double[] shadingHeights, out bool hasShading)
```

#### 引数（Parameters）

`frame` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

`gridQuads` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`priority` [float](https://learn.microsoft.com/dotnet/api/system.single)

`ringHeights` [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]

`shadingHeights` [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]

`hasShading` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [PlanetCellHeightStatus](VirtualGeometry.World.PlanetCellHeightStatus.md)
