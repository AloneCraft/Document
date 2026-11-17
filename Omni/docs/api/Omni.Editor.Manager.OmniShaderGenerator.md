# <a id="Omni_Editor_Manager_OmniShaderGenerator"></a> Class OmniShaderGenerator

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

元シェーダーを<b>そのまま複製し、テキストで最小限だけパッチ</b>して Radial 対応版を生成します。

<p>
さらに昔の実装は HLSL ブロックを正規表現で抽出して別ファイルへ出し、シェーダー本体を
組み立て直していました。その方式は <code>Blend [_SrcBlend][_DstBlend]</code> のような SubShader
レベルのレンダーステート、Pass の <code>Name</code> / <code>LightMode</code> タグ、相対 include を
落としてしまい、生成物が壊れます。複製＋パッチなら原文の構造がそのまま残るため、
これらの取りこぼしが原理的に発生しません。
</p>
<p>
パッチの当て方は<b>正規表現から構文解析へ移行済み</b>です。ShaderLab の構造は
<xref href="Omni.Editor.Manager.ShaderLab.ShaderLabParser" data-throw-if-not-resolved="false"></xref> が、頂点フックの挿入位置は
<xref href="Omni.Editor.Manager.Hlsl.HlslIncludeGraph" data-throw-if-not-resolved="false"></xref> が決めます。
なぜ HLSL パーサーを導入しないのか、その前提が崩れる条件、対応できないシェーダーが
出たときの手順は <xref href="Omni.Editor.Manager.Radial.OmniShaderPatcher" data-throw-if-not-resolved="false"></xref> の冒頭コメントにまとめてあります。
<b>ここに正規表現を足して個別対応しないでください。</b>
</p>

```csharp
public static class OmniShaderGenerator
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniShaderGenerator](Omni.Editor.Manager.OmniShaderGenerator.md)

## フィールド（Fields）

### <a id="Omni_Editor_Manager_OmniShaderGenerator_ScreenSpaceShadowsShaderName"></a> ScreenSpaceShadowsShaderName

```csharp
public const string ScreenSpaceShadowsShaderName = "Hidden/Omni/Radial Screen Space Shadows"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_OmniShaderGenerator_ScreenSpaceShadowsShaderSourcePath"></a> ScreenSpaceShadowsShaderSourcePath

```csharp
public const string ScreenSpaceShadowsShaderSourcePath = "Packages/com.unity.render-pipelines.universal/Shaders/Utils/ScreenSpaceShadows.shader"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_OmniShaderGenerator_SsaoShaderName"></a> SsaoShaderName

```csharp
public const string SsaoShaderName = "Hidden/Omni/Radial Screen Space Ambient Occlusion"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_OmniShaderGenerator_SsaoShaderSourcePath"></a> SsaoShaderSourcePath

```csharp
public const string SsaoShaderSourcePath = "Packages/com.unity.render-pipelines.universal/Shaders/Utils/ScreenSpaceAmbientOcclusion.shader"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## プロパティ（Properties）

### <a id="Omni_Editor_Manager_OmniShaderGenerator_ScreenSpaceShadowsShaderOutputPath"></a> ScreenSpaceShadowsShaderOutputPath

```csharp
public static string ScreenSpaceShadowsShaderOutputPath { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_OmniShaderGenerator_SsaoHlslOutputPath"></a> SsaoHlslOutputPath

```csharp
public static string SsaoHlslOutputPath { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_OmniShaderGenerator_SsaoShaderOutputPath"></a> SsaoShaderOutputPath

```csharp
public static string SsaoShaderOutputPath { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Editor_Manager_OmniShaderGenerator_Generate_System_String_"></a> Generate\(string\)

元Shaderの対数版を生成し、生成先のパスを返します（変換できなければnull）。保証表の対象の元は、判定を記録する門
（<xref href="Omni.Converter.Guarantees.OmniConversionGuarantee.RunGuarded(System.String%2cSystem.Func%7bSystem.String%2cSystem.String%7d)" data-throw-if-not-resolved="false"></xref>）を通します。自作Shaderはそのまま変換します。

```csharp
public static string Generate(string shaderPath)
```

#### 引数（Parameters）

`shaderPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_OmniShaderGenerator_GenerateScreenSpaceShadows"></a> GenerateScreenSpaceShadows\(\)

URP ScreenSpaceShadowsだけをRadial対応版へ複製して、利用者の環境へ生成します。元のShaderは深度バッファから
ワールド位置を復元して物理座標のシャドウマップを引きますが、Radialの深度は歪めた位置の深度なので影が消えます。
復元の1行だけを<code>RadialScreenSpaceShadows.hlsl</code>の関数へ置き換えます（汎用patcherは通さないので、
Pickingやobject vertex hookは注入しません）。URPの原本の形が変わったときは、部分適用せずFail Closedします。
呼ばれるのは、対数への切替で<xref href="Omni.Editor.Build.OmniScreenSpaceShadowsAdapter" data-throw-if-not-resolved="false"></xref>が接続するときだけです。

```csharp
public static string GenerateScreenSpaceShadows()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_OmniShaderGenerator_GenerateSsao"></a> GenerateSsao\(\)

URP SSAOだけをfullscreen専用のRadial sidecarへ接続して、利用者の環境へ生成します。
汎用patcherを通さないため、Pickingやobject vertex hookは注入しません。
呼ばれるのは、対数への切替で<xref href="Omni.Editor.Build.OmniSsaoResourceAdapter" data-throw-if-not-resolved="false"></xref>が接続するときだけです。

```csharp
public static string GenerateSsao()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_OmniShaderGenerator_IsGeneratedShaderStale_System_String_System_String__"></a> IsGeneratedShaderStale\(string, out string\)

ディスク上の生成シェーダーが、<b>現在の</b>パッチャの出力と食い違っていないかを返します。

```csharp
public static bool IsGeneratedShaderStale(string shaderPath, out string reason)
```

#### 引数（Parameters）

`shaderPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

元シェーダーの論理パス（<code>.shader</code>）。

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

陳腐化の理由（人間向け）。最新なら null。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

作り直しが必要なら true。

#### 補足（Remarks）

<p>
生成物は <code>Assets/Radial/</code>（gitignore 対象のローカル生成物）にあり、
パッチャや注入先 HLSL を改良しても<b>自動では作り直されません</b>。
2026-08 の「対数表示オブジェクトがクリックで選択できない」不具合は、
<code>ScenePickingPass</code> の合成を実装したのに生成物が古いまま残っていたことが原因で、
症状だけを見て3回別の原因を疑うという回り道をしました。そのときの恒久対策がこれです。
</p>
<p>
判定はバージョン印の埋め込みではなく<b>パッチャを実際に走らせて全文比較する</b>方式です。
印を上げ忘れるというヒューマンエラーが上記バグの本質だったため、記録に頼らず
常に真の答えが出る形にしています。比較は <xref href="Omni.Editor.Manager.OmniShaderGenerator.WriteGeneratedText(System.String%2cSystem.String)" data-throw-if-not-resolved="false"></xref> と同じ
<xref href="Omni.Editor.Manager.OmniShaderGenerator.NormalizeLineEndings(System.String)" data-throw-if-not-resolved="false"></xref> ＋ 完全一致で、書き込み判定と食い違いません。
</p>
<p>
<code>.shadergraph</code> は対象外です（<xref href="Omni.Editor.Manager.OmniShaderGenerator.CopyShaderGraph(System.String%2cSystem.String)" data-throw-if-not-resolved="false"></xref> が毎回ファイルを
上書きコピーするため陳腐化しません）。呼び出し側はソース1本ぶんの再パッチを行うので、
数百本を一度に問い合わせる用途には向きません。
</p>

### <a id="Omni_Editor_Manager_OmniShaderGenerator_IsHiddenShader_System_String_"></a> IsHiddenShader\(string\)

宣言名がHidden/かを返す。生成の適格性はShouldSkipHiddenShaderが構文と閉包で判定する。

```csharp
public static bool IsHiddenShader(string shaderPath)
```

#### 引数（Parameters）

`shaderPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_OmniShaderGenerator_ShouldSkipHiddenShader_System_String_"></a> ShouldSkipHiddenShader\(string\)

内部用Hidden Shaderを生成しない境界です。利用者AssetsのShaderは、既存の構文解析と
include閉包でURPのobject passへの注入を実証できる場合だけ通常の生成へ渡します。
Packageの内部Shaderと、object注入の無いfullscreen/utilityは従来どおり除外します。

```csharp
public static bool ShouldSkipHiddenShader(string shaderPath)
```

#### 引数（Parameters）

`shaderPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
