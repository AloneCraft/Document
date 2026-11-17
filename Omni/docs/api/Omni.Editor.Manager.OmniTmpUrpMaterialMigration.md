# <a id="Omni_Editor_Manager_OmniTmpUrpMaterialMigration"></a> Class OmniTmpUrpMaterialMigration

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

既存TMP MaterialをGUIDを維持したまま公式URP原本へ移行し、Omni Managerの
共通経路でRadial版を生成します。GUID参照のため全Scene/Prefabへ一括波及し、
Active Sceneでは表示モードに依存せず、BRG Manifestが解決できるURP
Authoring正本へ即時同期します。Radial生成物はsidecarとして使用します。

```csharp
public static class OmniTmpUrpMaterialMigration
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniTmpUrpMaterialMigration](Omni.Editor.Manager.OmniTmpUrpMaterialMigration.md)

## メソッド（Methods）

### <a id="Omni_Editor_Manager_OmniTmpUrpMaterialMigration_MigrateActiveScene"></a> MigrateActiveScene\(\)

Material Assetの移動は全参照へ波及します。Active SceneのワールドTMPだけは
Undo可能に表示Materialを同期し、Sceneを保存せずDirtyにします。

```csharp
public static string MigrateActiveScene()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

移行件数と生成先を含む診断文字列。
