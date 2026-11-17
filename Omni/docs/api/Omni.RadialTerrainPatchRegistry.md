# <a id="Omni_RadialTerrainPatchRegistry"></a> Class RadialTerrainPatchRegistry

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

TerrainDataを正本として、Radial描画に使う非保存MeshRenderer patchを管理します。

<p>
これはGalaxy/Saturn等のSceneへコンポーネントを保存しないRuntime registryです。Native Terrainを
隠すのは全patchを構築できた<xref href="Omni.RadialTerrainBackendState.Ready" data-throw-if-not-resolved="false"></xref>後だけで、構築失敗・
解除・Scene境界では必ず元の<xref href="UnityEngine.Terrain.drawHeightmap" data-throw-if-not-resolved="false"></xref>へ戻します。
</p>
<p>
写像しないCameraが描く間は、patchを壊さずに隠して元の表示へ戻します
（<xref href="Omni.RadialTerrainPatchRegistry.HideForCamera(UnityEngine.Terrain)" data-throw-if-not-resolved="false"></xref>／<xref href="Omni.RadialTerrainPatchRegistry.ShowAfterCamera(UnityEngine.Terrain)" data-throw-if-not-resolved="false"></xref>）。写像するCameraと交互に描いても作り直しません。
</p>
<p>
現段階は33×33相当の固定LOD 0を提供する安全な土台です。カメラ依存quadtree選択は、
呼び出し側がpatch一覧をカメラ別に利用できるようになってから追加します。
</p>

```csharp
public static class RadialTerrainPatchRegistry
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialTerrainPatchRegistry](Omni.RadialTerrainPatchRegistry.md)

## フィールド（Fields）

### <a id="Omni_RadialTerrainPatchRegistry_PatchQuadResolution"></a> PatchQuadResolution

1patch辺のquad数です。

```csharp
public const int PatchQuadResolution = 32
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_RadialTerrainPatchRegistry_PatchVertexResolution"></a> PatchVertexResolution

完全patch辺の頂点数です。

```csharp
public const int PatchVertexResolution = 33
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_RadialTerrainPatchRegistry_HideForCamera_UnityEngine_Terrain_"></a> HideForCamera\(Terrain\)

写像しないCameraが描く間だけ、patchを隠して元のNative Terrain表示へ戻します。patchは壊しません。

```csharp
public static bool HideForCamera(Terrain terrain)
```

#### 引数（Parameters）

`terrain` Terrain

対象Terrain。未登録・Ready以外・既に隠している場合は何もしません。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

隠した場合はtrueです。呼び出し側はそのCameraの描画の後で<xref href="Omni.RadialTerrainPatchRegistry.ShowAfterCamera(UnityEngine.Terrain)" data-throw-if-not-resolved="false"></xref>を呼びます。

### <a id="Omni_RadialTerrainPatchRegistry_MarkHeightmapDirty_UnityEngine_Terrain_UnityEngine_RectInt_"></a> MarkHeightmapDirty\(Terrain, RectInt\)

TerrainCallbacksから受け取ったHeightmap変更範囲をdirtyとして記録します。

```csharp
public static void MarkHeightmapDirty(Terrain terrain, RectInt changedSamples)
```

#### 引数（Parameters）

`terrain` Terrain

変更されたTerrainです。未登録の場合は何もしません。

`changedSamples` RectInt

変更されたheightmap sample矩形です。境界法線が参照する隣接sampleの変更も再構築対象にします。

### <a id="Omni_RadialTerrainPatchRegistry_MarkHolesDirty_UnityEngine_Terrain_UnityEngine_RectInt_"></a> MarkHolesDirty\(Terrain, RectInt\)

TerrainCallbacksから受け取った穴の変更範囲をdirtyとして記録します。

```csharp
public static void MarkHolesDirty(Terrain terrain, RectInt changedQuads)
```

#### 引数（Parameters）

`terrain` Terrain

変更されたTerrainです。未登録の場合は何もしません。

`changedQuads` RectInt

変更された穴のtexel矩形です。穴の1 texelはheightmapの1 quadに対応します。
空の矩形は範囲不明として全patchを再構築対象にします。

### <a id="Omni_RadialTerrainPatchRegistry_RebuildDirty_UnityEngine_Terrain_Omni_RadialTerrainPatchDiagnostics__"></a> RebuildDirty\(Terrain, out RadialTerrainPatchDiagnostics\)

Heightmap更新済みのpatchだけを再構築します。

```csharp
public static bool RebuildDirty(Terrain terrain, out RadialTerrainPatchDiagnostics diagnostics)
```

#### 引数（Parameters）

`terrain` Terrain

対象Terrain。未登録ならfalseです。

`diagnostics` [RadialTerrainPatchDiagnostics](Omni.RadialTerrainPatchDiagnostics.md)

再構築後またはfault後の状態です。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

Ready状態を維持できた場合はtrueです。

### <a id="Omni_RadialTerrainPatchRegistry_Release_UnityEngine_Terrain_"></a> Release\(Terrain\)

指定Terrainのpatch backendを破棄し、元のNative Terrain表示を戻します。

```csharp
public static void Release(Terrain terrain)
```

#### 引数（Parameters）

`terrain` Terrain

解除対象。nullや未登録なら何もしません。

### <a id="Omni_RadialTerrainPatchRegistry_ReleaseAll"></a> ReleaseAll\(\)

すべての非保存patchを破棄し、全TerrainのNative表示を復元します。
Scene unload、Assembly Reload、テスト後始末で呼びます。

```csharp
public static void ReleaseAll()
```

### <a id="Omni_RadialTerrainPatchRegistry_ShowAfterCamera_UnityEngine_Terrain_"></a> ShowAfterCamera\(Terrain\)

<xref href="Omni.RadialTerrainPatchRegistry.HideForCamera(UnityEngine.Terrain)" data-throw-if-not-resolved="false"></xref>で隠したpatchを表示へ戻し、Native Terrain surfaceを再び止めます。

```csharp
public static void ShowAfterCamera(Terrain terrain)
```

#### 引数（Parameters）

`terrain` Terrain

対象Terrain。未登録または隠していない場合は何もしません。

### <a id="Omni_RadialTerrainPatchRegistry_TryActivate_UnityEngine_Terrain_Omni_RadialTerrainPatchDiagnostics__"></a> TryActivate\(Terrain, out RadialTerrainPatchDiagnostics\)

指定Terrainの非保存patch backendを有効化します。

```csharp
public static bool TryActivate(Terrain terrain, out RadialTerrainPatchDiagnostics diagnostics)
```

#### 引数（Parameters）

`terrain` Terrain

TerrainDataを保持する元Terrainです。nullまたはTerrainData欠落時はfalseを返し、
Sceneやアセットを作成・保存しません。

`diagnostics` [RadialTerrainPatchDiagnostics](Omni.RadialTerrainPatchDiagnostics.md)

成功・失敗後の読み取り専用状態です。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

全patchがReadyになった場合だけtrueです。

### <a id="Omni_RadialTerrainPatchRegistry_TryGetAllPatchRenderers_UnityEngine_Terrain_System_Collections_Generic_List_UnityEngine_Renderer__"></a> TryGetAllPatchRenderers\(Terrain, List<Renderer\>\)

Mesh と Billboard の両方を描画対象として取得します。

```csharp
public static bool TryGetAllPatchRenderers(Terrain terrain, List<Renderer> destination)
```

#### 引数（Parameters）

`terrain` Terrain

`destination` [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<Renderer\>

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_RadialTerrainPatchRegistry_TryGetDiagnostics_UnityEngine_Terrain_Omni_RadialTerrainPatchDiagnostics__"></a> TryGetDiagnostics\(Terrain, out RadialTerrainPatchDiagnostics\)

指定Terrainの現在状態を返します。

```csharp
public static bool TryGetDiagnostics(Terrain terrain, out RadialTerrainPatchDiagnostics diagnostics)
```

#### 引数（Parameters）

`terrain` Terrain

照会対象のTerrainです。

`diagnostics` [RadialTerrainPatchDiagnostics](Omni.RadialTerrainPatchDiagnostics.md)

登録されている場合の診断値です。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

登録済みならtrueです。

### <a id="Omni_RadialTerrainPatchRegistry_TryGetPatchRenderers_UnityEngine_Terrain_System_Collections_Generic_List_UnityEngine_MeshRenderer__"></a> TryGetPatchRenderers\(Terrain, List<MeshRenderer\>\)

指定Terrainに紐付くpatch Rendererを末尾へ追加します。

```csharp
public static bool TryGetPatchRenderers(Terrain terrain, List<MeshRenderer> destination)
```

#### 引数（Parameters）

`terrain` Terrain

登録済みTerrainです。

`destination` [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<MeshRenderer\>

追加先リストです。nullの場合はfalseを返します。既存要素は消しません。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

Ready backendのpatchを少なくとも1件返せた場合はtrueです。
