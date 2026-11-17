# <a id="VirtualizedGeometry_VirtualGeometryClusterSource"></a> Class VirtualGeometryClusterSource

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

実行時に Cell(slot)の頂点を作って持つ供給元の基底(球など。頂点が Cell ごとに違う地形)。CPU uploadまたは所有権を持つGPU生成で、pool の頂点 buffer(32 B の頂点を slot ごとに並べる)と、
cluster の bounds の表(layoutの格子と4辺に対応する球をslotごとに並べる)へ書く。描画は、派生クラスがメッシュ版 VG の描画(<xref href="VirtualizedGeometry.VirtualGeometryRenderFeature" data-throw-if-not-resolved="false"></xref>)へ
渡す instance で行う(階層・cull・選択は共通の単位格子の page、頂点と bounds は pool から)。
slot の頂点は frame ごとに 1 回(beginContextRendering)、予算の範囲で生成する。生成済み(ready)の slot だけを描く。

```csharp
[ExecuteAlways]
public abstract class VirtualGeometryClusterSource : MonoBehaviour
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[VirtualGeometryClusterSource](VirtualizedGeometry.VirtualGeometryClusterSource.md)

#### 派生した型（Derived）

[PlanetLayerSource](VirtualGeometry.World.PlanetLayerSource.md)

## プロパティ（Properties）

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_DeferredGenerationLeases"></a> DeferredGenerationLeases

```csharp
protected PlanetGpuGenerationLeases DeferredGenerationLeases { get; }
```

#### 値（Property Value）

 [PlanetGpuGenerationLeases](VirtualGeometry.World.PlanetGpuGenerationLeases.md)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_EnableFrustumCulling"></a> EnableFrustumCulling

```csharp
public bool EnableFrustumCulling { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_EnableOcclusionCulling"></a> EnableOcclusionCulling

```csharp
public bool EnableOcclusionCulling { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_ExactTerrainStorageCapacity"></a> ExactTerrainStorageCapacity

```csharp
protected virtual int ExactTerrainStorageCapacity { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_FreeSlots"></a> FreeSlots

空いているslot数。poolがまだ無いときは0。

```csharp
public int FreeSlots { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_GenerationBudget"></a> GenerationBudget

```csharp
public int GenerationBudget { get; set; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_LastError"></a> LastError

直近の生成・描画で起きた設定エラー。無ければnull。

```csharp
public string LastError { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_Layout"></a> Layout

```csharp
protected VirtualGeometryGridLayout Layout { get; }
```

#### 値（Property Value）

 [VirtualGeometryGridLayout](VirtualizedGeometry.VirtualGeometryGridLayout.md)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_Material"></a> Material

```csharp
public Material Material { get; set; }
```

#### 値（Property Value）

 Material

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_PackedStorageReason"></a> PackedStorageReason

```csharp
public string PackedStorageReason { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_PackedVertexStorage"></a> PackedVertexStorage

```csharp
protected PlanetTerrainVertexPool PackedVertexStorage { get; }
```

#### 値（Property Value）

 [PlanetTerrainVertexPool](VirtualGeometry.World.PlanetTerrainVertexPool.md)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_PackedVertexStorageActive"></a> PackedVertexStorageActive

```csharp
public bool PackedVertexStorageActive { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_PendingGeneration"></a> PendingGeneration

生成を待っているslot数。

```csharp
public int PendingGeneration { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_PoolCapacity"></a> PoolCapacity

```csharp
public int PoolCapacity { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_TerrainExactCpuBytes"></a> TerrainExactCpuBytes

```csharp
public long TerrainExactCpuBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_TerrainExactSlotsUsed"></a> TerrainExactSlotsUsed

```csharp
public int TerrainExactSlotsUsed { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_TerrainVertexStorageBytes"></a> TerrainVertexStorageBytes

```csharp
public long TerrainVertexStorageBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_UsePackedTerrainStorage"></a> UsePackedTerrainStorage

```csharp
protected virtual bool UsePackedTerrainStorage { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_CompleteDeferredGeneration_VirtualGeometry_World_PlanetGpuGenerationLeases_VirtualGeometry_World_PlanetGpuGenerationLease__VirtualGeometry_World_PlanetGpuGenerationResult__System_Boolean_"></a> CompleteDeferredGeneration\(PlanetGpuGenerationLeases, in PlanetGpuGenerationLease, in PlanetGpuGenerationResult, bool\)

ownerはdispatch時のpool。GPU完了が確定したcallbackからのみ呼ぶ。古いpoolも必ず自身のleaseを完了する。

```csharp
protected PlanetGpuGenerationCompletion CompleteDeferredGeneration(PlanetGpuGenerationLeases owner, in PlanetGpuGenerationLease lease, in PlanetGpuGenerationResult result, bool readbackFailed = false)
```

#### 引数（Parameters）

`owner` [PlanetGpuGenerationLeases](VirtualGeometry.World.PlanetGpuGenerationLeases.md)

`lease` [PlanetGpuGenerationLease](VirtualGeometry.World.PlanetGpuGenerationLease.md)

`result` [PlanetGpuGenerationResult](VirtualGeometry.World.PlanetGpuGenerationResult.md)

`readbackFailed` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [PlanetGpuGenerationCompletion](VirtualGeometry.World.PlanetGpuGenerationCompletion.md)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_CpuPromotionRequired_System_Int32_"></a> CpuPromotionRequired\(int\)

```csharp
protected bool CpuPromotionRequired(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_CreateLayout"></a> CreateLayout\(\)

全slotが使うgridとclusterの配置。poolを作るときに1回だけ読む。

```csharp
protected abstract VirtualGeometryGridLayout CreateLayout()
```

#### 戻り値（Returns）

 [VirtualGeometryGridLayout](VirtualizedGeometry.VirtualGeometryGridLayout.md)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_GenerateSlots_System_Collections_Generic_IReadOnlyList_System_Int32__"></a> GenerateSlots\(IReadOnlyList<int\>\)

生成を予約したslotを、<xref href="VirtualizedGeometry.VirtualGeometryClusterSource.StoreSlot(System.Int32%2cVirtualizedGeometry.VirtualGeometryPackedVertex%5b%5d)" data-throw-if-not-resolved="false"></xref>でuploadするか、GPUのleaseを取得して完了後に公開する。

```csharp
protected abstract void GenerateSlots(IReadOnlyList<int> slots)
```

#### 引数（Parameters）

`slots` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[int](https://learn.microsoft.com/dotnet/api/system.int32)\>

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_GenerationVersion_System_Int32_"></a> GenerationVersion\(int\)

```csharp
protected virtual int GenerationVersion(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_IsCpuGeometryReady_System_Int32_"></a> IsCpuGeometryReady\(int\)

```csharp
protected bool IsCpuGeometryReady(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_IsGenerationInputReady_System_Int32_"></a> IsGenerationInputReady\(int\)

slot の生成の入力が揃っているか(既定は true)。揃っていない slot は生成を次の frame へ送る。

```csharp
protected virtual bool IsGenerationInputReady(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_IsReady_System_Int32_"></a> IsReady\(int\)

```csharp
protected bool IsReady(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_IsSlotGenerationPending_System_Int32_"></a> IsSlotGenerationPending\(int\)

```csharp
protected bool IsSlotGenerationPending(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_IsUnsupported_UnityEngine_Camera_"></a> IsUnsupported\(Camera\)

```csharp
protected bool IsUnsupported(Camera camera)
```

#### 引数（Parameters）

`camera` Camera

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_OnDeferredSlotReady_System_Int32_VirtualGeometry_World_PlanetGpuGenerationResult__"></a> OnDeferredSlotReady\(int, in PlanetGpuGenerationResult\)

```csharp
protected virtual void OnDeferredSlotReady(int slot, in PlanetGpuGenerationResult result)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`result` [PlanetGpuGenerationResult](VirtualGeometry.World.PlanetGpuGenerationResult.md)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_OnDisable"></a> OnDisable\(\)

```csharp
protected virtual void OnDisable()
```

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_OnEnable"></a> OnEnable\(\)

```csharp
protected virtual void OnEnable()
```

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_OnSlotReadinessChanged_System_Int32_"></a> OnSlotReadinessChanged\(int\)

割当中のslotのready変更。GPU選択の差分producerへ通知する。通常の描画はこの通知を待たない。

```csharp
protected virtual void OnSlotReadinessChanged(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_PollDeferredGenerationCompletions"></a> PollDeferredGenerationCompletions\(\)

```csharp
protected virtual void PollDeferredGenerationCompletions()
```

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_PrepareGenerationInputs_System_Collections_Generic_IReadOnlyList_System_Int32__"></a> PrepareGenerationInputs\(IReadOnlyList<int\>\)

生成を待っている slot(要求の順)の、生成の入力を CPU で用意する(頂点を CPU で作る供給元。既定は何もしない)。
生成の直前、frame に 1 回だけ呼ぶ。用意できた slot は <xref href="VirtualizedGeometry.VirtualGeometryClusterSource.IsGenerationInputReady(System.Int32)" data-throw-if-not-resolved="false"></xref> が true を返すこと。

```csharp
protected virtual void PrepareGenerationInputs(IReadOnlyList<int> pendingSlots)
```

#### 引数（Parameters）

`pendingSlots` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[int](https://learn.microsoft.com/dotnet/api/system.int32)\>

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_ReadbackSlotVerticesForDiagnostics_System_Int32_"></a> ReadbackSlotVerticesForDiagnostics\(int\)

検証用。slot の頂点(配置は Layout)を同期 readback で返す。

```csharp
public VirtualGeometryPackedVertex[] ReadbackSlotVerticesForDiagnostics(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [VirtualGeometryPackedVertex](VirtualizedGeometry.VirtualGeometryPackedVertex.md)\[\]

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_ReleaseSlot_System_Int32_"></a> ReleaseSlot\(int\)

```csharp
protected void ReleaseSlot(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_RequestCpuGeneration_System_Int32_"></a> RequestCpuGeneration\(int\)

既にGPU生成済みの接地slotもCPUへ昇格する。準備中は親で覆い、CPUの準備完了を偽らない。

```csharp
protected void RequestCpuGeneration(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_RequestGeneration_System_Int32_"></a> RequestGeneration\(int\)

```csharp
protected void RequestGeneration(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_RequestRegeneration_System_Int32_"></a> RequestRegeneration\(int\)

生成済みの slot を、描ける状態のまま作り直す(時間で動く頂点など)。まだ生成していない slot は、生成済みになるまで描けないまま(<xref href="VirtualizedGeometry.VirtualGeometryClusterSource.RequestGeneration(System.Int32)" data-throw-if-not-resolved="false"></xref> と同じ)。

```csharp
protected void RequestRegeneration(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_RequiresCpuGeneration_System_Int32_"></a> RequiresCpuGeneration\(int\)

```csharp
protected virtual bool RequiresCpuGeneration(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_SetUnsupported_UnityEngine_Camera_System_String_"></a> SetUnsupported\(Camera, string\)

```csharp
protected void SetUnsupported(Camera camera, string reason)
```

#### 引数（Parameters）

`camera` Camera

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_StoreSlot_System_Int32_VirtualizedGeometry_VirtualGeometryPackedVertex___"></a> StoreSlot\(int, VirtualGeometryPackedVertex\[\]\)

slot の頂点(VirtualGeometryPackedVertex、slot内配置はLayout)を pool へ書き、cluster の bounds を求めて表へ書く。

```csharp
protected void StoreSlot(int slot, VirtualGeometryPackedVertex[] vertices)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`vertices` [VirtualGeometryPackedVertex](VirtualizedGeometry.VirtualGeometryPackedVertex.md)\[\]

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_TerrainQuantizationPadding_System_Int32_"></a> TerrainQuantizationPadding\(int\)

```csharp
protected float TerrainQuantizationPadding(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_TerrainSlotFaceRange_System_Int32_"></a> TerrainSlotFaceRange\(int\)

```csharp
protected virtual Vector4 TerrainSlotFaceRange(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 Vector4

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_TryAllocateSlot_System_Int32__"></a> TryAllocateSlot\(out int\)

```csharp
protected bool TryAllocateSlot(out int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_TryBeginDeferredGeneration_System_Int32_VirtualGeometry_World_PlanetGpuGenerationLease__"></a> TryBeginDeferredGeneration\(int, out PlanetGpuGenerationLease\)

GPUへ書込みを予約する。完了まで未readyとし、接地・readyなslotはGPUへ渡さない。

```csharp
protected bool TryBeginDeferredGeneration(int slot, out PlanetGpuGenerationLease lease)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`lease` [PlanetGpuGenerationLease](VirtualGeometry.World.PlanetGpuGenerationLease.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryClusterSource_UnsupportedReason_UnityEngine_Camera_"></a> UnsupportedReason\(Camera\)

この camera で描けない理由。描けるならnull。

```csharp
public string UnsupportedReason(Camera camera)
```

#### 引数（Parameters）

`camera` Camera

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
