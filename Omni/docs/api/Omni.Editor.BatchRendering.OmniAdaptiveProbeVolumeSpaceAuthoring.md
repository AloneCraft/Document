# <a id="Omni_Editor_BatchRendering_OmniAdaptiveProbeVolumeSpaceAuthoring"></a> Class OmniAdaptiveProbeVolumeSpaceAuthoring

Namespace: [Omni.Editor.BatchRendering](Omni.Editor.BatchRendering.md)  
Assembly: Omni.Editor.dll  

URP APVのworldOffsetと、同じ表示RootにあるLight Probe空間契約を一括構成します。
APVの公式offsetが表現できる有限な平行移動だけを受け入れます。

```csharp
public static class OmniAdaptiveProbeVolumeSpaceAuthoring
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniAdaptiveProbeVolumeSpaceAuthoring](Omni.Editor.BatchRendering.OmniAdaptiveProbeVolumeSpaceAuthoring.md)

## フィールド（Fields）

### <a id="Omni_Editor_BatchRendering_OmniAdaptiveProbeVolumeSpaceAuthoring_WorldOffsetVolumePriority"></a> WorldOffsetVolumePriority

他のVolume overrideより後に適用する専用world-offset Volume priorityです。

```csharp
public const float WorldOffsetVolumePriority = 3.4028235E+38
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

## メソッド（Methods）

### <a id="Omni_Editor_BatchRendering_OmniAdaptiveProbeVolumeSpaceAuthoring_TryEnsureContract_UnityEngine_GameObject_UnityEngine_Transform_System_Boolean_System_Boolean__System_String__"></a> TryEnsureContract\(GameObject, Transform, bool, out bool, out string\)

Legacy Light ProbeとAPVが共有する表示Rootへ明示契約を構成します。
Sceneをdirtyにしますが保存は行いません。

```csharp
public static bool TryEnsureContract(GameObject displayRoot, Transform expectedBakedSpaceRoot, bool recordUndo, out bool changed, out string reason)
```

#### 引数（Parameters）

`displayRoot` GameObject

`expectedBakedSpaceRoot` Transform

`recordUndo` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`changed` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
