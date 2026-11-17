# <a id="Omni_Sequencer_Path_LogicalTimelineClip"></a> Class LogicalTimelineClip

Namespace: [Omni.Sequencer.Path](Omni.Sequencer.Path.md)  
Assembly: Omni.Sequencer.Runtime.dll  

「この区間は、この識別子の評価で再生する」ことだけを持つクリップ。
中身(経路の式、Cosmic 系の場面の式など)は受け手(<xref href="Omni.Sequencer.Path.ILogicalTimelineSink" data-throw-if-not-resolved="false"></xref>)が識別子から選ぶ。
経路は開始位置で変わるため焼き込まず、受け手が実行時に時刻→姿勢を求める。

```csharp
[Serializable]
public class LogicalTimelineClip : PlayableAsset, IPlayableAsset, ITimelineClipAsset
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
ScriptableObject ← 
PlayableAsset ← 
[LogicalTimelineClip](Omni.Sequencer.Path.LogicalTimelineClip.md)

#### 実装するインターフェース（Implements）

IPlayableAsset, 
ITimelineClipAsset

## プロパティ（Properties）

### <a id="Omni_Sequencer_Path_LogicalTimelineClip_ClipDuration"></a> ClipDuration

シーケンス上の長さ(秒)。トラックがミキサーを作るたびに書く。

```csharp
public double ClipDuration { get; set; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Sequencer_Path_LogicalTimelineClip_ClipId"></a> ClipId

受け手が評価を選ぶ識別子。

```csharp
public string ClipId { get; set; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Sequencer_Path_LogicalTimelineClip_ClipStart"></a> ClipStart

シーケンス上の開始時刻(秒)。トラックがミキサーを作るたびに書く。シリアライズしない。

```csharp
public double ClipStart { get; set; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Sequencer_Path_LogicalTimelineClip_clipCaps"></a> clipCaps

ブレンドしない。2つの評価の出力(カメラ姿勢・shader の値・場面の有効化)を混ぜた中間には意味が無く、
各デモの見た目を変えないことを優先する。

```csharp
public ClipCaps clipCaps { get; }
```

#### 値（Property Value）

 ClipCaps

## メソッド（Methods）

### <a id="Omni_Sequencer_Path_LogicalTimelineClip_CreatePlayable_UnityEngine_Playables_PlayableGraph_UnityEngine_GameObject_"></a> CreatePlayable\(PlayableGraph, GameObject\)

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
