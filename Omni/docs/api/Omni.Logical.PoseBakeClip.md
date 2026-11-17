# <a id="Omni_Logical_PoseBakeClip"></a> Class PoseBakeClip

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Omni.Sequencer.Runtime.dll  

ベイク済みLogical姿勢を1区間ぶん再生するクリップです。

<p>
クリップ自体はサンプルを持たず、シーケンス全体で1つの<xref href="Omni.Logical.PoseBake" data-throw-if-not-resolved="false"></xref>を
指します。ショットごとにサンプル列を分割すると、境界でサンプルが二重に必要になり、
クリップを動かすたびにベイク全体を作り直すことになるためです。クリップは
「シーケンス時刻のこの区間を、このチャンネルで駆動する」ことだけを持ちます。
</p>

```csharp
[Serializable]
[MovedFrom(true, "Omni.Sequencer.Timeline", null, "LogicalPoseBakeClip")]
public class PoseBakeClip : PlayableAsset, IPlayableAsset, ITimelineClipAsset
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
ScriptableObject ← 
PlayableAsset ← 
[PoseBakeClip](Omni.Logical.PoseBakeClip.md)

#### 実装するインターフェース（Implements）

IPlayableAsset, 
ITimelineClipAsset

## プロパティ（Properties）

### <a id="Omni_Logical_PoseBakeClip_Bake"></a> Bake

参照するベイクアセット。未設定ならリアルタイム経路へ倒れます。

```csharp
public PoseBake Bake { get; set; }
```

#### 値（Property Value）

 [PoseBake](Omni.Logical.PoseBake.md)

### <a id="Omni_Logical_PoseBakeClip_ChannelTargetPath"></a> ChannelTargetPath

駆動対象のチャンネル識別子（"Camera" / "KeyLight" など）。

```csharp
public string ChannelTargetPath { get; set; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Logical_PoseBakeClip_ClipStart"></a> ClipStart

このクリップがシーケンス上で始まる時刻（秒）。
<xref href="Omni.Logical.PoseBakeTrack.CreateTrackMixer(UnityEngine.Playables.PlayableGraph%2cUnityEngine.GameObject%2cSystem.Int32)" data-throw-if-not-resolved="false"></xref> が毎回書き込みます。
クリップをドラッグしただけでベイクが無効にならないよう、シリアライズはしません。

```csharp
public double ClipStart { get; set; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Logical_PoseBakeClip_clipCaps"></a> clipCaps

ブレンドもループも許可しません。ショット境界は「切り替わる」のが正しく、
2つのショットのカメラ姿勢を混ぜた中間姿勢には意味がないためです。

```csharp
public ClipCaps clipCaps { get; }
```

#### 値（Property Value）

 ClipCaps

## メソッド（Methods）

### <a id="Omni_Logical_PoseBakeClip_CreatePlayable_UnityEngine_Playables_PlayableGraph_UnityEngine_GameObject_"></a> CreatePlayable\(PlayableGraph, GameObject\)

<p>Implement this method to have your asset inject playables into the given graph.</p>

```csharp
public override Playable CreatePlayable(PlayableGraph graph, GameObject owner)
```

#### 引数（Parameters）

`graph` PlayableGraph

The graph to inject playables into.

`owner` GameObject

The game object which initiated the build.

#### 戻り値（Returns）

 Playable

<p>The playable injected into the graph, or the root playable if multiple playables are injected.</p>
