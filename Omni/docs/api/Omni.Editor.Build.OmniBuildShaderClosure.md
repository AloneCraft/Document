# <a id="Omni_Editor_Build_OmniBuildShaderClosure"></a> Class OmniBuildShaderClosure

Namespace: [Omni.Editor.Build](Omni.Editor.Build.md)  
Assembly: Omni.Editor.dll  

Player に残す Shader を、資産（パス）と理由で求めた結果です。名前は表示にだけ使います。
理由: scene、pipeline（対象ビルドの URP 資産・Renderer と、グローバル設定のうち Player に入る設定が直接参照する Shader）、
brg-sidecar、dependency / usepass / fallback（ShaderLab の宣言を辿ったもの）、runtime-lookup、extra。
元 ↔ Radial の対応は使わない。Player 側に元 ↔ Radial の切り替えは無いので、対応する Shader は残さない（変換の版の確認は、ビルドの前の準備 <code>OmniRadialBuildPreparation</code> の変換保証が行う）。

```csharp
public sealed class OmniBuildShaderClosure
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniBuildShaderClosure](Omni.Editor.Build.OmniBuildShaderClosure.md)

## プロパティ（Properties）

### <a id="Omni_Editor_Build_OmniBuildShaderClosure_KeepReasons"></a> KeepReasons

残す Shader の資産パス → 最初に当たった理由。

```csharp
public IReadOnlyDictionary<string, string> KeepReasons { get; }
```

#### 値（Property Value）

 [IReadOnlyDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlydictionary\-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Editor_Build_OmniBuildShaderClosure_SkippedAddPassShaders"></a> SkippedAddPassShaders

Terrain の層が少ないので残さなかった Shader（AddPassShader）の資産パス。

```csharp
public IReadOnlyCollection<string> SkippedAddPassShaders { get; }
```

#### 値（Property Value）

 [IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Editor_Build_OmniBuildShaderClosure_StripUnclassifiedHidden"></a> StripUnclassifiedHidden

どの理由にも当たらない <code>Hidden/</code> の Shader も外す設定か。

```csharp
public bool StripUnclassifiedHidden { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Build_OmniBuildShaderClosure_Warnings"></a> Warnings

Scene を開けない、宣言や実行時に探す Shader を解決できない、2D Renderer や Terrain の細部が無いので残さないなど、除外の判断についての注意。

```csharp
public IReadOnlyList<string> Warnings { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

## メソッド（Methods）

### <a id="Omni_Editor_Build_OmniBuildShaderClosure_Classify_UnityEngine_Shader_"></a> Classify\(Shader\)

この Shader をどう扱うか。

```csharp
public OmniBuildShaderClosure.Decision Classify(Shader shader)
```

#### 引数（Parameters）

`shader` Shader

#### 戻り値（Returns）

 [OmniBuildShaderClosure](Omni.Editor.Build.OmniBuildShaderClosure.md).[Decision](Omni.Editor.Build.OmniBuildShaderClosure.Decision.md)

### <a id="Omni_Editor_Build_OmniBuildShaderClosure_Compute_Omni_Editor_Build_OmniBuildShaderRequest_"></a> Compute\(OmniBuildShaderRequest\)

Scene・パイプライン・宣言から、残す Shader を計算します。Editor で読み取るだけで、資産は変えません。

```csharp
public static OmniBuildShaderClosure Compute(OmniBuildShaderRequest request)
```

#### 引数（Parameters）

`request` [OmniBuildShaderRequest](Omni.Editor.Build.OmniBuildShaderRequest.md)

#### 戻り値（Returns）

 [OmniBuildShaderClosure](Omni.Editor.Build.OmniBuildShaderClosure.md)
