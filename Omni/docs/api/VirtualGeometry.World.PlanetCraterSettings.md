# <a id="VirtualGeometry_World_PlanetCraterSettings"></a> Struct PlanetCraterSettings

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

生成クレーターの分布の値(天体ごと。同じ天体はどのデモでも同じ値)。
段 0 が最も大きい(最小直径 = 最も小さい段の最小直径 × 2^(段の数 − 1))。各段の最小直径 dMin の 3 次元の格子(1 辺 4dMin)に候補を 1 つ置く。

```csharp
public readonly struct PlanetCraterSettings
```

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetCraterSettings__ctor_System_UInt32_System_Int32_System_Double_System_Double_"></a> PlanetCraterSettings\(uint, int, double, double\)

```csharp
public PlanetCraterSettings(uint seed, int levels, double smallestDiameterMeters, double equilibriumLimitMeters)
```

#### 引数（Parameters）

`seed` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`levels` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`smallestDiameterMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

`equilibriumLimitMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetCraterSettings_EquilibriumLimitMeters"></a> EquilibriumLimitMeters

平衡分布に従う最後の段の最小直径(m)。これより大きい段は生成分布(1 段ごとにさらに半分)。

```csharp
public readonly double EquilibriumLimitMeters
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetCraterSettings_Levels"></a> Levels

段の数(最大 <xref href="VirtualGeometry.World.PlanetCraterField.MaximumLevels" data-throw-if-not-resolved="false"></xref>)。

```csharp
public readonly int Levels
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetCraterSettings_Seed"></a> Seed

```csharp
public readonly uint Seed
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualGeometry_World_PlanetCraterSettings_SmallestDiameterMeters"></a> SmallestDiameterMeters

最も小さい段の最小直径(m)。

```csharp
public readonly double SmallestDiameterMeters
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)
