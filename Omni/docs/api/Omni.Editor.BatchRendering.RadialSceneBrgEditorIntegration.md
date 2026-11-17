# <a id="Omni_Editor_BatchRendering_RadialSceneBrgEditorIntegration"></a> Class RadialSceneBrgEditorIntegration

Namespace: [Omni.Editor.BatchRendering](Omni.Editor.BatchRendering.md)  
Assembly: Omni.Editor.dll  

Scene BRGのEditor通知集約、sidecar生成、Build検証を管理します。

```csharp
[InitializeOnLoad]
public static class RadialSceneBrgEditorIntegration
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialSceneBrgEditorIntegration](Omni.Editor.BatchRendering.RadialSceneBrgEditorIntegration.md)

## プロパティ（Properties）

### <a id="Omni_Editor_BatchRendering_RadialSceneBrgEditorIntegration_CurrentReadiness"></a> CurrentReadiness

現在のbackendと直近結果から求めた、ロード済みSceneの準備分類です。

```csharp
public static RadialSceneBrgReadiness CurrentReadiness { get; }
```

#### 値（Property Value）

 [RadialSceneBrgReadiness](Omni.Editor.BatchRendering.RadialSceneBrgReadiness.md)

### <a id="Omni_Editor_BatchRendering_RadialSceneBrgEditorIntegration_IsManualRequestPending"></a> IsManualRequestPending

Omni Managerからの明示要求が未完了かどうかです。

```csharp
public static bool IsManualRequestPending { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_BatchRendering_RadialSceneBrgEditorIntegration_IsPreparationInProgress"></a> IsPreparationInProgress

準備を予約済み、または実行中かどうかです。

```csharp
public static bool IsPreparationInProgress { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_BatchRendering_RadialSceneBrgEditorIntegration_LastBuildScenesReport"></a> LastBuildScenesReport

直近のBuild Settingsを含む全体生成の結果です。未実行ならnullです。

```csharp
public static RadialSceneBrgPreparationReport LastBuildScenesReport { get; }
```

#### 値（Property Value）

 [RadialSceneBrgPreparationReport](Omni.Editor.BatchRendering.RadialSceneBrgPreparationReport.md)

### <a id="Omni_Editor_BatchRendering_RadialSceneBrgEditorIntegration_LastPreparationReport"></a> LastPreparationReport

直近の準備結果です。このEditorセッションで未実行ならnullです。

```csharp
public static RadialSceneBrgPreparationReport LastPreparationReport { get; }
```

#### 値（Property Value）

 [RadialSceneBrgPreparationReport](Omni.Editor.BatchRendering.RadialSceneBrgPreparationReport.md)

## メソッド（Methods）

### <a id="Omni_Editor_BatchRendering_RadialSceneBrgEditorIntegration_GenerateSidecars"></a> GenerateSidecars\(\)

Build Settingsの有効Sceneとロード済みScene向けsidecarを全件再生成し、
Manifestをその集合で置き換えます。失敗時は生成物を中途半端に書き換えず、
Scene BRGを準備保留（Fail Closed）のまま例外を投げます。

```csharp
public static void GenerateSidecars()
```

### <a id="Omni_Editor_BatchRendering_RadialSceneBrgEditorIntegration_PrepareLoadedSceneSidecarsForAutomation"></a> PrepareLoadedSceneSidecarsForAutomation\(\)

外部検証がScene open直後の遅延生成と競合しないよう、ロード済みScene分だけを
同期準備します。Player/runtime APIではなくEditor automation専用入口です。

```csharp
public static string PrepareLoadedSceneSidecarsForAutomation()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_BatchRendering_RadialSceneBrgEditorIntegration_RequestBuildScenesGeneration"></a> RequestBuildScenesGeneration\(\)

Build Settingsの有効Sceneとロード済みSceneのsidecarを、次の安全なEditor更新境界で
全件生成します。Build対象Sceneをpreviewとして読むため、ロード済みSceneだけの
再確認とは別操作にします。

```csharp
public static bool RequestBuildScenesGeneration()
```

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

新しく予約した場合true。既に予約済み・実行中ならfalse。

### <a id="Omni_Editor_BatchRendering_RadialSceneBrgEditorIntegration_RequestLoadedSceneRegeneration"></a> RequestLoadedSceneRegeneration\(\)

ロード済みSceneのsidecarを、次の安全なEditor更新境界で再確認・再生成します。
依存Hashが一致するsidecarも元Materialから写し直します。OnGUIから直接生成しないため、
呼出し側は要求だけを出します。

```csharp
public static bool RequestLoadedSceneRegeneration()
```

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

新しく予約した場合true。既に予約済み・実行中ならfalse。

### <a id="Omni_Editor_BatchRendering_RadialSceneBrgEditorIntegration_TryValidateManifest_System_String__"></a> TryValidateManifest\(out string\)

```csharp
public static bool TryValidateManifest(out string reason)
```

#### 引数（Parameters）

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_BatchRendering_RadialSceneBrgEditorIntegration_PreparationStatusChanged"></a> PreparationStatusChanged

準備結果または準備中状態が変わったときに通知します。Omni Managerは再描画だけを行い、
この通知から生成を開始してはいけません。

```csharp
public static event Action PreparationStatusChanged
```

#### 型（Event Type）

 [Action](https://learn.microsoft.com/dotnet/api/system.action)
