# <a id="Omni_Sequencer_Path_LogicalKeyframeMixerBehaviour"></a> Class LogicalKeyframeMixerBehaviour

Namespace: [Omni.Sequencer.Path](Omni.Sequencer.Path.md)  
Assembly: Omni.Sequencer.Runtime.dll  

有効なクリップがあれば、シーケンスの時刻を受け手へ渡す。

```csharp
public class LogicalKeyframeMixerBehaviour : PlayableBehaviour, IPlayableBehaviour, ICloneable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
PlayableBehaviour ← 
[LogicalKeyframeMixerBehaviour](Omni.Sequencer.Path.LogicalKeyframeMixerBehaviour.md)

#### 実装するインターフェース（Implements）

IPlayableBehaviour, 
[ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable)

## メソッド（Methods）

### <a id="Omni_Sequencer_Path_LogicalKeyframeMixerBehaviour_OnPlayableDestroy_UnityEngine_Playables_Playable_"></a> OnPlayableDestroy\(Playable\)

<p>This function is called when the Playable that owns the PlayableBehaviour is destroyed.</p>

```csharp
public override void OnPlayableDestroy(Playable playable)
```

#### 引数（Parameters）

`playable` Playable

The Playable that owns the current PlayableBehaviour.

### <a id="Omni_Sequencer_Path_LogicalKeyframeMixerBehaviour_ProcessFrame_UnityEngine_Playables_Playable_UnityEngine_Playables_FrameData_System_Object_"></a> ProcessFrame\(Playable, FrameData, object\)

<p>This function is called during the ProcessFrame phase of the PlayableGraph.</p>

```csharp
public override void ProcessFrame(Playable playable, FrameData info, object playerData)
```

#### 引数（Parameters）

`playable` Playable

The Playable that owns the current PlayableBehaviour.

`info` FrameData

A FrameData structure that contains information about the current frame context.

`playerData` [object](https://learn.microsoft.com/dotnet/api/system.object)

The user data of the ScriptPlayableOutput that initiated the process pass.
