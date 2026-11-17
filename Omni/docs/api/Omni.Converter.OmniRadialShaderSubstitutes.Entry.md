# <a id="Omni_Converter_OmniRadialShaderSubstitutes_Entry"></a> Class OmniRadialShaderSubstitutes.Entry

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

元のShaderと代わりのShaderの組です。

```csharp
[Serializable]
public sealed class OmniRadialShaderSubstitutes.Entry
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniRadialShaderSubstitutes.Entry](Omni.Converter.OmniRadialShaderSubstitutes.Entry.md)

## フィールド（Fields）

### <a id="Omni_Converter_OmniRadialShaderSubstitutes_Entry_source"></a> source

```csharp
[Tooltip("Omniが変換できない元のShader。このShaderの元ファイルは変えません。")]
public Shader source
```

#### 値（Field Value）

 Shader

### <a id="Omni_Converter_OmniRadialShaderSubstitutes_Entry_substitute"></a> substitute

```csharp
[Tooltip("元のShaderと同じPropertyを宣言する、URPのShader。これからRadial版を生成します。")]
public Shader substitute
```

#### 値（Field Value）

 Shader
