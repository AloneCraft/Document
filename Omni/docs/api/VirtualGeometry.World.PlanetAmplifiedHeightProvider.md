# <a id="VirtualGeometry_World_PlanetAmplifiedHeightProvider"></a> Class PlanetAmplifiedHeightProvider

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

基の高さ(実データなど)に、その帯域より短い波長の細部を足す(増幅)。細部は 3 次元の gradient noise の octave の和で、
遮断波長 <xref href="VirtualGeometry.World.PlanetAmplifiedHeightProvider.CutoffWavelengthMeters" data-throw-if-not-resolved="false"></xref> の octave の振幅が <xref href="VirtualGeometry.World.PlanetAmplifiedHeightProvider.CutoffAmplitudeMeters" data-throw-if-not-resolved="false"></xref>、波長が半分になるごとに振幅が 2^−H 倍
(H は Hurst 指数 <xref href="VirtualGeometry.World.PlanetAmplifiedHeightProvider.Hurst" data-throw-if-not-resolved="false"></xref>。月の表面の粗さは 0.8〜0.9 程度)。最も短い波長は <xref href="VirtualGeometry.World.PlanetAmplifiedHeightProvider.MinimumWavelengthMeters" data-throw-if-not-resolved="false"></xref>。
帯域制限: 波長 λ の octave の重みは、λ がメッシュの間隔の 4 倍以上で 1、2 倍以下で 0、その間は滑らかにつなぐ(細かい Cell ほど octave が増える)。
noise は球面上の点 R·方向 の座標で評価し、格子の番号は 64 ビットの整数で持つ(半径 10^9 m・波長 1 mm でも番号が潰れない)。

```csharp
public sealed class PlanetAmplifiedHeightProvider : IPlanetShadingHeightProvider, IThreadSafePlanetHeightProvider, IPlanetHeightProvider, IPlanetHeightBoundsSource
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetAmplifiedHeightProvider](VirtualGeometry.World.PlanetAmplifiedHeightProvider.md)

#### 実装するインターフェース（Implements）

[IPlanetShadingHeightProvider](VirtualGeometry.World.IPlanetShadingHeightProvider.md), 
[IThreadSafePlanetHeightProvider](VirtualGeometry.World.IThreadSafePlanetHeightProvider.md), 
[IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md), 
[IPlanetHeightBoundsSource](VirtualGeometry.World.IPlanetHeightBoundsSource.md)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetAmplifiedHeightProvider__ctor_VirtualGeometry_World_IPlanetHeightProvider_System_Double_System_Double_System_Double_System_Double_System_Double_System_UInt32_"></a> PlanetAmplifiedHeightProvider\(IPlanetHeightProvider, double, double, double, double, double, uint\)

```csharp
public PlanetAmplifiedHeightProvider(IPlanetHeightProvider basis, double radiusMeters, double cutoffWavelengthMeters, double cutoffAmplitudeMeters, double hurst, double minimumWavelengthMeters, uint seed)
```

#### 引数（Parameters）

`basis` [IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

`radiusMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

`cutoffWavelengthMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

`cutoffAmplitudeMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

`hurst` [double](https://learn.microsoft.com/dotnet/api/system.double)

`minimumWavelengthMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

`seed` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetAmplifiedHeightProvider_Basis"></a> Basis

増幅前の高さ。形を保ったまま、増幅層の陰影を画素側へ分離するための読み取り口。

```csharp
public IPlanetHeightProvider Basis { get; }
```

#### 値（Property Value）

 [IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

### <a id="VirtualGeometry_World_PlanetAmplifiedHeightProvider_CutoffAmplitudeMeters"></a> CutoffAmplitudeMeters

```csharp
public double CutoffAmplitudeMeters { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetAmplifiedHeightProvider_CutoffWavelengthMeters"></a> CutoffWavelengthMeters

```csharp
public double CutoffWavelengthMeters { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetAmplifiedHeightProvider_DetailMaximumMeters"></a> DetailMaximumMeters

細部の項の絶対値の上界(m)。

```csharp
public double DetailMaximumMeters { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetAmplifiedHeightProvider_Hurst"></a> Hurst

```csharp
public double Hurst { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetAmplifiedHeightProvider_IsThreadSafe"></a> IsThreadSafe

複数のスレッドから同時に呼べるか（基の供給元も含めて）。

```csharp
public bool IsThreadSafe { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetAmplifiedHeightProvider_MaximumAbsoluteHeightMeters"></a> MaximumAbsoluteHeightMeters

高さの絶対値の上界(m)。Cell の選択の bounds に含める。

```csharp
public double MaximumAbsoluteHeightMeters { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetAmplifiedHeightProvider_MinimumWavelengthMeters"></a> MinimumWavelengthMeters

```csharp
public double MinimumWavelengthMeters { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetAmplifiedHeightProvider_Octaves"></a> Octaves

```csharp
public int Octaves { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetAmplifiedHeightProvider_RadiusMeters"></a> RadiusMeters

noise を評価する球の半径(m)と、octave の seed の元(GPU 版 PlanetGradientNoise.hlsl へ同じ値を渡すため)。

```csharp
public double RadiusMeters { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetAmplifiedHeightProvider_Seed"></a> Seed

```csharp
public uint Seed { get; }
```

#### 値（Property Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetAmplifiedHeightProvider_BandWeight_System_Double_System_Double_"></a> BandWeight\(double, double\)

波長 λ の octave の、メッシュの間隔 spacing での重み(0〜1)。spacing が 0 なら 1。

```csharp
public static double BandWeight(double wavelength, double spacing)
```

#### 引数（Parameters）

`wavelength` [double](https://learn.microsoft.com/dotnet/api/system.double)

`spacing` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetAmplifiedHeightProvider_DetailMeters_System_Double_System_Double_System_Double_System_Double_"></a> DetailMeters\(double, double, double, double\)

細部の項だけ(帯域制限あり)。

```csharp
public double DetailMeters(double unitX, double unitY, double unitZ, double spacingMeters)
```

#### 引数（Parameters）

`unitX` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitY` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitZ` [double](https://learn.microsoft.com/dotnet/api/system.double)

`spacingMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetAmplifiedHeightProvider_OctaveAmplitude_System_Int32_"></a> OctaveAmplitude\(int\)

```csharp
public double OctaveAmplitude(int k)
```

#### 引数（Parameters）

`k` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetAmplifiedHeightProvider_OctaveSeed_System_Int32_"></a> OctaveSeed\(int\)

```csharp
public uint OctaveSeed(int k)
```

#### 引数（Parameters）

`k` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualGeometry_World_PlanetAmplifiedHeightProvider_OctaveWavelength_System_Int32_"></a> OctaveWavelength\(int\)

octave k の波長(m)、振幅(m)、seed。

```csharp
public double OctaveWavelength(int k)
```

#### 引数（Parameters）

`k` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetAmplifiedHeightProvider_ResidualDetailMeters_System_Double_System_Double_System_Double_System_Double_"></a> ResidualDetailMeters\(double, double, double, double\)

メッシュの間隔より短い波長の細部だけ(<xref href="VirtualGeometry.World.PlanetAmplifiedHeightProvider.DetailMeters(System.Double%2cSystem.Double%2cSystem.Double%2cSystem.Double)" data-throw-if-not-resolved="false"></xref> で落とした残り。画素ごとの陰影用、検証用)。

```csharp
public double ResidualDetailMeters(double unitX, double unitY, double unitZ, double spacingMeters)
```

#### 引数（Parameters）

`unitX` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitY` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitZ` [double](https://learn.microsoft.com/dotnet/api/system.double)

`spacingMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetAmplifiedHeightProvider_SampleHeightMeters_System_Double_System_Double_System_Double_System_Double_"></a> SampleHeightMeters\(double, double, double, double\)

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

### <a id="VirtualGeometry_World_PlanetAmplifiedHeightProvider_SampleShadingHeightMeters_System_Double_System_Double_System_Double_System_Double_"></a> SampleShadingHeightMeters\(double, double, double, double\)

法線に使う高さ。基の供給元が陰影用の高さを持てば、それに細部を足す。

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

### <a id="VirtualGeometry_World_PlanetAmplifiedHeightProvider_TryGetHeightRange_VirtualGeometry_World_PlanetCellFrame__System_Double_System_Double__System_Double__"></a> TryGetHeightRange\(in PlanetCellFrame, double, out double, out double\)

```csharp
public bool TryGetHeightRange(in PlanetCellFrame frame, double spacing, out double minimum, out double maximum)
```

#### 引数（Parameters）

`frame` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

`spacing` [double](https://learn.microsoft.com/dotnet/api/system.double)

`minimum` [double](https://learn.microsoft.com/dotnet/api/system.double)

`maximum` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
