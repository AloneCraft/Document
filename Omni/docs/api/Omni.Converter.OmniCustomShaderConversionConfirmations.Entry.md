# <a id="Omni_Converter_OmniCustomShaderConversionConfirmations_Entry"></a> Class OmniCustomShaderConversionConfirmations.Entry

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

確認済みの記録と、承認した検出です。

```csharp
[Serializable]
public sealed class OmniCustomShaderConversionConfirmations.Entry
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniCustomShaderConversionConfirmations.Entry](Omni.Converter.OmniCustomShaderConversionConfirmations.Entry.md)

## フィールド（Fields）

### <a id="Omni_Converter_OmniCustomShaderConversionConfirmations_Entry_approvedSilentHits"></a> approvedSilentHits

```csharp
[Tooltip("利用者が「この検出は誤り」と承認した、検出箇所の指紋（SHA-256）。")]
public List<string> approvedSilentHits
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Converter_OmniCustomShaderConversionConfirmations_Entry_confirmedUtc"></a> confirmedUtc

```csharp
[Tooltip("確認した日時（UTC、ISO 8601）。")]
public string confirmedUtc
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniCustomShaderConversionConfirmations_Entry_judgeSchema"></a> judgeSchema

```csharp
[Tooltip("確認したときの機械判定の版。")]
public int judgeSchema
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Converter_OmniCustomShaderConversionConfirmations_Entry_kind"></a> kind

```csharp
[Tooltip("shaderlab か graph。")]
public string kind
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniCustomShaderConversionConfirmations_Entry_outputFingerprint"></a> outputFingerprint

```csharp
[Tooltip("確認したときの出力（生成物）の指紋。空なら生成物が無いまま確認したことを表します。")]
public string outputFingerprint
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniCustomShaderConversionConfirmations_Entry_source"></a> source

```csharp
[Tooltip("確認済みにした、または検出を承認した、元の Shader。")]
public Shader source
```

#### 値（Field Value）

 Shader

### <a id="Omni_Converter_OmniCustomShaderConversionConfirmations_Entry_sourceFingerprint"></a> sourceFingerprint

```csharp
[Tooltip("確認したときの元の指紋。空なら確認済みではありません（承認だけの項目）。")]
public string sourceFingerprint
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
