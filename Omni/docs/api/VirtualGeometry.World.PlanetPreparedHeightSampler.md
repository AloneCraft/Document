# <a id="VirtualGeometry_World_PlanetPreparedHeightSampler"></a> Class PlanetPreparedHeightSampler

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

1 Cell で不変の帯域を一度だけ選び、形と陰影で同じ基底・noise を再評価しない。演算順と採用 octave は元の供給元と同じ。

```csharp
public sealed class PlanetPreparedHeightSampler
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetPreparedHeightSampler](VirtualGeometry.World.PlanetPreparedHeightSampler.md)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetPreparedHeightSampler_SupportsNative"></a> SupportsNative

```csharp
public bool SupportsNative { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetPreparedHeightSampler_Sample_System_Double_System_Double_System_Double_System_Boolean_System_Double__System_Double__"></a> Sample\(double, double, double, bool, out double, out double\)

```csharp
public void Sample(double x, double y, double z, bool hasShading, out double height, out double shading)
```

#### 引数（Parameters）

`x` [double](https://learn.microsoft.com/dotnet/api/system.double)

`y` [double](https://learn.microsoft.com/dotnet/api/system.double)

`z` [double](https://learn.microsoft.com/dotnet/api/system.double)

`hasShading` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`height` [double](https://learn.microsoft.com/dotnet/api/system.double)

`shading` [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetPreparedHeightSampler_SampleBasisBatch_System_Double___System_Double___System_Double___System_Int32_System_Boolean_System_Double___System_Double___System_Threading_CancellationToken_"></a> SampleBasisBatch\(double\[\], double\[\], double\[\], int, bool, double\[\], double\[\], CancellationToken\)

```csharp
public void SampleBasisBatch(double[] x, double[] y, double[] z, int count, bool hasShading, double[] height, double[] shading, CancellationToken cancellation = default)
```

#### 引数（Parameters）

`x` [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]

`y` [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]

`z` [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]

`count` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`hasShading` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`height` [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]

`shading` [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]

`cancellation` [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)

### <a id="VirtualGeometry_World_PlanetPreparedHeightSampler_SampleBatch_System_Double___System_Double___System_Double___System_Int32_System_Boolean_System_Double___System_Double___System_Threading_CancellationToken_"></a> SampleBatch\(double\[\], double\[\], double\[\], int, bool, double\[\], double\[\], CancellationToken\)

```csharp
public void SampleBatch(double[] x, double[] y, double[] z, int count, bool hasShading, double[] height, double[] shading, CancellationToken cancellation = default)
```

#### 引数（Parameters）

`x` [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]

`y` [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]

`z` [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]

`count` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`hasShading` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`height` [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]

`shading` [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]

`cancellation` [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)

### <a id="VirtualGeometry_World_PlanetPreparedHeightSampler_Snapshot_System_Double___System_Double___"></a> Snapshot\(double\[\], double\[\]\)

```csharp
public PlanetNativeHeightInputs Snapshot(double[] height, double[] shading)
```

#### 引数（Parameters）

`height` [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]

`shading` [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]

#### 戻り値（Returns）

 [PlanetNativeHeightInputs](VirtualGeometry.World.PlanetNativeHeightInputs.md)

### <a id="VirtualGeometry_World_PlanetPreparedHeightSampler_TryCreate_VirtualGeometry_World_IPlanetHeightProvider_System_Double_"></a> TryCreate\(IPlanetHeightProvider, double\)

既知の不変な増幅層だけを展開する。他の供給元には既存の呼出し規約を維持する。

```csharp
public static PlanetPreparedHeightSampler TryCreate(IPlanetHeightProvider source, double spacing)
```

#### 引数（Parameters）

`source` [IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

`spacing` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [PlanetPreparedHeightSampler](VirtualGeometry.World.PlanetPreparedHeightSampler.md)
