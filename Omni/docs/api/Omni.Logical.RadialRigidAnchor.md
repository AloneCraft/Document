# <a id="Omni_Logical_RadialRigidAnchor"></a> Class RadialRigidAnchor

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

同じGameObjectのRendererを、中心アンカー基準のRadial剛体として描画します。

```csharp
[ExecuteAlways]
[DisallowMultipleComponent]
[RequireComponent(typeof(Renderer))]
public sealed class RadialRigidAnchor : MonoBehaviour, IRadialRigidAnchorProvider
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[RadialRigidAnchor](Omni.Logical.RadialRigidAnchor.md)

#### 実装するインターフェース（Implements）

[IRadialRigidAnchorProvider](Omni.Logical.IRadialRigidAnchorProvider.md)

## 補足（Remarks）

頂点を追加したりTransformを移動したりせず、GPU側で中心をRadial写像し、
ローカル形状には中心の接線倍率を等方適用します。
