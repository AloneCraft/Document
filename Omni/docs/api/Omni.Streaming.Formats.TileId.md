# <a id="Omni_Streaming_Formats_TileId"></a> Class TileId

Namespace: [Omni.Streaming.Formats](Omni.Streaming.Formats.md)  
Assembly: Omni.Streaming.Formats.dll  

四分木のマスを、階層をまたいだ1本の整数 ID にする(PMTiles v3 と同じ考え方): 階層 L のマスは、
階層 0〜L−1 のマスの総数 (4^L−1)/3 に、その階層内の Hilbert 順の位置を足した値。ID が連続するマスは、空間でも近い。

```csharp
public static class TileId
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[TileId](Omni.Streaming.Formats.TileId.md)

## メソッド（Methods）

### <a id="Omni_Streaming_Formats_TileId_FromId_System_UInt64_System_Int32__System_UInt32__System_UInt32__"></a> FromId\(ulong, out int, out uint, out uint\)

```csharp
public static void FromId(ulong id, out int level, out uint x, out uint y)
```

#### 引数（Parameters）

`id` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`x` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`y` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="Omni_Streaming_Formats_TileId_LevelOffset_System_Int32_"></a> LevelOffset\(int\)

```csharp
public static ulong LevelOffset(int level)
```

#### 引数（Parameters）

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Streaming_Formats_TileId_ToId_System_Int32_System_UInt32_System_UInt32_"></a> ToId\(int, uint, uint\)

```csharp
public static ulong ToId(int level, uint x, uint y)
```

#### 引数（Parameters）

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`x` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`y` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

#### 戻り値（Returns）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)
