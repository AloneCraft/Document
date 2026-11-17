# <a id="Omni_Logical_LightBakeTrack"></a> Class LightBakeTrack

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Omni.Sequencer.Runtime.dll  

ベイク済みLogical回転で<xref href="UnityEngine.Light" data-throw-if-not-resolved="false"></xref>を駆動するトラックです。

<p>
光源の姿勢はカメラの向きから毎フレーム導出していましたが、演出が固定なら
これも時刻の純関数です。焼いてしまえば、カメラのワールド論理姿勢を解決する
処理そのものが再生時から消えます。
</p>

```csharp
[TrackClipType(typeof(PoseBakeClip))]
[TrackBindingType(typeof(Light))]
[TrackColor(0.94, 0.82, 0.36)]
[MovedFrom(true, "Omni.Sequencer.Timeline", null, "LogicalLightBakeTrack")]
public class LightBakeTrack : TrackAsset, IPlayableAsset, ISerializationCallbackReceiver, IPropertyPreview
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
ScriptableObject ← 
PlayableAsset ← 
TrackAsset ← 
[LightBakeTrack](Omni.Logical.LightBakeTrack.md)

#### 実装するインターフェース（Implements）

IPlayableAsset, 
ISerializationCallbackReceiver, 
IPropertyPreview

## プロパティ（Properties）

### <a id="Omni_Logical_LightBakeTrack_ChannelTargetPath"></a> ChannelTargetPath

このトラックが駆動するチャンネル識別子。

```csharp
public string ChannelTargetPath { get; set; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Logical_LightBakeTrack_CreateMixerPlayable_UnityEngine_Playables_PlayableGraph_System_Int32_Omni_Logical_BakeMixerBehaviour__"></a> CreateMixerPlayable\(PlayableGraph, int, out BakeMixerBehaviour\)

ミキサーのPlayableを作ります。Profilerマーカーを足したい演出は、
これをoverrideして派生ビヘイビアを返します。

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

### <a id="Omni_Logical_LightBakeTrack_CreateTrackMixer_UnityEngine_Playables_PlayableGraph_UnityEngine_GameObject_System_Int32_"></a> CreateTrackMixer\(PlayableGraph, GameObject, int\)

```csharp
public override Playable CreateTrackMixer(PlayableGraph graph, GameObject go, int inputCount)
```

#### 引数（Parameters）

`graph` PlayableGraph

`go` GameObject

`inputCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 Playable
