# <a id="Omni_Editor_Manager_RadialRenderingSwitch"></a> Class RadialRenderingSwitch

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

「Unityレンダリング / Radialレンダリング」の統合切替です。

<p>
マテリアル設定・シェーダー設定・ベイク設定・カメラへの <xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref> 付与は、
「Radial で見るか Unity 標準で見るか」という 1 つの意思決定の各側面であり、個別に
操作する意味がありません（シェーダー生成はマテリアル生成が内部で自動的に呼ぶため、
独立項目にする意味自体が無い）。このクラスが単一の入口になります。
</p>
<p>
マテリアル部分の実行エンジンは <xref href="Omni.Converter.RadialMaterialApplier" data-throw-if-not-resolved="false"></xref> /
<xref href="Omni.Converter.RadialSceneMaterialState" data-throw-if-not-resolved="false"></xref>（前段で作った、シーン実データから毎回状態を
数え直す仕組み）をそのまま再利用します。ここで新たに持つ状態はありません。
</p>

```csharp
public static class RadialRenderingSwitch
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialRenderingSwitch](Omni.Editor.Manager.RadialRenderingSwitch.md)

## プロパティ（Properties）

### <a id="Omni_Editor_Manager_RadialRenderingSwitch_LastLedgerReconcileSummary"></a> LastLedgerReconcileSummary

直前の切替で整理した古い切替記録の要約です。整理が無ければ空です。

```csharp
public static string LastLedgerReconcileSummary { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_RadialRenderingSwitch_LastRendererResourceWarning"></a> LastRendererResourceWarning

直前の対数切替で、URP共有resource（Camera MotionVectors／SSAO）をOmni版へ
接続できなかった理由です。接続済み、または接続できたときは空です。

```csharp
public static string LastRendererResourceWarning { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Editor_Manager_RadialRenderingSwitch_DescribeStage_Omni_Editor_Manager_RadialRenderingSwitch_FailureStage_"></a> DescribeStage\(FailureStage\)

切替が止まった段階の、利用者向けの名前です。

```csharp
public static string DescribeStage(RadialRenderingSwitch.FailureStage stage)
```

#### 引数（Parameters）

`stage` [RadialRenderingSwitch](Omni.Editor.Manager.RadialRenderingSwitch.md).[FailureStage](Omni.Editor.Manager.RadialRenderingSwitch.FailureStage.md)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_RadialRenderingSwitch_RetryPendingManifestSave"></a> RetryPendingManifestSave\(\)

```csharp
public static OmniGuidManifest.SaveResult RetryPendingManifestSave()
```

#### 戻り値（Returns）

 OmniGuidManifest.SaveResult

### <a id="Omni_Editor_Manager_RadialRenderingSwitch_Scan"></a> Scan\(\)

現在の状態をシーンの実データから数えます（キャッシュしません）。

```csharp
public static RadialRenderingSwitch.State Scan()
```

#### 戻り値（Returns）

 [RadialRenderingSwitch](Omni.Editor.Manager.RadialRenderingSwitch.md).[State](Omni.Editor.Manager.RadialRenderingSwitch.State.md)

### <a id="Omni_Editor_Manager_RadialRenderingSwitch_SwitchToRadial"></a> SwitchToRadial\(\)

Radial レンダリングへ切り替えます。カメラ追加の確認で Cancel された場合は
何も変更せずに戻ります（マテリアルにも一切触れません）。

```csharp
public static void SwitchToRadial()
```

### <a id="Omni_Editor_Manager_RadialRenderingSwitch_SwitchToUnity"></a> SwitchToUnity\(\)

```csharp
public static void SwitchToUnity()
```

### <a id="Omni_Editor_Manager_RadialRenderingSwitch_TrySwitch_Omni_Editor_Manager_RadialRenderingSwitch_RenderingMode_"></a> TrySwitch\(RenderingMode\)

```csharp
public static RadialRenderingSwitch.RadialRenderingSwitchResult TrySwitch(RadialRenderingSwitch.RenderingMode mode)
```

#### 引数（Parameters）

`mode` [RadialRenderingSwitch](Omni.Editor.Manager.RadialRenderingSwitch.md).[RenderingMode](Omni.Editor.Manager.RadialRenderingSwitch.RenderingMode.md)

#### 戻り値（Returns）

 [RadialRenderingSwitch](Omni.Editor.Manager.RadialRenderingSwitch.md).[RadialRenderingSwitchResult](Omni.Editor.Manager.RadialRenderingSwitch.RadialRenderingSwitchResult.md)

### <a id="Omni_Editor_Manager_RadialRenderingSwitch_TrySwitchLoadedSceneCameras_Omni_Editor_Manager_RadialRenderingSwitch_RenderingMode_"></a> TrySwitchLoadedSceneCameras\(RenderingMode\)

ロード済みSceneのカメラだけを切り替えます（Project範囲の切替から使います）。
対数: RadialCameraの無いカメラへ追加し、無効なものを有効化します。標準: 有効なものを無効化します
（追加したComponentは削除しません）。観察Rigの枠カメラと保存されない隠しカメラは対象外です
（<xref href="Omni.Editor.Manager.OmniCameraScanner.IsRadialSwitchTarget(UnityEngine.Camera)" data-throw-if-not-resolved="false"></xref>）。

```csharp
public static RadialRenderingSwitch.RadialRenderingSwitchResult TrySwitchLoadedSceneCameras(RadialRenderingSwitch.RenderingMode mode)
```

#### 引数（Parameters）

`mode` [RadialRenderingSwitch](Omni.Editor.Manager.RadialRenderingSwitch.md).[RenderingMode](Omni.Editor.Manager.RadialRenderingSwitch.RenderingMode.md)

#### 戻り値（Returns）

 [RadialRenderingSwitch](Omni.Editor.Manager.RadialRenderingSwitch.md).[RadialRenderingSwitchResult](Omni.Editor.Manager.RadialRenderingSwitch.RadialRenderingSwitchResult.md)

### <a id="Omni_Editor_Manager_RadialRenderingSwitch_TrySwitchProjectMaterials_Omni_Editor_Manager_RadialRenderingSwitch_RenderingMode_System_Collections_Generic_IEnumerable_UnityEngine_Material__"></a> TrySwitchProjectMaterials\(RenderingMode, IEnumerable<Material\>\)

Project範囲のMaterialだけを切り替えます。Camera、VFX、Rendererの状態は
Project Material構成のラジオ判定へ混ぜず、ロード済みScene切替からも変更しません。

```csharp
public static RadialRenderingSwitch.RadialRenderingSwitchResult TrySwitchProjectMaterials(RadialRenderingSwitch.RenderingMode mode, IEnumerable<Material> materials)
```

#### 引数（Parameters）

`mode` [RadialRenderingSwitch](Omni.Editor.Manager.RadialRenderingSwitch.md).[RenderingMode](Omni.Editor.Manager.RadialRenderingSwitch.RenderingMode.md)

`materials` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<Material\>

#### 戻り値（Returns）

 [RadialRenderingSwitch](Omni.Editor.Manager.RadialRenderingSwitch.md).[RadialRenderingSwitchResult](Omni.Editor.Manager.RadialRenderingSwitch.RadialRenderingSwitchResult.md)
