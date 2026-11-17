# <a id="Omni_Converter_OmniMaterialShaderSwitchService_BuiltInPlanItem"></a> Class OmniMaterialShaderSwitchService.BuiltInPlanItem

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

```csharp
public sealed class OmniMaterialShaderSwitchService.BuiltInPlanItem
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniMaterialShaderSwitchService.BuiltInPlanItem](Omni.Converter.OmniMaterialShaderSwitchService.BuiltInPlanItem.md)

## フィールド（Fields）

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_BuiltInPlanItem_AssetPath"></a> AssetPath

```csharp
public string AssetPath
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_BuiltInPlanItem_OriginalMaterial"></a> OriginalMaterial

```csharp
public Material OriginalMaterial
```

#### 値（Field Value）

 Material

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_BuiltInPlanItem_SourceShader"></a> SourceShader

```csharp
public Shader SourceShader
```

#### 値（Field Value）

 Shader

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_BuiltInPlanItem_StateHash"></a> StateHash

```csharp
public string StateHash
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_BuiltInPlanItem_TargetShader"></a> TargetShader

```csharp
public Shader TargetShader
```

#### 値（Field Value）

 Shader

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_BuiltInPlanItem_UrpUpgrader"></a> UrpUpgrader

Built-in専用ShaderをURPのShaderへ移すUpgraderです。不要ならnullです。

```csharp
public MaterialUpgrader UrpUpgrader
```

#### 値（Field Value）

 MaterialUpgrader

## プロパティ（Properties）

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_BuiltInPlanItem_UsesUrpUpgrade"></a> UsesUrpUpgrade

管理Materialの写しをURPのShaderへ移してから対数へ切り替えるならtrueです。

```csharp
public bool UsesUrpUpgrade { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
