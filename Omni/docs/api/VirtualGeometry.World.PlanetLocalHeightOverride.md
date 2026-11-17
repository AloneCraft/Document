# <a id="VirtualGeometry_World_PlanetLocalHeightOverride"></a> Class PlanetLocalHeightOverride

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

中心の方向と東の方向で決まる局所の長方形(東・北の弧長、m)を書き換える層。縁の feather の幅で滑らかに元へ戻す(縁の傾きは 0)。
sample は東・北の弧長(m)からその場所の高さ(m)を返す関数で、寿命中に変わらず、複数のスレッドから同時に呼べること。

```csharp
public sealed class PlanetLocalHeightOverride : IPlanetHeightOverride, IPlanetRealDataRegion
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetLocalHeightOverride](VirtualGeometry.World.PlanetLocalHeightOverride.md)

#### 実装するインターフェース（Implements）

[IPlanetHeightOverride](VirtualGeometry.World.IPlanetHeightOverride.md), 
[IPlanetRealDataRegion](VirtualGeometry.World.IPlanetRealDataRegion.md)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetLocalHeightOverride__ctor_System_Double_VirtualGeometry_World_PlanetDouble3_VirtualGeometry_World_PlanetDouble3_System_Double_System_Double_System_Double_System_Func_System_Double_System_Double_System_Double__System_Double_System_String_System_Boolean_System_Double_"></a> PlanetLocalHeightOverride\(double, PlanetDouble3, PlanetDouble3, double, double, double, Func<double, double, double\>, double, string, bool, double\)

```csharp
public PlanetLocalHeightOverride(double radius, PlanetDouble3 center, PlanetDouble3 east, double halfEast, double halfNorth, double feather, Func<double, double, double> sample, double maximumAbsoluteHeightMeters, string contentHash, bool clearScatter, double resolvedWavelengthMeters = 0)
```

#### 引数（Parameters）

`radius` [double](https://learn.microsoft.com/dotnet/api/system.double)

天体の基準半径(m)。弧長の尺度。

`center` [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

長方形の中心の方向(天体のローカル座標)。

`east` [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

東の方向(中心に直交していなくてよい。直交成分を使う)。

`halfEast` [double](https://learn.microsoft.com/dotnet/api/system.double)

東西の半幅(m)。

`halfNorth` [double](https://learn.microsoft.com/dotnet/api/system.double)

南北の半幅(m)。

`feather` [double](https://learn.microsoft.com/dotnet/api/system.double)

縁で元へ戻す幅(m)。

`sample` [Func](https://learn.microsoft.com/dotnet/api/system.func\-3)<[double](https://learn.microsoft.com/dotnet/api/system.double), [double](https://learn.microsoft.com/dotnet/api/system.double), [double](https://learn.microsoft.com/dotnet/api/system.double)\>

東・北の弧長(m)→高さ(m)。

`maximumAbsoluteHeightMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

sample が返す高さの絶対値の上界(m)。超えたら例外。

`contentHash` [string](https://learn.microsoft.com/dotnet/api/system.string)

sample のデータの内容 hash(キャッシュの識別子へ入れる)。

`clearScatter` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

true なら、書き換えた範囲に岩などを置かない(ScatterWeight を下げる)。

`resolvedWavelengthMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

実データが表せる最短の波長(m)。正の値なら、範囲の中ではこれより長い手続きの細部を足さない。0 なら知らせない。

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetLocalHeightOverride_CacheIdentity"></a> CacheIdentity

```csharp
public string CacheIdentity { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualGeometry_World_PlanetLocalHeightOverride_MaximumAbsoluteHeightMeters"></a> MaximumAbsoluteHeightMeters

```csharp
public double MaximumAbsoluteHeightMeters { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetLocalHeightOverride_RadiusMeters"></a> RadiusMeters

```csharp
public double RadiusMeters { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetLocalHeightOverride_Locate_System_Double_System_Double_System_Double_System_Double__System_Double__"></a> Locate\(double, double, double, out double, out double\)

方向の東・北の弧長(m)と、長方形の重み(0〜1)。裏側は重み 0。

```csharp
public double Locate(double unitX, double unitY, double unitZ, out double east, out double north)
```

#### 引数（Parameters）

`unitX` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitY` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitZ` [double](https://learn.microsoft.com/dotnet/api/system.double)

`east` [double](https://learn.microsoft.com/dotnet/api/system.double)

`north` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetLocalHeightOverride_Sample_System_Double_System_Double_System_Double_"></a> Sample\(double, double, double\)

```csharp
public PlanetHeightBlend Sample(double unitX, double unitY, double unitZ)
```

#### 引数（Parameters）

`unitX` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitY` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitZ` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [PlanetHeightBlend](VirtualGeometry.World.PlanetHeightBlend.md)

### <a id="VirtualGeometry_World_PlanetLocalHeightOverride_SampleRegionWeight_System_Double_System_Double_System_Double_System_Double__"></a> SampleRegionWeight\(double, double, double, out double\)

範囲の重み(0〜1。範囲の外は 0)と、実データが表せる最短の波長(m)。

```csharp
public double SampleRegionWeight(double unitX, double unitY, double unitZ, out double resolvedWavelengthMeters)
```

#### 引数（Parameters）

`unitX` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitY` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitZ` [double](https://learn.microsoft.com/dotnet/api/system.double)

`resolvedWavelengthMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)
