# <a id="Omni_Lighting_OmniAdaptiveProbeVolumeSpace"></a> Class OmniAdaptiveProbeVolumeSpace

Namespace: [Omni.Lighting](Omni.Lighting.md)  
Assembly: Radial.Runtime.dll  

表示Rootの平行移動をURP APVの公式worldOffsetへ反映します。
Volume.profileの実行時cloneだけを変更し、共有Profile assetを変更しません。

```csharp
[ExecuteAlways]
[DisallowMultipleComponent]
[RequireComponent(typeof(OmniLightProbeSpace))]
[RequireComponent(typeof(Volume))]
public sealed class OmniAdaptiveProbeVolumeSpace : MonoBehaviour
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[OmniAdaptiveProbeVolumeSpace](Omni.Lighting.OmniAdaptiveProbeVolumeSpace.md)

## フィールド（Fields）

### <a id="Omni_Lighting_OmniAdaptiveProbeVolumeSpace_DedicatedVolumePriority"></a> DedicatedVolumePriority

```csharp
public const float DedicatedVolumePriority = 3.4028235E+38
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

## プロパティ（Properties）

### <a id="Omni_Lighting_OmniAdaptiveProbeVolumeSpace_CurrentWorldOffset"></a> CurrentWorldOffset

```csharp
public Vector3 CurrentWorldOffset { get; }
```

#### 値（Property Value）

 Vector3

### <a id="Omni_Lighting_OmniAdaptiveProbeVolumeSpace_IsApplied"></a> IsApplied

```csharp
public bool IsApplied { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_Lighting_OmniAdaptiveProbeVolumeSpace_TryEvaluate_UnityEngine_Vector3__System_String__"></a> TryEvaluate\(out Vector3, out string\)

現在のScene構成を変更せずに、適用できるworldOffsetを評価します。

```csharp
public bool TryEvaluate(out Vector3 worldOffset, out string reason)
```

#### 引数（Parameters）

`worldOffset` Vector3

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Lighting_OmniAdaptiveProbeVolumeSpace_TryRefreshNow_System_String__"></a> TryRefreshNow\(out string\)

評価したoffsetを専用Volumeへ反映します。成立しない状態ではoverrideを外します。

```csharp
public bool TryRefreshNow(out string reason)
```

#### 引数（Parameters）

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
