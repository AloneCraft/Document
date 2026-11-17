# <a id="Omni_Observer"></a> Namespace Omni.Observer

### 名前空間（Namespaces）

 [Omni.Observer.Editor](Omni.Observer.Editor.md)

### クラス（Classes）

 [RadialObserverChannelGuard](Omni.Observer.RadialObserverChannelGuard.md)

観察枠のVirtual Cameraを、その枠のBrainだけが拾うように分離します。

<p>
CinemachineBrainの既定のChannelMaskは「全チャンネル」で、シーン内の別のBrain
（ゲーム側の主カメラ）が観察枠のVirtual Cameraを拾うと、主カメラが観察位置へ動いてしまいます。
そのため、枠ごとに専用のOutputChannel（Channel01〜05）を割り当て、枠のBrainをそのチャンネルだけにし、
有効化時点で存在する他のBrainからこのチャンネルを外します（無効化時に元へ戻します）。
有効化より後に作られたBrainは対象外なので、その場合はそのBrainのChannelMaskを設定してください。
</p>

 [RadialObserverFraming](Omni.Observer.RadialObserverFraming.md)

変形後の世界を俯瞰するカメラの枠取り数学です。Unity型へ依存する副作用を持ちません。

<p>
変形後の世界は有限です（<code>F(M*d)</code>は距離の対数に比例）。巨大・遠距離の対象も、
Logical差分を<xref href="Omni.RadialSettings.TryMap(Omni.Logical.Vector3%40%2cUnity.Mathematics.float3%40)" data-throw-if-not-resolved="false"></xref>で有限の描画座標へ落としてから扱うため、
絶対座標をfloatへ狭小化しません。
</p>

 [RadialObserverLayout](Omni.Observer.RadialObserverLayout.md)

観察枠のCamera.rect（正規化viewport）を計算します。副作用を持たない純粋関数です。
枠0が周回、枠1〜4が固定（Front／Right／Top／Iso）です。

 [RadialObserverOrbit](Omni.Observer.RadialObserverOrbit.md)

観察枠1つのCinemachine仮想カメラを駆動します。

<p>
距離は枠の固定距離（<xref href="Omni.Observer.ObserverFrame.FixedDistance" data-throw-if-not-resolved="false"></xref>）です。
桁違いのスケール間を滑らかに動くよう、距離はlog空間でSmoothDampします。
周回枠は自動周回し、右ボタンドラッグ（枠の内側）で手動回転、ホイールで拡縮、操作後は一定時間おいて周回を再開します。
固定枠は角度を固定します。
</p>

 [RadialObserverRig](Omni.Observer.RadialObserverRig.md)

<xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref>が見ている「変形後の世界」を、別のカメラ（観察枠）から外側へ引いて見るためのRigです。

<p>
観察枠のCameraには<xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref>を付けません。<xref href="Omni.RadialGlobalWarpSourceRegistry" data-throw-if-not-resolved="false"></xref>へ
「ワープ中心＝ソースのRadialCamera」「仮想論理視点＝Pivotがソース位置C、PhysicalPivotがこのRigの原点」と登録し、
比較表示と同じ契約（対象だけを<code>C+F(P-C)</code>へ圧縮し、視点Eは物理位置のまま）で描かせます。
</p>
<p>
Rig配下は有限な描画空間です（原点がC）。LogicalTransformを付けないため、Cinemachineと同居できます。
Rig自体は動かさず、Cへの追従はPivot（論理）側で行います。既定ではPlayモードだけで動作します。
<xref href="Omni.Observer.RadialObserverRig.RunInEditMode" data-throw-if-not-resolved="false"></xref>をオンにしたRigだけ、Editモードでも登録と枠の表示を行います（オフのRigはEditモードで何も変えません）。
</p>

 [RadialObserverSlot](Omni.Observer.RadialObserverSlot.md)

観察枠1つの設定です。Cameraとレイアウト上の番号（<xref href="Omni.Observer.RadialObserverLayout" data-throw-if-not-resolved="false"></xref> の枠番号）を持ち、
配置と表示は <xref href="Omni.Observer.RadialObserverRig" data-throw-if-not-resolved="false"></xref> が決めます。
平行投影のCameraは、Radialでは写像が常に恒等になり変形後の世界を見られないため使いません。

### 構造体（Structs）

 [ObserverFrame](Omni.Observer.ObserverFrame.md)

変形後の世界を俯瞰するための枠取り結果です。Focusはワープ中心Cを原点とした
有限の描画座標（メートル＝描画単位）、BoundingRadiusは近遠クリップ用の球の半径です。

### 列挙型（Enums）

 [ObserverCorner](Omni.Observer.ObserverCorner.md)

枠を寄せる画面の隅です。

 [ObserverLayoutPreset](Omni.Observer.ObserverLayoutPreset.md)

観察枠の並べ方です。

 [ObserverSlotKind](Omni.Observer.ObserverSlotKind.md)

枠が周回か固定角度かです。
