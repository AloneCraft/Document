# <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionInputs"></a> Struct OmniAiConversionInputs

Namespace: [Omni.Editor.Manager.AiConversion](Omni.Editor.Manager.AiConversion.md)  
Assembly: Omni.Manager.dll  

<xref href="Omni.Editor.Manager.AiConversion.OmniAiConversionState.Evaluate(Omni.Editor.Manager.AiConversion.OmniAiConversionInputs%40)" data-throw-if-not-resolved="false"></xref> への入力です。呼び出し側が、保存済みのデータから 1 本ぶん組み立てます。

```csharp
public struct OmniAiConversionInputs
```

## フィールド（Fields）

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionInputs_Attempt"></a> Attempt

依頼の試行回数（1 始まり）。<xref href="Omni.Editor.Manager.AiConversion.OmniAiConversionInputs.HasRequest" data-throw-if-not-resolved="false"></xref> が false のときは使わない。

```csharp
public int Attempt
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionInputs_ConfirmedOutputFingerprint"></a> ConfirmedOutputFingerprint

確認済みにしたときの出力の指紋。空なら「生成待ち」（元の指紋の一致だけで確認済みとみなす）。

```csharp
public string ConfirmedOutputFingerprint
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionInputs_ConfirmedSourceFingerprint"></a> ConfirmedSourceFingerprint

確認済みにしたときの元の指紋。

```csharp
public string ConfirmedSourceFingerprint
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionInputs_CurrentSourceFingerprint"></a> CurrentSourceFingerprint

今の元の指紋。

```csharp
public string CurrentSourceFingerprint
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionInputs_Experimental"></a> Experimental

依頼が実験的な経路（Deferred の振り分け I）を有効にしていた。表示の「β」にだけ使う。

```csharp
public bool Experimental
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionInputs_HasConfirmation"></a> HasConfirmation

確認済みの表に、この Shader の記録が有る。

```csharp
public bool HasConfirmation
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionInputs_HasJudge"></a> HasJudge

機械判定の結果（judge.json）が有る。

```csharp
public bool HasJudge
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionInputs_HasRequest"></a> HasRequest

この Shader への AI 依頼（request.json）が有る。

```csharp
public bool HasRequest
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionInputs_HasResult"></a> HasResult

今の依頼（試行回数が一致するもの）に対する AI の結果が取り込み済みである。

```csharp
public bool HasResult
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionInputs_JudgeOutputFingerprint"></a> JudgeOutputFingerprint

判定したときの出力（生成物）の指紋。生成物が無い間は空。

```csharp
public string JudgeOutputFingerprint
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionInputs_JudgePassed"></a> JudgePassed

機械判定が成功した。

```csharp
public bool JudgePassed
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionInputs_JudgeSourceFingerprint"></a> JudgeSourceFingerprint

判定したときの元の指紋。今の指紋と違えば、その判定は今の内容に対するものではない。

```csharp
public string JudgeSourceFingerprint
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionInputs_RequestSourceFingerprint"></a> RequestSourceFingerprint

依頼したときの元の指紋。

```csharp
public string RequestSourceFingerprint
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionInputs_ResultAction"></a> ResultAction

AI の結果の action（"modified" か "none"。<xref href="Omni.Editor.Manager.AiConversion.OmniAiConversionResult.EffectiveAction" data-throw-if-not-resolved="false"></xref> を渡す）。

```csharp
public string ResultAction
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
