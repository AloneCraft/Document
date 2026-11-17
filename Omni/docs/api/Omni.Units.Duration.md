# <a id="Omni_Units_Duration"></a> Struct Duration

Namespace: [Omni.Units](Omni.Units.md)  
Assembly: Radial.Runtime.dll  

秒を保持する符号付きQ63.64固定小数点値です。
シーケンス・物理・音声時刻のCPU側Source of Truthに使用します。

```csharp
public readonly struct Duration : IEquatable<Duration>, IComparable<Duration>
```

#### 実装するインターフェース（Implements）

[IEquatable<Duration\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1), 
[IComparable<Duration\>](https://learn.microsoft.com/dotnet/api/system.icomparable\-1)

## フィールド（Fields）

### <a id="Omni_Units_Duration_FractionalBits"></a> FractionalBits

```csharp
public const int FractionalBits = 64
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Units_Duration_OneSecond"></a> OneSecond

```csharp
public static readonly Duration OneSecond
```

#### 値（Field Value）

 [Duration](Omni.Units.Duration.md)

### <a id="Omni_Units_Duration_Zero"></a> Zero

```csharp
public static readonly Duration Zero
```

#### 値（Field Value）

 [Duration](Omni.Units.Duration.md)

## プロパティ（Properties）

### <a id="Omni_Units_Duration_IsNegative"></a> IsNegative

```csharp
public bool IsNegative { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Duration_IsZero"></a> IsZero

```csharp
public bool IsZero { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_Units_Duration_CompareTo_Omni_Units_Duration_"></a> CompareTo\(Duration\)

```csharp
public int CompareTo(Duration other)
```

#### 引数（Parameters）

`other` [Duration](Omni.Units.Duration.md)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Units_Duration_Equals_Omni_Units_Duration_"></a> Equals\(Duration\)

```csharp
public bool Equals(Duration other)
```

#### 引数（Parameters）

`other` [Duration](Omni.Units.Duration.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Duration_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object obj)
```

#### 引数（Parameters）

`obj` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Duration_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Units_Duration_ToString"></a> ToString\(\)

```csharp
public override string ToString()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Units_Duration_TryAdd_Omni_Units_Duration__Omni_Units_Duration__Omni_Units_Duration__"></a> TryAdd\(in Duration, in Duration, out Duration\)

```csharp
public static bool TryAdd(in Duration left, in Duration right, out Duration result)
```

#### 引数（Parameters）

`left` [Duration](Omni.Units.Duration.md)

`right` [Duration](Omni.Units.Duration.md)

`result` [Duration](Omni.Units.Duration.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Duration_TryDivideToFloor_Omni_Units_Duration__Omni_Units_Duration__System_Int64__"></a> TryDivideToFloor\(in Duration, in Duration, out long\)

2つの非負Durationの比を切り捨て、Int64へ返します。

```csharp
public static bool TryDivideToFloor(in Duration numerator, in Duration denominator, out long quotient)
```

#### 引数（Parameters）

`numerator` [Duration](Omni.Units.Duration.md)

`denominator` [Duration](Omni.Units.Duration.md)

`quotient` [long](https://learn.microsoft.com/dotnet/api/system.int64)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Duration_TryFromSeconds_System_String_Omni_Units_Duration__"></a> TryFromSeconds\(string, out Duration\)

```csharp
public static bool TryFromSeconds(string text, out Duration result)
```

#### 引数（Parameters）

`text` [string](https://learn.microsoft.com/dotnet/api/system.string)

`result` [Duration](Omni.Units.Duration.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Duration_TryFromSeconds_System_Double_Omni_Units_Duration__"></a> TryFromSeconds\(double, out Duration\)

```csharp
public static bool TryFromSeconds(double value, out Duration result)
```

#### 引数（Parameters）

`value` [double](https://learn.microsoft.com/dotnet/api/system.double)

`result` [Duration](Omni.Units.Duration.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Duration_TryMultiply_Omni_Units_Duration__System_Int64_Omni_Units_Duration__"></a> TryMultiply\(in Duration, long, out Duration\)

```csharp
public static bool TryMultiply(in Duration value, long multiplier, out Duration result)
```

#### 引数（Parameters）

`value` [Duration](Omni.Units.Duration.md)

`multiplier` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`result` [Duration](Omni.Units.Duration.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Duration_TryScale_Omni_Units_Duration__Omni_Units_TimeScale__Omni_Units_Duration__"></a> TryScale\(in Duration, in TimeScale, out Duration\)

```csharp
public static bool TryScale(in Duration value, in TimeScale scale, out Duration result)
```

#### 引数（Parameters）

`value` [Duration](Omni.Units.Duration.md)

`scale` [TimeScale](Omni.Units.TimeScale.md)

`result` [Duration](Omni.Units.Duration.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Duration_TrySubtract_Omni_Units_Duration__Omni_Units_Duration__Omni_Units_Duration__"></a> TrySubtract\(in Duration, in Duration, out Duration\)

```csharp
public static bool TrySubtract(in Duration left, in Duration right, out Duration result)
```

#### 引数（Parameters）

`left` [Duration](Omni.Units.Duration.md)

`right` [Duration](Omni.Units.Duration.md)

`result` [Duration](Omni.Units.Duration.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Duration_TryToSeconds_System_Double__"></a> TryToSeconds\(out double\)

```csharp
public bool TryToSeconds(out double result)
```

#### 引数（Parameters）

`result` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Duration_TryToSecondsFloat_System_Single__"></a> TryToSecondsFloat\(out float\)

```csharp
public bool TryToSecondsFloat(out float result)
```

#### 引数（Parameters）

`result` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## 演算子（Operators）

### <a id="Omni_Units_Duration_op_Equality_Omni_Units_Duration_Omni_Units_Duration_"></a> operator ==\(Duration, Duration\)

```csharp
public static bool operator ==(Duration left, Duration right)
```

#### 引数（Parameters）

`left` [Duration](Omni.Units.Duration.md)

`right` [Duration](Omni.Units.Duration.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Duration_op_GreaterThan_Omni_Units_Duration_Omni_Units_Duration_"></a> operator \>\(Duration, Duration\)

```csharp
public static bool operator >(Duration left, Duration right)
```

#### 引数（Parameters）

`left` [Duration](Omni.Units.Duration.md)

`right` [Duration](Omni.Units.Duration.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Duration_op_GreaterThanOrEqual_Omni_Units_Duration_Omni_Units_Duration_"></a> operator \>=\(Duration, Duration\)

```csharp
public static bool operator >=(Duration left, Duration right)
```

#### 引数（Parameters）

`left` [Duration](Omni.Units.Duration.md)

`right` [Duration](Omni.Units.Duration.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Duration_op_Inequality_Omni_Units_Duration_Omni_Units_Duration_"></a> operator \!=\(Duration, Duration\)

```csharp
public static bool operator !=(Duration left, Duration right)
```

#### 引数（Parameters）

`left` [Duration](Omni.Units.Duration.md)

`right` [Duration](Omni.Units.Duration.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Duration_op_LessThan_Omni_Units_Duration_Omni_Units_Duration_"></a> operator <\(Duration, Duration\)

```csharp
public static bool operator <(Duration left, Duration right)
```

#### 引数（Parameters）

`left` [Duration](Omni.Units.Duration.md)

`right` [Duration](Omni.Units.Duration.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Duration_op_LessThanOrEqual_Omni_Units_Duration_Omni_Units_Duration_"></a> operator <=\(Duration, Duration\)

```csharp
public static bool operator <=(Duration left, Duration right)
```

#### 引数（Parameters）

`left` [Duration](Omni.Units.Duration.md)

`right` [Duration](Omni.Units.Duration.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
