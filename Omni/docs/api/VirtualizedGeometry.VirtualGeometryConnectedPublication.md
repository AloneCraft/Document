# <a id="VirtualizedGeometry_VirtualGeometryConnectedPublication"></a> Class VirtualGeometryConnectedPublication

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

接続集合のCPU公開判定。snapshot使用中のpage寿命は呼出し側が保持する。既存Rendererへ自動接続はしない。

```csharp
public sealed class VirtualGeometryConnectedPublication
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryConnectedPublication](VirtualizedGeometry.VirtualGeometryConnectedPublication.md)

## コンストラクター（Constructors）

### <a id="VirtualizedGeometry_VirtualGeometryConnectedPublication__ctor_VirtualizedGeometry_VirtualGeometryStreamMetadata___"></a> VirtualGeometryConnectedPublication\(params VirtualGeometryStreamMetadata\[\]\)

```csharp
public VirtualGeometryConnectedPublication(params VirtualGeometryStreamMetadata[] archives)
```

#### 引数（Parameters）

`archives` [VirtualGeometryStreamMetadata](VirtualizedGeometry.VirtualGeometryStreamMetadata.md)\[\]

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometryConnectedPublication_TryPublish_System_Boolean___System_Func_System_Int32_System_Int32_System_Boolean__System_UInt32______"></a> TryPublish\(bool\[\], Func<int, int, bool\>, out uint\[\]\[\]\)

leaf/rootの完全表現を集合として返す。詳細不足はrootへ戻し、root不足なら空集合を返す。

```csharp
public bool TryPublish(bool[] preferLeaves, Func<int, int, bool> pageReady, out uint[][] nodes)
```

#### 引数（Parameters）

`preferLeaves` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)\[\]

`pageReady` [Func](https://learn.microsoft.com/dotnet/api/system.func\-3)<[int](https://learn.microsoft.com/dotnet/api/system.int32), [int](https://learn.microsoft.com/dotnet/api/system.int32), [bool](https://learn.microsoft.com/dotnet/api/system.boolean)\>

`nodes` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]\[\]

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryConnectedPublication_TrySelect_VirtualizedGeometry_VirtualGeometryLodSelectionContext___System_Func_System_Int32_System_Int32_System_Boolean__VirtualizedGeometry_VirtualGeometryLodSelectionResult____"></a> TrySelect\(VirtualGeometryLodSelectionContext\[\], Func<int, int, bool\>, out VirtualGeometryLodSelectionResult\[\]\)

既存CPU selectorの完全cutを接続集合として公開する。部分的なgroup出力はSelectedClustersを正本にする。

```csharp
public bool TrySelect(VirtualGeometryLodSelectionContext[] contexts, Func<int, int, bool> pageReady, out VirtualGeometryLodSelectionResult[] cuts)
```

#### 引数（Parameters）

`contexts` [VirtualGeometryLodSelectionContext](VirtualizedGeometry.VirtualGeometryLodSelectionContext.md)\[\]

`pageReady` [Func](https://learn.microsoft.com/dotnet/api/system.func\-3)<[int](https://learn.microsoft.com/dotnet/api/system.int32), [int](https://learn.microsoft.com/dotnet/api/system.int32), [bool](https://learn.microsoft.com/dotnet/api/system.boolean)\>

`cuts` [VirtualGeometryLodSelectionResult](VirtualizedGeometry.VirtualGeometryLodSelectionResult.md)\[\]

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
