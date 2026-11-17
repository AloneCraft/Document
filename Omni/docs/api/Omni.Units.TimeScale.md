# <a id="Omni_Units_TimeScale"></a> Struct TimeScale

Namespace: [Omni.Units](Omni.Units.md)  
Assembly: Radial.Runtime.dll  

時間倍率を保持する符号付きQ31.96固定小数点値です。

```csharp
public readonly struct TimeScale : IEquatable<TimeScale>, IComparable<TimeScale>
```

#### 実装するインターフェース（Implements）

[IEquatable<TimeScale\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1), 
[IComparable<TimeScale\>](https://learn.microsoft.com/dotnet/api/system.icomparable\-1)

## フィールド（Fields）

### <a id="Omni_Units_TimeScale_FractionalBits"></a> FractionalBits

```csharp
public const int FractionalBits = 96
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Units_TimeScale_One"></a> One

```csharp
public static readonly TimeScale One
```

#### 値（Field Value）

 [TimeScale](Omni.Units.TimeScale.md)

### <a id="Omni_Units_TimeScale_Zero"></a> Zero

```csharp
public static readonly TimeScale Zero
```

#### 値（Field Value）

 [TimeScale](Omni.Units.TimeScale.md)

## プロパティ（Properties）

### <a id="Omni_Units_TimeScale_IsNegative"></a> IsNegative

```csharp
public bool IsNegative { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_TimeScale_IsZero"></a> IsZero

```csharp
public bool IsZero { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_Units_TimeScale_CompareTo_Omni_Units_TimeScale_"></a> CompareTo\(TimeScale\)

```csharp
public int CompareTo(TimeScale other)
```

#### 引数（Parameters）

`other` [TimeScale](Omni.Units.TimeScale.md)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Units_TimeScale_Equals_Omni_Units_TimeScale_"></a> Equals\(TimeScale\)

```csharp
public bool Equals(TimeScale other)
```

#### 引数（Parameters）

`other` [TimeScale](Omni.Units.TimeScale.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_TimeScale_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object obj)
```

#### 引数（Parameters）

`obj` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_TimeScale_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Units_TimeScale_ToString"></a> ToString\(\)

```csharp
public override string ToString()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Units_TimeScale_TryFromDouble_System_Double_Omni_Units_TimeScale__"></a> TryFromDouble\(double, out TimeScale\)

```csharp
public static bool TryFromDouble(double value, out TimeScale result)
```

#### 引数（Parameters）

`value` [double](https://learn.microsoft.com/dotnet/api/system.double)

`result` [TimeScale](Omni.Units.TimeScale.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_TimeScale_TryParse_System_String_Omni_Units_TimeScale__"></a> TryParse\(string, out TimeScale\)

```csharp
public static bool TryParse(string text, out TimeScale result)
```

#### 引数（Parameters）

`text` [string](https://learn.microsoft.com/dotnet/api/system.string)

`result` [TimeScale](Omni.Units.TimeScale.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_TimeScale_TryToDouble_System_Double__"></a> TryToDouble\(out double\)

```csharp
public bool TryToDouble(out double result)
```

#### 引数（Parameters）

`result` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## 演算子（Operators）

### <a id="Omni_Units_TimeScale_op_Equality_Omni_Units_TimeScale_Omni_Units_TimeScale_"></a> operator ==\(TimeScale, TimeScale\)

```csharp
public static bool operator ==(TimeScale left, TimeScale right)
```

#### 引数（Parameters）

`left` [TimeScale](Omni.Units.TimeScale.md)

`right` [TimeScale](Omni.Units.TimeScale.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_TimeScale_op_GreaterThan_Omni_Units_TimeScale_Omni_Units_TimeScale_"></a> operator \>\(TimeScale, TimeScale\)

```csharp
public static bool operator >(TimeScale left, TimeScale right)
```

#### 引数（Parameters）

`left` [TimeScale](Omni.Units.TimeScale.md)

`right` [TimeScale](Omni.Units.TimeScale.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_TimeScale_op_GreaterThanOrEqual_Omni_Units_TimeScale_Omni_Units_TimeScale_"></a> operator \>=\(TimeScale, TimeScale\)

```csharp
public static bool operator >=(TimeScale left, TimeScale right)
```

#### 引数（Parameters）

`left` [TimeScale](Omni.Units.TimeScale.md)

`right` [TimeScale](Omni.Units.TimeScale.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_TimeScale_op_Inequality_Omni_Units_TimeScale_Omni_Units_TimeScale_"></a> operator \!=\(TimeScale, TimeScale\)

```csharp
public static bool operator !=(TimeScale left, TimeScale right)
```

#### 引数（Parameters）

`left` [TimeScale](Omni.Units.TimeScale.md)

`right` [TimeScale](Omni.Units.TimeScale.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_TimeScale_op_LessThan_Omni_Units_TimeScale_Omni_Units_TimeScale_"></a> operator <\(TimeScale, TimeScale\)

```csharp
public static bool operator <(TimeScale left, TimeScale right)
```

#### 引数（Parameters）

`left` [TimeScale](Omni.Units.TimeScale.md)

`right` [TimeScale](Omni.Units.TimeScale.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_TimeScale_op_LessThanOrEqual_Omni_Units_TimeScale_Omni_Units_TimeScale_"></a> operator <=\(TimeScale, TimeScale\)

```csharp
public static bool operator <=(TimeScale left, TimeScale right)
```

#### 引数（Parameters）

`left` [TimeScale](Omni.Units.TimeScale.md)

`right` [TimeScale](Omni.Units.TimeScale.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
