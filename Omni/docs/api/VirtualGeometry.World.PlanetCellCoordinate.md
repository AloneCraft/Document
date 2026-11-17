# <a id="VirtualGeometry_World_PlanetCellCoordinate"></a> Struct PlanetCellCoordinate

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

cube-sphere の1つの面の上の、Cell の格子番号(0〜2^階層−1)。96ビットの符号なし整数。
10^20 m の天体を 1mm まで分けると約77段になり、64ビットでは足りないため。

```csharp
public readonly struct PlanetCellCoordinate : IEquatable<PlanetCellCoordinate>
```

#### 実装するインターフェース（Implements）

[IEquatable<PlanetCellCoordinate\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetCellCoordinate__ctor_System_UInt64_System_UInt32_"></a> PlanetCellCoordinate\(ulong, uint\)

```csharp
public PlanetCellCoordinate(ulong low, uint high)
```

#### 引数（Parameters）

`low` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

`high` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetCellCoordinate_Bits"></a> Bits

```csharp
public const int Bits = 96
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetCellCoordinate_High"></a> High

```csharp
public readonly uint High
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualGeometry_World_PlanetCellCoordinate_Low"></a> Low

```csharp
public readonly ulong Low
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetCellCoordinate_IsZero"></a> IsZero

```csharp
public bool IsZero { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetCellCoordinate_LowestBit"></a> LowestBit

最下位ビット(子のどちら側か)。

```csharp
public int LowestBit { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetCellCoordinate_Zero"></a> Zero

```csharp
public static PlanetCellCoordinate Zero { get; }
```

#### 値（Property Value）

 [PlanetCellCoordinate](VirtualGeometry.World.PlanetCellCoordinate.md)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetCellCoordinate_Child_System_Int32_"></a> Child\(int\)

1つ細かい階層の番号(2倍+bit)。

```csharp
public PlanetCellCoordinate Child(int bit)
```

#### 引数（Parameters）

`bit` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [PlanetCellCoordinate](VirtualGeometry.World.PlanetCellCoordinate.md)

### <a id="VirtualGeometry_World_PlanetCellCoordinate_Complement_System_Int32_"></a> Complement\(int\)

同じ階層で反対側から数えた番号(2^level−1−this)。

```csharp
public PlanetCellCoordinate Complement(int level)
```

#### 引数（Parameters）

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [PlanetCellCoordinate](VirtualGeometry.World.PlanetCellCoordinate.md)

### <a id="VirtualGeometry_World_PlanetCellCoordinate_Decrement"></a> Decrement\(\)

```csharp
public PlanetCellCoordinate Decrement()
```

#### 戻り値（Returns）

 [PlanetCellCoordinate](VirtualGeometry.World.PlanetCellCoordinate.md)

### <a id="VirtualGeometry_World_PlanetCellCoordinate_Equals_VirtualGeometry_World_PlanetCellCoordinate_"></a> Equals\(PlanetCellCoordinate\)

```csharp
public bool Equals(PlanetCellCoordinate other)
```

#### 引数（Parameters）

`other` [PlanetCellCoordinate](VirtualGeometry.World.PlanetCellCoordinate.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetCellCoordinate_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object obj)
```

#### 引数（Parameters）

`obj` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetCellCoordinate_Fraction_System_Int32_"></a> Fraction\(int\)

this/2^level を float で近似する。CPU の Cell の選択の幾何に使う(細かい階層では精度が落ちる)。

```csharp
public float Fraction(int level)
```

#### 引数（Parameters）

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetCellCoordinate_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetCellCoordinate_Increment"></a> Increment\(\)

```csharp
public PlanetCellCoordinate Increment()
```

#### 戻り値（Returns）

 [PlanetCellCoordinate](VirtualGeometry.World.PlanetCellCoordinate.md)

### <a id="VirtualGeometry_World_PlanetCellCoordinate_IsWithin_System_Int32_"></a> IsWithin\(int\)

この階層で表せる範囲(0〜2^level−1)にあるか。

```csharp
public bool IsWithin(int level)
```

#### 引数（Parameters）

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetCellCoordinate_Last_System_Int32_"></a> Last\(int\)

2^level−1(その階層の最後の番号)。

```csharp
public static PlanetCellCoordinate Last(int level)
```

#### 引数（Parameters）

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [PlanetCellCoordinate](VirtualGeometry.World.PlanetCellCoordinate.md)

### <a id="VirtualGeometry_World_PlanetCellCoordinate_Parent"></a> Parent\(\)

1つ粗い階層の番号(半分)。

```csharp
public PlanetCellCoordinate Parent()
```

#### 戻り値（Returns）

 [PlanetCellCoordinate](VirtualGeometry.World.PlanetCellCoordinate.md)

### <a id="VirtualGeometry_World_PlanetCellCoordinate_ToString"></a> ToString\(\)

```csharp
public override string ToString()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
