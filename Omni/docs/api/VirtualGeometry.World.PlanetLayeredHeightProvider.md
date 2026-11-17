# <a id="VirtualGeometry_World_PlanetLayeredHeightProvider"></a> Class PlanetLayeredHeightProvider

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

基の高さ(natural)の上に、書き換えの層を順に重ねる。層の式は前から順に合成する(後の層が前の層の結果を書き換える)。
陰影用の高さ(<xref href="VirtualGeometry.World.IPlanetShadingHeightProvider" data-throw-if-not-resolved="false"></xref>)は、基の陰影用の高さへ同じ式を掛ける。
基は複数のスレッドから同時に呼べること(層も状態を持たないこと)。

```csharp
public sealed class PlanetLayeredHeightProvider : IPlanetShadingHeightProvider, IThreadSafePlanetHeightProvider, IPlanetHeightProvider
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetLayeredHeightProvider](VirtualGeometry.World.PlanetLayeredHeightProvider.md)

#### 実装するインターフェース（Implements）

[IPlanetShadingHeightProvider](VirtualGeometry.World.IPlanetShadingHeightProvider.md), 
[IThreadSafePlanetHeightProvider](VirtualGeometry.World.IThreadSafePlanetHeightProvider.md), 
[IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetLayeredHeightProvider__ctor_VirtualGeometry_World_IPlanetHeightProvider_VirtualGeometry_World_IPlanetHeightOverride___"></a> PlanetLayeredHeightProvider\(IPlanetHeightProvider, params IPlanetHeightOverride\[\]\)

```csharp
public PlanetLayeredHeightProvider(IPlanetHeightProvider natural, params IPlanetHeightOverride[] layers)
```

#### 引数（Parameters）

`natural` [IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

`layers` [IPlanetHeightOverride](VirtualGeometry.World.IPlanetHeightOverride.md)\[\]

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetLayeredHeightProvider_LayerCount"></a> LayerCount

```csharp
public int LayerCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetLayeredHeightProvider_LayerHash"></a> LayerHash

基と層の組の識別子(キャッシュ用)。

```csharp
public string LayerHash { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualGeometry_World_PlanetLayeredHeightProvider_MaximumAbsoluteHeightMeters"></a> MaximumAbsoluteHeightMeters

高さの絶対値の上界(m)。Cell の選択の bounds に含める。

```csharp
public double MaximumAbsoluteHeightMeters { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetLayeredHeightProvider_Natural"></a> Natural

```csharp
public IPlanetHeightProvider Natural { get; }
```

#### 値（Property Value）

 [IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetLayeredHeightProvider_Layer_System_Int32_"></a> Layer\(int\)

```csharp
public IPlanetHeightOverride Layer(int index)
```

#### 引数（Parameters）

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [IPlanetHeightOverride](VirtualGeometry.World.IPlanetHeightOverride.md)

### <a id="VirtualGeometry_World_PlanetLayeredHeightProvider_SampleHeightBlend_System_Double_System_Double_System_Double_"></a> SampleHeightBlend\(double, double, double\)

全ての層を合成した式。

```csharp
public PlanetHeightBlend SampleHeightBlend(double unitX, double unitY, double unitZ)
```

#### 引数（Parameters）

`unitX` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitY` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitZ` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [PlanetHeightBlend](VirtualGeometry.World.PlanetHeightBlend.md)

### <a id="VirtualGeometry_World_PlanetLayeredHeightProvider_SampleHeightMeters_System_Double_System_Double_System_Double_System_Double_"></a> SampleHeightMeters\(double, double, double, double\)

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

### <a id="VirtualGeometry_World_PlanetLayeredHeightProvider_SampleShadingHeightMeters_System_Double_System_Double_System_Double_System_Double_"></a> SampleShadingHeightMeters\(double, double, double, double\)

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
