# <a id="Omni_Logical_IntRaw"></a> Struct IntRaw

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

符号付き<xref href="Omni.Logical.Precision.TotalBits" data-throw-if-not-resolved="false"></xref>ビット2の補数整数です。
64ビットlimbを<xref href="Omni.Logical.Precision.LimbCount" data-throw-if-not-resolved="false"></xref>本並べて格納します。
Limb0が最下位64ビット、最上位limbのbit63が符号ビットです。
Scale系の型（<xref href="Omni.Logical.Scalar" data-throw-if-not-resolved="false"></xref>等）の生表現として使う共通の整数演算基盤です。
Silent Wraparound / Silent Clampは行わず、Overflowが起き得る演算はすべてTry APIです。

```csharp
public readonly struct IntRaw : IEquatable<IntRaw>, IComparable<IntRaw>
```

#### 実装するインターフェース（Implements）

[IEquatable<IntRaw\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1), 
[IComparable<IntRaw\>](https://learn.microsoft.com/dotnet/api/system.icomparable\-1)

## コンストラクター（Constructors）

### <a id="Omni_Logical_IntRaw__ctor_System_UInt64_System_UInt64_"></a> IntRaw\(ulong, ulong\)

128ビットの2の補数の値（下位・上位64bit）を、同じ値の<xref href="Omni.Logical.Precision.TotalBits" data-throw-if-not-resolved="false"></xref>ビット整数へ
符号拡張して構築します（上位64bitのbit63が符号）。

```csharp
public IntRaw(ulong low, ulong high)
```

#### 引数（Parameters）

`low` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

`high` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Logical_IntRaw__ctor_System_UInt64_System_UInt64_System_UInt64_"></a> IntRaw\(ulong, ulong, ulong\)

3本のlimb（下位から）で構築します。

```csharp
public IntRaw(ulong limb0, ulong limb1, ulong limb2)
```

#### 引数（Parameters）

`limb0` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

`limb1` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

`limb2` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Logical_IntRaw__ctor_System_ReadOnlySpan_System_UInt64__"></a> IntRaw\(ReadOnlySpan<ulong\>\)

下位limbから順に並んだスパンから構築します。
要素が足りない分はゼロ、余った分は捨てます（呼び出し側の切り詰め忘れで
例外を投げるより、上位ビットの脱落を明示的に扱う各Try APIへ任せます）。

```csharp
public IntRaw(ReadOnlySpan<ulong> limbs)
```

#### 引数（Parameters）

`limbs` [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[ulong](https://learn.microsoft.com/dotnet/api/system.uint64)\>

## フィールド（Fields）

### <a id="Omni_Logical_IntRaw_LegacyLimbCount"></a> LegacyLimbCount

保存の旧形式（Logicalが128ビット・小数32ビット、Q95.32だったころ）の、値1つあたりのlimb数です。

```csharp
public const int LegacyLimbCount = 2
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_IntRaw_LegacyLimbShift"></a> LegacyLimbShift

旧形式の値を現在の形式へ移すとき、下位に足すlimb数です（小数部が32ビットから96ビットへ64ビット増えたため）。
旧rawに2^64を掛けると同じ数値の現在のrawになり、limb列では [L0, L1] → [0, L0, L1] です。

```csharp
public const int LegacyLimbShift = 1
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_IntRaw_Limb0"></a> Limb0

最下位64ビット（bit0-63）です。

```csharp
public readonly ulong Limb0
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Logical_IntRaw_Limb1"></a> Limb1

bit64-127です。

```csharp
public readonly ulong Limb1
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Logical_IntRaw_Limb2"></a> Limb2

最上位64ビット（bit128-191、bit63が符号ビット）です。

```csharp
public readonly ulong Limb2
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Logical_IntRaw_MaxValue"></a> MaxValue

表現可能な最大値（2^(TotalBits-1) - 1）です。

```csharp
public static readonly IntRaw MaxValue
```

#### 値（Field Value）

 [IntRaw](Omni.Logical.IntRaw.md)

### <a id="Omni_Logical_IntRaw_MinValue"></a> MinValue

表現可能な最小値（-2^(TotalBits-1)）です。

```csharp
public static readonly IntRaw MinValue
```

#### 値（Field Value）

 [IntRaw](Omni.Logical.IntRaw.md)

### <a id="Omni_Logical_IntRaw_One"></a> One

1を表す値です。

```csharp
public static readonly IntRaw One
```

#### 値（Field Value）

 [IntRaw](Omni.Logical.IntRaw.md)

### <a id="Omni_Logical_IntRaw_Zero"></a> Zero

ゼロ値です。

```csharp
public static readonly IntRaw Zero
```

#### 値（Field Value）

 [IntRaw](Omni.Logical.IntRaw.md)

## プロパティ（Properties）

### <a id="Omni_Logical_IntRaw_IsNegative"></a> IsNegative

この値が負であればtrueです。

```csharp
public bool IsNegative { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_IntRaw_IsZero"></a> IsZero

この値がゼロであればtrueです。

```csharp
public bool IsZero { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_Logical_IntRaw_CompareTo_Omni_Logical_IntRaw_"></a> CompareTo\(IntRaw\)

```csharp
public int CompareTo(IntRaw other)
```

#### 引数（Parameters）

`other` [IntRaw](Omni.Logical.IntRaw.md)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_IntRaw_CopyTo_System_Span_System_UInt64__"></a> CopyTo\(Span<ulong\>\)

下位limbから順にスパンへ書き出します。

```csharp
public void CopyTo(Span<ulong> destination)
```

#### 引数（Parameters）

`destination` [Span](https://learn.microsoft.com/dotnet/api/system.span\-1)<[ulong](https://learn.microsoft.com/dotnet/api/system.uint64)\>

### <a id="Omni_Logical_IntRaw_Equals_Omni_Logical_IntRaw_"></a> Equals\(IntRaw\)

```csharp
public bool Equals(IntRaw other)
```

#### 引数（Parameters）

`other` [IntRaw](Omni.Logical.IntRaw.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_IntRaw_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object obj)
```

#### 引数（Parameters）

`obj` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_IntRaw_FromLegacyLimbs_System_ReadOnlySpan_System_UInt64__System_Int32_"></a> FromLegacyLimbs\(ReadOnlySpan<ulong\>, int\)

旧形式（Q95.32、<xref href="Omni.Logical.IntRaw.LegacyLimbCount" data-throw-if-not-resolved="false"></xref>本）のlimbを<code class="paramref">offset</code>から読み、同じ数値の現在の形式へ移します。

```csharp
public static IntRaw FromLegacyLimbs(ReadOnlySpan<ulong> limbs, int offset)
```

#### 引数（Parameters）

`limbs` [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[ulong](https://learn.microsoft.com/dotnet/api/system.uint64)\>

`offset` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [IntRaw](Omni.Logical.IntRaw.md)

### <a id="Omni_Logical_IntRaw_FromLimbArray_System_UInt64___"></a> FromLimbArray\(ulong\[\]\)

Limb0順のulong配列から復元します。
nullまたは要素数が<xref href="Omni.Logical.Precision.LimbCount" data-throw-if-not-resolved="false"></xref>でない場合はゼロを返します
（破損したシリアライズデータに対する安全側フォールバック）。

<p>
現在の構成と幅が異なる配列は互換変換せずゼロとして扱います。
ここで黙って詰め直すと、異なるrawビット列を現在の構成として
誤解釈した値が正しい値の顔をして通ってしまいます。
</p>

```csharp
public static IntRaw FromLimbArray(ulong[] limbs)
```

#### 引数（Parameters）

`limbs` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)\[\]

#### 戻り値（Returns）

 [IntRaw](Omni.Logical.IntRaw.md)

### <a id="Omni_Logical_IntRaw_FromSerializedLimbs_System_UInt64___"></a> FromSerializedLimbs\(ulong\[\]\)

Unityの保存値（Limb0順のulong配列）から<xref href="Omni.Logical.Scalar" data-throw-if-not-resolved="false"></xref>のrawを復元します。
現在の形式（<xref href="Omni.Logical.Precision.LimbCount" data-throw-if-not-resolved="false"></xref>本）はそのまま、旧形式（<xref href="Omni.Logical.IntRaw.LegacyLimbCount" data-throw-if-not-resolved="false"></xref>本、Q95.32）は
下位に0のlimbを足して同じ数値の現在の形式（Q95.96）へ移します。それ以外の長さ・nullはゼロです
（配布先の既存資産を読むための互換。書き込みは常に現在の形式）。

```csharp
public static IntRaw FromSerializedLimbs(ulong[] limbs)
```

#### 引数（Parameters）

`limbs` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)\[\]

#### 戻り値（Returns）

 [IntRaw](Omni.Logical.IntRaw.md)

### <a id="Omni_Logical_IntRaw_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_IntRaw_GetLimb_System_Int32_"></a> GetLimb\(int\)

指定したlimbを返します。範囲外のインデックスはゼロを返します
（シフト演算が範囲外を素の値として読むため）。

```csharp
public ulong GetLimb(int index)
```

#### 引数（Parameters）

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Logical_IntRaw_ToLimbArray"></a> ToLimbArray\(\)

Limb0から順に<xref href="Omni.Logical.Precision.LimbCount" data-throw-if-not-resolved="false"></xref>要素のulong配列へパックします
（Unity SerializeField用。個別ulongフィールドの代わりに配列でまとめる）。

```csharp
public ulong[] ToLimbArray()
```

#### 戻り値（Returns）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)\[\]

### <a id="Omni_Logical_IntRaw_TryAdd_Omni_Logical_IntRaw__Omni_Logical_IntRaw__Omni_Logical_IntRaw__"></a> TryAdd\(in IntRaw, in IntRaw, out IntRaw\)

加算を試みます。同符号の加算で結果の符号が反転した場合はオーバーフローです。

```csharp
public static bool TryAdd(in IntRaw left, in IntRaw right, out IntRaw result)
```

#### 引数（Parameters）

`left` [IntRaw](Omni.Logical.IntRaw.md)

左辺値。

`right` [IntRaw](Omni.Logical.IntRaw.md)

右辺値。

`result` [IntRaw](Omni.Logical.IntRaw.md)

加算結果。オーバーフロー時はゼロ。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

オーバーフローしなかった場合はtrue。

### <a id="Omni_Logical_IntRaw_TryCopyTo_System_UInt64___"></a> TryCopyTo\(ulong\[\]\)

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

### <a id="Omni_Logical_IntRaw_TryNegate_Omni_Logical_IntRaw__Omni_Logical_IntRaw__"></a> TryNegate\(in IntRaw, out IntRaw\)

符号反転を試みます。MinValue（-2^(TotalBits-1)）の反転は
+2^(TotalBits-1)が表現不可のため失敗します。

```csharp
public static bool TryNegate(in IntRaw value, out IntRaw result)
```

#### 引数（Parameters）

`value` [IntRaw](Omni.Logical.IntRaw.md)

反転する値。

`result` [IntRaw](Omni.Logical.IntRaw.md)

反転結果。失敗時はゼロ。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

表現可能な場合はtrue。

### <a id="Omni_Logical_IntRaw_TrySubtract_Omni_Logical_IntRaw__Omni_Logical_IntRaw__Omni_Logical_IntRaw__"></a> TrySubtract\(in IntRaw, in IntRaw, out IntRaw\)

減算を試みます。左辺と右辺の符号が異なり、かつ結果の符号が左辺と異なる場合はオーバーフローです。

```csharp
public static bool TrySubtract(in IntRaw left, in IntRaw right, out IntRaw result)
```

#### 引数（Parameters）

`left` [IntRaw](Omni.Logical.IntRaw.md)

左辺値。

`right` [IntRaw](Omni.Logical.IntRaw.md)

右辺値。

`result` [IntRaw](Omni.Logical.IntRaw.md)

減算結果。オーバーフロー時はゼロ。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

オーバーフローしなかった場合はtrue。

### <a id="Omni_Logical_IntRaw_WidenLegacyLimbArray_System_UInt64___System_Int32_"></a> WidenLegacyLimbArray\(ulong\[\], int\)

値を<code class="paramref">valueCount</code>個並べた平坦な旧形式の配列（値ごとに<xref href="Omni.Logical.IntRaw.LegacyLimbCount" data-throw-if-not-resolved="false"></xref>本）を、現在の形式の配列へ移します。

```csharp
public static ulong[] WidenLegacyLimbArray(ulong[] legacy, int valueCount)
```

#### 引数（Parameters）

`legacy` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)\[\]

`valueCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)\[\]

## 演算子（Operators）

### <a id="Omni_Logical_IntRaw_op_Equality_Omni_Logical_IntRaw_Omni_Logical_IntRaw_"></a> operator ==\(IntRaw, IntRaw\)

2つの値が等しい場合はtrueです。

```csharp
public static bool operator ==(IntRaw left, IntRaw right)
```

#### 引数（Parameters）

`left` [IntRaw](Omni.Logical.IntRaw.md)

`right` [IntRaw](Omni.Logical.IntRaw.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_IntRaw_op_Inequality_Omni_Logical_IntRaw_Omni_Logical_IntRaw_"></a> operator \!=\(IntRaw, IntRaw\)

2つの値が異なる場合はtrueです。

```csharp
public static bool operator !=(IntRaw left, IntRaw right)
```

#### 引数（Parameters）

`left` [IntRaw](Omni.Logical.IntRaw.md)

`right` [IntRaw](Omni.Logical.IntRaw.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
