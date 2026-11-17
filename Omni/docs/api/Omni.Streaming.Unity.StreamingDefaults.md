# <a id="Omni_Streaming_Unity_StreamingDefaults"></a> Class StreamingDefaults

Namespace: [Omni.Streaming.Unity](Omni.Streaming.Unity.md)  
Assembly: Omni.Streaming.Unity.dll  

プラットフォームの能力から出す既定値(すべて上書きできる)。ランタイムの定数ではなく、ここと利用者のプロファイルで決める。

```csharp
public static class StreamingDefaults
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[StreamingDefaults](Omni.Streaming.Unity.StreamingDefaults.md)

## メソッド（Methods）

### <a id="Omni_Streaming_Unity_StreamingDefaults_CreateDiskStore_System_String_System_Int64_Omni_Streaming_BufferPool_"></a> CreateDiskStore\(string, long, BufferPool\)

persistentDataPath 下の、ディスク(ブラウザでは IndexedDB を背にしたファイルシステム)のストア。

```csharp
public static FileStore CreateDiskStore(string subdirectory, long budgetBytes, BufferPool pool)
```

#### 引数（Parameters）

`subdirectory` [string](https://learn.microsoft.com/dotnet/api/system.string)

`budgetBytes` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`pool` [BufferPool](Omni.Streaming.BufferPool.md)

#### 戻り値（Returns）

 [FileStore](Omni.Streaming.FileStore.md)

### <a id="Omni_Streaming_Unity_StreamingDefaults_DefaultFrameBudget"></a> DefaultFrameBudget\(\)

1フレームに展開に使ってよい CPU 時間(ミリ秒)の既定。ブラウザは他の処理(VGのCell生成など)と分け合うので小さめ。

```csharp
public static FrameBudget DefaultFrameBudget()
```

#### 戻り値（Returns）

 [FrameBudget](Omni.Streaming.FrameBudget.md)

### <a id="Omni_Streaming_Unity_StreamingDefaults_Options"></a> Options\(\)

ブラウザ(WebGL/WebGPU)はスレッドと同時接続が限られるので控えめに、デスクトップは大きめにする。

```csharp
public static StreamingOptions Options()
```

#### 戻り値（Returns）

 [StreamingOptions](Omni.Streaming.StreamingOptions.md)
