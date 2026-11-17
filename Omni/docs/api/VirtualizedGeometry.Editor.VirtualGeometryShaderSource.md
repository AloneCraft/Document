# <a id="VirtualizedGeometry_Editor_VirtualGeometryShaderSource"></a> Class VirtualGeometryShaderSource

Namespace: [VirtualizedGeometry.Editor](VirtualizedGeometry.Editor.md)  
Assembly: Omni.VirtualGeometry.Editor.dll  

URPのShaderLabソースから、元の全passに「頂点入力だけをVGのbufferへ差し替えたpass」を加えたソースを作る。
fragment処理・keyword・Propertiesは元shaderのものをそのまま使うため、Materialの見た目は通常Meshと同じになる。
必須はUniversalPipelineのforward pass(UniversalForward/UniversalForwardOnly/LightModeなし)。同じSubShaderにDepthOnly・DepthNormals(無ければDepthNormalsOnly)・
ShadowCasterがあれば、それぞれもVG版にする(prepassと影にVGの面を描くため。pass名は<xref href="VirtualizedGeometry.VirtualGeometryMaterials" data-throw-if-not-resolved="false"></xref>)。
追加のpassを変換できないときは、そのpassだけ作らない(<xref href="VirtualizedGeometry.Editor.VirtualGeometryShaderConversion.Warnings" data-throw-if-not-resolved="false"></xref>)。Deferred専用・BRP・HDRP・tessellation/geometry stageは扱わない。

```csharp
public static class VirtualGeometryShaderSource
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryShaderSource](VirtualizedGeometry.Editor.VirtualGeometryShaderSource.md)

## フィールド（Fields）

### <a id="VirtualizedGeometry_Editor_VirtualGeometryShaderSource_PassName"></a> PassName

```csharp
public const string PassName = "VirtualGeometryForward"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualizedGeometry_Editor_VirtualGeometryShaderSource_ShaderPrefix"></a> ShaderPrefix

```csharp
public const string ShaderPrefix = "VirtualGeometry/"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## プロパティ（Properties）

### <a id="VirtualizedGeometry_Editor_VirtualGeometryShaderSource_VertexInputInclude"></a> VertexInputInclude

VG の頂点入力（VirtualGeometryVertexInput.hlsl）の include のパス。置き場所は配布の形（Assets 直下か、UPM の Packages/...）で変わるので、
importer が資産の GUID から求めて設定する（<xref href="VirtualizedGeometry.Editor.VirtualGeometryShaderImporter" data-throw-if-not-resolved="false"></xref>）。

```csharp
public static string VertexInputInclude { get; set; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="VirtualizedGeometry_Editor_VirtualGeometryShaderSource_Convert_System_String_System_String_System_Func_System_String_System_String__System_Boolean_"></a> Convert\(string, string, Func<string, string\>, bool\)

```csharp
public static VirtualGeometryShaderConversion Convert(string text, string sourceAssetPath, Func<string, string> resolvePhysical, bool indexedTerrain = false)
```

#### 引数（Parameters）

`text` [string](https://learn.microsoft.com/dotnet/api/system.string)

元のShaderLabソース(.shaderまたはShader Graphの生成コード)。

`sourceAssetPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

相対includeの基準になるasset path。生成コードではnull。

`resolvePhysical` [Func](https://learn.microsoft.com/dotnet/api/system.func\-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [string](https://learn.microsoft.com/dotnet/api/system.string)\>

"Assets/…"や"Packages/…"のasset pathを実ファイルのpathへ変換する。

`indexedTerrain` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [VirtualGeometryShaderConversion](VirtualizedGeometry.Editor.VirtualGeometryShaderConversion.md)
