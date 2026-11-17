# <a id="Omni_Editor_Manager_OmniMaterialGenerator"></a> Class OmniMaterialGenerator

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

Omni マテリアルの生成を管理します。<xref href="Omni.Converter.RadialMaterialConverter" data-throw-if-not-resolved="false"></xref> のラッパーです。

```csharp
[InitializeOnLoad]
public static class OmniMaterialGenerator
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniMaterialGenerator](Omni.Editor.Manager.OmniMaterialGenerator.md)

## メソッド（Methods）

### <a id="Omni_Editor_Manager_OmniMaterialGenerator_Exists_UnityEngine_Material_"></a> Exists\(Material\)

既に Omni 版が存在するかどうかを返します。

```csharp
public static bool Exists(Material source)
```

#### 引数（Parameters）

`source` Material

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_OmniMaterialGenerator_Generate_UnityEngine_Material_"></a> Generate\(Material\)

指定された元マテリアルから Omni 版を生成します。

```csharp
public static Material Generate(Material source)
```

#### 引数（Parameters）

`source` Material

#### 戻り値（Returns）

 Material

生成されたマテリアル。失敗またはスキップ時は null。

### <a id="Omni_Editor_Manager_OmniMaterialGenerator_Regenerate_UnityEngine_Material_"></a> Regenerate\(Material\)

既存の Omni 版を削除して再生成します。

```csharp
public static Material Regenerate(Material source)
```

#### 引数（Parameters）

`source` Material

#### 戻り値（Returns）

 Material
