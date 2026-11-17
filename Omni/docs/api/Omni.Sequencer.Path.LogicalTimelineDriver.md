# <a id="Omni_Sequencer_Path_LogicalTimelineDriver"></a> Class LogicalTimelineDriver

Namespace: [Omni.Sequencer.Path](Omni.Sequencer.Path.md)  
Assembly: Omni.Sequencer.Runtime.dll  

<xref href="Omni.Sequencer.Path.LogicalTimelineClock" data-throw-if-not-resolved="false"></xref> の時刻で <code>PlayableDirector</code> を評価する。
Director は手動更新にし、Timeline 自身の時計では進めない(進める量はゲートが決めるため)。
単発の移動のために、実行時に1本の Timeline を組むこともできる。

```csharp
public sealed class LogicalTimelineDriver
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[LogicalTimelineDriver](Omni.Sequencer.Path.LogicalTimelineDriver.md)

## コンストラクター（Constructors）

### <a id="Omni_Sequencer_Path_LogicalTimelineDriver__ctor_UnityEngine_Playables_PlayableDirector_"></a> LogicalTimelineDriver\(PlayableDirector\)

既存の Director(アセットとバインドは設定済み)を手動更新で使う。

```csharp
public LogicalTimelineDriver(PlayableDirector director)
```

#### 引数（Parameters）

`director` PlayableDirector

## プロパティ（Properties）

### <a id="Omni_Sequencer_Path_LogicalTimelineDriver_Director"></a> Director

```csharp
public PlayableDirector Director { get; }
```

#### 値（Property Value）

 PlayableDirector

### <a id="Omni_Sequencer_Path_LogicalTimelineDriver_Duration"></a> Duration

Timeline 全体の長さ(秒)。

```csharp
public double Duration { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

## メソッド（Methods）

### <a id="Omni_Sequencer_Path_LogicalTimelineDriver_AddClips_UnityEngine_Timeline_TimelineAsset_System_Collections_Generic_IReadOnlyList_Omni_Sequencer_Path_LogicalTimelineClipSpec__System_String_"></a> AddClips\(TimelineAsset, IReadOnlyList<LogicalTimelineClipSpec\>, string\)

保存用の Timeline の中身(Logical のトラック1本とクリップ)を <code class="paramref">asset</code> へ足す。作った物を返す(エディタがアセットへ保存する)。

```csharp
public static LogicalTimelineTrack AddClips(TimelineAsset asset, IReadOnlyList<LogicalTimelineClipSpec> clips, string trackName = "Logical")
```

#### 引数（Parameters）

`asset` TimelineAsset

`clips` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[LogicalTimelineClipSpec](Omni.Sequencer.Path.LogicalTimelineClipSpec.md)\>

`trackName` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [LogicalTimelineTrack](Omni.Sequencer.Path.LogicalTimelineTrack.md)

### <a id="Omni_Sequencer_Path_LogicalTimelineDriver_Create_UnityEngine_Playables_PlayableDirector_UnityEngine_MonoBehaviour_System_Collections_Generic_IReadOnlyList_Omni_Sequencer_Path_LogicalTimelineClipSpec__System_String_"></a> Create\(PlayableDirector, MonoBehaviour, IReadOnlyList<LogicalTimelineClipSpec\>, string\)

実行時に Timeline を組んで <code class="paramref">director</code> へ設定し、<code class="paramref">sink</code> をトラックへ結ぶ。
作ったアセットは保存しない(Scene・プロジェクトへ残さない)。

```csharp
public static LogicalTimelineDriver Create(PlayableDirector director, MonoBehaviour sink, IReadOnlyList<LogicalTimelineClipSpec> clips, string name = "Logical Timeline")
```

#### 引数（Parameters）

`director` PlayableDirector

`sink` MonoBehaviour

`clips` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[LogicalTimelineClipSpec](Omni.Sequencer.Path.LogicalTimelineClipSpec.md)\>

`name` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [LogicalTimelineDriver](Omni.Sequencer.Path.LogicalTimelineDriver.md)

### <a id="Omni_Sequencer_Path_LogicalTimelineDriver_Create_UnityEngine_Playables_PlayableDirector_Omni_Sequencer_Path_ILogicalTimelineSink_System_Collections_Generic_IReadOnlyList_Omni_Sequencer_Path_LogicalTimelineClipSpec__System_String_"></a> Create\(PlayableDirector, ILogicalTimelineSink, IReadOnlyList<LogicalTimelineClipSpec\>, string\)

MonoBehaviour ではない受け手を、Director と同じ GameObject の <xref href="Omni.Sequencer.Path.LogicalTimelineSinkRelay" data-throw-if-not-resolved="false"></xref> 経由で結ぶ。
中継は無ければ足し、Scene へ保存しない。

```csharp
public static LogicalTimelineDriver Create(PlayableDirector director, ILogicalTimelineSink sink, IReadOnlyList<LogicalTimelineClipSpec> clips, string name = "Logical Timeline")
```

#### 引数（Parameters）

`director` PlayableDirector

`sink` [ILogicalTimelineSink](Omni.Sequencer.Path.ILogicalTimelineSink.md)

`clips` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[LogicalTimelineClipSpec](Omni.Sequencer.Path.LogicalTimelineClipSpec.md)\>

`name` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [LogicalTimelineDriver](Omni.Sequencer.Path.LogicalTimelineDriver.md)

### <a id="Omni_Sequencer_Path_LogicalTimelineDriver_Evaluate_System_Double_"></a> Evaluate\(double\)

再生位置 <code class="paramref">seconds</code> で評価する。終わりの時刻ちょうどでも最後のクリップを評価するよう、
長さの直前へ収める(Timeline のクリップは終わりの時刻を含まない)。

```csharp
public void Evaluate(double seconds)
```

#### 引数（Parameters）

`seconds` [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Sequencer_Path_LogicalTimelineDriver_Evaluate_Omni_Sequencer_Path_LogicalTimelineClock_"></a> Evaluate\(LogicalTimelineClock\)

時計の今の時刻で評価する。

```csharp
public void Evaluate(LogicalTimelineClock clock)
```

#### 引数（Parameters）

`clock` [LogicalTimelineClock](Omni.Sequencer.Path.LogicalTimelineClock.md)

### <a id="Omni_Sequencer_Path_LogicalTimelineDriver_Release"></a> Release\(\)

<xref href="Omni.Sequencer.Path.LogicalTimelineDriver.Create(UnityEngine.Playables.PlayableDirector%2cUnityEngine.MonoBehaviour%2cSystem.Collections.Generic.IReadOnlyList%7bOmni.Sequencer.Path.LogicalTimelineClipSpec%7d%2cSystem.String)" data-throw-if-not-resolved="false"></xref> が作った Timeline を破棄する(単発の移動の後)。
Director がまだそのアセットを再生していれば外す。既存のアセットを渡した Driver では何もしない。

```csharp
public void Release()
```

### <a id="Omni_Sequencer_Path_LogicalTimelineDriver_TryReadClips_UnityEngine_Timeline_TimelineAsset_System_Collections_Generic_List_Omni_Sequencer_Path_LogicalTimelineClipSpec___System_String__"></a> TryReadClips\(TimelineAsset, out List<LogicalTimelineClipSpec\>, out string\)

保存した Timeline の Logical のクリップ(識別子・開始・長さ)を、開始の順に読む。アセットが正本で、これはその読み出し。
外れたら(Logical のトラックが無い、クリップが無い、識別子が空、長さが 0 以下、クリップが重なる)false と理由を返す(Fail Closed)。

```csharp
public static bool TryReadClips(TimelineAsset asset, out List<LogicalTimelineClipSpec> clips, out string error)
```

#### 引数（Parameters）

`asset` TimelineAsset

`clips` [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[LogicalTimelineClipSpec](Omni.Sequencer.Path.LogicalTimelineClipSpec.md)\>

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Sequencer_Path_LogicalTimelineDriver_Use_UnityEngine_Playables_PlayableDirector_UnityEngine_Timeline_TimelineAsset_UnityEngine_MonoBehaviour_"></a> Use\(PlayableDirector, TimelineAsset, MonoBehaviour\)

プロジェクトに保存した Timeline(デザイン時に作ったアセット)を <code class="paramref">director</code> で使い、
中の <xref href="Omni.Sequencer.Path.LogicalTimelineTrack" data-throw-if-not-resolved="false"></xref> をすべて <code class="paramref">sink</code> へ結ぶ。アセットは破棄しない。

```csharp
public static LogicalTimelineDriver Use(PlayableDirector director, TimelineAsset asset, MonoBehaviour sink)
```

#### 引数（Parameters）

`director` PlayableDirector

`asset` TimelineAsset

`sink` MonoBehaviour

#### 戻り値（Returns）

 [LogicalTimelineDriver](Omni.Sequencer.Path.LogicalTimelineDriver.md)
