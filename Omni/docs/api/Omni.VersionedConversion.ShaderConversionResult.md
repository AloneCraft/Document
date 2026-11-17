# <a id="Omni_VersionedConversion_ShaderConversionResult"></a> Class ShaderConversionResult

Namespace: [Omni.VersionedConversion](Omni.VersionedConversion.md)  
Assembly: Omni.VersionedConversion.dll  

シェーダー変換の出力と失敗・除外・副生成物です。

```csharp
public sealed class ShaderConversionResult
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[ShaderConversionResult](Omni.VersionedConversion.ShaderConversionResult.md)

## プロパティ（Properties）

### <a id="Omni_VersionedConversion_ShaderConversionResult_Diagnostics"></a> Diagnostics

```csharp
public List<ShaderPassDiagnostic> Diagnostics { get; }
```

#### 値（Property Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[ShaderPassDiagnostic](Omni.VersionedConversion.ShaderPassDiagnostic.md)\>

### <a id="Omni_VersionedConversion_ShaderConversionResult_FixedFunctionConvertedPasses"></a> FixedFunctionConvertedPasses

```csharp
public int FixedFunctionConvertedPasses { get; set; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_VersionedConversion_ShaderConversionResult_FixedFunctionConvertible"></a> FixedFunctionConvertible

```csharp
public bool FixedFunctionConvertible { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_VersionedConversion_ShaderConversionResult_FixedFunctionReason"></a> FixedFunctionReason

```csharp
public string FixedFunctionReason { get; set; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_VersionedConversion_ShaderConversionResult_InjectedCount"></a> InjectedCount

```csharp
public int InjectedCount { get; set; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_VersionedConversion_ShaderConversionResult_IsFixedFunction"></a> IsFixedFunction

```csharp
public bool IsFixedFunction { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_VersionedConversion_ShaderConversionResult_LightingContractFailed"></a> LightingContractFailed

```csharp
public bool LightingContractFailed { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_VersionedConversion_ShaderConversionResult_LightingContractFailureReason"></a> LightingContractFailureReason

```csharp
public string LightingContractFailureReason { get; set; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_VersionedConversion_ShaderConversionResult_NestedIncludeSidecars"></a> NestedIncludeSidecars

```csharp
public List<KeyValuePair<string, string>> NestedIncludeSidecars { get; }
```

#### 値（Property Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair\-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [string](https://learn.microsoft.com/dotnet/api/system.string)\>\>

### <a id="Omni_VersionedConversion_ShaderConversionResult_Parsed"></a> Parsed

```csharp
public bool Parsed { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_VersionedConversion_ShaderConversionResult_Text"></a> Text

```csharp
public string Text { get; set; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_VersionedConversion_ShaderConversionResult_UnreachableReferences"></a> UnreachableReferences

```csharp
public List<string> UnreachableReferences { get; }
```

#### 値（Property Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>
