# <a id="Omni_BatchRendering_RadialBrgMaterialManifestEntry"></a> Class RadialBrgMaterialManifestEntry

Namespace: [Omni.BatchRendering](Omni.BatchRendering.md)  
Assembly: Omni.BatchRendering.Runtime.dll  

元Materialと生成BRG sidecarの対応です。

```csharp
[Serializable]
public sealed class RadialBrgMaterialManifestEntry
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialBrgMaterialManifestEntry](Omni.BatchRendering.RadialBrgMaterialManifestEntry.md)

## プロパティ（Properties）

### <a id="Omni_BatchRendering_RadialBrgMaterialManifestEntry_DependencyHash"></a> DependencyHash

元Shader/Material依存関係のHashです。

```csharp
public string DependencyHash { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_BatchRendering_RadialBrgMaterialManifestEntry_DirectDraw"></a> DirectDraw

BRGコンパイル不可のため通常のRadial描画へ残します。

```csharp
public bool DirectDraw { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_BatchRendering_RadialBrgMaterialManifestEntry_DirectDrawReason"></a> DirectDrawReason

通常描画へ残すコンパイラ診断です。

```csharp
public string DirectDrawReason { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_BatchRendering_RadialBrgMaterialManifestEntry_SidecarMaterial"></a> SidecarMaterial

DOTS Instancingを有効化した生成Materialです。

```csharp
public Material SidecarMaterial { get; }
```

#### 値（Property Value）

 Material

### <a id="Omni_BatchRendering_RadialBrgMaterialManifestEntry_SourceMaterial"></a> SourceMaterial

Authoring正本のMaterialです。

```csharp
public Material SourceMaterial { get; }
```

#### 値（Property Value）

 Material

## メソッド（Methods）

### <a id="Omni_BatchRendering_RadialBrgMaterialManifestEntry_Initialize_UnityEngine_Material_UnityEngine_Material_System_String_System_Boolean_System_String_"></a> Initialize\(Material, Material, string, bool, string\)

Editor生成器だけがentryを初期化します。

```csharp
public void Initialize(Material source, Material sidecar, string dependencyHash, bool directDraw = false, string directDrawReason = "")
```

#### 引数（Parameters）

`source` Material

`sidecar` Material

`dependencyHash` [string](https://learn.microsoft.com/dotnet/api/system.string)

`directDraw` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`directDrawReason` [string](https://learn.microsoft.com/dotnet/api/system.string)
