# <a id="Omni_Celestial_CelestialPhysicalConstants"></a> Struct CelestialPhysicalConstants

Namespace: [Omni.Celestial](Omni.Celestial.md)  
Assembly: Omni.Celestial.Core.dll  

1天体の不変な物理定数です。幾何量は<xref href="Omni.Logical.Scalar" data-throw-if-not-resolved="false"></xref>、
質量は桁域の異なる<xref href="Omni.Units.Mass" data-throw-if-not-resolved="false"></xref>で保持します。

```csharp
public readonly struct CelestialPhysicalConstants
```

## コンストラクター（Constructors）

### <a id="Omni_Celestial_CelestialPhysicalConstants__ctor_Omni_Logical_Scalar_Omni_Units_Mass_Omni_Logical_Scalar_"></a> CelestialPhysicalConstants\(Scalar, Mass, Scalar\)

物理定数を構築します。

```csharp
public CelestialPhysicalConstants(Scalar diameterMeters, Mass mass, Scalar axialTiltDegrees)
```

#### 引数（Parameters）

`diameterMeters` Scalar

赤道直径（メートル）。

`mass` Mass

質量。

`axialTiltDegrees` Scalar

自転軸傾斜角（度）。

## フィールド（Fields）

### <a id="Omni_Celestial_CelestialPhysicalConstants_AxialTiltDegrees"></a> AxialTiltDegrees

自転軸傾斜角（度）です。

```csharp
public readonly Scalar AxialTiltDegrees
```

#### 値（Field Value）

 Scalar

### <a id="Omni_Celestial_CelestialPhysicalConstants_DiameterMeters"></a> DiameterMeters

赤道直径（メートル）です。

```csharp
public readonly Scalar DiameterMeters
```

#### 値（Field Value）

 Scalar

### <a id="Omni_Celestial_CelestialPhysicalConstants_Mass"></a> Mass

質量です。正規単位はキログラムです。

```csharp
public readonly Mass Mass
```

#### 値（Field Value）

 Mass

## メソッド（Methods）

### <a id="Omni_Celestial_CelestialPhysicalConstants_TryGetRadiusMeters_Omni_Logical_Scalar__"></a> TryGetRadiusMeters\(out Scalar\)

赤道半径（メートル）を返します。

```csharp
public bool TryGetRadiusMeters(out Scalar radiusMeters)
```

#### 引数（Parameters）

`radiusMeters` Scalar

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

直径を2で割れない精度構成ではfalse。
