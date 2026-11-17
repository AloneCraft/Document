# <a id="Omni_Logical_PoseBakeMixerBehaviour"></a> Class PoseBakeMixerBehaviour

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Omni.Sequencer.Runtime.dll  

```csharp
[MovedFrom(true, "Omni.Sequencer.Timeline", null, "LogicalPoseBakeMixerBehaviour")]
public class PoseBakeMixerBehaviour : BakeMixerBehaviour, IPlayableBehaviour, ICloneable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
PlayableBehaviour ← 
[BakeMixerBehaviour](Omni.Logical.BakeMixerBehaviour.md) ← 
[PoseBakeMixerBehaviour](Omni.Logical.PoseBakeMixerBehaviour.md)

#### 実装するインターフェース（Implements）

IPlayableBehaviour, 
[ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable)

## プロパティ（Properties）

### <a id="Omni_Logical_PoseBakeMixerBehaviour_Camera"></a> Camera

画角とクリップ範囲の反映先です。未設定なら姿勢だけを書きます。

```csharp
public Camera Camera { get; set; }
```

#### 値（Property Value）

 Camera

### <a id="Omni_Logical_PoseBakeMixerBehaviour_LastFieldOfView"></a> LastFieldOfView

直近に適用した画角（度）。ベイクに画角が無い場合は0です。

```csharp
public float LastFieldOfView { get; protected set; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Logical_PoseBakeMixerBehaviour_LastPosition"></a> LastPosition

直近に適用したLogical位置です。リアルタイム経路と結果を突き合わせる検証で使います。

```csharp
public Position3 LastPosition { get; protected set; }
```

#### 値（Property Value）

 Position3

### <a id="Omni_Logical_PoseBakeMixerBehaviour_LastRotation"></a> LastRotation

直近に適用したLogical回転です。

```csharp
public Quaternion LastRotation { get; protected set; }
```

#### 値（Property Value）

 Quaternion

## メソッド（Methods）

### <a id="Omni_Logical_PoseBakeMixerBehaviour_ApplyCameraSettings_System_Single_System_Single_System_Single_"></a> ApplyCameraSettings\(float, float, float\)

画角とクリップ範囲をカメラへ反映します。

```csharp
protected void ApplyCameraSettings(float fieldOfView, float nearClip, float farClip)
```

#### 引数（Parameters）

`fieldOfView` [float](https://learn.microsoft.com/dotnet/api/system.single)

`nearClip` [float](https://learn.microsoft.com/dotnet/api/system.single)

`farClip` [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Logical_PoseBakeMixerBehaviour_ProcessFrame_UnityEngine_Playables_Playable_UnityEngine_Playables_FrameData_System_Object_"></a> ProcessFrame\(Playable, FrameData, object\)

<p>This function is called during the ProcessFrame phase of the PlayableGraph.</p>

```csharp
public override void ProcessFrame(Playable playable, FrameData info, object playerData)
```

#### 引数（Parameters）

`playable` Playable

The Playable that owns the current PlayableBehaviour.

`info` FrameData

A FrameData structure that contains information about the current frame context.

`playerData` [object](https://learn.microsoft.com/dotnet/api/system.object)

The user data of the ScriptPlayableOutput that initiated the process pass.

### <a id="Omni_Logical_PoseBakeMixerBehaviour_TryApply_UnityEngine_Playables_Playable_Omni_Logical_Transform_"></a> TryApply\(Playable, Transform\)

有効クリップのベイクを解決し、補間して書き込みます。

```csharp
protected bool TryApply(Playable playable, Transform target)
```

#### 引数（Parameters）

`playable` Playable

ミキサーのPlayable。

`target` Transform

バインドされた書き込み先。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_PoseBakeMixerBehaviour_TryInterpolate_Omni_Logical_PoseBake_Omni_Logical_PoseBakeChannel_System_Double_Omni_Logical_Position3__Omni_Logical_Quaternion__System_Single__System_Single__System_Single__"></a> TryInterpolate\(PoseBake, PoseBakeChannel, double, out Position3, out Quaternion, out float, out float, out float\)

時刻からLogical姿勢とカメラ設定を復元します。

```csharp
protected bool TryInterpolate(PoseBake bake, PoseBakeChannel channel, double sequenceTime, out Position3 position, out Quaternion rotation, out float fieldOfView, out float nearClip, out float farClip)
```

#### 引数（Parameters）

`bake` [PoseBake](Omni.Logical.PoseBake.md)

`channel` [PoseBakeChannel](Omni.Logical.PoseBakeChannel.md)

`sequenceTime` [double](https://learn.microsoft.com/dotnet/api/system.double)

`position` Position3

`rotation` Quaternion

`fieldOfView` [float](https://learn.microsoft.com/dotnet/api/system.single)

`nearClip` [float](https://learn.microsoft.com/dotnet/api/system.single)

`farClip` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_PoseBakeMixerBehaviour_WritePose_Omni_Logical_Transform_Omni_Logical_Position3__Omni_Logical_Quaternion__"></a> WritePose\(Transform, in Position3, in Quaternion\)

Logical姿勢を書き込み、Unity Transformへ同期します。

```csharp
protected void WritePose(Transform target, in Position3 position, in Quaternion rotation)
```

#### 引数（Parameters）

`target` Transform

`position` Position3

`rotation` Quaternion
