# <a id="VirtualGeometry_World_PlanetCraterField"></a> Class PlanetCraterField

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

天体全体の生成クレーターの場(CPU の正本。GPU 版は Shaders/PlanetCraters.hlsl で、同じ定義)。

<p>
置き方: 段ごとに天体の中心に固定した 3 次元の格子(1 辺 4dMin)を置き、各マスの中央半分に候補の点 q を 1 つ置く。q の基準球からの高さ |q| − R が
[−マス/2, マス/2) のときだけクレーターにする(基準球を通るマスの層 1 枚分なので、面積あたりの数は 1 マスあたりの期待値 ÷ マス²)。
中心は q の真下の基準球の点。高さによらず基準球の方向で置くので、地形の高さが変わってもクレーターは滑らない。
画素に届くのは各軸で近い側の 2 マス(2×2×2)。半径は dMin 未満、ゆがみを含む影響半径は 2.25r 未満で、調べないマスの候補は面に沿って 2.24dMin より遠い。
</p>
<p>
分布: 直径 [dMin, 2dMin) の数は Gault(1970)の平衡分布 N(&gt;D)=10^-1.1 D^-2(個/m²)。<xref href="VirtualGeometry.World.PlanetCraterSettings.EquilibriumLimitMeters" data-throw-if-not-resolved="false"></xref> より大きい段は生成分布。
古さ: 新しい約 5%(深さ/直径 0.15〜0.2、縁と内側の段差)、中くらい約 25%(0.06〜0.15)、古い約 70%(0.015〜0.06、縁のない、裾の広いなだらかな窪み)。
形: 楕円(長短比 1〜1.15、面積を保つ)とふちの緩い欠け(3 つ山、±5%)。
</p>

状態を持たないので、複数のスレッドから呼べる。

```csharp
public sealed class PlanetCraterField
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetCraterField](VirtualGeometry.World.PlanetCraterField.md)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetCraterField__ctor_System_Double_VirtualGeometry_World_PlanetCraterSettings__System_Collections_Generic_IReadOnlyList_VirtualGeometry_World_PlanetCraterKeepOut__"></a> PlanetCraterField\(double, in PlanetCraterSettings, IReadOnlyList<PlanetCraterKeepOut\>\)

```csharp
public PlanetCraterField(double radiusMeters, in PlanetCraterSettings settings, IReadOnlyList<PlanetCraterKeepOut> keepOuts = null)
```

#### 引数（Parameters）

`radiusMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

`settings` [PlanetCraterSettings](VirtualGeometry.World.PlanetCraterSettings.md)

`keepOuts` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[PlanetCraterKeepOut](VirtualGeometry.World.PlanetCraterKeepOut.md)\>

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetCraterField_GeometryFullCells"></a> GeometryFullCells

地形メッシュがクレーターを表すのに要る、直径あたりのメッシュ間隔の数(この間で凹みを入れていく)。

```csharp
public const double GeometryFullCells = 12
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetCraterField_GeometryMinCells"></a> GeometryMinCells

地形メッシュがクレーターを表すのに要る、直径あたりのメッシュ間隔の数(この間で凹みを入れていく)。

```csharp
public const double GeometryMinCells = 6
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetCraterField_MaximumKeepOuts"></a> MaximumKeepOuts

置かない範囲の最大数(shader の配列の大きさ)。

```csharp
public const int MaximumKeepOuts = 4
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetCraterField_MaximumLevels"></a> MaximumLevels

```csharp
public const int MaximumLevels = 16
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetCraterField_KeepOuts"></a> KeepOuts

```csharp
public IReadOnlyList<PlanetCraterKeepOut> KeepOuts { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[PlanetCraterKeepOut](VirtualGeometry.World.PlanetCraterKeepOut.md)\>

### <a id="VirtualGeometry_World_PlanetCraterField_MaximumAbsoluteHeightMeters"></a> MaximumAbsoluteHeightMeters

|高さ| の上界(m)。1 段で届くのは最大 8 個、1 個は |高さ| ≤ 0.3 × 直径(&lt; 0.6 dMin × 2)。

```csharp
public double MaximumAbsoluteHeightMeters { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetCraterField_RadiusMeters"></a> RadiusMeters

```csharp
public double RadiusMeters { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetCraterField_Settings"></a> Settings

```csharp
public PlanetCraterSettings Settings { get; }
```

#### 値（Property Value）

 [PlanetCraterSettings](VirtualGeometry.World.PlanetCraterSettings.md)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetCraterField_FieldHeight_System_Double_System_Double_System_Double_System_Double_"></a> FieldHeight\(double, double, double, double\)

単位方向の点の、地形メッシュ(間隔 spacing m)が持つ生成クレーターの高さ(m)。

```csharp
public double FieldHeight(double unitX, double unitY, double unitZ, double spacing)
```

#### 引数（Parameters）

`unitX` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitY` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitZ` [double](https://learn.microsoft.com/dotnet/api/system.double)

`spacing` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetCraterField_GeometryWeight_System_Double_System_Double_"></a> GeometryWeight\(double, double\)

地形メッシュ(間隔 spacing m)がクレーター(直径 diameter m)の凹みを持つ割合。

```csharp
public static double GeometryWeight(double diameter, double spacing)
```

#### 引数（Parameters）

`diameter` [double](https://learn.microsoft.com/dotnet/api/system.double)

`spacing` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetCraterField_Height_VirtualGeometry_World_PlanetCraterField_Crater__System_Double_"></a> Height\(in Crater, double\)

断面(中心からのゆがめた距離 d)の高さ(m、地表 0 基準)。影響半径は 2r。
新しいものは椀 rim+depth(x²−1)(内側の段差)と外側の噴出物 rim·x^-3 の滑らかな最小、崩れたものは縁のない裾の広い窪み。崩れ具合で連続的に混ぜる。

```csharp
public static double Height(in PlanetCraterField.Crater crater, double distance)
```

#### 引数（Parameters）

`crater` [PlanetCraterField](VirtualGeometry.World.PlanetCraterField.md).[Crater](VirtualGeometry.World.PlanetCraterField.Crater.md)

`distance` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetCraterField_LevelCell_System_Int32_"></a> LevelCell\(int\)

段 m の格子の 1 辺(m)= 4dMin。

```csharp
public double LevelCell(int level)
```

#### 引数（Parameters）

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetCraterField_LevelMinimumDiameter_System_Int32_"></a> LevelMinimumDiameter\(int\)

段 m の最小直径(m)。段 0 が最も大きい。

```csharp
public double LevelMinimumDiameter(int level)
```

#### 引数（Parameters）

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetCraterField_LevelSeed_System_UInt32_System_Int32_"></a> LevelSeed\(uint, int\)

段 m の hash の種(shader と同じ式: Mix(seed + 0x9e3779b9 × (m + 1)))。

```csharp
public static uint LevelSeed(uint seed, int level)
```

#### 引数（Parameters）

`seed` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualGeometry_World_PlanetCraterField_Shape_System_Double_System_Double_VirtualGeometry_World_PlanetCraterField_Crater__"></a> Shape\(double, double, ref Crater\)

古さ age(0〜1)から深さ・縁・段差・新しさ・崩れ具合を決める(shader の VGCraterShape と同じ)。

```csharp
public static void Shape(double age, double diameter, ref PlanetCraterField.Crater crater)
```

#### 引数（Parameters）

`age` [double](https://learn.microsoft.com/dotnet/api/system.double)

`diameter` [double](https://learn.microsoft.com/dotnet/api/system.double)

`crater` [PlanetCraterField](VirtualGeometry.World.PlanetCraterField.md).[Crater](VirtualGeometry.World.PlanetCraterField.Crater.md)

### <a id="VirtualGeometry_World_PlanetCraterField_TryCrater_System_Int64_System_Int64_System_Int64_System_Int32_VirtualGeometry_World_PlanetCraterField_Crater__"></a> TryCrater\(long, long, long, int, out Crater\)

段 m のマス(ix, iy, iz)にクレーターがあれば作る。q の基準球からの高さが窓の外、置かない範囲の中なら false。

```csharp
public bool TryCrater(long ix, long iy, long iz, int level, out PlanetCraterField.Crater crater)
```

#### 引数（Parameters）

`ix` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`iy` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`iz` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`crater` [PlanetCraterField](VirtualGeometry.World.PlanetCraterField.md).[Crater](VirtualGeometry.World.PlanetCraterField.Crater.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetCraterField_Unit_System_UInt32_"></a> Unit\(uint\)

```csharp
public static double Unit(uint h)
```

#### 引数（Parameters）

`h` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetCraterField_WarpedDistance_VirtualGeometry_World_PlanetCraterField_Crater__VirtualGeometry_World_PlanetDouble3_VirtualGeometry_World_PlanetDouble3_"></a> WarpedDistance\(in Crater, PlanetDouble3, PlanetDouble3\)

画素の点 p(基準球の点)から見た、クレーターの中心までのゆがめた距離(m)。n は p の単位方向。
面に沿った差(接平面へ射影)を、楕円(面積を保つ)とふちの 3 つ山の波で割る。

```csharp
public static double WarpedDistance(in PlanetCraterField.Crater crater, PlanetDouble3 offset, PlanetDouble3 n)
```

#### 引数（Parameters）

`crater` [PlanetCraterField](VirtualGeometry.World.PlanetCraterField.md).[Crater](VirtualGeometry.World.PlanetCraterField.Crater.md)

`offset` [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

`n` [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetCraterField_WarpedDistance_VirtualGeometry_World_PlanetCraterField_Crater__System_Double_System_Double_"></a> WarpedDistance\(in Crater, double, double\)

楕円の軸の座標(u, v)でのゆがめた距離。

```csharp
public static double WarpedDistance(in PlanetCraterField.Crater crater, double u, double v)
```

#### 引数（Parameters）

`crater` [PlanetCraterField](VirtualGeometry.World.PlanetCraterField.md).[Crater](VirtualGeometry.World.PlanetCraterField.Crater.md)

`u` [double](https://learn.microsoft.com/dotnet/api/system.double)

`v` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)
