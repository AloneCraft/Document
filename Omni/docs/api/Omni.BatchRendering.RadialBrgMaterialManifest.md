# <a id="Omni_BatchRendering_RadialBrgMaterialManifest"></a> Class RadialBrgMaterialManifest

Namespace: [Omni.BatchRendering](Omni.BatchRendering.md)  
Assembly: Omni.BatchRendering.Runtime.dll  

BRG material sidecarと依存Hashの生成Manifestです。

```csharp
public sealed class RadialBrgMaterialManifest : ScriptableObject
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
ScriptableObject ← 
[RadialBrgMaterialManifest](Omni.BatchRendering.RadialBrgMaterialManifest.md)

## フィールド（Fields）

### <a id="Omni_BatchRendering_RadialBrgMaterialManifest_ResourceName"></a> ResourceName

旧Resources資産の移行に使う名前です。PlayerへはScene manifestで渡します。

```csharp
public const string ResourceName = "RadialBrgMaterialManifest"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## プロパティ（Properties）

### <a id="Omni_BatchRendering_RadialBrgMaterialManifest_Entries"></a> Entries

Manifest内の全entryです。

```csharp
public IReadOnlyList<RadialBrgMaterialManifestEntry> Entries { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[RadialBrgMaterialManifestEntry](Omni.BatchRendering.RadialBrgMaterialManifestEntry.md)\>

## メソッド（Methods）

### <a id="Omni_BatchRendering_RadialBrgMaterialManifest_ContainsSourceShader_UnityEngine_Shader_"></a> ContainsSourceShader\(Shader\)

生成時に検証済みのSource Shaderかを返します。

```csharp
public bool ContainsSourceShader(Shader shader)
```

#### 引数（Parameters）

`shader` Shader

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_BatchRendering_RadialBrgMaterialManifest_IsDirectDraw_UnityEngine_Material_"></a> IsDirectDraw\(Material\)

正本または一意な実行時コピーの通常描画判定です。

```csharp
public bool IsDirectDraw(Material source)
```

#### 引数（Parameters）

`source` Material

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_BatchRendering_RadialBrgMaterialManifest_ReplaceEntries_System_Collections_Generic_List_Omni_BatchRendering_RadialBrgMaterialManifestEntry__"></a> ReplaceEntries\(List<RadialBrgMaterialManifestEntry\>\)

Editor生成器がentry一覧を原子的に置き換えます。

```csharp
public void ReplaceEntries(List<RadialBrgMaterialManifestEntry> entries)
```

#### 引数（Parameters）

`entries` [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[RadialBrgMaterialManifestEntry](Omni.BatchRendering.RadialBrgMaterialManifestEntry.md)\>

### <a id="Omni_BatchRendering_RadialBrgMaterialManifest_TryResolve_UnityEngine_Material_UnityEngine_Material__System_String__"></a> TryResolve\(Material, out Material, out string\)

元Materialに対応する有効sidecarを返します。

```csharp
public bool TryResolve(Material source, out Material sidecar, out string dependencyHash)
```

#### 引数（Parameters）

`source` Material

`sidecar` Material

`dependencyHash` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_BatchRendering_RadialBrgMaterialManifest_TryResolveAuthoringMaterial_UnityEngine_Material_UnityEngine_Material__"></a> TryResolveAuthoringMaterial\(Material, out Material\)

runtime cloneまたはManifestに直接登録されたMaterialから、Authoring正本を返します。
domain reload直後にRenderer側の元Material辞書が消えていても、
「Shader＋(Omni Runtime)を除いた名前」の一意なManifest契約を使えます。

```csharp
public bool TryResolveAuthoringMaterial(Material source, out Material authoring)
```

#### 引数（Parameters）

`source` Material

`authoring` Material

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
