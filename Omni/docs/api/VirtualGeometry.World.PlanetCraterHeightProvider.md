# <a id="VirtualGeometry_World_PlanetCraterHeightProvider"></a> Class PlanetCraterHeightProvider

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

高さの層: 内側の高さに、生成クレーター(<xref href="VirtualGeometry.World.PlanetCraterField" data-throw-if-not-resolved="false"></xref>)の凹みを足す。地形メッシュ・接地・岩はこれを使う。
凹みはメッシュ間隔で帯域制限する(直径がメッシュ間隔の 6〜12 倍の間で入れていく)。細かいクレーターは shader の陰影だけ(PlanetCraters.hlsl)。
陰影は二重にしない: 頂点法線の高さ(<xref href="VirtualGeometry.World.PlanetCraterHeightProvider.SampleShadingHeightMeters(System.Double%2cSystem.Double%2cSystem.Double%2cSystem.Double)" data-throw-if-not-resolved="false"></xref>)にはクレーターを入れない。
間隔 0(接地・岩)は最も細かいメッシュの間隔として扱い、接地と描かれる最も細かい地表を一致させる。

```csharp
public class PlanetCraterHeightProvider : IPlanetShadingHeightProvider, IPlanetHeightProvider
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetCraterHeightProvider](VirtualGeometry.World.PlanetCraterHeightProvider.md)

#### 実装するインターフェース（Implements）

[IPlanetShadingHeightProvider](VirtualGeometry.World.IPlanetShadingHeightProvider.md), 
[IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetCraterHeightProvider_Field"></a> Field

```csharp
public PlanetCraterField Field { get; }
```

#### 値（Property Value）

 [PlanetCraterField](VirtualGeometry.World.PlanetCraterField.md)

### <a id="VirtualGeometry_World_PlanetCraterHeightProvider_Inner"></a> Inner

```csharp
public IPlanetHeightProvider Inner { get; }
```

#### 値（Property Value）

 [IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

### <a id="VirtualGeometry_World_PlanetCraterHeightProvider_MaximumAbsoluteHeightMeters"></a> MaximumAbsoluteHeightMeters

高さの絶対値の上界(m)。Cell の選択の bounds に含める。

```csharp
public double MaximumAbsoluteHeightMeters { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetCraterHeightProvider_Create_VirtualGeometry_World_IPlanetHeightProvider_VirtualGeometry_World_PlanetCraterField_System_Double_System_Func_VirtualGeometry_World_PlanetDouble3_System_Double__"></a> Create\(IPlanetHeightProvider, PlanetCraterField, double, Func<PlanetDouble3, double\>\)

内側が複数のスレッドから呼べるなら、同じく呼べる供給元を作る(weight も複数のスレッドから呼べること)。
weight は単位方向ごとのクレーターの重み(0〜1、造成面などで 0)。null なら 1。shader では VGPlanetCraters の weight に同じ値を渡す。

```csharp
public static PlanetCraterHeightProvider Create(IPlanetHeightProvider inner, PlanetCraterField field, double minimumSpacingMeters, Func<PlanetDouble3, double> weight = null)
```

#### 引数（Parameters）

`inner` [IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

`field` [PlanetCraterField](VirtualGeometry.World.PlanetCraterField.md)

`minimumSpacingMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

`weight` [Func](https://learn.microsoft.com/dotnet/api/system.func\-2)<[PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md), [double](https://learn.microsoft.com/dotnet/api/system.double)\>

#### 戻り値（Returns）

 [PlanetCraterHeightProvider](VirtualGeometry.World.PlanetCraterHeightProvider.md)

### <a id="VirtualGeometry_World_PlanetCraterHeightProvider_SampleCraterHeightMeters_System_Double_System_Double_System_Double_System_Double_"></a> SampleCraterHeightMeters\(double, double, double, double\)

方向のクレーターの高さ(m)。間隔 0 は最も細かいメッシュの間隔として扱う。

```csharp
public double SampleCraterHeightMeters(double unitX, double unitY, double unitZ, double spacingMeters)
```

#### 引数（Parameters）

`unitX` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitY` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitZ` [double](https://learn.microsoft.com/dotnet/api/system.double)

`spacingMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetCraterHeightProvider_SampleHeightMeters_System_Double_System_Double_System_Double_System_Double_"></a> SampleHeightMeters\(double, double, double, double\)

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

### <a id="VirtualGeometry_World_PlanetCraterHeightProvider_SampleShadingHeightMeters_System_Double_System_Double_System_Double_System_Double_"></a> SampleShadingHeightMeters\(double, double, double, double\)

頂点法線に使う、クレーターを含まない高さ。

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
