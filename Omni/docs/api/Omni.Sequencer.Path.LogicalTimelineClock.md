# <a id="Omni_Sequencer_Path_LogicalTimelineClock"></a> Class LogicalTimelineClock

Namespace: [Omni.Sequencer.Path](Omni.Sequencer.Path.md)  
Assembly: Omni.Sequencer.Runtime.dll  

Timeline の再生位置(double 秒)。Unity に依存しない。時刻を進める唯一の所有者で、
デモの監督クラスは「どの時刻を評価するか」をここから受け取る。
進める量は実時間×速さで、ゲートがあれば許可された秒数までに制限する(経路のある移動の「粗くても進む」)。
フレーム時間に依存する積み上げを持たないので、同じ時刻へ通しで着いても Seek で飛んでも同じ時刻になる。

```csharp
public sealed class LogicalTimelineClock
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[LogicalTimelineClock](Omni.Sequencer.Path.LogicalTimelineClock.md)

## コンストラクター（Constructors）

### <a id="Omni_Sequencer_Path_LogicalTimelineClock__ctor_System_Double_Omni_Sequencer_Path_LogicalTimelineWrap_"></a> LogicalTimelineClock\(double, LogicalTimelineWrap\)

```csharp
public LogicalTimelineClock(double duration, LogicalTimelineWrap wrap = LogicalTimelineWrap.Hold)
```

#### 引数（Parameters）

`duration` [double](https://learn.microsoft.com/dotnet/api/system.double)

`wrap` [LogicalTimelineWrap](Omni.Sequencer.Path.LogicalTimelineWrap.md)

## プロパティ（Properties）

### <a id="Omni_Sequencer_Path_LogicalTimelineClock_Duration"></a> Duration

```csharp
public double Duration { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Sequencer_Path_LogicalTimelineClock_Failure"></a> Failure

ゲートが返した失敗の理由。値がある間は進めない(有限に終える)。

```csharp
public string Failure { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Sequencer_Path_LogicalTimelineClock_Finished"></a> Finished

終わりで止まる時計が終わりに着いた。

```csharp
public bool Finished { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Sequencer_Path_LogicalTimelineClock_Loops"></a> Loops

最初へ戻った回数。

```csharp
public int Loops { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Sequencer_Path_LogicalTimelineClock_Playing"></a> Playing

```csharp
public bool Playing { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Sequencer_Path_LogicalTimelineClock_Seconds"></a> Seconds

再生位置(秒)。0 以上 <xref href="Omni.Sequencer.Path.LogicalTimelineClock.Duration" data-throw-if-not-resolved="false"></xref> 以下。

```csharp
public double Seconds { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Sequencer_Path_LogicalTimelineClock_Speed"></a> Speed

実時間1秒あたりに進める再生位置の秒数。0 以上。

```csharp
public double Speed { get; set; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Sequencer_Path_LogicalTimelineClock_Wrap"></a> Wrap

```csharp
public LogicalTimelineWrap Wrap { get; }
```

#### 値（Property Value）

 [LogicalTimelineWrap](Omni.Sequencer.Path.LogicalTimelineWrap.md)

## メソッド（Methods）

### <a id="Omni_Sequencer_Path_LogicalTimelineClock_Abort_System_String_"></a> Abort\(string\)

外から止める(操作による中断など)。最初の理由を残す。

```csharp
public void Abort(string reason)
```

#### 引数（Parameters）

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Sequencer_Path_LogicalTimelineClock_Advance_System_Double_Omni_Sequencer_Path_ILogicalPathGate_Omni_Sequencer_Path_ILogicalPath_"></a> Advance\(double, ILogicalPathGate, ILogicalPath\)

実時間 <code class="paramref">realSeconds</code> 分を進め、実際に進んだ再生位置の秒数を返す。
<code class="paramref">gate</code> があれば、要求した秒数のうち許可された分だけ進める。止まっている・失敗済み・終わりでは 0。

```csharp
public double Advance(double realSeconds, ILogicalPathGate gate = null, ILogicalPath path = null)
```

#### 引数（Parameters）

`realSeconds` [double](https://learn.microsoft.com/dotnet/api/system.double)

`gate` [ILogicalPathGate](Omni.Sequencer.Path.ILogicalPathGate.md)

`path` [ILogicalPath](Omni.Sequencer.Path.ILogicalPath.md)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Sequencer_Path_LogicalTimelineClock_Seek_System_Double_"></a> Seek\(double\)

再生位置を移す。終わりで止まる時計は範囲へ収め、戻る時計は周期で折り返す。失敗は解除しない。

```csharp
public void Seek(double seconds)
```

#### 引数（Parameters）

`seconds` [double](https://learn.microsoft.com/dotnet/api/system.double)
