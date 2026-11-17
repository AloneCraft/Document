# <a id="VirtualizedGeometry_IVirtualGeometryConnectedMeshSource"></a> Interface IVirtualGeometryConnectedMeshSource

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

任意meshの接続、局所配置と共通描画原点を供給する口。惑星のface/XY/格子はこの実装側だけが扱う。

```csharp
public interface IVirtualGeometryConnectedMeshSource
```

## メソッド（Methods）

### <a id="VirtualizedGeometry_IVirtualGeometryConnectedMeshSource_TryPrepareCut_System_Collections_Generic_IReadOnlyList_System_Int32__VirtualizedGeometry_IVirtualGeometryGeometryResidency_System_Func_System_Int32_VirtualizedGeometry_VirtualGeometryPackedVertex____VirtualizedGeometry_VirtualGeometryConnectedCut_VirtualizedGeometry_VirtualGeometryConnectedCut__"></a> TryPrepareCut\(IReadOnlyList<int\>, IVirtualGeometryGeometryResidency, Func<int, VirtualGeometryPackedVertex\[\]\>, VirtualGeometryConnectedCut, out VirtualGeometryConnectedCut\)

```csharp
bool TryPrepareCut(IReadOnlyList<int> groups, IVirtualGeometryGeometryResidency residency, Func<int, VirtualGeometryPackedVertex[]> vertices, VirtualGeometryConnectedCut previous, out VirtualGeometryConnectedCut cut)
```

#### 引数（Parameters）

`groups` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[int](https://learn.microsoft.com/dotnet/api/system.int32)\>

`residency` [IVirtualGeometryGeometryResidency](VirtualizedGeometry.IVirtualGeometryGeometryResidency.md)

`vertices` [Func](https://learn.microsoft.com/dotnet/api/system.func\-2)<[int](https://learn.microsoft.com/dotnet/api/system.int32), [VirtualGeometryPackedVertex](VirtualizedGeometry.VirtualGeometryPackedVertex.md)\[\]\>

`previous` [VirtualGeometryConnectedCut](VirtualizedGeometry.VirtualGeometryConnectedCut.md)

`cut` [VirtualGeometryConnectedCut](VirtualizedGeometry.VirtualGeometryConnectedCut.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_IVirtualGeometryConnectedMeshSource_TrySharedFrame_VirtualizedGeometry_VirtualGeometryGeometryView__System_Object_System_Object__Omni_Logical_Vector3__"></a> TrySharedFrame\(in VirtualGeometryGeometryView, object, out object, out Vector3\)

```csharp
bool TrySharedFrame(in VirtualGeometryGeometryView frame, object previous, out object state, out Vector3 origin)
```

#### 引数（Parameters）

`frame` [VirtualGeometryGeometryView](VirtualizedGeometry.VirtualGeometryGeometryView.md)

`previous` [object](https://learn.microsoft.com/dotnet/api/system.object)

`state` [object](https://learn.microsoft.com/dotnet/api/system.object)

`origin` Vector3

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_IVirtualGeometryConnectedMeshSource_TrySharedPlacement_System_Int32_VirtualizedGeometry_VirtualGeometryGeometryView__System_Object_UnityEngine_MaterialPropertyBlock_UnityEngine_Matrix4x4__"></a> TrySharedPlacement\(int, in VirtualGeometryGeometryView, object, MaterialPropertyBlock, out Matrix4x4\)

```csharp
bool TrySharedPlacement(int group, in VirtualGeometryGeometryView frame, object sharedFrame, MaterialPropertyBlock properties, out Matrix4x4 objectToWorld)
```

#### 引数（Parameters）

`group` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`frame` [VirtualGeometryGeometryView](VirtualizedGeometry.VirtualGeometryGeometryView.md)

`sharedFrame` [object](https://learn.microsoft.com/dotnet/api/system.object)

`properties` MaterialPropertyBlock

`objectToWorld` Matrix4x4

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
