# <a id="Omni_Editor_Performance_OmniProfilerCaptureExporter"></a> Class OmniProfilerCaptureExporter

Namespace: [Omni.Editor.Performance](Omni.Editor.Performance.md)  
Assembly: Omni.Manager.dll  

Unity Profilerの.dataを読み込み、全体値とRuntime限定値をJSON/CSVへ分けて出力します。

```csharp
public static class OmniProfilerCaptureExporter
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniProfilerCaptureExporter](Omni.Editor.Performance.OmniProfilerCaptureExporter.md)

## 補足（Remarks）

キャプチャ自体へ書き込むことはありません。ただしProfilerDriver.LoadProfileは現在のEditor内
Profilerセッションを置換するため、通常は同じUnityバージョンのbatchmodeプロセスで実行します。

## メソッド（Methods）

### <a id="Omni_Editor_Performance_OmniProfilerCaptureExporter_ExportCapture_System_String_System_String_"></a> ExportCapture\(string, string\)

指定.dataを読み込み、summary JSONとframes/markers CSVを出力します。

```csharp
public static string ExportCapture(string capturePath, string outputDirectory)
```

#### 引数（Parameters）

`capturePath` [string](https://learn.microsoft.com/dotnet/api/system.string)

Unity Profilerが保存した.data。読み取り専用で扱います。

`outputDirectory` [string](https://learn.microsoft.com/dotnet/api/system.string)

出力先ディレクトリ。nullならTemp/OmniPerformance。

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

生成したsummary JSONの絶対パス。

### <a id="Omni_Editor_Performance_OmniProfilerCaptureExporter_ExportFromCommandLine"></a> ExportFromCommandLine\(\)

Unityの-executeMethod用入口です。

```csharp
public static void ExportFromCommandLine()
```

#### 補足（Remarks）

例: <code>-executeMethod Omni.Editor.Performance.OmniProfilerCaptureExporter.ExportFromCommandLine
-omni-profiler-capture &lt;path&gt; -omni-profiler-output &lt;directory&gt;</code>。
