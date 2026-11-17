# <a id="VirtualGeometry_World_PlanetNoiseShadingSource"></a> Class PlanetNoiseShadingSource

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

形は元の高さを保ち、手続きの細部の陰影を画素側へ分離する。Cell の階層では陰影の帯域を変えない。

```csharp
public class PlanetNoiseShadingSource : IPlanetShadingHeightProvider, IPlanetHeightProvider, IPlanetAnchorPropertySource, IPlanetCellPropertySource, IPlanetHeightBoundsSource
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetNoiseShadingSource](VirtualGeometry.World.PlanetNoiseShadingSource.md)

#### 実装するインターフェース（Implements）

[IPlanetShadingHeightProvider](VirtualGeometry.World.IPlanetShadingHeightProvider.md), 
[IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md), 
[IPlanetAnchorPropertySource](VirtualGeometry.World.IPlanetAnchorPropertySource.md), 
[IPlanetCellPropertySource](VirtualGeometry.World.IPlanetCellPropertySource.md), 
[IPlanetHeightBoundsSource](VirtualGeometry.World.IPlanetHeightBoundsSource.md)

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetNoiseShadingSource_MaximumOctaves"></a> MaximumOctaves

```csharp
public const int MaximumOctaves = 64
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetNoiseShadingSource_Geometry"></a> Geometry

```csharp
public IPlanetHeightProvider Geometry { get; }
```

#### 値（Property Value）

 [IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

### <a id="VirtualGeometry_World_PlanetNoiseShadingSource_MaximumAbsoluteHeightMeters"></a> MaximumAbsoluteHeightMeters

高さの絶対値の上界(m)。Cell の選択の bounds に含める。

```csharp
public double MaximumAbsoluteHeightMeters { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetNoiseShadingSource_Create_VirtualGeometry_World_IPlanetHeightProvider_System_Int32_"></a> Create\(IPlanetHeightProvider, int\)

```csharp
public static PlanetNoiseShadingSource Create(IPlanetHeightProvider geometry, int capacity)
```

#### 引数（Parameters）

`geometry` [IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

`capacity` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [PlanetNoiseShadingSource](VirtualGeometry.World.PlanetNoiseShadingSource.md)

### <a id="VirtualGeometry_World_PlanetNoiseShadingSource_SampleHeightMeters_System_Double_System_Double_System_Double_System_Double_"></a> SampleHeightMeters\(double, double, double, double\)

```csharp
public double SampleHeightMeters(double x, double y, double z, double spacing)
```

#### 引数（Parameters）

`x` [double](https://learn.microsoft.com/dotnet/api/system.double)

`y` [double](https://learn.microsoft.com/dotnet/api/system.double)

`z` [double](https://learn.microsoft.com/dotnet/api/system.double)

`spacing` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetNoiseShadingSource_SampleShadingHeightMeters_System_Double_System_Double_System_Double_System_Double_"></a> SampleShadingHeightMeters\(double, double, double, double\)

```csharp
public double SampleShadingHeightMeters(double x, double y, double z, double spacing)
```

#### 引数（Parameters）

`x` [double](https://learn.microsoft.com/dotnet/api/system.double)

`y` [double](https://learn.microsoft.com/dotnet/api/system.double)

`z` [double](https://learn.microsoft.com/dotnet/api/system.double)

`spacing` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetNoiseShadingSource_TryGetHeightRange_VirtualGeometry_World_PlanetCellFrame__System_Double_System_Double__System_Double__"></a> TryGetHeightRange\(in PlanetCellFrame, double, out double, out double\)

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

### <a id="VirtualGeometry_World_PlanetNoiseShadingSource_WriteProperties_VirtualGeometry_World_PlanetCellKey__System_Single_UnityEngine_MaterialPropertyBlock_"></a> WriteProperties\(in PlanetCellKey, float, MaterialPropertyBlock\)

key の Cell の draw の値を block に書く。priority は大きいほど先に取りたい(まだ届いていない値を要求するときの優先度)。
値が無い間も、shader が見分けられる値(例: 番号 −1)を必ず書くこと(MaterialPropertyBlock は前の Cell の値を残さないが、書かないと shader の既定値になる)。

```csharp
public void WriteProperties(in PlanetCellKey key, float priority, MaterialPropertyBlock block)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

`priority` [float](https://learn.microsoft.com/dotnet/api/system.single)

`block` MaterialPropertyBlock
