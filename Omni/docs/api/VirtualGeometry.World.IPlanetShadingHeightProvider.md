# <a id="VirtualGeometry_World_IPlanetShadingHeightProvider"></a> Interface IPlanetShadingHeightProvider

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

頂点の法線に、形とは別の高さを使う供給元(形には入れるが、陰影は画素ごとに別に付ける細部を、法線へ二重に入れないため)。
実装しない供給元では、法線も形と同じ高さから求める。

```csharp
public interface IPlanetShadingHeightProvider : IPlanetHeightProvider
```

#### 実装するインターフェース（Implements）

[IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

## メソッド（Methods）

### <a id="VirtualGeometry_World_IPlanetShadingHeightProvider_SampleShadingHeightMeters_System_Double_System_Double_System_Double_System_Double_"></a> SampleShadingHeightMeters\(double, double, double, double\)

```csharp
double SampleShadingHeightMeters(double unitX, double unitY, double unitZ, double spacingMeters)
```

#### 引数（Parameters）

`unitX` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitY` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitZ` [double](https://learn.microsoft.com/dotnet/api/system.double)

`spacingMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)
