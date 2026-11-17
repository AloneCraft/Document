# <a id="Omni_Observer_Editor_RadialObserverRigBuilder"></a> Class RadialObserverRigBuilder

Namespace: [Omni.Observer.Editor](Omni.Observer.Editor.md)  
Assembly: Omni.RadialObserver.Editor.dll  

<code>RadialObserverRig.prefab</code> をコードから生成します。Prefabは手編集せず、この生成器を正本とします。
構成: Rig／Focus／枠5つ（Orbit・Front・Right・Top・Iso。各枠はCamera＋Brain、VCam＋OrbitalFollow＋RotationComposer）。
RadialCameraもLogicalTransformも付けません（LogicalTransformはCinemachineと同居できず、観察Cameraは
Registry経由でワープ元を借りるため）。

```csharp
public static class RadialObserverRigBuilder
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialObserverRigBuilder](Omni.Observer.Editor.RadialObserverRigBuilder.md)

## フィールド（Fields）

### <a id="Omni_Observer_Editor_RadialObserverRigBuilder_PrefabPath"></a> PrefabPath

```csharp
public static readonly string PrefabPath
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Observer_Editor_RadialObserverRigBuilder_BuildRig"></a> BuildRig\(\)

メモリ上にRigを組み立てます。呼び出し側がPrefab化または破棄します。

```csharp
public static GameObject BuildRig()
```

#### 戻り値（Returns）

 GameObject

### <a id="Omni_Observer_Editor_RadialObserverRigBuilder_RebuildPrefab"></a> RebuildPrefab\(\)

```csharp
public static void RebuildPrefab()
```
