# <a id="Omni_BatchRendering_RadialBrgSceneManifest"></a> Class RadialBrgSceneManifest

Namespace: [Omni.BatchRendering](Omni.BatchRendering.md)  
Assembly: Omni.BatchRendering.Runtime.dll  

Player Build時のSceneコピーへEditorが付加する、Scene単位のBRG Material対応表です。
GardenSceneでは元Sceneを変更せず、同Sceneで参照するsidecarだけをPlayerへ含めます。

```csharp
[AddComponentMenu("")]
[DisallowMultipleComponent]
[ExecuteAlways]
public sealed class RadialBrgSceneManifest : MonoBehaviour
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[RadialBrgSceneManifest](Omni.BatchRendering.RadialBrgSceneManifest.md)
