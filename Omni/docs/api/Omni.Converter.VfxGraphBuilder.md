# <a id="Omni_Converter_VfxGraphBuilder"></a> Class VfxGraphBuilder

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

VFX Graph のグラフを組み立てる薄い層です（<xref href="Omni.Converter.VfxGraphAuthoring.Author(System.String%2cSystem.Action%7bOmni.Converter.VfxGraphBuilder%7d%2cSystem.Boolean)" data-throw-if-not-resolved="false"></xref> が渡します）。
Context・Block・Operator・公開パラメーターを型名と設定名で作り、slot を名前で繋ぎます。
返す値は VFX Graph の internal のモデルなので、このクラスのメソッドにだけ渡してください。
型・設定・slot が見つからないときは、名前と候補を含む例外で止めます。

```csharp
public sealed class VfxGraphBuilder
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VfxGraphBuilder](Omni.Converter.VfxGraphBuilder.md)

## フィールド（Fields）

### <a id="Omni_Converter_VfxGraphBuilder_CustomHlslBlockType"></a> CustomHlslBlockType

Custom HLSL のブロックの型の完全名（同名の演算子があるため完全名で引きます）。

```csharp
public const string CustomHlslBlockType = "UnityEditor.VFX.Block.CustomHLSL"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Converter_VfxGraphBuilder_Block_System_Object_System_String_System_ValueTuple_System_String_System_Object____"></a> Block\(object, string, params \(string Name, object Value\)\[\]\)

ブロックを作り、設定を入れてから Context へ足します。

```csharp
public object Block(object context, string typeName, params (string Name, object Value)[] settings)
```

#### 引数（Parameters）

`context` [object](https://learn.microsoft.com/dotnet/api/system.object)

`typeName` [string](https://learn.microsoft.com/dotnet/api/system.string)

`settings` \([string](https://learn.microsoft.com/dotnet/api/system.string) [Name](https://learn.microsoft.com/dotnet/api/system.valuetuple\-system.string,system.object\-.name), [object](https://learn.microsoft.com/dotnet/api/system.object) [Value](https://learn.microsoft.com/dotnet/api/system.valuetuple\-system.string,system.object\-.value)\)\[\]

#### 戻り値（Returns）

 [object](https://learn.microsoft.com/dotnet/api/system.object)

### <a id="Omni_Converter_VfxGraphBuilder_Box_UnityEngine_Vector3_UnityEngine_Vector3_"></a> Box\(Vector3, Vector3\)

境界箱（AABox）の値です。<xref href="Omni.Converter.VfxGraphBuilder.SetValue(System.Object%2cSystem.Object)" data-throw-if-not-resolved="false"></xref> で bounds の slot へ入れます。

```csharp
public object Box(Vector3 center, Vector3 size)
```

#### 引数（Parameters）

`center` Vector3

`size` Vector3

#### 戻り値（Returns）

 [object](https://learn.microsoft.com/dotnet/api/system.object)

### <a id="Omni_Converter_VfxGraphBuilder_ComposedQuadOutput_UnityEngine_Vector2_"></a> ComposedQuadOutput\(Vector2\)

VFX Graph package の既定の ShaderGraph で描く、Quad の Composed 出力を作ります。

```csharp
public object ComposedQuadOutput(Vector2 position)
```

#### 引数（Parameters）

`position` Vector2

#### 戻り値（Returns）

 [object](https://learn.microsoft.com/dotnet/api/system.object)

### <a id="Omni_Converter_VfxGraphBuilder_ComposedQuadStripOutput_UnityEngine_Vector2_"></a> ComposedQuadStripOutput\(Vector2\)

VFX Graph package の既定の ShaderGraph で描く、Quad Strip の Composed 出力を作ります（粒子のデータは Strip にします）。

```csharp
public object ComposedQuadStripOutput(Vector2 position)
```

#### 引数（Parameters）

`position` Vector2

#### 戻り値（Returns）

 [object](https://learn.microsoft.com/dotnet/api/system.object)

### <a id="Omni_Converter_VfxGraphBuilder_Connect_System_Object_System_Object_"></a> Connect\(object, object\)

公開パラメーターの出力を入力 slot へ繋ぎます。

```csharp
public void Connect(object parameter, object input)
```

#### 引数（Parameters）

`parameter` [object](https://learn.microsoft.com/dotnet/api/system.object)

`input` [object](https://learn.microsoft.com/dotnet/api/system.object)

### <a id="Omni_Converter_VfxGraphBuilder_Context_System_String_UnityEngine_Vector2_"></a> Context\(string, Vector2\)

Context（VFXBasicSpawner、VFXBasicInitialize、VFXPlanarPrimitiveOutput など）を作ってグラフへ足します。

```csharp
public object Context(string typeName, Vector2 position)
```

#### 引数（Parameters）

`typeName` [string](https://learn.microsoft.com/dotnet/api/system.string)

`position` Vector2

#### 戻り値（Returns）

 [object](https://learn.microsoft.com/dotnet/api/system.object)

### <a id="Omni_Converter_VfxGraphBuilder_CustomHlslBlock_System_Object_System_String_"></a> CustomHlslBlock\(object, string\)

Custom HLSL のブロックを足します。入力 slot は関数の引数から作られ、名前は引数名の前に "_" が付きます
（例: <code>in float radius</code> → <code>_radius</code>）。

```csharp
public object CustomHlslBlock(object context, string hlslCode)
```

#### 引数（Parameters）

`context` [object](https://learn.microsoft.com/dotnet/api/system.object)

`hlslCode` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [object](https://learn.microsoft.com/dotnet/api/system.object)

### <a id="Omni_Converter_VfxGraphBuilder_DataOf_System_Object_"></a> DataOf\(object\)

Context の粒子のデータ（capacity、boundsMode などの設定を持つ）。

```csharp
public object DataOf(object context)
```

#### 引数（Parameters）

`context` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [object](https://learn.microsoft.com/dotnet/api/system.object)

### <a id="Omni_Converter_VfxGraphBuilder_FirstInput_System_Object_"></a> FirstInput\(object\)

```csharp
public object FirstInput(object model)
```

#### 引数（Parameters）

`model` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [object](https://learn.microsoft.com/dotnet/api/system.object)

### <a id="Omni_Converter_VfxGraphBuilder_Input_System_Object_System_Int32_"></a> Input\(object, int\)

```csharp
public object Input(object model, int index)
```

#### 引数（Parameters）

`model` [object](https://learn.microsoft.com/dotnet/api/system.object)

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [object](https://learn.microsoft.com/dotnet/api/system.object)

### <a id="Omni_Converter_VfxGraphBuilder_Link_System_Object_System_Object_"></a> Link\(object, object\)

Context の流れを繋ぎます（繋げない組み合わせは例外）。

```csharp
public void Link(object from, object to)
```

#### 引数（Parameters）

`from` [object](https://learn.microsoft.com/dotnet/api/system.object)

`to` [object](https://learn.microsoft.com/dotnet/api/system.object)

### <a id="Omni_Converter_VfxGraphBuilder_LinkSlots_System_Object_System_Object_"></a> LinkSlots\(object, object\)

```csharp
public void LinkSlots(object output, object input)
```

#### 引数（Parameters）

`output` [object](https://learn.microsoft.com/dotnet/api/system.object)

`input` [object](https://learn.microsoft.com/dotnet/api/system.object)

### <a id="Omni_Converter_VfxGraphBuilder_Operator_System_String_UnityEngine_Vector2_"></a> Operator\(string, Vector2\)

Operator（Multiply、Length、ChangeSpace など）を作ってグラフへ足します。

```csharp
public object Operator(string typeName, Vector2 position)
```

#### 引数（Parameters）

`typeName` [string](https://learn.microsoft.com/dotnet/api/system.string)

`position` Vector2

#### 戻り値（Returns）

 [object](https://learn.microsoft.com/dotnet/api/system.object)

### <a id="Omni_Converter_VfxGraphBuilder_Output_System_Object_System_Int32_"></a> Output\(object, int\)

```csharp
public object Output(object model, int index)
```

#### 引数（Parameters）

`model` [object](https://learn.microsoft.com/dotnet/api/system.object)

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [object](https://learn.microsoft.com/dotnet/api/system.object)

### <a id="Omni_Converter_VfxGraphBuilder_OverrideSurfaceType_System_Object_System_Boolean_"></a> OverrideSurfaceType\(object, bool\)

Material Override を許す ShaderGraph の出力の Surface を上書きします（Inspector の「Surface Type」と同じ設定）。
URP の VFX 出力は Surface を materialSettings の _Surface（0: Opaque、1: Transparent）から読みます。

```csharp
public void OverrideSurfaceType(object output, bool opaque)
```

#### 引数（Parameters）

`output` [object](https://learn.microsoft.com/dotnet/api/system.object)

`opaque` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_VfxGraphBuilder_Parameter_System_Type_System_String_System_Object_UnityEngine_Vector2_"></a> Parameter\(Type, string, object, Vector2\)

公開パラメーターを作ります。<code class="paramref">value</code> が null なら既定値のままにします（Texture など）。

```csharp
public object Parameter(Type type, string exposedName, object value, Vector2 position)
```

#### 引数（Parameters）

`type` [Type](https://learn.microsoft.com/dotnet/api/system.type)

`exposedName` [string](https://learn.microsoft.com/dotnet/api/system.string)

`value` [object](https://learn.microsoft.com/dotnet/api/system.object)

`position` Vector2

#### 戻り値（Returns）

 [object](https://learn.microsoft.com/dotnet/api/system.object)

### <a id="Omni_Converter_VfxGraphBuilder_Set_System_Object_System_String_System_Object_"></a> Set\(object, string, object\)

設定（VFXSetting）を入れます。列挙型の設定は名前の文字列でも渡せます。

```csharp
public void Set(object model, string setting, object value)
```

#### 引数（Parameters）

`model` [object](https://learn.microsoft.com/dotnet/api/system.object)

`setting` [string](https://learn.microsoft.com/dotnet/api/system.string)

`value` [object](https://learn.microsoft.com/dotnet/api/system.object)

### <a id="Omni_Converter_VfxGraphBuilder_SetPositionValue_System_Object_UnityEngine_Vector3_"></a> SetPositionValue\(object, Vector3\)

Position 型の slot（SetAttribute position の入力）へ、Local 空間の固定位置を入れます。

```csharp
public void SetPositionValue(object slot, Vector3 position)
```

#### 引数（Parameters）

`slot` [object](https://learn.microsoft.com/dotnet/api/system.object)

`position` Vector3

### <a id="Omni_Converter_VfxGraphBuilder_SetSlotSpace_System_Object_System_String_"></a> SetSlotSpace\(object, string\)

空間を持つ slot（位置・球など）の空間。

```csharp
public void SetSlotSpace(object slot, string space)
```

#### 引数（Parameters）

`slot` [object](https://learn.microsoft.com/dotnet/api/system.object)

`space` [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_VfxGraphBuilder_SetSpace_System_Object_System_String_"></a> SetSpace\(object, string\)

Context の空間（"Local" または "World"）。

```csharp
public void SetSpace(object context, string space)
```

#### 引数（Parameters）

`context` [object](https://learn.microsoft.com/dotnet/api/system.object)

`space` [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_VfxGraphBuilder_SetValue_System_Object_System_Object_"></a> SetValue\(object, object\)

slot の値（float、Vector3、Texture、<xref href="Omni.Converter.VfxGraphBuilder.Box(UnityEngine.Vector3%2cUnityEngine.Vector3)" data-throw-if-not-resolved="false"></xref> の値など）を入れます。

```csharp
public void SetValue(object slot, object value)
```

#### 引数（Parameters）

`slot` [object](https://learn.microsoft.com/dotnet/api/system.object)

`value` [object](https://learn.microsoft.com/dotnet/api/system.object)

### <a id="Omni_Converter_VfxGraphBuilder_Slot_System_Object_System_String___"></a> Slot\(object, params string\[\]\)

入力 slot を名前の経路で引きます（例: "arcSphere", "sphere", "radius"）。

```csharp
public object Slot(object model, params string[] path)
```

#### 引数（Parameters）

`model` [object](https://learn.microsoft.com/dotnet/api/system.object)

`path` [string](https://learn.microsoft.com/dotnet/api/system.string)\[\]

#### 戻り値（Returns）

 [object](https://learn.microsoft.com/dotnet/api/system.object)

### <a id="Omni_Converter_VfxGraphBuilder_WorldLengthOfLocalUnit_UnityEngine_Vector2_"></a> WorldLengthOfLocalUnit\(Vector2\)

Local 空間の (1, 0, 0) を World 空間へ変換した長さ（Effect の縮尺）を出す Operator の出力 slot です。

```csharp
public object WorldLengthOfLocalUnit(Vector2 position)
```

#### 引数（Parameters）

`position` Vector2

#### 戻り値（Returns）

 [object](https://learn.microsoft.com/dotnet/api/system.object)
