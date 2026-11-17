# <a id="Omni_Logical"></a> Namespace Omni.Logical

### クラス（Classes）

 [ActiveCameraResolver](Omni.Logical.ActiveCameraResolver.md)

 [BakeMixerBehaviour](Omni.Logical.BakeMixerBehaviour.md)

 [BakePlaybackController](Omni.Logical.BakePlaybackController.md)

ベイク再生とリアルタイム経路の切り替えを、シーケンス全体で1か所に集約するコンポーネントです。

<p>
<code>PlayableDirector</code>と同じGameObjectに付けます。ベイクトラックのミキサーは
<code>CreateTrackMixer</code>に渡されるGameObjectからこのコンポーネントを見つけ、
「照合すべきGUID・ハッシュ」を受け取り、「今フレーム適用できたか」を報告します。
</p>
<p>
演出側（Director）はこの1点だけを見てフォールバックを判断できます。トラックごとに
判定が散らばると、カメラだけベイク・光源だけリアルタイムのような食い違った絵が
生まれるためです。
</p>

 [FiniteSkinnedPresentation](Omni.Logical.FiniteSkinnedPresentation.md)

Asteria の runtime actor root など、巨大な Unity 祖先を持たない専用骨格だけを
有限 native 空間で更新する明示 opt-in です。Logical raw 姿勢は変更しません。

 [LightBakeMixerBehaviour](Omni.Logical.LightBakeMixerBehaviour.md)

 [LightBakeTrack](Omni.Logical.LightBakeTrack.md)

ベイク済みLogical回転で<xref href="UnityEngine.Light" data-throw-if-not-resolved="false"></xref>を駆動するトラックです。

<p>
光源の姿勢はカメラの向きから毎フレーム導出していましたが、演出が固定なら
これも時刻の純関数です。焼いてしまえば、カメラのワールド論理姿勢を解決する
処理そのものが再生時から消えます。
</p>

 [Math](Omni.Logical.Math.md)

 [NavigationBounds](Omni.Logical.NavigationBounds.md)

Rendererを持たない対象（頂点をGPUで生成する地形など）に付けて、Scene Viewの接近・飛行の基準になる大きさを
Inspectorで宣言するcomponentです。実装は<xref href="Omni.Logical.INavigationBoundsSource" data-throw-if-not-resolved="false"></xref>の標準版です。
実行時の表示やLogical Transformには影響しません。

 [NearClipMath](Omni.Logical.NearClipMath.md)

 [OmniCullingDebug](Omni.Logical.OmniCullingDebug.md)

 [PhysicalSafety](Omni.Logical.PhysicalSafety.md)

 [PoseBake](Omni.Logical.PoseBake.md)

 [PoseBakeChannel](Omni.Logical.PoseBakeChannel.md)

1つの対象（カメラ、主光源など）についての時系列サンプル列です。

<p>
Logical値はサンプルごとの<xref href="Omni.Logical.ScalarField" data-throw-if-not-resolved="false"></xref>ではなく、チャンネル単位の
平坦な<code>ulong</code>配列（SoA）へ詰めます。<xref href="Omni.Logical.ScalarField" data-throw-if-not-resolved="false"></xref>は
<code>OnBeforeSerialize</code>のたびに<code>ulong[LimbCount]</code>を新規確保するため、
9000サンプル×11スカラーでは10万個規模の小配列が生まれます。平坦配列なら
チャンネルあたり数本で済み、読み出しも<xref href="System.ReadOnlySpan%601" data-throw-if-not-resolved="false"></xref>経由で
割り当てなしに行えます。加えてUnityは整数配列をYAMLへ16進ブロブ1行で書くため、
アセットの行数も桁違いに小さくなります。
</p>
<p>
空間値をfloatやdoubleへ落とした形では一切保存しません。保存されるのは
<xref href="Omni.Logical.IntRaw" data-throw-if-not-resolved="false"></xref>のraw limbそのものです。画角・クリップ・光の強さ・色は
空間量ではないのでfloatのまま持ちます。
</p>

 [PoseBakeClip](Omni.Logical.PoseBakeClip.md)

ベイク済みLogical姿勢を1区間ぶん再生するクリップです。

<p>
クリップ自体はサンプルを持たず、シーケンス全体で1つの<xref href="Omni.Logical.PoseBake" data-throw-if-not-resolved="false"></xref>を
指します。ショットごとにサンプル列を分割すると、境界でサンプルが二重に必要になり、
クリップを動かすたびにベイク全体を作り直すことになるためです。クリップは
「シーケンス時刻のこの区間を、このチャンネルで駆動する」ことだけを持ちます。
</p>

 [PoseBakeClipBehaviour](Omni.Logical.PoseBakeClipBehaviour.md)

 [PoseBakeMixerBehaviour](Omni.Logical.PoseBakeMixerBehaviour.md)

 [PoseBakeSampler](Omni.Logical.PoseBakeSampler.md)

 [PoseBakeTrack](Omni.Logical.PoseBakeTrack.md)

ベイク済みLogical姿勢で<xref href="Omni.Logical.Transform" data-throw-if-not-resolved="false"></xref>を駆動するトラックです。

<p>
Timeline標準のAnimationTrackは使えません。あちらはUnity Transformを直接書くため、
「LogicalTransformがTransformの唯一の書き手」という不変条件を壊し、
巨大座標では姿勢がfloatへ丸められて論理値と食い違うためです。
</p>

 [Precision](Omni.Logical.Precision.md)

 [RadialRigidAnchor](Omni.Logical.RadialRigidAnchor.md)

同じGameObjectのRendererを、中心アンカー基準のRadial剛体として描画します。

 [RenderProxyRegistry](Omni.Logical.RenderProxyRegistry.md)

 [ScalarFieldDrawer](Omni.Logical.ScalarFieldDrawer.md)

<xref href="Omni.Logical.ScalarField" data-throw-if-not-resolved="false"></xref>のInspector表示です。

<p>
既定のインスペクタは内部のlimb配列(<code>ulong[]</code>)をそのまま表示してしまい編集できません。
<xref href="Omni.Logical.TransformEditor" data-throw-if-not-resolved="false"></xref>と同様に、<xref href="Omni.Logical.Scalar.ToString" data-throw-if-not-resolved="false"></xref>/
共通の論理数式評価器で編集します。式自体は保存せず評価した数値だけを保存します。
ラベルは<xref href="Omni.Logical.ScalarDragHandle" data-throw-if-not-resolved="false"></xref>により標準Transformと同じ
「ラベルをドラッグして値をスクラブ」操作にも対応しています。
</p>

 [ScaleSweep](Omni.Logical.ScaleSweep.md)

 [Transform](Omni.Logical.Transform.md)

Logical位置・回転・符号付きXYZ Scaleを固定小数点で保持するRuntimeコンポーネントです。
Unity Transformは描画・編集境界の有限プロキシであり、空間の正本にはなりません。
親子合成、Bounds、距離判定はすべてLogical型で行います。

 [TransformEditor](Omni.Logical.TransformEditor.md)

<xref href="Omni.Logical.Transform" data-throw-if-not-resolved="false"></xref> のインスペクタです。

<p>
既定のインスペクタは固定小数点の生limb配列(<code>ulong[]</code>)をそのまま表示してしまい
編集できません。標準Transformと同じ「Position/Rotation/ScaleがそれぞれX/Y/Zの1行」
レイアウトで表示します。
</p>
<p>
Position/Scaleは<xref href="Omni.Logical.Scalar.ToString" data-throw-if-not-resolved="false"></xref>/<xref href="Omni.Logical.Scalar.TryParse(System.String%2cOmni.Logical.Scalar%40)" data-throw-if-not-resolved="false"></xref>
を使い、Logical正本のまま任意精度10進文字列として編集します。
Rotationは向きの精度要件がPosition/Scaleほど厳しくないため、
標準の<code>EditorGUILayout.Vector3Field(string, global::UnityEngine.Vector3)</code>(float精度)をそのまま使います。
</p>
<p>
Position/ScaleのX/Y/Zラベルは、<xref href="Omni.Logical.ScalarDragHandle" data-throw-if-not-resolved="false"></xref>により標準Transformと
同じ「ラベルをドラッグして値をスクラブ」操作にも対応しています。
</p>

 [TransformHierarchy](Omni.Logical.TransformHierarchy.md)

 [TransformReadOnlyEditor](Omni.Logical.TransformReadOnlyEditor.md)

LogicalOriginalTransformなどの通常Transform編集をUnity標準Inspectorへ委譲し、
LogicalTransformの出力先だけを読み取り専用にします。

 [WarpCameraSelection](Omni.Logical.WarpCameraSelection.md)

### 構造体（Structs）

 [Aabb](Omni.Logical.Aabb.md)

Logicalワールド軸に沿ったAABBです。

 [BakePlaybackController.ChannelState](Omni.Logical.BakePlaybackController.ChannelState.md)

1チャンネルぶんの直近の状態です。

 [DetachResult](Omni.Logical.DetachResult.md)

Detachの状態と診断メッセージを返す不変値です。

 [IntRaw](Omni.Logical.IntRaw.md)

符号付き<xref href="Omni.Logical.Precision.TotalBits" data-throw-if-not-resolved="false"></xref>ビット2の補数整数です。
64ビットlimbを<xref href="Omni.Logical.Precision.LimbCount" data-throw-if-not-resolved="false"></xref>本並べて格納します。
Limb0が最下位64ビット、最上位limbのbit63が符号ビットです。
Scale系の型（<xref href="Omni.Logical.Scalar" data-throw-if-not-resolved="false"></xref>等）の生表現として使う共通の整数演算基盤です。
Silent Wraparound / Silent Clampは行わず、Overflowが起き得る演算はすべてTry APIです。

 [IntRaw128](Omni.Logical.IntRaw128.md)

符号付き128ビット2の補数整数です（回転成分<xref href="Omni.Logical.RotationScalar" data-throw-if-not-resolved="false"></xref>の生表現）。
64ビットlimbを<xref href="Omni.Logical.IntRaw128.LimbCount" data-throw-if-not-resolved="false"></xref>本並べて格納します。
Limb0が最下位64ビット、最上位limbのbit63が符号ビットです。
演算は<xref href="Omni.Logical.IntRaw" data-throw-if-not-resolved="false"></xref>（<xref href="Omni.Logical.Scalar" data-throw-if-not-resolved="false"></xref>の生表現）を128ビットへ写したもので、
片方を直したらもう片方も直します。除算・平方根・浮動小数点や10進との変換は持たず、
<xref href="Omni.Logical.IntRaw128.Widen" data-throw-if-not-resolved="false"></xref>で<xref href="Omni.Logical.IntRaw" data-throw-if-not-resolved="false"></xref>へ広げてそちらの演算を使い、<xref href="Omni.Logical.IntRaw128.TryNarrow(Omni.Logical.IntRaw%40%2cOmni.Logical.IntRaw128%40)" data-throw-if-not-resolved="false"></xref>で戻します。
Silent Wraparound / Silent Clampは行わず、Overflowが起き得る演算はすべてTry APIです。

 [Matrix3x3](Omni.Logical.Matrix3x3.md)

9つの<xref href="Omni.Logical.Scalar" data-throw-if-not-resolved="false"></xref>で構成される高精度3x3行列です。論理親子合成の
World Basisキャッシュ（回転・非一様Scale・Shearを含み得る合成済み行列）として使います。
行列×ベクトル・行列×行列の各成分は、LogicalWideIntアキュムレータで複数項を合成してから
一度だけ丸めます（個々の積を先に丸めてから合成する誤差の蓄積を避けるため）。

 [OmniCullingRange](Omni.Logical.OmniCullingRange.md)

第1層が実際に使ったカリング範囲です。描画空間のnear/farと、それを逆写像した実距離を
並べて持ちます。「実距離の下限が跳ね上がって手前を全部刈っている」ような状態を
数値で読めるようにするためのものです。

 [OmniEyeOverride](Omni.Logical.OmniEyeOverride.md)

そのフレームにカメラの目（<xref href="UnityEngine.Camera.worldToCameraMatrix" data-throw-if-not-resolved="false"></xref>）をワープ中心基準へ
上書きしたかどうかと、その判断材料です。

<p>
自己中心モードでこの上書きが誤って適用されると、目とワープ中心が別々の座標系で解決されて
食い違い、本来ゼロであるべき相対位置が非ゼロになって画面が変形します。この構造体は
「目とワープ中心の距離」を1行で読めるようにし、変形が残ったときに「まだ乖離があるのか」
「乖離0なのに崩れているのか（別の既知問題）」を推測せず切り分けるためのものです。
<xref href="Omni.Logical.OmniCullingDebug.NoteCullingMatrix(UnityEngine.Camera%2cUnityEngine.Matrix4x4%40%2cSystem.String)" data-throw-if-not-resolved="false"></xref>と同じ理由で、<b>適用した時点で</b>記録します。
</p>

 [OmniNearClip](Omni.Logical.OmniNearClip.md)

そのフレームにカメラへ適用した論理 Near Clip の実値と、その決め方です。

<p>
「手前が切れすぎる／切れなさすぎる」の切り分けには、論理 Near（設定値）だけでなく
<b>実際に投影行列へ入った描画空間 near</b> と、それが厳密な平面だったのか保守的な
近似だったのかが要ります。<xref href="Omni.Logical.OmniCullingDebug.NoteCullingMatrix(UnityEngine.Camera%2cUnityEngine.Matrix4x4%40%2cSystem.String)" data-throw-if-not-resolved="false"></xref> と同じ理由で、
描画後に <xref href="UnityEngine.Camera.projectionMatrix" data-throw-if-not-resolved="false"></xref> を読み直しても復元できない情報
（恒等領域だったので<b>上書きしなかった</b>、など）を含むため、<b>決めた時点で</b>記録します。
</p>

 [OmniProjectionClip](Omni.Logical.OmniProjectionClip.md)

CameraへFar Clip拡張を判断した時点の入力と適用値です。

 [OmniWarpMode](Omni.Logical.OmniWarpMode.md)

そのフレームにカメラへ適用したワープ経路と、恒等（ワープなし）を選んだ判断材料です。

<p>
「互換性非表示」が跳ね上がるときの原因はほぼ恒等分岐ですが、恒等を選ぶ3条件
（ワープ全体の有効／ワープ元ドライバの解決／平行投影）はどれも描画後に読み直しても
当時の値を復元できません。<xref href="Omni.Logical.OmniCullingDebug.NoteCullingMatrix(UnityEngine.Camera%2cUnityEngine.Matrix4x4%40%2cSystem.String)" data-throw-if-not-resolved="false"></xref> と同じ理由で、
<b>決めた時点で</b>記録します。
</p>

 [PhysicalSafetyResult](Omni.Logical.PhysicalSafetyResult.md)

論理AABBをUnity標準空間へ置けるか判定した結果です。

 [Position3](Omni.Logical.Position3.md)

論理Position用途の<xref href="Omni.Logical.Vector3" data-throw-if-not-resolved="false"></xref>ラッパーです。Position専用の意味を持たせ、
単なる差分・方向ベクトルとしての<xref href="Omni.Logical.Vector3" data-throw-if-not-resolved="false"></xref>と区別するために
独立した型として定義します。

 [Quaternion](Omni.Logical.Quaternion.md)

<xref href="Omni.Logical.RotationScalar" data-throw-if-not-resolved="false"></xref>を4成分(X,Y,Z,W)持つ高精度Quaternionです。
乗算は各成分の4項の積を256ビットのアキュムレータで全て合成してから一度だけ丸めます
（個々の積を先に丸めて足す誤差の蓄積を避けるため）。
正規化・nlerp・ベクトルの回転は複数の段に分かれ、段ごとに丸めます。
丸めの回数と誤差の上限は各演算の説明にあります（正規化は係数をScalar（2^-96刻み）で持つため、
成分の精度が約2^-96で頭打ちになり、単位Quaternionによるベクトルの回転は成分あたり最大約1.9量子の誤差です。
非単位Quaternionでは<xref href="Omni.Logical.Quaternion.TryRotate(Omni.Logical.Quaternion%40%2cOmni.Logical.Vector3%40%2cOmni.Logical.Vector3%40)" data-throw-if-not-resolved="false"></xref>の説明のとおり上限が大きくなり、成分が±2に近いと4量子に近づきます）。
論理Positionの回転でも、途中でUnity Quaternion/Matrix4x4へ変換しません。

 [RenderPose](Omni.Logical.RenderPose.md)

LogicalTransformまたは通常Transformから解決する描画用Logicalワールド姿勢です。
PositionとBasisだけを空間値の正本とし、浮動小数の残差は保持しません。

 [RenderProxyDiagnostics](Omni.Logical.RenderProxyDiagnostics.md)

有限描画プロキシの現在状態です。プロキシは「隠す仕組み」ではなく「描く仕組み」なので、
対象が見えないときは<b>プロキシが実際に描かれているか</b>を確認する必要があります。

 [RotationScalar](Omni.Logical.RotationScalar.md)

回転成分用の固定小数点数（Q1.126、128ビット符号付き2の補数）です。
整数部1ビット・小数部<xref href="Omni.Logical.Precision.RotationFractionalBits" data-throw-if-not-resolved="false"></xref>ビットで、
数値 = SignedRawInteger / 2^RotationFractionalBits、範囲は -2〜2 - 2^-RotationFractionalBits です。
<xref href="Omni.Logical.Quaternion" data-throw-if-not-resolved="false"></xref>の各成分として使います。
クォータニオン成分は常に -1〜1 に収まるため、整数部を増やしても無駄になるだけです。
生表現は<xref href="Omni.Logical.Scalar" data-throw-if-not-resolved="false"></xref>（位置・長さ）と別の128ビット型（<xref href="Omni.Logical.IntRaw128" data-throw-if-not-resolved="false"></xref>）で、
位置を192ビットへ広げても回転は128ビットのままにします（2026-10-05 のユーザーの判断: 保存した回転成分の量子化が位置に
与える誤差は距離 × 約2×10^-38 で、速さと保存値を優先する）。回転同士の演算は128ビット、位置との積は192ビットへ広げて計算します。
ただし正規化と補間（nlerp）は係数をScalar（2^-96刻み）で持つため、それを経た成分の誤差は、単位Quaternionでは導出した上限で
約4.75×2^-96（約6×10^-29）以内で（上限の式は<xref href="Omni.Logical.Quaternion.TryNormalize(Omni.Logical.Quaternion%40%2cOmni.Logical.Quaternion%40)" data-throw-if-not-resolved="false"></xref>にあります）、
その回転が位置に与える誤差は距離 × 10^-28 の桁以下になります。
Silent Wraparound / Silent Clampは行わず、Overflowが起き得る演算はすべてTry APIです。

 [Scalar](Omni.Logical.Scalar.md)

位置・スケール用の固定小数点数（符号付き2の補数）です。
総ビット数は<xref href="Omni.Logical.Precision.TotalBits" data-throw-if-not-resolved="false"></xref>、小数部は
<xref href="Omni.Logical.Precision.FractionalBits" data-throw-if-not-resolved="false"></xref>で、数値 = SignedRawInteger / 2^FractionalBits、
範囲は概ね ±2^<xref href="Omni.Logical.Precision.IntegerBits" data-throw-if-not-resolved="false"></xref> です。
構成はQ95.96（192ビット）へ固定されています。Omniの論理Position/Scaleで使う
共通Scalar型です（Position用途の意味の分離は<xref href="Omni.Logical.Position3" data-throw-if-not-resolved="false"></xref>で行い、
Scaleはこの型を直接3成分（<xref href="Omni.Logical.Vector3" data-throw-if-not-resolved="false"></xref>）で使います）。
Silent Wraparound / Silent Clampは行わず、Overflowが起き得る演算はすべてTry APIです。

 [ScalarField](Omni.Logical.ScalarField.md)

<xref href="Omni.Logical.Scalar" data-throw-if-not-resolved="false"></xref>をUnityの<xref href="UnityEngine.SerializeField" data-throw-if-not-resolved="false"></xref>で直接保持できるようにする
シリアライズ用ラッパーです。

<p>
<xref href="Omni.Logical.Scalar" data-throw-if-not-resolved="false"></xref>自体は<code>readonly struct</code>で書き込み可能フィールドを持たないため
Unityの標準シリアライザでは扱えません。このラッパーは<xref href="Omni.Logical.IntRaw.ToLimbArray" data-throw-if-not-resolved="false"></xref>/
<xref href="Omni.Logical.IntRaw.FromSerializedLimbs(System.UInt64%5b%5d)" data-throw-if-not-resolved="false"></xref>を介して、シリアライズ時にlimb配列へパックし、
デシリアライズ時に<xref href="Omni.Logical.Scalar" data-throw-if-not-resolved="false"></xref>へ復元します（旧形式Q95.32の2 limbも同じ数値として読みます）。
利用側は暗黙変換で通常の<xref href="Omni.Logical.Scalar" data-throw-if-not-resolved="false"></xref>と同様に読み書きできます。
</p>

 [SceneViewRenderContext](Omni.Logical.SceneViewRenderContext.md)

1台のScene Viewが描画中に使う仮想論理視点です。
Editor側がカメラ単位で供給し、Runtimeの描画処理はLogicalPivotを正本として
オブジェクト相対座標を作ります。

 [Vector3](Omni.Logical.Vector3.md)

<xref href="Omni.Logical.Scalar" data-throw-if-not-resolved="false"></xref>を3成分持つ共通数学Vectorです。Omniの論理
Position/Scaleの基礎になります（Position用途の意味の分離は<xref href="Omni.Logical.Position3" data-throw-if-not-resolved="false"></xref>で
行い、Scaleはこの型を直接使います）。

 [WideInt](Omni.Logical.WideInt.md)

符号付き<xref href="Omni.Logical.Precision.WideBits" data-throw-if-not-resolved="false"></xref>ビット2の補数整数です。
64ビットlimbを<xref href="Omni.Logical.Precision.WideLimbCount" data-throw-if-not-resolved="false"></xref>本並べて格納します。
Scale系の乗算・Quaternion合成で使う中間Accumulatorです
（<xref href="Omni.Logical.IntRaw" data-throw-if-not-resolved="false"></xref>同士の積は最大でも 2*TotalBits-1 ビットで厳密に表現できるため、
倍幅は単一の積に加えて複数項の合成にも十分なheadroomを持ちます）。
Silent Wraparound / Silent Clampは行わず、Overflowが起き得る演算はすべてTry APIです。

 [WideInt256](Omni.Logical.WideInt256.md)

符号付き256ビット2の補数整数です（回転成分<xref href="Omni.Logical.IntRaw128" data-throw-if-not-resolved="false"></xref>同士の積の中間値）。
<xref href="Omni.Logical.WideInt" data-throw-if-not-resolved="false"></xref>を256ビットへ写したもので、片方を直したらもう片方も直します。
64ビットlimbを<xref href="Omni.Logical.IntRaw128.WideLimbCount" data-throw-if-not-resolved="false"></xref>本並べて格納します。
Scale系の乗算・Quaternion合成で使う中間Accumulatorです
（<xref href="Omni.Logical.IntRaw128" data-throw-if-not-resolved="false"></xref>同士の積は最大でも 2*TotalBits-1 ビットで厳密に表現できるため、
倍幅は単一の積に加えて複数項の合成にも十分なheadroomを持ちます）。
Silent Wraparound / Silent Clampは行わず、Overflowが起き得る演算はすべてTry APIです。

### インターフェース（Interfaces）

 [INavigationBoundsSource](Omni.Logical.INavigationBoundsSource.md)

Rendererを持たない対象（頂点を実行時に生成する地形など）が、Scene Viewの接近・飛行の基準になる
大きさを宣言するための契約です。

<p>
Rendererが無いと、Omniは対象をLogical Transformの位置にある直径の小さな点として扱います。
実際の大きさが数百kmあっても、ホイール1ノッチが「遠い点までの距離の一定割合」になり、
面の上にいる目が数十km飛びます。このcomponentを付けると、Rendererの<code>localBounds</code>と同じ規則
（Logical Transformの姿勢で8頂点を包む外接球）で対象の大きさを使います。
</p>

 [IRadialBatchCameraFacingLabelProvider](Omni.Logical.IRadialBatchCameraFacingLabelProvider.md)

BRG上でカメラ正対するラベルへ、カメラ非依存の論理アンカー姿勢を供給します。

 [IRadialRigidAnchorProvider](Omni.Logical.IRadialRigidAnchorProvider.md)

Radial写像後も局所形状を剛体として維持するRendererの明示契約です。

 [IRenderPoseProvider](Omni.Logical.IRenderPoseProvider.md)

CameraCombinationVerificationのTMPラベルなど、カメラごとに論理姿勢が変わるRendererへ
Transformを書き戻さず描画姿勢を供給するインターフェースです。

 [ISceneViewPositionProvider](Omni.Logical.ISceneViewPositionProvider.md)

Scene View の高精度表示に使うワールド論理位置を提供します。

<p>
CameraCombinationVerification など、Unity の <code>Transform.position</code> だけでは
下位ビットを保持できない対象に付く <xref href="Omni.Logical.Transform" data-throw-if-not-resolved="false"></xref> と同じ契約です。
実装しない対象は描画を継続できますが、Scene View 上では精度保証外として扱われます。
</p>

### 列挙型（Enums）

 [DetachStatus](Omni.Logical.DetachStatus.md)

LogicalTransformのDetach結果です。

 [OmniHideLayer](Omni.Logical.OmniHideLayer.md)

Rendererを非表示にした層の種別です。

 [PhysicalSafetyMode](Omni.Logical.PhysicalSafetyMode.md)

有限描画プロキシを強制するかどうかです。設定UIには出さず、既定はAutoです（ForceProxyはテストが使います）。

 [PoseBakeChannelKind](Omni.Logical.PoseBakeChannelKind.md)

1本のベイクチャンネルが何を駆動するかです。

 [PoseBakeRejection](Omni.Logical.PoseBakeRejection.md)

ベイク済みサンプルを使えないと判断した理由です。

<p>
「使えない」ことを bool ひとつで返すと、どの前提が崩れたのかが再生時に分からなくなります。
フォールバックは正常動作の一部（ベイク未生成のクリーンチェックアウトでも絵は出る）なので、
理由を値として持ち、診断とテストの両方から同じ列挙で確認できるようにします。
</p>
