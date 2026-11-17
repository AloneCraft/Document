# <a id="VirtualizedGeometry_VirtualGeometryConnectedCut"></a> Class VirtualGeometryConnectedCut

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

完全な置換cutを一つの公開単位にする。準備前には旧cutを保持する。

```csharp
public sealed class VirtualGeometryConnectedCut
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryConnectedCut](VirtualizedGeometry.VirtualGeometryConnectedCut.md)

## コンストラクター（Constructors）

### <a id="VirtualizedGeometry_VirtualGeometryConnectedCut__ctor_System_Int32_System_Int32___VirtualizedGeometry_VirtualGeometryConnectedRegion___"></a> VirtualGeometryConnectedCut\(int, int\[\], VirtualGeometryConnectedRegion\[\]\)

```csharp
public VirtualGeometryConnectedCut(int epoch, int[] groups, VirtualGeometryConnectedRegion[] regions)
```

#### 引数（Parameters）

`epoch` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`groups` [int](https://learn.microsoft.com/dotnet/api/system.int32)\[\]

`regions` [VirtualGeometryConnectedRegion](VirtualizedGeometry.VirtualGeometryConnectedRegion.md)\[\]

## フィールド（Fields）

### <a id="VirtualizedGeometry_VirtualGeometryConnectedCut_Epoch"></a> Epoch

```csharp
public readonly int Epoch
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryConnectedCut_Groups"></a> Groups

```csharp
public readonly int[] Groups
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)\[\]

### <a id="VirtualizedGeometry_VirtualGeometryConnectedCut_Regions"></a> Regions

```csharp
public readonly VirtualGeometryConnectedRegion[] Regions
```

#### 値（Field Value）

 [VirtualGeometryConnectedRegion](VirtualizedGeometry.VirtualGeometryConnectedRegion.md)\[\]

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometryConnectedCut_Matches_System_Int32_System_Collections_Generic_IReadOnlyList_System_Int32__"></a> Matches\(int, IReadOnlyList<int\>\)

```csharp
public bool Matches(int epoch, IReadOnlyList<int> groups)
```

#### 引数（Parameters）

`epoch` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`groups` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[int](https://learn.microsoft.com/dotnet/api/system.int32)\>

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
