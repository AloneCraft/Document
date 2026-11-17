# <a id="Omni_Sequencer_Path_LogicalPathKeypoint"></a> Struct LogicalPathKeypoint

Namespace: [Omni.Sequencer.Path](Omni.Sequencer.Path.md)  
Assembly: Omni.Sequencer.Runtime.dll  

先読みの要点。

```csharp
public readonly struct LogicalPathKeypoint
```

## コンストラクター（Constructors）

### <a id="Omni_Sequencer_Path_LogicalPathKeypoint__ctor_System_Double_Omni_Sequencer_Path_LogicalPathIntent__System_Double_System_Double_System_Boolean_"></a> LogicalPathKeypoint\(double, in LogicalPathIntent, double, double, bool\)

```csharp
public LogicalPathKeypoint(double seconds, in LogicalPathIntent intent, double slack, double contribution, bool arrival)
```

#### 引数（Parameters）

`seconds` [double](https://learn.microsoft.com/dotnet/api/system.double)

`intent` [LogicalPathIntent](Omni.Sequencer.Path.LogicalPathIntent.md)

`slack` [double](https://learn.microsoft.com/dotnet/api/system.double)

`contribution` [double](https://learn.microsoft.com/dotnet/api/system.double)

`arrival` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## フィールド（Fields）

### <a id="Omni_Sequencer_Path_LogicalPathKeypoint_Arrival"></a> Arrival

```csharp
public readonly bool Arrival
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Sequencer_Path_LogicalPathKeypoint_Contribution"></a> Contribution

画面への寄与の目安(大きいほど先に読む)。

```csharp
public readonly double Contribution
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Sequencer_Path_LogicalPathKeypoint_Intent"></a> Intent

```csharp
public readonly LogicalPathIntent Intent
```

#### 値（Field Value）

 [LogicalPathIntent](Omni.Sequencer.Path.LogicalPathIntent.md)

### <a id="Omni_Sequencer_Path_LogicalPathKeypoint_Seconds"></a> Seconds

```csharp
public readonly double Seconds
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Sequencer_Path_LogicalPathKeypoint_Slack"></a> Slack

再生位置から、この要点の時刻までの余裕(秒)。差し出すときに更新する。

```csharp
public readonly double Slack
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

## メソッド（Methods）

### <a id="Omni_Sequencer_Path_LogicalPathKeypoint_WithSlack_System_Double_"></a> WithSlack\(double\)

```csharp
public LogicalPathKeypoint WithSlack(double slack)
```

#### 引数（Parameters）

`slack` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [LogicalPathKeypoint](Omni.Sequencer.Path.LogicalPathKeypoint.md)
