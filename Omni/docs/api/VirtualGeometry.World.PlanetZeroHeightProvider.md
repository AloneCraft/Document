# <a id="VirtualGeometry_World_PlanetZeroHeightProvider"></a> Class PlanetZeroHeightProvider

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

どこも高さ 0 の球。

```csharp
public sealed class PlanetZeroHeightProvider : IThreadSafePlanetHeightProvider, IPlanetHeightProvider, IPlanetHeightBoundsSource
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetZeroHeightProvider](VirtualGeometry.World.PlanetZeroHeightProvider.md)

#### 実装するインターフェース（Implements）

[IThreadSafePlanetHeightProvider](VirtualGeometry.World.IThreadSafePlanetHeightProvider.md), 
[IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md), 
[IPlanetHeightBoundsSource](VirtualGeometry.World.IPlanetHeightBoundsSource.md)

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetZeroHeightProvider_Instance"></a> Instance

```csharp
public static readonly PlanetZeroHeightProvider Instance
```

#### 値（Field Value）

 [PlanetZeroHeightProvider](VirtualGeometry.World.PlanetZeroHeightProvider.md)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetZeroHeightProvider_MaximumAbsoluteHeightMeters"></a> MaximumAbsoluteHeightMeters

高さの絶対値の上界(m)。Cell の選択の bounds に含める。

```csharp
public double MaximumAbsoluteHeightMeters { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetZeroHeightProvider_SampleHeightMeters_System_Double_System_Double_System_Double_System_Double_"></a> SampleHeightMeters\(double, double, double, double\)

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

### <a id="VirtualGeometry_World_PlanetZeroHeightProvider_TryGetHeightRange_VirtualGeometry_World_PlanetCellFrame__System_Double_System_Double__System_Double__"></a> TryGetHeightRange\(in PlanetCellFrame, double, out double, out double\)

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
