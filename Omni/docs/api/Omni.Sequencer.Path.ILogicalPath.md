# <a id="Omni_Sequencer_Path_ILogicalPath"></a> Interface ILogicalPath

Namespace: [Omni.Sequencer.Path](Omni.Sequencer.Path.md)  
Assembly: Omni.Sequencer.Runtime.dll  

時刻(秒) → 意図。開始時に確定し、途中で変えない純関数。

```csharp
public interface ILogicalPath
```

## プロパティ（Properties）

### <a id="Omni_Sequencer_Path_ILogicalPath_Duration"></a> Duration

```csharp
double Duration { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

## メソッド（Methods）

### <a id="Omni_Sequencer_Path_ILogicalPath_TryEvaluate_System_Double_Omni_Sequencer_Path_LogicalPathIntent__"></a> TryEvaluate\(double, out LogicalPathIntent\)

```csharp
bool TryEvaluate(double seconds, out LogicalPathIntent intent)
```

#### 引数（Parameters）

`seconds` [double](https://learn.microsoft.com/dotnet/api/system.double)

`intent` [LogicalPathIntent](Omni.Sequencer.Path.LogicalPathIntent.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
