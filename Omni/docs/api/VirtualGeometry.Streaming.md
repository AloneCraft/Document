# <a id="VirtualGeometry_Streaming"></a> Namespace VirtualGeometry.Streaming

### クラス（Classes）

 [CellAlbedoPackBaker](VirtualGeometry.Streaming.CellAlbedoPackBaker.md)

色の供給元(<xref href="VirtualGeometry.Streaming.DirectionColorSampler" data-throw-if-not-resolved="false"></xref>)を、Cell ごとの画像タイル(<xref href="Omni.Streaming.Formats.ImageTile" data-throw-if-not-resolved="false"></xref>、BC1)にして pack(.otp)へ焼く。
1 タイルは Cell を size×size の画素で表し、外周に border 画素の余白(隣の Cell の色)を持つ(全体は size + 2·border 四方で、4 の倍数)。
画素の位置は Cell の面の座標で等角に並ぶ(shader が面の UV から引く規則と同じ)。階層 0〜MaximumLevel の全 Cell を、面ごとに1つの pack へ書く。
同じ色の Cell は内容が同じなので、pack の中で1つにまとまる。

 [CellHeightGrid](VirtualGeometry.Streaming.CellHeightGrid.md)

Cell の格子の高さ(外の 1 周を含む side×side、<xref href="VirtualGeometry.World.PlanetCellMeshBuilder.RingSide" data-throw-if-not-resolved="false"></xref>)を、共通の固定量子化(step メートル刻みの int16)で
持つ展開済みの中身。隣り合う Cell の共有する格子点は同じ高さ(同じ整数)になるので、継ぎ目で割れない。

 [CellHeightGridCodec](VirtualGeometry.Streaming.CellHeightGridCodec.md)

格子の高さの中身の形式 "CHT1": [0..4) "CHT1"、[4..6) side、[6..8) 旗(bit0 = 陰影用の高さの面がある)、[8..12) step(float、メートル/整数)、
以降は Deflate した面(高さ、あれば陰影)。1 面は side² 個の int16 で、左の格子点との差(各行の先頭は上の行の先頭との差、最初の点は 0 との差)を
2 byte little endian で並べたもの(差は int16 の剰余で表し、復元は同じ剰余で足すので正確)。滑らかな地形ほど小さな値が並び、Deflate がよく効く。

 [CellHeightGridDecoder](VirtualGeometry.Streaming.CellHeightGridDecoder.md)

種別 <xref href="VirtualGeometry.Streaming.CellHeightGridCodec.Kind" data-throw-if-not-resolved="false"></xref> の展開器。

 [CellHeightPackBaker](VirtualGeometry.Streaming.CellHeightPackBaker.md)

高さの供給元(<xref href="VirtualGeometry.World.IPlanetHeightProvider" data-throw-if-not-resolved="false"></xref>)を、Cell ごとの格子の高さ(<xref href="VirtualGeometry.Streaming.CellHeightGridCodec" data-throw-if-not-resolved="false"></xref>)にして pack(.otp)へ焼く。
格子点の方向は実行時の <xref href="VirtualGeometry.World.PlanetCellMeshBuilder.GridDirections(VirtualGeometry.World.PlanetCellFrame%40%2cSystem.Double%2cSystem.Double%5b%5d%2cSystem.Double%5b%5d%2cSystem.Double%5b%5d)" data-throw-if-not-resolved="false"></xref> と同じなので、実行時に <xref href="VirtualGeometry.World.PlanetCellMeshBuilder.BuildFromHeights(VirtualGeometry.World.PlanetCellFrame%40%2cSystem.Double%2cSystem.ReadOnlySpan%7bSystem.Double%7d%2cSystem.ReadOnlySpan%7bSystem.Double%7d%2cSystem.Single%2cUnityEngine.Vector4%2cVirtualizedGeometry.VirtualGeometryPackedVertex%5b%5d%2cSystem.Int32%2cUnityEngine.Vector4%40%2cSystem.Double%40%2cSystem.Double%40)" data-throw-if-not-resolved="false"></xref> で作った
Cell は、供給元から直接作った Cell と(量子化の範囲で)一致する。階層 0〜MaximumLevel の全 Cell を、面ごとに1つの pack へ書く。
Editor にも Player にも依存しない(コマンドラインのツールからも動かせる)。

 [CellKeyMap](VirtualGeometry.Streaming.CellKeyMap.md)

VG の <xref href="VirtualGeometry.World.PlanetCellKey" data-throw-if-not-resolved="false"></xref>(96 bit の格子番号)と、ストリーミングのキー <xref href="Omni.Streaming.StreamKey" data-throw-if-not-resolved="false"></xref>(31 階層まで)の対応。

 [CellTileCache](VirtualGeometry.Streaming.CellTileCache.md)

届いた画像タイル(<xref href="Omni.Streaming.Formats.ImageTile" data-throw-if-not-resolved="false"></xref>)を GPU の <xref href="UnityEngine.Texture2DArray" data-throw-if-not-resolved="false"></xref> の slice に置くキャッシュ。slice は最近使った順(frame の番号)で再利用する。
GPU が BC1 を使えるときは BC1 のまま置き(展開しない)、使えないときは RGBA32 へ展開して置く。mip は持たない
(Cell は画面の密度に合わせて選ばれるので、タイルは拡大して使う)。sRGB の画像として扱う。

 [CubeGridMap](VirtualGeometry.Streaming.CubeGridMap.md)

方向 → cube-sphere の面・Cell・格子の座標。Cell の格子点は面の上で等角(角度が格子の番号に比例)に並ぶ
(<xref href="VirtualGeometry.World.PlanetCellMeshBuilder.SpherePoint(VirtualGeometry.World.PlanetCellFrame%40%2cSystem.Int32%2cSystem.Double%2cSystem.Double%2cSystem.Double%2cSystem.Double%40%2cSystem.Double%40%2cSystem.Double%40%2cSystem.Double%40%2cSystem.Double%40%2cSystem.Double%40)" data-throw-if-not-resolved="false"></xref> と同じ規則)ので、方向の面座標の角度 atan(s)、atan(t) を [0, 1] に正規化して 2^level 倍する。

 [CellHeightPackBaker.Options](VirtualGeometry.Streaming.CellHeightPackBaker.Options.md)

 [CellAlbedoPackBaker.Options](VirtualGeometry.Streaming.CellAlbedoPackBaker.Options.md)

 [ResidentCellHeights](VirtualGeometry.Streaming.ResidentCellHeights.md)

浅い階層(<xref href="VirtualGeometry.Streaming.ResidentCellHeights.Level" data-throw-if-not-resolved="false"></xref>)の全ての Cell の格子を、最初に読み込んで手放さない「常駐する粗い層」。
細かい格子(<xref href="VirtualGeometry.Streaming.StreamedPlanetHeightProvider" data-throw-if-not-resolved="false"></xref>)が届いていない場所の高さを、接地・岩などの問い合わせに答える予備に使う
(<xref href="VirtualGeometry.World.PlanetFallbackHeightProvider" data-throw-if-not-resolved="false"></xref>)。VG の Cell を作る供給元には使わない。
揃うまでは、まだ持っていない方向に NaN を返す。<xref href="VirtualGeometry.Streaming.ResidentCellHeights.Tick" data-throw-if-not-resolved="false"></xref> を main thread で毎 frame 呼ぶ(揃ったら何もしない)。
補間は <xref href="VirtualGeometry.Streaming.StreamedPlanetHeightProvider" data-throw-if-not-resolved="false"></xref> と同じ双三次。格子は作られた後に変わらないので、別 thread から読んでよい。

 [StreamedCellHeightSource](VirtualGeometry.Streaming.StreamedCellHeightSource.md)

<xref href="VirtualGeometry.World.IPlanetCellHeightSource" data-throw-if-not-resolved="false"></xref> をストリーミング(<xref href="Omni.Streaming.StreamingHost" data-throw-if-not-resolved="false"></xref>)で満たす。階層が maximumLevel 以下の Cell は、その Cell の格子の高さ
(<xref href="VirtualGeometry.Streaming.CellHeightGrid" data-throw-if-not-resolved="false"></xref>)が常駐したら Ready、届くまで Pending(取得を宣言)。カタログが「無い」(Absent)と答えた Cell と、階層が深い Cell は
NotProvided(高さの供給元 = <xref href="VirtualGeometry.Streaming.StreamedPlanetHeightProvider" data-throw-if-not-resolved="false"></xref> などで作る)。取得に失敗した・取得手段が無い・pack に無い Cell は Unavailable
(作らない。偽の高さで埋めない。pack は階層 0〜MaximumLevel の全 Cell を持つこと)。
階層が深い Cell を問い合わせると、その祖先(階層 MaximumLevel)の格子を手元に確保(pin)し、確保できてから NotProvided を返す
(深い Cell を作る供給元が、同じ格子から補間するため)。届いていなければ Pending。
宣言は <xref href="VirtualGeometry.Streaming.StreamedCellHeightSource.PublishInterest(System.Int32)" data-throw-if-not-resolved="false"></xref> が行う(毎 frame、描画の後に呼ぶ)。直近 <xref href="VirtualGeometry.Streaming.StreamedCellHeightSource.InterestFrames" data-throw-if-not-resolved="false"></xref> frame に問い合わせのあった Cell だけを宣言し続ける。

 [StreamedCellTileSource](VirtualGeometry.Streaming.StreamedCellTileSource.md)

Cell ごとの色のタイルを、ストリーミング(<xref href="Omni.Streaming.StreamingHost" data-throw-if-not-resolved="false"></xref>)で届けて <xref href="VirtualGeometry.Streaming.CellTileCache" data-throw-if-not-resolved="false"></xref> に置き、Cell の draw の値として渡す
(<xref href="VirtualGeometry.World.IPlanetCellPropertySource" data-throw-if-not-resolved="false"></xref>)。Cell の階層が pack の最大階層を超えるときは、最大階層の祖先のタイルを拡大して使う
(テクセルが画素より大きくなる所。そこから先の細部は shader の手続きの細部が受け持つ)。自分のタイルが届くまでは、届いている最も近い祖先のタイルで描く。
書く値: _PlanetTileSlice.x = slice(タイルが無ければ −1)、_PlanetTileMap = (scaleU, scaleV, offsetU, offsetV)
(面の UV からタイルの UV への変換。タイルの外周の border は隣へのにじみを防ぐ余白)。

 [StreamedCubicHeightBounds](VirtualGeometry.Streaming.StreamedCubicHeightBounds.md)

Catmull-RomをBezier制御点へ写し、補間値の凸包で囲う。元の格子を変更しない。

 [StreamedPlanetHeightProvider](VirtualGeometry.Streaming.StreamedPlanetHeightProvider.md)

ストリーミングで確保した(<xref href="VirtualGeometry.Streaming.StreamedCellHeightSource.TryGetPinned(Omni.Streaming.StreamKey%40%2cVirtualGeometry.Streaming.CellHeightGrid%40)" data-throw-if-not-resolved="false"></xref>)階層 MaximumLevel の Cell の格子から、方向の高さを双三次補間で返す。
焼いた階層より細かい Cell を作る供給元として、<xref href="VirtualGeometry.World.PlanetAmplifiedHeightProvider" data-throw-if-not-resolved="false"></xref> の基(basis)に使う: 焼いた分解能までは実データ、その先は増幅ノイズ。
確保した格子の外(まだ届いていない・手放した)の方向は NaN を返し、Cell は作られない(偽の高さで埋めない)。
確保した格子は作られた後に変わらず、別 thread から読んでよい。補間は格子点で格子の値そのものになる。

 [StreamedTerrainConnector](VirtualGeometry.Streaming.StreamedTerrainConnector.md)

<xref href="VirtualGeometry.World.PlanetHeightTerrainSource" data-throw-if-not-resolved="false"></xref> に <xref href="VirtualGeometry.Streaming.StreamedCellHeightSource" data-throw-if-not-resolved="false"></xref> を接続し、描画の後に関心を宣言する。
host の組み立てと Tick(<code>Omni.Streaming.Unity.StreamingBehaviour</code>)は利用者が行う。
Edit Mode でも動く(Scene に保存されず、利用者が足して接続したときだけ関心を宣言する)。

### デリゲート（Delegates）

 [DirectionColorSampler](VirtualGeometry.Streaming.DirectionColorSampler.md)

方向(単位ベクトル)の色を返す(0〜255、sRGB)。例: 正距円筒の画像の双一次補間。
