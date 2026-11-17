# <a id="Omni_Logical_Quaternion"></a> Struct Quaternion

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

<xref href="Omni.Logical.RotationScalar" data-throw-if-not-resolved="false"></xref>を4成分(X,Y,Z,W)持つ高精度Quaternionです。
乗算は各成分の4項の積を256ビットのアキュムレータで全て合成してから一度だけ丸めます
（個々の積を先に丸めて足す誤差の蓄積を避けるため）。
正規化・nlerp・ベクトルの回転は複数の段に分かれ、段ごとに丸めます。
丸めの回数と誤差の上限は各演算の説明にあります（正規化は係数をScalar（2^-96刻み）で持つため、
成分の精度が約2^-96で頭打ちになり、単位Quaternionによるベクトルの回転は成分あたり最大約1.9量子の誤差です。
非単位Quaternionでは<xref href="Omni.Logical.Quaternion.TryRotate(Omni.Logical.Quaternion%40%2cOmni.Logical.Vector3%40%2cOmni.Logical.Vector3%40)" data-throw-if-not-resolved="false"></xref>の説明のとおり上限が大きくなり、成分が±2に近いと4量子に近づきます）。
論理Positionの回転でも、途中でUnity Quaternion/Matrix4x4へ変換しません。

```csharp
public readonly struct Quaternion : IEquatable<Quaternion>
```

#### 実装するインターフェース（Implements）

[IEquatable<Quaternion\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1)

## コンストラクター（Constructors）

### <a id="Omni_Logical_Quaternion__ctor_Omni_Logical_RotationScalar__Omni_Logical_RotationScalar__Omni_Logical_RotationScalar__Omni_Logical_RotationScalar__"></a> Quaternion\(in RotationScalar, in RotationScalar, in RotationScalar, in RotationScalar\)

4つの成分から構築します。

```csharp
public Quaternion(in RotationScalar x, in RotationScalar y, in RotationScalar z, in RotationScalar w)
```

#### 引数（Parameters）

`x` [RotationScalar](Omni.Logical.RotationScalar.md)

`y` [RotationScalar](Omni.Logical.RotationScalar.md)

`z` [RotationScalar](Omni.Logical.RotationScalar.md)

`w` [RotationScalar](Omni.Logical.RotationScalar.md)

## フィールド（Fields）

### <a id="Omni_Logical_Quaternion_Identity"></a> Identity

単位Quaternion（無回転）です。

```csharp
public static readonly Quaternion Identity
```

#### 値（Field Value）

 [Quaternion](Omni.Logical.Quaternion.md)

### <a id="Omni_Logical_Quaternion_W"></a> W

W成分（スカラー部）です。

```csharp
public readonly RotationScalar W
```

#### 値（Field Value）

 [RotationScalar](Omni.Logical.RotationScalar.md)

### <a id="Omni_Logical_Quaternion_X"></a> X

X成分（ベクトル部）です。

```csharp
public readonly RotationScalar X
```

#### 値（Field Value）

 [RotationScalar](Omni.Logical.RotationScalar.md)

### <a id="Omni_Logical_Quaternion_Y"></a> Y

Y成分（ベクトル部）です。

```csharp
public readonly RotationScalar Y
```

#### 値（Field Value）

 [RotationScalar](Omni.Logical.RotationScalar.md)

### <a id="Omni_Logical_Quaternion_Z"></a> Z

Z成分（ベクトル部）です。

```csharp
public readonly RotationScalar Z
```

#### 値（Field Value）

 [RotationScalar](Omni.Logical.RotationScalar.md)

## メソッド（Methods）

### <a id="Omni_Logical_Quaternion_Equals_Omni_Logical_Quaternion_"></a> Equals\(Quaternion\)

```csharp
public bool Equals(Quaternion other)
```

#### 引数（Parameters）

`other` [Quaternion](Omni.Logical.Quaternion.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Quaternion_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object obj)
```

#### 引数（Parameters）

`obj` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Quaternion_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_Quaternion_ToString"></a> ToString\(\)

```csharp
public override string ToString()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Logical_Quaternion_TryConjugate_Omni_Logical_Quaternion__Omni_Logical_Quaternion__"></a> TryConjugate\(in Quaternion, out Quaternion\)

共役（単位Quaternionであれば逆回転）を試みます。X/Y/Zを符号反転し、Wはそのまま返します。
いずれかの成分がMinValue（-2、単位Quaternionでは実質到達しない値）の場合のみ失敗します。

```csharp
public static bool TryConjugate(in Quaternion value, out Quaternion result)
```

#### 引数（Parameters）

`value` [Quaternion](Omni.Logical.Quaternion.md)

`result` [Quaternion](Omni.Logical.Quaternion.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Quaternion_TryFromFloat4_System_Single_System_Single_System_Single_System_Single_Omni_Logical_Quaternion__"></a> TryFromFloat4\(float, float, float, float, out Quaternion\)

IEEE 754単精度の4成分(X,Y,Z,W)から変換を試みます。正規化はしません
（UnityEngine.Quaternion/Unity.Mathematics.quaternionいずれの成分を渡しても
使えるよう、この型自体はUnity側の型に依存させていません）。

```csharp
public static bool TryFromFloat4(float x, float y, float z, float w, out Quaternion result)
```

#### 引数（Parameters）

`x` [float](https://learn.microsoft.com/dotnet/api/system.single)

`y` [float](https://learn.microsoft.com/dotnet/api/system.single)

`z` [float](https://learn.microsoft.com/dotnet/api/system.single)

`w` [float](https://learn.microsoft.com/dotnet/api/system.single)

`result` [Quaternion](Omni.Logical.Quaternion.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Quaternion_TryMultiply_Omni_Logical_Quaternion__Omni_Logical_Quaternion__Omni_Logical_Quaternion__"></a> TryMultiply\(in Quaternion, in Quaternion, out Quaternion\)

Hamilton積（result = left * right）を試みます。各成分は4項の和で、
符号付き256ビット（小数部252ビット）のアキュムレータで全項を合成してから一度だけ最近接偶数で丸めます。
結果の成分が表現範囲（-2以上2未満）を超えるときは失敗します。
途中の和が±8.0に達しても失敗しますが、これは成分が±2に近い極端な非単位Quaternionの場合で、
単位Quaternion同士では起きません。

```csharp
public static bool TryMultiply(in Quaternion left, in Quaternion right, out Quaternion result)
```

#### 引数（Parameters）

`left` [Quaternion](Omni.Logical.Quaternion.md)

`right` [Quaternion](Omni.Logical.Quaternion.md)

`result` [Quaternion](Omni.Logical.Quaternion.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Quaternion_TryNlerp_Omni_Logical_Quaternion__Omni_Logical_Quaternion__Omni_Logical_Scalar__Omni_Logical_Quaternion__"></a> TryNlerp\(in Quaternion, in Quaternion, in Scalar, out Quaternion\)

2つの回転を成分ごとに線形補間し、正規化して返します（nlerp）。

<p>
slerpではなくnlerpにしているのは、ベイク済みサンプル間の補間が対象で、
隣接サンプルの角度差が1/60秒ぶんと小さく、この範囲では両者の差が
角速度のわずかなむらにしかならない一方、slerpは<code>acos</code>と<code>sin</code>を
固定小数点で評価する必要があり、毎フレームの経路には重すぎるためです。
</p>
<p>
内積が負の場合は<code class="paramref">to</code>の符号を反転してから補間します。
Quaternionはqと-qが同じ回転を表すため、これをしないと補間が
長い方の弧を通り、カメラが1フレームだけ逆回転して見えます。
</p>
<p>
<code class="paramref">t</code> が0のときは<code class="paramref">from</code>を、1のときは<code class="paramref">to</code>を、
正規化も符号の反転もせずそのまま返します（非単位Quaternionでも成功します）。
0と1の間では、成分ごとの補間を <code>from + RNE((to-from)*t)</code> の順で積だけ丸め、その結果を
<xref href="Omni.Logical.Quaternion.TryNormalize(Omni.Logical.Quaternion%40%2cOmni.Logical.Quaternion%40)" data-throw-if-not-resolved="false"></xref> で正規化します。積の丸めは成分あたり2^-127以内で、
正規化の段階の誤差は、補間した値に<xref href="Omni.Logical.Quaternion.TryNormalize(Omni.Logical.Quaternion%40%2cOmni.Logical.Quaternion%40)" data-throw-if-not-resolved="false"></xref>の誤差上限を当てはめたものです。
単位Quaternion同士では、補間した値の二乗和が0.5〜1になるため、正規化の段階の誤差は成分あたり約4.75*2^-96以内です。
</p>
<p>
次の場合は失敗します（resultはIdentity）。<code class="paramref">t</code>の範囲外以外の条件は、
単位Quaternion同士では起きず、成分が±2に近い極端な非単位Quaternionなどの場合です。
</p>
<ul><li><code class="paramref">t</code> が0〜1の範囲外のとき。</li><li>内積 <code>from・to</code> の4項の和が表現範囲（-2以上2未満）を超えるとき。</li><li>内積が負で、<code class="paramref">to</code>のいずれかの成分がMinValue（-2）のとき。符号を反転できません。</li><li>反転後の<code class="paramref">to</code>と<code class="paramref">from</code>の成分の差が、表現範囲を超えるとき。</li><li>補間した値が<xref href="Omni.Logical.Quaternion.TryNormalize(Omni.Logical.Quaternion%40%2cOmni.Logical.Quaternion%40)" data-throw-if-not-resolved="false"></xref>の失敗条件に当たるとき（二乗和が小さすぎる・大きすぎる場合など）。</li></ul>

```csharp
public static bool TryNlerp(in Quaternion from, in Quaternion to, in Scalar t, out Quaternion result)
```

#### 引数（Parameters）

`from` [Quaternion](Omni.Logical.Quaternion.md)

開始回転。

`to` [Quaternion](Omni.Logical.Quaternion.md)

終了回転。

`t` [Scalar](Omni.Logical.Scalar.md)

補間比率(0〜1)。範囲外は失敗します。

`result` [Quaternion](Omni.Logical.Quaternion.md)

補間結果。失敗時はIdentity。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Quaternion_TryNormalize_Omni_Logical_Quaternion__Omni_Logical_Quaternion__"></a> TryNormalize\(in Quaternion, out Quaternion\)

正規化を試みます。成分二乗和(X2+Y2+Z2+W2)を256ビットのアキュムレータで合成して、
一度だけ最近接偶数でScalar（小数部96ビット）へ丸め、その逆平方根
（<xref href="Omni.Logical.Scalar.TryReciprocalSqrt(Omni.Logical.Scalar%40%2cOmni.Logical.Scalar%40)" data-throw-if-not-resolved="false"></xref>）を係数として各成分に掛けます
（成分ごとに最近接偶数で丸めます）。丸めは、二乗和で1回、成分ごとに1回です。

<p>
係数がScalar（2^-96刻み）なので、正規化後の精度は回転成分の分解能（2^-126）より粗く、約2^-96で頭打ちになります。
二乗和Sが0.25〜4（長さが0.5〜2）の範囲では、厳密な q/|q| との成分ごとの絶対誤差は、入力の成分をq_iとして
|q_i|*(0.25*S^-1.5 + 4*max(1, 1/sqrt(S)) + 0.5*sqrt(S))*2^-96 + 2^-127 以内です
（二乗和の丸め（2^-97）が係数へ伝わる分、<xref href="Omni.Logical.Scalar.TryReciprocalSqrt(Omni.Logical.Scalar%40%2cOmni.Logical.Scalar%40)" data-throw-if-not-resolved="false"></xref>の誤差上限、成分の丸めから導いた上限です）。
単位Quaternion（S≈1）では、成分あたり約4.75*2^-96（約6×10^-29）以内です。
二乗和が小さいほど、二乗和を2^-96刻みに丸める相対誤差が大きくなるため、精度は落ちます。
</p>
<p>
次の場合は失敗します（resultはIdentity）。
</p>
<ul><li>二乗和が2^-97以下のとき。Scalarの分解能の半分以下でゼロに丸まるためで、全成分がゼロの場合を含みます（長さにして約2^-48.5以下）。</li><li>二乗和が丸めて、ちょうど1量子（2^-96）になるとき。<xref href="Omni.Logical.Scalar.TryReciprocalSqrt(Omni.Logical.Scalar%40%2cOmni.Logical.Scalar%40)" data-throw-if-not-resolved="false"></xref>がこの値で失敗するためです。</li><li>二乗和が8.0以上のとき。256ビットのアキュムレータが桁あふれします。単位Quaternionでは起きません。</li><li>結果の成分が表現範囲を超えるとき。</li></ul>

```csharp
public static bool TryNormalize(in Quaternion value, out Quaternion result)
```

#### 引数（Parameters）

`value` [Quaternion](Omni.Logical.Quaternion.md)

`result` [Quaternion](Omni.Logical.Quaternion.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Quaternion_TryRotate_Omni_Logical_Quaternion__Omni_Logical_Vector3__Omni_Logical_Vector3__"></a> TryRotate\(in Quaternion, in Vector3, out Vector3\)

単位Quaternionによる論理Vectorの回転を試みます（呼び出し側で正規化済みであることが
前提です。正規化はこのメソッドの責務ではありません）。
効率化されたQuaternion回転式 t = 2*cross(q.xyz, v)、v' = v + q.w*t + cross(q.xyz, t)
を使います。途中でUnity Quaternion・Matrix4x4への変換は一切行いません。

<p>
丸めは3か所です。t、q.w*t、cross(q.xyz, t) を、それぞれScalarへ最近接偶数で丸めます
（tとcrossの各項の積と差は、アキュムレータで厳密に合成してから一度だけ丸めます）。
q.w*t と cross は丸め済みのtから計算するため、tの丸めが伝わります。最後の加算は厳密です。
厳密な式の値との差は、各成分で 1 + 0.5*(|w| + |qa| + |qb|) 量子（1量子 = 2^-96）以内です。
qa、qbはその成分の外積に現れるQuaternionの2成分です。この上限は単位Quaternionでは最大でも約1.87量子で、
成分が±2に近い非単位Quaternionでは4量子に近づきます。
</p>
<p>
t、q.w*t、cross(q.xyz, t)、または部分和 v + q.w*t のどれかがScalarの範囲を超えると、
最終的な結果が表現できる場合でも失敗します。丸めの差が上の上限まで届くため、
厳密な値がこれらの範囲の端から上限以内にあるときも、範囲を超えて失敗することがあります。
</p>

```csharp
public static bool TryRotate(in Quaternion rotation, in Vector3 vector, out Vector3 result)
```

#### 引数（Parameters）

`rotation` [Quaternion](Omni.Logical.Quaternion.md)

`vector` [Vector3](Omni.Logical.Vector3.md)

`result` [Vector3](Omni.Logical.Vector3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Quaternion_TryToFloat4_System_Single__System_Single__System_Single__System_Single__"></a> TryToFloat4\(out float, out float, out float, out float\)

Unity描画境界向けの単精度4成分への変換を試みます。

```csharp
public bool TryToFloat4(out float x, out float y, out float z, out float w)
```

#### 引数（Parameters）

`x` [float](https://learn.microsoft.com/dotnet/api/system.single)

`y` [float](https://learn.microsoft.com/dotnet/api/system.single)

`z` [float](https://learn.microsoft.com/dotnet/api/system.single)

`w` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## 演算子（Operators）

### <a id="Omni_Logical_Quaternion_op_Equality_Omni_Logical_Quaternion_Omni_Logical_Quaternion_"></a> operator ==\(Quaternion, Quaternion\)

2つの値が等しい場合はtrueです。

```csharp
public static bool operator ==(Quaternion left, Quaternion right)
```

#### 引数（Parameters）

`left` [Quaternion](Omni.Logical.Quaternion.md)

`right` [Quaternion](Omni.Logical.Quaternion.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Quaternion_op_Inequality_Omni_Logical_Quaternion_Omni_Logical_Quaternion_"></a> operator \!=\(Quaternion, Quaternion\)

2つの値が異なる場合はtrueです。

```csharp
public static bool operator !=(Quaternion left, Quaternion right)
```

#### 引数（Parameters）

`left` [Quaternion](Omni.Logical.Quaternion.md)

`right` [Quaternion](Omni.Logical.Quaternion.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
