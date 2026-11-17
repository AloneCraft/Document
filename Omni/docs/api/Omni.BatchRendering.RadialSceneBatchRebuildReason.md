# <a id="Omni_BatchRendering_RadialSceneBatchRebuildReason"></a> Enum RadialSceneBatchRebuildReason

Namespace: [Omni.BatchRendering](Omni.BatchRendering.md)  
Assembly: Omni.BatchRendering.Runtime.dll  

Scene BRG backend全再構築を要求した原因です。複数通知は同じUpdateまで合成します。

```csharp
[Flags]
public enum RadialSceneBatchRebuildReason : ushort
```

## フィールド（Fields）

`BackendModeChanged = 128` 

`BackendUnavailable = 2048` 

`CameraRenderingPathChanged = 16384` 

`EditorManifestChanged = 4` 

`ExplicitRequest = 2` 

`HierarchyClassificationChanged = 512` 

`LightProbeSpaceChanged = 8192` 

`MeshBoundsInvariantRecovery = 4096` 

`None = 0` 

`PatchEscalation = 1024` 

`RegisteredRendererContractChanged = 16` 

`RendererBindingChanged = 32` 

`SceneLifecycleChanged = 256` 

`SceneManifestChanged = 8` 

`StableCacheDisabled = 64` 

`Startup = 1`
