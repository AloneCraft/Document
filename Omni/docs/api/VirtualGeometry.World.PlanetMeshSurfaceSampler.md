# <a id="VirtualGeometry_World_PlanetMeshSurfaceSampler"></a> Class PlanetMeshSurfaceSampler

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

描画と同じfloat頂点・三角形から、指定方向の地表高を求める。全帯域の高さ場の直接評価を接地の代用にしない。
Moon/OldMoon の視点と、手続きメッシュproducerの接地問い合わせで使用する。

```csharp
public static class PlanetMeshSurfaceSampler
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetMeshSurfaceSampler](VirtualGeometry.World.PlanetMeshSurfaceSampler.md)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetMeshSurfaceSampler_TrySample_VirtualGeometry_World_PlanetCellFrame__System_Double_System_Int32_VirtualGeometry_World_IPlanetHeightProvider_System_ReadOnlySpan_System_Double__Omni_Logical_Vector3__System_Double__System_Double_"></a> TrySample\(in PlanetCellFrame, double, int, IPlanetHeightProvider, ReadOnlySpan<double\>, in Vector3, out double, double\)

```csharp
public static bool TrySample(in PlanetCellFrame frame, double radius, int quads, IPlanetHeightProvider provider, ReadOnlySpan<double> ringHeights, in Vector3 point, out double height, double spacingMeters = NaN)
```

#### 引数（Parameters）

`frame` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

`radius` [double](https://learn.microsoft.com/dotnet/api/system.double)

`quads` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`provider` [IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

`ringHeights` [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[double](https://learn.microsoft.com/dotnet/api/system.double)\>

`point` Vector3

`height` [double](https://learn.microsoft.com/dotnet/api/system.double)

`spacingMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
