# <a id="VirtualGeometry_World_PlanetHeightShiftProvider"></a> Delegate PlanetHeightShiftProvider

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

Cell の原点を半径 R の球面から外向きに持ち上げる高さ(m)を返す。sphereFrame は持ち上げていない Cell の値。
同じ Cell には常に同じ値を返すこと(選択の bounds と、生成した頂点の基準が一致する前提)。false または 0 なら持ち上げない。

```csharp
public delegate bool PlanetHeightShiftProvider(in PlanetCellFrame sphereFrame, out float shift)
```

#### 引数（Parameters）

`sphereFrame` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

`shift` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
