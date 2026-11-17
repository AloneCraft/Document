# <a id="VirtualGeometry_World_PlanetTriangleSoup"></a> Class PlanetTriangleSoup

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

三角形の集まり(頂点と、3 つずつの頂点番号)。

```csharp
public sealed class PlanetTriangleSoup
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetTriangleSoup](VirtualGeometry.World.PlanetTriangleSoup.md)

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetTriangleSoup_Indices"></a> Indices

```csharp
public readonly List<int> Indices
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[int](https://learn.microsoft.com/dotnet/api/system.int32)\>

### <a id="VirtualGeometry_World_PlanetTriangleSoup_Vertices"></a> Vertices

```csharp
public readonly List<PlanetDouble3> Vertices
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)\>

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetTriangleSoup_TriangleCount"></a> TriangleCount

```csharp
public int TriangleCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetTriangleSoup_AddTriangle_System_Int32_System_Int32_System_Int32_"></a> AddTriangle\(int, int, int\)

```csharp
public void AddTriangle(int a, int b, int c)
```

#### 引数（Parameters）

`a` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`b` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`c` [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetTriangleSoup_AddVertex_VirtualGeometry_World_PlanetDouble3_"></a> AddVertex\(PlanetDouble3\)

```csharp
public int AddVertex(PlanetDouble3 v)
```

#### 引数（Parameters）

`v` [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetTriangleSoup_Clear"></a> Clear\(\)

```csharp
public void Clear()
```
