# <a id="Omni_Converter_RadialMaterialConverter"></a> Class RadialMaterialConverter

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

シーン内のマテリアル・シェーダーを走査し、Radial対応版へ一括変換する Editor ツールです。

<p>
変換後アセットは <code>Assets/Radial/</code> 配下に集約されます。
標準URP Shaderは同梱カタログの検証済みShaderへ差し替えます。
ユーザーShaderGraphは <code>.shadergraph</code> を複製し、
<code>_RadialGlobal_*</code> プロパティを注入します。
</p>

```csharp
public static class RadialMaterialConverter
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialMaterialConverter](Omni.Converter.RadialMaterialConverter.md)

## メソッド（Methods）

### <a id="Omni_Converter_RadialMaterialConverter_ConvertMaterial_UnityEngine_Material_"></a> ConvertMaterial\(Material\)

マテリアルを複製し、シェーダーを Radial 版に差し替えます。

<p>
出力先は <xref href="Omni.Converter.RadialMaterialConverter.GetOmniOutputPath(System.String)" data-throw-if-not-resolved="false"></xref> のルールに従います。
Packages 内のマテリアルは <code>new Material(source)</code> で新規作成、
Assets 内のマテリアルは <code>AssetDatabase.CopyAsset</code> で複製します。
</p>

```csharp
public static Material ConvertMaterial(Material material)
```

#### 引数（Parameters）

`material` Material

元マテリアル。

#### 戻り値（Returns）

 Material

複製したマテリアル。失敗時、または <code>Assets/Omni/</code> 配下の場合は null。

### <a id="Omni_Converter_RadialMaterialConverter_ConvertShaderGraph_System_String_"></a> ConvertShaderGraph\(string\)

```csharp
public static string ConvertShaderGraph(string shaderGraphPath)
```

#### 引数（Parameters）

`shaderGraphPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_RadialMaterialConverter_GetOmniMaterialOutputPath_UnityEngine_Material_"></a> GetOmniMaterialOutputPath\(Material\)

Returns the generated material path for a material asset or an embedded model material.
Embedded materials cannot be addressed by copying the model asset, so each one is
externalized as an independent generated .mat while retaining its source properties.

```csharp
public static string GetOmniMaterialOutputPath(Material material)
```

#### 引数（Parameters）

`material` Material

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_RadialMaterialConverter_GetOmniOutputPath_System_String_"></a> GetOmniOutputPath\(string\)

ソースパスから Omni 出力先パスを生成します。

<p>
<code>Packages/X</code>（Shader・Shader Graph を含む全て） → <code>Assets/Radial/Packages/X</code><br />
<code>Assets/X.mat</code> → <code>Assets/Radial/Project/X.mat</code><br />
<code>Assets/X.shader</code> / <code>.shadergraph</code> → <code>Assets/Radial/User/X.*</code>
</p>
<p>
出力は元の根を写します（Packages 由来は Packages、Assets 由来は User／Project）。
以前は Packages 由来の Shader も <code>User/&lt;パッケージ名&gt;/…</code> へ置いていましたが、
User がパッケージ由来を含むと、元が Assets か Packages かをパス名の「.」の有無から推測するしかなくなるため改めました
（旧配置の移行は <xref href="Omni.Converter.OmniRadialOutputMigration" data-throw-if-not-resolved="false"></xref>）。
</p>

```csharp
public static string GetOmniOutputPath(string srcPath)
```

#### 引数（Parameters）

`srcPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_RadialMaterialConverter_IsExternallyOwnedAsset_System_String_"></a> IsExternallyOwnedAsset\(string\)

検証・サンプルなど、製品の自動生成物へ取り込まない外部所有assetかを返します。

```csharp
public static bool IsExternallyOwnedAsset(string assetPath)
```

#### 引数（Parameters）

`assetPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_RadialMaterialConverter_RegisterExternalAssetOwnership_System_Func_System_String_System_Boolean__"></a> RegisterExternalAssetOwnership\(Func<string, bool\>\)

検証やサンプルが自ら生成物を所有するasset pathを登録します。
登録されたassetは製品用Material／GUID manifestへ取り込みません。

```csharp
public static void RegisterExternalAssetOwnership(Func<string, bool> ownership)
```

#### 引数（Parameters）

`ownership` [Func](https://learn.microsoft.com/dotnet/api/system.func\-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [bool](https://learn.microsoft.com/dotnet/api/system.boolean)\>

### <a id="Omni_Converter_RadialMaterialConverter_SaveGuidManifest"></a> SaveGuidManifest\(\)

GUID安定化マニフェスト（<xref href="Omni.Converter.OmniGuidManifest" data-throw-if-not-resolved="false"></xref>）への変更をディスクへ保存します。
<xref href="Omni.Converter.RadialMaterialConverter.ConvertMaterial(UnityEngine.Material)" data-throw-if-not-resolved="false"></xref> を連続呼び出しするバッチ処理の最後に1回呼ぶこと
（1件ごとの保存は遅いため、内部では記録のみ・保存はまとめて行う設計）。

```csharp
public static void SaveGuidManifest()
```

### <a id="Omni_Converter_RadialMaterialConverter_ScanMaterials_System_String_"></a> ScanMaterials\(string\)

指定フォルダ配下の全マテリアルを列挙します（<code>Assets/Omni/</code> 配下は除外）。

```csharp
public static List<Material> ScanMaterials(string folder)
```

#### 引数（Parameters）

`folder` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<Material\>

### <a id="Omni_Converter_RadialMaterialConverter_ScanShaderGraphs_System_String_"></a> ScanShaderGraphs\(string\)

指定フォルダ配下の全 ShaderGraph アセットを列挙します（<code>Assets/Omni/</code> 配下は除外）。

```csharp
public static List<string> ScanShaderGraphs(string folder)
```

#### 引数（Parameters）

`folder` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Converter_RadialMaterialConverter_ShouldSkip_System_String_"></a> ShouldSkip\(string\)

<code>Assets/Radial/</code> 配下と外部所有assetは変換対象外です。

```csharp
public static bool ShouldSkip(string assetPath)
```

#### 引数（Parameters）

`assetPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
