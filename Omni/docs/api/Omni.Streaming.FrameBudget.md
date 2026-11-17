# <a id="Omni_Streaming_FrameBudget"></a> Struct FrameBudget

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

1回のTickでデコードを追加開始するCPU時間と件数の目安。開始済み1件は中断しない。取得・検証・store・関心処理を含むTick全体の上限ではない。

```csharp
public readonly struct FrameBudget
```

## コンストラクター（Constructors）

### <a id="Omni_Streaming_FrameBudget__ctor_System_Double_System_Int32_"></a> FrameBudget\(double, int\)

```csharp
public FrameBudget(double cpuMilliseconds, int maximumDecodes = 2147483647)
```

#### 引数（Parameters）

`cpuMilliseconds` [double](https://learn.microsoft.com/dotnet/api/system.double)

`maximumDecodes` [int](https://learn.microsoft.com/dotnet/api/system.int32)

## フィールド（Fields）

### <a id="Omni_Streaming_FrameBudget_CpuMilliseconds"></a> CpuMilliseconds

```csharp
public readonly double CpuMilliseconds
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Streaming_FrameBudget_MaximumDecodes"></a> MaximumDecodes

```csharp
public readonly int MaximumDecodes
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="Omni_Streaming_FrameBudget_Unlimited"></a> Unlimited

```csharp
public static FrameBudget Unlimited { get; }
```

#### 値（Property Value）

 [FrameBudget](Omni.Streaming.FrameBudget.md)
