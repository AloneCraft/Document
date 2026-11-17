# <a id="VirtualizedGeometry_Editor_VirtualGeometryShaderImporter"></a> Class VirtualGeometryShaderImporter

Namespace: [VirtualizedGeometry.Editor](VirtualizedGeometry.Editor.md)  
Assembly: Omni.VirtualGeometry.Editor.dll  

Virtual Geometry Shader(.vgshader)。参照先shader(.shader / Shader Graph)から、元の全passとVG用forward passを持つShaderを生成する。
Materialのshaderにこれを選ぶと、同じMaterialで通常Mesh・Proxy・影とVG描画の両方に使える。参照先を編集すると再生成される。

```csharp
[ScriptedImporter(4, "vgshader")]
public sealed class VirtualGeometryShaderImporter : ScriptedImporter
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
AssetImporter ← 
ScriptedImporter ← 
[VirtualGeometryShaderImporter](VirtualizedGeometry.Editor.VirtualGeometryShaderImporter.md)

## プロパティ（Properties）

### <a id="VirtualizedGeometry_Editor_VirtualGeometryShaderImporter_IndexedTerrain"></a> IndexedTerrain

```csharp
public bool IndexedTerrain { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_Editor_VirtualGeometryShaderImporter_Source"></a> Source

```csharp
public Shader Source { get; set; }
```

#### 値（Property Value）

 Shader

## メソッド（Methods）

### <a id="VirtualizedGeometry_Editor_VirtualGeometryShaderImporter_Create_UnityEngine_Shader_"></a> Create\(Shader\)

選択shaderを参照する.vgshaderを同じフォルダに作る。MaterialのshaderにはVirtualGeometry/&lt;元の名前&gt;を選ぶ。

```csharp
public static string Create(Shader shader)
```

#### 引数（Parameters）

`shader` Shader

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualizedGeometry_Editor_VirtualGeometryShaderImporter_OnImportAsset_UnityEditor_AssetImporters_AssetImportContext_"></a> OnImportAsset\(AssetImportContext\)

<p>This method must be overriden by the derived class and is called by the Asset pipeline to import files.</p>

```csharp
public override void OnImportAsset(AssetImportContext ctx)
```

#### 引数（Parameters）

`ctx` AssetImportContext

This argument contains all the contextual information needed to process the import event and is also used by the custom importer to store the resulting Unity Asset.
