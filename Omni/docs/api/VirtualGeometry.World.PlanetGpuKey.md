# <a id="VirtualGeometry_World_PlanetGpuKey"></a> Struct PlanetGpuKey

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

structured buffer用の96 bit×2座標。演算は32 bit wordで行い、floatへ変換しない。

```csharp
public readonly struct PlanetGpuKey : IEquatable<PlanetGpuKey>
```

#### 実装するインターフェース（Implements）

[IEquatable<PlanetGpuKey\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetGpuKey__ctor_System_UInt32_System_UInt32_System_UInt32_System_UInt32_System_UInt32_System_UInt32_System_UInt32_System_UInt32_"></a> PlanetGpuKey\(uint, uint, uint, uint, uint, uint, uint, uint\)

```csharp
public PlanetGpuKey(uint x0, uint x1, uint x2, uint y0, uint y1, uint y2, uint meta, uint reserved = 0)
```

#### 引数（Parameters）

`x0` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`x1` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`x2` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`y0` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`y1` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`y2` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`meta` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`reserved` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetGpuKey_Meta"></a> Meta

```csharp
public readonly uint Meta
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualGeometry_World_PlanetGpuKey_Reserved"></a> Reserved

```csharp
public readonly uint Reserved
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualGeometry_World_PlanetGpuKey_Stride"></a> Stride

```csharp
public const int Stride = 32
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetGpuKey_X0"></a> X0

```csharp
public readonly uint X0
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualGeometry_World_PlanetGpuKey_X1"></a> X1

```csharp
public readonly uint X1
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualGeometry_World_PlanetGpuKey_X2"></a> X2

```csharp
public readonly uint X2
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualGeometry_World_PlanetGpuKey_Y0"></a> Y0

```csharp
public readonly uint Y0
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualGeometry_World_PlanetGpuKey_Y1"></a> Y1

```csharp
public readonly uint Y1
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualGeometry_World_PlanetGpuKey_Y2"></a> Y2

```csharp
public readonly uint Y2
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetGpuKey_Face"></a> Face

```csharp
public int Face { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetGpuKey_IsCanonical"></a> IsCanonical

```csharp
public bool IsCanonical { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetGpuKey_Level"></a> Level

```csharp
public int Level { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetGpuKey_Child_System_Int32_"></a> Child\(int\)

```csharp
public PlanetGpuKey Child(int quadrant)
```

#### 引数（Parameters）

`quadrant` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [PlanetGpuKey](VirtualGeometry.World.PlanetGpuKey.md)

### <a id="VirtualGeometry_World_PlanetGpuKey_Contains_VirtualGeometry_World_PlanetGpuKey_"></a> Contains\(PlanetGpuKey\)

```csharp
public bool Contains(PlanetGpuKey other)
```

#### 引数（Parameters）

`other` [PlanetGpuKey](VirtualGeometry.World.PlanetGpuKey.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetGpuKey_Equals_VirtualGeometry_World_PlanetGpuKey_"></a> Equals\(PlanetGpuKey\)

```csharp
public bool Equals(PlanetGpuKey other)
```

#### 引数（Parameters）

`other` [PlanetGpuKey](VirtualGeometry.World.PlanetGpuKey.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetGpuKey_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object other)
```

#### 引数（Parameters）

`other` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetGpuKey_FromKey_VirtualGeometry_World_PlanetCellKey_"></a> FromKey\(PlanetCellKey\)

```csharp
public static PlanetGpuKey FromKey(PlanetCellKey key)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

#### 戻り値（Returns）

 [PlanetGpuKey](VirtualGeometry.World.PlanetGpuKey.md)

### <a id="VirtualGeometry_World_PlanetGpuKey_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetGpuKey_Hash32"></a> Hash32\(\)

```csharp
public uint Hash32()
```

#### 戻り値（Returns）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualGeometry_World_PlanetGpuKey_Parent"></a> Parent\(\)

```csharp
public PlanetGpuKey Parent()
```

#### 戻り値（Returns）

 [PlanetGpuKey](VirtualGeometry.World.PlanetGpuKey.md)

### <a id="VirtualGeometry_World_PlanetGpuKey_ToKey"></a> ToKey\(\)

```csharp
public PlanetCellKey ToKey()
```

#### 戻り値（Returns）

 [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)
