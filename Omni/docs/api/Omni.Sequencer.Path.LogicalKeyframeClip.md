# <a id="Omni_Sequencer_Path_LogicalKeyframeClip"></a> Class LogicalKeyframeClip

Namespace: [Omni.Sequencer.Path](Omni.Sequencer.Path.md)  
Assembly: Omni.Sequencer.Runtime.dll  

double のキーを持つクリップ。標準の Animation クリップの、float のカーブの代わり(大きな座標や細かい値を float に丸めない)。

<p>
時刻と値の両方がアセットにある(正本)。クリップを動かす・<code>Clip In</code>・速さを変えると、標準のクリップと同じく再生が変わる。
補間はしない。値の意味と補間の式は、受け手(<xref href="Omni.Sequencer.Path.ILogicalKeyframeSink" data-throw-if-not-resolved="false"></xref>)が決める(リグの部品の値をキーにするのと同じ)。
読み出しは <xref href="Omni.Sequencer.Path.LogicalKeyframeSequence.TryRead(UnityEngine.Timeline.TimelineAsset%2cOmni.Sequencer.Path.LogicalKeyframeSequence%40%2cSystem.String%40)" data-throw-if-not-resolved="false"></xref>。
</p>

```csharp
[Serializable]
public class LogicalKeyframeClip : PlayableAsset, IPlayableAsset, ITimelineClipAsset
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
ScriptableObject ← 
PlayableAsset ← 
[LogicalKeyframeClip](Omni.Sequencer.Path.LogicalKeyframeClip.md)

#### 実装するインターフェース（Implements）

IPlayableAsset, 
ITimelineClipAsset

## プロパティ（Properties）

### <a id="Omni_Sequencer_Path_LogicalKeyframeClip_Channels"></a> Channels

チャンネルの名前(各キーの値の並び)。

```csharp
public IReadOnlyList<string> Channels { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Sequencer_Path_LogicalKeyframeClip_Keys"></a> Keys

キー(クリップの中の秒の順)。

```csharp
public IReadOnlyList<LogicalKeyframe> Keys { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[LogicalKeyframe](Omni.Sequencer.Path.LogicalKeyframe.md)\>

### <a id="Omni_Sequencer_Path_LogicalKeyframeClip_clipCaps"></a> clipCaps

Clip In と速さの変更を受け付ける。ブレンドはしない(2 つの経路の中間に意味が無い)。

```csharp
public ClipCaps clipCaps { get; }
```

#### 値（Property Value）

 ClipCaps

### <a id="Omni_Sequencer_Path_LogicalKeyframeClip_duration"></a> duration

クリップの既定の長さ = 最後のキーの時刻(標準の Animation クリップの長さと同じ)。

```csharp
public override double duration { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

## メソッド（Methods）

### <a id="Omni_Sequencer_Path_LogicalKeyframeClip_CreatePlayable_UnityEngine_Playables_PlayableGraph_UnityEngine_GameObject_"></a> CreatePlayable\(PlayableGraph, GameObject\)

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

### <a id="Omni_Sequencer_Path_LogicalKeyframeClip_SetKeys_System_Collections_Generic_IReadOnlyList_System_String__System_Collections_Generic_IEnumerable_Omni_Sequencer_Path_LogicalKeyframe__"></a> SetKeys\(IReadOnlyList<string\>, IEnumerable<LogicalKeyframe\>\)

チャンネルとキーを置き換える(アセットを作るとき)。

```csharp
public void SetKeys(IReadOnlyList<string> channels, IEnumerable<LogicalKeyframe> keys)
```

#### 引数（Parameters）

`channels` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

`keys` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<[LogicalKeyframe](Omni.Sequencer.Path.LogicalKeyframe.md)\>
