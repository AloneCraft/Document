# <a id="VirtualGeometry_World_PlanetContactResult"></a> Struct PlanetContactResult

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

接地の結果。

```csharp
public readonly struct PlanetContactResult
```

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetContactResult__ctor_System_Double_VirtualGeometry_World_PlanetDouble3_System_Int32_System_Int32_System_Int32_"></a> PlanetContactResult\(double, PlanetDouble3, int, int, int\)

```csharp
public PlanetContactResult(double travel, PlanetDouble3 point, int kind, int bodyTriangles, int terrainTriangles)
```

#### 引数（Parameters）

`travel` [double](https://learn.microsoft.com/dotnet/api/system.double)

`point` [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

`kind` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`bodyTriangles` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`terrainTriangles` [int](https://learn.microsoft.com/dotnet/api/system.int32)

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetContactResult_BodyTriangles"></a> BodyTriangles

計算に使った物体の三角形と地形の三角形の数(診断用)。

```csharp
public readonly int BodyTriangles
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetContactResult_Kind"></a> Kind

接点の種類(0: 物体の頂点と地形の面、1: 地形の頂点と物体の面、2: 辺と辺)。

```csharp
public readonly int Kind
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetContactResult_Point"></a> Point

接点(入力の座標系、動かした後)。

```csharp
public readonly PlanetDouble3 Point
```

#### 値（Field Value）

 [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

### <a id="VirtualGeometry_World_PlanetContactResult_TerrainTriangles"></a> TerrainTriangles

計算に使った物体の三角形と地形の三角形の数(診断用)。

```csharp
public readonly int TerrainTriangles
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetContactResult_Travel"></a> Travel

物体を落下方向へ動かす距離(m)。物体はこの距離だけ動かした位置で、地形の三角形に初めて触れる。

```csharp
public readonly double Travel
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)
