# <a id="Omni_Logical_TransformReadOnlyEditor"></a> Class TransformReadOnlyEditor

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Omni.Editor.dll  

LogicalOriginalTransformなどの通常Transform編集をUnity標準Inspectorへ委譲し、
LogicalTransformの出力先だけを読み取り専用にします。

```csharp
[CustomEditor(typeof(Transform), true)]
[CanEditMultipleObjects]
[MovedFrom(true, "Omni.Editor", null, "LogicalTransformReadOnlyEditor")]
public sealed class TransformReadOnlyEditor : Editor
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
ScriptableObject ← 
Editor ← 
[TransformReadOnlyEditor](Omni.Logical.TransformReadOnlyEditor.md)

## メソッド（Methods）

### <a id="Omni_Logical_TransformReadOnlyEditor_OnInspectorGUI"></a> OnInspectorGUI\(\)

<p>Implement this function to make a custom inspector.</p>

```csharp
public override void OnInspectorGUI()
```
