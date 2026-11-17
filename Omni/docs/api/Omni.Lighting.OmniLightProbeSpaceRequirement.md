# <a id="Omni_Lighting_OmniLightProbeSpaceRequirement"></a> Class OmniLightProbeSpaceRequirement

Namespace: [Omni.Lighting](Omni.Lighting.md)  
Assembly: Radial.Runtime.dll  

移動した表示RootにLight Probeベイク空間との明示的な対応が必要であることを保存します。
TerminalSceneなど、表示座標と物理Lighting Dataの座標が異なるScene Rootで使用します。

```csharp
[DisallowMultipleComponent]
[RequireComponent(typeof(OmniLightProbeSpace))]
public sealed class OmniLightProbeSpaceRequirement : MonoBehaviour
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[OmniLightProbeSpaceRequirement](Omni.Lighting.OmniLightProbeSpaceRequirement.md)

## プロパティ（Properties）

### <a id="Omni_Lighting_OmniLightProbeSpaceRequirement_ExpectedBakedSpaceRoot"></a> ExpectedBakedSpaceRoot

契約上期待するベイク空間の原点です。nullはUnityワールド原点を表します。

```csharp
public Transform ExpectedBakedSpaceRoot { get; }
```

#### 値（Property Value）

 Transform
