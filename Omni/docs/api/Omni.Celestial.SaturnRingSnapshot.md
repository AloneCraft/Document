# <a id="Omni_Celestial_SaturnRingSnapshot"></a> Struct SaturnRingSnapshot

Namespace: [Omni.Celestial](Omni.Celestial.md)  
Assembly: Omni.Celestial.Core.dll  

Saturnリングの物理寸法だけを表す、Unity Objectを含まない不変値です。
Authoringの唯一の正本は、<xref href="Omni.Celestial.ISaturnRingDefinitionSource" data-throw-if-not-resolved="false"></xref>を実装する
既存のSaturnRingDefinitionAssetです。Galaxyはその型に依存せず、この値だけを読みます。

```csharp
public readonly struct SaturnRingSnapshot
```

## フィールド（Fields）

### <a id="Omni_Celestial_SaturnRingSnapshot_InnerRadius"></a> InnerRadius

リング内縁半径（メートル）のCPU側固定精度値です。

```csharp
public readonly Scalar InnerRadius
```

#### 値（Field Value）

 Scalar

### <a id="Omni_Celestial_SaturnRingSnapshot_OuterRadius"></a> OuterRadius

リング外縁半径（メートル）のCPU側固定精度値です。

```csharp
public readonly Scalar OuterRadius
```

#### 値（Field Value）

 Scalar

### <a id="Omni_Celestial_SaturnRingSnapshot_VerticalHalfHeight"></a> VerticalHalfHeight

リング平面からの最大高さ（メートル）のCPU側固定精度値です。

```csharp
public readonly Scalar VerticalHalfHeight
```

#### 値（Field Value）

 Scalar

## プロパティ（Properties）

### <a id="Omni_Celestial_SaturnRingSnapshot_InnerRadiusMeters"></a> InnerRadiusMeters

互換・表示境界用の内縁半径（m）です。

```csharp
public double InnerRadiusMeters { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Celestial_SaturnRingSnapshot_IsDefined"></a> IsDefined

物理寸法が有限かつ内外縁の順序を満たす場合はtrueです。

```csharp
public bool IsDefined { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Celestial_SaturnRingSnapshot_OuterRadiusMeters"></a> OuterRadiusMeters

互換・表示境界用の外縁半径（m）です。

```csharp
public double OuterRadiusMeters { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Celestial_SaturnRingSnapshot_VerticalHalfHeightMeters"></a> VerticalHalfHeightMeters

互換・表示境界用の最大高さ（m）です。

```csharp
public double VerticalHalfHeightMeters { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

## メソッド（Methods）

### <a id="Omni_Celestial_SaturnRingSnapshot_TryCreate_System_Double_System_Double_System_Double_Omni_Celestial_SaturnRingSnapshot__System_String__"></a> TryCreate\(double, double, double, out SaturnRingSnapshot, out string\)

物理寸法を検証し、成功時だけSnapshotを作成します。

```csharp
public static bool TryCreate(double innerRadiusMeters, double outerRadiusMeters, double verticalHalfHeightMeters, out SaturnRingSnapshot snapshot, out string error)
```

#### 引数（Parameters）

`innerRadiusMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

内縁半径（m）。

`outerRadiusMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

外縁半径（m）。

`verticalHalfHeightMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

平面からの最大高さ（m）。

`snapshot` [SaturnRingSnapshot](Omni.Celestial.SaturnRingSnapshot.md)

成功時の不変Snapshot。

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

失敗時の日本語エラー。成功時は空文字。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

物理寸法が有効な場合はtrue。

### <a id="Omni_Celestial_SaturnRingSnapshot_TryCreate_Omni_Logical_Scalar_Omni_Logical_Scalar_Omni_Logical_Scalar_Omni_Celestial_SaturnRingSnapshot__System_String__"></a> TryCreate\(Scalar, Scalar, Scalar, out SaturnRingSnapshot, out string\)

固定精度の物理寸法を検証し、成功時だけSnapshotを作成します。

```csharp
public static bool TryCreate(Scalar innerRadius, Scalar outerRadius, Scalar verticalHalfHeight, out SaturnRingSnapshot snapshot, out string error)
```

#### 引数（Parameters）

`innerRadius` Scalar

`outerRadius` Scalar

`verticalHalfHeight` Scalar

`snapshot` [SaturnRingSnapshot](Omni.Celestial.SaturnRingSnapshot.md)

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
