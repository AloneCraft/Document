# <a id="VirtualGeometry_World_PlanetGpuGenerationLeases"></a> Class PlanetGpuGenerationLeases

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

惑星GPU生成のslot書込み所有権。完了はGPU fence/readbackの後だけ渡す。
この型自身はGPU完了を観測せず、描画readyの変更やbufferの解放もしない。

```csharp
public sealed class PlanetGpuGenerationLeases
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetGpuGenerationLeases](VirtualGeometry.World.PlanetGpuGenerationLeases.md)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetGpuGenerationLeases__ctor_System_Int32_System_UInt32_"></a> PlanetGpuGenerationLeases\(int, uint\)

```csharp
public PlanetGpuGenerationLeases(int capacity, uint poolEpoch)
```

#### 引数（Parameters）

`capacity` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`poolEpoch` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetGpuGenerationLeases_CanDisposeRetiredBuffers"></a> CanDisposeRetiredBuffers

```csharp
public bool CanDisposeRetiredBuffers { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetGpuGenerationLeases_CanStartGeneration"></a> CanStartGeneration

```csharp
public bool CanStartGeneration { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetGpuGenerationLeases_InFlightCount"></a> InFlightCount

```csharp
public int InFlightCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetGpuGenerationLeases_PoolEpoch"></a> PoolEpoch

```csharp
public uint PoolEpoch { get; }
```

#### 値（Property Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetGpuGenerationLeases_Cancel_System_Int32_"></a> Cancel\(int\)

要求を取消す。書込み中のslotは完了まで隔離し、予約を解放しない。

```csharp
public bool Cancel(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetGpuGenerationLeases_CompleteAfterFence_VirtualGeometry_World_PlanetGpuGenerationLease__VirtualGeometry_World_PlanetGpuGenerationResult__System_Int32_System_UInt32_System_Boolean_"></a> CompleteAfterFence\(in PlanetGpuGenerationLease, in PlanetGpuGenerationResult, int, uint, bool\)

正常readback後の完了。結果の世代・status・boundsが有効な場合だけ公開を返す。

```csharp
public PlanetGpuGenerationCompletion CompleteAfterFence(in PlanetGpuGenerationLease lease, in PlanetGpuGenerationResult result, int currentVersion, uint currentEpoch, bool contactNow)
```

#### 引数（Parameters）

`lease` [PlanetGpuGenerationLease](VirtualGeometry.World.PlanetGpuGenerationLease.md)

`result` [PlanetGpuGenerationResult](VirtualGeometry.World.PlanetGpuGenerationResult.md)

`currentVersion` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`currentEpoch` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`contactNow` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [PlanetGpuGenerationCompletion](VirtualGeometry.World.PlanetGpuGenerationCompletion.md)

### <a id="VirtualGeometry_World_PlanetGpuGenerationLeases_FailedAfterFence_VirtualGeometry_World_PlanetGpuGenerationLease__System_Int32_System_UInt32_System_Boolean_"></a> FailedAfterFence\(in PlanetGpuGenerationLease, int, uint, bool\)

readback自体の失敗も、GPU書込み完了が確定した後でだけ渡す。現役の要求は再試行へ残す。

```csharp
public PlanetGpuGenerationCompletion FailedAfterFence(in PlanetGpuGenerationLease lease, int currentVersion, uint currentEpoch, bool contactNow)
```

#### 引数（Parameters）

`lease` [PlanetGpuGenerationLease](VirtualGeometry.World.PlanetGpuGenerationLease.md)

`currentVersion` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`currentEpoch` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`contactNow` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [PlanetGpuGenerationCompletion](VirtualGeometry.World.PlanetGpuGenerationCompletion.md)

### <a id="VirtualGeometry_World_PlanetGpuGenerationLeases_IsInFlight_System_Int32_"></a> IsInFlight\(int\)

```csharp
public bool IsInFlight(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetGpuGenerationLeases_RequireCpu_System_Int32_"></a> RequireCpu\(int\)

生成中に接地が入ったことを記録する。GPU成功でもCPUの正本を用意する。

```csharp
public bool RequireCpu(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetGpuGenerationLeases_Retire_System_Action_"></a> Retire\(Action\)

```csharp
public void Retire(Action releaseAfterWriters = null)
```

#### 引数（Parameters）

`releaseAfterWriters` [Action](https://learn.microsoft.com/dotnet/api/system.action)

### <a id="VirtualGeometry_World_PlanetGpuGenerationLeases_TryBegin_System_Int32_System_Int32_System_Boolean_System_Boolean_VirtualGeometry_World_PlanetGpuGenerationLease__"></a> TryBegin\(int, int, bool, bool, out PlanetGpuGenerationLease\)

未ready・非接地のslotだけを予約する。呼出し側はslotの割当とversionの正本を保持する。

```csharp
public bool TryBegin(int slot, int version, bool currentlyReady, bool contactProtected, out PlanetGpuGenerationLease lease)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`version` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`currentlyReady` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`contactProtected` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`lease` [PlanetGpuGenerationLease](VirtualGeometry.World.PlanetGpuGenerationLease.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
