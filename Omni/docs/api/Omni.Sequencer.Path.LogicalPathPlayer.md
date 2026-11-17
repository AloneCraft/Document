# <a id="Omni_Sequencer_Path_LogicalPathPlayer"></a> Class LogicalPathPlayer

Namespace: [Omni.Sequencer.Path](Omni.Sequencer.Path.md)  
Assembly: Omni.Sequencer.Runtime.dll  

経路の再生器(Unity に依存しない)。時計はゲートが許可した秒数だけ進む。先行カーソルは再生位置から
<xref href="Omni.Sequencer.Path.LogicalPathPlayer.HorizonSeconds" data-throw-if-not-resolved="false"></xref> 先までの要点を、期限の近い順・画面への寄与が大きい順に差し出す。時計が止まっている間も差し出し続ける。
失敗(ゲートの理由、経路の評価失敗)は有限に終える。

```csharp
public sealed class LogicalPathPlayer
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[LogicalPathPlayer](Omni.Sequencer.Path.LogicalPathPlayer.md)

## コンストラクター（Constructors）

### <a id="Omni_Sequencer_Path_LogicalPathPlayer__ctor_Omni_Sequencer_Path_ILogicalPath_Omni_Sequencer_Path_ILogicalPathGate_Omni_Sequencer_Path_ILogicalPathLookahead_System_Collections_Generic_IReadOnlyList_Omni_Sequencer_Path_LogicalPathKeypoint__"></a> LogicalPathPlayer\(ILogicalPath, ILogicalPathGate, ILogicalPathLookahead, IReadOnlyList<LogicalPathKeypoint\>\)

```csharp
public LogicalPathPlayer(ILogicalPath path, ILogicalPathGate gate, ILogicalPathLookahead lookahead = null, IReadOnlyList<LogicalPathKeypoint> keypoints = null)
```

#### 引数（Parameters）

`path` [ILogicalPath](Omni.Sequencer.Path.ILogicalPath.md)

`gate` [ILogicalPathGate](Omni.Sequencer.Path.ILogicalPathGate.md)

`lookahead` [ILogicalPathLookahead](Omni.Sequencer.Path.ILogicalPathLookahead.md)

`keypoints` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[LogicalPathKeypoint](Omni.Sequencer.Path.LogicalPathKeypoint.md)\>

## プロパティ（Properties）

### <a id="Omni_Sequencer_Path_LogicalPathPlayer_Elapsed"></a> Elapsed

```csharp
public double Elapsed { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Sequencer_Path_LogicalPathPlayer_Failure"></a> Failure

```csharp
public string Failure { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Sequencer_Path_LogicalPathPlayer_Finished"></a> Finished

```csharp
public bool Finished { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Sequencer_Path_LogicalPathPlayer_HorizonSeconds"></a> HorizonSeconds

先読みする長さ(秒)。生成の遅れの実測から伸び縮みさせる。

```csharp
public double HorizonSeconds { get; set; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Sequencer_Path_LogicalPathPlayer_Keypoints"></a> Keypoints

```csharp
public IReadOnlyList<LogicalPathKeypoint> Keypoints { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[LogicalPathKeypoint](Omni.Sequencer.Path.LogicalPathKeypoint.md)\>

### <a id="Omni_Sequencer_Path_LogicalPathPlayer_Path"></a> Path

```csharp
public ILogicalPath Path { get; }
```

#### 値（Property Value）

 [ILogicalPath](Omni.Sequencer.Path.ILogicalPath.md)

### <a id="Omni_Sequencer_Path_LogicalPathPlayer_PendingKeypoints"></a> PendingKeypoints

直前の差し出しで処理されなかった要点の数。

```csharp
public int PendingKeypoints { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_Sequencer_Path_LogicalPathPlayer_Abort_System_String_"></a> Abort\(string\)

経路を外から止める(操作による中断など)。

```csharp
public void Abort(string reason)
```

#### 引数（Parameters）

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Sequencer_Path_LogicalPathPlayer_Advance_System_Double_"></a> Advance\(double\)

実時間 <code class="paramref">deltaSeconds</code> 分を要求し、許可された秒数だけ進める。進んだ秒数を返す。

```csharp
public double Advance(double deltaSeconds)
```

#### 引数（Parameters）

`deltaSeconds` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Sequencer_Path_LogicalPathPlayer_IsKeypointDone_System_Int32_"></a> IsKeypointDone\(int\)

要点が処理済みか(テスト・診断用)。

```csharp
public bool IsKeypointDone(int index)
```

#### 引数（Parameters）

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Sequencer_Path_LogicalPathPlayer_TryCurrentIntent_Omni_Sequencer_Path_LogicalPathIntent__"></a> TryCurrentIntent\(out LogicalPathIntent\)

現在の再生位置の意図。

```csharp
public bool TryCurrentIntent(out LogicalPathIntent intent)
```

#### 引数（Parameters）

`intent` [LogicalPathIntent](Omni.Sequencer.Path.LogicalPathIntent.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
