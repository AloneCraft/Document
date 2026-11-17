# <a id="VirtualGeometry_World_PlanetNoiseColorSource"></a> Class PlanetNoiseColorSource

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

地表の色のゆらぎ(色画像の 1 画素より細かい帯域の零平均の変動)の、Cell ごとの格子原点を書く(shader は Shaders/PlanetSurfaceColor.hlsl の VGApplyColorNoise)。
内側の値(色タイルなど)を先に書いてから、_VGColorNoiseInfo と _VGColorNoiseA〜D を書く。各 octave は独立した格子原点を 48bit で符号化する
(粗い格子の float の端数を何百万倍にも拡大しない)。SolarSystem・EarthToMoon が同じ部品を使う。

```csharp
public sealed class PlanetNoiseColorSource : IPlanetCellPropertySource
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetNoiseColorSource](VirtualGeometry.World.PlanetNoiseColorSource.md)

#### 実装するインターフェース（Implements）

[IPlanetCellPropertySource](VirtualGeometry.World.IPlanetCellPropertySource.md)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetNoiseColorSource__ctor_VirtualGeometry_World_IPlanetCellPropertySource_System_Double_System_Double_System_Single_System_UInt32_System_Int32_"></a> PlanetNoiseColorSource\(IPlanetCellPropertySource, double, double, float, uint, int\)

```csharp
public PlanetNoiseColorSource(IPlanetCellPropertySource inner, double radiusMeters, double sourceMeters, float strength, uint seed, int capacity)
```

#### 引数（Parameters）

`inner` [IPlanetCellPropertySource](VirtualGeometry.World.IPlanetCellPropertySource.md)

先に書く値(色タイルなど)。無ければ null。

`radiusMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

球の半径(m)。

`sourceMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

色画像の 1 画素(m)。ゆらぎはこれより細かい帯域だけに足す(最も長い波長はこの 2 倍)。

`strength` [float](https://learn.microsoft.com/dotnet/api/system.single)

ゆらぎの強さ(色に掛ける 1 ± strength)。

`seed` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

シード。同じ天体はどのデモでも同じ値にする。

`capacity` [int](https://learn.microsoft.com/dotnet/api/system.int32)

格子原点を覚えておく Cell の数。

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetNoiseColorSource_Hurst"></a> Hurst

octave ごとの振幅の比の指数(Hurst)。

```csharp
public const double Hurst = 0.8
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetNoiseColorSource_MaximumOctaves"></a> MaximumOctaves

```csharp
public const int MaximumOctaves = 32
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetNoiseColorSource_MinimumWavelengthMeters"></a> MinimumWavelengthMeters

色のゆらぎの最短の波長(m)。これより細かい色の変動は作らない。

```csharp
public const double MinimumWavelengthMeters = 0.0026
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetNoiseColorSource_TryGetLayers_VirtualGeometry_World_PlanetCellKey__UnityEngine_Vector4______"></a> TryGetLayers\(in PlanetCellKey, out Vector4\[\]\[\]\)

key の Cell の格子原点(A〜D の 4 つの配列)。Cell の原点を作れなければ false。

```csharp
public bool TryGetLayers(in PlanetCellKey key, out Vector4[][] values)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

`values` Vector4\[\]\[\]

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetNoiseColorSource_WriteProperties_VirtualGeometry_World_PlanetCellKey__System_Single_UnityEngine_MaterialPropertyBlock_"></a> WriteProperties\(in PlanetCellKey, float, MaterialPropertyBlock\)

key の Cell の draw の値を block に書く。priority は大きいほど先に取りたい(まだ届いていない値を要求するときの優先度)。
値が無い間も、shader が見分けられる値(例: 番号 −1)を必ず書くこと(MaterialPropertyBlock は前の Cell の値を残さないが、書かないと shader の既定値になる)。

```csharp
public void WriteProperties(in PlanetCellKey key, float priority, MaterialPropertyBlock block)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

`priority` [float](https://learn.microsoft.com/dotnet/api/system.single)

`block` MaterialPropertyBlock
