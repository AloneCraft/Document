# <a id="VirtualGeometry_World_PlanetGpuResidencyMirror"></a> Class PlanetGpuResidencyMirror

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

consumerごとに実Layerのresident/ready差分を保持する。1つの読取りが終わるまでGPU表を書き換えない。

```csharp
public sealed class PlanetGpuResidencyMirror : IDisposable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetGpuResidencyMirror](VirtualGeometry.World.PlanetGpuResidencyMirror.md)

#### 実装するインターフェース（Implements）

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetGpuResidencyMirror__ctor_System_Int32_System_UInt32_"></a> PlanetGpuResidencyMirror\(int, uint\)

```csharp
public PlanetGpuResidencyMirror(int poolCapacity, uint epoch)
```

#### 引数（Parameters）

`poolCapacity` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`epoch` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetGpuResidencyMirror_ActiveReadbacks"></a> ActiveReadbacks

```csharp
public static int ActiveReadbacks { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetGpuResidencyMirror_Epoch"></a> Epoch

```csharp
public uint Epoch { get; }
```

#### 値（Property Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualGeometry_World_PlanetGpuResidencyMirror_GpuBytes"></a> GpuBytes

```csharp
public long GpuBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualGeometry_World_PlanetGpuResidencyMirror_LastReadyPatchEntries"></a> LastReadyPatchEntries

```csharp
public int LastReadyPatchEntries { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetGpuResidencyMirror_LastTablePatchEntries"></a> LastTablePatchEntries

```csharp
public int LastTablePatchEntries { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetGpuResidencyMirror_Pending"></a> Pending

```csharp
public bool Pending { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetGpuResidencyMirror_PoolCapacity"></a> PoolCapacity

```csharp
public int PoolCapacity { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetGpuResidencyMirror_ResidentCount"></a> ResidentCount

```csharp
public int ResidentCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetGpuResidencyMirror_SubmissionError"></a> SubmissionError

```csharp
public string SubmissionError { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualGeometry_World_PlanetGpuResidencyMirror_TableCapacity"></a> TableCapacity

```csharp
public int TableCapacity { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetGpuResidencyMirror_Dispose"></a> Dispose\(\)

GPU読取り中のmirrorはcallbackまで資源を残す。

```csharp
public void Dispose()
```

### <a id="VirtualGeometry_World_PlanetGpuResidencyMirror_TryProbe_VirtualGeometry_World_PlanetGpuKey___System_Action_VirtualGeometry_World_PlanetGpuResidentProbeResult___System_String__System_String__"></a> TryProbe\(PlanetGpuKey\[\], Action<PlanetGpuResidentProbeResult\[\], string\>, out string\)

差分適用→lookup→小さなreadbackを同じqueueへ置く。callbackは取消後も1度呼び、callerのslot保護を返せるようにする。

```csharp
public bool TryProbe(PlanetGpuKey[] query, Action<PlanetGpuResidentProbeResult[], string> complete, out string reason)
```

#### 引数（Parameters）

`query` [PlanetGpuKey](VirtualGeometry.World.PlanetGpuKey.md)\[\]

`complete` [Action](https://learn.microsoft.com/dotnet/api/system.action\-2)<[PlanetGpuResidentProbeResult](VirtualGeometry.World.PlanetGpuResidentProbeResult.md)\[\], [string](https://learn.microsoft.com/dotnet/api/system.string)\>

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetGpuResidencyMirror_TryRefine_VirtualGeometry_World_PlanetGpuSelectionRoundInput_System_Action_VirtualGeometry_World_PlanetGpuSelectionRound_System_String__System_String__"></a> TryRefine\(PlanetGpuSelectionRoundInput, Action<PlanetGpuSelectionRound, string\>, out string\)

実snapshot上で誤差評価と分割1回を行う。描画cutへの公開はcontrollerが別に検証する。

```csharp
public bool TryRefine(PlanetGpuSelectionRoundInput input, Action<PlanetGpuSelectionRound, string> complete, out string reason)
```

#### 引数（Parameters）

`input` [PlanetGpuSelectionRoundInput](VirtualGeometry.World.PlanetGpuSelectionRoundInput.md)

`complete` [Action](https://learn.microsoft.com/dotnet/api/system.action\-2)<[PlanetGpuSelectionRound](VirtualGeometry.World.PlanetGpuSelectionRound.md), [string](https://learn.microsoft.com/dotnet/api/system.string)\>

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetGpuResidencyMirror_Update_System_Int32_VirtualGeometry_World_PlanetGpuKey_System_UInt32_System_Boolean_System_Boolean_"></a> Update\(int, PlanetGpuKey, uint, bool, bool\)

slotの変更だけを反映する。slotの再利用では先に古いkeyを削除し、ready世代も更新する。

```csharp
public void Update(int slot, PlanetGpuKey key, uint generation, bool isReady, bool assigned = true)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`key` [PlanetGpuKey](VirtualGeometry.World.PlanetGpuKey.md)

`generation` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`isReady` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`assigned` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
