# <a id="Omni_Editor_Diagnostics_OmniSceneViewVerification"></a> Class OmniSceneViewVerification

Namespace: [Omni.Editor.Diagnostics](Omni.Editor.Diagnostics.md)  
Assembly: Omni.Editor.dll  

<b>実際のScene Viewを駆動して</b>ナビゲーションの不変条件を検証します。

```csharp
public static class OmniSceneViewVerification
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniSceneViewVerification](Omni.Editor.Diagnostics.OmniSceneViewVerification.md)

## 補足（Remarks）

<p>
EditModeテストでは検証しきれない領域を埋めるためのものです。ヘッドレスに生成した
<xref href="UnityEditor.SceneView" data-throw-if-not-resolved="false"></xref>は<xref href="Omni.Logical.SceneViewViewportController.UsesVirtualViewport(UnityEditor.SceneView)" data-throw-if-not-resolved="false"></xref>
がfalseになり、安全上限が実機の250,000mではなく2,500mになるうえ、
<code>camera.transform.position</code>がUnityの実描画サイクル抜きには更新されません
（本プロジェクトで繰り返し踏んだ制約）。ここでは生きているScene Viewをそのまま使い、
描画サイクルを回しながら観測します。
</p>
<p>
<b>テレポートの判定は「要求した論理位置」と「読み直した論理位置」の差</b>で行います。
症状の言葉（飛ぶ・戻る）ではなく、入出力の不一致という検証可能な形へ落としています。
</p>
<p>
検証の前後でScene Viewの視点は元へ戻します。
</p>

## メソッド（Methods）

### <a id="Omni_Editor_Diagnostics_OmniSceneViewVerification_BeginAcceptanceSceneStateRestore"></a> BeginAcceptanceSceneStateRestore\(\)

Acceptance state の Scene 復元中は条件付き自動フレームを停止します。

```csharp
public static void BeginAcceptanceSceneStateRestore()
```

### <a id="Omni_Editor_Diagnostics_OmniSceneViewVerification_ClearRadialSourceForVerification"></a> ClearRadialSourceForVerification\(\)

受入検証で一時選択した設定元を解除します。探索/観察状態は保持します。

```csharp
public static string ClearRadialSourceForVerification()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniSceneViewVerification_CompleteAcceptanceSceneStateRestore"></a> CompleteAcceptanceSceneStateRestore\(\)

Acceptance state の Scene View 復元完了を現在の Scene 世代へ確定します。

```csharp
public static void CompleteAcceptanceSceneStateRestore()
```

### <a id="Omni_Editor_Diagnostics_OmniSceneViewVerification_ConfigureBoundaryDebug_System_String_"></a> ConfigureBoundaryDebug\(string\)

安全境界面の切り分け用に、辺の抑止・面の抑止・1面だけの描画を切り替えます。
<code>reset</code>で全て元へ戻します。切り替え後にScene Viewを再描画し、現在の設定を返します。

```csharp
public static string ConfigureBoundaryDebug(string mode)
```

#### 引数（Parameters）

`mode` [string](https://learn.microsoft.com/dotnet/api/system.string)

edges-off、edges-on、faces-off、faces-on、face-next（-1→0→…→5→-1）、reset。

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniSceneViewVerification_ConfigureGridPlanesForVerification_System_Boolean_"></a> ConfigureGridPlanesForVerification\(bool\)

性能A/B中だけ3軸グリッド平面を一括で表示・非表示にします。

```csharp
public static string ConfigureGridPlanesForVerification(bool enabled)
```

#### 引数（Parameters）

`enabled` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniSceneViewVerification_ConfigureRadialModeForVerification_System_Boolean_"></a> ConfigureRadialModeForVerification\(bool\)

現在のScene Viewへ優先順位先頭のRadialCameraを一時選択し、探索/観察を設定します。
受入自動化専用で、呼び出し側はacceptance-stateを使って元状態へ復元します。

```csharp
public static string ConfigureRadialModeForVerification(bool exploreFromSceneView)
```

#### 引数（Parameters）

`exploreFromSceneView` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniSceneViewVerification_ConfigureReflectionComparisonOverviewForVerification"></a> ConfigureReflectionComparisonOverviewForVerification\(\)

ReflectionProbesの設定元Cameraと比較対象を同時に見渡す外部Scene Viewを構成します。
Camera中心と対象中心の間を斜めから見るため、物理位置と対数位置の距離関係を観測できます。

```csharp
public static string ConfigureReflectionComparisonOverviewForVerification()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniSceneViewVerification_DescribeBoundaryEdgeState"></a> DescribeBoundaryEdgeState\(\)

直近に辺を描いたRepaintで、12辺ごとの結果（描いた・捨てた理由・画面外の大きさ・最小深度）を報告します。
固定グリッドのキャッシュ再生の回は辺を再計算しないため、報告は最後に描いた回のものです。

```csharp
public static string DescribeBoundaryEdgeState()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniSceneViewVerification_DescribeBoundaryFaceState"></a> DescribeBoundaryFaceState\(\)

直近のScene View Repaintで安全境界面を描いた条件（far/near、各面の入る側判定、
各頂点の視点前判定とnear/far内判定）を報告します。

```csharp
public static string DescribeBoundaryFaceState()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniSceneViewVerification_DescribeGridSubmissionState"></a> DescribeGridSubmissionState\(\)

直近のScene View Repaintで、グリッドがどの経路で描かれたかを報告します。

```csharp
public static string DescribeGridSubmissionState()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 補足（Remarks）

グリッドにはGPU深度経路とCPUフォールバック経路があり、GPU経路にはさらに
固定グリッドキャッシュの再生と完全提出があります。画面を見ただけではどれを
通ったか区別できないため、欠落や二重描画の切り分けにはこの値が必要です。

### <a id="Omni_Editor_Diagnostics_OmniSceneViewVerification_DescribeNavigationState"></a> DescribeNavigationState\(\)

```csharp
public static string DescribeNavigationState()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniSceneViewVerification_DescribeRadialWarpState"></a> DescribeRadialWarpState\(\)

現在のScene Viewカメラについて、レンダーパイプラインが実際に使うのと同じ経路
（<xref href="Omni.RadialGlobalRenderSystem.SceneViewDriverProvider" data-throw-if-not-resolved="false"></xref>）で対数ワープが
有効かどうかを解決します。Omniオーバーレイの表示/非表示（<code>OverlayHidden</code>）が
対数レンダリングの有効/無効へ正しく反映されているかを、自動化から確認するためです。

```csharp
public static string DescribeRadialWarpState()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniSceneViewVerification_DescribeSceneViewAnimationState"></a> DescribeSceneViewAnimationState\(\)

Scene Viewの位置・回転・サイズについて、Unity内部のアニメーション値（現在値と目標値）と、
Omniが最後に記録した物理ピボットの基底を並べて報告します。

```csharp
public static string DescribeSceneViewAnimationState()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 補足（Remarks）

Unityは視点の変化をアニメーション値として保持し、目標値が残っていると入力なしで
pivot／rotation／sizeを動かします。目標値≠現在値のままレイアウトが保存されると、次回起動時に
Omniの基底と食い違い、最初の再構築で差分が拒否されます（UB-008の調査記録）。どの操作が
目標値を残すかは画面から判別できないため、この値で切り分けます。内部フィールドは公開APIでは
ないのでリフレクションで読み、取得できない値は理由として<code>&lt;unavailable&gt;</code>を返します。

### <a id="Omni_Editor_Diagnostics_OmniSceneViewVerification_RequestViewSyncToRadialSourceForVerification"></a> RequestViewSyncToRadialSourceForVerification\(\)

Overlayの「設定元カメラへ視点を合わせる」と同じ一回限りの要求を、実Scene Viewへ発行します。
GPU画像検証で前Sceneの空の視点を誤って撮影しないための自動化入口です。

```csharp
public static string RequestViewSyncToRadialSourceForVerification()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniSceneViewVerification_Run_System_String_System_Action_System_Boolean_System_String__"></a> Run\(string, Action<bool, string\>\)

検証を開始します。完了時に<code class="paramref">onComplete</code>を呼びます。

```csharp
public static void Run(string scenario, Action<bool, string> onComplete)
```

#### 引数（Parameters）

`scenario` [string](https://learn.microsoft.com/dotnet/api/system.string)

`onComplete` [Action](https://learn.microsoft.com/dotnet/api/system.action\-2)<[bool](https://learn.microsoft.com/dotnet/api/system.boolean), [string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Editor_Diagnostics_OmniSceneViewVerification_SetNavigatorOverlayVisibleForAutomation_System_Boolean_"></a> SetNavigatorOverlayVisibleForAutomation\(bool\)

```csharp
public static string SetNavigatorOverlayVisibleForAutomation(bool visible)
```

#### 引数（Parameters）

`visible` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniSceneViewVerification_TryConfigureViewForAutomation_UnityEditor_SceneView_UnityEngine_Vector3_System_Single_UnityEngine_Quaternion_System_String__"></a> TryConfigureViewForAutomation\(SceneView, Vector3, float, Quaternion, out string\)

保存Sceneを変更せず、診断用Scene Viewを決定的な論理Pivotへ初期化します。

```csharp
public static bool TryConfigureViewForAutomation(SceneView sceneView, Vector3 logicalCenter, float physicalSize, Quaternion rotation, out string failure)
```

#### 引数（Parameters）

`sceneView` SceneView

`logicalCenter` Vector3

`physicalSize` [float](https://learn.microsoft.com/dotnet/api/system.single)

`rotation` Quaternion

`failure` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_OmniSceneViewVerification_TryGetAcceptancePivot_UnityEditor_SceneView_Omni_Logical_Position3__"></a> TryGetAcceptancePivot\(SceneView, out Position3\)

Galaxy受入の復元境界用に、Scene Viewの論理Pivotを固定小数点のまま取得します。
Unityの物理Pivotは遠距離で圧縮されたproxyになり得るため、復元用の正本には使いません。

```csharp
public static bool TryGetAcceptancePivot(SceneView sceneView, out Position3 logicalPivot)
```

#### 引数（Parameters）

`sceneView` SceneView

`logicalPivot` Position3

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_OmniSceneViewVerification_TryMoveLogicalCameraForAutomation_UnityEditor_SceneView_Omni_Logical_Position3__UnityEngine_Quaternion_System_String__"></a> TryMoveLogicalCameraForAutomation\(SceneView, in Position3, Quaternion, out string\)

巨大座標をfloatへ落とさず、Scene ViewのLogical eyeを直接移動します。

```csharp
public static bool TryMoveLogicalCameraForAutomation(SceneView sceneView, in Position3 logicalCameraPosition, Quaternion rotation, out string failure)
```

#### 引数（Parameters）

`sceneView` SceneView

`logicalCameraPosition` Position3

`rotation` Quaternion

`failure` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_OmniSceneViewVerification_TryRestoreAcceptancePivot_UnityEditor_SceneView_Omni_Logical_Position3__System_Single_"></a> TryRestoreAcceptancePivot\(SceneView, in Position3, float\)

Galaxy受入の復元境界用に、保存済み論理Pivotと距離をScene Viewへ戻します。

```csharp
public static bool TryRestoreAcceptancePivot(SceneView sceneView, in Position3 logicalPivot, float physicalSize)
```

#### 引数（Parameters）

`sceneView` SceneView

`logicalPivot` Position3

`physicalSize` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
