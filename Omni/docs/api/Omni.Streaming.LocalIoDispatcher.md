# <a id="Omni_Streaming_LocalIoDispatcher"></a> Class LocalIoDispatcher

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

ローカルI/O専用。全session共通で最大1本、queueは最大64件。待機中はthreadを占有しない。

```csharp
public sealed class LocalIoDispatcher
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[LocalIoDispatcher](Omni.Streaming.LocalIoDispatcher.md)

## フィールド（Fields）

### <a id="Omni_Streaming_LocalIoDispatcher_Shared"></a> Shared

```csharp
public static readonly LocalIoDispatcher Shared
```

#### 値（Field Value）

 [LocalIoDispatcher](Omni.Streaming.LocalIoDispatcher.md)

## プロパティ（Properties）

### <a id="Omni_Streaming_LocalIoDispatcher_ActiveWorkers"></a> ActiveWorkers

```csharp
public static int ActiveWorkers { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_LocalIoDispatcher_CompletedOperations"></a> CompletedOperations

```csharp
public static long CompletedOperations { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Streaming_LocalIoDispatcher_FailedOperations"></a> FailedOperations

```csharp
public static long FailedOperations { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Streaming_LocalIoDispatcher_PeakReservedBytes"></a> PeakReservedBytes

```csharp
public static long PeakReservedBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Streaming_LocalIoDispatcher_ReservedBytes"></a> ReservedBytes

```csharp
public static long ReservedBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Streaming_LocalIoDispatcher_SkippedCacheWrites"></a> SkippedCacheWrites

```csharp
public static long SkippedCacheWrites { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

## メソッド（Methods）

### <a id="Omni_Streaming_LocalIoDispatcher_ResetPeak"></a> ResetPeak\(\)

```csharp
public static void ResetPeak()
```
