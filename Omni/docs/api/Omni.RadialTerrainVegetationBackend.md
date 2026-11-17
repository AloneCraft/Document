# <a id="Omni_RadialTerrainVegetationBackend"></a> Class RadialTerrainVegetationBackend

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

TerrainDataを正本に保ち、非保存の植生描画（木・mesh detail）だけを組み立てます。
組み立てられない木のprototypeやdetailは、そのprototypeだけをFail Closedで外して診断へ記録し、
他の植生は描画します（1つの非対応素材で全植生が消えないようにするため）。

```csharp
public static class RadialTerrainVegetationBackend
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialTerrainVegetationBackend](Omni.RadialTerrainVegetationBackend.md)

## メソッド（Methods）

### <a id="Omni_RadialTerrainVegetationBackend_GetDiagnostics_UnityEngine_Terrain_"></a> GetDiagnostics\(Terrain\)

準備で外した木・detailの理由です（準備前または未対応のTerrainは空）。

```csharp
public static IReadOnlyList<string> GetDiagnostics(Terrain terrain)
```

#### 引数（Parameters）

`terrain` Terrain

#### 戻り値（Returns）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_RadialTerrainVegetationBackend_Release_UnityEngine_Terrain_"></a> Release\(Terrain\)

```csharp
public static void Release(Terrain terrain)
```

#### 引数（Parameters）

`terrain` Terrain

### <a id="Omni_RadialTerrainVegetationBackend_ReleaseAll"></a> ReleaseAll\(\)

```csharp
public static void ReleaseAll()
```

### <a id="Omni_RadialTerrainVegetationBackend_SetCameraVisibility_UnityEngine_Terrain_UnityEngine_Camera_System_Boolean_"></a> SetCameraVisibility\(Terrain, Camera, bool\)

```csharp
public static void SetCameraVisibility(Terrain terrain, Camera camera, bool requested)
```

#### 引数（Parameters）

`terrain` Terrain

`camera` Camera

`requested` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_RadialTerrainVegetationBackend_TryGetBillboardLocalBounds_UnityEngine_Renderer_UnityEngine_Bounds__"></a> TryGetBillboardLocalBounds\(Renderer, out Bounds\)

```csharp
public static bool TryGetBillboardLocalBounds(Renderer renderer, out Bounds bounds)
```

#### 引数（Parameters）

`renderer` Renderer

`bounds` Bounds

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_RadialTerrainVegetationBackend_TryGetPoseSource_UnityEngine_Renderer_UnityEngine_Transform__"></a> TryGetPoseSource\(Renderer, out Transform\)

```csharp
public static bool TryGetPoseSource(Renderer renderer, out Transform source)
```

#### 引数（Parameters）

`renderer` Renderer

`source` Transform

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_RadialTerrainVegetationBackend_TryPrepare_UnityEngine_Terrain_System_Collections_Generic_List_UnityEngine_MeshRenderer__System_String__"></a> TryPrepare\(Terrain, List<MeshRenderer\>, out string\)

```csharp
public static bool TryPrepare(Terrain terrain, List<MeshRenderer> destination, out string reason)
```

#### 引数（Parameters）

`terrain` Terrain

`destination` [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<MeshRenderer\>

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_RadialTerrainVegetationBackend_TryPrepareAll_UnityEngine_Terrain_System_Collections_Generic_List_UnityEngine_Renderer__System_String__"></a> TryPrepareAll\(Terrain, List<Renderer\>, out string\)

```csharp
public static bool TryPrepareAll(Terrain terrain, List<Renderer> destination, out string reason)
```

#### 引数（Parameters）

`terrain` Terrain

`destination` [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<Renderer\>

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
