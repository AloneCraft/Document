# <a id="VirtualGeometry_World_PlanetHeightBlend"></a> Struct PlanetHeightBlend

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

基の高さへ掛ける重ね書きの式(基の重み・足す高さ・岩を置く重み)。高さ = <xref href="VirtualGeometry.World.PlanetHeightBlend.NaturalWeight" data-throw-if-not-resolved="false"></xref> × 基の高さ + <xref href="VirtualGeometry.World.PlanetHeightBlend.OffsetHeightMeters" data-throw-if-not-resolved="false"></xref>。

```csharp
public readonly struct PlanetHeightBlend
```

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetHeightBlend__ctor_System_Double_System_Double_System_Double_"></a> PlanetHeightBlend\(double, double, double\)

```csharp
public PlanetHeightBlend(double naturalWeight, double offsetHeightMeters, double scatterWeight = 1)
```

#### 引数（Parameters）

`naturalWeight` [double](https://learn.microsoft.com/dotnet/api/system.double)

`offsetHeightMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

`scatterWeight` [double](https://learn.microsoft.com/dotnet/api/system.double)

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetHeightBlend_NaturalWeight"></a> NaturalWeight

```csharp
public readonly double NaturalWeight
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetHeightBlend_OffsetHeightMeters"></a> OffsetHeightMeters

```csharp
public readonly double OffsetHeightMeters
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetHeightBlend_ScatterWeight"></a> ScatterWeight

```csharp
public readonly double ScatterWeight
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetHeightBlend_Identity"></a> Identity

```csharp
public static PlanetHeightBlend Identity { get; }
```

#### 値（Property Value）

 [PlanetHeightBlend](VirtualGeometry.World.PlanetHeightBlend.md)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetHeightBlend_Apply_System_Double_"></a> Apply\(double\)

```csharp
public double Apply(double naturalHeight)
```

#### 引数（Parameters）

`naturalHeight` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)
