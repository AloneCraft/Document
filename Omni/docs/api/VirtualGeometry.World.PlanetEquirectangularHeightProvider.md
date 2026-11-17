# <a id="VirtualGeometry_World_PlanetEquirectangularHeightProvider"></a> Class PlanetEquirectangularHeightProvider

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

正距円筒(緯度経度)の格子の標高(m)を、方向から求める供給元(<xref href="VirtualGeometry.World.IPlanetHeightProvider" data-throw-if-not-resolved="false"></xref>)。
格子は北の行から南へ、経度 −180° の列から東へ、画素の中心が格子点(LOLA などの全球の地図の並び)。
方向の規約: +Y が北極、+X が経度 0°、+Z が経度 +90°(経度 = atan2(z, x)、緯度 = asin(y))。別の規約の天体は、呼び出し側で軸を入れ替える。
帯域制限: 格子を 2×2 ずつ平均した mip を作り、メッシュの間隔が赤道の 1 画素より広いときは、間隔に合う 2 つの mip を補間する
(粗い Cell が細かい起伏を拾って遠景がちらつかない。間隔 0 は元の格子の双線形補間)。
値は呼び出し側が持つ配列から作り(コピーする)、作った後は変えない。スレッドから同時に呼んでよい。

```csharp
public sealed class PlanetEquirectangularHeightProvider : IPlanetHeightBoundsSource, IThreadSafePlanetHeightProvider, IPlanetHeightProvider
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetEquirectangularHeightProvider](VirtualGeometry.World.PlanetEquirectangularHeightProvider.md)

#### 実装するインターフェース（Implements）

[IPlanetHeightBoundsSource](VirtualGeometry.World.IPlanetHeightBoundsSource.md), 
[IThreadSafePlanetHeightProvider](VirtualGeometry.World.IThreadSafePlanetHeightProvider.md), 
[IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetEquirectangularHeightProvider__ctor_System_Single___System_Int32_System_Int32_System_Double_"></a> PlanetEquirectangularHeightProvider\(float\[\], int, int, double\)

```csharp
public PlanetEquirectangularHeightProvider(float[] values, int width, int height, double radiusMeters)
```

#### 引数（Parameters）

`values` [float](https://learn.microsoft.com/dotnet/api/system.single)\[\]

`width` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`height` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`radiusMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetEquirectangularHeightProvider_Height"></a> Height

```csharp
public int Height { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetEquirectangularHeightProvider_MaximumAbsoluteHeightMeters"></a> MaximumAbsoluteHeightMeters

高さの絶対値の上界(m)。Cell の選択の bounds に含める。

```csharp
public double MaximumAbsoluteHeightMeters { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetEquirectangularHeightProvider_MipCount"></a> MipCount

```csharp
public int MipCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetEquirectangularHeightProvider_TexelMeters"></a> TexelMeters

赤道での 1 画素の大きさ(m)。

```csharp
public double TexelMeters { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetEquirectangularHeightProvider_Width"></a> Width

```csharp
public int Width { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetEquirectangularHeightProvider_Downsample_System_Single___System_Int32_System_Int32_System_Int32__System_Int32__"></a> Downsample\(float\[\], int, int, out int, out int\)

格子を 2×2 ずつ平均して半分の大きさにする(大きな実データを小さくして持つとき)。幅と高さは偶数。

```csharp
public static float[] Downsample(float[] values, int width, int height, out int halfWidth, out int halfHeight)
```

#### 引数（Parameters）

`values` [float](https://learn.microsoft.com/dotnet/api/system.single)\[\]

`width` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`height` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`halfWidth` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`halfHeight` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [float](https://learn.microsoft.com/dotnet/api/system.single)\[\]

### <a id="VirtualGeometry_World_PlanetEquirectangularHeightProvider_SampleHeightMeters_System_Double_System_Double_System_Double_System_Double_"></a> SampleHeightMeters\(double, double, double, double\)

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

### <a id="VirtualGeometry_World_PlanetEquirectangularHeightProvider_TryGetHeightRange_VirtualGeometry_World_PlanetCellFrame__System_Double_System_Double__System_Double__"></a> TryGetHeightRange\(in PlanetCellFrame, double, out double, out double\)

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
