# <a id="Omni_Streaming_PayloadState"></a> Enum PayloadState

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

キーごとの状態。利用者は Absent(存在の表で「無い」)と Unavailable(取得手段が無い・まだ答えられない)を区別して扱う。

```csharp
public enum PayloadState
```

## フィールド（Fields）

`Absent = 1` 

カタログが「このキーの中身は無い」と答えた(取得も再試行もしない)。



`Failed = 4` 

取得または展開に失敗した。取得の失敗は再試行の上限まで自動で再試行する。上限に達したら <xref href="Omni.Streaming.StreamingHost.Invalidate(Omni.Streaming.StreamKey%40)" data-throw-if-not-resolved="false"></xref> まで止まる。



`Pending = 2` 

取得・展開の途中、または順番待ち。



`Resident = 3` 

展開済みで、<xref href="Omni.Streaming.StreamingHost.TryAcquire(Omni.Streaming.StreamKey%40%2cOmni.Streaming.PayloadLease%40)" data-throw-if-not-resolved="false"></xref> で使える。



`Unavailable = 5` 

カタログが答えられない(読み込めない)。取得手段が無い。一定時間ごとに問い合わせ直す。



`Unknown = 0` 

まだ誰も要求していない(または、使われなくなって記録を捨てた)。
