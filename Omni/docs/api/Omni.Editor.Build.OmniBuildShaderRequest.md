# <a id="Omni_Editor_Build_OmniBuildShaderRequest"></a> Class OmniBuildShaderRequest

Namespace: [Omni.Editor.Build](Omni.Editor.Build.md)  
Assembly: Omni.Editor.dll  

Player 用に残す Shader の集合を計算する入力です（<xref href="Omni.Editor.Build.OmniBuildShaderClosure.Compute(Omni.Editor.Build.OmniBuildShaderRequest)" data-throw-if-not-resolved="false"></xref>）。

```csharp
public sealed class OmniBuildShaderRequest
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniBuildShaderRequest](Omni.Editor.Build.OmniBuildShaderRequest.md)

## フィールド（Fields）

### <a id="Omni_Editor_Build_OmniBuildShaderRequest_ExtraRootAssetPaths"></a> ExtraRootAssetPaths

Scene 以外で Player の依存になる資産（例: WebGPU 用に差し替える月の定義）。

```csharp
public readonly List<string> ExtraRootAssetPaths
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Editor_Build_OmniBuildShaderRequest_Label"></a> Label

ログに出す呼び出し元の名前。

```csharp
public string Label
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Build_OmniBuildShaderRequest_RuntimeLookupAssemblies"></a> RuntimeLookupAssemblies

実行時 Shader 宣言を採用するアセンブリ名。null は全宣言、空集合は宣言を採用しない。

```csharp
public HashSet<string> RuntimeLookupAssemblies
```

#### 値（Field Value）

 [HashSet](https://learn.microsoft.com/dotnet/api/system.collections.generic.hashset\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Editor_Build_OmniBuildShaderRequest_ScenePaths"></a> ScenePaths

Player に入れる Scene（ステージした Scene を含む）。

```csharp
public readonly List<string> ScenePaths
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Editor_Build_OmniBuildShaderRequest_SkipTerrainAddPassWhenLayersUpToFour"></a> SkipTerrainAddPassWhenLayersUpToFour

true にすると、<code class="paramref">ScenePaths</code> の全 Terrain の TerrainLayer が4以下のとき、Terrain Shader の
<code>AddPassShader</code>（層が5以上のときだけ使う追加の Pass 用 Shader）を残さない。Scene を開いて層の数を読む。
層を実行時に足す Scene では使わない（開発用ビルド限定）。

```csharp
public bool SkipTerrainAddPassWhenLayersUpToFour
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Build_OmniBuildShaderRequest_SkipTerrainDetailShadersWhenNoDetails"></a> SkipTerrainDetailShadersWhenNoDetails

true にすると、<code class="paramref">ScenePaths</code> のどの Terrain にも細部（detail prototype）が無いとき、グローバル設定の
Terrain 細部・草の Shader（UniversalRenderPipelineRuntimeTerrainShaders）を残さない。Scene を開いて数える。
Terrain や細部を実行時に足す Scene では使わない（開発用ビルド限定）。

```csharp
public bool SkipTerrainDetailShadersWhenNoDetails
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Build_OmniBuildShaderRequest_StripKeywords"></a> StripKeywords

残す Shader の variant のうち、ここにあるキーワードを 1 つでも含むものを外す（<xref href="Omni.Editor.Build.OmniBuildShaderStripper" data-throw-if-not-resolved="false"></xref>）。
既定は空（何も外さない）。Scene とコードがそのキーワードを使わないと確かめたビルドだけで足す（開発用ビルド限定）。
ある Pass の variant が全部外れる場合は外さず、警告を出す。

```csharp
public readonly HashSet<string> StripKeywords
```

#### 値（Field Value）

 [HashSet](https://learn.microsoft.com/dotnet/api/system.collections.generic.hashset\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Editor_Build_OmniBuildShaderRequest_StripUnclassifiedHidden"></a> StripUnclassifiedHidden

true にすると、どの理由にも当たらない <code>Hidden/</code> の Shader も外す。false（既定）は外さずログに出す。
「パイプライン」の理由が実際にコンパイルされる URP の内部 Shader を覆うと実測で確かめてから true にする。

```csharp
public bool StripUnclassifiedHidden
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Build_OmniBuildShaderRequest_Target"></a> Target

対象のビルド先。<xref href="UnityEditor.BuildTarget.NoTarget" data-throw-if-not-resolved="false"></xref> なら今の Editor の Active Build Target。

```csharp
public BuildTarget Target
```

#### 値（Field Value）

 BuildTarget

## メソッド（Methods）

### <a id="Omni_Editor_Build_OmniBuildShaderRequest_KeepShader_UnityEngine_Shader_System_String_"></a> KeepShader\(Shader, string\)

理由つきで残す Shader を足す。理由はログに出る。

```csharp
public void KeepShader(Shader shader, string reason)
```

#### 引数（Parameters）

`shader` Shader

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)
