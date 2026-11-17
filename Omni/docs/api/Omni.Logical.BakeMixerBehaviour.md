# <a id="Omni_Logical_BakeMixerBehaviour"></a> Class BakeMixerBehaviour

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Omni.Sequencer.Runtime.dll  

```csharp
[MovedFrom(true, "Omni.Sequencer.Timeline", null, "LogicalBakeMixerBehaviour")]
public abstract class BakeMixerBehaviour : PlayableBehaviour, IPlayableBehaviour, ICloneable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
PlayableBehaviour ← 
[BakeMixerBehaviour](Omni.Logical.BakeMixerBehaviour.md)

#### 派生した型（Derived）

[LightBakeMixerBehaviour](Omni.Logical.LightBakeMixerBehaviour.md), 
[PoseBakeMixerBehaviour](Omni.Logical.PoseBakeMixerBehaviour.md)

#### 実装するインターフェース（Implements）

IPlayableBehaviour, 
[ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable)

## プロパティ（Properties）

### <a id="Omni_Logical_BakeMixerBehaviour_Controller"></a> Controller

ベイク再生の可否を集約するコンポーネント。<code>PlayableDirector</code>と同じGameObjectから
トラックが見つけて渡します。nullでも動きます（テストでは付けません）。

```csharp
public BakePlaybackController Controller { get; set; }
```

#### 値（Property Value）

 [BakePlaybackController](Omni.Logical.BakePlaybackController.md)

### <a id="Omni_Logical_BakeMixerBehaviour_ExpectedContentHash"></a> ExpectedContentHash

照合する内容ハッシュ。空なら照合しません。

```csharp
public string ExpectedContentHash { get; set; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Logical_BakeMixerBehaviour_ExpectedSceneGuid"></a> ExpectedSceneGuid

照合するシーンGUID。空なら照合しません。

```csharp
public string ExpectedSceneGuid { get; set; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Logical_BakeMixerBehaviour_ExpectedSourceGuid"></a> ExpectedSourceGuid

照合するシーケンスGUID。空なら照合しません。

```csharp
public string ExpectedSourceGuid { get; set; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Logical_BakeMixerBehaviour_ExternalOverride"></a> ExternalOverride

ベイク済み姿勢の適用を、外部の都合で一時的に禁止します。
ユーザーがカメラを操作した、Observerの視点差分が要る、といった
「データは正しいが今は使ってはいけない」状況で立てます。
<xref href="Omni.Logical.BakeMixerBehaviour.Controller" data-throw-if-not-resolved="false"></xref>があればそちらの値が優先されます。

```csharp
public PoseBakeRejection ExternalOverride { get; set; }
```

#### 値（Property Value）

 [PoseBakeRejection](Omni.Logical.PoseBakeRejection.md)

### <a id="Omni_Logical_BakeMixerBehaviour_LastApplied"></a> LastApplied

直近の評価でベイク済みサンプルを適用できた場合はtrueです。
falseの間は、上位（Director）がリアルタイム経路で姿勢を決めます。

```csharp
public bool LastApplied { get; protected set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_BakeMixerBehaviour_LastChannelPath"></a> LastChannelPath

直近に評価したチャンネル識別子です。

```csharp
protected string LastChannelPath { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Logical_BakeMixerBehaviour_LastRejection"></a> LastRejection

直近の評価でベイクを使えなかった理由です。使えた場合は
<xref href="Omni.Logical.PoseBakeRejection.None" data-throw-if-not-resolved="false"></xref> になります。

```csharp
public PoseBakeRejection LastRejection { get; protected set; }
```

#### 値（Property Value）

 [PoseBakeRejection](Omni.Logical.PoseBakeRejection.md)

### <a id="Omni_Logical_BakeMixerBehaviour_TrackChannelTargetPath"></a> TrackChannelTargetPath

このトラックが駆動するチャンネル識別子。状態報告のキーになります。
クリップが自分でチャンネルを指定していればそちらが優先されます。

```csharp
public string TrackChannelTargetPath { get; set; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Logical_BakeMixerBehaviour_ReportToController"></a> ReportToController\(\)

今フレームの結果を<xref href="Omni.Logical.BakeMixerBehaviour.Controller" data-throw-if-not-resolved="false"></xref>へ報告します。
派生の<code>ProcessFrame</code>の最後で必ず呼びます。

```csharp
protected void ReportToController()
```

### <a id="Omni_Logical_BakeMixerBehaviour_ToFloatFraction_Omni_Logical_Scalar__"></a> ToFloatFraction\(in Scalar\)

比率をfloatへ落とします。画角や光の強さなど、空間量ではない値の補間に使います。

```csharp
protected static float ToFloatFraction(in Scalar fraction)
```

#### 引数（Parameters）

`fraction` Scalar

#### 戻り値（Returns）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Logical_BakeMixerBehaviour_TryGetActiveClip_UnityEngine_Playables_Playable_Omni_Logical_PoseBakeClipBehaviour__System_Double__"></a> TryGetActiveClip\(Playable, out PoseBakeClipBehaviour, out double\)

重みが最大の入力クリップと、そのクリップ内での経過時刻を返します。

```csharp
protected static bool TryGetActiveClip(Playable playable, out PoseBakeClipBehaviour clip, out double clipTime)
```

#### 引数（Parameters）

`playable` Playable

`clip` [PoseBakeClipBehaviour](Omni.Logical.PoseBakeClipBehaviour.md)

`clipTime` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_BakeMixerBehaviour_TryResolveActiveSample_UnityEngine_Playables_Playable_System_String_Omni_Logical_PoseBake__Omni_Logical_PoseBakeChannel__System_Double__"></a> TryResolveActiveSample\(Playable, string, out PoseBake, out PoseBakeChannel, out double\)

重みが最大のクリップを選び、そのベイク・チャンネル・シーケンス時刻を返します。

```csharp
protected bool TryResolveActiveSample(Playable playable, string channelTargetPath, out PoseBake bake, out PoseBakeChannel channel, out double sequenceTime)
```

#### 引数（Parameters）

`playable` Playable

ミキサーのPlayable。

`channelTargetPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

引きたいチャンネルの識別子。空ならクリップの指定に従います。

`bake` [PoseBake](Omni.Logical.PoseBake.md)

解決したベイクアセット。

`channel` [PoseBakeChannel](Omni.Logical.PoseBakeChannel.md)

解決したチャンネル。

`sequenceTime` [double](https://learn.microsoft.com/dotnet/api/system.double)

シーケンス先頭からの時刻（秒）。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_BakeMixerBehaviour_TryResolveIndices_Omni_Logical_PoseBake_System_Double_System_Int32__System_Int32__Omni_Logical_Scalar__"></a> TryResolveIndices\(PoseBake, double, out int, out int, out Scalar\)

時刻から前後サンプルの索引と比率を求めます。

```csharp
protected bool TryResolveIndices(PoseBake bake, double sequenceTime, out int index, out int nextIndex, out Scalar fraction)
```

#### 引数（Parameters）

`bake` [PoseBake](Omni.Logical.PoseBake.md)

`sequenceTime` [double](https://learn.microsoft.com/dotnet/api/system.double)

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`nextIndex` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`fraction` Scalar

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_BakeMixerBehaviour_TryToUnityRotation_Omni_Logical_Quaternion__UnityEngine_Quaternion__"></a> TryToUnityRotation\(in Quaternion, out Quaternion\)

LogicalQuaternionをUnityのQuaternionへ狭小化します。
回転は無次元量なので、この変換は巨大座標のfloat化とは別物です。

```csharp
protected static bool TryToUnityRotation(in Quaternion value, out Quaternion result)
```

#### 引数（Parameters）

`value` Quaternion

`result` Quaternion

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_BakeMixerBehaviour_TryToUnityVector_Omni_Logical_Vector3__UnityEngine_Vector3__"></a> TryToUnityVector\(in Vector3, out Vector3\)

LogicalVector3をUnityのVector3へ狭小化します。

```csharp
protected static bool TryToUnityVector(in Vector3 value, out Vector3 result)
```

#### 引数（Parameters）

`value` Vector3

`result` Vector3

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
