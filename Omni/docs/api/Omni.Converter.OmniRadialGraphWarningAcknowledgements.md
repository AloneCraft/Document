# <a id="Omni_Converter_OmniRadialGraphWarningAcknowledgements"></a> Class OmniRadialGraphWarningAcknowledgements

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

Radial へ変換するときに視線の警告（変換器が直せない View Direction などの使い方）が出る Shader Graph のうち、
利用者が手で直した・問題ないと確かめたものを「確認済み」として記録する表です。プロジェクトのアセットなので Git で共有できます。
項目は元の Graph と、記録したときの Graph の内容の指紋です。Graph を変えると指紋が合わなくなり、警告が戻ります。
解除は Omni Manager の Shaders タブ（1 件・すべて）か、このアセットの Inspector（すべて・項目の削除）で行います。

```csharp
[CreateAssetMenu(menuName = "Omni/Radial Graph Warning Acknowledgements", fileName = "OmniRadialGraphWarningAcknowledgements")]
public sealed class OmniRadialGraphWarningAcknowledgements : ScriptableObject
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
ScriptableObject ← 
[OmniRadialGraphWarningAcknowledgements](Omni.Converter.OmniRadialGraphWarningAcknowledgements.md)

## フィールド（Fields）

### <a id="Omni_Converter_OmniRadialGraphWarningAcknowledgements_DefaultAssetPath"></a> DefaultAssetPath

表が 1 つも無いときに、「確認済みにする」が作る場所です。

```csharp
public const string DefaultAssetPath = "Assets/Settings/Omni/OmniRadialGraphWarningAcknowledgements.asset"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Converter_OmniRadialGraphWarningAcknowledgements_Acknowledge_UnityEngine_Shader_System_String_"></a> Acknowledge\(Shader, string\)

Graph を今の内容で確認済みにします。既に記録があれば指紋を書き換え、無ければ最初の表へ足します。
表が無ければ <xref href="Omni.Converter.OmniRadialGraphWarningAcknowledgements.DefaultAssetPath" data-throw-if-not-resolved="false"></xref> に作ります。Undo できます。書き込んだ表を返します。

```csharp
public static OmniRadialGraphWarningAcknowledgements Acknowledge(Shader graph, string graphText)
```

#### 引数（Parameters）

`graph` Shader

`graphText` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [OmniRadialGraphWarningAcknowledgements](Omni.Converter.OmniRadialGraphWarningAcknowledgements.md)

### <a id="Omni_Converter_OmniRadialGraphWarningAcknowledgements_Clear"></a> Clear\(\)

この表の確認済みを全て外します。Undo できます。外した件数を返します。

```csharp
public int Clear()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Converter_OmniRadialGraphWarningAcknowledgements_ComputeContentHash_System_String_"></a> ComputeContentHash\(string\)

Graph の内容の指紋です。改行は LF にそろえてから求めます（Git の改行の変換で、同じ Graph の指紋が変わらないように）。

```csharp
public static string ComputeContentHash(string graphText)
```

#### 引数（Parameters）

`graphText` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniRadialGraphWarningAcknowledgements_CountAll"></a> CountAll\(\)

プロジェクトの全ての表で、確認済みの記録の数です。

```csharp
public static int CountAll()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Converter_OmniRadialGraphWarningAcknowledgements_GetState_UnityEngine_Shader_System_String_"></a> GetState\(Shader, string\)

プロジェクトの全ての表から、Graph の確認済みの状態を求めます。

```csharp
public static OmniRadialGraphWarningAcknowledgements.State GetState(Shader graph, string graphText)
```

#### 引数（Parameters）

`graph` Shader

`graphText` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [OmniRadialGraphWarningAcknowledgements](Omni.Converter.OmniRadialGraphWarningAcknowledgements.md).[State](Omni.Converter.OmniRadialGraphWarningAcknowledgements.State.md)

### <a id="Omni_Converter_OmniRadialGraphWarningAcknowledgements_Unacknowledge_UnityEngine_Shader_"></a> Unacknowledge\(Shader\)

Graph の確認済みを、全ての表から外します（警告が戻ります）。Undo できます。外した件数を返します。

```csharp
public static int Unacknowledge(Shader graph)
```

#### 引数（Parameters）

`graph` Shader

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Converter_OmniRadialGraphWarningAcknowledgements_UnacknowledgeAll"></a> UnacknowledgeAll\(\)

全ての表の確認済みを外します（全ての警告が戻ります）。Undo できます。外した件数を返します。

```csharp
public static int UnacknowledgeAll()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Converter_OmniRadialGraphWarningAcknowledgements_Changed"></a> Changed

どれかの表の中身が変わったときに呼ばれます（確認済みにする・解除・Inspector での編集・Undo／Redo）。
Omni Manager の Shaders タブは、どの経路で変えても警告の件数と詳細をこれで表に合わせます。

```csharp
public static event Action Changed
```

#### 型（Event Type）

 [Action](https://learn.microsoft.com/dotnet/api/system.action)
