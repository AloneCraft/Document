# <a id="Omni_Sequencer_Path_LogicalTimelineTrack"></a> Class LogicalTimelineTrack

Namespace: [Omni.Sequencer.Path](Omni.Sequencer.Path.md)  
Assembly: Omni.Sequencer.Runtime.dll  

Logical 座標のデモの再生位置を、受け手(<xref href="Omni.Sequencer.Path.ILogicalTimelineSink" data-throw-if-not-resolved="false"></xref> を実装した MonoBehaviour)へ渡すトラック。

<p>
書き込み先(Logical の Transform、shader の値、場面の有効化)を直接書かない。各デモの今の書き手が、
受け取った時刻で自分の評価を行って書く。SolarSystem ではカメラ制御の状態(モード・追従・天体固定)が書き手なので、
ここで Transform を書くとクリップの終わりで状態が古い値へ戻る。
</p>
<p>
時刻は <xref href="Omni.Sequencer.Path.LogicalTimelineClock" data-throw-if-not-resolved="false"></xref> が持ち、<xref href="Omni.Sequencer.Path.LogicalTimelineDriver" data-throw-if-not-resolved="false"></xref> が
<code>PlayableDirector</code>(手動更新)へ渡して評価する。Timeline はクリップを並べる殻として使う。
</p>

```csharp
[TrackClipType(typeof(LogicalTimelineClip))]
[TrackBindingType(typeof(MonoBehaviour))]
[TrackColor(0.36, 0.74, 0.52)]
public class LogicalTimelineTrack : TrackAsset, IPlayableAsset, ISerializationCallbackReceiver, IPropertyPreview
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
ScriptableObject ← 
PlayableAsset ← 
TrackAsset ← 
[LogicalTimelineTrack](Omni.Sequencer.Path.LogicalTimelineTrack.md)

#### 実装するインターフェース（Implements）

IPlayableAsset, 
ISerializationCallbackReceiver, 
IPropertyPreview

## メソッド（Methods）

### <a id="Omni_Sequencer_Path_LogicalTimelineTrack_CreateTrackMixer_UnityEngine_Playables_PlayableGraph_UnityEngine_GameObject_System_Int32_"></a> CreateTrackMixer\(PlayableGraph, GameObject, int\)

```csharp
public override Playable CreateTrackMixer(PlayableGraph graph, GameObject go, int inputCount)
```

#### 引数（Parameters）

`graph` PlayableGraph

`go` GameObject

`inputCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 Playable

### <a id="Omni_Sequencer_Path_LogicalTimelineTrack_GatherProperties_UnityEngine_Playables_PlayableDirector_UnityEngine_Timeline_IPropertyCollector_"></a> GatherProperties\(PlayableDirector, IPropertyCollector\)

プレビュー(スクラブ)で受け手が書き換える値を登録する。標準のトラックと同じく、プレビューを終えると元の値へ戻る。

```csharp
public override void GatherProperties(PlayableDirector director, IPropertyCollector driver)
```

#### 引数（Parameters）

`director` PlayableDirector

`driver` IPropertyCollector
