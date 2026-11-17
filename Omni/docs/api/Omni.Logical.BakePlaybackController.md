# <a id="Omni_Logical_BakePlaybackController"></a> Class BakePlaybackController

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Omni.Sequencer.Runtime.dll  

ベイク再生とリアルタイム経路の切り替えを、シーケンス全体で1か所に集約するコンポーネントです。

<p>
<code>PlayableDirector</code>と同じGameObjectに付けます。ベイクトラックのミキサーは
<code>CreateTrackMixer</code>に渡されるGameObjectからこのコンポーネントを見つけ、
「照合すべきGUID・ハッシュ」を受け取り、「今フレーム適用できたか」を報告します。
</p>
<p>
演出側（Director）はこの1点だけを見てフォールバックを判断できます。トラックごとに
判定が散らばると、カメラだけベイク・光源だけリアルタイムのような食い違った絵が
生まれるためです。
</p>

```csharp
[DisallowMultipleComponent]
[MovedFrom(true, "Omni.Sequencer", null, "LogicalBakePlaybackController")]
public sealed class BakePlaybackController : MonoBehaviour
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[BakePlaybackController](Omni.Logical.BakePlaybackController.md)

## プロパティ（Properties）

### <a id="Omni_Logical_BakePlaybackController_AllChannelsApplied"></a> AllChannelsApplied

報告済みのチャンネルが1つ以上あり、すべて適用できていればtrueです。

```csharp
public bool AllChannelsApplied { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_BakePlaybackController_ChannelStates"></a> ChannelStates

報告済みのチャンネル状態を返します。診断表示用です。

```csharp
public IReadOnlyList<BakePlaybackController.ChannelState> ChannelStates { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[BakePlaybackController](Omni.Logical.BakePlaybackController.md).[ChannelState](Omni.Logical.BakePlaybackController.ChannelState.md)\>

### <a id="Omni_Logical_BakePlaybackController_ExpectedContentHash"></a> ExpectedContentHash

照合する内容ハッシュ。空なら照合しません。

```csharp
public string ExpectedContentHash { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Logical_BakePlaybackController_ExpectedSceneGuid"></a> ExpectedSceneGuid

照合するシーンGUID。空なら照合しません。

```csharp
public string ExpectedSceneGuid { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Logical_BakePlaybackController_ExpectedSourceGuid"></a> ExpectedSourceGuid

照合するシーケンスGUID。空なら照合しません。

```csharp
public string ExpectedSourceGuid { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Logical_BakePlaybackController_ExternalOverride"></a> ExternalOverride

ベイク済み姿勢の適用を外部の都合で禁止します。
<xref href="Omni.Logical.PoseBakeRejection.None" data-throw-if-not-resolved="false"></xref>で解除します。

```csharp
public PoseBakeRejection ExternalOverride { get; set; }
```

#### 値（Property Value）

 [PoseBakeRejection](Omni.Logical.PoseBakeRejection.md)

### <a id="Omni_Logical_BakePlaybackController_FirstRejection"></a> FirstRejection

適用できなかったチャンネルのうち最初の理由を返します。すべて適用できていれば
<xref href="Omni.Logical.PoseBakeRejection.None" data-throw-if-not-resolved="false"></xref>です。

```csharp
public PoseBakeRejection FirstRejection { get; }
```

#### 値（Property Value）

 [PoseBakeRejection](Omni.Logical.PoseBakeRejection.md)

## メソッド（Methods）

### <a id="Omni_Logical_BakePlaybackController_ConfigureExpectations_System_String_System_String_System_String_"></a> ConfigureExpectations\(string, string, string\)

照合に使う識別情報を設定します。シーン生成時とベイク生成時に書き込みます。

```csharp
public void ConfigureExpectations(string sceneGuid, string sourceGuid, string contentHash)
```

#### 引数（Parameters）

`sceneGuid` [string](https://learn.microsoft.com/dotnet/api/system.string)

シーンのアセットGUID。

`sourceGuid` [string](https://learn.microsoft.com/dotnet/api/system.string)

シーケンス（Timelineアセット）のGUID。

`contentHash` [string](https://learn.microsoft.com/dotnet/api/system.string)

シーケンス内容と天体配置のハッシュ。

### <a id="Omni_Logical_BakePlaybackController_ReportChannel_System_String_System_Boolean_Omni_Logical_PoseBakeRejection_"></a> ReportChannel\(string, bool, PoseBakeRejection\)

ミキサーが毎フレーム自分の状態を報告します。

```csharp
public void ReportChannel(string targetPath, bool applied, PoseBakeRejection rejection)
```

#### 引数（Parameters）

`targetPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

チャンネル識別子。

`applied` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

ベイク済みサンプルを適用できたか。

`rejection` [PoseBakeRejection](Omni.Logical.PoseBakeRejection.md)

できなかった理由。

### <a id="Omni_Logical_BakePlaybackController_ResetReports"></a> ResetReports\(\)

報告をすべて捨てます。ショーの切り替えやシークの直前に呼び、
前のシーケンスの状態が残らないようにします。

```csharp
public void ResetReports()
```
