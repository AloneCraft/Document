# <a id="Omni_Observer_Editor"></a> Namespace Omni.Observer.Editor

### クラス（Classes）

 [RadialObserverRigBuilder](Omni.Observer.Editor.RadialObserverRigBuilder.md)

<code>RadialObserverRig.prefab</code> をコードから生成します。Prefabは手編集せず、この生成器を正本とします。
構成: Rig／Focus／枠5つ（Orbit・Front・Right・Top・Iso。各枠はCamera＋Brain、VCam＋OrbitalFollow＋RotationComposer）。
RadialCameraもLogicalTransformも付けません（LogicalTransformはCinemachineと同居できず、観察Cameraは
Registry経由でワープ元を借りるため）。

 [RadialObserverTerminalInstaller](Omni.Observer.Editor.RadialObserverTerminalInstaller.md)

sceneへ観察Rigを置きます。sceneの<code>SceneMetaData</code>は、Awakeで
Root・PlayerRig・自分以外のシーンルートを全て非アクティブにします（複数シーン構成のため）。
シーンルート直下に置いたRigは消されるので、必ず<code>SceneMetaData.Root</code>の子へ置きます。
