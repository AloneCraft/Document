# <a id="Omni_Sequencer_Path_LogicalKeyframeSequence"></a> Class LogicalKeyframeSequence

Namespace: [Omni.Sequencer.Path](Omni.Sequencer.Path.md)  
Assembly: Omni.Sequencer.Runtime.dll  

Timeline のアセットから読んだキーの並び(時刻は Timeline の先頭からの秒)。アセットが正本で、これはその読み出し。

```csharp
public sealed class LogicalKeyframeSequence
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[LogicalKeyframeSequence](Omni.Sequencer.Path.LogicalKeyframeSequence.md)

## プロパティ（Properties）

### <a id="Omni_Sequencer_Path_LogicalKeyframeSequence_Channels"></a> Channels

```csharp
public IReadOnlyList<string> Channels { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Sequencer_Path_LogicalKeyframeSequence_Clip"></a> Clip

読んだクリップ(変更の検出用)。

```csharp
public LogicalKeyframeClip Clip { get; }
```

#### 値（Property Value）

 [LogicalKeyframeClip](Omni.Sequencer.Path.LogicalKeyframeClip.md)

### <a id="Omni_Sequencer_Path_LogicalKeyframeSequence_Count"></a> Count

```csharp
public int Count { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Sequencer_Path_LogicalKeyframeSequence_Labels"></a> Labels

```csharp
public IReadOnlyList<string> Labels { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Sequencer_Path_LogicalKeyframeSequence_Times"></a> Times

キーの時刻(Timeline の先頭からの秒)。増える順。

```csharp
public IReadOnlyList<double> Times { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[double](https://learn.microsoft.com/dotnet/api/system.double)\>

### <a id="Omni_Sequencer_Path_LogicalKeyframeSequence_Values"></a> Values

キーごとの値(チャンネルの順)。

```csharp
public IReadOnlyList<double[]> Values { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[double](https://learn.microsoft.com/dotnet/api/system.double)\[\]\>

## メソッド（Methods）

### <a id="Omni_Sequencer_Path_LogicalKeyframeSequence_ChannelIndex_System_String_"></a> ChannelIndex\(string\)

チャンネルの番号。無ければ -1。

```csharp
public int ChannelIndex(string name)
```

#### 引数（Parameters）

`name` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Sequencer_Path_LogicalKeyframeSequence_TryRead_UnityEngine_Timeline_TimelineAsset_Omni_Sequencer_Path_LogicalKeyframeSequence__System_String__"></a> TryRead\(TimelineAsset, out LogicalKeyframeSequence, out string\)

<code class="paramref">asset</code> の <xref href="Omni.Sequencer.Path.LogicalKeyframeTrack" data-throw-if-not-resolved="false"></xref>(ちょうど 1 本)の、ちょうど 1 本のクリップのキーを読む。
時刻は標準のクリップと同じく <code>start + (key.time − clipIn) ÷ timeScale</code>。
外れたら(トラック・クリップの数、キーが 2 個未満、時刻が増えない・有限でない、値の数がチャンネルの数と違う、キーがクリップの範囲の外)
false と理由を返す(Fail Closed。呼ぶ側はコードの値へ戻らない)。

```csharp
public static bool TryRead(TimelineAsset asset, out LogicalKeyframeSequence sequence, out string error)
```

#### 引数（Parameters）

`asset` TimelineAsset

`sequence` [LogicalKeyframeSequence](Omni.Sequencer.Path.LogicalKeyframeSequence.md)

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Sequencer_Path_LogicalKeyframeSequence_TryRead_Omni_Sequencer_Path_LogicalKeyframeClip_System_Double_System_Double_System_Double_System_Double_Omni_Sequencer_Path_LogicalKeyframeSequence__System_String__"></a> TryRead\(LogicalKeyframeClip, double, double, double, double, out LogicalKeyframeSequence, out string\)

クリップの配置(開始・Clip In・速さ・長さ)を明示して読む(テストと、アセット以外から組む場合)。

```csharp
public static bool TryRead(LogicalKeyframeClip clip, double start, double clipIn, double timeScale, double clipDuration, out LogicalKeyframeSequence sequence, out string error)
```

#### 引数（Parameters）

`clip` [LogicalKeyframeClip](Omni.Sequencer.Path.LogicalKeyframeClip.md)

`start` [double](https://learn.microsoft.com/dotnet/api/system.double)

`clipIn` [double](https://learn.microsoft.com/dotnet/api/system.double)

`timeScale` [double](https://learn.microsoft.com/dotnet/api/system.double)

`clipDuration` [double](https://learn.microsoft.com/dotnet/api/system.double)

`sequence` [LogicalKeyframeSequence](Omni.Sequencer.Path.LogicalKeyframeSequence.md)

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
