# <a id="Omni_Logical_TransformEditor"></a> Class TransformEditor

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Omni.Editor.dll  

<xref href="Omni.Logical.Transform" data-throw-if-not-resolved="false"></xref> のインスペクタです。

<p>
既定のインスペクタは固定小数点の生limb配列(<code>ulong[]</code>)をそのまま表示してしまい
編集できません。標準Transformと同じ「Position/Rotation/ScaleがそれぞれX/Y/Zの1行」
レイアウトで表示します。
</p>
<p>
Position/Scaleは<xref href="Omni.Logical.Scalar.ToString" data-throw-if-not-resolved="false"></xref>/<xref href="Omni.Logical.Scalar.TryParse(System.String%2cOmni.Logical.Scalar%40)" data-throw-if-not-resolved="false"></xref>
を使い、Logical正本のまま任意精度10進文字列として編集します。
Rotationは向きの精度要件がPosition/Scaleほど厳しくないため、
標準の<code>EditorGUILayout.Vector3Field(string, global::UnityEngine.Vector3)</code>(float精度)をそのまま使います。
</p>
<p>
Position/ScaleのX/Y/Zラベルは、<xref href="Omni.Logical.ScalarDragHandle" data-throw-if-not-resolved="false"></xref>により標準Transformと
同じ「ラベルをドラッグして値をスクラブ」操作にも対応しています。
</p>

```csharp
[CustomEditor(typeof(Transform))]
[CanEditMultipleObjects]
[MovedFrom(true, "Omni.Editor", null, "LogicalTransformEditor")]
public sealed class TransformEditor : Editor
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
ScriptableObject ← 
Editor ← 
[TransformEditor](Omni.Logical.TransformEditor.md)

## メソッド（Methods）

### <a id="Omni_Logical_TransformEditor_OnInspectorGUI"></a> OnInspectorGUI\(\)

<p>Implement this function to make a custom inspector.</p>

```csharp
public override void OnInspectorGUI()
```
