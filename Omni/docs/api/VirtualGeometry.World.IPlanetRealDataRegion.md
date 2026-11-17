# <a id="VirtualGeometry_World_IPlanetRealDataRegion"></a> Interface IPlanetRealDataRegion

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

実データの細かさを知らせる層。その範囲では、実データが表せる長い波長の手続きの細部を足さない(<xref href="VirtualGeometry.World.PlanetDetailBandSuppression" data-throw-if-not-resolved="false"></xref>)。

```csharp
public interface IPlanetRealDataRegion
```

## メソッド（Methods）

### <a id="VirtualGeometry_World_IPlanetRealDataRegion_SampleRegionWeight_System_Double_System_Double_System_Double_System_Double__"></a> SampleRegionWeight\(double, double, double, out double\)

範囲の重み(0〜1。範囲の外は 0)と、実データが表せる最短の波長(m)。

```csharp
double SampleRegionWeight(double unitX, double unitY, double unitZ, out double resolvedWavelengthMeters)
```

#### 引数（Parameters）

`unitX` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitY` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitZ` [double](https://learn.microsoft.com/dotnet/api/system.double)

`resolvedWavelengthMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)
