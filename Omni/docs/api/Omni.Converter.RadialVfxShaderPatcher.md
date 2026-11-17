# <a id="Omni_Converter_RadialVfxShaderPatcher"></a> Class RadialVfxShaderPatcher

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

外部化VFX presentation shaderへRadial描画フックを冪等注入します。

```csharp
public static class RadialVfxShaderPatcher
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialVfxShaderPatcher](Omni.Converter.RadialVfxShaderPatcher.md)

## フィールド（Fields）

### <a id="Omni_Converter_RadialVfxShaderPatcher_DecalOutputMarker"></a> DecalOutputMarker

```csharp
public const string DecalOutputMarker = "#define OMNI_RADIAL_VFX_DECAL_OUTPUT 1"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_RadialVfxShaderPatcher_InjectInclude"></a> InjectInclude

```csharp
public static readonly string InjectInclude
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_RadialVfxShaderPatcher_SchemaMarker"></a> SchemaMarker

```csharp
public const string SchemaMarker = "// OMNI_RADIAL_VFX_PATCH_SCHEMA 7"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_RadialVfxShaderPatcher_SchemaVersion"></a> SchemaVersion

```csharp
public const int SchemaVersion = 7
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Converter_RadialVfxShaderPatcher_SentinelProperty"></a> SentinelProperty

```csharp
public const string SentinelProperty = "_OmniRadialVfxPatched"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Converter_RadialVfxShaderPatcher_Patch_System_String_"></a> Patch\(string\)

```csharp
public static RadialVfxShaderPatcher.PatchResult Patch(string source)
```

#### 引数（Parameters）

`source` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [RadialVfxShaderPatcher](Omni.Converter.RadialVfxShaderPatcher.md).[PatchResult](Omni.Converter.RadialVfxShaderPatcher.PatchResult.md)
