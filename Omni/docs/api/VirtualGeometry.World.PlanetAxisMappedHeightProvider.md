# <a id="VirtualGeometry_World_PlanetAxisMappedHeightProvider"></a> Class PlanetAxisMappedHeightProvider

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

天体のローカル座標の向きの決め方が、高さの供給元(inner)の決め方と違うときに、方向を回してから inner へ聞く。
inner の方向 = (dot(d, xRow), dot(d, yRow), dot(d, zRow))。行は互いに直交する単位ベクトル(回転)であること。
例: 北極 +Z・経度 0 が +Y・東経 90 度が +X の天体座標から、<xref href="VirtualGeometry.World.PlanetEquirectangularHeightProvider" data-throw-if-not-resolved="false"></xref>(北極 +Y・経度 0 が +X・東経 90 度が +Z)へ聞くには
<xref href="VirtualGeometry.World.PlanetAxisMappedHeightProvider.ZNorthYPrimeMeridianToEquirectangular(VirtualGeometry.World.IPlanetHeightProvider)" data-throw-if-not-resolved="false"></xref>。

```csharp
public sealed class PlanetAxisMappedHeightProvider : IPlanetShadingHeightProvider, IThreadSafePlanetHeightProvider, IPlanetHeightProvider
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetAxisMappedHeightProvider](VirtualGeometry.World.PlanetAxisMappedHeightProvider.md)

#### 実装するインターフェース（Implements）

[IPlanetShadingHeightProvider](VirtualGeometry.World.IPlanetShadingHeightProvider.md), 
[IThreadSafePlanetHeightProvider](VirtualGeometry.World.IThreadSafePlanetHeightProvider.md), 
[IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetAxisMappedHeightProvider__ctor_VirtualGeometry_World_IPlanetHeightProvider_VirtualGeometry_World_PlanetDouble3_VirtualGeometry_World_PlanetDouble3_VirtualGeometry_World_PlanetDouble3_"></a> PlanetAxisMappedHeightProvider\(IPlanetHeightProvider, PlanetDouble3, PlanetDouble3, PlanetDouble3\)

```csharp
public PlanetAxisMappedHeightProvider(IPlanetHeightProvider inner, PlanetDouble3 xRow, PlanetDouble3 yRow, PlanetDouble3 zRow)
```

#### 引数（Parameters）

`inner` [IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

`xRow` [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

`yRow` [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

`zRow` [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetAxisMappedHeightProvider_Inner"></a> Inner

```csharp
public IPlanetHeightProvider Inner { get; }
```

#### 値（Property Value）

 [IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

### <a id="VirtualGeometry_World_PlanetAxisMappedHeightProvider_MaximumAbsoluteHeightMeters"></a> MaximumAbsoluteHeightMeters

高さの絶対値の上界(m)。Cell の選択の bounds に含める。

```csharp
public double MaximumAbsoluteHeightMeters { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetAxisMappedHeightProvider_Map_System_Double_System_Double_System_Double_System_Double__System_Double__System_Double__"></a> Map\(double, double, double, out double, out double, out double\)

天体座標の方向を inner の座標へ回す。

```csharp
public void Map(double x, double y, double z, out double innerX, out double innerY, out double innerZ)
```

#### 引数（Parameters）

`x` [double](https://learn.microsoft.com/dotnet/api/system.double)

`y` [double](https://learn.microsoft.com/dotnet/api/system.double)

`z` [double](https://learn.microsoft.com/dotnet/api/system.double)

`innerX` [double](https://learn.microsoft.com/dotnet/api/system.double)

`innerY` [double](https://learn.microsoft.com/dotnet/api/system.double)

`innerZ` [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetAxisMappedHeightProvider_SampleHeightMeters_System_Double_System_Double_System_Double_System_Double_"></a> SampleHeightMeters\(double, double, double, double\)

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

### <a id="VirtualGeometry_World_PlanetAxisMappedHeightProvider_SampleShadingHeightMeters_System_Double_System_Double_System_Double_System_Double_"></a> SampleShadingHeightMeters\(double, double, double, double\)

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

### <a id="VirtualGeometry_World_PlanetAxisMappedHeightProvider_ZNorthYPrimeMeridianToEquirectangular_VirtualGeometry_World_IPlanetHeightProvider_"></a> ZNorthYPrimeMeridianToEquirectangular\(IPlanetHeightProvider\)

北極 +Z・経度 0 が +Y・東経 90 度が +X の天体座標(EarthToMoon の地球、旧 PlanetSurface の規約)から、
正距円筒の供給元の規約(北極 +Y・経度 0 が +X・東経 90 度が +Z)への回転。inner = (y, z, x)。

```csharp
public static PlanetAxisMappedHeightProvider ZNorthYPrimeMeridianToEquirectangular(IPlanetHeightProvider inner)
```

#### 引数（Parameters）

`inner` [IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

#### 戻り値（Returns）

 [PlanetAxisMappedHeightProvider](VirtualGeometry.World.PlanetAxisMappedHeightProvider.md)
