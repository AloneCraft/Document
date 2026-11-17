# <a id="Omni_Streaming_Unity_WebBackgroundPump"></a> Class WebBackgroundPump

Namespace: [Omni.Streaming.Unity](Omni.Streaming.Unity.md)  
Assembly: Omni.Streaming.Unity.dll  

ブラウザ(WebGL)でタブが背面のとき、<xref href="Omni.Streaming.Unity.StreamingBehaviour" data-throw-if-not-resolved="false"></xref> を約 10 Hz で進める。
ブラウザは隠れたタブの描画ループ(requestAnimationFrame とタイマー)を約 1 秒に 1 回へ絞るので、Update だけで進めると、取得の完了の検出と次の要求の発行が 1 fps に落ちる。
Web Worker のタイマーは絞られないので、そこから(<code>OmniStreaming.jslib</code>)隠れているときだけ <code>Module.SendMessage</code> で <xref href="Omni.Streaming.Unity.WebBackgroundPump.OnPump" data-throw-if-not-resolved="false"></xref> を呼ぶ。
<xref href="Omni.Streaming.Unity.StreamingBehaviour.BackgroundPump" data-throw-if-not-resolved="false"></xref> を true にした利用者だけが対象。他のプラットフォーム・Editor では何もしない。

```csharp
public sealed class WebBackgroundPump : MonoBehaviour
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[WebBackgroundPump](Omni.Streaming.Unity.WebBackgroundPump.md)

## フィールド（Fields）

### <a id="Omni_Streaming_Unity_WebBackgroundPump_IntervalMilliseconds"></a> IntervalMilliseconds

```csharp
public const int IntervalMilliseconds = 100
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_Unity_WebBackgroundPump_ObjectName"></a> ObjectName

```csharp
public const string ObjectName = "OmniStreamingBackgroundPump"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## プロパティ（Properties）

### <a id="Omni_Streaming_Unity_WebBackgroundPump_Pumps"></a> Pumps

背面のポンプで host を進めた回数(診断用)。

```csharp
public static long Pumps { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

## メソッド（Methods）

### <a id="Omni_Streaming_Unity_WebBackgroundPump_Register_Omni_Streaming_Unity_StreamingBehaviour_"></a> Register\(StreamingBehaviour\)

```csharp
public static void Register(StreamingBehaviour behaviour)
```

#### 引数（Parameters）

`behaviour` [StreamingBehaviour](Omni.Streaming.Unity.StreamingBehaviour.md)

### <a id="Omni_Streaming_Unity_WebBackgroundPump_Unregister_Omni_Streaming_Unity_StreamingBehaviour_"></a> Unregister\(StreamingBehaviour\)

```csharp
public static void Unregister(StreamingBehaviour behaviour)
```

#### 引数（Parameters）

`behaviour` [StreamingBehaviour](Omni.Streaming.Unity.StreamingBehaviour.md)
