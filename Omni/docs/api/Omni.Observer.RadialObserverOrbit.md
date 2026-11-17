# <a id="Omni_Observer_RadialObserverOrbit"></a> Class RadialObserverOrbit

Namespace: [Omni.Observer](Omni.Observer.md)  
Assembly: Omni.RadialObserver.Cinemachine.dll  

観察枠1つのCinemachine仮想カメラを駆動します。

<p>
距離は枠の固定距離（<xref href="Omni.Observer.ObserverFrame.FixedDistance" data-throw-if-not-resolved="false"></xref>）です。
桁違いのスケール間を滑らかに動くよう、距離はlog空間でSmoothDampします。
周回枠は自動周回し、右ボタンドラッグ（枠の内側）で手動回転、ホイールで拡縮、操作後は一定時間おいて周回を再開します。
固定枠は角度を固定します。
</p>

```csharp
[DisallowMultipleComponent]
[DefaultExecutionOrder(200)]
[AddComponentMenu("Omni/Radial Observer Orbit")]
public sealed class RadialObserverOrbit : MonoBehaviour
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[RadialObserverOrbit](Omni.Observer.RadialObserverOrbit.md)

## メソッド（Methods）

### <a id="Omni_Observer_RadialObserverOrbit_Configure_Omni_Observer_RadialObserverRig_Omni_Observer_RadialObserverSlot_Unity_Cinemachine_CinemachineCamera_Unity_Cinemachine_CinemachineOrbitalFollow_"></a> Configure\(RadialObserverRig, RadialObserverSlot, CinemachineCamera, CinemachineOrbitalFollow\)

コードから構成します（Prefab生成とテスト用）。

```csharp
public void Configure(RadialObserverRig rig, RadialObserverSlot slot, CinemachineCamera virtualCamera, CinemachineOrbitalFollow orbital)
```

#### 引数（Parameters）

`rig` RadialObserverRig

`slot` RadialObserverSlot

`virtualCamera` CinemachineCamera

`orbital` CinemachineOrbitalFollow
