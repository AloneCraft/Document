# <a id="Omni_Units_Mass"></a> Struct Mass

Namespace: [Omni.Units](Omni.Units.md)  
Assembly: Radial.Runtime.dll  

キログラムをSI正規単位とする非負の質量です。
座標用の固定小数点とは分離し、128-bit係数と10進指数で広い桁域を保持します。

```csharp
public readonly struct Mass : IEquatable<Mass>, IComparable<Mass>
```

#### 実装するインターフェース（Implements）

[IEquatable<Mass\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1), 
[IComparable<Mass\>](https://learn.microsoft.com/dotnet/api/system.icomparable\-1)

## プロパティ（Properties）

### <a id="Omni_Units_Mass_IsZero"></a> IsZero

質量0ならtrueです。

```csharp
public bool IsZero { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Mass_Zero"></a> Zero

質量0です。

```csharp
public static Mass Zero { get; }
```

#### 値（Property Value）

 [Mass](Omni.Units.Mass.md)

## メソッド（Methods）

### <a id="Omni_Units_Mass_CompareTo_Omni_Units_Mass_"></a> CompareTo\(Mass\)

```csharp
public int CompareTo(Mass other)
```

#### 引数（Parameters）

`other` [Mass](Omni.Units.Mass.md)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Units_Mass_Equals_Omni_Units_Mass_"></a> Equals\(Mass\)

```csharp
public bool Equals(Mass other)
```

#### 引数（Parameters）

`other` [Mass](Omni.Units.Mass.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Mass_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object obj)
```

#### 引数（Parameters）

`obj` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Mass_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Units_Mass_ToString"></a> ToString\(\)

キログラム単位の正規化済み10進科学表記を返します。

```csharp
public override string ToString()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Units_Mass_TryFromGrams_System_String_Omni_Units_Mass__"></a> TryFromGrams\(string, out Mass\)

グラム表記を解析し、キログラムへ正規化します。

```csharp
public static bool TryFromGrams(string text, out Mass mass)
```

#### 引数（Parameters）

`text` [string](https://learn.microsoft.com/dotnet/api/system.string)

`mass` [Mass](Omni.Units.Mass.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Mass_TryFromKilograms_System_String_Omni_Units_Mass__"></a> TryFromKilograms\(string, out Mass\)

キログラム表記を解析します。

```csharp
public static bool TryFromKilograms(string text, out Mass mass)
```

#### 引数（Parameters）

`text` [string](https://learn.microsoft.com/dotnet/api/system.string)

`mass` [Mass](Omni.Units.Mass.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## 演算子（Operators）

### <a id="Omni_Units_Mass_op_Equality_Omni_Units_Mass_Omni_Units_Mass_"></a> operator ==\(Mass, Mass\)

```csharp
public static bool operator ==(Mass left, Mass right)
```

#### 引数（Parameters）

`left` [Mass](Omni.Units.Mass.md)

`right` [Mass](Omni.Units.Mass.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Mass_op_GreaterThan_Omni_Units_Mass_Omni_Units_Mass_"></a> operator \>\(Mass, Mass\)

```csharp
public static bool operator >(Mass left, Mass right)
```

#### 引数（Parameters）

`left` [Mass](Omni.Units.Mass.md)

`right` [Mass](Omni.Units.Mass.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Mass_op_GreaterThanOrEqual_Omni_Units_Mass_Omni_Units_Mass_"></a> operator \>=\(Mass, Mass\)

```csharp
public static bool operator >=(Mass left, Mass right)
```

#### 引数（Parameters）

`left` [Mass](Omni.Units.Mass.md)

`right` [Mass](Omni.Units.Mass.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Mass_op_Inequality_Omni_Units_Mass_Omni_Units_Mass_"></a> operator \!=\(Mass, Mass\)

```csharp
public static bool operator !=(Mass left, Mass right)
```

#### 引数（Parameters）

`left` [Mass](Omni.Units.Mass.md)

`right` [Mass](Omni.Units.Mass.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Mass_op_LessThan_Omni_Units_Mass_Omni_Units_Mass_"></a> operator <\(Mass, Mass\)

```csharp
public static bool operator <(Mass left, Mass right)
```

#### 引数（Parameters）

`left` [Mass](Omni.Units.Mass.md)

`right` [Mass](Omni.Units.Mass.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Mass_op_LessThanOrEqual_Omni_Units_Mass_Omni_Units_Mass_"></a> operator <=\(Mass, Mass\)

```csharp
public static bool operator <=(Mass left, Mass right)
```

#### 引数（Parameters）

`left` [Mass](Omni.Units.Mass.md)

`right` [Mass](Omni.Units.Mass.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
