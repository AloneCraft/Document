# <a id="Omni_Streaming_SpatialOrder"></a> Class SpatialOrder

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

四分木の1マスの並び順。近いマスを連続させて、1回の範囲取得でまとめて取れるようにする(コンテナの並べ方)。

```csharp
public static class SpatialOrder
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[SpatialOrder](Omni.Streaming.SpatialOrder.md)

## メソッド（Methods）

### <a id="Omni_Streaming_SpatialOrder_Hilbert_System_Int32_System_UInt32_System_UInt32_"></a> Hilbert\(int, uint, uint\)

階層 level の格子 (x, y) の Hilbert 曲線上の位置(0〜4^level−1)。隣り合う位置は空間でも隣り合う。

```csharp
public static ulong Hilbert(int level, uint x, uint y)
```

#### 引数（Parameters）

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`x` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`y` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

#### 戻り値（Returns）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Streaming_SpatialOrder_InverseHilbert_System_Int32_System_UInt64_System_UInt32__System_UInt32__"></a> InverseHilbert\(int, ulong, out uint, out uint\)

Hilbert の位置から格子 (x, y) へ戻す。

```csharp
public static void InverseHilbert(int level, ulong d, out uint x, out uint y)
```

#### 引数（Parameters）

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`d` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

`x` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`y` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)
