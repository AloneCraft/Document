# <a id="VirtualGeometry_World_PlanetDetailBandSuppression"></a> Class PlanetDetailBandSuppression

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

実データの範囲(<xref href="VirtualGeometry.World.IPlanetRealDataRegion" data-throw-if-not-resolved="false"></xref>)で、増幅の細部(<xref href="VirtualGeometry.World.PlanetAmplifiedHeightProvider" data-throw-if-not-resolved="false"></xref> の鎖)のうち、
実データが表せる長い波長の octave を引く(本物の起伏の上に偽の起伏を二重に足さない)。範囲の外では元の高さそのまま。
波長 λ の octave を引く割合は、範囲の重み × smoothstep((λ − 実データの波長) / 実データの波長)(λ が実データの波長の 2 倍以上で全部引く)。
増幅の部品そのものは変えない(GPU 生成と前もって帯域を選ぶ経路は増幅の部品を直接ほどくため)。

```csharp
public sealed class PlanetDetailBandSuppression : IPlanetShadingHeightProvider, IThreadSafePlanetHeightProvider, IPlanetHeightProvider
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetDetailBandSuppression](VirtualGeometry.World.PlanetDetailBandSuppression.md)

#### 実装するインターフェース（Implements）

[IPlanetShadingHeightProvider](VirtualGeometry.World.IPlanetShadingHeightProvider.md), 
[IThreadSafePlanetHeightProvider](VirtualGeometry.World.IThreadSafePlanetHeightProvider.md), 
[IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetDetailBandSuppression__ctor_VirtualGeometry_World_IPlanetHeightProvider_VirtualGeometry_World_IPlanetRealDataRegion___"></a> PlanetDetailBandSuppression\(IPlanetHeightProvider, params IPlanetRealDataRegion\[\]\)

```csharp
public PlanetDetailBandSuppression(IPlanetHeightProvider inner, params IPlanetRealDataRegion[] regions)
```

#### 引数（Parameters）

`inner` [IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

増幅の部品の鎖(一番外側が増幅でなくてもよい。鎖の中の増幅の部品を全部対象にする)。

`regions` [IPlanetRealDataRegion](VirtualGeometry.World.IPlanetRealDataRegion.md)\[\]

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetDetailBandSuppression_Inner"></a> Inner

```csharp
public IPlanetHeightProvider Inner { get; }
```

#### 値（Property Value）

 [IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

### <a id="VirtualGeometry_World_PlanetDetailBandSuppression_MaximumAbsoluteHeightMeters"></a> MaximumAbsoluteHeightMeters

高さの絶対値の上界(m)。Cell の選択の bounds に含める。

```csharp
public double MaximumAbsoluteHeightMeters { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetDetailBandSuppression_SampleHeightMeters_System_Double_System_Double_System_Double_System_Double_"></a> SampleHeightMeters\(double, double, double, double\)

```csharp
public double SampleHeightMeters(double unitX, double unitY, double unitZ, double spacingMeters)
```

#### 引数（Parameters）

`unitX` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitY` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitZ` [double](https://learn.microsoft.com/dotnet/api/system.double)

`spacingMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetDetailBandSuppression_SampleShadingHeightMeters_System_Double_System_Double_System_Double_System_Double_"></a> SampleShadingHeightMeters\(double, double, double, double\)

```csharp
public double SampleShadingHeightMeters(double unitX, double unitY, double unitZ, double spacingMeters)
```

#### 引数（Parameters）

`unitX` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitY` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitZ` [double](https://learn.microsoft.com/dotnet/api/system.double)

`spacingMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetDetailBandSuppression_SuppressedDetailMeters_System_Double_System_Double_System_Double_System_Double_"></a> SuppressedDetailMeters\(double, double, double, double\)

この方向で引く細部の高さ(m)。範囲の外では 0。

```csharp
public double SuppressedDetailMeters(double unitX, double unitY, double unitZ, double spacingMeters)
```

#### 引数（Parameters）

`unitX` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitY` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitZ` [double](https://learn.microsoft.com/dotnet/api/system.double)

`spacingMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)
