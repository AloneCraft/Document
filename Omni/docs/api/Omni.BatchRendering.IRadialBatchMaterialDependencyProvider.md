# <a id="Omni_BatchRendering_IRadialBatchMaterialDependencyProvider"></a> Interface IRadialBatchMaterialDependencyProvider

Namespace: [Omni.BatchRendering](Omni.BatchRendering.md)  
Assembly: Omni.BatchRendering.Runtime.dll  

Play時に生成するbatch MaterialのAuthoring依存をEditor生成器へ申告します。

```csharp
public interface IRadialBatchMaterialDependencyProvider
```

## メソッド（Methods）

### <a id="Omni_BatchRendering_IRadialBatchMaterialDependencyProvider_CollectBatchMaterialDependencies_System_Collections_Generic_List_UnityEngine_Material__"></a> CollectBatchMaterialDependencies\(List<Material\>\)

sidecar生成が必要な正本Materialを追加します。

```csharp
void CollectBatchMaterialDependencies(List<Material> destination)
```

#### 引数（Parameters）

`destination` [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<Material\>
