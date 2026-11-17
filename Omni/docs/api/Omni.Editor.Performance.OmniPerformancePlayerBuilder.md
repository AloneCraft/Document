# <a id="Omni_Editor_Performance_OmniPerformancePlayerBuilder"></a> Class OmniPerformancePlayerBuilder

Namespace: [Omni.Editor.Performance](Omni.Editor.Performance.md)  
Assembly: Omni.Manager.dll  

Build Settingsを変更せず、許可済み段階Sceneまたは製品Sceneだけを含むIL2CPP性能計測Playerを生成します。

```csharp
public static class OmniPerformancePlayerBuilder
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniPerformancePlayerBuilder](Omni.Editor.Performance.OmniPerformancePlayerBuilder.md)

## メソッド（Methods）

### <a id="Omni_Editor_Performance_OmniPerformancePlayerBuilder_BuildForScene_System_String_System_String_"></a> BuildForScene\(string, string\)

許可済み段階Sceneまたは製品Sceneを唯一のBuild SceneとしてPlayerを生成します。

```csharp
public static string BuildForScene(string sceneName, string outputDirectory)
```

#### 引数（Parameters）

`sceneName` [string](https://learn.microsoft.com/dotnet/api/system.string)

許可済み段階Sceneまたは製品Scene。大小文字は区別しません。

`outputDirectory` [string](https://learn.microsoft.com/dotnet/api/system.string)

出力ディレクトリ。nullならTemp/OmniPerformance/Players。

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

生成した実行ファイルの絶対パス。

### <a id="Omni_Editor_Performance_OmniPerformancePlayerBuilder_BuildFromCommandLine"></a> BuildFromCommandLine\(\)

Unityの-executeMethodから、許可済み段階Sceneまたは製品Sceneを受けてPlayerを生成します。

```csharp
public static void BuildFromCommandLine()
```

### <a id="Omni_Editor_Performance_OmniPerformancePlayerBuilder_BuildPreparedGardenFromCommandLine"></a> BuildPreparedGardenFromCommandLine\(\)

DX12設定で起動済みのEditorからGardenをBuildし、元設定を復元します。

```csharp
public static void BuildPreparedGardenFromCommandLine()
```

### <a id="Omni_Editor_Performance_OmniPerformancePlayerBuilder_PrepareGardenDx12FromCommandLine"></a> PrepareGardenDx12FromCommandLine\(\)

別Editor起動前にGarden Build用DX12設定を保存します。

```csharp
public static void PrepareGardenDx12FromCommandLine()
```

### <a id="Omni_Editor_Performance_OmniPerformancePlayerBuilder_RestoreGardenGraphicsApisFromCommandLine"></a> RestoreGardenGraphicsApisFromCommandLine\(\)

異常終了後に残ったGarden Build用Graphics API退避を復元します。

```csharp
public static void RestoreGardenGraphicsApisFromCommandLine()
```

### <a id="Omni_Editor_Performance_OmniPerformancePlayerBuilder_TryResolveScenePath_System_String_System_String__"></a> TryResolveScenePath\(string, out string\)

CLIとMenuで共通に使う、性能計測シーン名からアセットパスへの安全な対応表です。

```csharp
public static bool TryResolveScenePath(string sceneName, out string scenePath)
```

#### 引数（Parameters）

`sceneName` [string](https://learn.microsoft.com/dotnet/api/system.string)

`scenePath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
