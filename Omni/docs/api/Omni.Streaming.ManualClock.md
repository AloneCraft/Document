# <a id="Omni_Streaming_ManualClock"></a> Class ManualClock

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

テスト・再現用の手動の時計。

```csharp
public sealed class ManualClock : IClock
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[ManualClock](Omni.Streaming.ManualClock.md)

#### 実装するインターフェース（Implements）

[IClock](Omni.Streaming.IClock.md)

## プロパティ（Properties）

### <a id="Omni_Streaming_ManualClock_Ticks"></a> Ticks

```csharp
public long Ticks { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Streaming_ManualClock_TicksPerSecond"></a> TicksPerSecond

```csharp
public long TicksPerSecond { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

## メソッド（Methods）

### <a id="Omni_Streaming_ManualClock_AdvanceMilliseconds_System_Double_"></a> AdvanceMilliseconds\(double\)

```csharp
public void AdvanceMilliseconds(double milliseconds)
```

#### 引数（Parameters）

`milliseconds` [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Streaming_ManualClock_AdvanceSeconds_System_Double_"></a> AdvanceSeconds\(double\)

```csharp
public void AdvanceSeconds(double seconds)
```

#### 引数（Parameters）

`seconds` [double](https://learn.microsoft.com/dotnet/api/system.double)
