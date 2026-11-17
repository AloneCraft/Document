# <a id="VirtualGeometry_World_PlanetNoiseLattice"></a> Class PlanetNoiseLattice

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

GPU 版の <xref href="VirtualGeometry.World.PlanetGradientNoise" data-throw-if-not-resolved="false"></xref>(Shaders/PlanetGradientNoise.hlsl)へ渡す Cell ごとの値を作る。
メッシュは波長が quad の 4 倍より短い octave を落とす(<xref href="VirtualGeometry.World.PlanetAmplifiedHeightProvider.BandWeight(System.Double%2cSystem.Double)" data-throw-if-not-resolved="false"></xref>)ので、shader がその分を画素ごとに同じ関数で足す。
惑星の座標 ÷ 波長は 10^9 周期に達し float では位相が潰れるため、Cell の球面上の原点(R·中心の方向)の格子番号と端数を、
shader が足す最初の octave(波長が quad の <xref href="VirtualGeometry.World.PlanetNoiseLattice.CoarsestQuads" data-throw-if-not-resolved="false"></xref> 倍より短いもの)について double で求める。細かい octave は shader が 2 倍を正確に繰り返して作る。
値の並びは hlsl の冒頭の契約と同じ(1 層 4 つの Vector4)。格子番号は 48 ビットの 2 の補数を 24 ビットずつ float で渡す(float で正確に表せる)。

```csharp
public static class PlanetNoiseLattice
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetNoiseLattice](VirtualGeometry.World.PlanetNoiseLattice.md)

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetNoiseLattice_CoarsestQuads"></a> CoarsestQuads

shader が足す最初の octave の波長の上限(quad の何倍より短いか)。これより長い octave はメッシュが表し、頂点の法線が弱める勾配も 3% 未満。

```csharp
public const double CoarsestQuads = 8
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetNoiseLattice_MaximumLattice"></a> MaximumLattice

格子番号の絶対値の上限(48 ビットの 2 の補数で表せる範囲)。超えたら層を無効にする(Fail Closed)。

```csharp
public const double MaximumLattice = 140737488355328
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetNoiseLattice_Decode_System_Single_System_Single_"></a> Decode\(float, float\)

48 ビットの 2 の補数の 24 ビットずつ(下位、上位)から整数へ(検証用。shader の PlanetNoiseDecode と同じ規則)。

```csharp
public static long Decode(float low, float high)
```

#### 引数（Parameters）

`low` [float](https://learn.microsoft.com/dotnet/api/system.single)

`high` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualGeometry_World_PlanetNoiseLattice_TryEncodeLayer_VirtualGeometry_World_PlanetAmplifiedHeightProvider_System_Double_System_Double_System_Double_System_Double_UnityEngine_Vector4__UnityEngine_Vector4__UnityEngine_Vector4__UnityEngine_Vector4__"></a> TryEncodeLayer\(PlanetAmplifiedHeightProvider, double, double, double, double, out Vector4, out Vector4, out Vector4, out Vector4\)

1 層の値。unit は Cell の中心の単位方向(球面上の原点の方向)、quadMeters はこの Cell の quad の弧長。
shader が足す octave が無い、または格子番号が範囲外なら false(値は全部 0 = shader では無効)。

```csharp
public static bool TryEncodeLayer(PlanetAmplifiedHeightProvider layer, double unitX, double unitY, double unitZ, double quadMeters, out Vector4 a, out Vector4 b, out Vector4 c, out Vector4 d)
```

#### 引数（Parameters）

`layer` [PlanetAmplifiedHeightProvider](VirtualGeometry.World.PlanetAmplifiedHeightProvider.md)

`unitX` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitY` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitZ` [double](https://learn.microsoft.com/dotnet/api/system.double)

`quadMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

`a` Vector4

`b` Vector4

`c` Vector4

`d` Vector4

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
