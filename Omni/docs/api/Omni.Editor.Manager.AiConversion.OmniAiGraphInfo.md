# <a id="Omni_Editor_Manager_AiConversion_OmniAiGraphInfo"></a> Class OmniAiGraphInfo

Namespace: [Omni.Editor.Manager.AiConversion](Omni.Editor.Manager.AiConversion.md)  
Assembly: Omni.Manager.dll  

Shader Graph のときの作業内容です。

```csharp
[Serializable]
public sealed class OmniAiGraphInfo
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniAiGraphInfo](Omni.Editor.Manager.AiConversion.OmniAiGraphInfo.md)

## フィールド（Fields）

### <a id="Omni_Editor_Manager_AiConversion_OmniAiGraphInfo_customFunctionFiles"></a> customFunctionFiles

```csharp
public List<string> customFunctionFiles
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Editor_Manager_AiConversion_OmniAiGraphInfo_mode"></a> mode

"direct"（.shadergraph を直接編集した）／"manual"（手順書）／""（Graph ではない）。

```csharp
public string mode
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiGraphInfo_steps"></a> steps

```csharp
public List<string> steps
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>
