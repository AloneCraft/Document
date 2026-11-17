# <a id="VirtualGeometry_World_IPlanetHeightBoundsSource"></a> Interface IPlanetHeightBoundsSource

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

main threadの選択用。取得やdecodeを行わず、現在保証できる高さの範囲だけを返す。

```csharp
public interface IPlanetHeightBoundsSource
```

## メソッド（Methods）

### <a id="VirtualGeometry_World_IPlanetHeightBoundsSource_TryGetHeightRange_VirtualGeometry_World_PlanetCellFrame__System_Double_System_Double__System_Double__"></a> TryGetHeightRange\(in PlanetCellFrame, double, out double, out double\)

```csharp
bool TryGetHeightRange(in PlanetCellFrame frame, double spacing, out double minimum, out double maximum)
```

#### 引数（Parameters）

`frame` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

`spacing` [double](https://learn.microsoft.com/dotnet/api/system.double)

`minimum` [double](https://learn.microsoft.com/dotnet/api/system.double)

`maximum` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
