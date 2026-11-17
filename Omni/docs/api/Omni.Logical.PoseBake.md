# <a id="Omni_Logical_PoseBake"></a> Class PoseBake

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Omni.Sequencer.Runtime.dll  

```csharp
[MovedFrom(true, "Omni.Sequencer", null, "LogicalPoseBake")]
public sealed class PoseBake : ScriptableObject
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
ScriptableObject ← 
[PoseBake](Omni.Logical.PoseBake.md)

## フィールド（Fields）

### <a id="Omni_Logical_PoseBake_CurrentFormatVersion"></a> CurrentFormatVersion

現在の実装が読める形式バージョンです。データの意味を変える修正をしたら上げます。
一致しないベイクは詰め直さずリアルタイム経路へ倒します。

```csharp
public const int CurrentFormatVersion = 1
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="Omni_Logical_PoseBake_BakedUtc"></a> BakedUtc

ベイクを実行した時刻（ISO 8601、UTC）。診断表示用です。

```csharp
public string BakedUtc { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Logical_PoseBake_Channels"></a> Channels

ベイクされたチャンネル一覧。

```csharp
public PoseBakeChannel[] Channels { get; }
```

#### 値（Property Value）

 [PoseBakeChannel](Omni.Logical.PoseBakeChannel.md)\[\]

### <a id="Omni_Logical_PoseBake_EndTimeSeconds"></a> EndTimeSeconds

最後のサンプルの時刻（秒）。

```csharp
public double EndTimeSeconds { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Logical_PoseBake_FormatVersion"></a> FormatVersion

ベイクデータの形式バージョン。

```csharp
public int FormatVersion { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_PoseBake_SampleCount"></a> SampleCount

サンプル数。

```csharp
public int SampleCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_PoseBake_SampleIntervalSeconds"></a> SampleIntervalSeconds

サンプル間隔（秒）。

```csharp
public double SampleIntervalSeconds { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Logical_PoseBake_SceneGuid"></a> SceneGuid

ベイク元シーンのアセットGUID。

```csharp
public string SceneGuid { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Logical_PoseBake_SourceContentHash"></a> SourceContentHash

ベイク時のシーケンス内容と天体配置のハッシュ。陳腐化検出に使います。

```csharp
public string SourceContentHash { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Logical_PoseBake_SourceGuid"></a> SourceGuid

ベイク元シーケンス（Timelineアセット）のGUID。

```csharp
public string SourceGuid { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Logical_PoseBake_StartTimeSeconds"></a> StartTimeSeconds

最初のサンプルの時刻（秒）。

```csharp
public double StartTimeSeconds { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Logical_PoseBake_TargetIds"></a> TargetIds

注視対象の安定ID表。チャンネルの索引はここを指します。

```csharp
public string[] TargetIds { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)\[\]

## メソッド（Methods）

### <a id="Omni_Logical_PoseBake_SetData_System_String_System_String_System_String_System_String_System_Double_System_Double_System_Int32_System_String___Omni_Logical_PoseBakeChannel___"></a> SetData\(string, string, string, string, double, double, int, string\[\], PoseBakeChannel\[\]\)

ベイク結果を設定します。ベイカーからのみ呼ぶ想定です。

```csharp
public void SetData(string sceneGuid, string sourceGuid, string sourceContentHash, string bakedUtc, double startTimeSeconds, double sampleIntervalSeconds, int sampleCount, string[] targetIds, PoseBakeChannel[] channels)
```

#### 引数（Parameters）

`sceneGuid` [string](https://learn.microsoft.com/dotnet/api/system.string)

`sourceGuid` [string](https://learn.microsoft.com/dotnet/api/system.string)

`sourceContentHash` [string](https://learn.microsoft.com/dotnet/api/system.string)

`bakedUtc` [string](https://learn.microsoft.com/dotnet/api/system.string)

`startTimeSeconds` [double](https://learn.microsoft.com/dotnet/api/system.double)

`sampleIntervalSeconds` [double](https://learn.microsoft.com/dotnet/api/system.double)

`sampleCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`targetIds` [string](https://learn.microsoft.com/dotnet/api/system.string)\[\]

`channels` [PoseBakeChannel](Omni.Logical.PoseBakeChannel.md)\[\]

### <a id="Omni_Logical_PoseBake_TryGetChannel_System_String_Omni_Logical_PoseBakeChannel__"></a> TryGetChannel\(string, out PoseBakeChannel\)

指定した対象パスのチャンネルを引きます。

```csharp
public bool TryGetChannel(string targetPath, out PoseBakeChannel channel)
```

#### 引数（Parameters）

`targetPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

バインド対象の安定識別子。

`channel` [PoseBakeChannel](Omni.Logical.PoseBakeChannel.md)

見つかったチャンネル。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_PoseBake_TryGetTargetId_System_Int32_System_String__"></a> TryGetTargetId\(int, out string\)

索引から注視対象の安定IDを引きます。

```csharp
public bool TryGetTargetId(int index, out string targetId)
```

#### 引数（Parameters）

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`targetId` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_PoseBake_TryValidate_System_String_System_String_System_String_Omni_Logical_PoseBakeRejection__"></a> TryValidate\(string, string, string, out PoseBakeRejection\)

このベイクをそのまま使えるかを検証します。

<p>
固定小数点の構成を保存して比較しているのが要点です。Project Settings で
ビット幅を変えるとraw limbの意味が変わりますが、limb本数が同じままだと
壊れた値が「正しい値の顔をして」通ってしまいます。ここで弾いて
リアルタイム経路へ倒します。
</p>

```csharp
public bool TryValidate(string expectedSceneGuid, string expectedSourceGuid, string expectedContentHash, out PoseBakeRejection rejection)
```

#### 引数（Parameters）

`expectedSceneGuid` [string](https://learn.microsoft.com/dotnet/api/system.string)

現在のシーンのGUID。空なら照合しません。

`expectedSourceGuid` [string](https://learn.microsoft.com/dotnet/api/system.string)

現在のシーケンスのGUID。空なら照合しません。

`expectedContentHash` [string](https://learn.microsoft.com/dotnet/api/system.string)

現在の内容ハッシュ。空なら照合しません。

`rejection` [PoseBakeRejection](Omni.Logical.PoseBakeRejection.md)

使えない場合の理由。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
