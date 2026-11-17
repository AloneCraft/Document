# <a id="VirtualGeometry_World_PlanetTerrainVertexPool"></a> Class PlanetTerrainVertexPool

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

惑星の共有index用の混合pool。接地のCPU正本を保持し、保護から外れた32 B領域を再利用する。

```csharp
public sealed class PlanetTerrainVertexPool : IDisposable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetTerrainVertexPool](VirtualGeometry.World.PlanetTerrainVertexPool.md)

#### 実装するインターフェース（Implements）

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetTerrainVertexPool__ctor_System_Int32_System_Int32_System_Int32_System_Int64_"></a> PlanetTerrainVertexPool\(int, int, int, long\)

```csharp
public PlanetTerrainVertexPool(int n, int capacity, int exactCapacity, long maximumStorageBytes)
```

#### 引数（Parameters）

`n` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`capacity` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`exactCapacity` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`maximumStorageBytes` [long](https://learn.microsoft.com/dotnet/api/system.int64)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetTerrainVertexPool_Capacity"></a> Capacity

```csharp
public int Capacity { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetTerrainVertexPool_ExactCapacity"></a> ExactCapacity

```csharp
public int ExactCapacity { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetTerrainVertexPool_ExactCpuBytes"></a> ExactCpuBytes

```csharp
public long ExactCpuBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualGeometry_World_PlanetTerrainVertexPool_ExactUsed"></a> ExactUsed

```csharp
public int ExactUsed { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetTerrainVertexPool_GpuBytes"></a> GpuBytes

```csharp
public long GpuBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualGeometry_World_PlanetTerrainVertexPool_GridQuads"></a> GridQuads

```csharp
public int GridQuads { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetTerrainVertexPool_Records"></a> Records

```csharp
public GraphicsBuffer Records { get; }
```

#### 値（Property Value）

 GraphicsBuffer

### <a id="VirtualGeometry_World_PlanetTerrainVertexPool_SlotVertices"></a> SlotVertices

```csharp
public int SlotVertices { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetTerrainVertexPool_WordCount"></a> WordCount

```csharp
public int WordCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetTerrainVertexPool_Words"></a> Words

```csharp
public GraphicsBuffer Words { get; }
```

#### 値（Property Value）

 GraphicsBuffer

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetTerrainVertexPool_Dispose"></a> Dispose\(\)

```csharp
public void Dispose()
```

### <a id="VirtualGeometry_World_PlanetTerrainVertexPool_IsExact_System_Int32_"></a> IsExact\(int\)

```csharp
public bool IsExact(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetTerrainVertexPool_QuantizationPadding_System_Int32_"></a> QuantizationPadding\(int\)

量子化半刻みだけでなくfloat復元の丸めも囲む余裕。exactを後で圧縮する場合にも使う。

```csharp
public float QuantizationPadding(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetTerrainVertexPool_Readback_System_Int32_"></a> Readback\(int\)

検証用の同期readback。32 B領域は位置・法線・UVを元のbitで返す。

```csharp
public VirtualGeometryPackedVertex[] Readback(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [VirtualGeometryPackedVertex](VirtualizedGeometry.VirtualGeometryPackedVertex.md)\[\]

### <a id="VirtualGeometry_World_PlanetTerrainVertexPool_Release_System_Int32_"></a> Release\(int\)

```csharp
public void Release(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetTerrainVertexPool_ResolveCapacity_System_Int32_System_Int32_System_Int32_System_Int64_"></a> ResolveCapacity\(int, int, int, long\)

単一word bindingの上限からlogical slot数を決める。接地別枠も同じbindingへ含める。

```csharp
public static int ResolveCapacity(int wanted, int n, int exactSlots, long maximumBytes)
```

#### 引数（Parameters）

`wanted` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`n` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`exactSlots` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`maximumBytes` [long](https://learn.microsoft.com/dotnet/api/system.int64)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetTerrainVertexPool_TryAcceptGpuRecord_System_Int32_VirtualGeometry_World_PlanetTerrainStorageRecord__System_UInt32_System_UInt32_UnityEngine_Vector4_System_String__"></a> TryAcceptGpuRecord\(int, in PlanetTerrainStorageRecord, uint, uint, Vector4, out string\)

生成→圧縮の完了後だけCPU側のrecordを受理する。bufferの再uploadや同期readbackはしない。

```csharp
public bool TryAcceptGpuRecord(int slot, in PlanetTerrainStorageRecord record, uint version, uint epoch, Vector4 faceRange, out string reason)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`record` [PlanetTerrainStorageRecord](VirtualGeometry.World.PlanetTerrainStorageRecord.md)

`version` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`epoch` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`faceRange` Vector4

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetTerrainVertexPool_TryDemoteOne_System_Func_System_Int32_System_Boolean__"></a> TryDemoteOne\(Func<int, bool\>\)

接地から外れた32 BのCPU正本を圧縮して枠を返す。通常frameのGPU同期読取りは不要。

```csharp
public bool TryDemoteOne(Func<int, bool> mustRemainExact)
```

#### 引数（Parameters）

`mustRemainExact` [Func](https://learn.microsoft.com/dotnet/api/system.func\-2)<[int](https://learn.microsoft.com/dotnet/api/system.int32), [bool](https://learn.microsoft.com/dotnet/api/system.boolean)\>

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetTerrainVertexPool_TryStore_System_Int32_VirtualizedGeometry_VirtualGeometryPackedVertex___System_Boolean_UnityEngine_Vector4_System_UInt32_VirtualizedGeometry_VirtualGeometryPackedVertex____System_String__"></a> TryStore\(int, VirtualGeometryPackedVertex\[\], bool, Vector4, uint, out VirtualGeometryPackedVertex\[\], out string\)

全入力の検査後にuploadする。falseでは既存のreadyデータと割当を変更しない。

```csharp
public bool TryStore(int slot, VirtualGeometryPackedVertex[] input, bool exact, Vector4 faceRange, uint version, out VirtualGeometryPackedVertex[] stored, out string reason)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`input` [VirtualGeometryPackedVertex](VirtualizedGeometry.VirtualGeometryPackedVertex.md)\[\]

`exact` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`faceRange` Vector4

`version` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`stored` [VirtualGeometryPackedVertex](VirtualizedGeometry.VirtualGeometryPackedVertex.md)\[\]

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
