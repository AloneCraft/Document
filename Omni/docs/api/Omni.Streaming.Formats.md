# <a id="Omni_Streaming_Formats"></a> Namespace Omni.Streaming.Formats

### クラス（Classes）

 [Bc1](Omni.Streaming.Formats.Bc1.md)

BC1(DXT1)。4×4 画素を 8 byte に圧縮する GPU 圧縮形式。GPU が圧縮のまま読めるので、届いたタイルを展開せずにテクスチャへ送れる。
符号化は包含箱の両端を色の端点にする簡易な方式(月面のような低彩度の画像向け。4 色モードのみ、アルファなし)。
GPU が BC1 を使えない環境のために、RGBA32 へ展開する復号もある(<xref href="Omni.Streaming.Formats.Bc1.DecodeImage(System.ReadOnlySpan%7bSystem.Byte%7d%2cSystem.Int32%2cSystem.Int32)" data-throw-if-not-resolved="false"></xref>)。

 [Crc32](Omni.Streaming.Formats.Crc32.md)

CRC-32(IEEE 802.3)。ディレクトリページの破損検出に使う。

 [ImageTile](Omni.Streaming.Formats.ImageTile.md)

展開済みの画像タイル(幅×高さの画素)。<xref href="Omni.Streaming.Formats.ImageTile.Data" data-throw-if-not-resolved="false"></xref> は <xref href="Omni.Streaming.Formats.ImageTile.Format" data-throw-if-not-resolved="false"></xref> のまま(BC1 ならブロック列)。

 [ImageTileCodec](Omni.Streaming.Formats.ImageTileCodec.md)

画像タイルの中身の形式 "IMT1": [0..4) "IMT1"、[4..6) 幅、[6..8) 高さ、[8] 形式、[9..12) 予備、以降は画素のデータ(形式のまま)。

 [ImageTileDecoder](Omni.Streaming.Formats.ImageTileDecoder.md)

種別 <xref href="Omni.Streaming.Formats.ImageTileCodec.Kind" data-throw-if-not-resolved="false"></xref> の展開器。

 [PackCatalog](Omni.Streaming.Formats.PackCatalog.md)

pack(.otp)を引くカタログ。目録は遅延して読む: 先頭(ヘッダー+根の目録+付随情報)を1回取得し、キーを引くときに必要な葉のページだけを取得する。
答えられない間は Pending を返し、<xref href="Omni.Streaming.Formats.PackCatalog.Pump" data-throw-if-not-resolved="false"></xref> が取得を進める。ページの取得に失敗したら再試行し、使い切ると一定時間 Unavailable を返す。
面・層・階層の範囲が合わないキーは Absent(この pack に無い)。目録の項目が無いキーも Absent(= 平坦などで親から導けるマス)。

 [PackDirectory](Omni.Streaming.Formats.PackDirectory.md)

目録の探索(同期の純関数)。<xref href="Omni.Streaming.Formats.PackCatalog" data-throw-if-not-resolved="false"></xref>(非同期)と <xref href="Omni.Streaming.Formats.PackFile" data-throw-if-not-resolved="false"></xref>(同期)が共有する。

 [PackFile](Omni.Streaming.Formats.PackFile.md)

メモリ上の pack を同期で読む(書き出しの検証、小さな pack、ツール用)。

 [PackFormatException](Omni.Streaming.Formats.PackFormatException.md)

pack の形式が壊れている・対応しない版、のとき。

 [PackSetCatalog](Omni.Streaming.Formats.PackSetCatalog.md)

面ごとに分けた pack(層×面で1ファイル)を、キーの層と面で引き分ける。登録の無い(層, 面)は Unavailable(取得手段が無い)。
面を指定しない pack(<xref href="Omni.Streaming.Formats.PackHeader.AnyFace" data-throw-if-not-resolved="false"></xref>)は、face に −1 で登録する。

 [PackWriter](Omni.Streaming.Formats.PackWriter.md)

pack を書く。マスは ID(<xref href="Omni.Streaming.Formats.TileId" data-throw-if-not-resolved="false"></xref>)の昇順に <xref href="Omni.Streaming.Formats.PackWriter.AddTile(System.Int32%2cSystem.UInt32%2cSystem.UInt32%2cSystem.ReadOnlySpan%7bSystem.Byte%7d)" data-throw-if-not-resolved="false"></xref> する(Hilbert 順で並ぶので、近いマスの中身が本体の中でも連続する)。
同じ中身は1回だけ保存し、ID が連続して同じ中身を指すマスは1項目にまとめる。

 [PackWriterOptions](Omni.Streaming.Formats.PackWriterOptions.md)

 [TileId](Omni.Streaming.Formats.TileId.md)

四分木のマスを、階層をまたいだ1本の整数 ID にする(PMTiles v3 と同じ考え方): 階層 L のマスは、
階層 0〜L−1 のマスの総数 (4^L−1)/3 に、その階層内の Hilbert 順の位置を足した値。ID が連続するマスは、空間でも近い。

### 構造体（Structs）

 [PackEntry](Omni.Streaming.Formats.PackEntry.md)

葉の目録の1項目(48 byte): ID が TileId から RunLength 個連続するマスが、同じ中身(Offset・Length は本体の先頭から)を指す
(平坦なマスなど同一の中身を1つにまとめる)。中身の ID は取得後の照合に使う。

 [PackHeader](Omni.Streaming.Formats.PackHeader.md)

pack ファイルの先頭(固定 128 byte、little endian)。版 1.0:
[0..4) "OTPK"、[4..6) 主版、[6..8) 副版、[8..12) 機能フラグ(上位16bit = 必須。読み手が知らない必須の機能があれば拒否する)、
[12..16) 層、[16] 面(255 = どの面も)、[17] 最小階層、[18] 最大階層、[20..22) 既定の種別、
[24..32) 掲載したマスの数、[32..40) 目録の項目数、[40..48) 保存した中身の数、
[48..56)+[56..64) 根の目録の位置と長さ、[64..72)+[72..80) 付随情報、[80..88)+[88..96) 葉の目録、[96..104)+[104..112) 中身の本体、
[112..116) 1ページの項目数、[120..124) ヘッダー([0..120))の CRC-32。
並び: ヘッダー、根の目録、付随情報、葉の目録、中身の本体。ヘッダー+根の目録+付随情報が 16 KiB 以内なら、先頭1回の取得で足りる。

 [PackRootEntry](Omni.Streaming.Formats.PackRootEntry.md)

根の目録の1項目(32 byte): 葉のページの最初の ID、ページの位置(葉の目録の先頭から)、圧縮後の長さ、項目数、CRC-32。

 [PackWriteResult](Omni.Streaming.Formats.PackWriteResult.md)

### 列挙型（Enums）

 [ImageTileFormat](Omni.Streaming.Formats.ImageTileFormat.md)

 [PackCatalog.InitState](Omni.Streaming.Formats.PackCatalog.InitState.md)
