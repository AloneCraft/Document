# <a id="VirtualGeometry_World_PlanetFallbackHeightProvider"></a> Class PlanetFallbackHeightProvider

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

主の供給元が答えられない(NaN)方向だけ、予備の供給元で答える(読み込みを待つ間の接地・岩の問い合わせ用)。
VG の Cell を作る供給元には使わないこと(届いていない場所を偽の高さで作らないため)。

```csharp
public sealed class PlanetFallbackHeightProvider : IThreadSafePlanetHeightProvider, IPlanetHeightProvider
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetFallbackHeightProvider](VirtualGeometry.World.PlanetFallbackHeightProvider.md)

#### 実装するインターフェース（Implements）

[IThreadSafePlanetHeightProvider](VirtualGeometry.World.IThreadSafePlanetHeightProvider.md), 
[IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetFallbackHeightProvider__ctor_VirtualGeometry_World_IPlanetHeightProvider_VirtualGeometry_World_IPlanetHeightProvider_"></a> PlanetFallbackHeightProvider\(IPlanetHeightProvider, IPlanetHeightProvider\)

```csharp
public PlanetFallbackHeightProvider(IPlanetHeightProvider primary, IPlanetHeightProvider fallback)
```

#### 引数（Parameters）

`primary` [IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

`fallback` [IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetFallbackHeightProvider_MaximumAbsoluteHeightMeters"></a> MaximumAbsoluteHeightMeters

高さの絶対値の上界(m)。Cell の選択の bounds に含める。

```csharp
public double MaximumAbsoluteHeightMeters { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetFallbackHeightProvider_SampleHeightMeters_System_Double_System_Double_System_Double_System_Double_"></a> SampleHeightMeters\(double, double, double, double\)

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

### <a id="VirtualGeometry_World_PlanetFallbackHeightProvider_UsesFallback_System_Double_System_Double_System_Double_System_Double_"></a> UsesFallback\(double, double, double, double\)

この方向で予備を使うか(主の供給元が NaN を返すか。診断用)。

```csharp
public bool UsesFallback(double unitX, double unitY, double unitZ, double spacingMeters)
```

#### 引数（Parameters）

`unitX` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitY` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitZ` [double](https://learn.microsoft.com/dotnet/api/system.double)

`spacingMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
