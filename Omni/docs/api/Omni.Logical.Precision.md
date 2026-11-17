# <a id="Omni_Logical_Precision"></a> Class Precision

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

```csharp
[MovedFrom(true, "Omni.Core", null, "LogicalPrecision")]
public static class Precision
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[Precision](Omni.Logical.Precision.md)

## フィールド（Fields）

### <a id="Omni_Logical_Precision_FractionalBits"></a> FractionalBits

```csharp
public const int FractionalBits = 96
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_Precision_IntegerBits"></a> IntegerBits

```csharp
public const int IntegerBits = 95
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_Precision_LimbCount"></a> LimbCount

```csharp
public const int LimbCount = 3
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_Precision_RotationFractionalBits"></a> RotationFractionalBits

```csharp
public const int RotationFractionalBits = 126
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_Precision_TotalBits"></a> TotalBits

```csharp
public const int TotalBits = 192
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_Precision_WideBits"></a> WideBits

```csharp
public const int WideBits = 384
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_Precision_WideLimbCount"></a> WideLimbCount

```csharp
public const int WideLimbCount = 6
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="Omni_Logical_Precision_CurrentResolution"></a> CurrentResolution

論理座標の最小正値（2^-96）です。

```csharp
public static Scalar CurrentResolution { get; }
```

#### 値（Property Value）

 [Scalar](Omni.Logical.Scalar.md)

## メソッド（Methods）

### <a id="Omni_Logical_Precision_TryGetPowerOfTwoExponent_Omni_Logical_Scalar__System_Int32__"></a> TryGetPowerOfTwoExponent\(in Scalar, out int\)

正のLogical値が厳密な2の冪なら、その2進指数を返します。

```csharp
public static bool TryGetPowerOfTwoExponent(in Scalar value, out int binaryExponent)
```

#### 引数（Parameters）

`value` [Scalar](Omni.Logical.Scalar.md)

`binaryExponent` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
