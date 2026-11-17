# <a id="Omni_Units_GravitationalParameter"></a> Struct GravitationalParameter

Namespace: [Omni.Units](Omni.Units.md)  
Assembly: Radial.Runtime.dll  

重力パラメータμをm³/s²で保持する10進科学表記型です。
桁域はScientific128、軌道演算への変換先はScalar（Q95.96）です。

```csharp
public readonly struct GravitationalParameter : IEquatable<GravitationalParameter>, IComparable<GravitationalParameter>
```

#### 実装するインターフェース（Implements）

[IEquatable<GravitationalParameter\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1), 
[IComparable<GravitationalParameter\>](https://learn.microsoft.com/dotnet/api/system.icomparable\-1)

## プロパティ（Properties）

### <a id="Omni_Units_GravitationalParameter_IsZero"></a> IsZero

```csharp
public bool IsZero { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_Units_GravitationalParameter_CompareTo_Omni_Units_GravitationalParameter_"></a> CompareTo\(GravitationalParameter\)

```csharp
public int CompareTo(GravitationalParameter other)
```

#### 引数（Parameters）

`other` [GravitationalParameter](Omni.Units.GravitationalParameter.md)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Units_GravitationalParameter_Equals_Omni_Units_GravitationalParameter_"></a> Equals\(GravitationalParameter\)

```csharp
public bool Equals(GravitationalParameter other)
```

#### 引数（Parameters）

`other` [GravitationalParameter](Omni.Units.GravitationalParameter.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_GravitationalParameter_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object obj)
```

#### 引数（Parameters）

`obj` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_GravitationalParameter_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Units_GravitationalParameter_ToString"></a> ToString\(\)

```csharp
public override string ToString()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Units_GravitationalParameter_TryFromMetersCubedPerSecondSquared_System_String_Omni_Units_GravitationalParameter__"></a> TryFromMetersCubedPerSecondSquared\(string, out GravitationalParameter\)

```csharp
public static bool TryFromMetersCubedPerSecondSquared(string text, out GravitationalParameter result)
```

#### 引数（Parameters）

`text` [string](https://learn.microsoft.com/dotnet/api/system.string)

`result` [GravitationalParameter](Omni.Units.GravitationalParameter.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_GravitationalParameter_TryToDouble_System_Double__"></a> TryToDouble\(out double\)

```csharp
public bool TryToDouble(out double result)
```

#### 引数（Parameters）

`result` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_GravitationalParameter_TryToLogicalScalar_Omni_Logical_Scalar__"></a> TryToLogicalScalar\(out Scalar\)

```csharp
public bool TryToLogicalScalar(out Scalar result)
```

#### 引数（Parameters）

`result` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## 演算子（Operators）

### <a id="Omni_Units_GravitationalParameter_op_Equality_Omni_Units_GravitationalParameter_Omni_Units_GravitationalParameter_"></a> operator ==\(GravitationalParameter, GravitationalParameter\)

```csharp
public static bool operator ==(GravitationalParameter left, GravitationalParameter right)
```

#### 引数（Parameters）

`left` [GravitationalParameter](Omni.Units.GravitationalParameter.md)

`right` [GravitationalParameter](Omni.Units.GravitationalParameter.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_GravitationalParameter_op_GreaterThan_Omni_Units_GravitationalParameter_Omni_Units_GravitationalParameter_"></a> operator \>\(GravitationalParameter, GravitationalParameter\)

```csharp
public static bool operator >(GravitationalParameter left, GravitationalParameter right)
```

#### 引数（Parameters）

`left` [GravitationalParameter](Omni.Units.GravitationalParameter.md)

`right` [GravitationalParameter](Omni.Units.GravitationalParameter.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_GravitationalParameter_op_Inequality_Omni_Units_GravitationalParameter_Omni_Units_GravitationalParameter_"></a> operator \!=\(GravitationalParameter, GravitationalParameter\)

```csharp
public static bool operator !=(GravitationalParameter left, GravitationalParameter right)
```

#### 引数（Parameters）

`left` [GravitationalParameter](Omni.Units.GravitationalParameter.md)

`right` [GravitationalParameter](Omni.Units.GravitationalParameter.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Units_GravitationalParameter_op_LessThan_Omni_Units_GravitationalParameter_Omni_Units_GravitationalParameter_"></a> operator <\(GravitationalParameter, GravitationalParameter\)

```csharp
public static bool operator <(GravitationalParameter left, GravitationalParameter right)
```

#### 引数（Parameters）

`left` [GravitationalParameter](Omni.Units.GravitationalParameter.md)

`right` [GravitationalParameter](Omni.Units.GravitationalParameter.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
