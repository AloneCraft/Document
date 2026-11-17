# <a id="Omni_Units_UnitInterval"></a> Struct UnitInterval

Namespace: [Omni.Units](Omni.Units.md)  
Assembly: Radial.Runtime.dll  

0以上1以下の比率を保持するQ1.126固定小数点値です。

```csharp
public readonly struct UnitInterval : IEquatable<UnitInterval>, IComparable<UnitInterval>
```

#### 実装するインターフェース（Implements）

[IEquatable<UnitInterval\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1), 
[IComparable<UnitInterval\>](https://learn.microsoft.com/dotnet/api/system.icomparable\-1)

## フィールド（Fields）

### <a id="Omni_Units_UnitInterval_FractionalBits"></a> FractionalBits

```csharp
public const int FractionalBits = 126
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Units_UnitInterval_One"></a> One

```csharp
public static readonly UnitInterval One
```

#### 値（Field Value）

 [UnitInterval](Omni.Units.UnitInterval.md)

### <a id="Omni_Units_UnitInterval_Zero"></a> Zero

```csharp
public static readonly UnitInterval Zero
```

#### 値（Field Value）

 [UnitInterval](Omni.Units.UnitInterval.md)

## メソッド（Methods）

### <a id="Omni_Units_UnitInterval_CompareTo_Omni_Units_UnitInterval_"></a> CompareTo\(UnitInterval\)

```csharp
public int CompareTo(UnitInterval other)
```

#### 引数（Parameters）

`other` [UnitInterval](Omni.Units.UnitInterval.md)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Units_UnitInterval_Equals_Omni_Units_UnitInterval_"></a> Equals\(UnitInterval\)

```csharp
public bool Equals(UnitInterval other)
```

#### 引数（Parameters）

`other` [UnitInterval](Omni.Units.UnitInterval.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_UnitInterval_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object obj)
```

#### 引数（Parameters）

`obj` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_UnitInterval_FromQ32_System_UInt32_"></a> FromQ32\(uint\)

```csharp
public static UnitInterval FromQ32(uint value)
```

#### 引数（Parameters）

`value` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

#### 戻り値（Returns）

 [UnitInterval](Omni.Units.UnitInterval.md)

### <a id="Omni_Units_UnitInterval_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Units_UnitInterval_ToString"></a> ToString\(\)

```csharp
public override string ToString()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Units_UnitInterval_TryParse_System_String_Omni_Units_UnitInterval__"></a> TryParse\(string, out UnitInterval\)

```csharp
public static bool TryParse(string text, out UnitInterval result)
```

#### 引数（Parameters）

`text` [string](https://learn.microsoft.com/dotnet/api/system.string)

`result` [UnitInterval](Omni.Units.UnitInterval.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_UnitInterval_TryToDouble_System_Double__"></a> TryToDouble\(out double\)

```csharp
public bool TryToDouble(out double result)
```

#### 引数（Parameters）

`result` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## 演算子（Operators）

### <a id="Omni_Units_UnitInterval_op_Equality_Omni_Units_UnitInterval_Omni_Units_UnitInterval_"></a> operator ==\(UnitInterval, UnitInterval\)

```csharp
public static bool operator ==(UnitInterval left, UnitInterval right)
```

#### 引数（Parameters）

`left` [UnitInterval](Omni.Units.UnitInterval.md)

`right` [UnitInterval](Omni.Units.UnitInterval.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_UnitInterval_op_GreaterThan_Omni_Units_UnitInterval_Omni_Units_UnitInterval_"></a> operator \>\(UnitInterval, UnitInterval\)

```csharp
public static bool operator >(UnitInterval left, UnitInterval right)
```

#### 引数（Parameters）

`left` [UnitInterval](Omni.Units.UnitInterval.md)

`right` [UnitInterval](Omni.Units.UnitInterval.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_UnitInterval_op_GreaterThanOrEqual_Omni_Units_UnitInterval_Omni_Units_UnitInterval_"></a> operator \>=\(UnitInterval, UnitInterval\)

```csharp
public static bool operator >=(UnitInterval left, UnitInterval right)
```

#### 引数（Parameters）

`left` [UnitInterval](Omni.Units.UnitInterval.md)

`right` [UnitInterval](Omni.Units.UnitInterval.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_UnitInterval_op_Inequality_Omni_Units_UnitInterval_Omni_Units_UnitInterval_"></a> operator \!=\(UnitInterval, UnitInterval\)

```csharp
public static bool operator !=(UnitInterval left, UnitInterval right)
```

#### 引数（Parameters）

`left` [UnitInterval](Omni.Units.UnitInterval.md)

`right` [UnitInterval](Omni.Units.UnitInterval.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_UnitInterval_op_LessThan_Omni_Units_UnitInterval_Omni_Units_UnitInterval_"></a> operator <\(UnitInterval, UnitInterval\)

```csharp
public static bool operator <(UnitInterval left, UnitInterval right)
```

#### 引数（Parameters）

`left` [UnitInterval](Omni.Units.UnitInterval.md)

`right` [UnitInterval](Omni.Units.UnitInterval.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_UnitInterval_op_LessThanOrEqual_Omni_Units_UnitInterval_Omni_Units_UnitInterval_"></a> operator <=\(UnitInterval, UnitInterval\)

```csharp
public static bool operator <=(UnitInterval left, UnitInterval right)
```

#### 引数（Parameters）

`left` [UnitInterval](Omni.Units.UnitInterval.md)

`right` [UnitInterval](Omni.Units.UnitInterval.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
