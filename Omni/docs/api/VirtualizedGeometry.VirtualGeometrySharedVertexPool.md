# <a id="VirtualizedGeometry_VirtualGeometrySharedVertexPool"></a> Class VirtualGeometrySharedVertexPool

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

明示indexを共有位置slotへ結ぶCPU publication host。GPU backendはBeginDraw/Completeのreceiptを実描画完了に結ぶ。
このhost単独ではGPUロードを有効化しない。全てmain threadで使用する。

```csharp
public sealed class VirtualGeometrySharedVertexPool
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometrySharedVertexPool](VirtualizedGeometry.VirtualGeometrySharedVertexPool.md)

## コンストラクター（Constructors）

### <a id="VirtualizedGeometry_VirtualGeometrySharedVertexPool__ctor_System_Int32_"></a> VirtualGeometrySharedVertexPool\(int\)

```csharp
public VirtualGeometrySharedVertexPool(int capacity)
```

#### 引数（Parameters）

`capacity` [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="VirtualizedGeometry_VirtualGeometrySharedVertexPool_Capacity"></a> Capacity

```csharp
public int Capacity { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometrySharedVertexPool_ResidentVertexCount"></a> ResidentVertexCount

```csharp
public int ResidentVertexCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometrySharedVertexPool_TryPublish_System_Collections_Generic_IReadOnlyList_VirtualizedGeometry_VirtualGeometrySharedRegion__System_Collections_Generic_IReadOnlyList_VirtualizedGeometry_VirtualGeometrySharedVertexId____VirtualizedGeometry_VirtualGeometrySharedSnapshot__"></a> TryPublish\(IReadOnlyList<VirtualGeometrySharedRegion\>, IReadOnlyList<VirtualGeometrySharedVertexId\[\]\>, out VirtualGeometrySharedSnapshot\)

未準備/取消/予算不足はfalse。現在のsnapshotは呼出し側が保持し、新公開成功時だけ置き換える。

```csharp
public bool TryPublish(IReadOnlyList<VirtualGeometrySharedRegion> regions, IReadOnlyList<VirtualGeometrySharedVertexId[]> seams, out VirtualGeometrySharedSnapshot snapshot)
```

#### 引数（Parameters）

`regions` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[VirtualGeometrySharedRegion](VirtualizedGeometry.VirtualGeometrySharedRegion.md)\>

`seams` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[VirtualGeometrySharedVertexId](VirtualizedGeometry.VirtualGeometrySharedVertexId.md)\[\]\>

`snapshot` [VirtualGeometrySharedSnapshot](VirtualizedGeometry.VirtualGeometrySharedSnapshot.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometrySharedVertexPool_TryRelativePosition_System_UInt32_Omni_Logical_Vector3__UnityEngine_Vector3__"></a> TryRelativePosition\(uint, in Vector3, out Vector3\)

共有slotを一つのLogical描画原点から局所化する。領域ごとのfloat行列を位置へ再適用しない。

```csharp
public bool TryRelativePosition(uint slot, in Vector3 viewOrigin, out Vector3 position)
```

#### 引数（Parameters）

`slot` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`viewOrigin` Vector3

`position` Vector3

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
