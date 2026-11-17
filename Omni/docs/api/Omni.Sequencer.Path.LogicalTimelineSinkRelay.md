# <a id="Omni_Sequencer_Path_LogicalTimelineSinkRelay"></a> Class LogicalTimelineSinkRelay

Namespace: [Omni.Sequencer.Path](Omni.Sequencer.Path.md)  
Assembly: Omni.Sequencer.Runtime.dll  

Timeline のバインド先(UnityEngine.Object が必要)と、MonoBehaviour ではない受け手をつなぐ中継。
実行時に <xref href="Omni.Sequencer.Path.LogicalTimelineSinkRelay.Target" data-throw-if-not-resolved="false"></xref> を設定する。Scene へ保存しない(受け手は実行時の物のため)。

```csharp
[AddComponentMenu("")]
public sealed class LogicalTimelineSinkRelay : MonoBehaviour, ILogicalTimelineSink
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[LogicalTimelineSinkRelay](Omni.Sequencer.Path.LogicalTimelineSinkRelay.md)

#### 実装するインターフェース（Implements）

[ILogicalTimelineSink](Omni.Sequencer.Path.ILogicalTimelineSink.md)

## プロパティ（Properties）

### <a id="Omni_Sequencer_Path_LogicalTimelineSinkRelay_Target"></a> Target

転送先。null の間は何もしない。

```csharp
public ILogicalTimelineSink Target { get; set; }
```

#### 値（Property Value）

 [ILogicalTimelineSink](Omni.Sequencer.Path.ILogicalTimelineSink.md)

## メソッド（Methods）

### <a id="Omni_Sequencer_Path_LogicalTimelineSinkRelay_Present_Omni_Sequencer_Path_LogicalTimelineSample__"></a> Present\(in LogicalTimelineSample\)

有効なクリップの時刻を受け取る。

```csharp
public void Present(in LogicalTimelineSample sample)
```

#### 引数（Parameters）

`sample` [LogicalTimelineSample](Omni.Sequencer.Path.LogicalTimelineSample.md)

### <a id="Omni_Sequencer_Path_LogicalTimelineSinkRelay_PresentNone_System_Double_"></a> PresentNone\(double\)

有効なクリップが無い時刻(クリップの間や範囲外)。

```csharp
public void PresentNone(double sequenceSeconds)
```

#### 引数（Parameters）

`sequenceSeconds` [double](https://learn.microsoft.com/dotnet/api/system.double)
