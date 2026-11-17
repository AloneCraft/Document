# <a id="Omni_RadialTerrainVegetationBinding"></a> Class RadialTerrainVegetationBinding

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

元の地形・Prefab・Materialを変更せず、植生用の生成MaterialをSceneへ保持します。

```csharp
[ExecuteAlways]
[DisallowMultipleComponent]
[RequireComponent(typeof(Terrain))]
[AddComponentMenu("")]
public sealed class RadialTerrainVegetationBinding : MonoBehaviour
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[RadialTerrainVegetationBinding](Omni.RadialTerrainVegetationBinding.md)

## プロパティ（Properties）

### <a id="Omni_RadialTerrainVegetationBinding_Revision"></a> Revision

```csharp
public int Revision { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_RadialTerrainVegetationBinding_SourceData"></a> SourceData

```csharp
public TerrainData SourceData { get; }
```

#### 値（Property Value）

 TerrainData

## メソッド（Methods）

### <a id="Omni_RadialTerrainVegetationBinding_Configure_UnityEngine_TerrainData_Omni_RadialTerrainVegetationBinding_MaterialPair___UnityEngine_Material___Omni_RadialTerrainVegetationBinding_DetailMeshPair___"></a> Configure\(TerrainData, MaterialPair\[\], Material\[\], DetailMeshPair\[\]\)

```csharp
public void Configure(TerrainData source, RadialTerrainVegetationBinding.MaterialPair[] materials, Material[] details, RadialTerrainVegetationBinding.DetailMeshPair[] detailMeshes = null)
```

#### 引数（Parameters）

`source` TerrainData

`materials` [RadialTerrainVegetationBinding](Omni.RadialTerrainVegetationBinding.md).[MaterialPair](Omni.RadialTerrainVegetationBinding.MaterialPair.md)\[\]

`details` Material\[\]

`detailMeshes` [RadialTerrainVegetationBinding](Omni.RadialTerrainVegetationBinding.md).[DetailMeshPair](Omni.RadialTerrainVegetationBinding.DetailMeshPair.md)\[\]

### <a id="Omni_RadialTerrainVegetationBinding_GetDetailMaterial_System_Int32_"></a> GetDetailMaterial\(int\)

```csharp
public Material GetDetailMaterial(int prototypeIndex)
```

#### 引数（Parameters）

`prototypeIndex` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 Material

### <a id="Omni_RadialTerrainVegetationBinding_MarkDirty"></a> MarkDirty\(\)

```csharp
public void MarkDirty()
```

### <a id="Omni_RadialTerrainVegetationBinding_TryResolve_UnityEngine_Material_UnityEngine_Material__"></a> TryResolve\(Material, out Material\)

```csharp
public bool TryResolve(Material source, out Material radial)
```

#### 引数（Parameters）

`source` Material

`radial` Material

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
