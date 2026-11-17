# <a id="VirtualizedGeometry_IVirtualGeometryCompatibleRenderFeature"></a> Interface IVirtualGeometryCompatibleRenderFeature

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

互換featureはVGより前にgeometryを必要とする場合だけ、VGの描画を止める(通常の描画へ戻す)。

```csharp
public interface IVirtualGeometryCompatibleRenderFeature
```

## プロパティ（Properties）

### <a id="VirtualizedGeometry_IVirtualGeometryCompatibleRenderFeature_RequiresEarlyGeometry"></a> RequiresEarlyGeometry

```csharp
bool RequiresEarlyGeometry { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
