# <a id="Omni_Units_Energy"></a> Struct Energy

Namespace: [Omni.Units](Omni.Units.md)  
Assembly: Radial.Runtime.dll  

ジュールをSI正規単位とする非負のエネルギーです。
光子、電子ボルト、質量エネルギー、宇宙規模の総エネルギーを同じ型で扱います。

```csharp
public readonly struct Energy : IEquatable<Energy>, IComparable<Energy>
```

#### 実装するインターフェース（Implements）

[IEquatable<Energy\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1), 
[IComparable<Energy\>](https://learn.microsoft.com/dotnet/api/system.icomparable\-1)

## プロパティ（Properties）

### <a id="Omni_Units_Energy_IsZero"></a> IsZero

エネルギー0ならtrueです。

```csharp
public bool IsZero { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Energy_Zero"></a> Zero

エネルギー0です。

```csharp
public static Energy Zero { get; }
```

#### 値（Property Value）

 [Energy](Omni.Units.Energy.md)

## メソッド（Methods）

### <a id="Omni_Units_Energy_CompareTo_Omni_Units_Energy_"></a> CompareTo\(Energy\)

```csharp
public int CompareTo(Energy other)
```

#### 引数（Parameters）

`other` [Energy](Omni.Units.Energy.md)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Units_Energy_Equals_Omni_Units_Energy_"></a> Equals\(Energy\)

```csharp
public bool Equals(Energy other)
```

#### 引数（Parameters）

`other` [Energy](Omni.Units.Energy.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Energy_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object obj)
```

#### 引数（Parameters）

`obj` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Energy_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Units_Energy_ToString"></a> ToString\(\)

ジュール単位の正規化済み10進科学表記を返します。

```csharp
public override string ToString()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Units_Energy_TryFromElectronVolts_System_String_Omni_Units_Energy__"></a> TryFromElectronVolts\(string, out Energy\)

電子ボルト表記を解析し、ジュールへ正確に変換します。

```csharp
public static bool TryFromElectronVolts(string text, out Energy energy)
```

#### 引数（Parameters）

`text` [string](https://learn.microsoft.com/dotnet/api/system.string)

`energy` [Energy](Omni.Units.Energy.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Energy_TryFromJoules_System_String_Omni_Units_Energy__"></a> TryFromJoules\(string, out Energy\)

ジュール表記を解析します。

```csharp
public static bool TryFromJoules(string text, out Energy energy)
```

#### 引数（Parameters）

`text` [string](https://learn.microsoft.com/dotnet/api/system.string)

`energy` [Energy](Omni.Units.Energy.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Energy_TryFromMegaElectronVolts_System_String_Omni_Units_Energy__"></a> TryFromMegaElectronVolts\(string, out Energy\)

メガ電子ボルト表記を解析し、ジュールへ正確に変換します。

```csharp
public static bool TryFromMegaElectronVolts(string text, out Energy energy)
```

#### 引数（Parameters）

`text` [string](https://learn.microsoft.com/dotnet/api/system.string)

`energy` [Energy](Omni.Units.Energy.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Energy_TryFromPairAnnihilation_Omni_Units_Mass_Omni_Units_Energy__"></a> TryFromPairAnnihilation\(Mass, out Energy\)

粒子と反粒子が同じ質量を持つ場合の完全対消滅エネルギー2mc²を返します。

```csharp
public static bool TryFromPairAnnihilation(Mass particleMass, out Energy energy)
```

#### 引数（Parameters）

`particleMass` [Mass](Omni.Units.Mass.md)

`energy` [Energy](Omni.Units.Energy.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Energy_TryFromPhotonFrequencyHertz_System_String_Omni_Units_Energy__"></a> TryFromPhotonFrequencyHertz\(string, out Energy\)

E=hνにより、周波数Hzから単一光子のエネルギーを返します。

```csharp
public static bool TryFromPhotonFrequencyHertz(string text, out Energy energy)
```

#### 引数（Parameters）

`text` [string](https://learn.microsoft.com/dotnet/api/system.string)

`energy` [Energy](Omni.Units.Energy.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Energy_TryFromRestMass_Omni_Units_Mass_Omni_Units_Energy__"></a> TryFromRestMass\(Mass, out Energy\)

E=mc²により、静止質量をジュールへ変換します。

```csharp
public static bool TryFromRestMass(Mass mass, out Energy energy)
```

#### 引数（Parameters）

`mass` [Mass](Omni.Units.Mass.md)

`energy` [Energy](Omni.Units.Energy.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## 演算子（Operators）

### <a id="Omni_Units_Energy_op_Equality_Omni_Units_Energy_Omni_Units_Energy_"></a> operator ==\(Energy, Energy\)

```csharp
public static bool operator ==(Energy left, Energy right)
```

#### 引数（Parameters）

`left` [Energy](Omni.Units.Energy.md)

`right` [Energy](Omni.Units.Energy.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Energy_op_GreaterThan_Omni_Units_Energy_Omni_Units_Energy_"></a> operator \>\(Energy, Energy\)

```csharp
public static bool operator >(Energy left, Energy right)
```

#### 引数（Parameters）

`left` [Energy](Omni.Units.Energy.md)

`right` [Energy](Omni.Units.Energy.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Energy_op_GreaterThanOrEqual_Omni_Units_Energy_Omni_Units_Energy_"></a> operator \>=\(Energy, Energy\)

```csharp
public static bool operator >=(Energy left, Energy right)
```

#### 引数（Parameters）

`left` [Energy](Omni.Units.Energy.md)

`right` [Energy](Omni.Units.Energy.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Energy_op_Inequality_Omni_Units_Energy_Omni_Units_Energy_"></a> operator \!=\(Energy, Energy\)

```csharp
public static bool operator !=(Energy left, Energy right)
```

#### 引数（Parameters）

`left` [Energy](Omni.Units.Energy.md)

`right` [Energy](Omni.Units.Energy.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Energy_op_LessThan_Omni_Units_Energy_Omni_Units_Energy_"></a> operator <\(Energy, Energy\)

```csharp
public static bool operator <(Energy left, Energy right)
```

#### 引数（Parameters）

`left` [Energy](Omni.Units.Energy.md)

`right` [Energy](Omni.Units.Energy.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_Energy_op_LessThanOrEqual_Omni_Units_Energy_Omni_Units_Energy_"></a> operator <=\(Energy, Energy\)

```csharp
public static bool operator <=(Energy left, Energy right)
```

#### 引数（Parameters）

`left` [Energy](Omni.Units.Energy.md)

`right` [Energy](Omni.Units.Energy.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
