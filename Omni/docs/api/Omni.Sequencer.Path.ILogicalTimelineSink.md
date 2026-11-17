# <a id="Omni_Sequencer_Path_ILogicalTimelineSink"></a> Interface ILogicalTimelineSink

Namespace: [Omni.Sequencer.Path](Omni.Sequencer.Path.md)  
Assembly: Omni.Sequencer.Runtime.dll  

Timeline の評価の受け手。ミキサーは書き込み先を直接書かず、ここへ時刻を渡すだけにする。
書くのは受け手(各デモの監督クラス)で、今の書き手を変えない。

```csharp
public interface ILogicalTimelineSink
```

## メソッド（Methods）

### <a id="Omni_Sequencer_Path_ILogicalTimelineSink_Present_Omni_Sequencer_Path_LogicalTimelineSample__"></a> Present\(in LogicalTimelineSample\)

有効なクリップの時刻を受け取る。

```csharp
void Present(in LogicalTimelineSample sample)
```

#### 引数（Parameters）

`sample` [LogicalTimelineSample](Omni.Sequencer.Path.LogicalTimelineSample.md)

### <a id="Omni_Sequencer_Path_ILogicalTimelineSink_PresentNone_System_Double_"></a> PresentNone\(double\)

有効なクリップが無い時刻(クリップの間や範囲外)。

```csharp
void PresentNone(double sequenceSeconds)
```

#### 引数（Parameters）

`sequenceSeconds` [double](https://learn.microsoft.com/dotnet/api/system.double)
