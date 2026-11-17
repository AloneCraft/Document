# <a id="VirtualizedGeometry_IVirtualGeometryGeometrySource"></a> Interface IVirtualGeometryGeometrySource

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

静的/手続きmeshを共通page常駐へ供給する口。面・XY・四分木を共通controllerへ持ち込まない。

```csharp
public interface IVirtualGeometryGeometrySource : IVirtualGeometryPageStore, IDisposable
```

#### 実装するインターフェース（Implements）

[IVirtualGeometryPageStore](VirtualizedGeometry.IVirtualGeometryPageStore.md), 
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

## プロパティ（Properties）

### <a id="VirtualizedGeometry_IVirtualGeometryGeometrySource_CatalogCapacity"></a> CatalogCapacity

```csharp
int CatalogCapacity { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_IVirtualGeometryGeometrySource_Epoch"></a> Epoch

```csharp
int Epoch { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_IVirtualGeometryGeometrySource_Roots"></a> Roots

```csharp
IReadOnlyList<int> Roots { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[int](https://learn.microsoft.com/dotnet/api/system.int32)\>

### <a id="VirtualizedGeometry_IVirtualGeometryGeometrySource_Topology"></a> Topology

```csharp
VirtualGeometryPage Topology { get; }
```

#### 値（Property Value）

 [VirtualGeometryPage](VirtualizedGeometry.VirtualGeometryPage.md)

## メソッド（Methods）

### <a id="VirtualizedGeometry_IVirtualGeometryGeometrySource_Describe_System_Int32_"></a> Describe\(int\)

```csharp
VirtualGeometryGeometryGroup Describe(int id)
```

#### 引数（Parameters）

`id` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [VirtualGeometryGeometryGroup](VirtualizedGeometry.VirtualGeometryGeometryGroup.md)

### <a id="VirtualizedGeometry_IVirtualGeometryGeometrySource_Inputs_System_Int32_"></a> Inputs\(int\)

```csharp
IReadOnlyList<int> Inputs(int id)
```

#### 引数（Parameters）

`id` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[int](https://learn.microsoft.com/dotnet/api/system.int32)\>

### <a id="VirtualizedGeometry_IVirtualGeometryGeometrySource_IsVisible_System_Int32_VirtualizedGeometry_VirtualGeometryGeometryView__"></a> IsVisible\(int, in VirtualGeometryGeometryView\)

```csharp
bool IsVisible(int id, in VirtualGeometryGeometryView frame)
```

#### 引数（Parameters）

`id` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`frame` [VirtualGeometryGeometryView](VirtualizedGeometry.VirtualGeometryGeometryView.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_IVirtualGeometryGeometrySource_Prepare_System_Int32_System_Single_"></a> Prepare\(int, float\)

```csharp
bool Prepare(int id, float priority)
```

#### 引数（Parameters）

`id` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`priority` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_IVirtualGeometryGeometrySource_TryBeginFrame_VirtualizedGeometry_VirtualGeometryClusterView__UnityEngine_Transform_VirtualizedGeometry_VirtualGeometryGeometryView__"></a> TryBeginFrame\(in VirtualGeometryClusterView, Transform, out VirtualGeometryGeometryView\)

```csharp
bool TryBeginFrame(in VirtualGeometryClusterView view, Transform transform, out VirtualGeometryGeometryView frame)
```

#### 引数（Parameters）

`view` [VirtualGeometryClusterView](VirtualizedGeometry.VirtualGeometryClusterView.md)

`transform` Transform

`frame` [VirtualGeometryGeometryView](VirtualizedGeometry.VirtualGeometryGeometryView.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_IVirtualGeometryGeometrySource_TryPlace_System_Int32_VirtualizedGeometry_VirtualGeometryGeometryView__UnityEngine_MaterialPropertyBlock_VirtualizedGeometry_VirtualGeometryInstancePose__"></a> TryPlace\(int, in VirtualGeometryGeometryView, MaterialPropertyBlock, out VirtualGeometryInstancePose\)

```csharp
bool TryPlace(int id, in VirtualGeometryGeometryView frame, MaterialPropertyBlock properties, out VirtualGeometryInstancePose pose)
```

#### 引数（Parameters）

`id` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`frame` [VirtualGeometryGeometryView](VirtualizedGeometry.VirtualGeometryGeometryView.md)

`properties` MaterialPropertyBlock

`pose` [VirtualGeometryInstancePose](VirtualizedGeometry.VirtualGeometryInstancePose.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
