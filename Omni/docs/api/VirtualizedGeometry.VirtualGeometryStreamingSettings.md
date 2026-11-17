# <a id="VirtualizedGeometry_VirtualGeometryStreamingSettings"></a> Class VirtualGeometryStreamingSettings

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

M4の独立予算。上限を実行時に自動拡大しない。

```csharp
[Serializable]
public sealed class VirtualGeometryStreamingSettings
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryStreamingSettings](VirtualizedGeometry.VirtualGeometryStreamingSettings.md)

## フィールド（Fields）

### <a id="VirtualizedGeometry_VirtualGeometryStreamingSettings_CpuCacheBudgetBytes"></a> CpuCacheBudgetBytes

```csharp
[Tooltip("読み込んだpageをCPU側に保持する上限(byte)。")]
public long CpuCacheBudgetBytes
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualizedGeometry_VirtualGeometryStreamingSettings_GpuGeometryBudgetBytes"></a> GpuGeometryBudgetBytes

```csharp
[Tooltip("GPUに置くgeometryの上限(byte)。同じassetを使うinstance間で共有します。")]
public long GpuGeometryBudgetBytes
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualizedGeometry_VirtualGeometryStreamingSettings_IoConcurrency"></a> IoConcurrency

```csharp
[Tooltip("同時に読み込むpage数。")]
public int IoConcurrency
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryStreamingSettings_IoDelayMilliseconds"></a> IoDelayMilliseconds

```csharp
public int IoDelayMilliseconds
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryStreamingSettings_RequestQueueCapacity"></a> RequestQueueCapacity

```csharp
[Tooltip("読み込み待ちの要求の上限。")]
public int RequestQueueCapacity
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryStreamingSettings_RequestTimeoutFrames"></a> RequestTimeoutFrames

```csharp
[Tooltip("要求されなくなったpageの読み込みを取り消すまでのframe数。")]
public int RequestTimeoutFrames
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryStreamingSettings_TransferBytesPerFrame"></a> TransferBytesPerFrame

```csharp
[Tooltip("1 frameにGPUへ転送する量の上限(byte)。")]
public int TransferBytesPerFrame
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometryStreamingSettings_Clone"></a> Clone\(\)

```csharp
public VirtualGeometryStreamingSettings Clone()
```

#### 戻り値（Returns）

 [VirtualGeometryStreamingSettings](VirtualizedGeometry.VirtualGeometryStreamingSettings.md)
