# <a id="VirtualGeometry_World_IPlanetCellHeightBoundsSource"></a> Interface IPlanetCellHeightBoundsSource

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

```csharp
public interface IPlanetCellHeightBoundsSource
```

## メソッド（Methods）

### <a id="VirtualGeometry_World_IPlanetCellHeightBoundsSource_GetHeightRange_VirtualGeometry_World_PlanetCellKey__System_Int32_System_Double__System_Double__"></a> GetHeightRange\(in PlanetCellKey, int, out double, out double\)

```csharp
PlanetCellHeightStatus GetHeightRange(in PlanetCellKey key, int gridQuads, out double minimum, out double maximum)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

`gridQuads` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`minimum` [double](https://learn.microsoft.com/dotnet/api/system.double)

`maximum` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [PlanetCellHeightStatus](VirtualGeometry.World.PlanetCellHeightStatus.md)
