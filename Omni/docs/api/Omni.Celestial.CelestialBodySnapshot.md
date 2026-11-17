# <a id="Omni_Celestial_CelestialBodySnapshot"></a> Struct CelestialBodySnapshot

Namespace: [Omni.Celestial](Omni.Celestial.md)  
Assembly: Omni.Celestial.Core.dll  

1天体分の、検証済みで不変なカタログ値です。

```csharp
public readonly struct CelestialBodySnapshot
```

## コンストラクター（Constructors）

### <a id="Omni_Celestial_CelestialBodySnapshot__ctor_System_String_System_String_Omni_Celestial_CelestialPhysicalConstants_Omni_Celestial_CelestialOrbitalElements_"></a> CelestialBodySnapshot\(string, string, CelestialPhysicalConstants, CelestialOrbitalElements\)

検証済みの天体Snapshotを構築します。

```csharp
public CelestialBodySnapshot(string key, string displayName, CelestialPhysicalConstants physical, CelestialOrbitalElements orbit)
```

#### 引数（Parameters）

`key` [string](https://learn.microsoft.com/dotnet/api/system.string)

一意キー。

`displayName` [string](https://learn.microsoft.com/dotnet/api/system.string)

表示名。

`physical` [CelestialPhysicalConstants](Omni.Celestial.CelestialPhysicalConstants.md)

物理定数。

`orbit` [CelestialOrbitalElements](Omni.Celestial.CelestialOrbitalElements.md)

軌道要素。

## フィールド（Fields）

### <a id="Omni_Celestial_CelestialBodySnapshot_DisplayName"></a> DisplayName

画面表示名です。

```csharp
public readonly string DisplayName
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Celestial_CelestialBodySnapshot_Key"></a> Key

大文字小文字を区別する一意キーです。

```csharp
public readonly string Key
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Celestial_CelestialBodySnapshot_Orbit"></a> Orbit

軌道要素です。

```csharp
public readonly CelestialOrbitalElements Orbit
```

#### 値（Field Value）

 [CelestialOrbitalElements](Omni.Celestial.CelestialOrbitalElements.md)

### <a id="Omni_Celestial_CelestialBodySnapshot_Physical"></a> Physical

物理定数です。

```csharp
public readonly CelestialPhysicalConstants Physical
```

#### 値（Field Value）

 [CelestialPhysicalConstants](Omni.Celestial.CelestialPhysicalConstants.md)
