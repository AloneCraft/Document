# <a id="VirtualGeometry_World_PlanetCraterKeepOut"></a> Struct PlanetCraterKeepOut

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

生成クレーターを置かない範囲。中心(天体の単位方向)から半径 RadiusMeters の円の中に中心がある、直径 MinimumDiameterMeters 以上のクレーターを置かない。
IncludeInfluence なら、クレーターの影響半径(2r)も半径に足す(施設の周りに凹みを届かせない)。実データで分かる大きさを実データの範囲に二重に足さないためにも使う。

```csharp
public readonly struct PlanetCraterKeepOut
```

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetCraterKeepOut__ctor_VirtualGeometry_World_PlanetDouble3_System_Double_System_Double_System_Boolean_"></a> PlanetCraterKeepOut\(PlanetDouble3, double, double, bool\)

```csharp
public PlanetCraterKeepOut(PlanetDouble3 direction, double radiusMeters, double minimumDiameterMeters, bool includeInfluence)
```

#### 引数（Parameters）

`direction` [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

`radiusMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

`minimumDiameterMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

`includeInfluence` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetCraterKeepOut_Direction"></a> Direction

```csharp
public readonly PlanetDouble3 Direction
```

#### 値（Field Value）

 [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

### <a id="VirtualGeometry_World_PlanetCraterKeepOut_IncludeInfluence"></a> IncludeInfluence

```csharp
public readonly bool IncludeInfluence
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetCraterKeepOut_MinimumDiameterMeters"></a> MinimumDiameterMeters

```csharp
public readonly double MinimumDiameterMeters
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetCraterKeepOut_RadiusMeters"></a> RadiusMeters

```csharp
public readonly double RadiusMeters
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)
