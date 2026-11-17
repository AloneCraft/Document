# <a id="Omni_Sequencer_Path_LogicalKeyframeTrack"></a> Class LogicalKeyframeTrack

Namespace: [Omni.Sequencer.Path](Omni.Sequencer.Path.md)  
Assembly: Omni.Sequencer.Runtime.dll  

<xref href="Omni.Sequencer.Path.LogicalKeyframeClip" data-throw-if-not-resolved="false"></xref> を並べるトラック。結び先(<xref href="Omni.Sequencer.Path.ILogicalKeyframeSink" data-throw-if-not-resolved="false"></xref> の MonoBehaviour)へシーケンスの時刻を渡す。
結び先が <xref href="Omni.Sequencer.Path.ILogicalTimelinePreview" data-throw-if-not-resolved="false"></xref> なら、プレビューで書き換える値を登録してもらう(スクラブの後に元へ戻る)。

```csharp
[TrackClipType(typeof(LogicalKeyframeClip))]
[TrackBindingType(typeof(MonoBehaviour))]
[TrackColor(0.86, 0.62, 0.32)]
public class LogicalKeyframeTrack : TrackAsset, IPlayableAsset, ISerializationCallbackReceiver, IPropertyPreview
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
ScriptableObject ← 
PlayableAsset ← 
TrackAsset ← 
[LogicalKeyframeTrack](Omni.Sequencer.Path.LogicalKeyframeTrack.md)

#### 実装するインターフェース（Implements）

IPlayableAsset, 
ISerializationCallbackReceiver, 
IPropertyPreview

## メソッド（Methods）

### <a id="Omni_Sequencer_Path_LogicalKeyframeTrack_CreateTrackMixer_UnityEngine_Playables_PlayableGraph_UnityEngine_GameObject_System_Int32_"></a> CreateTrackMixer\(PlayableGraph, GameObject, int\)

```csharp
public override Playable CreateTrackMixer(PlayableGraph graph, GameObject go, int inputCount)
```

#### 引数（Parameters）

`graph` PlayableGraph

`go` GameObject

`inputCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 Playable

### <a id="Omni_Sequencer_Path_LogicalKeyframeTrack_GatherProperties_UnityEngine_Playables_PlayableDirector_UnityEngine_Timeline_IPropertyCollector_"></a> GatherProperties\(PlayableDirector, IPropertyCollector\)

```csharp
public override void GatherProperties(PlayableDirector director, IPropertyCollector driver)
```

#### 引数（Parameters）

`director` PlayableDirector

`driver` IPropertyCollector
