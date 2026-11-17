# <a id="Omni_Converter_RadialSourceResolver"></a> Class RadialSourceResolver

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

生成マテリアル → 元マテリアルの逆引きです。「いつでも元に戻せる」の土台。

<p>
解決は 3 段で、<b>先勝ち・フォールスルー禁止</b>です。どれも駄目なら null を返し、
呼び出し側が理由を報告できるようにします（黙って別のものを返しません）。
</p>
<ol><li><b>マニフェストの GUID + localId</b> …… 正規経路。リネーム・移動に耐えます</li><li><b>マニフェストの GUID + 名前</b> …… DCC 側で作り直して localId が動いた場合</li><li><b>パス規則からの逆算</b> …… 逆引き未記録（v1 マニフェスト）のエントリの救済のみ</li></ol>
<p>
3 は<b>推測</b>であり、これだけに頼っていたのが従来の弱点でした。
バックフィル（<code>Backfill Source Ids</code>）を一度流せば
ほとんどのエントリが 1 で解決するようになります。
</p>

```csharp
public static class RadialSourceResolver
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialSourceResolver](Omni.Converter.RadialSourceResolver.md)

## メソッド（Methods）

### <a id="Omni_Converter_RadialSourceResolver_BackfillSourceIds"></a> BackfillSourceIds\(\)

```csharp
public static RadialSourceResolver.BackfillResult BackfillSourceIds()
```

#### 戻り値（Returns）

 [RadialSourceResolver](Omni.Converter.RadialSourceResolver.md).[BackfillResult](Omni.Converter.RadialSourceResolver.BackfillResult.md)

### <a id="Omni_Converter_RadialSourceResolver_IsGeneratedPath_System_String_"></a> IsGeneratedPath\(string\)

このパスが Omni の生成物かどうか。

```csharp
public static bool IsGeneratedPath(string assetPath)
```

#### 引数（Parameters）

`assetPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_RadialSourceResolver_IsRadialInjected_UnityEngine_Material_"></a> IsRadialInjected\(Material\)

マテリアルが実際に Radial ワープ注入済みのシェーダーを参照しているかどうかを返します。

```csharp
public static bool IsRadialInjected(Material material)
```

#### 引数（Parameters）

`material` Material

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 補足（Remarks）

「Omni版のマテリアルファイルが存在する」ことと「実際にワープする」ことは別問題です。
<xref href="Omni.Converter.RadialMaterialConverter.ConvertMaterial(UnityEngine.Material)" data-throw-if-not-resolved="false"></xref> はシェーダー解決に失敗しても
元シェーダーを指したまま成功扱いでマテリアルを返すため（当時ログのみ）、生成物として
存在するのに未ワープのままのマテリアルが実在します（2026-09、CameraCombinationVerification
の`*Metallic`系7本で確認）。自動生成Shaderは生成物パスで判定します。同梱カタログの
Shader（ShaderGraphを含む）は製造工程で検証済みなので、カタログの実参照で判定します。
Omni自身が所有する手書きShaderは、<code>OmniRadial=True</code>タグ、Radial Transform property、
対応Shaderの3点が揃う場合だけ同じ契約を満たすものとして認めます。

### <a id="Omni_Converter_RadialSourceResolver_ProbeSourceByPathRule_System_String_System_String_System_String__"></a> ProbeSourceByPathRule\(string, string, out string\)

パス規則で元アセットの有無を判定します。<xref href="Omni.Converter.RadialSourceResolver.ResolveByPathRule(System.String%2cSystem.String)" data-throw-if-not-resolved="false"></xref> と違い、
「元が無いと言い切れる」場合と「判定できない」場合を区別します。
元が消えた生成物を削除してよいかの判定に使うため、迷う場合は必ず
<xref href="Omni.Converter.RadialSourceResolver.PathRuleSourceProbe.Unverifiable" data-throw-if-not-resolved="false"></xref> を返します。

```csharp
public static RadialSourceResolver.PathRuleSourceProbe ProbeSourceByPathRule(string generatedPath, string materialName, out string sourcePath)
```

#### 引数（Parameters）

`generatedPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`materialName` [string](https://learn.microsoft.com/dotnet/api/system.string)

Materialの名前。Shaderなどでは null。

`sourcePath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [RadialSourceResolver](Omni.Converter.RadialSourceResolver.md).[PathRuleSourceProbe](Omni.Converter.RadialSourceResolver.PathRuleSourceProbe.md)

### <a id="Omni_Converter_RadialSourceResolver_ResolveByPathRule_System_String_System_String_"></a> ResolveByPathRule\(string, string\)

パス命名規則から元アセットのパスを逆算し、マテリアルを読み込みます。

<p>
旧実装はコンテナの拡張子を <code>.fbx</code> 決め打ちにしていましたが、実際には
<code>.vfx</code> / <code>.ttf</code> / <code>.asset</code> / <code>.shadergraph</code> のコンテナが存在します。
ここでは拡張子を推測せず、親フォルダを走査して名前が一致するファイルを探します。
</p>

```csharp
public static Material ResolveByPathRule(string generatedPath, string materialName)
```

#### 引数（Parameters）

`generatedPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`materialName` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 Material

### <a id="Omni_Converter_RadialSourceResolver_ResolveGeneratedAssetSourcePath_System_String_"></a> ResolveGeneratedAssetSourcePath\(string\)

生成物パスから元アセットの<b>パス</b>を解決します（型を問わず、実体のロードは
存在確認のためだけに行います）。<xref href="Omni.Converter.RadialSourceResolver.ResolveByPathRule(System.String%2cSystem.String)" data-throw-if-not-resolved="false"></xref> と違い、コンテナ埋め込み
（<code>*_Materials</code>）は扱いません — シェーダー / ShaderGraph はコンテナへ埋め込まれないためです。

```csharp
public static string ResolveGeneratedAssetSourcePath(string generatedPath)
```

#### 引数（Parameters）

`generatedPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 補足（Remarks）

マニフェストは <code>.shader</code> / <code>.shadergraph</code> のエントリを持たない
（2026-09時点で実測0件）ため、シェーダーの逆引きは現状これが唯一の経路です。

### <a id="Omni_Converter_RadialSourceResolver_ResolveSourceMaterial_UnityEngine_Material_System_String__"></a> ResolveSourceMaterial\(Material, out string\)

生成マテリアルから元マテリアルを解決します。解決できなければ null。

```csharp
public static Material ResolveSourceMaterial(Material generated, out string reason)
```

#### 引数（Parameters）

`generated` Material

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

解決できなかった理由（成功時は null）。

#### 戻り値（Returns）

 Material

### <a id="Omni_Converter_RadialSourceResolver_TryGetRestorableSourcePath_System_String_System_String__System_String__"></a> TryGetRestorableSourcePath\(string, out string, out string\)

生成物パスから、<b>復元先として書き込んでよい</b>元アセットのパスを求めます。

```csharp
public static bool TryGetRestorableSourcePath(string generatedPath, out string sourcePath, out string reason)
```

#### 引数（Parameters）

`generatedPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

生成マテリアルのパス。

`sourcePath` [string](https://learn.microsoft.com/dotnet/api/system.string)

復元先パス。失敗時は null。

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

復元対象にできない理由。成功時は null。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

復元先を決められた場合は true。

#### 補足（Remarks）

<xref href="Omni.Converter.RadialSourceResolver.ResolveByPathRule(System.String%2cSystem.String)" data-throw-if-not-resolved="false"></xref> は「既にある元アセットを探す」ためのものなので、
元が消えている場合は null しか返せません。こちらは「どこへ作り直せばよいか」を返します。

<p>
復元できるのは <code>Generated/Project/</code> 配下の<b>独立した .mat</b> だけです。
<code>Packages/</code> は書き込めず、<code>*_Materials/</code> は .fbx などのコンテナへ埋め込まれた
サブアセットなので、外から新規作成しても元の参照は復元されません。
</p>
