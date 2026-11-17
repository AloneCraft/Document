# <a id="Omni_Sequencer_Path"></a> Namespace Omni.Sequencer.Path

### クラス（Classes）

 [LogicalKeyframeClip](Omni.Sequencer.Path.LogicalKeyframeClip.md)

double のキーを持つクリップ。標準の Animation クリップの、float のカーブの代わり(大きな座標や細かい値を float に丸めない)。

<p>
時刻と値の両方がアセットにある(正本)。クリップを動かす・<code>Clip In</code>・速さを変えると、標準のクリップと同じく再生が変わる。
補間はしない。値の意味と補間の式は、受け手(<xref href="Omni.Sequencer.Path.ILogicalKeyframeSink" data-throw-if-not-resolved="false"></xref>)が決める(リグの部品の値をキーにするのと同じ)。
読み出しは <xref href="Omni.Sequencer.Path.LogicalKeyframeSequence.TryRead(UnityEngine.Timeline.TimelineAsset%2cOmni.Sequencer.Path.LogicalKeyframeSequence%40%2cSystem.String%40)" data-throw-if-not-resolved="false"></xref>。
</p>

 [LogicalKeyframeClipBehaviour](Omni.Sequencer.Path.LogicalKeyframeClipBehaviour.md)

クリップ 1 本ぶん(値はアセットから読むので持たない)。

 [LogicalKeyframeMixerBehaviour](Omni.Sequencer.Path.LogicalKeyframeMixerBehaviour.md)

有効なクリップがあれば、シーケンスの時刻を受け手へ渡す。

 [LogicalKeyframeSequence](Omni.Sequencer.Path.LogicalKeyframeSequence.md)

Timeline のアセットから読んだキーの並び(時刻は Timeline の先頭からの秒)。アセットが正本で、これはその読み出し。

 [LogicalKeyframeTrack](Omni.Sequencer.Path.LogicalKeyframeTrack.md)

<xref href="Omni.Sequencer.Path.LogicalKeyframeClip" data-throw-if-not-resolved="false"></xref> を並べるトラック。結び先(<xref href="Omni.Sequencer.Path.ILogicalKeyframeSink" data-throw-if-not-resolved="false"></xref> の MonoBehaviour)へシーケンスの時刻を渡す。
結び先が <xref href="Omni.Sequencer.Path.ILogicalTimelinePreview" data-throw-if-not-resolved="false"></xref> なら、プレビューで書き換える値を登録してもらう(スクラブの後に元へ戻る)。

 [LogicalPathKeypointPlanner](Omni.Sequencer.Path.LogicalPathKeypointPlanner.md)

経路を解析して先読みの要点を作る。区切りは時間の等分ではなく、高度が半分(または倍)になるごと、
視線が画角の1/4回るごと、錨が変わるごと。解析だけに double を使い、要点の意図は経路の値をそのまま持つ。

 [LogicalPathPlayer](Omni.Sequencer.Path.LogicalPathPlayer.md)

経路の再生器(Unity に依存しない)。時計はゲートが許可した秒数だけ進む。先行カーソルは再生位置から
<xref href="Omni.Sequencer.Path.LogicalPathPlayer.HorizonSeconds" data-throw-if-not-resolved="false"></xref> 先までの要点を、期限の近い順・画面への寄与が大きい順に差し出す。時計が止まっている間も差し出し続ける。
失敗(ゲートの理由、経路の評価失敗)は有限に終える。

 [LogicalTimelineClip](Omni.Sequencer.Path.LogicalTimelineClip.md)

「この区間は、この識別子の評価で再生する」ことだけを持つクリップ。
中身(経路の式、Cosmic 系の場面の式など)は受け手(<xref href="Omni.Sequencer.Path.ILogicalTimelineSink" data-throw-if-not-resolved="false"></xref>)が識別子から選ぶ。
経路は開始位置で変わるため焼き込まず、受け手が実行時に時刻→姿勢を求める。

 [LogicalTimelineClipBehaviour](Omni.Sequencer.Path.LogicalTimelineClipBehaviour.md)

クリップ1本ぶんの値。適用はミキサーが受け手へ渡す(バインド先はミキサーにしか来ない)。

 [LogicalTimelineClock](Omni.Sequencer.Path.LogicalTimelineClock.md)

Timeline の再生位置(double 秒)。Unity に依存しない。時刻を進める唯一の所有者で、
デモの監督クラスは「どの時刻を評価するか」をここから受け取る。
進める量は実時間×速さで、ゲートがあれば許可された秒数までに制限する(経路のある移動の「粗くても進む」)。
フレーム時間に依存する積み上げを持たないので、同じ時刻へ通しで着いても Seek で飛んでも同じ時刻になる。

 [LogicalTimelineDriver](Omni.Sequencer.Path.LogicalTimelineDriver.md)

<xref href="Omni.Sequencer.Path.LogicalTimelineClock" data-throw-if-not-resolved="false"></xref> の時刻で <code>PlayableDirector</code> を評価する。
Director は手動更新にし、Timeline 自身の時計では進めない(進める量はゲートが決めるため)。
単発の移動のために、実行時に1本の Timeline を組むこともできる。

 [LogicalTimelineMixerBehaviour](Omni.Sequencer.Path.LogicalTimelineMixerBehaviour.md)

重みが最大のクリップを1本選び、シーケンス時刻とクリップ内時刻を受け手へ渡す。
受け手が無い・<xref href="Omni.Sequencer.Path.ILogicalTimelineSink" data-throw-if-not-resolved="false"></xref> を実装しないバインドでは何もしない。

 [LogicalTimelinePreview](Omni.Sequencer.Path.LogicalTimelinePreview.md)

トラックの <code>GatherProperties</code> から、結び先の受け手へ登録を頼む。

 [LogicalTimelineSinkRelay](Omni.Sequencer.Path.LogicalTimelineSinkRelay.md)

Timeline のバインド先(UnityEngine.Object が必要)と、MonoBehaviour ではない受け手をつなぐ中継。
実行時に <xref href="Omni.Sequencer.Path.LogicalTimelineSinkRelay.Target" data-throw-if-not-resolved="false"></xref> を設定する。Scene へ保存しない(受け手は実行時の物のため)。

 [LogicalTimelineTrack](Omni.Sequencer.Path.LogicalTimelineTrack.md)

Logical 座標のデモの再生位置を、受け手(<xref href="Omni.Sequencer.Path.ILogicalTimelineSink" data-throw-if-not-resolved="false"></xref> を実装した MonoBehaviour)へ渡すトラック。

<p>
書き込み先(Logical の Transform、shader の値、場面の有効化)を直接書かない。各デモの今の書き手が、
受け取った時刻で自分の評価を行って書く。SolarSystem ではカメラ制御の状態(モード・追従・天体固定)が書き手なので、
ここで Transform を書くとクリップの終わりで状態が古い値へ戻る。
</p>
<p>
時刻は <xref href="Omni.Sequencer.Path.LogicalTimelineClock" data-throw-if-not-resolved="false"></xref> が持ち、<xref href="Omni.Sequencer.Path.LogicalTimelineDriver" data-throw-if-not-resolved="false"></xref> が
<code>PlayableDirector</code>(手動更新)へ渡して評価する。Timeline はクリップを並べる殻として使う。
</p>

### 構造体（Structs）

 [LogicalKeyframe](Omni.Sequencer.Path.LogicalKeyframe.md)

キー 1 つ。時刻はクリップの中の秒(標準の Animation クリップのキーと同じ)。値はチャンネルごとの double。

 [LogicalPathIntent](Omni.Sequencer.Path.LogicalPathIntent.md)

経路のある時刻の「意図」。地面の高さや錨の現在姿勢を含まない(後から届いて変わる値は解決器が当てはめる)。
時刻だけで決まり、経路の開始後に変わらない。

 [LogicalPathKeypoint](Omni.Sequencer.Path.LogicalPathKeypoint.md)

先読みの要点。

 [LogicalPathPermit](Omni.Sequencer.Path.LogicalPathPermit.md)

 [LogicalPose](Omni.Sequencer.Path.LogicalPose.md)

解決済みの姿勢。位置・回転は Logical の raw を正本にする。

 [LogicalTimelineClipSpec](Omni.Sequencer.Path.LogicalTimelineClipSpec.md)

Timeline に並べるクリップ1本の指定。

 [LogicalTimelineSample](Omni.Sequencer.Path.LogicalTimelineSample.md)

Timeline のミキサーが受け手へ渡す、ある時刻の有効なクリップ。

### インターフェース（Interfaces）

 [ILogicalKeyframeSink](Omni.Sequencer.Path.ILogicalKeyframeSink.md)

キーフレームのトラックの評価の受け手。書くのは受け手。

 [ILogicalPath](Omni.Sequencer.Path.ILogicalPath.md)

時刻(秒) → 意図。開始時に確定し、途中で変えない純関数。

 [ILogicalPathGate](Omni.Sequencer.Path.ILogicalPathGate.md)

移動の許可。要求した秒数のうち、今回進めてよい秒数を返す。

 [ILogicalPathLookahead](Omni.Sequencer.Path.ILogicalPathLookahead.md)

先読みの受け口。要点を予算内で処理し、処理しきれなかった数を返す。

 [ILogicalPathResolver](Omni.Sequencer.Path.ILogicalPathResolver.md)

意図 → Logical の姿勢。予測と配置が同じ解決器を通る。

 [ILogicalTimelinePreview](Omni.Sequencer.Path.ILogicalTimelinePreview.md)

Timeline ウィンドウのプレビュー(スクラブ)で受け手が書き換える値を、Timeline へ知らせる受け手。

<p>
標準の Animation トラックと同じく、ここで登録した値は、プレビューの間だけ変わり、プレビューを終えると元の値へ戻る。
Scene も「変更あり」にならない。登録しないと、スクラブで動いた値がそのまま残り、Scene を保存すると保存される。
</p>

 [ILogicalTimelineSink](Omni.Sequencer.Path.ILogicalTimelineSink.md)

Timeline の評価の受け手。ミキサーは書き込み先を直接書かず、ここへ時刻を渡すだけにする。
書くのは受け手(各デモの監督クラス)で、今の書き手を変えない。

### 列挙型（Enums）

 [LogicalPathAnchorKind](Omni.Sequencer.Path.LogicalPathAnchorKind.md)

意図の錨。座標の意味は利用者(アプリ)の解決器が決める。Core は天体を知らない。

 [LogicalPathPlacement](Omni.Sequencer.Path.LogicalPathPlacement.md)

錨に対する位置の表し方。

 [LogicalTimelineWrap](Omni.Sequencer.Path.LogicalTimelineWrap.md)

再生位置が終わりに着いたときの扱い。
