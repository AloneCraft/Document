# <a id="Omni_Celestial_CelestialBodyAuthoring"></a> Class CelestialBodyAuthoring

Namespace: [Omni.Celestial](Omni.Celestial.md)  
Assembly: Omni.Celestial.Core.dll  

<xref href="Omni.Celestial.CelestialCatalogAsset" data-throw-if-not-resolved="false"></xref>に直列化する1天体分のAuthoring値です。
数値はfloatではなく10進文字列で保持し、Snapshot化時に幾何量は
<xref href="Omni.Logical.Scalar" data-throw-if-not-resolved="false"></xref>、質量は<xref href="Omni.Units.Mass" data-throw-if-not-resolved="false"></xref>へ検証付きで
変換します。これによりInspectorの表示精度やカルチャ差で物理定数を失いません。

```csharp
[Serializable]
public sealed class CelestialBodyAuthoring
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[CelestialBodyAuthoring](Omni.Celestial.CelestialBodyAuthoring.md)

## コンストラクター（Constructors）

### <a id="Omni_Celestial_CelestialBodyAuthoring__ctor"></a> CelestialBodyAuthoring\(\)

Unityの直列化復元用の空コンストラクタです。

```csharp
public CelestialBodyAuthoring()
```

### <a id="Omni_Celestial_CelestialBodyAuthoring__ctor_System_String_System_String_System_String_System_String_System_String_System_Boolean_System_String_System_String_System_String_System_String_System_String_"></a> CelestialBodyAuthoring\(string, string, string, string, string, bool, string, string, string, string, string\)

完全な天体Authoringレコードを構築します。入力値の妥当性はSnapshot化時に検証します。

```csharp
public CelestialBodyAuthoring(string key, string displayName, string diameterMeters, string massKilograms, string axialTiltDegrees, bool hasOrbitRecord = false, string orbitCenterKey = "", string semiMajorAxisMeters = "", string orbitalPeriodSeconds = "", string eccentricity = "0", string orbitalInclinationDegrees = "0")
```

#### 引数（Parameters）

`key` [string](https://learn.microsoft.com/dotnet/api/system.string)

一意な天体キー。

`displayName` [string](https://learn.microsoft.com/dotnet/api/system.string)

表示名。

`diameterMeters` [string](https://learn.microsoft.com/dotnet/api/system.string)

赤道直径（メートル）。

`massKilograms` [string](https://learn.microsoft.com/dotnet/api/system.string)

質量（キログラム）。

`axialTiltDegrees` [string](https://learn.microsoft.com/dotnet/api/system.string)

自転軸傾斜角（度）。

`hasOrbitRecord` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

軌道要素を使う場合はtrue。

`orbitCenterKey` [string](https://learn.microsoft.com/dotnet/api/system.string)

軌道中心の天体キー。

`semiMajorAxisMeters` [string](https://learn.microsoft.com/dotnet/api/system.string)

軌道長半径（メートル）。

`orbitalPeriodSeconds` [string](https://learn.microsoft.com/dotnet/api/system.string)

軌道周期（秒）。

`eccentricity` [string](https://learn.microsoft.com/dotnet/api/system.string)

離心率。

`orbitalInclinationDegrees` [string](https://learn.microsoft.com/dotnet/api/system.string)

軌道傾斜角（度）。

## プロパティ（Properties）

### <a id="Omni_Celestial_CelestialBodyAuthoring_AxialTiltDegreesText"></a> AxialTiltDegreesText

自転軸傾斜角（度）の正確な10進表記です。

```csharp
public string AxialTiltDegreesText { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Celestial_CelestialBodyAuthoring_DiameterMetersText"></a> DiameterMetersText

赤道直径（メートル）の正確な10進表記です。

```csharp
public string DiameterMetersText { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Celestial_CelestialBodyAuthoring_DisplayName"></a> DisplayName

UIやクレジットで使う表示名です。

```csharp
public string DisplayName { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Celestial_CelestialBodyAuthoring_EccentricityText"></a> EccentricityText

軌道離心率の正確な10進表記です。

```csharp
public string EccentricityText { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Celestial_CelestialBodyAuthoring_HasOrbitRecord"></a> HasOrbitRecord

軌道レコードを定義する場合はtrueです。

```csharp
public bool HasOrbitRecord { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Celestial_CelestialBodyAuthoring_Key"></a> Key

カタログ内で一意な、大文字小文字を区別する天体キーです。

```csharp
public string Key { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Celestial_CelestialBodyAuthoring_MassKilogramsText"></a> MassKilogramsText

質量（キログラム）の正確な10進表記です。

```csharp
public string MassKilogramsText { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Celestial_CelestialBodyAuthoring_OrbitCenterKey"></a> OrbitCenterKey

軌道中心天体のキーです。

```csharp
public string OrbitCenterKey { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Celestial_CelestialBodyAuthoring_OrbitalInclinationDegreesText"></a> OrbitalInclinationDegreesText

軌道傾斜角（度）の正確な10進表記です。

```csharp
public string OrbitalInclinationDegreesText { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Celestial_CelestialBodyAuthoring_OrbitalPeriodSecondsText"></a> OrbitalPeriodSecondsText

軌道周期（秒）の正確な10進表記です。

```csharp
public string OrbitalPeriodSecondsText { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Celestial_CelestialBodyAuthoring_SemiMajorAxisMetersText"></a> SemiMajorAxisMetersText

軌道長半径（メートル）の正確な10進表記です。

```csharp
public string SemiMajorAxisMetersText { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
