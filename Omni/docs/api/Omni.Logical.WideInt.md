# <a id="Omni_Logical_WideInt"></a> Struct WideInt

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

符号付き<xref href="Omni.Logical.Precision.WideBits" data-throw-if-not-resolved="false"></xref>ビット2の補数整数です。
64ビットlimbを<xref href="Omni.Logical.Precision.WideLimbCount" data-throw-if-not-resolved="false"></xref>本並べて格納します。
Scale系の乗算・Quaternion合成で使う中間Accumulatorです
（<xref href="Omni.Logical.IntRaw" data-throw-if-not-resolved="false"></xref>同士の積は最大でも 2*TotalBits-1 ビットで厳密に表現できるため、
倍幅は単一の積に加えて複数項の合成にも十分なheadroomを持ちます）。
Silent Wraparound / Silent Clampは行わず、Overflowが起き得る演算はすべてTry APIです。

```csharp
public readonly struct WideInt : IEquatable<WideInt>
```

#### 実装するインターフェース（Implements）

[IEquatable<WideInt\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1)

## コンストラクター（Constructors）

### <a id="Omni_Logical_WideInt__ctor_System_ReadOnlySpan_System_UInt64__"></a> WideInt\(ReadOnlySpan<ulong\>\)

下位limbから順に並んだスパンから構築します。
要素が足りない分はゼロ、余った分は捨てます（呼び出し側の切り詰め忘れで
例外を投げるより、上位ビットの脱落を明示的に扱う各Try APIへ任せます）。

```csharp
public WideInt(ReadOnlySpan<ulong> limbs)
```

#### 引数（Parameters）

`limbs` [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[ulong](https://learn.microsoft.com/dotnet/api/system.uint64)\>

## フィールド（Fields）

### <a id="Omni_Logical_WideInt_MinValue"></a> MinValue

表現可能な最小値（-2^(WideBits-1)）です。

```csharp
public static readonly WideInt MinValue
```

#### 値（Field Value）

 [WideInt](Omni.Logical.WideInt.md)

### <a id="Omni_Logical_WideInt_WLimb0"></a> WLimb0

最下位64ビット（bit0-63）です。

```csharp
public readonly ulong WLimb0
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Logical_WideInt_WLimb1"></a> WLimb1

bit64-127です。

```csharp
public readonly ulong WLimb1
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Logical_WideInt_WLimb2"></a> WLimb2

bit128-191です。

```csharp
public readonly ulong WLimb2
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Logical_WideInt_WLimb3"></a> WLimb3

bit192-255です。

```csharp
public readonly ulong WLimb3
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Logical_WideInt_WLimb4"></a> WLimb4

bit256-319です。

```csharp
public readonly ulong WLimb4
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Logical_WideInt_WLimb5"></a> WLimb5

最上位64ビット（bit320-383、bit63が符号ビット）です。

```csharp
public readonly ulong WLimb5
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Logical_WideInt_Zero"></a> Zero

ゼロ値です。

```csharp
public static readonly WideInt Zero
```

#### 値（Field Value）

 [WideInt](Omni.Logical.WideInt.md)

## プロパティ（Properties）

### <a id="Omni_Logical_WideInt_IsNegative"></a> IsNegative

この値が負であればtrueです。

```csharp
public bool IsNegative { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_Logical_WideInt_Equals_Omni_Logical_WideInt_"></a> Equals\(WideInt\)

```csharp
public bool Equals(WideInt other)
```

#### 引数（Parameters）

`other` [WideInt](Omni.Logical.WideInt.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_WideInt_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object obj)
```

#### 引数（Parameters）

`obj` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_WideInt_FromSignedProduct_Omni_Logical_IntRaw__Omni_Logical_IntRaw__"></a> FromSignedProduct\(in IntRaw, in IntRaw\)

符号付き<xref href="Omni.Logical.Precision.TotalBits" data-throw-if-not-resolved="false"></xref>ビット同士の積を厳密な倍幅結果として計算します。
TotalBits × TotalBits の符号付き積は必ず倍幅に収まるため、
このメソッドはオーバーフローしません（Try接頭辞なし）。

```csharp
public static WideInt FromSignedProduct(in IntRaw left, in IntRaw right)
```

#### 引数（Parameters）

`left` [IntRaw](Omni.Logical.IntRaw.md)

左辺値。

`right` [IntRaw](Omni.Logical.IntRaw.md)

右辺値。

#### 戻り値（Returns）

 [WideInt](Omni.Logical.WideInt.md)

厳密な積。

### <a id="Omni_Logical_WideInt_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_WideInt_GetLimb_System_Int32_"></a> GetLimb\(int\)

指定したlimbを返します。範囲外のインデックスはゼロを返します
（シフト演算が範囲外を素の値として読むため）。

```csharp
public ulong GetLimb(int index)
```

#### 引数（Parameters）

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Logical_WideInt_TryAdd_Omni_Logical_WideInt__Omni_Logical_WideInt__Omni_Logical_WideInt__"></a> TryAdd\(in WideInt, in WideInt, out WideInt\)

加算を試みます。

```csharp
public static bool TryAdd(in WideInt left, in WideInt right, out WideInt result)
```

#### 引数（Parameters）

`left` [WideInt](Omni.Logical.WideInt.md)

`right` [WideInt](Omni.Logical.WideInt.md)

`result` [WideInt](Omni.Logical.WideInt.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_WideInt_TryNegate_Omni_Logical_WideInt__Omni_Logical_WideInt__"></a> TryNegate\(in WideInt, out WideInt\)

符号反転を試みます。MinValue（-2^(WideBits-1)）の反転は失敗します。

```csharp
public static bool TryNegate(in WideInt value, out WideInt result)
```

#### 引数（Parameters）

`value` [WideInt](Omni.Logical.WideInt.md)

`result` [WideInt](Omni.Logical.WideInt.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_WideInt_TryRoundToScaleInt_Omni_Logical_WideInt__System_Int32_Omni_Logical_IntRaw__"></a> TryRoundToScaleInt\(in WideInt, int, out IntRaw\)

このWide値を最近接偶数丸めで<code class="paramref">fractionalBitsToRemove</code>ビット右へ丸め、
<xref href="Omni.Logical.Precision.TotalBits" data-throw-if-not-resolved="false"></xref>ビット符号付き整数へ収めます。
丸め対象の絶対値に対して丸めを行い符号を再適用するため、
2の補数の直接算術シフトによる負方向バイアスを避けます。結果が
TotalBitsビット符号付き範囲を超える場合は失敗します。

```csharp
public static bool TryRoundToScaleInt(in WideInt value, int fractionalBitsToRemove, out IntRaw result)
```

#### 引数（Parameters）

`value` [WideInt](Omni.Logical.WideInt.md)

丸める対象のWide値。

`fractionalBitsToRemove` [int](https://learn.microsoft.com/dotnet/api/system.int32)

切り捨てる下位ビット数（0以上）。

`result` [IntRaw](Omni.Logical.IntRaw.md)

丸め結果。失敗時はゼロ。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

TotalBitsビット符号付き範囲に収まる場合はtrue。

### <a id="Omni_Logical_WideInt_TrySubtract_Omni_Logical_WideInt__Omni_Logical_WideInt__Omni_Logical_WideInt__"></a> TrySubtract\(in WideInt, in WideInt, out WideInt\)

減算を試みます。

```csharp
public static bool TrySubtract(in WideInt left, in WideInt right, out WideInt result)
```

#### 引数（Parameters）

`left` [WideInt](Omni.Logical.WideInt.md)

`right` [WideInt](Omni.Logical.WideInt.md)

`result` [WideInt](Omni.Logical.WideInt.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## 演算子（Operators）

### <a id="Omni_Logical_WideInt_op_Equality_Omni_Logical_WideInt_Omni_Logical_WideInt_"></a> operator ==\(WideInt, WideInt\)

2つの値が等しい場合はtrueです。

```csharp
public static bool operator ==(WideInt left, WideInt right)
```

#### 引数（Parameters）

`left` [WideInt](Omni.Logical.WideInt.md)

`right` [WideInt](Omni.Logical.WideInt.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_WideInt_op_Inequality_Omni_Logical_WideInt_Omni_Logical_WideInt_"></a> operator \!=\(WideInt, WideInt\)

2つの値が異なる場合はtrueです。

```csharp
public static bool operator !=(WideInt left, WideInt right)
```

#### 引数（Parameters）

`left` [WideInt](Omni.Logical.WideInt.md)

`right` [WideInt](Omni.Logical.WideInt.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
