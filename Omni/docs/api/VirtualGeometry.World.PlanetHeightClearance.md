# <a id="VirtualGeometry_World_PlanetHeightClearance"></a> Class PlanetHeightClearance

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

描画と同じ高さの正本(<xref href="VirtualGeometry.World.IPlanetHeightProvider" data-throw-if-not-resolved="false"></xref>)から、天体のローカル位置(m)と地面との距離を求め、地面より上へ保つ。
位置・半径・余裕はメートル。spacingMeters は高さを聞く網目の間隔(0 は全帯域)。高さが NaN(届いていない)なら例外にする(偽の地面で判定しない)。

```csharp
public static class PlanetHeightClearance
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetHeightClearance](VirtualGeometry.World.PlanetHeightClearance.md)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetHeightClearance_ClampRadius_VirtualGeometry_World_PlanetDouble3_VirtualGeometry_World_IPlanetHeightProvider_System_Double_System_Double_System_Double_"></a> ClampRadius\(PlanetDouble3, IPlanetHeightProvider, double, double, double\)

地面から clearance(m)より低ければ持ち上げる。高ければそのまま返す。

```csharp
public static PlanetDouble3 ClampRadius(PlanetDouble3 position, IPlanetHeightProvider source, double radius, double clearance, double spacingMeters = 0)
```

#### 引数（Parameters）

`position` [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

`source` [IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

`radius` [double](https://learn.microsoft.com/dotnet/api/system.double)

`clearance` [double](https://learn.microsoft.com/dotnet/api/system.double)

`spacingMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

### <a id="VirtualGeometry_World_PlanetHeightClearance_GetClearanceMeters_VirtualGeometry_World_PlanetDouble3_VirtualGeometry_World_IPlanetHeightProvider_System_Double_System_Double_"></a> GetClearanceMeters\(PlanetDouble3, IPlanetHeightProvider, double, double\)

位置と地面との符号付きの距離(m。地面より上が正)。

```csharp
public static double GetClearanceMeters(PlanetDouble3 position, IPlanetHeightProvider source, double radius, double spacingMeters = 0)
```

#### 引数（Parameters）

`position` [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

`source` [IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

`radius` [double](https://learn.microsoft.com/dotnet/api/system.double)

`spacingMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetHeightClearance_Length_VirtualGeometry_World_PlanetDouble3_"></a> Length\(PlanetDouble3\)

```csharp
public static double Length(PlanetDouble3 value)
```

#### 引数（Parameters）

`value` [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetHeightClearance_Normalize_VirtualGeometry_World_PlanetDouble3_"></a> Normalize\(PlanetDouble3\)

長さ 1 にした方向。0・有限でない値は例外。

```csharp
public static PlanetDouble3 Normalize(PlanetDouble3 value)
```

#### 引数（Parameters）

`value` [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

#### 戻り値（Returns）

 [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

### <a id="VirtualGeometry_World_PlanetHeightClearance_SetClearanceMeters_VirtualGeometry_World_PlanetDouble3_VirtualGeometry_World_IPlanetHeightProvider_System_Double_System_Double_System_Double_"></a> SetClearanceMeters\(PlanetDouble3, IPlanetHeightProvider, double, double, double\)

方向を保ったまま、地面から clearance(m)の位置へ移す。

```csharp
public static PlanetDouble3 SetClearanceMeters(PlanetDouble3 position, IPlanetHeightProvider source, double radius, double clearance, double spacingMeters = 0)
```

#### 引数（Parameters）

`position` [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

`source` [IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

`radius` [double](https://learn.microsoft.com/dotnet/api/system.double)

`clearance` [double](https://learn.microsoft.com/dotnet/api/system.double)

`spacingMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

### <a id="VirtualGeometry_World_PlanetHeightClearance_SurfaceRadius_VirtualGeometry_World_PlanetDouble3_VirtualGeometry_World_IPlanetHeightProvider_System_Double_System_Double_"></a> SurfaceRadius\(PlanetDouble3, IPlanetHeightProvider, double, double\)

位置の真下の地面の半径(m)。

```csharp
public static double SurfaceRadius(PlanetDouble3 position, IPlanetHeightProvider source, double radius, double spacingMeters = 0)
```

#### 引数（Parameters）

`position` [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

`source` [IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

`radius` [double](https://learn.microsoft.com/dotnet/api/system.double)

`spacingMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)
