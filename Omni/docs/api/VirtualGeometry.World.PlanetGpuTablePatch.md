# <a id="VirtualGeometry_World_PlanetGpuTablePatch"></a> Class PlanetGpuTablePatch

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

確定したrevisionの転送データ。作成後にproducerが更新しても内容は変わらない。

```csharp
public sealed class PlanetGpuTablePatch
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetGpuTablePatch](VirtualGeometry.World.PlanetGpuTablePatch.md)

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetGpuTablePatch_Count"></a> Count

```csharp
public readonly int Count
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetGpuTablePatch_FullUpload"></a> FullUpload

```csharp
public readonly bool FullUpload
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetGpuTablePatch_MaximumProbeLength"></a> MaximumProbeLength

```csharp
public readonly int MaximumProbeLength
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetGpuTablePatch_Revision"></a> Revision

```csharp
public readonly long Revision
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetGpuTablePatch_Entries"></a> Entries

```csharp
public ReadOnlySpan<PlanetGpuResidentEntry> Entries { get; }
```

#### 値（Property Value）

 [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[PlanetGpuResidentEntry](VirtualGeometry.World.PlanetGpuResidentEntry.md)\>

### <a id="VirtualGeometry_World_PlanetGpuTablePatch_Indices"></a> Indices

```csharp
public ReadOnlySpan<int> Indices { get; }
```

#### 値（Property Value）

 [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[int](https://learn.microsoft.com/dotnet/api/system.int32)\>

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetGpuTablePatch_CreateScatterEntries"></a> CreateScatterEntries\(\)

1回の転送とGPU scatterに使うpacket。実運用のarray再利用とfenceはcontroller側で扱う。

```csharp
public PlanetGpuResidentPatchEntry[] CreateScatterEntries()
```

#### 戻り値（Returns）

 [PlanetGpuResidentPatchEntry](VirtualGeometry.World.PlanetGpuResidentPatchEntry.md)\[\]
