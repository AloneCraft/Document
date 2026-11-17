# <a id="Omni_Logical_NearClipMath"></a> Class NearClipMath

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

```csharp
[MovedFrom(true, "Omni", null, "LogicalNearClipMath")]
public static class NearClipMath
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[NearClipMath](Omni.Logical.NearClipMath.md)

## フィールド（Fields）

### <a id="Omni_Logical_NearClipMath_MaximumCullingNear"></a> MaximumCullingNear

保守的カリングNearのLogical上限です。

```csharp
public static readonly Scalar MaximumCullingNear
```

#### 値（Field Value）

 [Scalar](Omni.Logical.Scalar.md)

### <a id="Omni_Logical_NearClipMath_SafeRenderNearGuard"></a> SafeRenderNearGuard

安全render nearを丸め誤差分だけ内側へ倒す係数です。

```csharp
public const float SafeRenderNearGuard = 0.999999
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

## メソッド（Methods）

### <a id="Omni_Logical_NearClipMath_ConservativeCullingNear_Omni_Logical_Scalar__"></a> ConservativeCullingNear\(in Scalar\)

Logicalカリングへ渡すNearを下方向にだけ制限します。
不正な非正値は0（fail-open）へ倒します。

```csharp
public static Scalar ConservativeCullingNear(in Scalar logicalNear)
```

#### 引数（Parameters）

`logicalNear` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [Scalar](Omni.Logical.Scalar.md)

### <a id="Omni_Logical_NearClipMath_TryGetCenterUnderClipRatio_Omni_RadialSettings__Omni_Logical_Scalar__System_Single_System_Single__"></a> TryGetCenterUnderClipRatio\(in RadialSettings, in Scalar, float, out float\)

安全render nearによる画面中央の過小クリップ率を返します。

```csharp
public static bool TryGetCenterUnderClipRatio(in RadialSettings settings, in Scalar logicalNear, float cosMinAngle, out float ratio)
```

#### 引数（Parameters）

`settings` [RadialSettings](Omni.RadialSettings.md)

`logicalNear` [Scalar](Omni.Logical.Scalar.md)

`cosMinAngle` [float](https://learn.microsoft.com/dotnet/api/system.single)

`ratio` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_NearClipMath_TryGetOrthographicCosMinAngle_Omni_Logical_Scalar__System_Single_System_Single_System_Single__"></a> TryGetOrthographicCosMinAngle\(in Scalar, float, float, out float\)

平行投影のNear矩形四隅方向と前方の最小コサインを返します。

```csharp
public static bool TryGetOrthographicCosMinAngle(in Scalar logicalNear, float orthographicSize, float aspect, out float cosMinAngle)
```

#### 引数（Parameters）

`logicalNear` [Scalar](Omni.Logical.Scalar.md)

`orthographicSize` [float](https://learn.microsoft.com/dotnet/api/system.single)

`aspect` [float](https://learn.microsoft.com/dotnet/api/system.single)

`cosMinAngle` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_NearClipMath_TryGetPerspectiveCosMinAngle_System_Single_System_Single_System_Single__"></a> TryGetPerspectiveCosMinAngle\(float, float, out float\)

透視視錐台の四隅方向と前方の最小コサインを返します。

```csharp
public static bool TryGetPerspectiveCosMinAngle(float verticalFovDegrees, float aspect, out float cosMinAngle)
```

#### 引数（Parameters）

`verticalFovDegrees` [float](https://learn.microsoft.com/dotnet/api/system.single)

`aspect` [float](https://learn.microsoft.com/dotnet/api/system.single)

`cosMinAngle` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_NearClipMath_TryGetSafeRenderNear_Omni_RadialSettings__Omni_Logical_Scalar__System_Single_System_Single__"></a> TryGetSafeRenderNear\(in RadialSettings, in Scalar, float, out float\)

Logical Near平面より奥を過剰クリップしない描画空間Nearを返します。

```csharp
public static bool TryGetSafeRenderNear(in RadialSettings settings, in Scalar logicalNear, float cosMinAngle, out float safeRenderNear)
```

#### 引数（Parameters）

`settings` [RadialSettings](Omni.RadialSettings.md)

`logicalNear` [Scalar](Omni.Logical.Scalar.md)

`cosMinAngle` [float](https://learn.microsoft.com/dotnet/api/system.single)

`safeRenderNear` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_NearClipMath_TryGetSignedNearDistance_Omni_Logical_Vector3__Omni_Logical_Vector3__Omni_Logical_Scalar__Omni_Logical_Scalar__"></a> TryGetSignedNearDistance\(in Vector3, in Vector3, in Scalar, out Scalar\)

Logical Near平面までの符号付き距離を返します。負ならクリップ対象です。

```csharp
public static bool TryGetSignedNearDistance(in Vector3 cameraRelative, in Vector3 forward, in Scalar logicalNear, out Scalar signedDistance)
```

#### 引数（Parameters）

`cameraRelative` [Vector3](Omni.Logical.Vector3.md)

`forward` [Vector3](Omni.Logical.Vector3.md)

`logicalNear` [Scalar](Omni.Logical.Scalar.md)

`signedDistance` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_NearClipMath_TryGetViewDepth_Omni_Logical_Vector3__Omni_Logical_Vector3__Omni_Logical_Scalar__"></a> TryGetViewDepth\(in Vector3, in Vector3, out Scalar\)

カメラ相対Logical位置の前方成分をLogicalScalarで返します。

```csharp
public static bool TryGetViewDepth(in Vector3 cameraRelative, in Vector3 forward, out Scalar viewDepth)
```

#### 引数（Parameters）

`cameraRelative` [Vector3](Omni.Logical.Vector3.md)

`forward` [Vector3](Omni.Logical.Vector3.md)

`viewDepth` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
