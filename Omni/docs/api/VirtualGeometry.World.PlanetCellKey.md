# <a id="VirtualGeometry_World_PlanetCellKey"></a> Struct PlanetCellKey

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

cube-sphere の四分木の1つの Cell(面、階層、格子番号)。

```csharp
public readonly struct PlanetCellKey : IEquatable<PlanetCellKey>
```

#### 実装するインターフェース（Implements）

[IEquatable<PlanetCellKey\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetCellKey__ctor_System_Int32_System_Int32_VirtualGeometry_World_PlanetCellCoordinate_VirtualGeometry_World_PlanetCellCoordinate_"></a> PlanetCellKey\(int, int, PlanetCellCoordinate, PlanetCellCoordinate\)

```csharp
public PlanetCellKey(int face, int level, PlanetCellCoordinate x, PlanetCellCoordinate y)
```

#### 引数（Parameters）

`face` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`x` [PlanetCellCoordinate](VirtualGeometry.World.PlanetCellCoordinate.md)

`y` [PlanetCellCoordinate](VirtualGeometry.World.PlanetCellCoordinate.md)

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetCellKey_DirectionCount"></a> DirectionCount

同じ階層の隣の向き。0:−u(x−1)、1:+u(x+1)、2:−v(y−1)、3:+v(y+1)。

```csharp
public const int DirectionCount = 4
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetCellKey_Face"></a> Face

```csharp
public readonly int Face
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetCellKey_Level"></a> Level

```csharp
public readonly int Level
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetCellKey_X"></a> X

```csharp
public readonly PlanetCellCoordinate X
```

#### 値（Field Value）

 [PlanetCellCoordinate](VirtualGeometry.World.PlanetCellCoordinate.md)

### <a id="VirtualGeometry_World_PlanetCellKey_Y"></a> Y

```csharp
public readonly PlanetCellCoordinate Y
```

#### 値（Field Value）

 [PlanetCellCoordinate](VirtualGeometry.World.PlanetCellCoordinate.md)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetCellKey_ChildIndex"></a> ChildIndex

この Cell が親の何番目の子か(0〜3)。

```csharp
public int ChildIndex { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetCellKey_Child_System_Int32_"></a> Child\(int\)

子(index は 0〜3。bit0 が x、bit1 が y)。

```csharp
public PlanetCellKey Child(int index)
```

#### 引数（Parameters）

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

### <a id="VirtualGeometry_World_PlanetCellKey_Contains_VirtualGeometry_World_PlanetCellKey__"></a> Contains\(in PlanetCellKey\)

この Cell の範囲が other の範囲を含むか(other が自分か子孫)。

```csharp
public bool Contains(in PlanetCellKey other)
```

#### 引数（Parameters）

`other` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetCellKey_Equals_VirtualGeometry_World_PlanetCellKey_"></a> Equals\(PlanetCellKey\)

```csharp
public bool Equals(PlanetCellKey other)
```

#### 引数（Parameters）

`other` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetCellKey_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object obj)
```

#### 引数（Parameters）

`obj` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetCellKey_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetCellKey_Neighbor_System_Int32_"></a> Neighbor\(int\)

同じ階層の隣の Cell。面の境界をまたぐときは、隣の面の格子番号へ整数で写す(浮動小数の誤差を持ち込まない)。
面 f の辺の点は n_f ± u_f + b·v_f(または n_f + a·u_f ± v_f)。隣の面 g は法線がその ±u_f(±v_f)の面で、
g の座標は、n_f の成分が g の辺(±1)に、辺に沿った成分(b または a)が g のもう一方の座標(±)になる。

```csharp
public PlanetCellKey Neighbor(int direction)
```

#### 引数（Parameters）

`direction` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

### <a id="VirtualGeometry_World_PlanetCellKey_Parent"></a> Parent\(\)

```csharp
public PlanetCellKey Parent()
```

#### 戻り値（Returns）

 [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

### <a id="VirtualGeometry_World_PlanetCellKey_Root_System_Int32_"></a> Root\(int\)

```csharp
public static PlanetCellKey Root(int face)
```

#### 引数（Parameters）

`face` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

### <a id="VirtualGeometry_World_PlanetCellKey_ToString"></a> ToString\(\)

```csharp
public override string ToString()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
