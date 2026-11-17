# <a id="Omni_Lighting_OmniAdaptiveProbeVolumeSpaceRequirement"></a> Class OmniAdaptiveProbeVolumeSpaceRequirement

Namespace: [Omni.Lighting](Omni.Lighting.md)  
Assembly: Radial.Runtime.dll  

表示RootにAPV焼成空間との明示的な対応が必要なことをSceneへ保存します。

```csharp
[DisallowMultipleComponent]
[RequireComponent(typeof(OmniAdaptiveProbeVolumeSpace))]
[RequireComponent(typeof(OmniLightProbeSpaceRequirement))]
public sealed class OmniAdaptiveProbeVolumeSpaceRequirement : MonoBehaviour
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[OmniAdaptiveProbeVolumeSpaceRequirement](Omni.Lighting.OmniAdaptiveProbeVolumeSpaceRequirement.md)

## プロパティ（Properties）

### <a id="Omni_Lighting_OmniAdaptiveProbeVolumeSpaceRequirement_ExpectedBakedSpaceRoot"></a> ExpectedBakedSpaceRoot

nullはUnityワールド原点を表します。

```csharp
public Transform ExpectedBakedSpaceRoot { get; }
```

#### 値（Property Value）

 Transform
