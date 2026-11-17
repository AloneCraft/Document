# <a id="Omni_Sequencer_Path_LogicalPathAnchorKind"></a> Enum LogicalPathAnchorKind

Namespace: [Omni.Sequencer.Path](Omni.Sequencer.Path.md)  
Assembly: Omni.Sequencer.Runtime.dll  

意図の錨。座標の意味は利用者(アプリ)の解決器が決める。Core は天体を知らない。

```csharp
public enum LogicalPathAnchorKind
```

## フィールド（Fields）

`Absolute = 0` 

絶対座標。<xref href="Omni.Sequencer.Path.LogicalPathIntent.Offset" data-throw-if-not-resolved="false"></xref> がそのまま位置になる。



`AnchorFixed = 1` 

錨(例: 天体)と一緒に回る座標系。



`AnchorRelative = 2` 

錨の位置にだけ追従し、向きは絶対座標のまま。
