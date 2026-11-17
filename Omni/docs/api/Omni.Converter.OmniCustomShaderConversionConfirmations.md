# <a id="Omni_Converter_OmniCustomShaderConversionConfirmations"></a> Class OmniCustomShaderConversionConfirmations

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

自作 Shader（利用者が編集できる .shader／.shadergraph）の AI 変換依頼で、機械判定に合格した結果を利用者が
「確認済み」にした記録と、機械判定の誤検出を「この検出は誤り」と承認した記録を持つ表です。
プロジェクトのアセットなので Git で共有できます（<xref href="Omni.Converter.OmniRadialGraphWarningAcknowledgements" data-throw-if-not-resolved="false"></xref> と同じ作りです）。

<p>
項目は元 Shader と、確認したときの（元の指紋, 出力の指紋）です。元か出力が変わると指紋が合わなくなり、
「確認済み」から「変換済み・未確認」へ戻ります。指紋は <code>OmniSourceFingerprints</code> が取った値を文字列で受け取ります
（この表は指紋の式を知りません）。
</p>
<p>
承認した検出は、検出箇所の指紋の一覧として元 Shader ごとに持ちます。確認済みにする前にも承認できるので、
項目は「確認なしで承認だけ」の状態を取れます。
</p>

```csharp
[CreateAssetMenu(menuName = "Omni/Custom Shader Conversion Confirmations", fileName = "OmniCustomShaderConversionConfirmations")]
public sealed class OmniCustomShaderConversionConfirmations : ScriptableObject
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
ScriptableObject ← 
[OmniCustomShaderConversionConfirmations](Omni.Converter.OmniCustomShaderConversionConfirmations.md)

## フィールド（Fields）

### <a id="Omni_Converter_OmniCustomShaderConversionConfirmations_CurrentJudgeSchema"></a> CurrentJudgeSchema

機械判定の仕様の版です。判定の規則（J1〜J6／G1〜G5）を変えて、過去の合格を信用できなくなったときに上げます。
記録の版と違う項目は <xref href="Omni.Converter.OmniCustomShaderConversionConfirmations.State.Changed" data-throw-if-not-resolved="false"></xref> になり、利用者が確かめ直します。

```csharp
public const int CurrentJudgeSchema = 1
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Converter_OmniCustomShaderConversionConfirmations_DefaultAssetPath"></a> DefaultAssetPath

表が 1 つも無いときに、「確認済みにする」が作る場所です。

```csharp
public const string DefaultAssetPath = "Assets/Settings/Omni/OmniCustomShaderConversionConfirmations.asset"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniCustomShaderConversionConfirmations_KindGraph"></a> KindGraph

```csharp
public const string KindGraph = "graph"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniCustomShaderConversionConfirmations_KindShaderLab"></a> KindShaderLab

```csharp
public const string KindShaderLab = "shaderlab"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Converter_OmniCustomShaderConversionConfirmations_ApproveSilentHit_UnityEngine_Shader_System_String_System_String_"></a> ApproveSilentHit\(Shader, string, string\)

機械判定の検出（<code>OmniJudgeSilentHit.fingerprint</code>）を「誤り」と承認します。確認済みでなくても記録できます。
既に承認済みなら何もせず false を返します。Undo できます。

```csharp
public static bool ApproveSilentHit(Shader source, string kind, string hitFingerprint)
```

#### 引数（Parameters）

`source` Shader

`kind` [string](https://learn.microsoft.com/dotnet/api/system.string)

`hitFingerprint` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniCustomShaderConversionConfirmations_Clear"></a> Clear\(\)

この表の全ての項目（確認と承認）を消します。Undo できます。消した項目の数を返します。

```csharp
public int Clear()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Converter_OmniCustomShaderConversionConfirmations_ClearConfirmations"></a> ClearConfirmations\(\)

この表の確認済みを全て外します（承認した検出は残します）。Undo できます。外した件数を返します。

```csharp
public int ClearConfirmations()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Converter_OmniCustomShaderConversionConfirmations_Confirm_UnityEngine_Shader_System_String_System_String_System_String_"></a> Confirm\(Shader, string, string, string\)

元の Shader を今の指紋で確認済みにします。既に項目があれば書き換え（承認した検出は残します）、無ければ最初の表へ足します。
表が無ければ <xref href="Omni.Converter.OmniCustomShaderConversionConfirmations.DefaultAssetPath" data-throw-if-not-resolved="false"></xref> に作ります。Undo できます。書き込んだ表を返します。

```csharp
public static OmniCustomShaderConversionConfirmations Confirm(Shader source, string kind, string sourceFingerprint, string outputFingerprint)
```

#### 引数（Parameters）

`source` Shader

`kind` [string](https://learn.microsoft.com/dotnet/api/system.string)

`sourceFingerprint` [string](https://learn.microsoft.com/dotnet/api/system.string)

`outputFingerprint` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [OmniCustomShaderConversionConfirmations](Omni.Converter.OmniCustomShaderConversionConfirmations.md)

### <a id="Omni_Converter_OmniCustomShaderConversionConfirmations_CountAll"></a> CountAll\(\)

プロジェクトの全ての表で、項目（確認と承認）の数です。

```csharp
public static int CountAll()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Converter_OmniCustomShaderConversionConfirmations_Evaluate_UnityEngine_Shader_System_String_System_String_"></a> Evaluate\(Shader, string, string\)

元の Shader の確認済みの状態を、プロジェクトの全ての表から求めます。
<code class="paramref">currentOutputFingerprint</code> が空（生成物が無い clone 直後）のときは、元の指紋と判定の版だけで比べます。

```csharp
public static OmniCustomShaderConversionConfirmations.State Evaluate(Shader source, string currentSourceFingerprint, string currentOutputFingerprint)
```

#### 引数（Parameters）

`source` Shader

`currentSourceFingerprint` [string](https://learn.microsoft.com/dotnet/api/system.string)

`currentOutputFingerprint` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [OmniCustomShaderConversionConfirmations](Omni.Converter.OmniCustomShaderConversionConfirmations.md).[State](Omni.Converter.OmniCustomShaderConversionConfirmations.State.md)

### <a id="Omni_Converter_OmniCustomShaderConversionConfirmations_Evaluate_System_String_System_String_System_String_"></a> Evaluate\(string, string, string\)

<xref href="Omni.Converter.OmniCustomShaderConversionConfirmations.Evaluate(UnityEngine.Shader%2cSystem.String%2cSystem.String)" data-throw-if-not-resolved="false"></xref> の、アセットのパスで指定する版です。

```csharp
public static OmniCustomShaderConversionConfirmations.State Evaluate(string sourcePath, string currentSourceFingerprint, string currentOutputFingerprint)
```

#### 引数（Parameters）

`sourcePath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`currentSourceFingerprint` [string](https://learn.microsoft.com/dotnet/api/system.string)

`currentOutputFingerprint` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [OmniCustomShaderConversionConfirmations](Omni.Converter.OmniCustomShaderConversionConfirmations.md).[State](Omni.Converter.OmniCustomShaderConversionConfirmations.State.md)

### <a id="Omni_Converter_OmniCustomShaderConversionConfirmations_RevokeSilentHit_UnityEngine_Shader_System_String_"></a> RevokeSilentHit\(Shader, string\)

承認した検出を取り消します（検出が戻ります）。取り消せたら true。Undo できます。

```csharp
public static bool RevokeSilentHit(Shader source, string hitFingerprint)
```

#### 引数（Parameters）

`source` Shader

`hitFingerprint` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniCustomShaderConversionConfirmations_TryGetApprovedFingerprints_System_String_System_Collections_Generic_HashSet_System_String___"></a> TryGetApprovedFingerprints\(string, out HashSet<string\>\)

元の Shader で承認済みの検出の指紋を集めます（機械判定の <code>JudgeOptions.approvedSilentHits</code> に渡します）。
承認が1件も無ければ false で、<code class="paramref">fingerprints</code> は空の集合です。

```csharp
public static bool TryGetApprovedFingerprints(string sourcePath, out HashSet<string> fingerprints)
```

#### 引数（Parameters）

`sourcePath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`fingerprints` [HashSet](https://learn.microsoft.com/dotnet/api/system.collections.generic.hashset\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniCustomShaderConversionConfirmations_Unconfirm_UnityEngine_Shader_"></a> Unconfirm\(Shader\)

元の Shader の確認済みを全ての表から外します（青へ戻ります）。承認した検出は残します。Undo できます。
確認を外した件数を返します。

```csharp
public static int Unconfirm(Shader source)
```

#### 引数（Parameters）

`source` Shader

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Converter_OmniCustomShaderConversionConfirmations_UnconfirmAll"></a> UnconfirmAll\(\)

全ての表の確認済みを外します。承認した検出は残します。Undo できます。外した件数を返します。

```csharp
public static int UnconfirmAll()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Converter_OmniCustomShaderConversionConfirmations_Changed"></a> Changed

どれかの表の中身が変わったときに呼ばれます（確認・解除・承認・Inspector での編集・Undo／Redo）。
Omni Manager の Shaders タブは、どの経路で変えても状態の表示をこれで表に合わせます。

```csharp
public static event Action Changed
```

#### 型（Event Type）

 [Action](https://learn.microsoft.com/dotnet/api/system.action)
