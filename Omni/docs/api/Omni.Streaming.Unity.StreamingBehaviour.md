# <a id="Omni_Streaming_Unity_StreamingBehaviour"></a> Class StreamingBehaviour

Namespace: [Omni.Streaming.Unity](Omni.Streaming.Unity.md)  
Assembly: Omni.Streaming.Unity.dll  

host を毎フレーム進める。host の組み立ては利用者(プロファイル)が行い、<xref href="Omni.Streaming.Unity.StreamingBehaviour.Attach(Omni.Streaming.StreamingHost%2cOmni.Streaming.FrameBudget)" data-throw-if-not-resolved="false"></xref> で渡す。
破棄時に host を Dispose する(進行中の取得の取り消し、展開済みの解放)。
Edit Mode でも動く(Scene に保存されず、利用者が足したときだけ host を進める)。

```csharp
[DefaultExecutionOrder(-100)]
[ExecuteAlways]
public sealed class StreamingBehaviour : MonoBehaviour
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[StreamingBehaviour](Omni.Streaming.Unity.StreamingBehaviour.md)

## プロパティ（Properties）

### <a id="Omni_Streaming_Unity_StreamingBehaviour_BackgroundPump"></a> BackgroundPump

true にすると、ブラウザ(WebGL)でタブが背面のとき(Unity のフレームが約 1 fps に絞られる)も、約 10 Hz で host を進める(<xref href="Omni.Streaming.Unity.WebBackgroundPump" data-throw-if-not-resolved="false"></xref>)。
既定は false: 背面で進めると、Update の外から呼ばれるので、展開などで Unity の API(GPU など)を使う利用者は有効にしてはいけない。
他のプラットフォームでは何もしない。

```csharp
public bool BackgroundPump { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_Unity_StreamingBehaviour_Budget"></a> Budget

```csharp
public FrameBudget Budget { get; set; }
```

#### 値（Property Value）

 [FrameBudget](Omni.Streaming.FrameBudget.md)

### <a id="Omni_Streaming_Unity_StreamingBehaviour_Host"></a> Host

```csharp
public StreamingHost Host { get; }
```

#### 値（Property Value）

 [StreamingHost](Omni.Streaming.StreamingHost.md)

## メソッド（Methods）

### <a id="Omni_Streaming_Unity_StreamingBehaviour_Attach_Omni_Streaming_StreamingHost_Omni_Streaming_FrameBudget_"></a> Attach\(StreamingHost, FrameBudget\)

```csharp
public void Attach(StreamingHost host, FrameBudget budget)
```

#### 引数（Parameters）

`host` [StreamingHost](Omni.Streaming.StreamingHost.md)

`budget` [FrameBudget](Omni.Streaming.FrameBudget.md)

### <a id="Omni_Streaming_Unity_StreamingBehaviour_PumpFromBackground"></a> PumpFromBackground\(\)

<xref href="Omni.Streaming.Unity.WebBackgroundPump" data-throw-if-not-resolved="false"></xref> から(試験のため public)。直前に Update が進めていたら(前面になった直後など)何もしない。

```csharp
public void PumpFromBackground()
```
