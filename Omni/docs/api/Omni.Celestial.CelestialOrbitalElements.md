# <a id="Omni_Celestial_CelestialOrbitalElements"></a> Struct CelestialOrbitalElements

Namespace: [Omni.Celestial](Omni.Celestial.md)  
Assembly: Omni.Celestial.Core.dll  

天体の不変な軌道要素です。中心天体を持たない場合は<xref href="Omni.Celestial.CelestialOrbitalElements.IsDefined" data-throw-if-not-resolved="false"></xref>がfalseです。

```csharp
public readonly struct CelestialOrbitalElements
```

## コンストラクター（Constructors）

### <a id="Omni_Celestial_CelestialOrbitalElements__ctor_System_Boolean_System_String_Omni_Logical_Scalar_Omni_Logical_Scalar_Omni_Logical_Scalar_Omni_Logical_Scalar_"></a> CelestialOrbitalElements\(bool, string, Scalar, Scalar, Scalar, Scalar\)

軌道要素を構築します。

```csharp
public CelestialOrbitalElements(bool isDefined, string centralBodyKey, Scalar semiMajorAxisMeters, Scalar orbitalPeriodSeconds, Scalar eccentricity, Scalar inclinationDegrees)
```

#### 引数（Parameters）

`isDefined` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

軌道要素を持つ場合はtrue。

`centralBodyKey` [string](https://learn.microsoft.com/dotnet/api/system.string)

中心天体キー。

`semiMajorAxisMeters` Scalar

軌道長半径（メートル）。

`orbitalPeriodSeconds` Scalar

軌道周期（秒）。

`eccentricity` Scalar

離心率。

`inclinationDegrees` Scalar

軌道傾斜角（度）。

## フィールド（Fields）

### <a id="Omni_Celestial_CelestialOrbitalElements_CentralBodyKey"></a> CentralBodyKey

中心天体キーです。軌道を持たない場合は空文字です。

```csharp
public readonly string CentralBodyKey
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Celestial_CelestialOrbitalElements_Eccentricity"></a> Eccentricity

軌道離心率です。

```csharp
public readonly Scalar Eccentricity
```

#### 値（Field Value）

 Scalar

### <a id="Omni_Celestial_CelestialOrbitalElements_InclinationDegrees"></a> InclinationDegrees

軌道傾斜角（度）です。

```csharp
public readonly Scalar InclinationDegrees
```

#### 値（Field Value）

 Scalar

### <a id="Omni_Celestial_CelestialOrbitalElements_IsDefined"></a> IsDefined

軌道要素を持つ場合はtrueです。

```csharp
public readonly bool IsDefined
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Celestial_CelestialOrbitalElements_OrbitalPeriodSeconds"></a> OrbitalPeriodSeconds

軌道周期（秒）です。

```csharp
public readonly Scalar OrbitalPeriodSeconds
```

#### 値（Field Value）

 Scalar

### <a id="Omni_Celestial_CelestialOrbitalElements_SemiMajorAxisMeters"></a> SemiMajorAxisMeters

軌道長半径（メートル）です。

```csharp
public readonly Scalar SemiMajorAxisMeters
```

#### 値（Field Value）

 Scalar

## プロパティ（Properties）

### <a id="Omni_Celestial_CelestialOrbitalElements_None"></a> None

中心天体を持たない空の軌道要素です。

```csharp
public static CelestialOrbitalElements None { get; }
```

#### 値（Property Value）

 [CelestialOrbitalElements](Omni.Celestial.CelestialOrbitalElements.md)
