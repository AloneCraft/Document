# <a id="Omni_RadialShellPolicy"></a> Class RadialShellPolicy

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

Radial near/farシェルのfail-open判定規約です。
SaturnシーンのMesoリングBRG Jobは、距離算出に失敗したセルを
<xref href="Omni.RadialShellRelation.Indeterminate" data-throw-if-not-resolved="false"></xref>として本規約へ渡します。

```csharp
public static class RadialShellPolicy
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialShellPolicy](Omni.RadialShellPolicy.md)

## メソッド（Methods）

### <a id="Omni_RadialShellPolicy_Compare_Omni_Logical_Scalar__Omni_Logical_Scalar__"></a> Compare\(in Scalar, in Scalar\)

2つの固定小数点論理距離を比較します。

```csharp
public static RadialShellRelation Compare(in Scalar left, in Scalar right)
```

#### 引数（Parameters）

`left` [Scalar](Omni.Logical.Scalar.md)

比較する左辺の有限論理距離です。

`right` [Scalar](Omni.Logical.Scalar.md)

比較する右辺の有限論理距離です。

#### 戻り値（Returns）

 [RadialShellRelation](Omni.RadialShellRelation.md)

固定小数点の順序に対応する関係です。

### <a id="Omni_RadialShellPolicy_FromComparison_System_Boolean_System_Int32_"></a> FromComparison\(bool, int\)

比較演算の成功可否と比較値を公開契約の関係値へ変換します。

```csharp
public static RadialShellRelation FromComparison(bool comparisonSucceeded, int comparison)
```

#### 引数（Parameters）

`comparisonSucceeded` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

安全な比較が完了した場合はtrueです。

`comparison` [int](https://learn.microsoft.com/dotnet/api/system.int32)

left-rightの符号です。負/0/正以外の意味は持ちません。

#### 戻り値（Returns）

 [RadialShellRelation](Omni.RadialShellRelation.md)

失敗時は必ずIndeterminate、成功時は符号に対応する関係です。

### <a id="Omni_RadialShellPolicy_IsFullyBeforeNear_Omni_RadialShellRelation_"></a> IsFullyBeforeNear\(RadialShellRelation\)

AABBの最遠距離がnearより完全に手前かを返します。
EqualとIndeterminateは境界欠落を避けるためfalseです。

```csharp
public static bool IsFullyBeforeNear(RadialShellRelation maximumDistanceToNear)
```

#### 引数（Parameters）

`maximumDistanceToNear` [RadialShellRelation](Omni.RadialShellRelation.md)

maxDistanceとnearの比較結果です。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

Lessのときだけtrueです。

### <a id="Omni_RadialShellPolicy_IsFullyBeyondFar_Omni_RadialShellRelation_"></a> IsFullyBeyondFar\(RadialShellRelation\)

AABBの最短距離がfarより完全に奥かを返します。
EqualとIndeterminateは境界欠落を避けるためfalseです。

```csharp
public static bool IsFullyBeyondFar(RadialShellRelation minimumDistanceToFar)
```

#### 引数（Parameters）

`minimumDistanceToFar` [RadialShellRelation](Omni.RadialShellRelation.md)

minDistanceとfarの比較結果です。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

Greaterのときだけtrueです。

### <a id="Omni_RadialShellPolicy_ShouldRemainVisible_Omni_RadialShellRelation_Omni_RadialShellRelation_System_Boolean_"></a> ShouldRemainVisible\(RadialShellRelation, RadialShellRelation, bool\)

near/farシェルに対してセルを描画し続けるべきかを返します。
Indeterminateは常に可視側です。falseを返すのは、near手前またはfar奥が
比較成功済みで完全に証明できた場合だけです。

```csharp
public static bool ShouldRemainVisible(RadialShellRelation maximumDistanceToNear, RadialShellRelation minimumDistanceToFar, bool hasFarClip)
```

#### 引数（Parameters）

`maximumDistanceToNear` [RadialShellRelation](Omni.RadialShellRelation.md)

maxDistanceとnearの比較結果です。

`minimumDistanceToFar` [RadialShellRelation](Omni.RadialShellRelation.md)

minDistanceとfarの比較結果です。

`hasFarClip` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

論理farを適用する場合はtrueです。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

BRGの可視IDへ残すべきならtrueです。

### <a id="Omni_RadialShellPolicy_TryClassifyBounds_Omni_Logical_Position3__Omni_Logical_Aabb__Omni_Logical_Scalar__Omni_Logical_Scalar__System_Boolean_Omni_RadialShellRelation__Omni_RadialShellRelation__"></a> TryClassifyBounds\(in Position3, in Aabb, in Scalar, in Scalar, bool, out RadialShellRelation, out RadialShellRelation\)

Logical AABBの距離範囲をnear/farの放射シェルと比較します。
<code class="paramref">origin</code>は描画cameraと同じ意味のLogical eye、
<code class="paramref">far</code>はそのeyeを中心とする到達半径として正しさを証明済みの値だけを
渡します。通常の透視far平面を無条件に渡してはいけません。

```csharp
public static bool TryClassifyBounds(in Position3 origin, in Aabb bounds, in Scalar near, in Scalar far, bool hasFarClip, out RadialShellRelation maximumDistanceToNear, out RadialShellRelation minimumDistanceToFar)
```

#### 引数（Parameters）

`origin` [Position3](Omni.Logical.Position3.md)

距離を測るLogical eyeです。Saturnセルのfloat Transformでは代用しません。

`bounds` [Aabb](Omni.Logical.Aabb.md)

時間窓の移動量と粒子半径まで含む保守的なLogical AABBです。

`near` [Scalar](Omni.Logical.Scalar.md)

正のnear放射境界です。0以下なら判定不能として可視側へ倒します。

`far` [Scalar](Omni.Logical.Scalar.md)

正のfar放射境界です。<code class="paramref">hasFarClip</code>がfalseなら使いません。

`hasFarClip` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

farがeye中心の保守的な到達半径として証明済みならtrueです。

`maximumDistanceToNear` [RadialShellRelation](Omni.RadialShellRelation.md)

AABB最遠距離とnearの関係です。失敗時はIndeterminateです。

`minimumDistanceToFar` [RadialShellRelation](Omni.RadialShellRelation.md)

AABB最短距離とfarの関係です。far未使用・失敗時はIndeterminateです。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

距離範囲と必要な境界を安全に算出できた場合はtrueです。

### <a id="Omni_RadialShellPolicy_TryClassifyBounds_Omni_Rendering_Radial_ViewSnapshot__Omni_Logical_Aabb__Omni_RadialShellRelation__Omni_RadialShellRelation__"></a> TryClassifyBounds\(in ViewSnapshot, in Aabb, out RadialShellRelation, out RadialShellRelation\)

自己中心RadialビューのLogical AABBをnear/farシェルと比較します。
Observerや不完全Snapshotは、非線形の逆写像領域を通常シェルで表せないためfalseを返します。

```csharp
public static bool TryClassifyBounds(in ViewSnapshot snapshot, in Aabb bounds, out RadialShellRelation maximumDistanceToNear, out RadialShellRelation minimumDistanceToFar)
```

#### 引数（Parameters）

`snapshot` [ViewSnapshot](Omni.Rendering.Radial.ViewSnapshot.md)

現フレームの不変Radialビュー状態です。stale値を渡してはいけません。

`bounds` [Aabb](Omni.Logical.Aabb.md)

時間窓全体を含むLogical AABBです。

`maximumDistanceToNear` [RadialShellRelation](Omni.RadialShellRelation.md)

AABB最遠距離とnearの関係です。失敗時はIndeterminateです。

`minimumDistanceToFar` [RadialShellRelation](Omni.RadialShellRelation.md)

AABB最短距離とfarの関係です。失敗時はIndeterminateです。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

自己中心Radialのシェル判定入力が完全に利用可能な場合はtrueです。
