# <a id="VirtualGeometry_World_PlanetMeshGeometrySource"></a> Class PlanetMeshGeometrySource

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

惑星固有の格子・標高を、汎用VGの局所mesh/page producerへ変換する。選択・退避・描画は所有しない。

```csharp
public sealed class PlanetMeshGeometrySource : IVirtualGeometryGeometrySource, IVirtualGeometryPageStore, IDisposable, IVirtualGeometryProtectedGroups, IVirtualGeometryConnectedMeshSource
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetMeshGeometrySource](VirtualGeometry.World.PlanetMeshGeometrySource.md)

#### 実装するインターフェース（Implements）

[IVirtualGeometryGeometrySource](VirtualizedGeometry.IVirtualGeometryGeometrySource.md), 
[IVirtualGeometryPageStore](VirtualizedGeometry.IVirtualGeometryPageStore.md), 
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), 
[IVirtualGeometryProtectedGroups](VirtualizedGeometry.IVirtualGeometryProtectedGroups.md), 
[IVirtualGeometryConnectedMeshSource](VirtualizedGeometry.IVirtualGeometryConnectedMeshSource.md)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource__ctor_VirtualGeometry_World_IPlanetHeightProvider_VirtualGeometry_World_IPlanetCellHeightSource_VirtualGeometry_World_IPlanetCellPropertySource_VirtualGeometry_World_IPlanetPlacement_System_Single_System_Int32_System_Func_VirtualGeometry_World_PlanetCellKey_System_Single__"></a> PlanetMeshGeometrySource\(IPlanetHeightProvider, IPlanetCellHeightSource, IPlanetCellPropertySource, IPlanetPlacement, float, int, Func<PlanetCellKey, float\>\)

```csharp
public PlanetMeshGeometrySource(IPlanetHeightProvider heights, IPlanetCellHeightSource grids, IPlanetCellPropertySource properties, IPlanetPlacement placement, float radius, int maximumLevel, Func<PlanetCellKey, float> sourceError)
```

#### 引数（Parameters）

`heights` [IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

`grids` [IPlanetCellHeightSource](VirtualGeometry.World.IPlanetCellHeightSource.md)

`properties` [IPlanetCellPropertySource](VirtualGeometry.World.IPlanetCellPropertySource.md)

`placement` [IPlanetPlacement](VirtualGeometry.World.IPlanetPlacement.md)

`radius` [float](https://learn.microsoft.com/dotnet/api/system.single)

`maximumLevel` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`sourceError` [Func](https://learn.microsoft.com/dotnet/api/system.func\-2)<[PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md), [float](https://learn.microsoft.com/dotnet/api/system.single)\>

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource_CatalogCapacity"></a> CatalogCapacity

```csharp
public int CatalogCapacity { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource_ConnectionWaitReason"></a> ConnectionWaitReason

```csharp
public string ConnectionWaitReason { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource_CpuBuildBackend"></a> CpuBuildBackend

```csharp
public PlanetCpuBuildBackend CpuBuildBackend { get; set; }
```

#### 値（Property Value）

 [PlanetCpuBuildBackend](VirtualGeometry.World.PlanetCpuBuildBackend.md)

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource_EnsureCanonicalHeight"></a> EnsureCanonicalHeight

```csharp
public Func<double, double, double, float, bool> EnsureCanonicalHeight { get; set; }
```

#### 値（Property Value）

 [Func](https://learn.microsoft.com/dotnet/api/system.func\-5)<[double](https://learn.microsoft.com/dotnet/api/system.double), [double](https://learn.microsoft.com/dotnet/api/system.double), [double](https://learn.microsoft.com/dotnet/api/system.double), [float](https://learn.microsoft.com/dotnet/api/system.single), [bool](https://learn.microsoft.com/dotnet/api/system.boolean)\>

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource_Epoch"></a> Epoch

```csharp
public int Epoch { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource_Heights"></a> Heights

```csharp
public IPlanetHeightProvider Heights { get; }
```

#### 値（Property Value）

 [IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource_MaximumLevel"></a> MaximumLevel

```csharp
public int MaximumLevel { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource_MaximumPublicationRegions"></a> MaximumPublicationRegions

```csharp
public int MaximumPublicationRegions { get; set; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource_ProtectedGroups"></a> ProtectedGroups

```csharp
public IReadOnlyList<int> ProtectedGroups { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[int](https://learn.microsoft.com/dotnet/api/system.int32)\>

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource_ReusedPreparedBoundaryVertices"></a> ReusedPreparedBoundaryVertices

```csharp
public long ReusedPreparedBoundaryVertices { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource_Roots"></a> Roots

```csharp
public IReadOnlyList<int> Roots { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[int](https://learn.microsoft.com/dotnet/api/system.int32)\>

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource_Topology"></a> Topology

```csharp
public VirtualGeometryPage Topology { get; }
```

#### 値（Property Value）

 [VirtualGeometryPage](VirtualizedGeometry.VirtualGeometryPage.md)

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource_UsePreparedSampling"></a> UsePreparedSampling

```csharp
public bool UsePreparedSampling { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource_Describe_System_Int32_"></a> Describe\(int\)

```csharp
public VirtualGeometryGeometryGroup Describe(int id)
```

#### 引数（Parameters）

`id` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [VirtualGeometryGeometryGroup](VirtualizedGeometry.VirtualGeometryGeometryGroup.md)

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource_Dispose"></a> Dispose\(\)

```csharp
public void Dispose()
```

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource_Frame_VirtualGeometry_World_PlanetCellKey__"></a> Frame\(in PlanetCellKey\)

```csharp
public PlanetCellFrame Frame(in PlanetCellKey key)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

#### 戻り値（Returns）

 [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource_IdFor_VirtualGeometry_World_PlanetCellKey__"></a> IdFor\(in PlanetCellKey\)

```csharp
public int IdFor(in PlanetCellKey key)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource_Inputs_System_Int32_"></a> Inputs\(int\)

```csharp
public IReadOnlyList<int> Inputs(int id)
```

#### 引数（Parameters）

`id` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[int](https://learn.microsoft.com/dotnet/api/system.int32)\>

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource_IsVisible_System_Int32_VirtualizedGeometry_VirtualGeometryGeometryView__"></a> IsVisible\(int, in VirtualGeometryGeometryView\)

```csharp
public bool IsVisible(int id, in VirtualGeometryGeometryView view)
```

#### 引数（Parameters）

`id` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`view` [VirtualGeometryGeometryView](VirtualizedGeometry.VirtualGeometryGeometryView.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource_KeyFor_System_Int32_"></a> KeyFor\(int\)

```csharp
public PlanetCellKey KeyFor(int id)
```

#### 引数（Parameters）

`id` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource_MustRefine_System_Int32_"></a> MustRefine\(int\)

```csharp
public bool MustRefine(int id)
```

#### 引数（Parameters）

`id` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource_Prepare_System_Int32_System_Single_"></a> Prepare\(int, float\)

```csharp
public bool Prepare(int id, float priority)
```

#### 引数（Parameters）

`id` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`priority` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource_QuadArc_System_Int32_"></a> QuadArc\(int\)

```csharp
public float QuadArc(int level)
```

#### 引数（Parameters）

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource_ReadAsync_System_Int32_System_Threading_CancellationToken_"></a> ReadAsync\(int, CancellationToken\)

```csharp
public Task<VirtualGeometryPagePayload> ReadAsync(int page, CancellationToken cancellation)
```

#### 引数（Parameters）

`page` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`cancellation` [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)

#### 戻り値（Returns）

 [Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task\-1)<[VirtualGeometryPagePayload](VirtualizedGeometry.VirtualGeometryPagePayload.md)\>

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource_SetContactRegions_System_Collections_Generic_IReadOnlyList_VirtualGeometry_World_PlanetContactRegion__"></a> SetContactRegions\(IReadOnlyList<PlanetContactRegion\>\)

```csharp
public void SetContactRegions(IReadOnlyList<PlanetContactRegion> regions)
```

#### 引数（Parameters）

`regions` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[PlanetContactRegion](VirtualGeometry.World.PlanetContactRegion.md)\>

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource_SetPublishedBounds_System_Int32_UnityEngine_Vector4_"></a> SetPublishedBounds\(int, Vector4\)

```csharp
public void SetPublishedBounds(int id, Vector4 bounds)
```

#### 引数（Parameters）

`id` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`bounds` Vector4

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource_TryBeginFrame_VirtualizedGeometry_VirtualGeometryClusterView__UnityEngine_Transform_VirtualizedGeometry_VirtualGeometryGeometryView__"></a> TryBeginFrame\(in VirtualGeometryClusterView, Transform, out VirtualGeometryGeometryView\)

```csharp
public bool TryBeginFrame(in VirtualGeometryClusterView view, Transform transform, out VirtualGeometryGeometryView frame)
```

#### 引数（Parameters）

`view` [VirtualGeometryClusterView](VirtualizedGeometry.VirtualGeometryClusterView.md)

`transform` Transform

`frame` [VirtualGeometryGeometryView](VirtualizedGeometry.VirtualGeometryGeometryView.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource_TryPlace_System_Int32_VirtualizedGeometry_VirtualGeometryGeometryView__UnityEngine_MaterialPropertyBlock_VirtualizedGeometry_VirtualGeometryInstancePose__"></a> TryPlace\(int, in VirtualGeometryGeometryView, MaterialPropertyBlock, out VirtualGeometryInstancePose\)

```csharp
public bool TryPlace(int id, in VirtualGeometryGeometryView frame, MaterialPropertyBlock block, out VirtualGeometryInstancePose pose)
```

#### 引数（Parameters）

`id` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`frame` [VirtualGeometryGeometryView](VirtualizedGeometry.VirtualGeometryGeometryView.md)

`block` MaterialPropertyBlock

`pose` [VirtualGeometryInstancePose](VirtualizedGeometry.VirtualGeometryInstancePose.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource_TryPrepareCut_System_Collections_Generic_IReadOnlyList_System_Int32__VirtualizedGeometry_IVirtualGeometryGeometryResidency_System_Func_System_Int32_VirtualizedGeometry_VirtualGeometryPackedVertex____VirtualizedGeometry_VirtualGeometryConnectedCut_VirtualizedGeometry_VirtualGeometryConnectedCut__"></a> TryPrepareCut\(IReadOnlyList<int\>, IVirtualGeometryGeometryResidency, Func<int, VirtualGeometryPackedVertex\[\]\>, VirtualGeometryConnectedCut, out VirtualGeometryConnectedCut\)

共有境界の高さ入力をまとめて要求し、2:1へ釣り合わせた完全cutだけを公開する。

```csharp
public bool TryPrepareCut(IReadOnlyList<int> selected, IVirtualGeometryGeometryResidency residency, Func<int, VirtualGeometryPackedVertex[]> vertices, VirtualGeometryConnectedCut previous, out VirtualGeometryConnectedCut cut)
```

#### 引数（Parameters）

`selected` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[int](https://learn.microsoft.com/dotnet/api/system.int32)\>

`residency` [IVirtualGeometryGeometryResidency](VirtualizedGeometry.IVirtualGeometryGeometryResidency.md)

`vertices` [Func](https://learn.microsoft.com/dotnet/api/system.func\-2)<[int](https://learn.microsoft.com/dotnet/api/system.int32), [VirtualGeometryPackedVertex](VirtualizedGeometry.VirtualGeometryPackedVertex.md)\[\]\>

`previous` [VirtualGeometryConnectedCut](VirtualizedGeometry.VirtualGeometryConnectedCut.md)

`cut` [VirtualGeometryConnectedCut](VirtualizedGeometry.VirtualGeometryConnectedCut.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource_TrySampleMeshHeight_Omni_Logical_Vector3__System_Int32_System_Double__"></a> TrySampleMeshHeight\(in Vector3, int, out double\)

```csharp
public bool TrySampleMeshHeight(in Vector3 point, int level, out double height)
```

#### 引数（Parameters）

`point` Vector3

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`height` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource_TrySamplePublishedHeight_VirtualizedGeometry_VirtualGeometryGeometryRenderer_UnityEngine_Camera_Omni_Logical_Vector3__System_Int32_System_Double__"></a> TrySamplePublishedHeight\(VirtualGeometryGeometryRenderer, Camera, in Vector3, int, out double\)

公開済み接続三角形のうち、問い合わせ点を含むclusterだけを描画と同じfloat位置で照合する。

```csharp
public bool TrySamplePublishedHeight(VirtualGeometryGeometryRenderer renderer, Camera camera, in Vector3 point, int level, out double height)
```

#### 引数（Parameters）

`renderer` [VirtualGeometryGeometryRenderer](VirtualizedGeometry.VirtualGeometryGeometryRenderer.md)

`camera` Camera

`point` Vector3

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`height` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource_TrySharedFrame_VirtualizedGeometry_VirtualGeometryGeometryView__System_Object_System_Object__Omni_Logical_Vector3__"></a> TrySharedFrame\(in VirtualGeometryGeometryView, object, out object, out Vector3\)

```csharp
public bool TrySharedFrame(in VirtualGeometryGeometryView frame, object previous, out object state, out Vector3 origin)
```

#### 引数（Parameters）

`frame` [VirtualGeometryGeometryView](VirtualizedGeometry.VirtualGeometryGeometryView.md)

`previous` [object](https://learn.microsoft.com/dotnet/api/system.object)

`state` [object](https://learn.microsoft.com/dotnet/api/system.object)

`origin` Vector3

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetMeshGeometrySource_TrySharedPlacement_System_Int32_VirtualizedGeometry_VirtualGeometryGeometryView__System_Object_UnityEngine_MaterialPropertyBlock_UnityEngine_Matrix4x4__"></a> TrySharedPlacement\(int, in VirtualGeometryGeometryView, object, MaterialPropertyBlock, out Matrix4x4\)

```csharp
public bool TrySharedPlacement(int group, in VirtualGeometryGeometryView frame, object sharedFrame, MaterialPropertyBlock properties, out Matrix4x4 objectToWorld)
```

#### 引数（Parameters）

`group` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`frame` [VirtualGeometryGeometryView](VirtualizedGeometry.VirtualGeometryGeometryView.md)

`sharedFrame` [object](https://learn.microsoft.com/dotnet/api/system.object)

`properties` MaterialPropertyBlock

`objectToWorld` Matrix4x4

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
