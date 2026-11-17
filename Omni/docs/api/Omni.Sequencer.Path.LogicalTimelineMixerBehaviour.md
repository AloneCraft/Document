# <a id="Omni_Sequencer_Path_LogicalTimelineMixerBehaviour"></a> Class LogicalTimelineMixerBehaviour

Namespace: [Omni.Sequencer.Path](Omni.Sequencer.Path.md)  
Assembly: Omni.Sequencer.Runtime.dll  

重みが最大のクリップを1本選び、シーケンス時刻とクリップ内時刻を受け手へ渡す。
受け手が無い・<xref href="Omni.Sequencer.Path.ILogicalTimelineSink" data-throw-if-not-resolved="false"></xref> を実装しないバインドでは何もしない。

```csharp
public class LogicalTimelineMixerBehaviour : PlayableBehaviour, IPlayableBehaviour, ICloneable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
PlayableBehaviour ← 
[LogicalTimelineMixerBehaviour](Omni.Sequencer.Path.LogicalTimelineMixerBehaviour.md)

#### 実装するインターフェース（Implements）

IPlayableBehaviour, 
[ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable)

## プロパティ（Properties）

### <a id="Omni_Sequencer_Path_LogicalTimelineMixerBehaviour_LastClipId"></a> LastClipId

直近に受け手へ渡したクリップ(診断・テスト用)。無ければ null。

```csharp
public string LastClipId { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Sequencer_Path_LogicalTimelineMixerBehaviour_OnPlayableDestroy_UnityEngine_Playables_Playable_"></a> OnPlayableDestroy\(Playable\)

<p>This function is called when the Playable that owns the PlayableBehaviour is destroyed.</p>

```csharp
public override void OnPlayableDestroy(Playable playable)
```

#### 引数（Parameters）

`playable` Playable

The Playable that owns the current PlayableBehaviour.

### <a id="Omni_Sequencer_Path_LogicalTimelineMixerBehaviour_ProcessFrame_UnityEngine_Playables_Playable_UnityEngine_Playables_FrameData_System_Object_"></a> ProcessFrame\(Playable, FrameData, object\)

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
