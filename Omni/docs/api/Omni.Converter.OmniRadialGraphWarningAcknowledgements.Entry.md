# <a id="Omni_Converter_OmniRadialGraphWarningAcknowledgements_Entry"></a> Class OmniRadialGraphWarningAcknowledgements.Entry

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

確認済みの Graph と、記録したときの内容の指紋です。

```csharp
[Serializable]
public sealed class OmniRadialGraphWarningAcknowledgements.Entry
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniRadialGraphWarningAcknowledgements.Entry](Omni.Converter.OmniRadialGraphWarningAcknowledgements.Entry.md)

## フィールド（Fields）

### <a id="Omni_Converter_OmniRadialGraphWarningAcknowledgements_Entry_contentHash"></a> contentHash

```csharp
[Tooltip("記録したときの Graph の内容の指紋（SHA-256）。Graph を変えると合わなくなり、警告が戻ります。")]
public string contentHash
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniRadialGraphWarningAcknowledgements_Entry_graph"></a> graph

```csharp
[Tooltip("視線の警告を確認済みにした、元の Shader Graph。")]
public Shader graph
```

#### 値（Field Value）

 Shader
