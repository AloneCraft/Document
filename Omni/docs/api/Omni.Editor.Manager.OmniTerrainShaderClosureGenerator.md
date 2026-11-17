# <a id="Omni_Editor_Manager_OmniTerrainShaderClosureGenerator"></a> Class OmniTerrainShaderClosureGenerator

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

URP TerrainLit と、その Add/Base/Basemap・Scene View 選択参照を一括生成します。

<p>
これは <xref href="Omni.Editor.Manager.OmniShaderGenerator" data-throw-if-not-resolved="false"></xref> の通常入口とは分けています。通常入口は Hidden
Shader を拒否する安全契約を持つため、Terrain の依存閉包だけを明示的に許可する方が
ポストプロセスなど全 Hidden Shader を誤変換するより安全です。
</p>
<p>
Galaxy を含む Runtime Scene では直接使いません。Omni Manager の Shader 生成と、
Terrain Material を置換する直前の Editor 経路から呼び出します。
</p>

```csharp
public static class OmniTerrainShaderClosureGenerator
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniTerrainShaderClosureGenerator](Omni.Editor.Manager.OmniTerrainShaderClosureGenerator.md)

## メソッド（Methods）

### <a id="Omni_Editor_Manager_OmniTerrainShaderClosureGenerator_Generate"></a> Generate\(\)

TerrainLit の必須依存をすべてメモリ上で検証してから、まとめて生成先へ公開します。

<p>
途中で 1 つでも読めない・変換できない場合、Terrain Material には一切触れません。
既存の生成物は診断用に残ることがありますが、<xref href="Omni.Editor.Manager.TerrainShaderClosureResult.IsReady" data-throw-if-not-resolved="false"></xref>
が false の限り、呼び出し側はそれを適用してはいけません。
</p>

```csharp
public static TerrainShaderClosureResult Generate()
```

#### 戻り値（Returns）

 [TerrainShaderClosureResult](Omni.Editor.Manager.TerrainShaderClosureResult.md)

閉包の成否、source fingerprint、生成先と不足依存を含む診断結果。

### <a id="Omni_Editor_Manager_OmniTerrainShaderClosureGenerator_IsTerrainClosureSource_System_String_"></a> IsTerrainClosureSource\(string\)

Terrain 専用閉包に属する URP Shader かを返します。
通常の SRP 一括生成がこれらを個別に処理しないようにする境界です。

```csharp
public static bool IsTerrainClosureSource(string shaderPath)
```

#### 引数（Parameters）

`shaderPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

Unity の論理アセットパス。null/空は false です。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

Terrain 依存閉包のソースなら true。

### <a id="Omni_Editor_Manager_OmniTerrainShaderClosureGenerator_TryPrepareTerrainLitReplacement_UnityEngine_Material_UnityEngine_Shader__Omni_Editor_Manager_TerrainShaderClosureResult__"></a> TryPrepareTerrainLitReplacement\(Material, out Shader, out TerrainShaderClosureResult\)

TerrainLit Material を変更せず、置換先 Shader だけを安全に準備します。
呼び出し側は true のときだけ複製 Material を作り、最後に Terrain.materialTemplate を
1 回だけ差し替えてください。

```csharp
public static bool TryPrepareTerrainLitReplacement(Material sourceMaterial, out Shader radialShader, out TerrainShaderClosureResult result)
```

#### 引数（Parameters）

`sourceMaterial` Material

元の TerrainLit Material。null は失敗です。

`radialShader` Shader

成功時の生成済み TerrainLit Shader。失敗時は null。

`result` [TerrainShaderClosureResult](Omni.Editor.Manager.TerrainShaderClosureResult.md)

依存不足や生成schemaを含む診断結果。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

元 Material を変更せず置換先 Shader を取得できた場合だけ true。
