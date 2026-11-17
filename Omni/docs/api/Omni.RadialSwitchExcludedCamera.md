# <a id="Omni_RadialSwitchExcludedCamera"></a> Class RadialSwitchExcludedCamera

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

この Camera(と子の Camera)を、対数への切り替えの対象から外す目印です。付けた Camera には RadialCamera が付かず、
標準の Unity のまま描きます。標準の Unity と Omni を同じ Scene で並べて比べる検証 Scene(Functions/Basics)などで使います。

```csharp
[DisallowMultipleComponent]
[AddComponentMenu("Omni/Radial Switch Excluded Camera")]
public sealed class RadialSwitchExcludedCamera : MonoBehaviour
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[RadialSwitchExcludedCamera](Omni.RadialSwitchExcludedCamera.md)
