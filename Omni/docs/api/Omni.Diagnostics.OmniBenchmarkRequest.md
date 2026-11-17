# <a id="Omni_Diagnostics_OmniBenchmarkRequest"></a> Struct OmniBenchmarkRequest

Namespace: [Omni.Diagnostics](Omni.Diagnostics.md)  
Assembly: Radial.Runtime.dll  

Runnerが計測開始前にシーンへ一度だけ渡す、不変のベンチマーク要求です。

```csharp
public readonly struct OmniBenchmarkRequest
```

## 補足（Remarks）

この値はコマンドラインを正規化したスナップショットです。Scene Controllerは
<xref href="Omni.Diagnostics.IOmniBenchmarkSceneController.TryPrepareBenchmark(Omni.Diagnostics.OmniBenchmarkRequest%2cOmni.Diagnostics.OmniBenchmarkSceneDescriptor%40%2cSystem.String%40)" data-throw-if-not-resolved="false"></xref>内でのみ適用し、
warmup以降に設定を変更してはなりません。

## コンストラクター（Constructors）

### <a id="Omni_Diagnostics_OmniBenchmarkRequest__ctor_System_String_Omni_Diagnostics_OmniBenchmarkKind_Omni_Diagnostics_OmniBenchmarkCullingMode_Omni_Diagnostics_OmniBenchmarkResidencyMode_System_Double_System_Boolean_System_Double_System_Double_System_Boolean_System_Int32_System_Int32_"></a> OmniBenchmarkRequest\(string, OmniBenchmarkKind, OmniBenchmarkCullingMode, OmniBenchmarkResidencyMode, double, bool, double, double, bool, int, int\)

不変のベンチマーク要求を作成します。

```csharp
public OmniBenchmarkRequest(string requestedScene, OmniBenchmarkKind benchmarkKind, OmniBenchmarkCullingMode cullingMode, OmniBenchmarkResidencyMode residencyMode, double sequenceTimeSeconds, bool hasSequenceTime, double streamingStartSequenceTimeSeconds, double streamingEndSequenceTimeSeconds, bool hasStreamingRange, int warmupFrames, int sampleFrames)
```

#### 引数（Parameters）

`requestedScene` [string](https://learn.microsoft.com/dotnet/api/system.string)

要求シーン名。nullは空文字列へ正規化します。

`benchmarkKind` [OmniBenchmarkKind](Omni.Diagnostics.OmniBenchmarkKind.md)

計測種別です。

`cullingMode` [OmniBenchmarkCullingMode](Omni.Diagnostics.OmniBenchmarkCullingMode.md)

カリング方式です。

`residencyMode` [OmniBenchmarkResidencyMode](Omni.Diagnostics.OmniBenchmarkResidencyMode.md)

常駐方式です。

`sequenceTimeSeconds` [double](https://learn.microsoft.com/dotnet/api/system.double)

固定評価時刻です。

`hasSequenceTime` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

固定評価時刻を使用する場合はtrueです。

`streamingStartSequenceTimeSeconds` [double](https://learn.microsoft.com/dotnet/api/system.double)

Streaming開始時刻です。

`streamingEndSequenceTimeSeconds` [double](https://learn.microsoft.com/dotnet/api/system.double)

Streaming終了時刻です。

`hasStreamingRange` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

Streaming時刻範囲を使用する場合はtrueです。

`warmupFrames` [int](https://learn.microsoft.com/dotnet/api/system.int32)

warmupフレーム数です。

`sampleFrames` [int](https://learn.microsoft.com/dotnet/api/system.int32)

採取フレーム数です。

## プロパティ（Properties）

### <a id="Omni_Diagnostics_OmniBenchmarkRequest_BenchmarkKind"></a> BenchmarkKind

測定種別です。

```csharp
public OmniBenchmarkKind BenchmarkKind { get; }
```

#### 値（Property Value）

 [OmniBenchmarkKind](Omni.Diagnostics.OmniBenchmarkKind.md)

### <a id="Omni_Diagnostics_OmniBenchmarkRequest_CullingMode"></a> CullingMode

比較対象となるカリング方式です。

```csharp
public OmniBenchmarkCullingMode CullingMode { get; }
```

#### 値（Property Value）

 [OmniBenchmarkCullingMode](Omni.Diagnostics.OmniBenchmarkCullingMode.md)

### <a id="Omni_Diagnostics_OmniBenchmarkRequest_HasSequenceTime"></a> HasSequenceTime

固定評価時刻が有限値として指定された場合にtrueです。

```csharp
public bool HasSequenceTime { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Diagnostics_OmniBenchmarkRequest_HasStreamingRange"></a> HasStreamingRange

有限かつ昇順のStreaming時刻範囲が指定された場合にtrueです。

```csharp
public bool HasStreamingRange { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Diagnostics_OmniBenchmarkRequest_IsDiagnosticOnly"></a> IsDiagnosticOnly

診断専用のカリング方式かを返します。

```csharp
public bool IsDiagnosticOnly { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Diagnostics_OmniBenchmarkRequest_RequestedScene"></a> RequestedScene

コマンドラインから要求されたシーン名です。

```csharp
public string RequestedScene { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Diagnostics_OmniBenchmarkRequest_ResidencyMode"></a> ResidencyMode

比較対象となる常駐方式です。

```csharp
public OmniBenchmarkResidencyMode ResidencyMode { get; }
```

#### 値（Property Value）

 [OmniBenchmarkResidencyMode](Omni.Diagnostics.OmniBenchmarkResidencyMode.md)

### <a id="Omni_Diagnostics_OmniBenchmarkRequest_SampleFrames"></a> SampleFrames

採取するフレーム数です。

```csharp
public int SampleFrames { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Diagnostics_OmniBenchmarkRequest_SequenceTimeSeconds"></a> SequenceTimeSeconds

固定評価時刻（秒）です。<xref href="Omni.Diagnostics.OmniBenchmarkRequest.HasSequenceTime" data-throw-if-not-resolved="false"></xref>がfalseなら未指定です。

```csharp
public double SequenceTimeSeconds { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Diagnostics_OmniBenchmarkRequest_StreamingEndSequenceTimeSeconds"></a> StreamingEndSequenceTimeSeconds

Streaming評価の終了時刻（秒）です。<xref href="Omni.Diagnostics.OmniBenchmarkRequest.HasStreamingRange" data-throw-if-not-resolved="false"></xref>がfalseなら未指定です。

```csharp
public double StreamingEndSequenceTimeSeconds { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Diagnostics_OmniBenchmarkRequest_StreamingStartSequenceTimeSeconds"></a> StreamingStartSequenceTimeSeconds

Streaming評価の開始時刻（秒）です。<xref href="Omni.Diagnostics.OmniBenchmarkRequest.HasStreamingRange" data-throw-if-not-resolved="false"></xref>がfalseなら未指定です。

```csharp
public double StreamingStartSequenceTimeSeconds { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Diagnostics_OmniBenchmarkRequest_WarmupFrames"></a> WarmupFrames

採取前に評価するwarmupフレーム数です。

```csharp
public int WarmupFrames { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)
