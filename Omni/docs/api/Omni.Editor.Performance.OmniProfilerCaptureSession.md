# <a id="Omni_Editor_Performance_OmniProfilerCaptureSession"></a> Class OmniProfilerCaptureSession

Namespace: [Omni.Editor.Performance](Omni.Editor.Performance.md)  
Assembly: Omni.Manager.dll  

起動中のUnity EditorのProfiler履歴を、指定フレーム数だけ収集して.dataへ保存します。

```csharp
[InitializeOnLoad]
public static class OmniProfilerCaptureSession
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniProfilerCaptureSession](Omni.Editor.Performance.OmniProfilerCaptureSession.md)

## 補足（Remarks）

収集中はEditor profilerを有効化し、既存履歴を消去します。収集完了後は開始前の
profileEditor/profileGPU設定へ戻します。保存後の.data集計は
<xref href="Omni.Editor.Performance.OmniProfilerCaptureExporter" data-throw-if-not-resolved="false"></xref>へ委譲します。

## メソッド（Methods）

### <a id="Omni_Editor_Performance_OmniProfilerCaptureSession_AbortActiveCapture_System_String__"></a> AbortActiveCapture\(out string\)

実行中のProfiler captureだけを保存せず明示中断し、開始前のProfiler/Warp設定へ
復元します。capture外では安全なno-opです。

```csharp
public static bool AbortActiveCapture(out string message)
```

#### 引数（Parameters）

`message` [string](https://learn.microsoft.com/dotnet/api/system.string)

IPCへ返す中断結果です。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

active captureを今回中断した場合だけtrueです。

### <a id="Omni_Editor_Performance_OmniProfilerCaptureSession_Begin_System_String_System_Int32_System_Int32_System_Action_System_Boolean_System_String__"></a> Begin\(string, int, int, Action<bool, string\>\)

収集を開始します。呼び出し元は完了callbackでIPC応答などを返します。

```csharp
public static void Begin(string outputPath, int warmupFrameCount, int sampleFrameCount, Action<bool, string> completion)
```

#### 引数（Parameters）

`outputPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`warmupFrameCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`sampleFrameCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`completion` [Action](https://learn.microsoft.com/dotnet/api/system.action\-2)<[bool](https://learn.microsoft.com/dotnet/api/system.boolean), [string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Editor_Performance_OmniProfilerCaptureSession_Begin_System_String_System_Int32_System_Int32_System_Boolean_System_Action_System_Boolean_System_String__"></a> Begin\(string, int, int, bool, Action<bool, string\>\)

GPU計測の有無を明示してProfiler収集を開始します。

```csharp
public static void Begin(string outputPath, int warmupFrameCount, int sampleFrameCount, bool profileGpu, Action<bool, string> completion)
```

#### 引数（Parameters）

`outputPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

保存する.dataの絶対パスです。

`warmupFrameCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

統計対象の前に収集するwarmupフレーム数です。

`sampleFrameCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

warmup後に収集するフレーム数です。

`profileGpu` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

GPU Profilerも有効化する場合はtrueです。

`completion` [Action](https://learn.microsoft.com/dotnet/api/system.action\-2)<[bool](https://learn.microsoft.com/dotnet/api/system.boolean), [string](https://learn.microsoft.com/dotnet/api/system.string)\>

保存完了または失敗を受け取るcallbackです。

### <a id="Omni_Editor_Performance_OmniProfilerCaptureSession_BeginDefault_System_String_System_Action_System_Boolean_System_String__"></a> BeginDefault\(string, Action<bool, string\>\)

標準のScene View評価条件向けの120 warmup/600 sample収集を開始します。

```csharp
public static void BeginDefault(string outputPath, Action<bool, string> completion)
```

#### 引数（Parameters）

`outputPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`completion` [Action](https://learn.microsoft.com/dotnet/api/system.action\-2)<[bool](https://learn.microsoft.com/dotnet/api/system.boolean), [string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Editor_Performance_OmniProfilerCaptureSession_BeginDefaultCpuOnly_System_String_System_Action_System_Boolean_System_String__"></a> BeginDefaultCpuOnly\(string, Action<bool, string\>\)

GardenSceneなど高負荷Editor向けに、GPU Profilerを使わず標準フレーム数を収集します。

```csharp
public static void BeginDefaultCpuOnly(string outputPath, Action<bool, string> completion)
```

#### 引数（Parameters）

`outputPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

保存する.dataの絶対パスです。

`completion` [Action](https://learn.microsoft.com/dotnet/api/system.action\-2)<[bool](https://learn.microsoft.com/dotnet/api/system.boolean), [string](https://learn.microsoft.com/dotnet/api/system.string)\>

保存完了または失敗を受け取るcallbackです。

### <a id="Omni_Editor_Performance_OmniProfilerCaptureSession_BeginDefaultCpuOnlyWithCameraMotionAndWarpEnabled_System_String_System_Boolean_System_Boolean_System_Action_System_Boolean_System_String__"></a> BeginDefaultCpuOnlyWithCameraMotionAndWarpEnabled\(string, bool, bool, Action<bool, string\>\)

120 warmup＋600 sampleの正式なScene View移動計測を行います。
hover停止はOverlayを残した因果分離セッションだけで使用します。

```csharp
public static void BeginDefaultCpuOnlyWithCameraMotionAndWarpEnabled(string outputPath, bool warpEnabled, bool suppressHoverRefresh, Action<bool, string> completion)
```

#### 引数（Parameters）

`outputPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`warpEnabled` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`suppressHoverRefresh` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`completion` [Action](https://learn.microsoft.com/dotnet/api/system.action\-2)<[bool](https://learn.microsoft.com/dotnet/api/system.boolean), [string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Editor_Performance_OmniProfilerCaptureSession_BeginDefaultCpuOnlyWithWarpEnabled_System_String_System_Boolean_System_Action_System_Boolean_System_String__"></a> BeginDefaultCpuOnlyWithWarpEnabled\(string, bool, Action<bool, string\>\)

GardenSceneの比較用にWarpEnabledを一時指定し、GPU Profilerなしで
120 warmup＋600 sampleを収集します。

```csharp
public static void BeginDefaultCpuOnlyWithWarpEnabled(string outputPath, bool warpEnabled, Action<bool, string> completion)
```

#### 引数（Parameters）

`outputPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

保存する.dataの絶対パスです。

`warpEnabled` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

収集期間だけ適用するRadialワープ状態です。

`completion` [Action](https://learn.microsoft.com/dotnet/api/system.action\-2)<[bool](https://learn.microsoft.com/dotnet/api/system.boolean), [string](https://learn.microsoft.com/dotnet/api/system.string)\>

元のワープ状態とProfiler設定を復元した後に呼ぶ完了callbackです。

### <a id="Omni_Editor_Performance_OmniProfilerCaptureSession_BeginDiagnosticCpuOnlyWithCameraMotionAndWarpEnabled_System_String_System_Boolean_System_Action_System_Boolean_System_String__"></a> BeginDiagnosticCpuOnlyWithCameraMotionAndWarpEnabled\(string, bool, Action<bool, string\>\)

比較値には使用しない35フレーム診断として、Warp状態を固定しながら
Scene View論理カメラを毎フレーム往復させます。

```csharp
public static void BeginDiagnosticCpuOnlyWithCameraMotionAndWarpEnabled(string outputPath, bool warpEnabled, Action<bool, string> completion)
```

#### 引数（Parameters）

`outputPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`warpEnabled` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`completion` [Action](https://learn.microsoft.com/dotnet/api/system.action\-2)<[bool](https://learn.microsoft.com/dotnet/api/system.boolean), [string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Editor_Performance_OmniProfilerCaptureSession_BeginDiagnosticCpuOnlyWithWarpEnabled_System_String_System_Boolean_System_Action_System_Boolean_System_String__"></a> BeginDiagnosticCpuOnlyWithWarpEnabled\(string, bool, Action<bool, string\>\)

受け入れ性能値には使用しない短時間診断として、WarpEnabledを一時指定し、
GPU Profilerなしで5 warmup＋30 sampleだけ収集します。

```csharp
public static void BeginDiagnosticCpuOnlyWithWarpEnabled(string outputPath, bool warpEnabled, Action<bool, string> completion)
```

#### 引数（Parameters）

`outputPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`warpEnabled` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`completion` [Action](https://learn.microsoft.com/dotnet/api/system.action\-2)<[bool](https://learn.microsoft.com/dotnet/api/system.boolean), [string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Editor_Performance_OmniProfilerCaptureSession_BeginPlayModeCpuOnly_System_String_System_Int32_System_Int32_System_Action_System_Boolean_System_String__"></a> BeginPlayModeCpuOnly\(string, int, int, Action<bool, string\>\)

Play Mode PlayerLoopをGPU Profilerなしで指定フレーム数だけ収集します。

```csharp
public static void BeginPlayModeCpuOnly(string outputPath, int warmupFrameCount, int sampleFrameCount, Action<bool, string> completion)
```

#### 引数（Parameters）

`outputPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`warmupFrameCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`sampleFrameCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`completion` [Action](https://learn.microsoft.com/dotnet/api/system.action\-2)<[bool](https://learn.microsoft.com/dotnet/api/system.boolean), [string](https://learn.microsoft.com/dotnet/api/system.string)\>
