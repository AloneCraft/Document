# <a id="VirtualGeometry_World_PlanetGradientNoise"></a> Class PlanetGradientNoise

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

3 次元の gradient noise(Perlin 型、quintic の補間)。格子の番号は 64 ビットの整数(床関数)、端数は double。値の範囲は ±<xref href="VirtualGeometry.World.PlanetGradientNoise.MaximumMagnitude" data-throw-if-not-resolved="false"></xref>。
hash は uint の演算だけ(GPU へ移すときも同じ値になる)。

```csharp
public static class PlanetGradientNoise
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetGradientNoise](VirtualGeometry.World.PlanetGradientNoise.md)

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetGradientNoise_MaximumMagnitude"></a> MaximumMagnitude

|値| の上界(12 方向の gradient で √3/… を超えない保守的な値)。

```csharp
public const double MaximumMagnitude = 1
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetGradientNoise_Hash_System_Int64_System_Int64_System_Int64_System_UInt32_"></a> Hash\(long, long, long, uint\)

```csharp
public static uint Hash(long x, long y, long z, uint seed)
```

#### 引数（Parameters）

`x` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`y` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`z` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`seed` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

#### 戻り値（Returns）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualGeometry_World_PlanetGradientNoise_Mix_System_UInt32_"></a> Mix\(uint\)

uint の混ぜ合わせ(lowbias32)。

```csharp
public static uint Mix(uint x)
```

#### 引数（Parameters）

`x` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

#### 戻り値（Returns）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualGeometry_World_PlanetGradientNoise_Sample_System_Double_System_Double_System_Double_System_UInt32_"></a> Sample\(double, double, double, uint\)

```csharp
public static double Sample(double x, double y, double z, uint seed)
```

#### 引数（Parameters）

`x` [double](https://learn.microsoft.com/dotnet/api/system.double)

`y` [double](https://learn.microsoft.com/dotnet/api/system.double)

`z` [double](https://learn.microsoft.com/dotnet/api/system.double)

`seed` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)
