# <a id="Omni_Streaming_Unity_HttpByteSource"></a> Class HttpByteSource

Namespace: [Omni.Streaming.Unity](Omni.Streaming.Unity.md)  
Assembly: Omni.Streaming.Unity.dll  

HTTP(S) の取得元(UnityWebRequest)。Container は <xref href="Omni.Streaming.Unity.HttpByteSource.Add(System.String)" data-throw-if-not-resolved="false"></xref> した URL の番号。範囲は Range ヘッダーで取る(サーバーが 206 を返すこと)。
サーバーが Range を無視して 200 で全体を返した場合は、全体から要求の範囲を切り出して使う(毎回全体を取るので、警告を1回出す)。
WebGL(ブラウザ)では別のオリジンの URL は CORS が通るサーバーに限る。どの URL を使うかは利用者(プロファイル)が決める。
独立chunkはwholeFilesを明示し、RangeなしGETで全body長を照合する。従来の範囲取得は既定のまま維持する。
取得した中身は、プールのバッファへコピーして渡す(UnityWebRequest の寿命と切り離すため)。

```csharp
public sealed class HttpByteSource : IByteSource
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[HttpByteSource](Omni.Streaming.Unity.HttpByteSource.md)

#### 実装するインターフェース（Implements）

[IByteSource](Omni.Streaming.IByteSource.md)

## コンストラクター（Constructors）

### <a id="Omni_Streaming_Unity_HttpByteSource__ctor_System_Int32_System_Boolean_"></a> HttpByteSource\(int, bool\)

wholeFiles=true は独立ファイルの完全取得。offset=0・HTTP200・復号後byte長一致を要求し、Rangeを送らない。

```csharp
public HttpByteSource(int preferredConcurrency = 6, bool wholeFiles = false)
```

#### 引数（Parameters）

`preferredConcurrency` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`wholeFiles` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## フィールド（Fields）

### <a id="Omni_Streaming_Unity_HttpByteSource_LaneCount"></a> LaneCount

0 より大きいと、要求の URL に ?omni-lane=N(N は 0〜LaneCount−1 を順に回す)を足す。ブラウザは同じ URL への Range 違いの同時要求を直列に処理する
(WebGPU ビルドの実測、Docs/Plans/StreamingSpike.md)ので、URL を変えて並列にする。サーバーが無視するクエリ(静的なファイル配信)でだけ使う。
既定は 0(足さない。GitHub Pages のように、URL ごとの別ファイル(面ごとの pack)で並列になる配信では不要)。

```csharp
public int LaneCount
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_Unity_HttpByteSource_TimeoutSeconds"></a> TimeoutSeconds

1回の要求の期限(秒)。0 は Unity の既定。

```csharp
public int TimeoutSeconds
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="Omni_Streaming_Unity_HttpByteSource_Info"></a> Info

```csharp
public ByteSourceInfo Info { get; }
```

#### 値（Property Value）

 [ByteSourceInfo](Omni.Streaming.ByteSourceInfo.md)

## メソッド（Methods）

### <a id="Omni_Streaming_Unity_HttpByteSource_Add_System_String_"></a> Add\(string\)

```csharp
public int Add(string url)
```

#### 引数（Parameters）

`url` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_Unity_HttpByteSource_Begin_Omni_Streaming_ByteLocation__Omni_Streaming_BufferPool_"></a> Begin\(in ByteLocation, BufferPool\)

location の範囲の取得を始める。結果のバッファは pool から借りる。始められないときは例外ではなく、完了済みの失敗を返してもよい。

```csharp
public IByteRequest Begin(in ByteLocation location, BufferPool pool)
```

#### 引数（Parameters）

`location` [ByteLocation](Omni.Streaming.ByteLocation.md)

`pool` [BufferPool](Omni.Streaming.BufferPool.md)

#### 戻り値（Returns）

 [IByteRequest](Omni.Streaming.IByteRequest.md)

### <a id="Omni_Streaming_Unity_HttpByteSource_UrlOf_System_Int32_"></a> UrlOf\(int\)

```csharp
public string UrlOf(int container)
```

#### 引数（Parameters）

`container` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
