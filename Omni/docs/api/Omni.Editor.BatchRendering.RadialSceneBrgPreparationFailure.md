# <a id="Omni_Editor_BatchRendering_RadialSceneBrgPreparationFailure"></a> Class RadialSceneBrgPreparationFailure

Namespace: [Omni.Editor.BatchRendering](Omni.Editor.BatchRendering.md)  
Assembly: Omni.Editor.dll  

sidecar準備の失敗内容です。原因のMaterial、Shader、段階、影響先を保持します。

```csharp
public sealed class RadialSceneBrgPreparationFailure
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialSceneBrgPreparationFailure](Omni.Editor.BatchRendering.RadialSceneBrgPreparationFailure.md)

## コンストラクター（Constructors）

### <a id="Omni_Editor_BatchRendering_RadialSceneBrgPreparationFailure__ctor_Omni_Editor_BatchRendering_RadialSceneBrgPreparationStage_System_String_System_String_System_String_System_String_System_Collections_Generic_IReadOnlyList_System_String__System_Int32_"></a> RadialSceneBrgPreparationFailure\(RadialSceneBrgPreparationStage, string, string, string, string, IReadOnlyList<string\>, int\)

失敗内容を作成します。

```csharp
public RadialSceneBrgPreparationFailure(RadialSceneBrgPreparationStage stage, string sourceMaterialPath, string sourceShaderName, string brgBaseShaderPath, string reason, IReadOnlyList<string> affectedRenderers, int affectedRendererTotal)
```

#### 引数（Parameters）

`stage` [RadialSceneBrgPreparationStage](Omni.Editor.BatchRendering.RadialSceneBrgPreparationStage.md)

失敗した段階。

`sourceMaterialPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

元Materialのasset path。特定できない場合は空文字列。

`sourceShaderName` [string](https://learn.microsoft.com/dotnet/api/system.string)

元MaterialのShader名。特定できない場合は空文字列。

`brgBaseShaderPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

BRG変換の入力にしたRadial Shaderのpath。未解決なら空文字列。

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

生成器が返した理由。

`affectedRenderers` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

影響するRendererの表示名（上限あり）。

`affectedRendererTotal` [int](https://learn.microsoft.com/dotnet/api/system.int32)

上限前の影響Renderer総数。

## プロパティ（Properties）

### <a id="Omni_Editor_BatchRendering_RadialSceneBrgPreparationFailure_AffectedRendererTotal"></a> AffectedRendererTotal

上限前の影響Renderer総数です。

```csharp
public int AffectedRendererTotal { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_BatchRendering_RadialSceneBrgPreparationFailure_AffectedRenderers"></a> AffectedRenderers

影響するロード済みSceneのRenderer（上限あり）です。

```csharp
public IReadOnlyList<string> AffectedRenderers { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Editor_BatchRendering_RadialSceneBrgPreparationFailure_BrgBaseShaderPath"></a> BrgBaseShaderPath

BRG変換の入力にしたRadial Shaderのpathです。

```csharp
public string BrgBaseShaderPath { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_BatchRendering_RadialSceneBrgPreparationFailure_Reason"></a> Reason

生成器が返した理由です。

```csharp
public string Reason { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_BatchRendering_RadialSceneBrgPreparationFailure_SourceMaterialPath"></a> SourceMaterialPath

元Materialのasset pathです。

```csharp
public string SourceMaterialPath { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_BatchRendering_RadialSceneBrgPreparationFailure_SourceShaderName"></a> SourceShaderName

元MaterialのShader名です。

```csharp
public string SourceShaderName { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_BatchRendering_RadialSceneBrgPreparationFailure_Stage"></a> Stage

失敗した段階です。

```csharp
public RadialSceneBrgPreparationStage Stage { get; }
```

#### 値（Property Value）

 [RadialSceneBrgPreparationStage](Omni.Editor.BatchRendering.RadialSceneBrgPreparationStage.md)

## メソッド（Methods）

### <a id="Omni_Editor_BatchRendering_RadialSceneBrgPreparationFailure_ToString"></a> ToString\(\)

Consoleと自動化応答へ出す1行表現です。

```csharp
public override string ToString()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
