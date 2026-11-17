# <a id="Omni_Streaming_ImpairedByteSource"></a> Class ImpairedByteSource

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

取得元に、遅延・帯域・失敗率を加える(擬似回線)。時間は <xref href="Omni.Streaming.IClock" data-throw-if-not-resolved="false"></xref> で進むので、仮想時計で決定的に再現できる。
回線は1本として扱い、要求は到着順に帯域を分け合わず順に流れる(完了時刻 = max(開始+遅延, 回線が空く時刻) + 長さ/帯域)。
実際のデモの回線制限(遅い回線の再現)にも使える。

```csharp
public sealed class ImpairedByteSource : IByteSource
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[ImpairedByteSource](Omni.Streaming.ImpairedByteSource.md)

#### 実装するインターフェース（Implements）

[IByteSource](Omni.Streaming.IByteSource.md)

## コンストラクター（Constructors）

### <a id="Omni_Streaming_ImpairedByteSource__ctor_Omni_Streaming_IByteSource_Omni_Streaming_IClock_System_Int32_"></a> ImpairedByteSource\(IByteSource, IClock, int\)

```csharp
public ImpairedByteSource(IByteSource inner, IClock clock, int seed = 1)
```

#### 引数（Parameters）

`inner` [IByteSource](Omni.Streaming.IByteSource.md)

`clock` [IClock](Omni.Streaming.IClock.md)

`seed` [int](https://learn.microsoft.com/dotnet/api/system.int32)

## フィールド（Fields）

### <a id="Omni_Streaming_ImpairedByteSource_BytesPerSecond"></a> BytesPerSecond

帯域(byte/秒)。0 以下は無制限。

```csharp
public double BytesPerSecond
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Streaming_ImpairedByteSource_FailureRate"></a> FailureRate

要求ごとの失敗の確率(0〜1)。擬似乱数は seed で決まる。

```csharp
public double FailureRate
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Streaming_ImpairedByteSource_LatencySeconds"></a> LatencySeconds

要求から最初のバイトまでの遅延(秒)。

```csharp
public double LatencySeconds
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Streaming_ImpairedByteSource_Log"></a> Log

```csharp
public readonly List<ByteLocation> Log
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[ByteLocation](Omni.Streaming.ByteLocation.md)\>

## プロパティ（Properties）

### <a id="Omni_Streaming_ImpairedByteSource_CanceledCount"></a> CanceledCount

```csharp
public int CanceledCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_ImpairedByteSource_InFlight"></a> InFlight

```csharp
public int InFlight { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_ImpairedByteSource_Info"></a> Info

```csharp
public ByteSourceInfo Info { get; }
```

#### 値（Property Value）

 [ByteSourceInfo](Omni.Streaming.ByteSourceInfo.md)

### <a id="Omni_Streaming_ImpairedByteSource_MaximumInFlightSeen"></a> MaximumInFlightSeen

```csharp
public int MaximumInFlightSeen { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_Streaming_ImpairedByteSource_Begin_Omni_Streaming_ByteLocation__Omni_Streaming_BufferPool_"></a> Begin\(in ByteLocation, BufferPool\)

location の範囲の取得を始める。結果のバッファは pool から借りる。始められないときは例外ではなく、完了済みの失敗を返してもよい。

```csharp
public IByteRequest Begin(in ByteLocation location, BufferPool pool)
```

#### 引数（Parameters）

`location` [ByteLocation](Omni.Streaming.ByteLocation.md)

`pool` [BufferPool](Omni.Streaming.BufferPool.md)

#### 戻り値（Returns）

 [IByteRequest](Omni.Streaming.IByteRequest.md)

### <a id="Omni_Streaming_ImpairedByteSource_FailNext_System_Int32_"></a> FailNext\(int\)

次の n 回の要求を必ず失敗させる。

```csharp
public void FailNext(int count)
```

#### 引数（Parameters）

`count` [int](https://learn.microsoft.com/dotnet/api/system.int32)
