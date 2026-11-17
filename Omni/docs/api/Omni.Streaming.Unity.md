# <a id="Omni_Streaming_Unity"></a> Namespace Omni.Streaming.Unity

### クラス（Classes）

 [FileSystemSync](Omni.Streaming.Unity.FileSystemSync.md)

ブラウザ(WebGL)の persistentDataPath の保存を促す。他のプラットフォームでは何もしない。
<xref href="Omni.Streaming.Unity.FileSystemSync.Request" data-throw-if-not-resolved="false"></xref> は何度呼んでもよい(間引いて、最後の呼びから <xref href="Omni.Streaming.Unity.FileSystemSync.MinimumIntervalSeconds" data-throw-if-not-resolved="false"></xref> 以上あけて1回保存する)。
保存の呼び出しは <xref href="Omni.Streaming.Unity.StreamingBehaviour" data-throw-if-not-resolved="false"></xref> の Update が行う。

 [HttpByteSource](Omni.Streaming.Unity.HttpByteSource.md)

HTTP(S) の取得元(UnityWebRequest)。Container は <xref href="Omni.Streaming.Unity.HttpByteSource.Add(System.String)" data-throw-if-not-resolved="false"></xref> した URL の番号。範囲は Range ヘッダーで取る(サーバーが 206 を返すこと)。
サーバーが Range を無視して 200 で全体を返した場合は、全体から要求の範囲を切り出して使う(毎回全体を取るので、警告を1回出す)。
WebGL(ブラウザ)では別のオリジンの URL は CORS が通るサーバーに限る。どの URL を使うかは利用者(プロファイル)が決める。
独立chunkはwholeFilesを明示し、RangeなしGETで全body長を照合する。従来の範囲取得は既定のまま維持する。
取得した中身は、プールのバッファへコピーして渡す(UnityWebRequest の寿命と切り離すため)。

 [StreamingBehaviour](Omni.Streaming.Unity.StreamingBehaviour.md)

host を毎フレーム進める。host の組み立ては利用者(プロファイル)が行い、<xref href="Omni.Streaming.Unity.StreamingBehaviour.Attach(Omni.Streaming.StreamingHost%2cOmni.Streaming.FrameBudget)" data-throw-if-not-resolved="false"></xref> で渡す。
破棄時に host を Dispose する(進行中の取得の取り消し、展開済みの解放)。
Edit Mode でも動く(Scene に保存されず、利用者が足したときだけ host を進める)。

 [StreamingDefaults](Omni.Streaming.Unity.StreamingDefaults.md)

プラットフォームの能力から出す既定値(すべて上書きできる)。ランタイムの定数ではなく、ここと利用者のプロファイルで決める。

 [WebBackgroundPump](Omni.Streaming.Unity.WebBackgroundPump.md)

ブラウザ(WebGL)でタブが背面のとき、<xref href="Omni.Streaming.Unity.StreamingBehaviour" data-throw-if-not-resolved="false"></xref> を約 10 Hz で進める。
ブラウザは隠れたタブの描画ループ(requestAnimationFrame とタイマー)を約 1 秒に 1 回へ絞るので、Update だけで進めると、取得の完了の検出と次の要求の発行が 1 fps に落ちる。
Web Worker のタイマーは絞られないので、そこから(<code>OmniStreaming.jslib</code>)隠れているときだけ <code>Module.SendMessage</code> で <xref href="Omni.Streaming.Unity.WebBackgroundPump.OnPump" data-throw-if-not-resolved="false"></xref> を呼ぶ。
<xref href="Omni.Streaming.Unity.StreamingBehaviour.BackgroundPump" data-throw-if-not-resolved="false"></xref> を true にした利用者だけが対象。他のプラットフォーム・Editor では何もしない。
