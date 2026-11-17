# <a id="Omni_Diagnostics_OmniPerformanceMarkers"></a> Class OmniPerformanceMarkers

Namespace: [Omni.Diagnostics](Omni.Diagnostics.md)  
Assembly: Radial.Runtime.dll  

Logical、Radial、Galaxyのホットパスで共有する低オーバーヘッドのProfilerマーカーです。

```csharp
public static class OmniPerformanceMarkers
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniPerformanceMarkers](Omni.Diagnostics.OmniPerformanceMarkers.md)

## 補足（Remarks）

利用側では<code>using(OmniPerformanceMarkers.GalaxyDirector.Auto())</code>のように
AutoScopeを使います。AutoScopeは値型のため、Profiler有効時にもGCを発生させません。

## フィールド（Fields）

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_GalaxyBodyRegistry"></a> GalaxyBodyRegistry

Galaxy Body Registryの登録・探索・状態同期を計測します。

```csharp
public static readonly ProfilerMarker GalaxyBodyRegistry
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_GalaxyDirector"></a> GalaxyDirector

Galaxy Directorによるショット評価・カメラ制御を計測します。

```csharp
public static readonly ProfilerMarker GalaxyDirector
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_GalaxyDirectorApplyCamera"></a> GalaxyDirectorApplyCamera

GalaxyのApplyCamera全体を計測します。

```csharp
public static readonly ProfilerMarker GalaxyDirectorApplyCamera
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_GalaxyDirectorApplyCameraApplyKeyLight"></a> GalaxyDirectorApplyCameraApplyKeyLight

主光源姿勢更新を計測します。

```csharp
public static readonly ProfilerMarker GalaxyDirectorApplyCameraApplyKeyLight
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_GalaxyDirectorApplyCameraBuildPose"></a> GalaxyDirectorApplyCameraBuildPose

カメラLogical姿勢の構築を計測します。

```csharp
public static readonly ProfilerMarker GalaxyDirectorApplyCameraBuildPose
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_GalaxyDirectorApplyCameraResolveTarget"></a> GalaxyDirectorApplyCameraResolveTarget

対象天体のLogical位置解決を計測します。

```csharp
public static readonly ProfilerMarker GalaxyDirectorApplyCameraResolveTarget
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_GalaxyDirectorApplyCameraSyncTransform"></a> GalaxyDirectorApplyCameraSyncTransform

カメラTransform同期を計測します。

```csharp
public static readonly ProfilerMarker GalaxyDirectorApplyCameraSyncTransform
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_GalaxyDirectorApplySpin"></a> GalaxyDirectorApplySpin

ApplySpin全体を計測します。

```csharp
public static readonly ProfilerMarker GalaxyDirectorApplySpin
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_GalaxyDirectorApplySpinResolveRotation"></a> GalaxyDirectorApplySpinResolveRotation

天体自転姿勢の解決を計測します。

```csharp
public static readonly ProfilerMarker GalaxyDirectorApplySpinResolveRotation
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_GalaxyDirectorApplySpinSyncTransform"></a> GalaxyDirectorApplySpinSyncTransform

天体Transform同期を計測します。

```csharp
public static readonly ProfilerMarker GalaxyDirectorApplySpinSyncTransform
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_GetLog2Convert"></a> GetLog2Convert

正規化済みLogicalScalarのfloat変換を計測します。

```csharp
public static readonly ProfilerMarker GetLog2Convert
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_GetLog2Finish"></a> GetLog2Finish

正規化仮数から最終log2値を確定します。

```csharp
public static readonly ProfilerMarker GetLog2Finish
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_GetLog2HighestBit"></a> GetLog2HighestBit

LogicalScalar log2変換の最上位bit解決を計測します。

```csharp
public static readonly ProfilerMarker GetLog2HighestBit
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_GetLog2Scale"></a> GetLog2Scale

LogicalScalar log2変換の仮数正規化を計測します。

```csharp
public static readonly ProfilerMarker GetLog2Scale
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialBoundsApply"></a> RadialBoundsApply

保守Boundsの厳密一致判定とRenderer適用を計測します。

```csharp
public static readonly ProfilerMarker RadialBoundsApply
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialBoundsBuild"></a> RadialBoundsBuild

GPU変形後を包む保守Bounds構築を計測します。

```csharp
public static readonly ProfilerMarker RadialBoundsBuild
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialBoundsBuildsCounterName"></a> RadialBoundsBuildsCounterName

Profiler上の保守Bounds構築数counter名です。

```csharp
public const string RadialBoundsBuildsCounterName = "Omni.Radial.Camera.BoundsBuilds"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialBoundsRecordCreationsCounterName"></a> RadialBoundsRecordCreationsCounterName

Profiler上のBounds Record生成数counter名です。

```csharp
public const string RadialBoundsRecordCreationsCounterName = "Omni.Radial.Bounds.RecordCreations"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialBoundsRestoresCounterName"></a> RadialBoundsRestoresCounterName

Profiler上のBounds復元数counter名です。

```csharp
public const string RadialBoundsRestoresCounterName = "Omni.Radial.Bounds.Restores"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialBoundsWriteSkipsCounterName"></a> RadialBoundsWriteSkipsCounterName

Profiler上のBounds write省略数counter名です。

```csharp
public const string RadialBoundsWriteSkipsCounterName = "Omni.Radial.Bounds.WriteSkips"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialBoundsWritesCounterName"></a> RadialBoundsWritesCounterName

Profiler上のBounds native write数counter名です。

```csharp
public const string RadialBoundsWritesCounterName = "Omni.Radial.Bounds.Writes"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialCameraCleanup"></a> RadialCameraCleanup

Camera終了時の差分Bounds・可視状態・投影復元を計測します。

```csharp
public static readonly ProfilerMarker RadialCameraCleanup
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialCameraContextResolve"></a> RadialCameraContextResolve

Camera、Radial driver、Logical Scene View文脈の解決を計測します。

```csharp
public static readonly ProfilerMarker RadialCameraContextResolve
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialCameraFrameReset"></a> RadialCameraFrameReset

Camera描画前に前viewの一時状態を復元する処理を計測します。

```csharp
public static readonly ProfilerMarker RadialCameraFrameReset
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialCameraPreparation"></a> RadialCameraPreparation

Radial CameraのLogical相対値と描画パラメータの準備を計測します。

```csharp
public static readonly ProfilerMarker RadialCameraPreparation
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialCameraProjection"></a> RadialCameraProjection

Camera投影、clip、カリング、camera-relative frame準備を計測します。

```csharp
public static readonly ProfilerMarker RadialCameraProjection
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialCameraProjectionClip"></a> RadialCameraProjectionClip

投影・clip・標準／Radialカリング状態の適用を計測します。

```csharp
public static readonly ProfilerMarker RadialCameraProjectionClip
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialCameraProjectionClipApply"></a> RadialCameraProjectionClipApply

確定したProjection ClipをCameraへ適用または復元します。

```csharp
public static readonly ProfilerMarker RadialCameraProjectionClipApply
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialCameraProjectionClipClear"></a> RadialCameraProjectionClipClear

Projection Clip経路でLegacy culling抑止状態を解除する処理を計測します。

```csharp
public static readonly ProfilerMarker RadialCameraProjectionClipClear
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialCameraProjectionClipDiagnostics"></a> RadialCameraProjectionClipDiagnostics

Projection Clipの確定値を診断キャッシュへ記録します。

```csharp
public static readonly ProfilerMarker RadialCameraProjectionClipDiagnostics
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialCameraProjectionClipNear"></a> RadialCameraProjectionClipNear

論理Nearから安全なhardware nearを解決します。

```csharp
public static readonly ProfilerMarker RadialCameraProjectionClipNear
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialCameraProjectionClipNote"></a> RadialCameraProjectionClipNote

Projection Clip経路で標準culling状態を診断へ記録する処理を計測します。

```csharp
public static readonly ProfilerMarker RadialCameraProjectionClipNote
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialCameraProjectionClipRequirements"></a> RadialCameraProjectionClipRequirements

Projection Clipが必要とするfar距離を常駐キャッシュから解決します。

```csharp
public static readonly ProfilerMarker RadialCameraProjectionClipRequirements
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialCameraProjectionClipReset"></a> RadialCameraProjectionClipReset

Projection Clip経路でUnity標準culling matrixへ戻す処理を計測します。

```csharp
public static readonly ProfilerMarker RadialCameraProjectionClipReset
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialCameraProjectionClipUpdate"></a> RadialCameraProjectionClipUpdate

Projection Clipのnear/far上書き全体を計測します。

```csharp
public static readonly ProfilerMarker RadialCameraProjectionClipUpdate
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialCameraProjectionSetup"></a> RadialCameraProjectionSetup

投影開始時のnative状態復元とワープモード確定を計測します。

```csharp
public static readonly ProfilerMarker RadialCameraProjectionSetup
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialCameraRelativeFrame"></a> RadialCameraRelativeFrame

Logical eyeからcamera-relative GPU frameを構築する処理を計測します。

```csharp
public static readonly ProfilerMarker RadialCameraRelativeFrame
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialCameraTargetMaintenance"></a> RadialCameraTargetMaintenance

dirty対象、fallback分類、Material互換キャッシュの保守を計測します。

```csharp
public static readonly ProfilerMarker RadialCameraTargetMaintenance
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialCompatibility"></a> RadialCompatibility

Camera別の互換対象判定と非表示化を計測します。

```csharp
public static readonly ProfilerMarker RadialCompatibility
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialCompatibilityWarning"></a> RadialCompatibilityWarning

互換警告をUnity Consoleへ通知する同期callbackを計測します。

```csharp
public static readonly ProfilerMarker RadialCompatibilityWarning
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialCulling"></a> RadialCulling

Radial描画のLogical AABB判定と可視集合の構築を計測します。

```csharp
public static readonly ProfilerMarker RadialCulling
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialFastCandidatesCounterName"></a> RadialFastCandidatesCounterName

Profiler上の共有Unity Transform fast候補数counter名です。

```csharp
public const string RadialFastCandidatesCounterName = "Omni.Radial.Fast.Candidates"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialFastWarmupWritesCounterName"></a> RadialFastWarmupWritesCounterName

Profiler上のfast-path初回MPB/Bounds準備数counter名です。

```csharp
public const string RadialFastWarmupWritesCounterName = "Omni.Radial.Fast.WarmupWrites"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialGlobalBindings"></a> RadialGlobalBindings

Radial描画用のGPUグローバル値・バッファをバインドする処理を計測します。

```csharp
public static readonly ProfilerMarker RadialGlobalBindings
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialMpbWritesCounterName"></a> RadialMpbWritesCounterName

Profiler上のMaterialPropertyBlock write数counter名です。

```csharp
public const string RadialMpbWritesCounterName = "Omni.Radial.Camera.MpbWrites"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialPoseEvaluatedCounterName"></a> RadialPoseEvaluatedCounterName

Profiler上のCamera別pose評価数counter名です。

```csharp
public const string RadialPoseEvaluatedCounterName = "Omni.Radial.Camera.PoseEvaluated"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialPreciseFallbackCounterName"></a> RadialPreciseFallbackCounterName

Profiler上の精密per-Renderer fallback数counter名です。

```csharp
public const string RadialPreciseFallbackCounterName = "Omni.Radial.Camera.PreciseFallbacks"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialPropertyBlock"></a> RadialPropertyBlock

RendererのMaterialPropertyBlock read-modify-writeを計測します。

```csharp
public static readonly ProfilerMarker RadialPropertyBlock
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialRendererTraversal"></a> RadialRendererTraversal

Camera別Renderer走査全体を計測します。

```csharp
public static readonly ProfilerMarker RadialRendererTraversal
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialRendererTraversalCounterName"></a> RadialRendererTraversalCounterName

Profiler上のCamera別Renderer走査数counter名です。

```csharp
public const string RadialRendererTraversalCounterName = "Omni.Radial.Camera.RendererTraversal.Count"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialSharedPacketWritesCounterName"></a> RadialSharedPacketWritesCounterName

Profiler上のcamera共有packet write数counter名です。

```csharp
public const string RadialSharedPacketWritesCounterName = "Omni.Radial.Camera.SharedPacketWrites"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialTargetRefresh"></a> RadialTargetRefresh

Radial対象一覧のdirty時再収集を計測します。

```csharp
public static readonly ProfilerMarker RadialTargetRefresh
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialViewPublish"></a> RadialViewPublish

BRGが参照するCamera別Radial View Snapshot公開を計測します。

```csharp
public static readonly ProfilerMarker RadialViewPublish
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialViewPublishCommit"></a> RadialViewPublishCommit

Radial View mappingと世代正本のcommitを計測します。

```csharp
public static readonly ProfilerMarker RadialViewPublishCommit
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialViewPublishIdentity"></a> RadialViewPublishIdentity

Radial View公開時のCamera EntityId取得を計測します。

```csharp
public static readonly ProfilerMarker RadialViewPublishIdentity
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialViewPublishKeys"></a> RadialViewPublishKeys

Radial ViewのEntityIdを常駐ulong keyへ正規化します。

```csharp
public static readonly ProfilerMarker RadialViewPublishKeys
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialViewPublishLookup"></a> RadialViewPublishLookup

Radial Viewの常駐Entryと旧Camera mappingを検索します。

```csharp
public static readonly ProfilerMarker RadialViewPublishLookup
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialViewPublishSnapshot"></a> RadialViewPublishSnapshot

Radial View Snapshotのrevision採番と常駐Entry更新を計測します。

```csharp
public static readonly ProfilerMarker RadialViewPublishSnapshot
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialViewPublishValidation"></a> RadialViewPublishValidation

Radial View公開草案とCamera identityの検証を計測します。

```csharp
public static readonly ProfilerMarker RadialViewPublishValidation
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RadialWarningCallbacksCounterName"></a> RadialWarningCallbacksCounterName

Profiler上の互換警告callback数counter名です。

```csharp
public const string RadialWarningCallbacksCounterName = "Omni.Radial.Compatibility.WarningCallbacks"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_RenderPose"></a> RenderPose

Logical poseから描画姿勢を組み立てる処理を計測します。

```csharp
public static readonly ProfilerMarker RenderPose
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_SaturnBatchCulling"></a> SaturnBatchCulling

Saturn BRGのカメラ別可視粒子判定を計測します。

```csharp
public static readonly ProfilerMarker SaturnBatchCulling
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_SaturnEpochRebuild"></a> SaturnEpochRebuild

Saturnの時間窓epochセル索引の直接再構築を計測します。

```csharp
public static readonly ProfilerMarker SaturnEpochRebuild
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_SaturnInstanceWrite"></a> SaturnInstanceWrite

Saturn BRGのinstance data書き込みを計測します。

```csharp
public static readonly ProfilerMarker SaturnInstanceWrite
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_SaturnSequenceEvaluation"></a> SaturnSequenceEvaluation

Saturnの純粋なSequenceTime評価とFrameState生成を計測します。

```csharp
public static readonly ProfilerMarker SaturnSequenceEvaluation
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_SceneViewCameraBoundary"></a> SceneViewCameraBoundary

Scene View境界のRenderer登録キャッシュ判定を計測します。

```csharp
public static readonly ProfilerMarker SceneViewCameraBoundary
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_SceneViewFreeFlight"></a> SceneViewFreeFlight

Scene Viewの入力サンプルと自由飛行適用を計測します。

```csharp
public static readonly ProfilerMarker SceneViewFreeFlight
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_SceneViewGridBuild"></a> SceneViewGridBuild

Scene ViewグリッドPrimitive構築を計測します。

```csharp
public static readonly ProfilerMarker SceneViewGridBuild
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_SceneViewGridGpu"></a> SceneViewGridGpu

Scene ViewグリッドGPU提出と深度描画を計測します。

```csharp
public static readonly ProfilerMarker SceneViewGridGpu
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_SceneViewNavigationCommit"></a> SceneViewNavigationCommit

Scene Viewの論理カメラ状態を正本から物理状態へ反映する処理です。

```csharp
public static readonly ProfilerMarker SceneViewNavigationCommit
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_SceneViewNavigationGesture"></a> SceneViewNavigationGesture

Scene Viewの統一マウス操作ルーター全体です。

```csharp
public static readonly ProfilerMarker SceneViewNavigationGesture
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_SceneViewOverlayCoordinateRefresh"></a> SceneViewOverlayCoordinateRefresh

Navigator Overlayの座標・角度表示更新です。

```csharp
public static readonly ProfilerMarker SceneViewOverlayCoordinateRefresh
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_SceneViewOverlayExternalRefresh"></a> SceneViewOverlayExternalRefresh

Navigator Overlayの選択・設定・外部状態表示更新です。

```csharp
public static readonly ProfilerMarker SceneViewOverlayExternalRefresh
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_SceneViewOverlayProjectionRefresh"></a> SceneViewOverlayProjectionRefresh

Navigator Overlayの投影方式表示更新です。

```csharp
public static readonly ProfilerMarker SceneViewOverlayProjectionRefresh
```

#### 値（Field Value）

 ProfilerMarker

### <a id="Omni_Diagnostics_OmniPerformanceMarkers_TransformWorld"></a> TransformWorld

LogicalTransformのWorld変換・親子合成を計測します。

```csharp
public static readonly ProfilerMarker TransformWorld
```

#### 値（Field Value）

 ProfilerMarker
