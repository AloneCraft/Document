# <a id="Omni_Sequencer_Path_LogicalPathPlacement"></a> Enum LogicalPathPlacement

Namespace: [Omni.Sequencer.Path](Omni.Sequencer.Path.md)  
Assembly: Omni.Sequencer.Runtime.dll  

錨に対する位置の表し方。

```csharp
public enum LogicalPathPlacement
```

## フィールド（Fields）

`Offset = 0` 

錨からの相対オフセット(<xref href="Omni.Sequencer.Path.LogicalPathIntent.Offset" data-throw-if-not-resolved="false"></xref>)。



`SurfaceAltitude = 1` 

錨の表面の方向(<xref href="Omni.Sequencer.Path.LogicalPathIntent.Direction" data-throw-if-not-resolved="false"></xref>、単位ベクトル)と、地面からの高度。地面の高さは解決器が当てはめる。
