# <a id="Omni_Units_Angle"></a> Struct Angle

Namespace: [Omni.Units](Omni.Units.md)  
Assembly: Radial.Runtime.dll  

1回転を2^64分割した循環角です。0を含み1 turnを含まないQ0.64表現です。

```csharp
public readonly struct Angle : IEquatable<Angle>, IComparable<Angle>
```

#### 実装するインターフェース（Implements）

[IEquatable<Angle\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1), 
[IComparable<Angle\>](https://learn.microsoft.com/dotnet/api/system.icomparable\-1)

## フィールド（Fields）

### <a id="Omni_Units_Angle_Zero"></a> Zero

```csharp
public static readonly Angle Zero
```

#### 値（Field Value）

 [Angle](Omni.Units.Angle.md)

## プロパティ（Properties）

### <a id="Omni_Units_Angle_RawTurns"></a> RawTurns

```csharp
public ulong RawTurns { get; }
```

#### 値（Property Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

## メソッド（Methods）

### <a id="Omni_Units_Angle_Add_Omni_Units_Angle__Omni_Units_Angle__"></a> Add\(in Angle, in Angle\)

```csharp
public static Angle Add(in Angle left, in Angle right)
```

#### 引数（Parameters）

`left` [Angle](Omni.Units.Angle.md)

`right` [Angle](Omni.Units.Angle.md)

#### 戻り値（Returns）

 [Angle](Omni.Units.Angle.md)

### <a id="Omni_Units_Angle_CompareTo_Omni_Units_Angle_"></a> CompareTo\(Angle\)

```csharp
public int CompareTo(Angle other)
```

#### 引数（Parameters）

`other` [Angle](Omni.Units.Angle.md)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Units_Angle_Equals_Omni_Units_Angle_"></a> Equals\(Angle\)

```csharp
public bool Equals(Angle other)
```

#### 引数（Parameters）

`other` [Angle](Omni.Units.Angle.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Angle_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object obj)
```

#### 引数（Parameters）

`obj` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Angle_FromSector_System_Int32_System_UInt32_System_Int32_"></a> FromSector\(int, uint, int\)

```csharp
public static Angle FromSector(int sectorIndex, uint phaseWithinSectorQ32, int sectorCount)
```

#### 引数（Parameters）

`sectorIndex` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`phaseWithinSectorQ32` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`sectorCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [Angle](Omni.Units.Angle.md)

### <a id="Omni_Units_Angle_GetCellIndex_System_Int32_"></a> GetCellIndex\(int\)

```csharp
public int GetCellIndex(int cellCount)
```

#### 引数（Parameters）

`cellCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Units_Angle_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Units_Angle_ToRadians"></a> ToRadians\(\)

```csharp
public double ToRadians()
```

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Units_Angle_ToString"></a> ToString\(\)

```csharp
public override string ToString()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Units_Angle_ToTurns"></a> ToTurns\(\)

```csharp
public double ToTurns()
```

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Units_Angle_TrySinCos_Omni_Logical_Scalar__Omni_Logical_Scalar__"></a> TrySinCos\(out Scalar, out Scalar\)

CORDIC整数演算だけでsin/cosをScalar（Q95.96）へ評価します。
浮動小数点は使用しません。

```csharp
public bool TrySinCos(out Scalar sine, out Scalar cosine)
```

#### 引数（Parameters）

`sine` [Scalar](Omni.Logical.Scalar.md)

`cosine` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## 演算子（Operators）

### <a id="Omni_Units_Angle_op_Equality_Omni_Units_Angle_Omni_Units_Angle_"></a> operator ==\(Angle, Angle\)

```csharp
public static bool operator ==(Angle left, Angle right)
```

#### 引数（Parameters）

`left` [Angle](Omni.Units.Angle.md)

`right` [Angle](Omni.Units.Angle.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Angle_op_GreaterThan_Omni_Units_Angle_Omni_Units_Angle_"></a> operator \>\(Angle, Angle\)

```csharp
public static bool operator >(Angle left, Angle right)
```

#### 引数（Parameters）

`left` [Angle](Omni.Units.Angle.md)

`right` [Angle](Omni.Units.Angle.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Angle_op_GreaterThanOrEqual_Omni_Units_Angle_Omni_Units_Angle_"></a> operator \>=\(Angle, Angle\)

```csharp
public static bool operator >=(Angle left, Angle right)
```

#### 引数（Parameters）

`left` [Angle](Omni.Units.Angle.md)

`right` [Angle](Omni.Units.Angle.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Angle_op_Inequality_Omni_Units_Angle_Omni_Units_Angle_"></a> operator \!=\(Angle, Angle\)

```csharp
public static bool operator !=(Angle left, Angle right)
```

#### 引数（Parameters）

`left` [Angle](Omni.Units.Angle.md)

`right` [Angle](Omni.Units.Angle.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Angle_op_LessThan_Omni_Units_Angle_Omni_Units_Angle_"></a> operator <\(Angle, Angle\)

```csharp
public static bool operator <(Angle left, Angle right)
```

#### 引数（Parameters）

`left` [Angle](Omni.Units.Angle.md)

`right` [Angle](Omni.Units.Angle.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Angle_op_LessThanOrEqual_Omni_Units_Angle_Omni_Units_Angle_"></a> operator <=\(Angle, Angle\)

```csharp
public static bool operator <=(Angle left, Angle right)
```

#### 引数（Parameters）

`left` [Angle](Omni.Units.Angle.md)

`right` [Angle](Omni.Units.Angle.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
