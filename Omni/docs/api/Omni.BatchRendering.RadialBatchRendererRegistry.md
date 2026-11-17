# <a id="Omni_BatchRendering_RadialBatchRendererRegistry"></a> Class RadialBatchRendererRegistry

Namespace: [Omni.BatchRendering](Omni.BatchRendering.md)  
Assembly: Omni.BatchRendering.Runtime.dll  

ランタイム生成MeshRendererをScene BRGへ登録する公開窓口です。
Sceneに保存されたMeshRendererはbackendが自動登録するため、このAPIは生成物専用です。

```csharp
public static class RadialBatchRendererRegistry
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialBatchRendererRegistry](Omni.BatchRendering.RadialBatchRendererRegistry.md)

## プロパティ（Properties）

### <a id="Omni_BatchRendering_RadialBatchRendererRegistry_Mode"></a> Mode

現在選択中のScene Mesh backendです。

```csharp
public static RadialSceneBatchBackendMode Mode { get; set; }
```

#### 値（Property Value）

 [RadialSceneBatchBackendMode](Omni.BatchRendering.RadialSceneBatchBackendMode.md)

### <a id="Omni_BatchRendering_RadialBatchRendererRegistry_RegisteredRendererCount"></a> RegisteredRendererCount

現在有効な明示登録Renderer数です。

```csharp
public static int RegisteredRendererCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_BatchRendering_RadialBatchRendererRegistry_MarkDirty_Omni_BatchRendering_RadialBatchInstanceHandle_Omni_BatchRendering_RadialBatchDirtyFlags_"></a> MarkDirty\(RadialBatchInstanceHandle, RadialBatchDirtyFlags\)

指定入力だけを次の安全な更新境界で再評価します。
Renderer.enabled変更後はVisibilityを通知してください。

```csharp
public static bool MarkDirty(RadialBatchInstanceHandle handle, RadialBatchDirtyFlags flags = RadialBatchDirtyFlags.All)
```

#### 引数（Parameters）

`handle` [RadialBatchInstanceHandle](Omni.BatchRendering.RadialBatchInstanceHandle.md)

`flags` [RadialBatchDirtyFlags](Omni.BatchRendering.RadialBatchDirtyFlags.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_BatchRendering_RadialBatchRendererRegistry_Register_UnityEngine_MeshRenderer_Omni_BatchRendering_IRadialBatchInstanceDataProvider_"></a> Register\(MeshRenderer, IRadialBatchInstanceDataProvider\)

ランタイム生成Rendererを登録します。

```csharp
public static RadialBatchInstanceHandle Register(MeshRenderer renderer, IRadialBatchInstanceDataProvider provider = null)
```

#### 引数（Parameters）

`renderer` MeshRenderer

`provider` [IRadialBatchInstanceDataProvider](Omni.BatchRendering.IRadialBatchInstanceDataProvider.md)

#### 戻り値（Returns）

 [RadialBatchInstanceHandle](Omni.BatchRendering.RadialBatchInstanceHandle.md)

### <a id="Omni_BatchRendering_RadialBatchRendererRegistry_Unregister_Omni_BatchRendering_RadialBatchInstanceHandle_"></a> Unregister\(RadialBatchInstanceHandle\)

世代が一致するランタイムRenderer登録を解除します。
生存中Rendererは通常描画へ戻し、再RegisterされるまでScene自動収集からも除外します。

```csharp
public static bool Unregister(RadialBatchInstanceHandle handle)
```

#### 引数（Parameters）

`handle` [RadialBatchInstanceHandle](Omni.BatchRendering.RadialBatchInstanceHandle.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
