# <a id="Omni_BatchRendering_RadialBatchDirtyFlags"></a> Enum RadialBatchDirtyFlags

Namespace: [Omni.BatchRendering](Omni.BatchRendering.md)  
Assembly: Omni.BatchRendering.Runtime.dll  

BRG instanceのどの入力が変わったかを表します。

```csharp
[Flags]
public enum RadialBatchDirtyFlags : byte
```

## フィールド（Fields）

`All = 63` 

すべての入力を再評価します。



`Filtering = 4` 

Layer、Shadow、Lightmap、Motionなどのfilter設定が変わりました。



`GeometryOrMaterial = 2` 

Mesh、SubMesh、MaterialまたはMaterial propertyが変わりました。



`MeshBinding = 32` 

同じRendererのMesh参照だけを差し替えます。Material、SubMeshの材質対応、
filtering、Transform、Logical分類は不変でなければなりません。



`MeshVertexData = 16` 

同じMeshの頂点内容とBoundsだけが変わりました。Mesh/SubMesh構成・材質は不変です。
共有Meshの場合は影響する各Rendererへ通知します。UVだけの変更には通知不要です。



`None = 0` 

変更はありません。



`Transform = 1` 

TransformまたはLogicalTransformが変わりました。



`Visibility = 8` 

Renderer.enabledまたはGameObjectのactive状態が変わりました。
