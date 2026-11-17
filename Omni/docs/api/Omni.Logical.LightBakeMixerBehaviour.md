# <a id="Omni_Logical_LightBakeMixerBehaviour"></a> Class LightBakeMixerBehaviour

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Omni.Sequencer.Runtime.dll  

```csharp
[MovedFrom(true, "Omni.Sequencer.Timeline", null, "LogicalLightBakeMixerBehaviour")]
public class LightBakeMixerBehaviour : BakeMixerBehaviour, IPlayableBehaviour, ICloneable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
PlayableBehaviour ← 
[BakeMixerBehaviour](Omni.Logical.BakeMixerBehaviour.md) ← 
[LightBakeMixerBehaviour](Omni.Logical.LightBakeMixerBehaviour.md)

#### 実装するインターフェース（Implements）

IPlayableBehaviour, 
[ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable)

## プロパティ（Properties）

### <a id="Omni_Logical_LightBakeMixerBehaviour_LastRotation"></a> LastRotation

直近に適用したLogical回転です。

```csharp
public Quaternion LastRotation { get; protected set; }
```

#### 値（Property Value）

 Quaternion

## メソッド（Methods）

### <a id="Omni_Logical_LightBakeMixerBehaviour_ProcessFrame_UnityEngine_Playables_Playable_UnityEngine_Playables_FrameData_System_Object_"></a> ProcessFrame\(Playable, FrameData, object\)

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

### <a id="Omni_Logical_LightBakeMixerBehaviour_TryApply_UnityEngine_Playables_Playable_UnityEngine_Light_"></a> TryApply\(Playable, Light\)

有効クリップのベイクを解決し、補間して書き込みます。

```csharp
protected bool TryApply(Playable playable, Light target)
```

#### 引数（Parameters）

`playable` Playable

`target` Light

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_LightBakeMixerBehaviour_TryInterpolate_Omni_Logical_PoseBake_Omni_Logical_PoseBakeChannel_System_Double_Omni_Logical_Quaternion__System_Single__UnityEngine_Color__"></a> TryInterpolate\(PoseBake, PoseBakeChannel, double, out Quaternion, out float, out Color\)

時刻から光源の回転・強度・色を復元します。

```csharp
protected bool TryInterpolate(PoseBake bake, PoseBakeChannel channel, double sequenceTime, out Quaternion rotation, out float intensity, out Color color)
```

#### 引数（Parameters）

`bake` [PoseBake](Omni.Logical.PoseBake.md)

`channel` [PoseBakeChannel](Omni.Logical.PoseBakeChannel.md)

`sequenceTime` [double](https://learn.microsoft.com/dotnet/api/system.double)

`rotation` Quaternion

`intensity` [float](https://learn.microsoft.com/dotnet/api/system.single)

`color` Color

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
