# <a id="Omni_Logical_BakePlaybackController_ChannelState"></a> Struct BakePlaybackController.ChannelState

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Omni.Sequencer.Runtime.dll  

1チャンネルぶんの直近の状態です。

```csharp
public readonly struct BakePlaybackController.ChannelState
```

## コンストラクター（Constructors）

### <a id="Omni_Logical_BakePlaybackController_ChannelState__ctor_System_String_System_Boolean_Omni_Logical_PoseBakeRejection_"></a> ChannelState\(string, bool, PoseBakeRejection\)

状態を組み立てます。

```csharp
public ChannelState(string targetPath, bool applied, PoseBakeRejection rejection)
```

#### 引数（Parameters）

`targetPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`applied` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`rejection` [PoseBakeRejection](Omni.Logical.PoseBakeRejection.md)

## フィールド（Fields）

### <a id="Omni_Logical_BakePlaybackController_ChannelState_Applied"></a> Applied

直近の評価でベイク済みサンプルを適用できたか。

```csharp
public readonly bool Applied
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_BakePlaybackController_ChannelState_Rejection"></a> Rejection

適用できなかった理由。

```csharp
public readonly PoseBakeRejection Rejection
```

#### 値（Field Value）

 [PoseBakeRejection](Omni.Logical.PoseBakeRejection.md)

### <a id="Omni_Logical_BakePlaybackController_ChannelState_TargetPath"></a> TargetPath

チャンネル識別子。

```csharp
public readonly string TargetPath
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
