# <a id="VirtualGeometry_World_PlanetGpuGenerationDispatch"></a> Class PlanetGpuGenerationDispatch

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

1 batchの入力を所有し、同じgraphics queueの生成→readback後にだけslot所有者へ結果を渡す。

```csharp
public sealed class PlanetGpuGenerationDispatch
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetGpuGenerationDispatch](VirtualGeometry.World.PlanetGpuGenerationDispatch.md)

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetGpuGenerationDispatch_MaximumPackedBatchCells"></a> MaximumPackedBatchCells

```csharp
public const int MaximumPackedBatchCells = 256
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetGpuGenerationDispatch_ActiveBatches"></a> ActiveBatches

```csharp
public static int ActiveBatches { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetGpuGenerationDispatch_ScratchVertexBytes"></a> ScratchVertexBytes

```csharp
public long ScratchVertexBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualGeometry_World_PlanetGpuGenerationDispatch_SubmissionError"></a> SubmissionError

```csharp
public string SubmissionError { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetGpuGenerationDispatch_Submit_UnityEngine_ComputeShader_UnityEngine_GraphicsBuffer_UnityEngine_GraphicsBuffer_System_Int32_System_Int32_VirtualGeometry_World_PlanetGpuGenerationTask___VirtualGeometry_World_PlanetGpuCubicPatch___VirtualGeometry_World_PlanetGpuGenerationOctave___System_Action_System_Int32_VirtualGeometry_World_PlanetGpuGenerationResult_System_Boolean__VirtualGeometry_World_PlanetTerrainVertexPool_"></a> Submit\(ComputeShader, GraphicsBuffer, GraphicsBuffer, int, int, PlanetGpuGenerationTask\[\], PlanetGpuCubicPatch\[\], PlanetGpuGenerationOctave\[\], Action<int, PlanetGpuGenerationResult, bool\>, PlanetTerrainVertexPool\)

完了callbackは取消やsource無効化後も必要。throwはqueue投入前に限り、呼出し側は未投入leaseを返せる。
queue投入APIの例外では追加readbackをqueue末尾へ置き、完了までbufferを保持する。

```csharp
public static PlanetGpuGenerationDispatch Submit(ComputeShader shader, GraphicsBuffer vertices, GraphicsBuffer bounds, int n, int pool, PlanetGpuGenerationTask[] input, PlanetGpuCubicPatch[] basis, PlanetGpuGenerationOctave[] noise, Action<int, PlanetGpuGenerationResult, bool> complete, PlanetTerrainVertexPool packedPool = null)
```

#### 引数（Parameters）

`shader` ComputeShader

`vertices` GraphicsBuffer

`bounds` GraphicsBuffer

`n` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`pool` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`input` [PlanetGpuGenerationTask](VirtualGeometry.World.PlanetGpuGenerationTask.md)\[\]

`basis` [PlanetGpuCubicPatch](VirtualGeometry.World.PlanetGpuCubicPatch.md)\[\]

`noise` [PlanetGpuGenerationOctave](VirtualGeometry.World.PlanetGpuGenerationOctave.md)\[\]

`complete` [Action](https://learn.microsoft.com/dotnet/api/system.action\-3)<[int](https://learn.microsoft.com/dotnet/api/system.int32), [PlanetGpuGenerationResult](VirtualGeometry.World.PlanetGpuGenerationResult.md), [bool](https://learn.microsoft.com/dotnet/api/system.boolean)\>

`packedPool` [PlanetTerrainVertexPool](VirtualGeometry.World.PlanetTerrainVertexPool.md)

#### 戻り値（Returns）

 [PlanetGpuGenerationDispatch](VirtualGeometry.World.PlanetGpuGenerationDispatch.md)
