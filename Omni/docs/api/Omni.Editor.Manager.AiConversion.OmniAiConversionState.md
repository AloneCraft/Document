# <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionState"></a> Class OmniAiConversionState

Namespace: [Omni.Editor.Manager.AiConversion](Omni.Editor.Manager.AiConversion.md)  
Assembly: Omni.Manager.dll  

状態を決める純粋関数です（UnityEngine を使わない）。順序:
今の元に対する機械判定が成功なら、依頼・AI の結果に関係なく「変換済み」系（機械判定が最終）。
失敗なら、依頼が無ければ「変換不能」、依頼の後に元が変わっていれば「AI 修正後も変換不能」、変わっていなければ
「対応不可」（AI が none と答えた）か「AI 依頼中」。今の元に対する判定が無いときは、依頼が有れば「AI 依頼中」（再判定待ち）。

```csharp
public static class OmniAiConversionState
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniAiConversionState](Omni.Editor.Manager.AiConversion.OmniAiConversionState.md)

## フィールド（Fields）

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionState_ActionModified"></a> ActionModified

```csharp
public const string ActionModified = "modified"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionState_ActionNone"></a> ActionNone

```csharp
public const string ActionNone = "none"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionState_Evaluate_Omni_Editor_Manager_AiConversion_OmniAiConversionInputs__"></a> Evaluate\(in OmniAiConversionInputs\)

```csharp
public static OmniAiConversionStatus Evaluate(in OmniAiConversionInputs i)
```

#### 引数（Parameters）

`i` [OmniAiConversionInputs](Omni.Editor.Manager.AiConversion.OmniAiConversionInputs.md)

#### 戻り値（Returns）

 [OmniAiConversionStatus](Omni.Editor.Manager.AiConversion.OmniAiConversionStatus.md)
