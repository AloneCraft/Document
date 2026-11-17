# <a id="Omni_Editor_Manager_OmniRenderingModeSettings"></a> Class OmniRenderingModeSettings

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

統合切替で選んだ描画方式（対数／標準）をプロジェクトに記録します。

<p>
Cameraへの <xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref> 付与はSceneの変更なので、保存しないまま開き直す、
別のSceneを開く、Player Buildする、のいずれでも失われます。対数を選んだ記録を残し、
Sceneを開いたとき、Playを始めたとき、Player Buildのときに付け直します
（<xref href="Omni.Editor.Manager.OmniRenderingModeAutoApply" data-throw-if-not-resolved="false"></xref>、<xref href="Omni.Editor.Manager.OmniRenderingModeSceneProcessor" data-throw-if-not-resolved="false"></xref>）。
</p>
<p>
標準は自動で外しません。RadialCameraを有効にして保存したデモSceneを壊さないためです。
記録が無いとき（未設定）も何もしません。
</p>

```csharp
public static class OmniRenderingModeSettings
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniRenderingModeSettings](Omni.Editor.Manager.OmniRenderingModeSettings.md)

## プロパティ（Properties）

### <a id="Omni_Editor_Manager_OmniRenderingModeSettings_AutoApplyActive"></a> AutoApplyActive

自動付与が働くか。対数が記録され、テストなどで止められていないときだけtrueです。

```csharp
public static bool AutoApplyActive { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_OmniRenderingModeSettings_Mode"></a> Mode

記録されている描画方式です。

```csharp
public static OmniRenderingModeSettings.RenderingMode Mode { get; }
```

#### 値（Property Value）

 [OmniRenderingModeSettings](Omni.Editor.Manager.OmniRenderingModeSettings.md).[RenderingMode](Omni.Editor.Manager.OmniRenderingModeSettings.RenderingMode.md)

## メソッド（Methods）

### <a id="Omni_Editor_Manager_OmniRenderingModeSettings_Resume"></a> Resume\(\)

```csharp
public static void Resume()
```

### <a id="Omni_Editor_Manager_OmniRenderingModeSettings_SetMode_Omni_Editor_Manager_OmniRenderingModeSettings_RenderingMode_"></a> SetMode\(RenderingMode\)

描画方式を記録します。対数にしたときは、ロード済みSceneへすぐ反映します。

```csharp
public static void SetMode(OmniRenderingModeSettings.RenderingMode mode)
```

#### 引数（Parameters）

`mode` [OmniRenderingModeSettings](Omni.Editor.Manager.OmniRenderingModeSettings.md).[RenderingMode](Omni.Editor.Manager.OmniRenderingModeSettings.RenderingMode.md)

### <a id="Omni_Editor_Manager_OmniRenderingModeSettings_Suspend"></a> Suspend\(\)

自動付与を一時的に止めます（テスト実行中など）。<xref href="Omni.Editor.Manager.OmniRenderingModeSettings.Resume" data-throw-if-not-resolved="false"></xref> と対で呼びます。

```csharp
public static void Suspend()
```
