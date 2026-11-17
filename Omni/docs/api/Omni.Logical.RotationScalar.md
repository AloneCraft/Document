# <a id="Omni_Logical_RotationScalar"></a> Struct RotationScalar

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

回転成分用の固定小数点数（Q1.126、128ビット符号付き2の補数）です。
整数部1ビット・小数部<xref href="Omni.Logical.Precision.RotationFractionalBits" data-throw-if-not-resolved="false"></xref>ビットで、
数値 = SignedRawInteger / 2^RotationFractionalBits、範囲は -2〜2 - 2^-RotationFractionalBits です。
<xref href="Omni.Logical.Quaternion" data-throw-if-not-resolved="false"></xref>の各成分として使います。
クォータニオン成分は常に -1〜1 に収まるため、整数部を増やしても無駄になるだけです。
生表現は<xref href="Omni.Logical.Scalar" data-throw-if-not-resolved="false"></xref>（位置・長さ）と別の128ビット型（<xref href="Omni.Logical.IntRaw128" data-throw-if-not-resolved="false"></xref>）で、
位置を192ビットへ広げても回転は128ビットのままにします（2026-10-05 のユーザーの判断: 保存した回転成分の量子化が位置に
与える誤差は距離 × 約2×10^-38 で、速さと保存値を優先する）。回転同士の演算は128ビット、位置との積は192ビットへ広げて計算します。
ただし正規化と補間（nlerp）は係数をScalar（2^-96刻み）で持つため、それを経た成分の誤差は、単位Quaternionでは導出した上限で
約4.75×2^-96（約6×10^-29）以内で（上限の式は<xref href="Omni.Logical.Quaternion.TryNormalize(Omni.Logical.Quaternion%40%2cOmni.Logical.Quaternion%40)" data-throw-if-not-resolved="false"></xref>にあります）、
その回転が位置に与える誤差は距離 × 10^-28 の桁以下になります。
Silent Wraparound / Silent Clampは行わず、Overflowが起き得る演算はすべてTry APIです。

```csharp
public readonly struct RotationScalar : IEquatable<RotationScalar>, IComparable<RotationScalar>
```

#### 実装するインターフェース（Implements）

[IEquatable<RotationScalar\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1), 
[IComparable<RotationScalar\>](https://learn.microsoft.com/dotnet/api/system.icomparable\-1)

## コンストラクター（Constructors）

### <a id="Omni_Logical_RotationScalar__ctor_Omni_Logical_IntRaw128__"></a> RotationScalar\(in IntRaw128\)

生の128ビット表現から値を構築します。

```csharp
public RotationScalar(in IntRaw128 raw)
```

#### 引数（Parameters）

`raw` [IntRaw128](Omni.Logical.IntRaw128.md)

## フィールド（Fields）

### <a id="Omni_Logical_RotationScalar_FractionalBits"></a> FractionalBits

小数部のビット数です。

```csharp
public const int FractionalBits = 126
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_RotationScalar_One"></a> One

1.0を表す値です（Raw = 2^FractionalBits）。

```csharp
public static readonly RotationScalar One
```

#### 値（Field Value）

 [RotationScalar](Omni.Logical.RotationScalar.md)

### <a id="Omni_Logical_RotationScalar_Raw"></a> Raw

この値の生の128ビット2の補数表現です。

```csharp
public readonly IntRaw128 Raw
```

#### 値（Field Value）

 [IntRaw128](Omni.Logical.IntRaw128.md)

### <a id="Omni_Logical_RotationScalar_Zero"></a> Zero

ゼロ値です。

```csharp
public static readonly RotationScalar Zero
```

#### 値（Field Value）

 [RotationScalar](Omni.Logical.RotationScalar.md)

## プロパティ（Properties）

### <a id="Omni_Logical_RotationScalar_IsNegative"></a> IsNegative

この値が負であればtrueです。

```csharp
public bool IsNegative { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_RotationScalar_IsZero"></a> IsZero

この値がゼロであればtrueです。

```csharp
public bool IsZero { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_Logical_RotationScalar_CompareTo_Omni_Logical_RotationScalar_"></a> CompareTo\(RotationScalar\)

```csharp
public int CompareTo(RotationScalar other)
```

#### 引数（Parameters）

`other` [RotationScalar](Omni.Logical.RotationScalar.md)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_RotationScalar_Equals_Omni_Logical_RotationScalar_"></a> Equals\(RotationScalar\)

```csharp
public bool Equals(RotationScalar other)
```

#### 引数（Parameters）

`other` [RotationScalar](Omni.Logical.RotationScalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_RotationScalar_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object obj)
```

#### 引数（Parameters）

`obj` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_RotationScalar_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_RotationScalar_ToString"></a> ToString\(\)

```csharp
public override string ToString()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Logical_RotationScalar_TryFromDouble_System_Double_Omni_Logical_RotationScalar__"></a> TryFromDouble\(double, out RotationScalar\)

倍精度値（|value| &lt; 2）を最近接偶数で回転成分へ量子化します。非有限値と表現範囲外は失敗します。

```csharp
public static bool TryFromDouble(double value, out RotationScalar result)
```

#### 引数（Parameters）

`value` [double](https://learn.microsoft.com/dotnet/api/system.double)

`result` [RotationScalar](Omni.Logical.RotationScalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_RotationScalar_TryFromFloat_System_Single_Omni_Logical_RotationScalar__"></a> TryFromFloat\(float, out RotationScalar\)

IEEE 754単精度値からの変換を試みます。
非有限値と表現範囲外（-2以上2未満の外）は失敗します。
分解能（2^-126）より細かい端数を持つ値（絶対値が約2^-103より小さいfloat）は、最近接偶数で丸めて成功します
（無損失ではありません）。

```csharp
public static bool TryFromFloat(float value, out RotationScalar result)
```

#### 引数（Parameters）

`value` [float](https://learn.microsoft.com/dotnet/api/system.single)

`result` [RotationScalar](Omni.Logical.RotationScalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_RotationScalar_TryNegate_Omni_Logical_RotationScalar__Omni_Logical_RotationScalar__"></a> TryNegate\(in RotationScalar, out RotationScalar\)

符号反転を試みます。表現可能な最小値（-2、Raw=<xref href="Omni.Logical.IntRaw128.MinValue" data-throw-if-not-resolved="false"></xref>）の反転は失敗します。

```csharp
public static bool TryNegate(in RotationScalar value, out RotationScalar result)
```

#### 引数（Parameters）

`value` [RotationScalar](Omni.Logical.RotationScalar.md)

`result` [RotationScalar](Omni.Logical.RotationScalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_RotationScalar_TryToDouble_System_Double__"></a> TryToDouble\(out double\)

最近接偶数の倍精度値への変換を試みます(回転の成分は |value| &lt; 2 なので常に成功します)。

```csharp
public bool TryToDouble(out double result)
```

#### 引数（Parameters）

`result` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_RotationScalar_TryToFloat_System_Single__"></a> TryToFloat\(out float\)

有限なIEEE 754単精度値への変換を試みます。
必要な丸めは最近接偶数で行います。

```csharp
public bool TryToFloat(out float result)
```

#### 引数（Parameters）

`result` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## 演算子（Operators）

### <a id="Omni_Logical_RotationScalar_op_Equality_Omni_Logical_RotationScalar_Omni_Logical_RotationScalar_"></a> operator ==\(RotationScalar, RotationScalar\)

2つの値が等しい場合はtrueです。

```csharp
public static bool operator ==(RotationScalar left, RotationScalar right)
```

#### 引数（Parameters）

`left` [RotationScalar](Omni.Logical.RotationScalar.md)

`right` [RotationScalar](Omni.Logical.RotationScalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_RotationScalar_op_GreaterThan_Omni_Logical_RotationScalar_Omni_Logical_RotationScalar_"></a> operator \>\(RotationScalar, RotationScalar\)

左辺が大きい場合はtrueです。

```csharp
public static bool operator >(RotationScalar left, RotationScalar right)
```

#### 引数（Parameters）

`left` [RotationScalar](Omni.Logical.RotationScalar.md)

`right` [RotationScalar](Omni.Logical.RotationScalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_RotationScalar_op_GreaterThanOrEqual_Omni_Logical_RotationScalar_Omni_Logical_RotationScalar_"></a> operator \>=\(RotationScalar, RotationScalar\)

左辺が同じか大きい場合はtrueです。

```csharp
public static bool operator >=(RotationScalar left, RotationScalar right)
```

#### 引数（Parameters）

`left` [RotationScalar](Omni.Logical.RotationScalar.md)

`right` [RotationScalar](Omni.Logical.RotationScalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_RotationScalar_op_Inequality_Omni_Logical_RotationScalar_Omni_Logical_RotationScalar_"></a> operator \!=\(RotationScalar, RotationScalar\)

2つの値が異なる場合はtrueです。

```csharp
public static bool operator !=(RotationScalar left, RotationScalar right)
```

#### 引数（Parameters）

`left` [RotationScalar](Omni.Logical.RotationScalar.md)

`right` [RotationScalar](Omni.Logical.RotationScalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_RotationScalar_op_LessThan_Omni_Logical_RotationScalar_Omni_Logical_RotationScalar_"></a> operator <\(RotationScalar, RotationScalar\)

左辺が小さい場合はtrueです。

```csharp
public static bool operator <(RotationScalar left, RotationScalar right)
```

#### 引数（Parameters）

`left` [RotationScalar](Omni.Logical.RotationScalar.md)

`right` [RotationScalar](Omni.Logical.RotationScalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_RotationScalar_op_LessThanOrEqual_Omni_Logical_RotationScalar_Omni_Logical_RotationScalar_"></a> operator <=\(RotationScalar, RotationScalar\)

左辺が同じか小さい場合はtrueです。

```csharp
public static bool operator <=(RotationScalar left, RotationScalar right)
```

#### 引数（Parameters）

`left` [RotationScalar](Omni.Logical.RotationScalar.md)

`right` [RotationScalar](Omni.Logical.RotationScalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
