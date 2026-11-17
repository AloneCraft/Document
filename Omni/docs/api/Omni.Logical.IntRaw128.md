# <a id="Omni_Logical_IntRaw128"></a> Struct IntRaw128

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

符号付き128ビット2の補数整数です（回転成分<xref href="Omni.Logical.RotationScalar" data-throw-if-not-resolved="false"></xref>の生表現）。
64ビットlimbを<xref href="Omni.Logical.IntRaw128.LimbCount" data-throw-if-not-resolved="false"></xref>本並べて格納します。
Limb0が最下位64ビット、最上位limbのbit63が符号ビットです。
演算は<xref href="Omni.Logical.IntRaw" data-throw-if-not-resolved="false"></xref>（<xref href="Omni.Logical.Scalar" data-throw-if-not-resolved="false"></xref>の生表現）を128ビットへ写したもので、
片方を直したらもう片方も直します。除算・平方根・浮動小数点や10進との変換は持たず、
<xref href="Omni.Logical.IntRaw128.Widen" data-throw-if-not-resolved="false"></xref>で<xref href="Omni.Logical.IntRaw" data-throw-if-not-resolved="false"></xref>へ広げてそちらの演算を使い、<xref href="Omni.Logical.IntRaw128.TryNarrow(Omni.Logical.IntRaw%40%2cOmni.Logical.IntRaw128%40)" data-throw-if-not-resolved="false"></xref>で戻します。
Silent Wraparound / Silent Clampは行わず、Overflowが起き得る演算はすべてTry APIです。

```csharp
public readonly struct IntRaw128 : IEquatable<IntRaw128>, IComparable<IntRaw128>
```

#### 実装するインターフェース（Implements）

[IEquatable<IntRaw128\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1), 
[IComparable<IntRaw128\>](https://learn.microsoft.com/dotnet/api/system.icomparable\-1)

## コンストラクター（Constructors）

### <a id="Omni_Logical_IntRaw128__ctor_System_UInt64_System_UInt64_"></a> IntRaw128\(ulong, ulong\)

固定された下位・上位64bitから128bit整数を構築します。

```csharp
public IntRaw128(ulong low, ulong high)
```

#### 引数（Parameters）

`low` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

`high` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Logical_IntRaw128__ctor_System_ReadOnlySpan_System_UInt64__"></a> IntRaw128\(ReadOnlySpan<ulong\>\)

下位limbから順に並んだスパンから構築します。
要素が足りない分はゼロ、余った分は捨てます（呼び出し側の切り詰め忘れで
例外を投げるより、上位ビットの脱落を明示的に扱う各Try APIへ任せます）。

```csharp
public IntRaw128(ReadOnlySpan<ulong> limbs)
```

#### 引数（Parameters）

`limbs` [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[ulong](https://learn.microsoft.com/dotnet/api/system.uint64)\>

## フィールド（Fields）

### <a id="Omni_Logical_IntRaw128_Limb0"></a> Limb0

最下位64ビット（bit0-63）です。

```csharp
public readonly ulong Limb0
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Logical_IntRaw128_Limb1"></a> Limb1

最上位64ビット（bit64-127、bit63が符号ビット）です。

```csharp
public readonly ulong Limb1
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Logical_IntRaw128_LimbCount"></a> LimbCount

64ビットlimbの本数です。

```csharp
public const int LimbCount = 2
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_IntRaw128_MaxValue"></a> MaxValue

表現可能な最大値（2^(TotalBits-1) - 1）です。

```csharp
public static readonly IntRaw128 MaxValue
```

#### 値（Field Value）

 [IntRaw128](Omni.Logical.IntRaw128.md)

### <a id="Omni_Logical_IntRaw128_MinValue"></a> MinValue

表現可能な最小値（-2^(TotalBits-1)）です。

```csharp
public static readonly IntRaw128 MinValue
```

#### 値（Field Value）

 [IntRaw128](Omni.Logical.IntRaw128.md)

### <a id="Omni_Logical_IntRaw128_One"></a> One

1を表す値です。

```csharp
public static readonly IntRaw128 One
```

#### 値（Field Value）

 [IntRaw128](Omni.Logical.IntRaw128.md)

### <a id="Omni_Logical_IntRaw128_TotalBits"></a> TotalBits

総ビット数です。

```csharp
public const int TotalBits = 128
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_IntRaw128_WideBits"></a> WideBits

積の中間値（<xref href="Omni.Logical.WideInt256" data-throw-if-not-resolved="false"></xref>）のビット数です。

```csharp
public const int WideBits = 256
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_IntRaw128_WideLimbCount"></a> WideLimbCount

積の中間値のlimbの本数です。

```csharp
public const int WideLimbCount = 4
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_IntRaw128_Zero"></a> Zero

ゼロ値です。

```csharp
public static readonly IntRaw128 Zero
```

#### 値（Field Value）

 [IntRaw128](Omni.Logical.IntRaw128.md)

## プロパティ（Properties）

### <a id="Omni_Logical_IntRaw128_IsNegative"></a> IsNegative

この値が負であればtrueです。

```csharp
public bool IsNegative { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_IntRaw128_IsZero"></a> IsZero

この値がゼロであればtrueです。

```csharp
public bool IsZero { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_Logical_IntRaw128_CompareTo_Omni_Logical_IntRaw128_"></a> CompareTo\(IntRaw128\)

```csharp
public int CompareTo(IntRaw128 other)
```

#### 引数（Parameters）

`other` [IntRaw128](Omni.Logical.IntRaw128.md)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_IntRaw128_CopyTo_System_Span_System_UInt64__"></a> CopyTo\(Span<ulong\>\)

下位limbから順にスパンへ書き出します。

```csharp
public void CopyTo(Span<ulong> destination)
```

#### 引数（Parameters）

`destination` [Span](https://learn.microsoft.com/dotnet/api/system.span\-1)<[ulong](https://learn.microsoft.com/dotnet/api/system.uint64)\>

### <a id="Omni_Logical_IntRaw128_Equals_Omni_Logical_IntRaw128_"></a> Equals\(IntRaw128\)

```csharp
public bool Equals(IntRaw128 other)
```

#### 引数（Parameters）

`other` [IntRaw128](Omni.Logical.IntRaw128.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_IntRaw128_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object obj)
```

#### 引数（Parameters）

`obj` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_IntRaw128_FromLimbArray_System_UInt64___"></a> FromLimbArray\(ulong\[\]\)

Limb0順のulong配列から復元します。
nullまたは要素数が<xref href="Omni.Logical.IntRaw128.LimbCount" data-throw-if-not-resolved="false"></xref>でない場合はゼロを返します
（破損したシリアライズデータに対する安全側フォールバック）。

<p>
現在の構成と幅が異なる配列は互換変換せずゼロとして扱います。
ここで黙って詰め直すと、異なるrawビット列を現在の構成として
誤解釈した値が正しい値の顔をして通ってしまいます。
</p>

```csharp
public static IntRaw128 FromLimbArray(ulong[] limbs)
```

#### 引数（Parameters）

`limbs` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)\[\]

#### 戻り値（Returns）

 [IntRaw128](Omni.Logical.IntRaw128.md)

### <a id="Omni_Logical_IntRaw128_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_IntRaw128_GetLimb_System_Int32_"></a> GetLimb\(int\)

指定したlimbを返します。範囲外のインデックスはゼロを返します
（シフト演算が範囲外を素の値として読むため）。

```csharp
public ulong GetLimb(int index)
```

#### 引数（Parameters）

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Logical_IntRaw128_ToLimbArray"></a> ToLimbArray\(\)

Limb0から順に<xref href="Omni.Logical.IntRaw128.LimbCount" data-throw-if-not-resolved="false"></xref>要素のulong配列へパックします
（Unity SerializeField用。個別ulongフィールドの代わりに配列でまとめる）。

```csharp
public ulong[] ToLimbArray()
```

#### 戻り値（Returns）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)\[\]

### <a id="Omni_Logical_IntRaw128_TryAdd_Omni_Logical_IntRaw128__Omni_Logical_IntRaw128__Omni_Logical_IntRaw128__"></a> TryAdd\(in IntRaw128, in IntRaw128, out IntRaw128\)

加算を試みます。同符号の加算で結果の符号が反転した場合はオーバーフローです。

```csharp
public static bool TryAdd(in IntRaw128 left, in IntRaw128 right, out IntRaw128 result)
```

#### 引数（Parameters）

`left` [IntRaw128](Omni.Logical.IntRaw128.md)

左辺値。

`right` [IntRaw128](Omni.Logical.IntRaw128.md)

右辺値。

`result` [IntRaw128](Omni.Logical.IntRaw128.md)

加算結果。オーバーフロー時はゼロ。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

オーバーフローしなかった場合はtrue。

### <a id="Omni_Logical_IntRaw128_TryCopyTo_System_UInt64___"></a> TryCopyTo\(ulong\[\]\)

既存のUnityシリアライズ用limb配列へ、このrawビット列を割り当てなしで書き込みます。
配列がnullまたは現行の固定小数点幅と異なる場合は、破損データを部分的に
書き換えないようfalseを返します。

```csharp
public bool TryCopyTo(ulong[] destination)
```

#### 引数（Parameters）

`destination` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)\[\]

書き込み先のLimb0順配列。nullや要素数不一致は受け付けません。
LogicalTransformが実行中に同じ配列を再利用してraw値を保存する用途です。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

全limbを書き込めた場合はtrue。

### <a id="Omni_Logical_IntRaw128_TryNarrow_Omni_Logical_IntRaw__Omni_Logical_IntRaw128__"></a> TryNarrow\(in IntRaw, out IntRaw128\)

<xref href="Omni.Logical.IntRaw" data-throw-if-not-resolved="false"></xref>の値が128ビットの符号付き範囲に収まれば変換します
（上位のlimbがbit127の符号拡張であること）。収まらなければfalseでゼロを返します。

```csharp
public static bool TryNarrow(in IntRaw value, out IntRaw128 result)
```

#### 引数（Parameters）

`value` [IntRaw](Omni.Logical.IntRaw.md)

`result` [IntRaw128](Omni.Logical.IntRaw128.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_IntRaw128_TryNegate_Omni_Logical_IntRaw128__Omni_Logical_IntRaw128__"></a> TryNegate\(in IntRaw128, out IntRaw128\)

符号反転を試みます。MinValue（-2^(TotalBits-1)）の反転は
+2^(TotalBits-1)が表現不可のため失敗します。

```csharp
public static bool TryNegate(in IntRaw128 value, out IntRaw128 result)
```

#### 引数（Parameters）

`value` [IntRaw128](Omni.Logical.IntRaw128.md)

反転する値。

`result` [IntRaw128](Omni.Logical.IntRaw128.md)

反転結果。失敗時はゼロ。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

表現可能な場合はtrue。

### <a id="Omni_Logical_IntRaw128_TrySubtract_Omni_Logical_IntRaw128__Omni_Logical_IntRaw128__Omni_Logical_IntRaw128__"></a> TrySubtract\(in IntRaw128, in IntRaw128, out IntRaw128\)

減算を試みます。左辺と右辺の符号が異なり、かつ結果の符号が左辺と異なる場合はオーバーフローです。

```csharp
public static bool TrySubtract(in IntRaw128 left, in IntRaw128 right, out IntRaw128 result)
```

#### 引数（Parameters）

`left` [IntRaw128](Omni.Logical.IntRaw128.md)

左辺値。

`right` [IntRaw128](Omni.Logical.IntRaw128.md)

右辺値。

`result` [IntRaw128](Omni.Logical.IntRaw128.md)

減算結果。オーバーフロー時はゼロ。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

オーバーフローしなかった場合はtrue。

### <a id="Omni_Logical_IntRaw128_Widen"></a> Widen\(\)

同じ値の<xref href="Omni.Logical.IntRaw" data-throw-if-not-resolved="false"></xref>（<xref href="Omni.Logical.Scalar" data-throw-if-not-resolved="false"></xref>の整数型）へ符号拡張します。

```csharp
public IntRaw Widen()
```

#### 戻り値（Returns）

 [IntRaw](Omni.Logical.IntRaw.md)

## 演算子（Operators）

### <a id="Omni_Logical_IntRaw128_op_Equality_Omni_Logical_IntRaw128_Omni_Logical_IntRaw128_"></a> operator ==\(IntRaw128, IntRaw128\)

2つの値が等しい場合はtrueです。

```csharp
public static bool operator ==(IntRaw128 left, IntRaw128 right)
```

#### 引数（Parameters）

`left` [IntRaw128](Omni.Logical.IntRaw128.md)

`right` [IntRaw128](Omni.Logical.IntRaw128.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_IntRaw128_op_Inequality_Omni_Logical_IntRaw128_Omni_Logical_IntRaw128_"></a> operator \!=\(IntRaw128, IntRaw128\)

2つの値が異なる場合はtrueです。

```csharp
public static bool operator !=(IntRaw128 left, IntRaw128 right)
```

#### 引数（Parameters）

`left` [IntRaw128](Omni.Logical.IntRaw128.md)

`right` [IntRaw128](Omni.Logical.IntRaw128.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
