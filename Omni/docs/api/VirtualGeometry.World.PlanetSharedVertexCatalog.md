# <a id="VirtualGeometry_World_PlanetSharedVertexCatalog"></a> Class PlanetSharedVertexCatalog

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

惑星固有の正本keyを汎用ID/Logical位置へ供給する。高さ未準備の頂点は登録しない。

```csharp
public sealed class PlanetSharedVertexCatalog
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetSharedVertexCatalog](VirtualGeometry.World.PlanetSharedVertexCatalog.md)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetSharedVertexCatalog__ctor_System_Guid_Omni_Logical_Vector3__Omni_Logical_Scalar__System_Int32_"></a> PlanetSharedVertexCatalog\(Guid, in Vector3, in Scalar, int\)

```csharp
public PlanetSharedVertexCatalog(Guid domain, in Vector3 origin, in Scalar radius, int capacity)
```

#### 引数（Parameters）

`domain` [Guid](https://learn.microsoft.com/dotnet/api/system.guid)

`origin` Vector3

`radius` Scalar

`capacity` [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetSharedVertexCatalog_Capacity"></a> Capacity

```csharp
public int Capacity { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetSharedVertexCatalog_TryCreate_VirtualGeometry_World_PlanetSharedVertexKey__System_UInt64_VirtualGeometry_World_PlanetSharedVertexCatalog_HeightQuery_VirtualizedGeometry_VirtualGeometrySharedVertex__"></a> TryCreate\(in PlanetSharedVertexKey, ulong, HeightQuery, out VirtualGeometrySharedVertex\)

```csharp
public bool TryCreate(in PlanetSharedVertexKey key, ulong revision, PlanetSharedVertexCatalog.HeightQuery query, out VirtualGeometrySharedVertex vertex)
```

#### 引数（Parameters）

`key` [PlanetSharedVertexKey](VirtualGeometry.World.PlanetSharedVertexKey.md)

`revision` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

`query` [PlanetSharedVertexCatalog](VirtualGeometry.World.PlanetSharedVertexCatalog.md).[HeightQuery](VirtualGeometry.World.PlanetSharedVertexCatalog.HeightQuery.md)

`vertex` [VirtualGeometrySharedVertex](VirtualizedGeometry.VirtualGeometrySharedVertex.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
