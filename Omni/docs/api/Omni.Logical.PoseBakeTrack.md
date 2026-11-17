# <a id="Omni_Logical_PoseBakeTrack"></a> Class PoseBakeTrack

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Omni.Sequencer.Runtime.dll  

ベイク済みLogical姿勢で<xref href="Omni.Logical.Transform" data-throw-if-not-resolved="false"></xref>を駆動するトラックです。

<p>
Timeline標準のAnimationTrackは使えません。あちらはUnity Transformを直接書くため、
「LogicalTransformがTransformの唯一の書き手」という不変条件を壊し、
巨大座標では姿勢がfloatへ丸められて論理値と食い違うためです。
</p>

```csharp
[TrackClipType(typeof(PoseBakeClip))]
[TrackBindingType(typeof(Transform))]
[TrackColor(0.32, 0.62, 0.86)]
[MovedFrom(true, "Omni.Sequencer.Timeline", null, "LogicalPoseBakeTrack")]
public class PoseBakeTrack : TrackAsset, IPlayableAsset, ISerializationCallbackReceiver, IPropertyPreview
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
ScriptableObject ← 
PlayableAsset ← 
TrackAsset ← 
[PoseBakeTrack](Omni.Logical.PoseBakeTrack.md)

#### 実装するインターフェース（Implements）

IPlayableAsset, 
ISerializationCallbackReceiver, 
IPropertyPreview

## プロパティ（Properties）

### <a id="Omni_Logical_PoseBakeTrack_ChannelTargetPath"></a> ChannelTargetPath

このトラックが駆動するチャンネル識別子。

```csharp
public string ChannelTargetPath { get; set; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Logical_PoseBakeTrack_AssignClipStarts"></a> AssignClipStarts\(\)

クリップの開始時刻をクリップアセットへ書き戻します(診断用)。
焼き込みはクリップの中の時刻で読む(標準のクリップと同じ。<xref href="Omni.Logical.PoseBakeTrack.TrySamplePose(UnityEngine.Timeline.TimelineAsset%2cSystem.String%2cSystem.Double%2cSystem.String%2cSystem.String%2cSystem.String%2cOmni.Logical.Position3%40%2cOmni.Logical.Quaternion%40%2cOmni.Logical.PoseBakeRejection%40)" data-throw-if-not-resolved="false"></xref>)ので、再生には使いません。

```csharp
protected void AssignClipStarts()
```

### <a id="Omni_Logical_PoseBakeTrack_ConfigureMixer_Omni_Logical_BakeMixerBehaviour_UnityEngine_GameObject_"></a> ConfigureMixer\(BakeMixerBehaviour, GameObject\)

ミキサーへ、切り替え判定に必要な参照を渡します。

```csharp
protected void ConfigureMixer(BakeMixerBehaviour behaviour, GameObject go)
```

#### 引数（Parameters）

`behaviour` [BakeMixerBehaviour](Omni.Logical.BakeMixerBehaviour.md)

生成したミキサーのビヘイビア。

`go` GameObject

<code>PlayableDirector</code>が付いているGameObject。

### <a id="Omni_Logical_PoseBakeTrack_CreateMixerPlayable_UnityEngine_Playables_PlayableGraph_System_Int32_Omni_Logical_BakeMixerBehaviour__"></a> CreateMixerPlayable\(PlayableGraph, int, out BakeMixerBehaviour\)

ミキサーのPlayableを作ります。Profilerマーカーを足したい演出は、
これをoverrideして派生ビヘイビアを返します。

<p>
ビヘイビアをoutで一緒に返すのは、<code>ScriptPlayable&lt;T&gt;</code>の型引数が
<code>new()</code>制約を要求するため、抽象基底では取り出せないからです。
生成した側だけが具体型を知っているので、そこで取り出して渡します。
</p>

```csharp
protected virtual Playable CreateMixerPlayable(PlayableGraph graph, int inputCount, out BakeMixerBehaviour behaviour)
```

#### 引数（Parameters）

`graph` PlayableGraph

再生グラフ。

`inputCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

クリップ数。

`behaviour` [BakeMixerBehaviour](Omni.Logical.BakeMixerBehaviour.md)

生成したミキサーのビヘイビア。

#### 戻り値（Returns）

 Playable

### <a id="Omni_Logical_PoseBakeTrack_CreateTrackMixer_UnityEngine_Playables_PlayableGraph_UnityEngine_GameObject_System_Int32_"></a> CreateTrackMixer\(PlayableGraph, GameObject, int\)

```csharp
public override Playable CreateTrackMixer(PlayableGraph graph, GameObject go, int inputCount)
```

#### 引数（Parameters）

`graph` PlayableGraph

`go` GameObject

`inputCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 Playable

### <a id="Omni_Logical_PoseBakeTrack_GatherProperties_UnityEngine_Playables_PlayableDirector_UnityEngine_Timeline_IPropertyCollector_"></a> GatherProperties\(PlayableDirector, IPropertyCollector\)

プレビュー(スクラブ)で書き換える Logical Transform と、それが書く Unity の Transform を登録します。
標準の Animation トラックと同じく、プレビューを終えると元の値へ戻り、Scene も「変更あり」になりません。

```csharp
public override void GatherProperties(PlayableDirector director, IPropertyCollector driver)
```

#### 引数（Parameters）

`director` PlayableDirector

`driver` IPropertyCollector

### <a id="Omni_Logical_PoseBakeTrack_TrySamplePose_UnityEngine_Timeline_TimelineAsset_System_String_System_Double_System_String_System_String_System_String_Omni_Logical_Position3__Omni_Logical_Quaternion__Omni_Logical_PoseBakeRejection__"></a> TrySamplePose\(TimelineAsset, string, double, string, string, string, out Position3, out Quaternion, out PoseBakeRejection\)

Timeline の時刻 <code class="paramref">seconds</code> の、チャンネル <code class="paramref">channelPath</code> の姿勢を、アセットの焼き込みから読む(再生と同じ時刻の対応)。
その時刻に有効な焼き込みのクリップ(最初に見つかったもの)のクリップの中の時刻 = (seconds − start) × timeScale + clipIn で読む。
有効なクリップが無い・焼き込みが検証を通らない・チャンネルが無いときは false と理由を返す。Play の外(先読み・代わりの姿勢)から使う。

```csharp
public static bool TrySamplePose(TimelineAsset timeline, string channelPath, double seconds, string expectedSceneGuid, string expectedSourceGuid, string expectedContentHash, out Position3 position, out Quaternion rotation, out PoseBakeRejection rejection)
```

#### 引数（Parameters）

`timeline` TimelineAsset

`channelPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`seconds` [double](https://learn.microsoft.com/dotnet/api/system.double)

`expectedSceneGuid` [string](https://learn.microsoft.com/dotnet/api/system.string)

`expectedSourceGuid` [string](https://learn.microsoft.com/dotnet/api/system.string)

`expectedContentHash` [string](https://learn.microsoft.com/dotnet/api/system.string)

`position` Position3

`rotation` Quaternion

`rejection` [PoseBakeRejection](Omni.Logical.PoseBakeRejection.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
