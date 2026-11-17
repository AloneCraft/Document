# <a id="Omni_RadialCamera"></a> Class RadialCamera

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

カメラに付与し、RadialGlobal 対数ワープのパラメータを保持するデータホルダです。
写像は Smooth Log（S = 1）だけで、曲線・S・線形半径の設定はありません（<xref href="Omni.RadialSettings" data-throw-if-not-resolved="false"></xref>）。
設定は論理 Near／Far Clip だけで、View Scale M は <code>Camera の Near ÷ nearClip</code> で決まります。
実際の適用は <xref href="Omni.RadialGlobalRenderSystem" data-throw-if-not-resolved="false"></xref> が
beginCameraRendering でカメラごとに、登録済み Renderer の MaterialPropertyBlock へ
書き込みます（旧: 本コンポーネントが Shader.SetGlobal* でグローバル設定）。
グローバルは SRP Batcher（UnityPerMaterial CBUFFER）に無視され、かつ複数カメラで
競合するため MaterialPropertyBlock 方式へ移行しています。

```csharp
public sealed class RadialCamera : MonoBehaviour
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[RadialCamera](Omni.RadialCamera.md)

## フィールド（Fields）

### <a id="Omni_RadialCamera_DefaultFarClip"></a> DefaultFarClip

論理 Far Clip の既定値です。表現できる最大値（Scalar.MaxValue、約3.96e28 m）で、実質的に無制限です。

```csharp
public static readonly Scalar DefaultFarClip
```

#### 値（Field Value）

 [Scalar](Omni.Logical.Scalar.md)

### <a id="Omni_RadialCamera_DefaultNearClip"></a> DefaultNearClip

論理 Near Clip の既定値です。Unity Camera の既定 Near Clip と揃えています。

```csharp
public static readonly Scalar DefaultNearClip
```

#### 値（Field Value）

 [Scalar](Omni.Logical.Scalar.md)

### <a id="Omni_RadialCamera_farClip"></a> farClip

論理座標上の Far Clip 距離です（単位は論理メートル）。ここより遠い対象は描きません。

<p>
対数ワープは論理 R〜∞ を有限の描画距離へ畳むため、放っておくと「どこまで見えるか」が
Unity 側の <xref href="UnityEngine.Camera.farClipPlane" data-throw-if-not-resolved="false"></xref> と、カリング側のハードコード上限という
誰も指定していない値で決まってしまいます。この値はその上限を明示的に置くためのものです。
</p>
<p>
2つの経路に効きます:

<ol><li>CPU側のシェル判定と、GPU変形後を包む保守Bounds。ここより遠い対象は
Radial固有の判定で非表示になります。</li><li>GPUの実クリップ far。<code>curve(farClip × M)</code> が収まるよう
カメラ単位の描画スコープ中だけ<xref href="UnityEngine.Camera.nearClipPlane" data-throw-if-not-resolved="false"></xref>／
<xref href="UnityEngine.Camera.farClipPlane" data-throw-if-not-resolved="false"></xref>と投影行列を同期し、描画後に完全復元します。</li></ol>
</p>

```csharp
public ScalarField farClip
```

#### 値（Field Value）

 [ScalarField](Omni.Logical.ScalarField.md)

### <a id="Omni_RadialCamera_nearClip"></a> nearClip

論理座標上の Near Clip 距離です（単位は論理メートル）。

<p>
Unity の <xref href="UnityEngine.Camera.nearClipPlane" data-throw-if-not-resolved="false"></xref> は<b>描画空間</b>の距離で、ユーザーが
Inspector で決めた値をそのまま使います（このコンポーネントは書き換えません）。一方この
<code>nearClip</code> は「その近クリップ面が論理空間で何メートルを表すか」です。両者の比が
そのまま View Scale (M) になります:
<code>M = Camera.nearClipPlane / nearClip</code>。
</p>
<p>
例えば Camera の Near Clip = 0.1 に対して <code>nearClip = 1e-9</code> なら、近クリップ面は
論理的に 1nm を表し M = 1e8 になります。値を小さくするほど近傍が拡大されるので、
<b>Camera の Near Clip を下げずに</b>ミクロな対象を描けます。単なる利便ではなく
深度精度に直結します。100nm を描くのに near を下げる方式では <code>far/near ≒ 3.0e9</code>
となり深度が破綻しますが、M=1e7 で拡大すれば near は 0.1 のままで
<code>far/near ≒ 2.8e3</code> に収まります。
</p>
<p>
Mはカーブへ渡す<b>前</b>の距離に掛かります（M-inside）。したがって S（= 1）は<b>描画単位</b>として
解釈され、曲がり始める論理距離は約 S/M となってMに追従します。外側
（カーブの結果へ後掛けし、Sを論理メートル固定にする）にはしません。外側だと
Mを上げても曲がり始めの論理距離が動かないため、極小スケールを見るためにMを大きくすると
見える範囲が全部ほぼ一様な拡大の範囲へ入り、対数圧縮が効かなくなります。
</p>
<p>
<b>この値は論理 Near 平面そのものです。</b>判定は放射距離ではなく、論理カメラ前方に
垂直な平面で行います:

<pre><code class="lang-csharp">logicalViewDepth = dot(P - C, F)
可視条件         = logicalViewDepth &gt;= nearClip</code></pre>

実際のクリップを行うのは Unity の投影行列です。Smooth Log の写像は Near 近傍でも恒等ではないため、
論理の Near 平面は単一のハードウェア平面では表現できません。
<xref href="Omni.Logical.NearClipMath.TryGetSafeRenderNear(Omni.RadialSettings%40%2cOmni.Logical.Scalar%40%2cSystem.Single%2cSystem.Single%40)" data-throw-if-not-resolved="false"></xref> が返す「四隅で過剰クリップしない」
値へ倒します。この場合、画面中央のクリップ位置がこの値よりわずかに手前へずれます
（量は Inspector の Center Under-clip に出ます）。
</p>

```csharp
public ScalarField nearClip
```

#### 値（Field Value）

 [ScalarField](Omni.Logical.ScalarField.md)

## プロパティ（Properties）

### <a id="Omni_RadialCamera_EffectiveFarClip"></a> EffectiveFarClip

常に正で有限な論理 Far Clip です。不正値は既定値へ丸めます。

```csharp
public Scalar EffectiveFarClip { get; }
```

#### 値（Property Value）

 [Scalar](Omni.Logical.Scalar.md)

### <a id="Omni_RadialCamera_EffectiveLog2ViewScale"></a> EffectiveLog2ViewScale

log2(View Scale) です。<code>RadialWarp.hlsl</code> の <code>log2ViewScale</code> 引数と
同じfloat値になります。Mそのものを一度も実体化せず、
<code>log2(Cameraの設定Near) - log2(nearClip)</code> という差で直接求めます。
描画スコープで同期したhardware nearは写像の出力なので、入力Mへ再利用しません。

```csharp
public float EffectiveLog2ViewScale { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_RadialCamera_EffectiveNearClip"></a> EffectiveNearClip

常に正で有限な論理 Near Clip です。不正値は既定値へ丸めます。

```csharp
public Scalar EffectiveNearClip { get; }
```

#### 値（Property Value）

 [Scalar](Omni.Logical.Scalar.md)

## メソッド（Methods）

### <a id="Omni_RadialCamera_FindAll_System_Collections_Generic_List_Omni_RadialCamera__UnityEngine_FindObjectsInactive_"></a> FindAll\(List<RadialCamera\>, FindObjectsInactive\)

読み込み済みSceneの<xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref>を、Cameraを経由して<code class="paramref">results</code>へ追加します。

```csharp
public static void FindAll(List<RadialCamera> results, FindObjectsInactive inactive = FindObjectsInactive.Exclude)
```

#### 引数（Parameters）

`results` [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[RadialCamera](Omni.RadialCamera.md)\>

追加先。呼び出し時にはクリアしません。

`inactive` FindObjectsInactive

非アクティブなGameObjectを含めるか。

#### 補足（Remarks）

<code>FindObjectsByType&lt;RadialCamera&gt;</code>は使いません。Omni ManagerがEditモードで自動付与した
RadialCameraは<xref href="UnityEngine.HideFlags.DontSaveInEditor" data-throw-if-not-resolved="false"></xref>を持ち、FindObjectsByTypeはそのような
コンポーネントを返さないためです（Resources.FindObjectsOfTypeAllでは見つかります）。
Camera自体は通常のオブジェクトなので、Cameraを列挙して付いているRadialCameraを取れば見落としません。
呼び出し側の絞り込み（有効・Scene・Preview Sceneの除外）は変わりません。

### <a id="Omni_RadialCamera_FindAny_UnityEngine_FindObjectsInactive_"></a> FindAny\(FindObjectsInactive\)

<xref href="Omni.RadialCamera.FindAll(System.Collections.Generic.List%7bOmni.RadialCamera%7d%2cUnityEngine.FindObjectsInactive)" data-throw-if-not-resolved="false"></xref>と同じ範囲で、最初に見つかったRadialCameraを返します。無ければnullです。

```csharp
public static RadialCamera FindAny(FindObjectsInactive inactive = FindObjectsInactive.Exclude)
```

#### 引数（Parameters）

`inactive` FindObjectsInactive

#### 戻り値（Returns）

 [RadialCamera](Omni.RadialCamera.md)

### <a id="Omni_RadialCamera_GetOrAdd_UnityEngine_Camera_"></a> GetOrAdd\(Camera\)

指定カメラのドライバを返します。無ければ追加します。
カーブはカメラ1台につき1つという前提を保つための入口です。

```csharp
public static RadialCamera GetOrAdd(Camera camera)
```

#### 引数（Parameters）

`camera` Camera

対象のカメラ。nullなら何もしません。

#### 戻り値（Returns）

 [RadialCamera](Omni.RadialCamera.md)

取得または追加したドライバ。カメラがnullならnull。

### <a id="Omni_RadialCamera_SetIdentityViewScale"></a> SetIdentityViewScale\(\)

カーブ入力前の追加倍率を等倍（M=1）にします。
論理 Near Clip を Camera の Near Clip 面へ一致させます。

```csharp
public void SetIdentityViewScale()
```

#### 補足（Remarks）

診断ツールのように「Mによる追加の入力倍率を掛けず、ワープカーブ自体を見たい」場面用です。
M は <code>Camera.nearClipPlane / nearClip</code> なので、等倍にする式を呼び出し側へ
散らさずに済むよう入口を1つにしています。写像はM=1でも
恒等変換にはならず、原点近傍の傾きは<code>1/ln(2)</code>のままです。

### <a id="Omni_RadialCamera_SetViewScale_System_Single_"></a> SetViewScale\(float\)

View Scale（M）を指定します。論理 Near Clip を <code>Camera の Near ÷ M</code> にします。

```csharp
public void SetViewScale(float viewScale)
```

#### 引数（Parameters）

`viewScale` [float](https://learn.microsoft.com/dotnet/api/system.single)

正で有限な M。そうでなければ等倍（M=1）にします。

#### 補足（Remarks）

写像の曲線は1つだけ（S = 1）なので、圧縮の強さ（曲がり始める論理距離 約 1/M）は M で変えます。
旧来の「S を小さくして強く圧縮する」構成は、S' = 1・M' = M ÷ S で同じ形の曲線になります
（描画空間の長さが 1/S 倍になるだけ）。検証や診断の入口です。
