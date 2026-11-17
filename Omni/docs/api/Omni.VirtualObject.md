# <a id="Omni_VirtualObject"></a> Namespace Omni.VirtualObject

### クラス（Classes）

 [DelegateGameObjectSource](Omni.VirtualObject.DelegateGameObjectSource.md)

delegate で同期に作る供給元（Begin で作り、すぐ TryTake できる）。EditMode のテストと、軽い生成に使う。

 [GameObjectRepresentation](Omni.VirtualObject.GameObjectRepresentation.md)

GameObject を 1 つの段の表現にする。準備は供給元（<xref href="Omni.VirtualObject.IGameObjectSource" data-throw-if-not-resolved="false"></xref>）が生成し、Show で SetActive(true)、Hide で非アクティブか破棄。
三角形と資源の大きさは診断用の見積もりを渡す（実測ではない）。

 [PrefabInstantiationSource](Omni.VirtualObject.PrefabInstantiationSource.md)

Prefab を <code>Object.InstantiateAsync</code> で非同期に生成する供給元。Play 中の準備向け（Edit Mode ではフレームが進まず終わらないことがある）。
Prefab のルートを非アクティブにしておくと、Show まで Awake / OnEnable が走らない。そうでなければ、完了を見つけた時点で非アクティブにする
（それまでの 1 フレームは Awake が走りうる）。

 [ProceduralMeshBuffer](Omni.VirtualObject.ProceduralMeshBuffer.md)

<xref href="Omni.VirtualObject.ProceduralMeshRepresentation" data-throw-if-not-resolved="false"></xref> が集めるメッシュの材料。ビルダーはここへ足していく。

 [ProceduralMeshRepresentation](Omni.VirtualObject.ProceduralMeshRepresentation.md)

プロシージャルなメッシュを 1 つの段の表現にする。<xref href="Omni.VirtualObject.ProceduralMeshRepresentation.Prepare" data-throw-if-not-resolved="false"></xref> 1 回で足す三角形を絞り（<code>trianglesPerPrepare</code>）、全部できたらメッシュと
非アクティブな GameObject を作る（IsReady）。全体の三角形とバイトの上限（<code>maxTriangles</code>、<code>maxBytes</code>）を超えたら Fail Closed:
<xref href="Omni.VirtualObject.ProceduralMeshRepresentation.Failure" data-throw-if-not-resolved="false"></xref> に理由を残して資源を捨て、準備できた状態にならない（<xref href="Omni.VirtualObject.ProceduralMeshRepresentation.ResetFailure" data-throw-if-not-resolved="false"></xref> までやり直さない）。

 [ScriptRepresentation](Omni.VirtualObject.ScriptRepresentation.md)

<xref href="Omni.VirtualObject.ScriptRepresentation.Behaviour" data-throw-if-not-resolved="false"></xref>（MonoBehaviour など）を 1 つの段の表現にする。描く物を持たず、振る舞い（Script）の有効化だけを段に結びつける:
Show で <code>enabled = true</code> にして開始のコールバック、Hide で終了のコールバックを呼んで <code>enabled = false</code> にする。
既存の Behaviour を渡すか、準備で作る関数を渡す（作った Behaviour は無効のまま受け取る）。
開始のコールバックが例外を投げたときは、有効化を取り消して例外を投げ直す（Fail Closed。コントローラが今の段を保つ）。

 [VfxRepresentation](Omni.VirtualObject.VfxRepresentation.md)

VFX（<xref href="UnityEngine.VFX.VisualEffect" data-throw-if-not-resolved="false"></xref>）を 1 つの段の表現にする。準備で非アクティブな GameObject に VisualEffect を作り、Show で有効にして再生、Hide で停止して無効にする。
粒子の数や寿命は資産が決める。ここでは資源の大きさの見積もり（<code>byteCount</code>）だけを診断用に受け取る。

 [VgCellRepresentation](Omni.VirtualObject.VgCellRepresentation.md)

VG の地形（R1）を 1 つの段の表現として包む。描くのは VG 自身（Cell を選んで描く）なので、Show / Hide は描くものを作らず、
「この段が望まれている」という印だけを持つ。つなぐのは準備の状態:
IsReady = 必要な Cell（<code>required</code> が返す <xref href="VirtualGeometry.World.PlanetCellKey" data-throw-if-not-resolved="false"></xref>）がすべて <xref href="VirtualGeometry.World.IPlanetCellResidency" data-throw-if-not-resolved="false"></xref> に常駐していること。
Prepare は、常駐していない Cell の生成を要求する（優先度は <code>priority</code>）。描いている間は <xref href="Omni.VirtualObject.VgCellRepresentation.OnFrame" data-throw-if-not-resolved="false"></xref> で Cell を退避させない（Touch）。
必要な Cell が 1 つも無いとき（空の列）は、待つものが無いので常に準備できている。

 [VirtualObjectBehaviour](Omni.VirtualObject.VirtualObjectBehaviour.md)

Virtual Object を Scene で組み立てる component。段のリスト（画素の閾値と表現）を持ち、毎フレーム、対象の画面上の大きさ（画素）を
求めて <xref href="Omni.VirtualObject.VirtualObjectController.Tick(System.Double)" data-throw-if-not-resolved="false"></xref> を呼ぶ。位置は Logical が正本: 対象とカメラの Logical 位置の差を固定小数点で引いてから double にし、
大きさは対象の <xref href="Omni.Logical.INavigationBoundsSource" data-throw-if-not-resolved="false"></xref>（なければ <code>radiusMeters</code>）の外接球から求める。
段の表現は、Inspector で選べる種類（GameObject の Prefab、VFX 資産、既存の Behaviour）か、コードから <xref href="Omni.VirtualObject.VirtualObjectBehaviour.SetLevels(Omni.VirtualObject.VirtualObjectSelector%2cOmni.VirtualObject.IVirtualRepresentation%5b%5d)" data-throw-if-not-resolved="false"></xref> で渡す
（プロシージャルメッシュ・VG の地形など、関数や供給元が要る表現はコードから）。

 [VirtualObjectController](Omni.VirtualObject.VirtualObjectController.md)

Virtual Object 1 つの状態（今の段）と、表現の切り替え。段の選択は <xref href="Omni.VirtualObject.VirtualObjectSelector" data-throw-if-not-resolved="false"></xref>（画素基準・ヒステリシス）に任せ、
ここでは「上がるときは準備ができた表現だけ」「新しい表現を先に出し、古い表現を後で外す」を守る。
表現の配列 levels[i] が段 i。null は「その段では何も描かない」（準備不要・常に描ける）。
失敗は Fail Closed: Show が例外を投げたら今の表現を描き続け、<xref href="Omni.VirtualObject.VirtualObjectController.LastFailure" data-throw-if-not-resolved="false"></xref> に残す。

 [VirtualObjectSelector](Omni.VirtualObject.VirtualObjectSelector.md)

Virtual Object の表現の選択（Docs/Plans/AsteriaVirtualObject.md の不変条件 1・2）。画面上の大きさ（画素）だけで表現の段（0 が最も粗い）を選ぶ。
段 i + 1 へ上がる画素の大きさ enter[i] は、対象ごとではなく段ごとの共通の値にできる（距離の m ではなく画素で決めるので、視野角や解像度が変わっても矛盾しない）。
ヒステリシス: 上がるには enter × hysteresis 以上、下がるには enter ÷ hysteresis 未満が要る（境で行き来しない）。
準備待ち: 上の段は準備ができている（ready）ときだけ選ぶ。できていなければ今の段のまま描き続ける（VG の「子が揃うまで親を描く」と同じ）。
Asteria の型には依存しない（後で VG へ統合するときにそのまま移せる）。

### 構造体（Structs）

 [VirtualObjectBehaviour.Stage](Omni.VirtualObject.VirtualObjectBehaviour.Stage.md)

### インターフェース（Interfaces）

 [IGameObjectSource](Omni.VirtualObject.IGameObjectSource.md)

GameObject のインスタンスの供給元。準備（生成）を非同期にしたいときに、表現から切り離す。

 [IVirtualRepresentation](Omni.VirtualObject.IVirtualRepresentation.md)

Virtual Object の「表現」1 つ（段 1 つぶん）。段 0 が最も粗い表現（点・基材のメッシュなど）、段が上がるほど細かい。
表現は自分で資源（メッシュ・BRG 登録・VG の cell など）を作って持つ。VirtualObjectController が、画素の大きさと IsReady から、描く表現を 1 つ選ぶ。
Asteria の型には依存しない（VG の地形を R1 の表現として包むときも、この契約をそのまま使う）。

 [IVirtualRepresentationFrame](Omni.VirtualObject.IVirtualRepresentationFrame.md)

毎フレームの世話が要る表現が実装する任意の契約（例: VG のセルを退避させないための Touch）。
<xref href="Omni.VirtualObject.VirtualObjectController" data-throw-if-not-resolved="false"></xref> は呼ばない。呼ぶのは持ち主（<xref href="Omni.VirtualObject.VirtualObjectBehaviour" data-throw-if-not-resolved="false"></xref> など）で、Tick の後に全表現へ呼ぶ。
描かれていない間に何をするかは表現が決める（普通は何もしない）。

### 列挙型（Enums）

 [VirtualObjectBehaviour.StageKind](Omni.VirtualObject.VirtualObjectBehaviour.StageKind.md)

 [VirtualHideMode](Omni.VirtualObject.VirtualHideMode.md)

<xref href="Omni.VirtualObject.GameObjectRepresentation" data-throw-if-not-resolved="false"></xref> が、描くのをやめたときに instance をどうするか。

### デリゲート（Delegates）

 [ProceduralMeshStep](Omni.VirtualObject.ProceduralMeshStep.md)

メッシュを少しずつ作る関数。呼ばれるたびに <code class="paramref">buffer</code> へ最大 <code class="paramref">triangleBudget</code> 個の三角形を足し、全部できたら true を返す。
どこまで作ったかは buffer（<xref href="Omni.VirtualObject.ProceduralMeshBuffer.TriangleCount" data-throw-if-not-resolved="false"></xref> など）から読んで再開する（関数自体は状態を持たなくてよい）。
予算を超えて足すと失敗として扱う。
