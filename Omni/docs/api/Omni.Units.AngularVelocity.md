# <a id="Omni_Units_AngularVelocity"></a> Struct AngularVelocity

Namespace: [Omni.Units](Omni.Units.md)  
Assembly: Radial.Runtime.dll  

角速度を保持する符号付きQ31.96固定小数点値です。
公開入出力はrad/s、内部値は位相加算を正確に行えるturn/sです。

```csharp
public readonly struct AngularVelocity : IEquatable<AngularVelocity>, IComparable<AngularVelocity>
```

#### 実装するインターフェース（Implements）

[IEquatable<AngularVelocity\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1), 
[IComparable<AngularVelocity\>](https://learn.microsoft.com/dotnet/api/system.icomparable\-1)

## フィールド（Fields）

### <a id="Omni_Units_AngularVelocity_FractionalBits"></a> FractionalBits

```csharp
public const int FractionalBits = 96
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Units_AngularVelocity_Zero"></a> Zero

```csharp
public static readonly AngularVelocity Zero
```

#### 値（Field Value）

 [AngularVelocity](Omni.Units.AngularVelocity.md)

## プロパティ（Properties）

### <a id="Omni_Units_AngularVelocity_IsNegative"></a> IsNegative

```csharp
public bool IsNegative { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_AngularVelocity_IsZero"></a> IsZero

```csharp
public bool IsZero { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_Units_AngularVelocity_CompareTo_Omni_Units_AngularVelocity_"></a> CompareTo\(AngularVelocity\)

```csharp
public int CompareTo(AngularVelocity other)
```

#### 引数（Parameters）

`other` [AngularVelocity](Omni.Units.AngularVelocity.md)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Units_AngularVelocity_Equals_Omni_Units_AngularVelocity_"></a> Equals\(AngularVelocity\)

```csharp
public bool Equals(AngularVelocity other)
```

#### 引数（Parameters）

`other` [AngularVelocity](Omni.Units.AngularVelocity.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_AngularVelocity_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object obj)
```

#### 引数（Parameters）

`obj` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_AngularVelocity_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Units_AngularVelocity_ToString"></a> ToString\(\)

```csharp
public override string ToString()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Units_AngularVelocity_TryApplyOrbitClassQ16_Omni_Units_AngularVelocity__System_UInt16_Omni_Units_AngularVelocity__"></a> TryApplyOrbitClassQ16\(in AngularVelocity, ushort, out AngularVelocity\)

0.9〜1.0の軌道クラス係数をQ16で適用します。

```csharp
public static bool TryApplyOrbitClassQ16(in AngularVelocity value, ushort orbitClassQ16, out AngularVelocity result)
```

#### 引数（Parameters）

`value` [AngularVelocity](Omni.Units.AngularVelocity.md)

`orbitClassQ16` [ushort](https://learn.microsoft.com/dotnet/api/system.uint16)

`result` [AngularVelocity](Omni.Units.AngularVelocity.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_AngularVelocity_TryCalculateHalfCellWindow_System_Int32_Omni_Units_AngularVelocity__Omni_Units_Duration__"></a> TryCalculateHalfCellWindow\(int, in AngularVelocity, out Duration\)

```csharp
public static bool TryCalculateHalfCellWindow(int angularCellCount, in AngularVelocity maximumVelocity, out Duration result)
```

#### 引数（Parameters）

`angularCellCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`maximumVelocity` [AngularVelocity](Omni.Units.AngularVelocity.md)

`result` [Duration](Omni.Units.Duration.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_AngularVelocity_TryFromKepler_Omni_Logical_Scalar__Omni_Logical_Scalar__Omni_Units_AngularVelocity__"></a> TryFromKepler\(in Scalar, in Scalar, out AngularVelocity\)

μと軌道半径からsqrt(μ/r³)を固定小数点だけで求めます。
μ/rを先に求めることでScalarの中間値を範囲内に保ち、
最後の除算をQ31.96へ直接丸めます。

```csharp
public static bool TryFromKepler(in Scalar gravitationalParameter, in Scalar radiusMeters, out AngularVelocity result)
```

#### 引数（Parameters）

`gravitationalParameter` [Scalar](Omni.Logical.Scalar.md)

`radiusMeters` [Scalar](Omni.Logical.Scalar.md)

`result` [AngularVelocity](Omni.Units.AngularVelocity.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_AngularVelocity_TryFromRadiansPerSecond_System_String_Omni_Units_AngularVelocity__"></a> TryFromRadiansPerSecond\(string, out AngularVelocity\)

```csharp
public static bool TryFromRadiansPerSecond(string text, out AngularVelocity result)
```

#### 引数（Parameters）

`text` [string](https://learn.microsoft.com/dotnet/api/system.string)

`result` [AngularVelocity](Omni.Units.AngularVelocity.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_AngularVelocity_TryFromRadiansPerSecond_System_Double_Omni_Units_AngularVelocity__"></a> TryFromRadiansPerSecond\(double, out AngularVelocity\)

```csharp
public static bool TryFromRadiansPerSecond(double value, out AngularVelocity result)
```

#### 引数（Parameters）

`value` [double](https://learn.microsoft.com/dotnet/api/system.double)

`result` [AngularVelocity](Omni.Units.AngularVelocity.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_AngularVelocity_TryLerpQ16_Omni_Units_AngularVelocity__Omni_Units_AngularVelocity__System_UInt16_Omni_Units_AngularVelocity__"></a> TryLerpQ16\(in AngularVelocity, in AngularVelocity, ushort, out AngularVelocity\)

2つの角速度をQ16比率で線形補間します。

```csharp
public static bool TryLerpQ16(in AngularVelocity from, in AngularVelocity to, ushort ratioQ16, out AngularVelocity result)
```

#### 引数（Parameters）

`from` [AngularVelocity](Omni.Units.AngularVelocity.md)

`to` [AngularVelocity](Omni.Units.AngularVelocity.md)

`ratioQ16` [ushort](https://learn.microsoft.com/dotnet/api/system.uint16)

`result` [AngularVelocity](Omni.Units.AngularVelocity.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_AngularVelocity_TryLerpQ32_Omni_Units_AngularVelocity__Omni_Units_AngularVelocity__System_UInt32_Omni_Units_AngularVelocity__"></a> TryLerpQ32\(in AngularVelocity, in AngularVelocity, uint, out AngularVelocity\)

```csharp
public static bool TryLerpQ32(in AngularVelocity from, in AngularVelocity to, uint ratioQ32, out AngularVelocity result)
```

#### 引数（Parameters）

`from` [AngularVelocity](Omni.Units.AngularVelocity.md)

`to` [AngularVelocity](Omni.Units.AngularVelocity.md)

`ratioQ32` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`result` [AngularVelocity](Omni.Units.AngularVelocity.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_AngularVelocity_TryMultiply_Omni_Units_AngularVelocity__Omni_Units_Duration__Omni_Units_Angle__"></a> TryMultiply\(in AngularVelocity, in Duration, out Angle\)

```csharp
public static bool TryMultiply(in AngularVelocity velocity, in Duration duration, out Angle result)
```

#### 引数（Parameters）

`velocity` [AngularVelocity](Omni.Units.AngularVelocity.md)

`duration` [Duration](Omni.Units.Duration.md)

`result` [Angle](Omni.Units.Angle.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_AngularVelocity_TryScale_Omni_Units_AngularVelocity__Omni_Units_TimeScale__Omni_Units_AngularVelocity__"></a> TryScale\(in AngularVelocity, in TimeScale, out AngularVelocity\)

```csharp
public static bool TryScale(in AngularVelocity value, in TimeScale scale, out AngularVelocity result)
```

#### 引数（Parameters）

`value` [AngularVelocity](Omni.Units.AngularVelocity.md)

`scale` [TimeScale](Omni.Units.TimeScale.md)

`result` [AngularVelocity](Omni.Units.AngularVelocity.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_AngularVelocity_TryToRadiansPerSecond_System_Double__"></a> TryToRadiansPerSecond\(out double\)

```csharp
public bool TryToRadiansPerSecond(out double result)
```

#### 引数（Parameters）

`result` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## 演算子（Operators）

### <a id="Omni_Units_AngularVelocity_op_Equality_Omni_Units_AngularVelocity_Omni_Units_AngularVelocity_"></a> operator ==\(AngularVelocity, AngularVelocity\)

```csharp
public static bool operator ==(AngularVelocity left, AngularVelocity right)
```

#### 引数（Parameters）

`left` [AngularVelocity](Omni.Units.AngularVelocity.md)

`right` [AngularVelocity](Omni.Units.AngularVelocity.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_AngularVelocity_op_GreaterThan_Omni_Units_AngularVelocity_Omni_Units_AngularVelocity_"></a> operator \>\(AngularVelocity, AngularVelocity\)

```csharp
public static bool operator >(AngularVelocity left, AngularVelocity right)
```

#### 引数（Parameters）

`left` [AngularVelocity](Omni.Units.AngularVelocity.md)

`right` [AngularVelocity](Omni.Units.AngularVelocity.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_AngularVelocity_op_GreaterThanOrEqual_Omni_Units_AngularVelocity_Omni_Units_AngularVelocity_"></a> operator \>=\(AngularVelocity, AngularVelocity\)

```csharp
public static bool operator >=(AngularVelocity left, AngularVelocity right)
```

#### 引数（Parameters）

`left` [AngularVelocity](Omni.Units.AngularVelocity.md)

`right` [AngularVelocity](Omni.Units.AngularVelocity.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_AngularVelocity_op_Inequality_Omni_Units_AngularVelocity_Omni_Units_AngularVelocity_"></a> operator \!=\(AngularVelocity, AngularVelocity\)

```csharp
public static bool operator !=(AngularVelocity left, AngularVelocity right)
```

#### 引数（Parameters）

`left` [AngularVelocity](Omni.Units.AngularVelocity.md)

`right` [AngularVelocity](Omni.Units.AngularVelocity.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_AngularVelocity_op_LessThan_Omni_Units_AngularVelocity_Omni_Units_AngularVelocity_"></a> operator <\(AngularVelocity, AngularVelocity\)

```csharp
public static bool operator <(AngularVelocity left, AngularVelocity right)
```

#### 引数（Parameters）

`left` [AngularVelocity](Omni.Units.AngularVelocity.md)

`right` [AngularVelocity](Omni.Units.AngularVelocity.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_AngularVelocity_op_LessThanOrEqual_Omni_Units_AngularVelocity_Omni_Units_AngularVelocity_"></a> operator <=\(AngularVelocity, AngularVelocity\)

```csharp
public static bool operator <=(AngularVelocity left, AngularVelocity right)
```

#### 引数（Parameters）

`left` [AngularVelocity](Omni.Units.AngularVelocity.md)

`right` [AngularVelocity](Omni.Units.AngularVelocity.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
