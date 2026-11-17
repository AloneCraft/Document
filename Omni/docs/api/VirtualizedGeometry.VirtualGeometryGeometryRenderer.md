# <a id="VirtualizedGeometry_VirtualGeometryGeometryRenderer"></a> Class VirtualGeometryGeometryRenderer

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

手続きsourceのmeshを、通常VGのpage/pool/cull/drawへ接続する。groupごとにGameObjectを増やさない。
Moon(汎用版)のMoonオブジェクトに付き、MoonStreamingSetupがgeometry producerと材質を設定する。
Edit Mode でも動く(設定した側が Edit Mode で用意したときだけ描く。設定が無ければ何もしない)。

```csharp
[DisallowMultipleComponent]
[ExecuteAlways]
public sealed class VirtualGeometryGeometryRenderer : MonoBehaviour
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[VirtualGeometryGeometryRenderer](VirtualizedGeometry.VirtualGeometryGeometryRenderer.md)

## プロパティ（Properties）

### <a id="VirtualizedGeometry_VirtualGeometryGeometryRenderer_AllocatedCanonicalPositionBytes"></a> AllocatedCanonicalPositionBytes

```csharp
public long AllocatedCanonicalPositionBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryRenderer_AllocatedGeometryBytes"></a> AllocatedGeometryBytes

```csharp
public long AllocatedGeometryBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryRenderer_AllocatedTemplateIndexBytes"></a> AllocatedTemplateIndexBytes

```csharp
public long AllocatedTemplateIndexBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryRenderer_CompleteGroupCount"></a> CompleteGroupCount

```csharp
public int CompleteGroupCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryRenderer_DeepestSelectedLevel"></a> DeepestSelectedLevel

```csharp
public int DeepestSelectedLevel { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryRenderer_DrawError"></a> DrawError

```csharp
public string DrawError { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryRenderer_DrawnCount"></a> DrawnCount

```csharp
public int DrawnCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryRenderer_LastProjectionScale"></a> LastProjectionScale

```csharp
public float LastProjectionScale { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryRenderer_LastPublicationMilliseconds"></a> LastPublicationMilliseconds

```csharp
public float LastPublicationMilliseconds { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryRenderer_LastSelectMilliseconds"></a> LastSelectMilliseconds

```csharp
public float LastSelectMilliseconds { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryRenderer_PendingGeneration"></a> PendingGeneration

```csharp
public int PendingGeneration { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryRenderer_PublishedGroupCount"></a> PublishedGroupCount

```csharp
public int PublishedGroupCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryRenderer_ResidentIndexPatterns"></a> ResidentIndexPatterns

```csharp
public int ResidentIndexPatterns { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryRenderer_ResourceCreationCpuMilliseconds"></a> ResourceCreationCpuMilliseconds

```csharp
public float ResourceCreationCpuMilliseconds { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryRenderer_RetainedCpuGeometryBytes"></a> RetainedCpuGeometryBytes

```csharp
public long RetainedCpuGeometryBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryRenderer_SelectedCount"></a> SelectedCount

```csharp
public int SelectedCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryRenderer_SharedBoundaryVertexCount"></a> SharedBoundaryVertexCount

```csharp
public int SharedBoundaryVertexCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryRenderer_Source"></a> Source

```csharp
public IVirtualGeometryGeometrySource Source { get; }
```

#### 値（Property Value）

 [IVirtualGeometryGeometrySource](VirtualizedGeometry.IVirtualGeometryGeometrySource.md)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryRenderer_StreamingStatistics"></a> StreamingStatistics

```csharp
public VirtualGeometryStreamingStatistics StreamingStatistics { get; }
```

#### 値（Property Value）

 [VirtualGeometryStreamingStatistics](VirtualizedGeometry.VirtualGeometryStreamingStatistics.md)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryRenderer_TargetPixels"></a> TargetPixels

```csharp
public float TargetPixels { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryRenderer_TemplateCreationCpuMilliseconds"></a> TemplateCreationCpuMilliseconds

```csharp
public double TemplateCreationCpuMilliseconds { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometryGeometryRenderer_Configure_VirtualizedGeometry_IVirtualGeometryGeometrySource_UnityEngine_Material_System_Int32_System_Single_System_Int64_System_Int32_System_Int32_"></a> Configure\(IVirtualGeometryGeometrySource, Material, int, float, long, int, int\)

```csharp
public void Configure(IVirtualGeometryGeometrySource geometry, Material material, int capacity, float pixels, long cpuBytes = 134217728, int workers = 6, int maximumDrawGroups = 2304)
```

#### 引数（Parameters）

`geometry` [IVirtualGeometryGeometrySource](VirtualizedGeometry.IVirtualGeometryGeometrySource.md)

`material` Material

`capacity` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`pixels` [float](https://learn.microsoft.com/dotnet/api/system.single)

`cpuBytes` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`workers` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`maximumDrawGroups` [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryRenderer_IsReady_System_Int32_"></a> IsReady\(int\)

```csharp
public bool IsReady(int id)
```

#### 引数（Parameters）

`id` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryRenderer_ReleaseGeometry"></a> ReleaseGeometry\(\)

設定した形と GPU の資源を手放す(Edit Mode の片付けで、設定した側が呼ぶ)。もう一度 <xref href="VirtualizedGeometry.VirtualGeometryGeometryRenderer.Configure(VirtualizedGeometry.IVirtualGeometryGeometrySource%2cUnityEngine.Material%2cSystem.Int32%2cSystem.Single%2cSystem.Int64%2cSystem.Int32%2cSystem.Int32)" data-throw-if-not-resolved="false"></xref> するまで描かない。

```csharp
public void ReleaseGeometry()
```

### <a id="VirtualizedGeometry_VirtualGeometryGeometryRenderer_Request_System_Int32_System_Single_"></a> Request\(int, float\)

```csharp
public void Request(int id, float priority)
```

#### 引数（Parameters）

`id` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`priority` [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryRenderer_SelectedForCamera_UnityEngine_Camera_"></a> SelectedForCamera\(Camera\)

```csharp
public IReadOnlyList<int> SelectedForCamera(Camera camera)
```

#### 引数（Parameters）

`camera` Camera

#### 戻り値（Returns）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[int](https://learn.microsoft.com/dotnet/api/system.int32)\>

### <a id="VirtualizedGeometry_VirtualGeometryGeometryRenderer_TryGetPublishedRegion_UnityEngine_Camera_System_Int32_VirtualizedGeometry_VirtualGeometryConnectedRegion__"></a> TryGetPublishedRegion\(Camera, int, out VirtualGeometryConnectedRegion\)

```csharp
public bool TryGetPublishedRegion(Camera camera, int group, out VirtualGeometryConnectedRegion region)
```

#### 引数（Parameters）

`camera` Camera

`group` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`region` [VirtualGeometryConnectedRegion](VirtualizedGeometry.VirtualGeometryConnectedRegion.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryGeometryRenderer_TryGetPublishedTriangle_UnityEngine_Camera_System_Int32_System_Int32_VirtualizedGeometry_VirtualGeometrySharedLocalTriangle__"></a> TryGetPublishedTriangle\(Camera, int, int, out VirtualGeometrySharedLocalTriangle\)

指定Cameraの実際の公開世代と、GPUと同じfloat位置から三角形を取得する。

```csharp
public bool TryGetPublishedTriangle(Camera camera, int group, int triangle, out VirtualGeometrySharedLocalTriangle value)
```

#### 引数（Parameters）

`camera` Camera

`group` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`triangle` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`value` [VirtualGeometrySharedLocalTriangle](VirtualizedGeometry.VirtualGeometrySharedLocalTriangle.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
