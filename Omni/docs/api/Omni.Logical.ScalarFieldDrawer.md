# <a id="Omni_Logical_ScalarFieldDrawer"></a> Class ScalarFieldDrawer

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Omni.Editor.dll  

<xref href="Omni.Logical.ScalarField" data-throw-if-not-resolved="false"></xref>のInspector表示です。

<p>
既定のインスペクタは内部のlimb配列(<code>ulong[]</code>)をそのまま表示してしまい編集できません。
<xref href="Omni.Logical.TransformEditor" data-throw-if-not-resolved="false"></xref>と同様に、<xref href="Omni.Logical.Scalar.ToString" data-throw-if-not-resolved="false"></xref>/
共通の論理数式評価器で編集します。式自体は保存せず評価した数値だけを保存します。
ラベルは<xref href="Omni.Logical.ScalarDragHandle" data-throw-if-not-resolved="false"></xref>により標準Transformと同じ
「ラベルをドラッグして値をスクラブ」操作にも対応しています。
</p>

```csharp
[CustomPropertyDrawer(typeof(ScalarField))]
[MovedFrom(true, "Omni.Editor", null, "LogicalScalarFieldDrawer")]
public sealed class ScalarFieldDrawer : PropertyDrawer
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
GUIDrawer ← 
PropertyDrawer ← 
[ScalarFieldDrawer](Omni.Logical.ScalarFieldDrawer.md)

## メソッド（Methods）

### <a id="Omni_Logical_ScalarFieldDrawer_CreatePropertyGUI_UnityEditor_SerializedProperty_"></a> CreatePropertyGUI\(SerializedProperty\)

UI Toolkit Inspectorでも同じIMGUI入力をホストし、確定・取消の挙動を統一します。

```csharp
public override VisualElement CreatePropertyGUI(SerializedProperty property)
```

#### 引数（Parameters）

`property` SerializedProperty

#### 戻り値（Returns）

 VisualElement

### <a id="Omni_Logical_ScalarFieldDrawer_GetPropertyHeight_UnityEditor_SerializedProperty_UnityEngine_GUIContent_"></a> GetPropertyHeight\(SerializedProperty, GUIContent\)

<p>Override this method to specify how tall the GUI for this field is in pixels.</p>

```csharp
public override float GetPropertyHeight(SerializedProperty property, GUIContent label)
```

#### 引数（Parameters）

`property` SerializedProperty

The SerializedProperty to make the custom GUI for.

`label` GUIContent

The label of this property.

#### 戻り値（Returns）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

<p>The height in pixels.</p>

### <a id="Omni_Logical_ScalarFieldDrawer_OnGUI_UnityEngine_Rect_UnityEditor_SerializedProperty_UnityEngine_GUIContent_"></a> OnGUI\(Rect, SerializedProperty, GUIContent\)

<p>Override this method to make your own IMGUI based GUI for the property.</p>

```csharp
public override void OnGUI(Rect position, SerializedProperty property, GUIContent label)
```

#### 引数（Parameters）

`position` Rect

Rectangle on the screen to use for the property GUI.

`property` SerializedProperty

The SerializedProperty to make the custom GUI for.

`label` GUIContent

The label of this property.
