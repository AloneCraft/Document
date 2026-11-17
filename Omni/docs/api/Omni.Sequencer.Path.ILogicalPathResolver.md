# <a id="Omni_Sequencer_Path_ILogicalPathResolver"></a> Interface ILogicalPathResolver

Namespace: [Omni.Sequencer.Path](Omni.Sequencer.Path.md)  
Assembly: Omni.Sequencer.Runtime.dll  

意図 → Logical の姿勢。予測と配置が同じ解決器を通る。

```csharp
public interface ILogicalPathResolver
```

## メソッド（Methods）

### <a id="Omni_Sequencer_Path_ILogicalPathResolver_TryResolve_Omni_Sequencer_Path_LogicalPathIntent__Omni_Sequencer_Path_LogicalPose__"></a> TryResolve\(in LogicalPathIntent, out LogicalPose\)

```csharp
bool TryResolve(in LogicalPathIntent intent, out LogicalPose pose)
```

#### 引数（Parameters）

`intent` [LogicalPathIntent](Omni.Sequencer.Path.LogicalPathIntent.md)

`pose` [LogicalPose](Omni.Sequencer.Path.LogicalPose.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
