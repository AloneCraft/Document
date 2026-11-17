# <a id="VirtualizedGeometry_IVirtualGeometryInstancePlacement"></a> Interface IVirtualGeometryInstancePlacement

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

<xref href="VirtualizedGeometry.VirtualGeometryRenderer" data-throw-if-not-resolved="false"></xref> を、Transform の行列とは別の配置で描くための差し込み口(Omni の Logical 座標と対数描画など)。
同じ GameObject の component が実装する。無ければ、これまでどおり Transform の行列で world 空間に描く。
RenderFeature が camera ごと・frame ごとに、記録中(RenderGraph の記録、main thread)に呼ぶ。
返した姿勢で、LOD の選択と cull(<xref href="VirtualizedGeometry.VirtualGeometryInstancePose.CullSpace" data-throw-if-not-resolved="false"></xref> の空間)と描画(描画行列と MaterialPropertyBlock)を行う。

```csharp
public interface IVirtualGeometryInstancePlacement
```

## メソッド（Methods）

### <a id="VirtualizedGeometry_IVirtualGeometryInstancePlacement_TryDescribe_VirtualizedGeometry_VirtualGeometryRenderer_VirtualizedGeometry_VirtualGeometryClusterView__UnityEngine_MaterialPropertyBlock_VirtualizedGeometry_VirtualGeometryInstancePose__"></a> TryDescribe\(VirtualGeometryRenderer, in VirtualGeometryClusterView, MaterialPropertyBlock, out VirtualGeometryInstancePose\)

この camera での姿勢を求め、draw 専用の値(物体ごとの値など)を properties に書く。
properties は renderer×camera ごとに 1 つで、前の frame の値が残っている。描けないときは false を返し、この camera では描かない。

```csharp
bool TryDescribe(VirtualGeometryRenderer renderer, in VirtualGeometryClusterView view, MaterialPropertyBlock properties, out VirtualGeometryInstancePose pose)
```

#### 引数（Parameters）

`renderer` [VirtualGeometryRenderer](VirtualizedGeometry.VirtualGeometryRenderer.md)

`view` [VirtualGeometryClusterView](VirtualizedGeometry.VirtualGeometryClusterView.md)

`properties` MaterialPropertyBlock

`pose` [VirtualGeometryInstancePose](VirtualizedGeometry.VirtualGeometryInstancePose.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
