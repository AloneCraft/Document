# <a id="Omni_Converter_OmniStandardUrpSources"></a> Class OmniStandardUrpSources

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

Radial版を作るURP同梱の標準Shaderの確定一覧です。利用者の環境で、対数への切替の準備の段に生成します
（同梱カタログを製造していた頃と同じ変換規則。TerrainLitは4本の閉包）。

```csharp
public static class OmniStandardUrpSources
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniStandardUrpSources](Omni.Converter.OmniStandardUrpSources.md)

## フィールド（Fields）

### <a id="Omni_Converter_OmniStandardUrpSources_DecalGraph"></a> DecalGraph

URP既定のDecal Projector用のShader Graphです（一般のShader Graphの注入器で変換します）。

```csharp
public const string DecalGraph = "Packages/com.unity.render-pipelines.universal/Shaders/Decal.shadergraph"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniStandardUrpSources_Ssao"></a> Ssao

URPのSSAOのShaderです（Renderer Featureの資源。Materialでは使いません）。

```csharp
public const string Ssao = "Packages/com.unity.render-pipelines.universal/Shaders/Utils/ScreenSpaceAmbientOcclusion.shader"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniStandardUrpSources_UrpPrefix"></a> UrpPrefix

```csharp
public const string UrpPrefix = "Packages/com.unity.render-pipelines.universal/"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## プロパティ（Properties）

### <a id="Omni_Converter_OmniStandardUrpSources_HandWrittenShaders"></a> HandWrittenShaders

URPの手書きShader（13本）です。

```csharp
public static IReadOnlyList<string> HandWrittenShaders { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Converter_OmniStandardUrpSources_ModuleSources"></a> ModuleSources

手書きShaderとTerrainの閉包をパスの順に並べた17本です（検証のModule Sceneの番号の順）。

```csharp
public static IReadOnlyList<string> ModuleSources { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Converter_OmniStandardUrpSources_StandardGraphs"></a> StandardGraphs

URPに同梱され、Materialに割り当てるShader Graph（5本）です。一般のShader Graphの注入器で変換し、保証表の対象です
（検証のGraphのModule Sceneと同じ一覧）。

```csharp
public static IReadOnlyList<string> StandardGraphs { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Converter_OmniStandardUrpSources_TerrainClosure"></a> TerrainClosure

TerrainLitの閉包（4本）です。

```csharp
public static IReadOnlyList<string> TerrainClosure { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

## メソッド（Methods）

### <a id="Omni_Converter_OmniStandardUrpSources_EnsureGenerated_System_String_System_String__"></a> EnsureGenerated\(string, out string\)

元のURP Shaderから、対数への切替の準備と同じ生成で対数版を用意して返します（検証・テスト・自動化の入口）。
生成できなければ、理由を<code class="paramref">reason</code>へ返してnullを返します。

```csharp
public static Shader EnsureGenerated(string urpRelativePath, out string reason)
```

#### 引数（Parameters）

`urpRelativePath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 Shader

### <a id="Omni_Converter_OmniStandardUrpSources_GetGeneratedHlslPath_System_String_"></a> GetGeneratedHlslPath\(string\)

URP package内の相対パスから、利用者の環境に生成したHLSLの資産パスを返します（生成は別）。

```csharp
public static string GetGeneratedHlslPath(string urpRelativePath)
```

#### 引数（Parameters）

`urpRelativePath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniStandardUrpSources_GetGeneratedShaderPath_System_String_"></a> GetGeneratedShaderPath\(string\)

URP package内の相対パスから、利用者の環境に生成したRadial Shaderの資産パスを返します（生成は別）。

```csharp
public static string GetGeneratedShaderPath(string urpRelativePath)
```

#### 引数（Parameters）

`urpRelativePath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniStandardUrpSources_GetRadialShaderName_System_String_"></a> GetRadialShaderName\(string\)

このShaderのRadial版の生成名（<code>Omni/Radial/&lt;package相対パス&gt;</code>）を返します。

```csharp
public static string GetRadialShaderName(string sourcePath)
```

#### 引数（Parameters）

`sourcePath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniStandardUrpSources_GetSourcePath_System_String_"></a> GetSourcePath\(string\)

URP package内の相対パス（例: <code>Shaders/Lit.shader</code>）から、元Shaderの資産パスを返します。

```csharp
public static string GetSourcePath(string urpRelativePath)
```

#### 引数（Parameters）

`urpRelativePath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
