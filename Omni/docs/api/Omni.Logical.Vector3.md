# <a id="Omni_Logical_Vector3"></a> Struct Vector3

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

<xref href="Omni.Logical.Scalar" data-throw-if-not-resolved="false"></xref>を3成分持つ共通数学Vectorです。Omniの論理
Position/Scaleの基礎になります（Position用途の意味の分離は<xref href="Omni.Logical.Position3" data-throw-if-not-resolved="false"></xref>で
行い、Scaleはこの型を直接使います）。

```csharp
public readonly struct Vector3 : IEquatable<Vector3>
```

#### 実装するインターフェース（Implements）

[IEquatable<Vector3\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1)

## コンストラクター（Constructors）

### <a id="Omni_Logical_Vector3__ctor_Omni_Logical_Scalar__Omni_Logical_Scalar__Omni_Logical_Scalar__"></a> Vector3\(in Scalar, in Scalar, in Scalar\)

3つの成分から構築します。

```csharp
public Vector3(in Scalar x, in Scalar y, in Scalar z)
```

#### 引数（Parameters）

`x` [Scalar](Omni.Logical.Scalar.md)

`y` [Scalar](Omni.Logical.Scalar.md)

`z` [Scalar](Omni.Logical.Scalar.md)

## フィールド（Fields）

### <a id="Omni_Logical_Vector3_One"></a> One

各成分が1.0のベクトルです。

```csharp
public static readonly Vector3 One
```

#### 値（Field Value）

 [Vector3](Omni.Logical.Vector3.md)

### <a id="Omni_Logical_Vector3_X"></a> X

X成分です。

```csharp
public readonly Scalar X
```

#### 値（Field Value）

 [Scalar](Omni.Logical.Scalar.md)

### <a id="Omni_Logical_Vector3_Y"></a> Y

Y成分です。

```csharp
public readonly Scalar Y
```

#### 値（Field Value）

 [Scalar](Omni.Logical.Scalar.md)

### <a id="Omni_Logical_Vector3_Z"></a> Z

Z成分です。

```csharp
public readonly Scalar Z
```

#### 値（Field Value）

 [Scalar](Omni.Logical.Scalar.md)

### <a id="Omni_Logical_Vector3_Zero"></a> Zero

ゼロベクトルです。

```csharp
public static readonly Vector3 Zero
```

#### 値（Field Value）

 [Vector3](Omni.Logical.Vector3.md)

## メソッド（Methods）

### <a id="Omni_Logical_Vector3_Equals_Omni_Logical_Vector3_"></a> Equals\(Vector3\)

```csharp
public bool Equals(Vector3 other)
```

#### 引数（Parameters）

`other` [Vector3](Omni.Logical.Vector3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Vector3_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object obj)
```

#### 引数（Parameters）

`obj` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Vector3_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_Vector3_ToString"></a> ToString\(\)

```csharp
public override string ToString()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Logical_Vector3_TryAdd_Omni_Logical_Vector3__Omni_Logical_Vector3__Omni_Logical_Vector3__"></a> TryAdd\(in Vector3, in Vector3, out Vector3\)

加算を試みます。いずれかの成分がオーバーフローすると失敗します。

```csharp
public static bool TryAdd(in Vector3 left, in Vector3 right, out Vector3 result)
```

#### 引数（Parameters）

`left` [Vector3](Omni.Logical.Vector3.md)

`right` [Vector3](Omni.Logical.Vector3.md)

`result` [Vector3](Omni.Logical.Vector3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Vector3_TryCross_Omni_Logical_Vector3__Omni_Logical_Vector3__Omni_Logical_Vector3__"></a> TryCross\(in Vector3, in Vector3, out Vector3\)

外積を試みます。各成分は2項の差（積2つ）で、LogicalWideIntアキュムレータで
合成してから一度だけLogicalScalarへ丸めます（厳密なGram-Schmidt直交化等に使用）。

```csharp
public static bool TryCross(in Vector3 left, in Vector3 right, out Vector3 result)
```

#### 引数（Parameters）

`left` [Vector3](Omni.Logical.Vector3.md)

`right` [Vector3](Omni.Logical.Vector3.md)

`result` [Vector3](Omni.Logical.Vector3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Vector3_TryDot_Omni_Logical_Vector3__Omni_Logical_Vector3__Omni_Logical_Scalar__"></a> TryDot\(in Vector3, in Vector3, out Scalar\)

内積を試みます。3つの積をLogicalWideIntアキュムレータで合成してから
一度だけLogicalScalarへ丸めます（個々の積を先に丸めてから合成する誤差の
蓄積を避けるため。厳密なGram-Schmidt直交化等に使用）。

```csharp
public static bool TryDot(in Vector3 left, in Vector3 right, out Scalar result)
```

#### 引数（Parameters）

`left` [Vector3](Omni.Logical.Vector3.md)

`right` [Vector3](Omni.Logical.Vector3.md)

`result` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Vector3_TryFromFloat3_Unity_Mathematics_float3_Omni_Logical_Vector3__"></a> TryFromFloat3\(float3, out Vector3\)

IEEE 754単精度3成分からの変換を試みます。
各成分の有限ビット列を固定小数点へ無損失で変換します。

```csharp
public static bool TryFromFloat3(float3 value, out Vector3 result)
```

#### 引数（Parameters）

`value` float3

`result` [Vector3](Omni.Logical.Vector3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Vector3_TryLength_Omni_Logical_Vector3__Omni_Logical_Scalar__"></a> TryLength\(in Vector3, out Scalar\)

長さを試みます。最大絶対成分で先に正規化するため、結果が表現可能なら
各成分の2乗がScalar範囲を越える巨大ベクトルでも計算できます。
成分がMinValue（-2^95）のときは、長さが2^95以上で表現できないため失敗します。

```csharp
public static bool TryLength(in Vector3 value, out Scalar result)
```

#### 引数（Parameters）

`value` [Vector3](Omni.Logical.Vector3.md)

`result` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Vector3_TryLerp_Omni_Logical_Vector3__Omni_Logical_Vector3__Omni_Logical_Scalar__Omni_Logical_Vector3__"></a> TryLerp\(in Vector3, in Vector3, in Scalar, out Vector3\)

成分ごとの線形補間を試みます。各成分は<xref href="Omni.Logical.Scalar.TryLerp(Omni.Logical.Scalar%40%2cOmni.Logical.Scalar%40%2cOmni.Logical.Scalar%40%2cOmni.Logical.Scalar%40)" data-throw-if-not-resolved="false"></xref>と
同じく「先に差を取ってから比率を掛ける」順序で計算するため、巨大な絶対座標どうしの
補間でも差分の精度が丸めに埋もれません。
失敗条件も成分ごとの<xref href="Omni.Logical.Scalar.TryLerp(Omni.Logical.Scalar%40%2cOmni.Logical.Scalar%40%2cOmni.Logical.Scalar%40%2cOmni.Logical.Scalar%40)" data-throw-if-not-resolved="false"></xref>と同じで、<code class="paramref">t</code> が0〜1の範囲外のときと、
いずれかの成分で差 <code>to-from</code> が表現範囲を超えるとき（<code>t</code> が0でも1でもなく、その成分の端点が異なる場合）に失敗します。

```csharp
public static bool TryLerp(in Vector3 from, in Vector3 to, in Scalar t, out Vector3 result)
```

#### 引数（Parameters）

`from` [Vector3](Omni.Logical.Vector3.md)

開始値。

`to` [Vector3](Omni.Logical.Vector3.md)

終了値。

`t` [Scalar](Omni.Logical.Scalar.md)

補間比率(0〜1)。範囲外は失敗します。

`result` [Vector3](Omni.Logical.Vector3.md)

補間結果。失敗時はゼロ。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Vector3_TryNegate_Omni_Logical_Vector3__Omni_Logical_Vector3__"></a> TryNegate\(in Vector3, out Vector3\)

符号反転を試みます。いずれかの成分がMinValueだと失敗します。

```csharp
public static bool TryNegate(in Vector3 value, out Vector3 result)
```

#### 引数（Parameters）

`value` [Vector3](Omni.Logical.Vector3.md)

`result` [Vector3](Omni.Logical.Vector3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Vector3_TryNormalize_Omni_Logical_Vector3__Omni_Logical_Vector3__"></a> TryNormalize\(in Vector3, out Vector3\)

単位長へ正規化を試みます。最大絶対成分で先に縮小してから長さで割るため、巨大な成分でも計算できます。
次の場合は失敗します（resultはゼロ）。

<ul><li>全成分がゼロのとき。</li><li>いずれかの成分がMinValue（-2^95）のとき。絶対値が表現できないため、正規化結果が表現できる場合（例: (MinValue, 0, 0) → (-1, 0, 0)）でも失敗します。</li></ul>

```csharp
public static bool TryNormalize(in Vector3 value, out Vector3 result)
```

#### 引数（Parameters）

`value` [Vector3](Omni.Logical.Vector3.md)

`result` [Vector3](Omni.Logical.Vector3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Vector3_TryScale_Omni_Logical_Vector3__Omni_Logical_Scalar__Omni_Logical_Vector3__"></a> TryScale\(in Vector3, in Scalar, out Vector3\)

スカラー倍を試みます。

```csharp
public static bool TryScale(in Vector3 value, in Scalar scalar, out Vector3 result)
```

#### 引数（Parameters）

`value` [Vector3](Omni.Logical.Vector3.md)

`scalar` [Scalar](Omni.Logical.Scalar.md)

`result` [Vector3](Omni.Logical.Vector3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Vector3_TrySqrLength_Omni_Logical_Vector3__Omni_Logical_Scalar__"></a> TrySqrLength\(in Vector3, out Scalar\)

長さの2乗を試みます（<xref href="Omni.Logical.Vector3.TryDot(Omni.Logical.Vector3%40%2cOmni.Logical.Vector3%40%2cOmni.Logical.Scalar%40)" data-throw-if-not-resolved="false"></xref>(value, value)と同じです）。

```csharp
public static bool TrySqrLength(in Vector3 value, out Scalar result)
```

#### 引数（Parameters）

`value` [Vector3](Omni.Logical.Vector3.md)

`result` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Vector3_TrySubtract_Omni_Logical_Vector3__Omni_Logical_Vector3__Omni_Logical_Vector3__"></a> TrySubtract\(in Vector3, in Vector3, out Vector3\)

減算を試みます。いずれかの成分がオーバーフローすると失敗します。

```csharp
public static bool TrySubtract(in Vector3 left, in Vector3 right, out Vector3 result)
```

#### 引数（Parameters）

`left` [Vector3](Omni.Logical.Vector3.md)

`right` [Vector3](Omni.Logical.Vector3.md)

`result` [Vector3](Omni.Logical.Vector3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Vector3_TryToFloat3_Unity_Mathematics_float3__"></a> TryToFloat3\(out float3\)

Unity描画境界向けの単精度3成分への変換を試みます。
いずれかの成分が有限な単精度範囲を超える場合は失敗します。

```csharp
public bool TryToFloat3(out float3 result)
```

#### 引数（Parameters）

`result` float3

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## 演算子（Operators）

### <a id="Omni_Logical_Vector3_op_Equality_Omni_Logical_Vector3_Omni_Logical_Vector3_"></a> operator ==\(Vector3, Vector3\)

2つの値が等しい場合はtrueです。

```csharp
public static bool operator ==(Vector3 left, Vector3 right)
```

#### 引数（Parameters）

`left` [Vector3](Omni.Logical.Vector3.md)

`right` [Vector3](Omni.Logical.Vector3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Vector3_op_Inequality_Omni_Logical_Vector3_Omni_Logical_Vector3_"></a> operator \!=\(Vector3, Vector3\)

2つの値が異なる場合はtrueです。

```csharp
public static bool operator !=(Vector3 left, Vector3 right)
```

#### 引数（Parameters）

`left` [Vector3](Omni.Logical.Vector3.md)

`right` [Vector3](Omni.Logical.Vector3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
