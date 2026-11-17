# <a id="Omni_Streaming"></a> Namespace Omni.Streaming

### 名前空間（Namespaces）

 [Omni.Streaming.Formats](Omni.Streaming.Formats.md)

 [Omni.Streaming.Unity](Omni.Streaming.Unity.md)

### クラス（Classes）

 [ArrayBufferPool](Omni.Streaming.ArrayBufferPool.md)

byte[] の既定のプール。2 の冪の大きさごとに返却を溜め、溜める総量に上限を持つ。

 [AsyncLocalContentStore](Omni.Streaming.AsyncLocalContentStore.md)

MemoryStoreはHost所有thread、diskはI/O workerだけが操作する。cacheの失敗はmissとして回復する。

 [BufferPool](Omni.Streaming.BufferPool.md)

バイト列の借り出し先。実装は借りたバッファの <xref href="Omni.Streaming.PooledBuffer.Release" data-throw-if-not-resolved="false"></xref> で戻る先を決める。

 [ChunkedByteSource](Omni.Streaming.ChunkedByteSource.md)

大きい論理packの範囲readを、最大4MiBの独立ファイルへ変換する。Unity不要の本体。
同じchunkの同時取得を共有し、hash照合後だけ公開する。Unityのmain threadからpollする。

 [CompletedByteRequest](Omni.Streaming.CompletedByteRequest.md)

1回で完了する取得(同期的に作った結果を返す)。取得元の実装や、メモリ・ファイルの取得元が使う。

 [FileByteSource](Omni.Streaming.FileByteSource.md)

ファイルから範囲を読む取得元(Container は <xref href="Omni.Streaming.FileByteSource.Add(System.String)" data-throw-if-not-resolved="false"></xref> した順の番号)。読みは呼び出し内で同期的に済ませる
(ローカルの SSD や IndexedDB 上のファイルでは小さな範囲の読みは短い。遅い保存先は別の取得元にする)。

 [FileStore](Omni.Streaming.FileStore.md)

ディスク(またはブラウザの IndexedDB を背にしたファイルシステム)上の内容ストア。中身は内容 ID を名前にしたファイルで、
書き込みは一時ファイルに書いてから名前を付け替える(途中で止まっても壊れたファイルを名乗らない)。
合計バイト数が予算を超えたら、使われていない古いファイルから消す。起動時にディレクトリを1回数え上げて索引を作る。
書き込み後に壊れうる保存先なので <xref href="Omni.Streaming.FileStore.RequiresVerification" data-throw-if-not-resolved="false"></xref> は true(host が取り出し時に ID を照合する)。
保存の失敗(容量不足・書き込み禁止など)は黙って捨てる(キャッシュなので)。<xref href="Omni.Streaming.FileStore.Failures" data-throw-if-not-resolved="false"></xref> で数える。

 [ImpairedByteSource](Omni.Streaming.ImpairedByteSource.md)

取得元に、遅延・帯域・失敗率を加える(擬似回線)。時間は <xref href="Omni.Streaming.IClock" data-throw-if-not-resolved="false"></xref> で進むので、仮想時計で決定的に再現できる。
回線は1本として扱い、要求は到着順に帯域を分け合わず順に流れる(完了時刻 = max(開始+遅延, 回線が空く時刻) + 長さ/帯域)。
実際のデモの回線制限(遅い回線の再現)にも使える。

 [InMemoryCatalog](Omni.Streaming.InMemoryCatalog.md)

メモリ上のカタログ(テスト・合成データ・小さなデータ用)。登録したキーは Found、<xref href="Omni.Streaming.InMemoryCatalog.MarkAbsent(Omni.Streaming.StreamKey%40)" data-throw-if-not-resolved="false"></xref> したキーは Absent、
それ以外は <xref href="Omni.Streaming.InMemoryCatalog.UnknownKeys" data-throw-if-not-resolved="false"></xref> の答え(既定は Absent: このカタログが全体の正本という扱い)。
<xref href="Omni.Streaming.InMemoryCatalog.PendingPumps" data-throw-if-not-resolved="false"></xref> 回の Pump が終わるまで、全キーが Pending を返す(目録の遅延読み込みの再現)。

 [LayeredCatalog](Omni.Streaming.LayeredCatalog.md)

層ごとに別のカタログへ振り分ける。登録の無い層は Unavailable(取得手段が無い)。

 [LocalIoDispatcher](Omni.Streaming.LocalIoDispatcher.md)

ローカルI/O専用。全session共通で最大1本、queueは最大64件。待機中はthreadを占有しない。

 [LocalIoSession](Omni.Streaming.LocalIoSession.md)

1HostのI/O予約。配列を作る前に予約し、引継ぎ後に通常の上限へ戻す。

 [ManualClock](Omni.Streaming.ManualClock.md)

テスト・再現用の手動の時計。

 [MemoryByteSource](Omni.Streaming.MemoryByteSource.md)

メモリ上のコンテナ(Container は登録順の番号)から範囲を返す取得元。事前に読み込んだデータの一括利用(プリロード)・テスト・合成データ用。

 [MemoryStore](Omni.Streaming.MemoryStore.md)

メモリ上の内容ストア。合計バイト数の予算を超えたら、使われていない(最後に触れたのが古い)ものから外す。
外すのはストア自身の参照だけで、利用者が取り出して持っているバッファは、その利用者が戻すまで生きる。

 [PayloadLease](Omni.Streaming.PayloadLease.md)

利用者が展開済みの中身を使っている間、host に追い出されないための参照。使い終わったら Dispose する(2回呼んでも1回分)。

 [PooledBuffer](Omni.Streaming.PooledBuffer.md)

参照カウントつきのバイト列。所有者(取得元・ストア・利用者)が <xref href="Omni.Streaming.PooledBuffer.Retain" data-throw-if-not-resolved="false"></xref>/<xref href="Omni.Streaming.PooledBuffer.Release" data-throw-if-not-resolved="false"></xref> で寿命を共有する。
参照が 0 になると <xref href="Omni.Streaming.PooledBuffer.OnReleased" data-throw-if-not-resolved="false"></xref> が呼ばれ、プールへ戻る(または解放される)。0 になった後は使えない。
派生クラスは Memory の実体(byte[]、NativeArray など)を決める。

 [PreloadHandle](Omni.Streaming.PreloadHandle.md)

メモリに余裕があるときの一括読み込み。Dispose するまで、キーを低い優先度で欲しがり続ける。

 [QueuedFileByteSource](Omni.Streaming.QueuedFileByteSource.md)

同期FileByteSourceを単独I/O workerで呼ぶ。Beginとpollではファイルへ触れない。

 [SpatialOrder](Omni.Streaming.SpatialOrder.md)

四分木の1マスの並び順。近いマスを連続させて、1回の範囲取得でまとめて取れるようにする(コンテナの並べ方)。

 [StreamingHost](Omni.Streaming.StreamingHost.md)

 [StreamingHostConfig](Omni.Streaming.StreamingHostConfig.md)

host の組み立て(必須は Catalog と Source。Store・Decoders・Options・Clock・Pool は省略できる)。

 [StreamingOptions](Omni.Streaming.StreamingOptions.md)

host の値で決める設定。ランタイムの定数にしない: 既定値は <xref href="Omni.Streaming.StreamingOptions.Default" data-throw-if-not-resolved="false"></xref> が出し、すべて上書きできる
(プラットフォームごとの既定は、Unity 側がプラットフォームの能力から作って渡す)。

 [StreamingTraceContext](Omni.Streaming.StreamingTraceContext.md)

1Hostの診断識別子と入れ子。Hostと同じ所有threadだけが操作する。

 [SystemClock](Omni.Streaming.SystemClock.md)

 [TieredStore](Omni.Streaming.TieredStore.md)

段を重ねた内容ストア。取り出しは先頭の段から順に探し、後ろの段で見つけたら前の段へ移す(昇格)。保存はすべての段に書く。
例: メモリ(速い・小さい)→ ディスク(遅い・大きい)。

### 構造体（Structs）

 [ByteLocation](Omni.Streaming.ByteLocation.md)

コンテナ内の範囲。Container は取得元が解釈する番号(ファイル、URL の配列の番号など)。

 [ByteSourceInfo](Omni.Streaming.ByteSourceInfo.md)

 [CatalogEntry](Omni.Streaming.CatalogEntry.md)

 [ContentChunk](Omni.Streaming.ContentChunk.md)

1個の独立した配信ファイル。ContainerはHTTP/FileByteSourceへ登録した番号。

 [ContentId](Omni.Streaming.ContentId.md)

中身(何)の識別子。SHA-256 の先頭 128 bit。同じ中身なら同じ ID になるので、版の更新・重複の排除・取得元をまたぐキャッシュの共有・
整合性の検査(<xref href="Omni.Streaming.StreamingOptions.VerifyIntegrity" data-throw-if-not-resolved="false"></xref>)が、すべて「ID が同じなら同じ」に帰着する。default は空(中身なし)。

 [FrameBudget](Omni.Streaming.FrameBudget.md)

1回のTickでデコードを追加開始するCPU時間と件数の目安。開始済み1件は中断しない。取得・検証・store・関心処理を含むTick全体の上限ではない。

 [KeyInfo](Omni.Streaming.KeyInfo.md)

ストリーミングの調停役。利用者は <xref href="Omni.Streaming.IInterestWriter" data-throw-if-not-resolved="false"></xref> で欲しいキーを宣言し、<code>TryAcquire</code> で展開済みの中身を借りる。
host は Tick ごとに、カタログで場所を引き、ストアに無ければ取得元から取り(隣り合う範囲は1回にまとめ、不要になった要求は取り消し)、
中身の ID を照合してストアへ入れ、frame の予算の範囲で展開し、メモリ予算を超えれば使われていない展開済みを古い順に追い出す。
単一 thread(Tick を呼ぶ thread)で使う。ワーカーや別の仕組みで完了する取得元は、<xref href="Omni.Streaming.IByteRequest.IsDone" data-throw-if-not-resolved="false"></xref> を安全に公開すること。

 [StreamingTraceContext.Scope](Omni.Streaming.StreamingTraceContext.Scope.md)

usingで確実に閉じる。診断がなければdefaultのScopeは何もしない。

 [StreamKey](Omni.Streaming.StreamKey.md)

ストリーミングするデータの論理キー(どこ)。層(高さ・色などの種類)+ 空間キー(面・階層・格子番号)。
空間キーは四分木の1マス: 面 Face、階層 Level(0〜<xref href="Omni.Streaming.StreamKey.MaximumLevel" data-throw-if-not-resolved="false"></xref>)、格子番号 X・Y(0〜2^Level−1)。
面の番号の意味は利用者が決める(VG の地形は、球が cube-sphere の 0〜5、平面が 2 を使い、そのまま写す)。階層が 31 を超える Cell は表せない(<xref href="Omni.Streaming.StreamKey.TryChild(System.Int32%2cOmni.Streaming.StreamKey%40)" data-throw-if-not-resolved="false"></xref> が false を返す)。
中身(何)を指す <xref href="Omni.Streaming.ContentId" data-throw-if-not-resolved="false"></xref> とは別: 同じ中身を複数のキーが共有できる。

 [StreamingStats](Omni.Streaming.StreamingStats.md)

host の累計と現在の数(診断・HUD・テスト用)。

 [StreamingTraceEvent](Omni.Streaming.StreamingTraceEvent.md)

区間は共通Stopwatch時刻。親子区間の時間は重複するため加算しない。

 [TransferInfo](Omni.Streaming.TransferInfo.md)

### インターフェース（Interfaces）

 [IAsyncContentStore](Omni.Streaming.IAsyncContentStore.md)

任意の非同期cache読込。完了までPendingを維持し、null結果だけをcache missとする。

 [IByteRequest](Omni.Streaming.IByteRequest.md)

進行中の1回の取得。完了の通知は <xref href="Omni.Streaming.IByteRequest.IsDone" data-throw-if-not-resolved="false"></xref> のポーリング(host の Tick が見る)。別スレッドや別の仕組みで完了する実装は、
結果を書いてから IsDone を立てる(他のスレッドから安全に公開する)こと。

 [IByteSource](Omni.Streaming.IByteSource.md)

バイト列の取得元(HTTP、ファイル、メモリ、WebSocket、独自 socket など)。

 [ICatalog](Omni.Streaming.ICatalog.md)

キー → 中身の ID・場所・種別・存在を引く。目録を遅延して読む実装は、<xref href="Omni.Streaming.ICatalog.Pump" data-throw-if-not-resolved="false"></xref> で進める。

 [IClock](Omni.Streaming.IClock.md)

時刻の供給元(テストでは仮想時計に替える)。

 [IContentStore](Omni.Streaming.IContentStore.md)

内容 ID でバイト列を保存・取得する(メモリ、ファイルなど)。段を重ねられる(<xref href="Omni.Streaming.TieredStore" data-throw-if-not-resolved="false"></xref>)。

 [IDecodedPayload](Omni.Streaming.IDecodedPayload.md)

展開済みの中身。<xref href="System.IDisposable.Dispose" data-throw-if-not-resolved="false"></xref> は、host が追い出したとき、かつ利用者の lease が全部戻ったときに1回だけ呼ぶ。

 [IInterestObserver](Omni.Streaming.IInterestObserver.md)

取得元が、host の関心(いま欲しいキー)の変化を知りたいときに実装する(サーバーが送り込む型の取得元)。
受け取った中身は <xref href="Omni.Streaming.StreamingHost.DeliverContent(Omni.Streaming.ContentId%40%2cOmni.Streaming.PooledBuffer)" data-throw-if-not-resolved="false"></xref> で渡す。host の Tick の中から呼ばれる。

 [IInterestWriter](Omni.Streaming.IInterestWriter.md)

欲しいキーの集合を毎フレーム宣言する口(複数の利用者が別々に持てる。host は全員の宣言を優先度の最大値で合成する)。

 [IPayloadDecoder](Omni.Streaming.IPayloadDecoder.md)

種別ごとの展開器(バイト列 → 利用できる形)。Decode は host の Tick の中(主 thread、frame の予算内)から呼ばれる。

 [IStreamingDiagnostics](Omni.Streaming.IStreamingDiagnostics.md)

任意の計測先。呼出しはHostを単独所有するthread上。実装は例外を投げず、I/Oしない。

### 列挙型（Enums）

 [CatalogLookup](Omni.Streaming.CatalogLookup.md)

 [PayloadState](Omni.Streaming.PayloadState.md)

キーごとの状態。利用者は Absent(存在の表で「無い」)と Unavailable(取得手段が無い・まだ答えられない)を区別して扱う。

 [StreamingPhase](Omni.Streaming.StreamingPhase.md)

Unity非依存のStreaming処理区間。値はCSVの対応表にも保存する。
