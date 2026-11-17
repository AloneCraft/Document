# <a id="Omni_Logical_Math"></a> Class Math

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

```csharp
[MovedFrom(true, "Omni.Logic", null, "Math")]
public static class Math
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[Math](Omni.Logical.Math.md)

## プロパティ（Properties）

### <a id="Omni_Logical_Math_E"></a> E

```csharp
public static Scalar E { get; }
```

#### 値（Property Value）

 [Scalar](Omni.Logical.Scalar.md)

### <a id="Omni_Logical_Math_Phi"></a> Phi

```csharp
public static Scalar Phi { get; }
```

#### 値（Property Value）

 [Scalar](Omni.Logical.Scalar.md)

### <a id="Omni_Logical_Math_Pi"></a> Pi

```csharp
public static Scalar Pi { get; }
```

#### 値（Property Value）

 [Scalar](Omni.Logical.Scalar.md)

### <a id="Omni_Logical_Math_Sqrt2"></a> Sqrt2

```csharp
public static Scalar Sqrt2 { get; }
```

#### 値（Property Value）

 [Scalar](Omni.Logical.Scalar.md)

### <a id="Omni_Logical_Math_Tau"></a> Tau

```csharp
public static Scalar Tau { get; }
```

#### 値（Property Value）

 [Scalar](Omni.Logical.Scalar.md)

## メソッド（Methods）

### <a id="Omni_Logical_Math_Max_Omni_Logical_Scalar__Omni_Logical_Scalar__"></a> Max\(in Scalar, in Scalar\)

```csharp
public static Scalar Max(in Scalar a, in Scalar b)
```

#### 引数（Parameters）

`a` [Scalar](Omni.Logical.Scalar.md)

`b` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [Scalar](Omni.Logical.Scalar.md)

### <a id="Omni_Logical_Math_Min_Omni_Logical_Scalar__Omni_Logical_Scalar__"></a> Min\(in Scalar, in Scalar\)

```csharp
public static Scalar Min(in Scalar a, in Scalar b)
```

#### 引数（Parameters）

`a` [Scalar](Omni.Logical.Scalar.md)

`b` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [Scalar](Omni.Logical.Scalar.md)

### <a id="Omni_Logical_Math_TryAbs_Omni_Logical_Scalar__Omni_Logical_Scalar__"></a> TryAbs\(in Scalar, out Scalar\)

```csharp
public static bool TryAbs(in Scalar value, out Scalar result)
```

#### 引数（Parameters）

`value` [Scalar](Omni.Logical.Scalar.md)

`result` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Math_TryCeiling_Omni_Logical_Scalar__Omni_Logical_Scalar__"></a> TryCeiling\(in Scalar, out Scalar\)

正の無限大方向へ整数化します。表現範囲超過は失敗します。

```csharp
public static bool TryCeiling(in Scalar value, out Scalar result)
```

#### 引数（Parameters）

`value` [Scalar](Omni.Logical.Scalar.md)

`result` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Math_TryClamp_Omni_Logical_Scalar__Omni_Logical_Scalar__Omni_Logical_Scalar__Omni_Logical_Scalar__"></a> TryClamp\(in Scalar, in Scalar, in Scalar, out Scalar\)

```csharp
public static bool TryClamp(in Scalar value, in Scalar min, in Scalar max, out Scalar result)
```

#### 引数（Parameters）

`value` [Scalar](Omni.Logical.Scalar.md)

`min` [Scalar](Omni.Logical.Scalar.md)

`max` [Scalar](Omni.Logical.Scalar.md)

`result` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Math_TryDivideRounded_Omni_Logical_Scalar__Omni_Logical_Scalar__Omni_Logical_Scalar__"></a> TryDivideRounded\(in Scalar, in Scalar, out Scalar\)

逆数を経由せずQ形式の商を求め、最近接偶数へ丸めます。
成功時の誤差は最大半量子です。

```csharp
public static bool TryDivideRounded(in Scalar numerator, in Scalar denominator, out Scalar result)
```

#### 引数（Parameters）

`numerator` [Scalar](Omni.Logical.Scalar.md)

`denominator` [Scalar](Omni.Logical.Scalar.md)

`result` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Math_TryFloor_Omni_Logical_Scalar__Omni_Logical_Scalar__"></a> TryFloor\(in Scalar, out Scalar\)

負の無限大方向へ整数化します。

```csharp
public static bool TryFloor(in Scalar value, out Scalar result)
```

#### 引数（Parameters）

`value` [Scalar](Omni.Logical.Scalar.md)

`result` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Math_TryLerp_Omni_Logical_Scalar__Omni_Logical_Scalar__Omni_Logical_Scalar__Omni_Logical_Scalar__"></a> TryLerp\(in Scalar, in Scalar, in Scalar, out Scalar\)

```csharp
public static bool TryLerp(in Scalar a, in Scalar b, in Scalar t, out Scalar result)
```

#### 引数（Parameters）

`a` [Scalar](Omni.Logical.Scalar.md)

`b` [Scalar](Omni.Logical.Scalar.md)

`t` [Scalar](Omni.Logical.Scalar.md)

`result` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Math_TryPowInteger_Omni_Logical_Scalar__System_Int64_Omni_Logical_Scalar__"></a> TryPowInteger\(in Scalar, long, out Scalar\)

整数べき乗です。各乗算と負指数の逆数はQ形式の最近接偶数丸めを行います。
0^0、ゼロの負数乗、中間結果の表現範囲超過は失敗します。

```csharp
public static bool TryPowInteger(in Scalar value, long exponent, out Scalar result)
```

#### 引数（Parameters）

`value` [Scalar](Omni.Logical.Scalar.md)

`exponent` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`result` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Math_TryRound_Omni_Logical_Scalar__Omni_Logical_Scalar__"></a> TryRound\(in Scalar, out Scalar\)

最近接偶数の整数へ丸めます。

```csharp
public static bool TryRound(in Scalar value, out Scalar result)
```

#### 引数（Parameters）

`value` [Scalar](Omni.Logical.Scalar.md)

`result` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Math_TrySqrt_Omni_Logical_Scalar__Omni_Logical_Scalar__"></a> TrySqrt\(in Scalar, out Scalar\)

非負値の平方根を固定長整数Newton法で求め、最近接偶数へ丸めます。
sqrt(0)は成功して0、負数と表現範囲超過は失敗します。

```csharp
public static bool TrySqrt(in Scalar value, out Scalar result)
```

#### 引数（Parameters）

`value` [Scalar](Omni.Logical.Scalar.md)

`result` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
