# <a id="VirtualGeometry_World_IPlanetHeightProvider"></a> Interface IPlanetHeightProvider

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

惑星の地表の高さ(半径 R の球面からの高さ、m)の正本を CPU で返す。<xref href="VirtualGeometry.World.PlanetHeightTerrainSource" data-throw-if-not-resolved="false"></xref> は Cell の頂点をこの値で作り、
描く頂点と接地の問い合わせ(<xref href="VirtualGeometry.World.PlanetTerrainContact" data-throw-if-not-resolved="false"></xref>)が同じ値を使う(GPU に別の式を持たない)。
方向は惑星のローカル座標の単位ベクトル。spacingMeters はメッシュの間隔(この間隔で表せない短い波長を落とす帯域制限。0 は全帯域)。
同じ引数には常に同じ値を返すこと(Cell を作り直しても形が変わらない前提)。呼び出しは main thread から。

```csharp
public interface IPlanetHeightProvider
```

## プロパティ（Properties）

### <a id="VirtualGeometry_World_IPlanetHeightProvider_MaximumAbsoluteHeightMeters"></a> MaximumAbsoluteHeightMeters

高さの絶対値の上界(m)。Cell の選択の bounds に含める。

```csharp
double MaximumAbsoluteHeightMeters { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

## メソッド（Methods）

### <a id="VirtualGeometry_World_IPlanetHeightProvider_SampleHeightMeters_System_Double_System_Double_System_Double_System_Double_"></a> SampleHeightMeters\(double, double, double, double\)

```csharp
double SampleHeightMeters(double unitX, double unitY, double unitZ, double spacingMeters)
```

#### 引数（Parameters）

`unitX` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitY` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitZ` [double](https://learn.microsoft.com/dotnet/api/system.double)

`spacingMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)
