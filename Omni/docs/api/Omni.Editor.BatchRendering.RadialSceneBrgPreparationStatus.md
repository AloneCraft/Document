# <a id="Omni_Editor_BatchRendering_RadialSceneBrgPreparationStatus"></a> Class RadialSceneBrgPreparationStatus

Namespace: [Omni.Editor.BatchRendering](Omni.Editor.BatchRendering.md)  
Assembly: Omni.Editor.dll  

準備状態を利用者向けの分類へ変換します。

```csharp
public static class RadialSceneBrgPreparationStatus
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialSceneBrgPreparationStatus](Omni.Editor.BatchRendering.RadialSceneBrgPreparationStatus.md)

## メソッド（Methods）

### <a id="Omni_Editor_BatchRendering_RadialSceneBrgPreparationStatus_Classify_Omni_BatchRendering_RadialSceneBatchBackendMode_System_Boolean_Omni_Editor_BatchRendering_RadialSceneBrgPreparationReport_"></a> Classify\(RadialSceneBatchBackendMode, bool, RadialSceneBrgPreparationReport\)

backend、準備中フラグ、直近結果から分類します。Legacyでは結果に関わらず不要とし、
失敗を成功や準備中へ読み替えません。

```csharp
public static RadialSceneBrgReadiness Classify(RadialSceneBatchBackendMode backendMode, bool preparing, RadialSceneBrgPreparationReport lastReport)
```

#### 引数（Parameters）

`backendMode` RadialSceneBatchBackendMode

現在のScene Mesh backend。

`preparing` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

準備を予約済みまたは実行中ならtrue。

`lastReport` [RadialSceneBrgPreparationReport](Omni.Editor.BatchRendering.RadialSceneBrgPreparationReport.md)

直近結果。未実行ならnull。

#### 戻り値（Returns）

 [RadialSceneBrgReadiness](Omni.Editor.BatchRendering.RadialSceneBrgReadiness.md)
