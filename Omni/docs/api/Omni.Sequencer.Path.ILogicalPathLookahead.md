# <a id="Omni_Sequencer_Path_ILogicalPathLookahead"></a> Interface ILogicalPathLookahead

Namespace: [Omni.Sequencer.Path](Omni.Sequencer.Path.md)  
Assembly: Omni.Sequencer.Runtime.dll  

先読みの受け口。要点を予算内で処理し、処理しきれなかった数を返す。

```csharp
public interface ILogicalPathLookahead
```

## メソッド（Methods）

### <a id="Omni_Sequencer_Path_ILogicalPathLookahead_Offer_System_Collections_Generic_IReadOnlyList_Omni_Sequencer_Path_LogicalPathKeypoint__"></a> Offer\(IReadOnlyList<LogicalPathKeypoint\>\)

```csharp
int Offer(IReadOnlyList<LogicalPathKeypoint> keypoints)
```

#### 引数（Parameters）

`keypoints` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[LogicalPathKeypoint](Omni.Sequencer.Path.LogicalPathKeypoint.md)\>

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)
