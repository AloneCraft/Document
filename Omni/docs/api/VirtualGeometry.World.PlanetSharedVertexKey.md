# <a id="VirtualGeometry_World_PlanetSharedVertexKey"></a> Struct PlanetSharedVertexKey

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

面IDを含まない、等角cubeのdyadic標本。面境界・角・異LODの同じ点は同じkeyへ正規化する。

```csharp
public readonly struct PlanetSharedVertexKey : IEquatable<PlanetSharedVertexKey>
```

#### 実装するインターフェース（Implements）

[IEquatable<PlanetSharedVertexKey\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1)

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetSharedVertexKey_Shift"></a> Shift

```csharp
public readonly int Shift
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetSharedVertexKey_X"></a> X

```csharp
public readonly BigInteger X
```

#### 値（Field Value）

 [BigInteger](https://learn.microsoft.com/dotnet/api/system.numerics.biginteger)

### <a id="VirtualGeometry_World_PlanetSharedVertexKey_Y"></a> Y

```csharp
public readonly BigInteger Y
```

#### 値（Field Value）

 [BigInteger](https://learn.microsoft.com/dotnet/api/system.numerics.biginteger)

### <a id="VirtualGeometry_World_PlanetSharedVertexKey_Z"></a> Z

```csharp
public readonly BigInteger Z
```

#### 値（Field Value）

 [BigInteger](https://learn.microsoft.com/dotnet/api/system.numerics.biginteger)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetSharedVertexKey_Create_VirtualGeometry_World_PlanetCellKey__System_Int32_System_Int32_System_Int32_"></a> Create\(in PlanetCellKey, int, int, int\)

```csharp
public static PlanetSharedVertexKey Create(in PlanetCellKey cell, int quads, int x, int y)
```

#### 引数（Parameters）

`cell` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

`quads` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`x` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`y` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [PlanetSharedVertexKey](VirtualGeometry.World.PlanetSharedVertexKey.md)

### <a id="VirtualGeometry_World_PlanetSharedVertexKey_Equals_VirtualGeometry_World_PlanetSharedVertexKey_"></a> Equals\(PlanetSharedVertexKey\)

```csharp
public bool Equals(PlanetSharedVertexKey other)
```

#### 引数（Parameters）

`other` [PlanetSharedVertexKey](VirtualGeometry.World.PlanetSharedVertexKey.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetSharedVertexKey_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object obj)
```

#### 引数（Parameters）

`obj` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetSharedVertexKey_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetSharedVertexKey_TryDirection_Omni_Logical_Vector3__"></a> TryDirection\(out Vector3\)

```csharp
public bool TryDirection(out Vector3 direction)
```

#### 引数（Parameters）

`direction` Vector3

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
