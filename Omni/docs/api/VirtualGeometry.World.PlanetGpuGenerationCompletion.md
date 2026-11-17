# <a id="VirtualGeometry_World_PlanetGpuGenerationCompletion"></a> Enum PlanetGpuGenerationCompletion

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

GPU書込み完了後に、生成要求の所有者が実行する遷移。

```csharp
public enum PlanetGpuGenerationCompletion
```

## フィールド（Fields）

`Ignored = 0` 

`PromoteCpu = 4` 

`PublishReady = 1` 

`Released = 3` 

`Retry = 2` 

`Stale = 5`
