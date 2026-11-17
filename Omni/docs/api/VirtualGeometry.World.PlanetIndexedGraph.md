# <a id="VirtualGeometry_World_PlanetIndexedGraph"></a> Class PlanetIndexedGraph

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

共有index描画のGraph部分。placement・材質・lightingは呼び出し元の既存契約で準備する。

```csharp
public static class PlanetIndexedGraph
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetIndexedGraph](VirtualGeometry.World.PlanetIndexedGraph.md)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetIndexedGraph_Record_UnityEngine_Rendering_RenderGraphModule_RenderGraph_VirtualGeometry_World_PlanetIndexedBatch_UnityEngine_ComputeShader_UnityEngine_Rendering_RenderGraphModule_BufferHandle_UnityEngine_Rendering_RenderGraphModule_BufferHandle_UnityEngine_Rendering_RenderGraphModule_TextureHandle_UnityEngine_Rendering_RenderGraphModule_TextureHandle_UnityEngine_Material_System_Int32_UnityEngine_MaterialPropertyBlock_UnityEngine_Matrix4x4_UnityEngine_Matrix4x4_UnityEngine_Vector4___System_Single_System_Boolean_System_Boolean_System_Boolean_UnityEngine_GraphicsBuffer_UnityEngine_GraphicsBuffer_"></a> Record\(RenderGraph, PlanetIndexedBatch, ComputeShader, BufferHandle, BufferHandle, TextureHandle, TextureHandle, Material, int, MaterialPropertyBlock, Matrix4x4, Matrix4x4, Vector4\[\], float, bool, bool, bool, GraphicsBuffer, GraphicsBuffer\)

頂点とboundsは上位Graphでimport済みの同一handleを渡す。
propertiesはこのCamera専用で、Graph実行完了まで他Cameraが変更してはならない。
source shaderにSV_InstanceID対応のVG adapterが必要。未対応材質からは呼ばない。

```csharp
public static void Record(RenderGraph graph, PlanetIndexedBatch batch, ComputeShader cullShader, BufferHandle vertices, BufferHandle bounds, TextureHandle color, TextureHandle depth, Material material, int pass, MaterialPropertyBlock properties, Matrix4x4 anchorToWorld, Matrix4x4 anchorToCull, Vector4[] planes, float maximumScale, bool frustum, bool invertCulling, bool readGlobalTextures = true, GraphicsBuffer terrainWords = null, GraphicsBuffer terrainStorage = null)
```

#### 引数（Parameters）

`graph` RenderGraph

`batch` [PlanetIndexedBatch](VirtualGeometry.World.PlanetIndexedBatch.md)

`cullShader` ComputeShader

`vertices` BufferHandle

`bounds` BufferHandle

`color` TextureHandle

`depth` TextureHandle

`material` Material

`pass` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`properties` MaterialPropertyBlock

`anchorToWorld` Matrix4x4

`anchorToCull` Matrix4x4

`planes` Vector4\[\]

`maximumScale` [float](https://learn.microsoft.com/dotnet/api/system.single)

`frustum` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`invertCulling` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`readGlobalTextures` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`terrainWords` GraphicsBuffer

`terrainStorage` GraphicsBuffer
