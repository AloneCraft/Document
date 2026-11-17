# <a id="Omni_Logical_FiniteSkinnedPresentation"></a> Class FiniteSkinnedPresentation

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

Asteria の runtime actor root など、巨大な Unity 祖先を持たない専用骨格だけを
有限 native 空間で更新する明示 opt-in です。Logical raw 姿勢は変更しません。

```csharp
[ExecuteAlways]
[DefaultExecutionOrder(-32000)]
[DisallowMultipleComponent]
[RequireComponent(typeof(Transform))]
public sealed class FiniteSkinnedPresentation : MonoBehaviour
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[FiniteSkinnedPresentation](Omni.Logical.FiniteSkinnedPresentation.md)

## 補足（Remarks）

Scene root の Logical Transform と、その plain FBX 子階層専用です。
Site への論理 anchor と world 姿勢の合成は actor owner が保持します。
巨大な Unity 親の逆変換相殺、Cloth、VFX、入れ子の Logical owner は対応に含めません。
可視性の外部操作は Renderer.enabled、共同抑止は suppression registry の lease を使います。
lease 中の forceRenderingOff への非参加 writer の直接代入は識別・復元できません。

## プロパティ（Properties）

### <a id="Omni_Logical_FiniteSkinnedPresentation_FailureReason"></a> FailureReason

前提が成立しなかった理由です。空なら初期化済みです。

```csharp
public string FailureReason { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Logical_FiniteSkinnedPresentation_IsReady"></a> IsReady

現在の opt-in 前提が成立している場合に true です。

```csharp
public bool IsReady { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
