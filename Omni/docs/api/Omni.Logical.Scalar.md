# <a id="Omni_Logical_Scalar"></a> Struct Scalar

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

位置・スケール用の固定小数点数（符号付き2の補数）です。
総ビット数は<xref href="Omni.Logical.Precision.TotalBits" data-throw-if-not-resolved="false"></xref>、小数部は
<xref href="Omni.Logical.Precision.FractionalBits" data-throw-if-not-resolved="false"></xref>で、数値 = SignedRawInteger / 2^FractionalBits、
範囲は概ね ±2^<xref href="Omni.Logical.Precision.IntegerBits" data-throw-if-not-resolved="false"></xref> です。
構成はQ95.96（192ビット）へ固定されています。Omniの論理Position/Scaleで使う
共通Scalar型です（Position用途の意味の分離は<xref href="Omni.Logical.Position3" data-throw-if-not-resolved="false"></xref>で行い、
Scaleはこの型を直接3成分（<xref href="Omni.Logical.Vector3" data-throw-if-not-resolved="false"></xref>）で使います）。
Silent Wraparound / Silent Clampは行わず、Overflowが起き得る演算はすべてTry APIです。

```csharp
public readonly struct Scalar : IEquatable<Scalar>, IComparable<Scalar>
```

#### 実装するインターフェース（Implements）

[IEquatable<Scalar\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1), 
[IComparable<Scalar\>](https://learn.microsoft.com/dotnet/api/system.icomparable\-1)

## コンストラクター（Constructors）

### <a id="Omni_Logical_Scalar__ctor_Omni_Logical_IntRaw__"></a> Scalar\(in IntRaw\)

生の<xref href="Omni.Logical.Precision.TotalBits" data-throw-if-not-resolved="false"></xref>ビット表現から値を構築します。

```csharp
public Scalar(in IntRaw raw)
```

#### 引数（Parameters）

`raw` [IntRaw](Omni.Logical.IntRaw.md)

## フィールド（Fields）

### <a id="Omni_Logical_Scalar_FractionalBits"></a> FractionalBits

小数部のビット数です。

```csharp
public const int FractionalBits = 96
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_Scalar_MaxValue"></a> MaxValue

表現可能な最大値（2^IntegerBits - 2^-FractionalBits）です。

```csharp
public static readonly Scalar MaxValue
```

#### 値（Field Value）

 [Scalar](Omni.Logical.Scalar.md)

### <a id="Omni_Logical_Scalar_MinValue"></a> MinValue

表現可能な最小値（-2^IntegerBits）です。

```csharp
public static readonly Scalar MinValue
```

#### 値（Field Value）

 [Scalar](Omni.Logical.Scalar.md)

### <a id="Omni_Logical_Scalar_One"></a> One

1.0を表す値です（Raw = 2^FractionalBits）。

```csharp
public static readonly Scalar One
```

#### 値（Field Value）

 [Scalar](Omni.Logical.Scalar.md)

### <a id="Omni_Logical_Scalar_Raw"></a> Raw

この値の生の<xref href="Omni.Logical.Precision.TotalBits" data-throw-if-not-resolved="false"></xref>ビット2の補数表現です。

```csharp
public readonly IntRaw Raw
```

#### 値（Field Value）

 [IntRaw](Omni.Logical.IntRaw.md)

### <a id="Omni_Logical_Scalar_Zero"></a> Zero

ゼロ値です。

```csharp
public static readonly Scalar Zero
```

#### 値（Field Value）

 [Scalar](Omni.Logical.Scalar.md)

## プロパティ（Properties）

### <a id="Omni_Logical_Scalar_IsDivisionSupported"></a> IsDivisionSupported

除算・逆数・逆平方根が使えるかどうかです。

<p>
Newton-Raphson反復は 2.0 と 0.5 と 1.5 を定数として必要とします。
小数部ビット数を極端に取ると（<code>FractionalBits &gt; TotalBits-3</code> で 2.0 が、
<code>FractionalBits &lt; 1</code> で 0.5 が）これらが表現できず、反復が破綻します。
黙って誤った値を返さないよう、その場合は除算系のAPIをすべて失敗させます。
Project Settings 側でも同じ条件を事前に警告します。
</p>

```csharp
public static bool IsDivisionSupported { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Scalar_IsNegative"></a> IsNegative

この値が負であればtrueです。

```csharp
public bool IsNegative { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Scalar_IsZero"></a> IsZero

この値がゼロであればtrueです。

```csharp
public bool IsZero { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_Logical_Scalar_CompareTo_Omni_Logical_Scalar_"></a> CompareTo\(Scalar\)

```csharp
public int CompareTo(Scalar other)
```

#### 引数（Parameters）

`other` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_Scalar_Equals_Omni_Logical_Scalar_"></a> Equals\(Scalar\)

```csharp
public bool Equals(Scalar other)
```

#### 引数（Parameters）

`other` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Scalar_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object obj)
```

#### 引数（Parameters）

`obj` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Scalar_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_Scalar_ToString"></a> ToString\(\)

```csharp
public override string ToString()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Logical_Scalar_TryAdd_Omni_Logical_Scalar__Omni_Logical_Scalar__Omni_Logical_Scalar__"></a> TryAdd\(in Scalar, in Scalar, out Scalar\)

加算を試みます。結果が表現範囲を超える場合は失敗します。

```csharp
public static bool TryAdd(in Scalar left, in Scalar right, out Scalar result)
```

#### 引数（Parameters）

`left` [Scalar](Omni.Logical.Scalar.md)

`right` [Scalar](Omni.Logical.Scalar.md)

`result` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Scalar_TryDivide_Omni_Logical_Scalar__Omni_Logical_Scalar__Omni_Logical_Scalar__"></a> TryDivide\(in Scalar, in Scalar, out Scalar\)

除算（left / right）を固定長整数カーネルで求めます。
逆数を経由せず、商を一度だけ最近接偶数丸めします。

```csharp
public static bool TryDivide(in Scalar left, in Scalar right, out Scalar result)
```

#### 引数（Parameters）

`left` [Scalar](Omni.Logical.Scalar.md)

`right` [Scalar](Omni.Logical.Scalar.md)

`result` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Scalar_TryFromDouble_System_Double_Omni_Logical_Scalar__"></a> TryFromDouble\(double, out Scalar\)

倍精度値を最近接偶数で量子化します。非有限値と表現範囲外は失敗します。
演出計算（倍精度）とLogicalの境界で使います。Logical演算そのものはScalarのまま行います。

```csharp
public static bool TryFromDouble(double value, out Scalar result)
```

#### 引数（Parameters）

`value` [double](https://learn.microsoft.com/dotnet/api/system.double)

`result` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Scalar_TryFromFloat_System_Single_Omni_Logical_Scalar__"></a> TryFromFloat\(float, out Scalar\)

IEEE 754単精度値からの変換を試みます。
小数部へ最近接偶数で丸めます。非有限値と表現範囲外は失敗します。

```csharp
public static bool TryFromFloat(float value, out Scalar result)
```

#### 引数（Parameters）

`value` [float](https://learn.microsoft.com/dotnet/api/system.single)

`result` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Scalar_TryLerp_Omni_Logical_Scalar__Omni_Logical_Scalar__Omni_Logical_Scalar__Omni_Logical_Scalar__"></a> TryLerp\(in Scalar, in Scalar, in Scalar, out Scalar\)

0〜1の補間比率で線形補間を試みます。

<p>
<code>from+(to-from)*t</code> の順で計算します。<code>from*(1-t)+to*t</code> ではありません。
端点が1e11メートル級で差が1メートルのような場合、後者は巨大な値どうしの
引き算になって差の精度が丸めに埋もれますが、前者は先に差を取るため
差分の精度がそのまま残ります。ベイク済みサンプル間の補間は
まさにその形（巨大な絶対座標＋小さな差分）なので、この順序が要件です。
</p>
<p>
<code class="paramref">t</code> が0または1のときは端点をraw一致でそのまま返します
（サンプル時刻ちょうどで補間誤差を混ぜないためです）。
</p>
<p>
次の場合は失敗します（resultはゼロ）。
</p>
<ul><li><code class="paramref">t</code> が0〜1の範囲外のとき。</li><li>
<code class="paramref">t</code> が0でも1でもなく、<code class="paramref">from</code> と <code class="paramref">to</code> が異なり、
差 <code>to-from</code> が表現範囲を超えるとき（符号の異なる巨大な端点どうし）。
補間結果そのものは常に端点の間にあり表現できますが、先に差を取る順序のため失敗します。
</li></ul>

```csharp
public static bool TryLerp(in Scalar from, in Scalar to, in Scalar t, out Scalar result)
```

#### 引数（Parameters）

`from` [Scalar](Omni.Logical.Scalar.md)

開始値。

`to` [Scalar](Omni.Logical.Scalar.md)

終了値。

`t` [Scalar](Omni.Logical.Scalar.md)

補間比率(0〜1)。範囲外は失敗します。

`result` [Scalar](Omni.Logical.Scalar.md)

補間結果。失敗時はゼロ。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Scalar_TryLerpLog2_Omni_Logical_Scalar__Omni_Logical_Scalar__Omni_Logical_Scalar__Omni_Logical_Scalar__"></a> TryLerpLog2\(in Scalar, in Scalar, in Scalar, out Scalar\)

0〜1の補間比率で対数2空間の補間を試みます。
正の端点は拡張精度のraw整数上で幾何補間し、非正の端点を含む場合は
同じraw整数上の線形補間へフォールバックします。

```csharp
public static bool TryLerpLog2(in Scalar from, in Scalar to, in Scalar t, out Scalar result)
```

#### 引数（Parameters）

`from` [Scalar](Omni.Logical.Scalar.md)

`to` [Scalar](Omni.Logical.Scalar.md)

`t` [Scalar](Omni.Logical.Scalar.md)

`result` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Scalar_TryMultiply_Omni_Logical_Scalar__Omni_Logical_Scalar__Omni_Logical_Scalar__"></a> TryMultiply\(in Scalar, in Scalar, out Scalar\)

乗算を試みます。LogicalWideIntアキュムレータで厳密な積を計算してから
最近接偶数丸めで<xref href="Omni.Logical.Scalar.FractionalBits" data-throw-if-not-resolved="false"></xref>ビット右シフトし、表現範囲を超える場合は失敗します。

```csharp
public static bool TryMultiply(in Scalar left, in Scalar right, out Scalar result)
```

#### 引数（Parameters）

`left` [Scalar](Omni.Logical.Scalar.md)

`right` [Scalar](Omni.Logical.Scalar.md)

`result` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Scalar_TryNegate_Omni_Logical_Scalar__Omni_Logical_Scalar__"></a> TryNegate\(in Scalar, out Scalar\)

符号反転を試みます。MinValueの反転は失敗します。

```csharp
public static bool TryNegate(in Scalar value, out Scalar result)
```

#### 引数（Parameters）

`value` [Scalar](Omni.Logical.Scalar.md)

`result` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Scalar_TryParse_System_String_Omni_Logical_Scalar__"></a> TryParse\(string, out Scalar\)

カルチャに依存しない固定小数点表記または科学表記から変換を試みます。
表現範囲外の値と不正な文字列は失敗し、二進分解能の中間値は最近接偶数へ丸めます。

```csharp
public static bool TryParse(string text, out Scalar result)
```

#### 引数（Parameters）

`text` [string](https://learn.microsoft.com/dotnet/api/system.string)

`result` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Scalar_TryReciprocal_Omni_Logical_Scalar__Omni_Logical_Scalar__"></a> TryReciprocal\(in Scalar, out Scalar\)

逆数（1/value）を固定長整数除算で求め、最後に最近接偶数丸めします。
最小単位の半分未満の結果はゼロになり、ゼロ除算・表現範囲外では失敗します。

```csharp
public static bool TryReciprocal(in Scalar value, out Scalar result)
```

#### 引数（Parameters）

`value` [Scalar](Omni.Logical.Scalar.md)

逆数を求める値。

`result` [Scalar](Omni.Logical.Scalar.md)

逆数。失敗時はゼロ。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

valueが非ゼロかつ逆数が表現可能な場合はtrue。

### <a id="Omni_Logical_Scalar_TryReciprocalSqrt_Omni_Logical_Scalar__Omni_Logical_Scalar__"></a> TryReciprocalSqrt\(in Scalar, out Scalar\)

逆平方根（1/sqrt(value)）を試みます。Newton-Raphson法
（y_(n+1) = y_n*(1.5 - 0.5*value*y_n^2)）で平方根・除算を使わず反復収束させます。
Quaternion正規化係数の計算に使うため、value（成分二乗和）はRotationScalarの
範囲(最大約2)を超え得る値を受け取れるよう、この十分な整数部を持つ
Scalar側に実装します（Quaternion正規化が渡す二乗和は8.0未満です）。

<p>
valueがゼロ、負、またはちょうど1量子（2^-FractionalBits）の場合は失敗します。
1量子の結果（2^48）は表現できますが、反復の初期値の二乗（2^96）がScalarの範囲（2^95未満）を超えるためです。
それ以外の正の値は、サンプルと特別値（2量子、最大値、2の冪とその前後など）で成功を確かめています。
</p>
<p>
結果の誤差（厳密な1/sqrt(value)との差、単位は1量子 = 2^-FractionalBits）は、
4*max(1, 1/sqrt(value)) + 0.5*sqrt(value) 量子以内です。
valueが小さい（結果が大きい）ほど第1項、valueが大きいほど第2項（途中のy^2の分解能が粗くなるため）が効きます。
サンプルでの実測の最大は、この上限のおよそ6割です。valueが2^8を超えると誤差は急に増え、2^94付近では結果の相対誤差が約1割に達します。
二乗和が8.0未満の範囲では、valueが大きい側でも上限は数量子です。
</p>

```csharp
public static bool TryReciprocalSqrt(in Scalar value, out Scalar result)
```

#### 引数（Parameters）

`value` [Scalar](Omni.Logical.Scalar.md)

`result` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Scalar_TryScaleByPowerOfTwo_Omni_Logical_Scalar__System_Int32_Omni_Logical_Scalar__"></a> TryScaleByPowerOfTwo\(in Scalar, int, out Scalar\)

2の冪を掛ける（<code class="paramref">exponent</code>が負なら割る）ことを試みます。
固定小数点の生表現はRaw（整数）と2^FractionalBitsの積なので、2の冪を掛ける操作は
Rawのビットシフトであり、Math.Powのような超越関数近似を経由しません
（2進指数分離の実装で使うためのビルディングブロックです）。

<p>
結果は厳密値 value*2^exponent の最近接偶数丸めです。exponentが0以上なら桁が増えるだけで丸めは起きません。
exponentが負で分解能（1量子 = 2^-FractionalBits）に満たない端数が出るときは、最近接偶数へ丸めます。
結果が半量子以下ならゼロ（ちょうど半量子は偶数側のゼロ）、半量子を超えて1.5量子未満なら1量子です。
ゼロへの切り捨てではありません。
</p>
<p>
valueがゼロなら、exponentに関わらず（<xref href="System.Int32.MinValue" data-throw-if-not-resolved="false"></xref> でも）成功してゼロを返します。
それ以外では、次の場合に失敗します（resultはゼロ）。
</p>
<ul><li>
exponentが <xref href="System.Int32.MinValue" data-throw-if-not-resolved="false"></xref> のとき。内部で -exponent を int で取るため符号が反転せず、
結果がゼロになるはずの入力でも失敗します。
</li><li>
exponentが0以上で、結果が表現範囲を超えるとき。
</li><li>
exponentが <code>TotalBits - 1</code>（191）以上のとき。2^exponent を正のRawとして作れないため、結果が表現できても失敗します。
該当するのは value = -1量子（Raw = -1）かつ exponent = 191 の、結果がちょうど <xref href="Omni.Logical.Scalar.MinValue" data-throw-if-not-resolved="false"></xref> になる1通りだけです。
</li></ul>
<p>
exponentに <xref href="System.Int32.MinValue" data-throw-if-not-resolved="false"></xref> を渡すのは呼び出し側の契約違反です。
<code>UNITY_ASSERTIONS</code> が定義された構成（EditorとDevelopment Build）では、valueがゼロの場合も含めて、
アサーションログ（<code>LogType.Assert</code>）で知らせます。ログを出すだけで、例外は投げず、戻り値も上の規則のまま変わりません。
定義されない構成（リリース）では、この検査は呼び出しごと除去されます。
</p>

```csharp
public static bool TryScaleByPowerOfTwo(in Scalar value, int exponent, out Scalar result)
```

#### 引数（Parameters）

`value` [Scalar](Omni.Logical.Scalar.md)

掛ける対象です。

`exponent` [int](https://learn.microsoft.com/dotnet/api/system.int32)

2の冪の指数です。<xref href="System.Int32.MinValue" data-throw-if-not-resolved="false"></xref> は渡さないでください。

`result` [Scalar](Omni.Logical.Scalar.md)

結果。失敗時はゼロ。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Scalar_TrySqrt_Omni_Logical_Scalar__Omni_Logical_Scalar__"></a> TrySqrt\(in Scalar, out Scalar\)

平方根を固定長整数カーネルで求めます。valueがゼロまたは負の場合は失敗します（sqrt(0)=0を有効値として
扱いたい呼び出し元は、この関数を呼ぶ前にIsZeroを検査してください）。

```csharp
public static bool TrySqrt(in Scalar value, out Scalar result)
```

#### 引数（Parameters）

`value` [Scalar](Omni.Logical.Scalar.md)

`result` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Scalar_TrySubtract_Omni_Logical_Scalar__Omni_Logical_Scalar__Omni_Logical_Scalar__"></a> TrySubtract\(in Scalar, in Scalar, out Scalar\)

減算を試みます。結果が表現範囲を超える場合は失敗します。

```csharp
public static bool TrySubtract(in Scalar left, in Scalar right, out Scalar result)
```

#### 引数（Parameters）

`left` [Scalar](Omni.Logical.Scalar.md)

`right` [Scalar](Omni.Logical.Scalar.md)

`result` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Scalar_TryToDouble_System_Double__"></a> TryToDouble\(out double\)

最近接偶数の倍精度値へ変換します（表現範囲の値は常に有限の倍精度に収まります）。

```csharp
public bool TryToDouble(out double result)
```

#### 引数（Parameters）

`result` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Scalar_TryToFloat_System_Single__"></a> TryToFloat\(out float\)

有限なIEEE 754単精度値への変換を試みます。
単精度の範囲を超える場合は失敗し、必要な丸めは最近接偶数で行います。

```csharp
public bool TryToFloat(out float result)
```

#### 引数（Parameters）

`result` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## 演算子（Operators）

### <a id="Omni_Logical_Scalar_op_Equality_Omni_Logical_Scalar_Omni_Logical_Scalar_"></a> operator ==\(Scalar, Scalar\)

2つの値が等しい場合はtrueです。

```csharp
public static bool operator ==(Scalar left, Scalar right)
```

#### 引数（Parameters）

`left` [Scalar](Omni.Logical.Scalar.md)

`right` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Scalar_op_GreaterThan_Omni_Logical_Scalar_Omni_Logical_Scalar_"></a> operator \>\(Scalar, Scalar\)

左辺が大きい場合はtrueです。

```csharp
public static bool operator >(Scalar left, Scalar right)
```

#### 引数（Parameters）

`left` [Scalar](Omni.Logical.Scalar.md)

`right` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Scalar_op_GreaterThanOrEqual_Omni_Logical_Scalar_Omni_Logical_Scalar_"></a> operator \>=\(Scalar, Scalar\)

左辺が同じか大きい場合はtrueです。

```csharp
public static bool operator >=(Scalar left, Scalar right)
```

#### 引数（Parameters）

`left` [Scalar](Omni.Logical.Scalar.md)

`right` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Scalar_op_Inequality_Omni_Logical_Scalar_Omni_Logical_Scalar_"></a> operator \!=\(Scalar, Scalar\)

2つの値が異なる場合はtrueです。

```csharp
public static bool operator !=(Scalar left, Scalar right)
```

#### 引数（Parameters）

`left` [Scalar](Omni.Logical.Scalar.md)

`right` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Scalar_op_LessThan_Omni_Logical_Scalar_Omni_Logical_Scalar_"></a> operator <\(Scalar, Scalar\)

左辺が小さい場合はtrueです。

```csharp
public static bool operator <(Scalar left, Scalar right)
```

#### 引数（Parameters）

`left` [Scalar](Omni.Logical.Scalar.md)

`right` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Scalar_op_LessThanOrEqual_Omni_Logical_Scalar_Omni_Logical_Scalar_"></a> operator <=\(Scalar, Scalar\)

左辺が同じか小さい場合はtrueです。

```csharp
public static bool operator <=(Scalar left, Scalar right)
```

#### 引数（Parameters）

`left` [Scalar](Omni.Logical.Scalar.md)

`right` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
