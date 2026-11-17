# <a id="Omni_OmniVirtualShadowTiles_Tile"></a> Struct OmniVirtualShadowTiles.Tile

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

タイル。X・Y はタイルの格子の番号(ページの番号 ÷ TilePages の切り捨て)。Start から Count 個が、並べ替えた一覧の中のこのタイルのページ。

```csharp
public readonly struct OmniVirtualShadowTiles.Tile
```

## コンストラクター（Constructors）

### <a id="Omni_OmniVirtualShadowTiles_Tile__ctor_System_Int32_System_Int64_System_Int64_System_Int32_System_Int32_"></a> Tile\(int, long, long, int, int\)

```csharp
public Tile(int level, long x, long y, int start, int count)
```

#### 引数（Parameters）

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`x` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`y` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`start` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`count` [int](https://learn.microsoft.com/dotnet/api/system.int32)

## フィールド（Fields）

### <a id="Omni_OmniVirtualShadowTiles_Tile_Count"></a> Count

```csharp
public readonly int Count
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_OmniVirtualShadowTiles_Tile_Level"></a> Level

```csharp
public readonly int Level
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_OmniVirtualShadowTiles_Tile_Start"></a> Start

```csharp
public readonly int Start
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_OmniVirtualShadowTiles_Tile_X"></a> X

```csharp
public readonly long X
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_OmniVirtualShadowTiles_Tile_Y"></a> Y

```csharp
public readonly long Y
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)
