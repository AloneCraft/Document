# <a id="Omni_Logical_Matrix3x3"></a> Struct Matrix3x3

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

9つの<xref href="Omni.Logical.Scalar" data-throw-if-not-resolved="false"></xref>で構成される高精度3x3行列です。論理親子合成の
World Basisキャッシュ（回転・非一様Scale・Shearを含み得る合成済み行列）として使います。
行列×ベクトル・行列×行列の各成分は、LogicalWideIntアキュムレータで複数項を合成してから
一度だけ丸めます（個々の積を先に丸めてから合成する誤差の蓄積を避けるため）。

```csharp
public readonly struct Matrix3x3 : IEquatable<Matrix3x3>
```

#### 実装するインターフェース（Implements）

[IEquatable<Matrix3x3\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1)

## コンストラクター（Constructors）

### <a id="Omni_Logical_Matrix3x3__ctor_Omni_Logical_Scalar__Omni_Logical_Scalar__Omni_Logical_Scalar__Omni_Logical_Scalar__Omni_Logical_Scalar__Omni_Logical_Scalar__Omni_Logical_Scalar__Omni_Logical_Scalar__Omni_Logical_Scalar__"></a> Matrix3x3\(in Scalar, in Scalar, in Scalar, in Scalar, in Scalar, in Scalar, in Scalar, in Scalar, in Scalar\)

9つの成分（行優先）から構築します。

```csharp
public Matrix3x3(in Scalar m00, in Scalar m01, in Scalar m02, in Scalar m10, in Scalar m11, in Scalar m12, in Scalar m20, in Scalar m21, in Scalar m22)
```

#### 引数（Parameters）

`m00` [Scalar](Omni.Logical.Scalar.md)

`m01` [Scalar](Omni.Logical.Scalar.md)

`m02` [Scalar](Omni.Logical.Scalar.md)

`m10` [Scalar](Omni.Logical.Scalar.md)

`m11` [Scalar](Omni.Logical.Scalar.md)

`m12` [Scalar](Omni.Logical.Scalar.md)

`m20` [Scalar](Omni.Logical.Scalar.md)

`m21` [Scalar](Omni.Logical.Scalar.md)

`m22` [Scalar](Omni.Logical.Scalar.md)

## フィールド（Fields）

### <a id="Omni_Logical_Matrix3x3_Identity"></a> Identity

単位行列です。

```csharp
public static readonly Matrix3x3 Identity
```

#### 値（Field Value）

 [Matrix3x3](Omni.Logical.Matrix3x3.md)

### <a id="Omni_Logical_Matrix3x3_M00"></a> M00

1行1列目です。

```csharp
public readonly Scalar M00
```

#### 値（Field Value）

 [Scalar](Omni.Logical.Scalar.md)

### <a id="Omni_Logical_Matrix3x3_M01"></a> M01

1行2列目です。

```csharp
public readonly Scalar M01
```

#### 値（Field Value）

 [Scalar](Omni.Logical.Scalar.md)

### <a id="Omni_Logical_Matrix3x3_M02"></a> M02

1行3列目です。

```csharp
public readonly Scalar M02
```

#### 値（Field Value）

 [Scalar](Omni.Logical.Scalar.md)

### <a id="Omni_Logical_Matrix3x3_M10"></a> M10

2行1列目です。

```csharp
public readonly Scalar M10
```

#### 値（Field Value）

 [Scalar](Omni.Logical.Scalar.md)

### <a id="Omni_Logical_Matrix3x3_M11"></a> M11

2行2列目です。

```csharp
public readonly Scalar M11
```

#### 値（Field Value）

 [Scalar](Omni.Logical.Scalar.md)

### <a id="Omni_Logical_Matrix3x3_M12"></a> M12

2行3列目です。

```csharp
public readonly Scalar M12
```

#### 値（Field Value）

 [Scalar](Omni.Logical.Scalar.md)

### <a id="Omni_Logical_Matrix3x3_M20"></a> M20

3行1列目です。

```csharp
public readonly Scalar M20
```

#### 値（Field Value）

 [Scalar](Omni.Logical.Scalar.md)

### <a id="Omni_Logical_Matrix3x3_M21"></a> M21

3行2列目です。

```csharp
public readonly Scalar M21
```

#### 値（Field Value）

 [Scalar](Omni.Logical.Scalar.md)

### <a id="Omni_Logical_Matrix3x3_M22"></a> M22

3行3列目です。

```csharp
public readonly Scalar M22
```

#### 値（Field Value）

 [Scalar](Omni.Logical.Scalar.md)

## メソッド（Methods）

### <a id="Omni_Logical_Matrix3x3_Equals_Omni_Logical_Matrix3x3_"></a> Equals\(Matrix3x3\)

```csharp
public bool Equals(Matrix3x3 other)
```

#### 引数（Parameters）

`other` [Matrix3x3](Omni.Logical.Matrix3x3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Matrix3x3_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object obj)
```

#### 引数（Parameters）

`obj` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Matrix3x3_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_Matrix3x3_TryInverse_Omni_Logical_Matrix3x3__"></a> TryInverse\(out Matrix3x3\)

逆行列をアジュゲート行列(余因子行列の転置)/行列式で試みます。
行列式がゼロ（特異行列）、または途中のオーバーフロー時は失敗します。
負のScale（行列式が負）やShear（非対角成分）は一般の余因子展開でそのまま
正しく扱われ、特別扱いを必要としません。

```csharp
public bool TryInverse(out Matrix3x3 result)
```

#### 引数（Parameters）

`result` [Matrix3x3](Omni.Logical.Matrix3x3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Matrix3x3_TryMultiply_Omni_Logical_Matrix3x3__Omni_Logical_Matrix3x3__Omni_Logical_Matrix3x3__"></a> TryMultiply\(in Matrix3x3, in Matrix3x3, out Matrix3x3\)

行列同士の積（left * right）を試みます。

```csharp
public static bool TryMultiply(in Matrix3x3 left, in Matrix3x3 right, out Matrix3x3 result)
```

#### 引数（Parameters）

`left` [Matrix3x3](Omni.Logical.Matrix3x3.md)

`right` [Matrix3x3](Omni.Logical.Matrix3x3.md)

`result` [Matrix3x3](Omni.Logical.Matrix3x3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Matrix3x3_TryMultiplyVector_Omni_Logical_Matrix3x3__Omni_Logical_Vector3__Omni_Logical_Vector3__"></a> TryMultiplyVector\(in Matrix3x3, in Vector3, out Vector3\)

行列とベクトルの積（matrix * vector）を試みます。

```csharp
public static bool TryMultiplyVector(in Matrix3x3 matrix, in Vector3 vector, out Vector3 result)
```

#### 引数（Parameters）

`matrix` [Matrix3x3](Omni.Logical.Matrix3x3.md)

`vector` [Vector3](Omni.Logical.Vector3.md)

`result` [Vector3](Omni.Logical.Vector3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## 演算子（Operators）

### <a id="Omni_Logical_Matrix3x3_op_Equality_Omni_Logical_Matrix3x3_Omni_Logical_Matrix3x3_"></a> operator ==\(Matrix3x3, Matrix3x3\)

2つの値が等しい場合はtrueです。

```csharp
public static bool operator ==(Matrix3x3 left, Matrix3x3 right)
```

#### 引数（Parameters）

`left` [Matrix3x3](Omni.Logical.Matrix3x3.md)

`right` [Matrix3x3](Omni.Logical.Matrix3x3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Matrix3x3_op_Inequality_Omni_Logical_Matrix3x3_Omni_Logical_Matrix3x3_"></a> operator \!=\(Matrix3x3, Matrix3x3\)

2つの値が異なる場合はtrueです。

```csharp
public static bool operator !=(Matrix3x3 left, Matrix3x3 right)
```

#### 引数（Parameters）

`left` [Matrix3x3](Omni.Logical.Matrix3x3.md)

`right` [Matrix3x3](Omni.Logical.Matrix3x3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
