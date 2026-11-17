# <a id="Omni_BatchRendering_RadialSceneBatchRendererService"></a> Class RadialSceneBatchRendererService

Namespace: [Omni.BatchRendering](Omni.BatchRendering.md)  
Assembly: Omni.BatchRendering.Runtime.dll  

Scene Mesh BRGのLifecycleを1か所で管理します。
Rebuild通知はdirty flagへ集約し、Renderer収集は安全なUpdate境界で1回だけ実行します。

```csharp
public static class RadialSceneBatchRendererService
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialSceneBatchRendererService](Omni.BatchRendering.RadialSceneBatchRendererService.md)

## プロパティ（Properties）

### <a id="Omni_BatchRendering_RadialSceneBatchRendererService_BackendGeneration"></a> BackendGeneration

backendの有効化・交換・解放を含む現在世代です。

```csharp
public static int BackendGeneration { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchRendererService_BackendState"></a> BackendState

現在のbackend状態です。

```csharp
public static RadialBatchBackendState BackendState { get; }
```

#### 値（Property Value）

 [RadialBatchBackendState](Omni.BatchRendering.RadialBatchBackendState.md)

### <a id="Omni_BatchRendering_RadialSceneBatchRendererService_IsActive"></a> IsActive

BRGが元MeshRendererの描画を所有しているかを返します。

```csharp
public static bool IsActive { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_BatchRendering_RadialSceneBatchRendererService_IsForwardRenderingBlocked"></a> IsForwardRenderingBlocked

Scene BRG が URP Forward の Camera のために止まり、Legacy（通常の Renderer）で描いている間 true です。
デモの HUD や Omni Manager が、理由を利用者へ説明するために読みます（<xref href="Omni.BatchRendering.OmniForwardLightingNotice" data-throw-if-not-resolved="false"></xref>）。

```csharp
public static bool IsForwardRenderingBlocked { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_BatchRendering_RadialSceneBatchRendererService_LastFailureReason"></a> LastFailureReason

直近の有効化失敗理由です。成功時は空文字列です。

```csharp
public static string LastFailureReason { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_BatchRendering_RadialSceneBatchRendererService_LastLightBatchId"></a> LastLightBatchId

直近のLight viewへ渡したcamera-specific BatchIDです。

```csharp
public static uint LastLightBatchId { get; }
```

#### 値（Property Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="Omni_BatchRendering_RadialSceneBatchRendererService_LastLightCameraPacketSlot"></a> LastLightCameraPacketSlot

直近のLight viewが参照した描画中Camera packet slotです。

```csharp
public static int LastLightCameraPacketSlot { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchRendererService_LastRebuildDetail"></a> LastRebuildDetail

Patch昇格など、列挙値を補足する直近の詳細です。

```csharp
public static string LastRebuildDetail { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_BatchRendering_RadialSceneBatchRendererService_LastRebuildReasons"></a> LastRebuildReasons

直近に全再構築を試みた原因です。差分Patchだけでは変化しません。

```csharp
public static RadialSceneBatchRebuildReason LastRebuildReasons { get; }
```

#### 値（Property Value）

 [RadialSceneBatchRebuildReason](Omni.BatchRendering.RadialSceneBatchRebuildReason.md)

### <a id="Omni_BatchRendering_RadialSceneBatchRendererService_LightCullingInvocationCount"></a> LightCullingInvocationCount

起動後にURP Light viewがScene BRGをカリングした回数です。

```csharp
public static int LightCullingInvocationCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchRendererService_RebuildAttemptCount"></a> RebuildAttemptCount

このDomainで全再構築を試みた累計回数です。

```csharp
public static int RebuildAttemptCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchRendererService_ResidentInstanceCount"></a> ResidentInstanceCount

BRGが所有するRenderer instance数です。

```csharp
public static int ResidentInstanceCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_BatchRendering_RadialSceneBatchRendererService_EnsureInitialized"></a> EnsureInitialized\(\)

RuntimeまたはEditorでScene BRG driverを初期化します。

```csharp
public static void EnsureInitialized()
```

### <a id="Omni_BatchRendering_RadialSceneBatchRendererService_NotifyRendererVisibilityChanged_UnityEngine_MeshRenderer_"></a> NotifyRendererVisibilityChanged\(MeshRenderer\)

Scene自動収集されたRendererのenabled変更を、次の安全な更新境界でresidentへ反映します。

```csharp
public static void NotifyRendererVisibilityChanged(MeshRenderer renderer)
```

#### 引数（Parameters）

`renderer` MeshRenderer

### <a id="Omni_BatchRendering_RadialSceneBatchRendererService_PrepareForEditorSceneTransition"></a> PrepareForEditorSceneTransition\(\)

Edit ModeのScene破棄が始まる前に、旧Scene Rendererの所有権とNative参照を解放します。
sceneOpened後の遅延rebuildだけでは、その間のDriver.Updateが破棄済みRendererへ触れるため、
EditorSceneManager.sceneClosingから同期的に呼ぶ必要があります。

```csharp
public static void PrepareForEditorSceneTransition()
```

### <a id="Omni_BatchRendering_RadialSceneBatchRendererService_ProcessPendingChanges"></a> ProcessPendingChanges\(\)

Editor自動検証など、既に安全な更新境界にいる呼び出し元が
保留中の再構築と常駐データ更新を明示的に消化します。

```csharp
public static void ProcessPendingChanges()
```

### <a id="Omni_BatchRendering_RadialSceneBatchRendererService_RequestRebuild"></a> RequestRebuild\(\)

次のUpdateでScene登録を原子的に再構築します。

```csharp
public static void RequestRebuild()
```

### <a id="Omni_BatchRendering_RadialSceneBatchRendererService_SetMode_Omni_BatchRendering_RadialSceneBatchBackendMode_"></a> SetMode\(RadialSceneBatchBackendMode\)

Legacy/BRGを明示的に切り替えます。

```csharp
public static void SetMode(RadialSceneBatchBackendMode mode)
```

#### 引数（Parameters）

`mode` [RadialSceneBatchBackendMode](Omni.BatchRendering.RadialSceneBatchBackendMode.md)
