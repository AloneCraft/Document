# <a id="Omni_Observer_RadialObserverChannelGuard"></a> Class RadialObserverChannelGuard

Namespace: [Omni.Observer](Omni.Observer.md)  
Assembly: Omni.RadialObserver.Cinemachine.dll  

観察枠のVirtual Cameraを、その枠のBrainだけが拾うように分離します。

<p>
CinemachineBrainの既定のChannelMaskは「全チャンネル」で、シーン内の別のBrain
（ゲーム側の主カメラ）が観察枠のVirtual Cameraを拾うと、主カメラが観察位置へ動いてしまいます。
そのため、枠ごとに専用のOutputChannel（Channel01〜05）を割り当て、枠のBrainをそのチャンネルだけにし、
有効化時点で存在する他のBrainからこのチャンネルを外します（無効化時に元へ戻します）。
有効化より後に作られたBrainは対象外なので、その場合はそのBrainのChannelMaskを設定してください。
</p>

```csharp
[DisallowMultipleComponent]
[DefaultExecutionOrder(-50)]
[AddComponentMenu("Omni/Radial Observer Channel Guard")]
public sealed class RadialObserverChannelGuard : MonoBehaviour
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[RadialObserverChannelGuard](Omni.Observer.RadialObserverChannelGuard.md)

## メソッド（Methods）

### <a id="Omni_Observer_RadialObserverChannelGuard_ChannelForSlot_System_Int32_"></a> ChannelForSlot\(int\)

枠番号に対応する観察専用チャンネルです（枠0→Channel01 … 枠4→Channel05）。

```csharp
public static OutputChannels ChannelForSlot(int slotIndex)
```

#### 引数（Parameters）

`slotIndex` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 OutputChannels

### <a id="Omni_Observer_RadialObserverChannelGuard_Configure_Omni_Observer_RadialObserverSlot_Unity_Cinemachine_CinemachineBrain_Unity_Cinemachine_CinemachineCamera_"></a> Configure\(RadialObserverSlot, CinemachineBrain, CinemachineCamera\)

コードから構成します（Prefab生成とテスト用）。

```csharp
public void Configure(RadialObserverSlot slot, CinemachineBrain brain, CinemachineCamera virtualCamera)
```

#### 引数（Parameters）

`slot` RadialObserverSlot

`brain` CinemachineBrain

`virtualCamera` CinemachineCamera
