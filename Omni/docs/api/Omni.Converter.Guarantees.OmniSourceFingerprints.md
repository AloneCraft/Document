# <a id="Omni_Converter_Guarantees_OmniSourceFingerprints"></a> Class OmniSourceFingerprints

Namespace: [Omni.Converter.Guarantees](Omni.Converter.Guarantees.md)  
Assembly: Omni.Converter.dll  

変換の元・出力の指紋を、決まった式（統合仕様 C 節）で取ります。
ShaderLab の include の閉包は Omni.Manager の HLSL 解析が辿るので、Manager が起動時に
<xref href="Omni.Converter.Guarantees.OmniSourceFingerprints.RegisterShaderLabClosure(Omni.Converter.Guarantees.OmniSourceFingerprints.ShaderLabClosure)" data-throw-if-not-resolved="false"></xref> で登録します（Converter は Manager を参照できないため）。

```csharp
public static class OmniSourceFingerprints
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniSourceFingerprints](Omni.Converter.Guarantees.OmniSourceFingerprints.md)

## メソッド（Methods）

### <a id="Omni_Converter_Guarantees_OmniSourceFingerprints_TryGraphOutput_System_String_System_String_Omni_Converter_Guarantees_OmniFingerprint__System_String__System_Boolean_"></a> TryGraphOutput\(string, string, out OmniFingerprint, out string, bool\)

```csharp
public static bool TryGraphOutput(string generatedGraphPath, string outputFormat, out OmniFingerprint fp, out string error, bool projectAssets = false)
```

#### 引数（Parameters）

`generatedGraphPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`outputFormat` [string](https://learn.microsoft.com/dotnet/api/system.string)

`fp` [OmniFingerprint](Omni.Converter.Guarantees.OmniFingerprint.md)

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

`projectAssets` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_Guarantees_OmniSourceFingerprints_TryGraphSource_System_String_System_String_Omni_Converter_Guarantees_OmniFingerprint__System_String__System_Boolean_"></a> TryGraphSource\(string, string, out OmniFingerprint, out string, bool\)

```csharp
public static bool TryGraphSource(string graphPath, string templateSetId, out OmniFingerprint fp, out string error, bool projectAssets = false)
```

#### 引数（Parameters）

`graphPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`templateSetId` [string](https://learn.microsoft.com/dotnet/api/system.string)

`fp` [OmniFingerprint](Omni.Converter.Guarantees.OmniFingerprint.md)

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

`projectAssets` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_Guarantees_OmniSourceFingerprints_TryShaderLabOutput_System_Collections_Generic_IReadOnlyList_System_String__System_String_Omni_Converter_Guarantees_OmniFingerprint__System_String__System_Boolean_"></a> TryShaderLabOutput\(IReadOnlyList<string\>, string, out OmniFingerprint, out string, bool\)

```csharp
public static bool TryShaderLabOutput(IReadOnlyList<string> unitOutputs, string outputFormat, out OmniFingerprint fp, out string error, bool projectAssets = false)
```

#### 引数（Parameters）

`unitOutputs` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

`outputFormat` [string](https://learn.microsoft.com/dotnet/api/system.string)

`fp` [OmniFingerprint](Omni.Converter.Guarantees.OmniFingerprint.md)

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

`projectAssets` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_Guarantees_OmniSourceFingerprints_TryShaderLabSource_System_Collections_Generic_IReadOnlyList_System_String__Omni_Converter_Guarantees_OmniFingerprint__System_String__System_Boolean_"></a> TryShaderLabSource\(IReadOnlyList<string\>, out OmniFingerprint, out string, bool\)

```csharp
public static bool TryShaderLabSource(IReadOnlyList<string> unitSources, out OmniFingerprint fp, out string error, bool projectAssets = false)
```

#### 引数（Parameters）

`unitSources` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

`fp` [OmniFingerprint](Omni.Converter.Guarantees.OmniFingerprint.md)

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

`projectAssets` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_Guarantees_OmniSourceFingerprints_TryTemplateSet_System_String_Omni_Converter_Guarantees_OmniFingerprint__System_String__"></a> TryTemplateSet\(string, out OmniFingerprint, out string\)

```csharp
public static bool TryTemplateSet(string templateSetId, out OmniFingerprint fp, out string error)
```

#### 引数（Parameters）

`templateSetId` [string](https://learn.microsoft.com/dotnet/api/system.string)

`fp` [OmniFingerprint](Omni.Converter.Guarantees.OmniFingerprint.md)

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_Guarantees_OmniSourceFingerprints_TryVfxOutputTypes_System_String_System_Collections_Generic_IReadOnlyList_System_String___System_String__"></a> TryVfxOutputTypes\(string, out IReadOnlyList<string\>, out string\)

```csharp
public static bool TryVfxOutputTypes(string vfxAssetPath, out IReadOnlyList<string> outputTypes, out string error)
```

#### 引数（Parameters）

`vfxAssetPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`outputTypes` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_Guarantees_OmniSourceFingerprints_TryVfxSource_System_String_System_Int32_Omni_Converter_Guarantees_OmniFingerprint__System_String__"></a> TryVfxSource\(string, int, out OmniFingerprint, out string\)

```csharp
public static bool TryVfxSource(string templateSetId, int patchSchema, out OmniFingerprint fp, out string error)
```

#### 引数（Parameters）

`templateSetId` [string](https://learn.microsoft.com/dotnet/api/system.string)

`patchSchema` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`fp` [OmniFingerprint](Omni.Converter.Guarantees.OmniFingerprint.md)

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_Guarantees_OmniSourceFingerprints_VfxOutput_System_Int32_"></a> VfxOutput\(int\)

```csharp
public static OmniFingerprint VfxOutput(int patchSchema)
```

#### 引数（Parameters）

`patchSchema` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [OmniFingerprint](Omni.Converter.Guarantees.OmniFingerprint.md)
