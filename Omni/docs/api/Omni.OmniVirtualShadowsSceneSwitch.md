# <a id="Omni_OmniVirtualShadowsSceneSwitch"></a> Class OmniVirtualShadowsSceneSwitch

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

この部品がある Scene では、Renderer の仮想シャドウマップ(OmniVirtualShadowsFeature)を、既定が無効でも使う。
全ての Scene で使うときは Feature の「全ての Scene で使う」をオンにする。

```csharp
[DisallowMultipleComponent]
[AddComponentMenu("Omni/Rendering/Virtual Shadows Scene Switch")]
public sealed class OmniVirtualShadowsSceneSwitch : MonoBehaviour
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[OmniVirtualShadowsSceneSwitch](Omni.OmniVirtualShadowsSceneSwitch.md)

## プロパティ（Properties）

### <a id="Omni_OmniVirtualShadowsSceneSwitch_ActiveCount"></a> ActiveCount

有効な部品の数。

```csharp
public static int ActiveCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)
