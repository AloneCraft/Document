# <a id="Omni_Logical_WideInt256"></a> Struct WideInt256

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

符号付き256ビット2の補数整数です（回転成分<xref href="Omni.Logical.IntRaw128" data-throw-if-not-resolved="false"></xref>同士の積の中間値）。
<xref href="Omni.Logical.WideInt" data-throw-if-not-resolved="false"></xref>を256ビットへ写したもので、片方を直したらもう片方も直します。
64ビットlimbを<xref href="Omni.Logical.IntRaw128.WideLimbCount" data-throw-if-not-resolved="false"></xref>本並べて格納します。
Scale系の乗算・Quaternion合成で使う中間Accumulatorです
（<xref href="Omni.Logical.IntRaw128" data-throw-if-not-resolved="false"></xref>同士の積は最大でも 2*TotalBits-1 ビットで厳密に表現できるため、
倍幅は単一の積に加えて複数項の合成にも十分なheadroomを持ちます）。
Silent Wraparound / Silent Clampは行わず、Overflowが起き得る演算はすべてTry APIです。

```csharp
public readonly struct WideInt256 : IEquatable<WideInt256>
```

#### 実装するインターフェース（Implements）

[IEquatable<WideInt256\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1)

## コンストラクター（Constructors）

### <a id="Omni_Logical_WideInt256__ctor_System_ReadOnlySpan_System_UInt64__"></a> WideInt256\(ReadOnlySpan<ulong\>\)

下位limbから順に並んだスパンから構築します。
要素が足りない分はゼロ、余った分は捨てます（呼び出し側の切り詰め忘れで
例外を投げるより、上位ビットの脱落を明示的に扱う各Try APIへ任せます）。

```csharp
public WideInt256(ReadOnlySpan<ulong> limbs)
```

#### 引数（Parameters）

`limbs` [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[ulong](https://learn.microsoft.com/dotnet/api/system.uint64)\>

## フィールド（Fields）

### <a id="Omni_Logical_WideInt256_MinValue"></a> MinValue

表現可能な最小値（-2^(WideBits-1)）です。

```csharp
public static readonly WideInt256 MinValue
```

#### 値（Field Value）

 [WideInt256](Omni.Logical.WideInt256.md)

### <a id="Omni_Logical_WideInt256_WLimb0"></a> WLimb0

最下位64ビット（bit0-63）です。

```csharp
public readonly ulong WLimb0
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Logical_WideInt256_WLimb1"></a> WLimb1

bit64-127です。

```csharp
public readonly ulong WLimb1
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Logical_WideInt256_WLimb2"></a> WLimb2

bit128-191です。

```csharp
public readonly ulong WLimb2
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Logical_WideInt256_WLimb3"></a> WLimb3

最上位64ビット（bit192-255、bit63が符号ビット）です。

```csharp
public readonly ulong WLimb3
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Logical_WideInt256_Zero"></a> Zero

ゼロ値です。

```csharp
public static readonly WideInt256 Zero
```

#### 値（Field Value）

 [WideInt256](Omni.Logical.WideInt256.md)

## プロパティ（Properties）

### <a id="Omni_Logical_WideInt256_IsNegative"></a> IsNegative

この値が負であればtrueです。

```csharp
public bool IsNegative { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_Logical_WideInt256_Equals_Omni_Logical_WideInt256_"></a> Equals\(WideInt256\)

```csharp
public bool Equals(WideInt256 other)
```

#### 引数（Parameters）

`other` [WideInt256](Omni.Logical.WideInt256.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_WideInt256_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object obj)
```

#### 引数（Parameters）

`obj` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_WideInt256_FromSignedProduct_Omni_Logical_IntRaw128__Omni_Logical_IntRaw128__"></a> FromSignedProduct\(in IntRaw128, in IntRaw128\)

符号付き<xref href="Omni.Logical.IntRaw128.TotalBits" data-throw-if-not-resolved="false"></xref>ビット同士の積を厳密な倍幅結果として計算します。
TotalBits × TotalBits の符号付き積は必ず倍幅に収まるため、
このメソッドはオーバーフローしません（Try接頭辞なし）。

```csharp
public static WideInt256 FromSignedProduct(in IntRaw128 left, in IntRaw128 right)
```

#### 引数（Parameters）

`left` [IntRaw128](Omni.Logical.IntRaw128.md)

左辺値。

`right` [IntRaw128](Omni.Logical.IntRaw128.md)

右辺値。

#### 戻り値（Returns）

 [WideInt256](Omni.Logical.WideInt256.md)

厳密な積。

### <a id="Omni_Logical_WideInt256_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_WideInt256_GetLimb_System_Int32_"></a> GetLimb\(int\)

指定したlimbを返します。範囲外のインデックスはゼロを返します
（シフト演算が範囲外を素の値として読むため）。

```csharp
public ulong GetLimb(int index)
```

#### 引数（Parameters）

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Logical_WideInt256_TryAdd_Omni_Logical_WideInt256__Omni_Logical_WideInt256__Omni_Logical_WideInt256__"></a> TryAdd\(in WideInt256, in WideInt256, out WideInt256\)

加算を試みます。

```csharp
public static bool TryAdd(in WideInt256 left, in WideInt256 right, out WideInt256 result)
```

#### 引数（Parameters）

`left` [WideInt256](Omni.Logical.WideInt256.md)

`right` [WideInt256](Omni.Logical.WideInt256.md)

`result` [WideInt256](Omni.Logical.WideInt256.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_WideInt256_TryNegate_Omni_Logical_WideInt256__Omni_Logical_WideInt256__"></a> TryNegate\(in WideInt256, out WideInt256\)

符号反転を試みます。MinValue（-2^(WideBits-1)）の反転は失敗します。

```csharp
public static bool TryNegate(in WideInt256 value, out WideInt256 result)
```

#### 引数（Parameters）

`value` [WideInt256](Omni.Logical.WideInt256.md)

`result` [WideInt256](Omni.Logical.WideInt256.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_WideInt256_TryRoundToScaleInt_Omni_Logical_WideInt256__System_Int32_Omni_Logical_IntRaw128__"></a> TryRoundToScaleInt\(in WideInt256, int, out IntRaw128\)

このWide値を最近接偶数丸めで<code class="paramref">fractionalBitsToRemove</code>ビット右へ丸め、
<xref href="Omni.Logical.IntRaw128.TotalBits" data-throw-if-not-resolved="false"></xref>ビット符号付き整数へ収めます。
丸め対象の絶対値に対して丸めを行い符号を再適用するため、
2の補数の直接算術シフトによる負方向バイアスを避けます。結果が
TotalBitsビット符号付き範囲を超える場合は失敗します。

```csharp
public static bool TryRoundToScaleInt(in WideInt256 value, int fractionalBitsToRemove, out IntRaw128 result)
```

#### 引数（Parameters）

`value` [WideInt256](Omni.Logical.WideInt256.md)

丸める対象のWide値。

`fractionalBitsToRemove` [int](https://learn.microsoft.com/dotnet/api/system.int32)

切り捨てる下位ビット数（0以上）。

`result` [IntRaw128](Omni.Logical.IntRaw128.md)

丸め結果。失敗時はゼロ。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

TotalBitsビット符号付き範囲に収まる場合はtrue。

### <a id="Omni_Logical_WideInt256_TrySubtract_Omni_Logical_WideInt256__Omni_Logical_WideInt256__Omni_Logical_WideInt256__"></a> TrySubtract\(in WideInt256, in WideInt256, out WideInt256\)

減算を試みます。

```csharp
public static bool TrySubtract(in WideInt256 left, in WideInt256 right, out WideInt256 result)
```

#### 引数（Parameters）

`left` [WideInt256](Omni.Logical.WideInt256.md)

`right` [WideInt256](Omni.Logical.WideInt256.md)

`result` [WideInt256](Omni.Logical.WideInt256.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## 演算子（Operators）

### <a id="Omni_Logical_WideInt256_op_Equality_Omni_Logical_WideInt256_Omni_Logical_WideInt256_"></a> operator ==\(WideInt256, WideInt256\)

2つの値が等しい場合はtrueです。

```csharp
public static bool operator ==(WideInt256 left, WideInt256 right)
```

#### 引数（Parameters）

`left` [WideInt256](Omni.Logical.WideInt256.md)

`right` [WideInt256](Omni.Logical.WideInt256.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_WideInt256_op_Inequality_Omni_Logical_WideInt256_Omni_Logical_WideInt256_"></a> operator \!=\(WideInt256, WideInt256\)

2つの値が異なる場合はtrueです。

```csharp
public static bool operator !=(WideInt256 left, WideInt256 right)
```

#### 引数（Parameters）

`left` [WideInt256](Omni.Logical.WideInt256.md)

`right` [WideInt256](Omni.Logical.WideInt256.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
