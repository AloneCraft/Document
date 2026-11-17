# <a id="Omni_BatchRendering_RadialBatchRendererConfiguration"></a> Struct RadialBatchRendererConfiguration

Namespace: [Omni.BatchRendering](Omni.BatchRendering.md)  
Assembly: Omni.BatchRendering.Runtime.dll  

1つのMeso粒子contentをBRGで描画するための不変設定です。
Saturnシーンの <code>SaturnMesoBatchRenderer</code> がBuilderからMesh、専用Material、保守的な
global boundsを渡して構築します。Meso粒子はv1で動的影を落とさないため、adapterは
常にShadowCastingMode.Offのdraw rangeを生成します。

```csharp
public struct RadialBatchRendererConfiguration
```

## コンストラクター（Constructors）

### <a id="Omni_BatchRendering_RadialBatchRendererConfiguration__ctor_UnityEngine_Mesh_UnityEngine_Material_UnityEngine_Bounds_System_Int32_System_Int32_System_Byte_System_UInt32_System_Int32_UnityEngine_MotionVectorGenerationMode_UnityEngine_Rendering_ShadowCastingMode_System_Boolean_"></a> RadialBatchRendererConfiguration\(Mesh, Material, Bounds, int, int, byte, uint, int, MotionVectorGenerationMode, ShadowCastingMode, bool\)

設定を作成します。

```csharp
public RadialBatchRendererConfiguration(Mesh mesh, Material material, Bounds globalBounds, int residentInstanceCount, int submeshIndex = 0, byte layer = 0, uint renderingLayerMask = 1, int instanceRecordByteSize = 32, MotionVectorGenerationMode motionMode = MotionVectorGenerationMode.ForceNoMotion, ShadowCastingMode shadowCastingMode = ShadowCastingMode.Off, bool receiveShadows = false)
```

#### 引数（Parameters）

`mesh` Mesh

共有Mesh。nullではBRGを初期化せずMacroOnlyへ縮退します。

`material` Material

RadialBrgParticle.shader等のDOTS対応Material。nullでは縮退します。

`globalBounds` Bounds

全粒子を包むworld bounds。非有限または退化boundsでは縮退します。

`residentInstanceCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

sentinelを除く粒子数。Large/Residentでは100万を渡します。

`submeshIndex` [int](https://learn.microsoft.com/dotnet/api/system.int32)

描画するsubmesh。通常は0です。

`layer` [byte](https://learn.microsoft.com/dotnet/api/system.byte)

Unity layer。通常は0です。

`renderingLayerMask` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

URP rendering layer。通常は1です。

`instanceRecordByteSize` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`motionMode` MotionVectorGenerationMode

`shadowCastingMode` ShadowCastingMode

`receiveShadows` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## フィールド（Fields）

### <a id="Omni_BatchRendering_RadialBatchRendererConfiguration_GlobalBounds"></a> GlobalBounds

全Resident粒子を包む有限・保守的なglobal boundsです。

```csharp
public Bounds GlobalBounds
```

#### 値（Field Value）

 Bounds

### <a id="Omni_BatchRendering_RadialBatchRendererConfiguration_InstanceRecordByteSize"></a> InstanceRecordByteSize

RawBuffer 内の instance record byte 数です。既定は既存粒子互換の32です。

```csharp
public int InstanceRecordByteSize
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialBatchRendererConfiguration_Layer"></a> Layer

Unity layerです。CameraのcullingLayerMaskと整合させます。

```csharp
public byte Layer
```

#### 値（Field Value）

 [byte](https://learn.microsoft.com/dotnet/api/system.byte)

### <a id="Omni_BatchRendering_RadialBatchRendererConfiguration_Material"></a> Material

DOTS Instancing対応の専用BRG Materialです。

```csharp
public Material Material
```

#### 値（Field Value）

 Material

### <a id="Omni_BatchRendering_RadialBatchRendererConfiguration_Mesh"></a> Mesh

全粒子で共有するquadまたはlow-poly meshです。

```csharp
public Mesh Mesh
```

#### 値（Field Value）

 Mesh

### <a id="Omni_BatchRendering_RadialBatchRendererConfiguration_MotionMode"></a> MotionMode

draw range が要求する MotionVectors モードです。

```csharp
public MotionVectorGenerationMode MotionMode
```

#### 値（Field Value）

 MotionVectorGenerationMode

### <a id="Omni_BatchRendering_RadialBatchRendererConfiguration_ReceiveShadows"></a> ReceiveShadows

draw range が shadow を受けるかです。

```csharp
public bool ReceiveShadows
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_BatchRendering_RadialBatchRendererConfiguration_RenderingLayerMask"></a> RenderingLayerMask

URP rendering layer maskです。0は無効値です。

```csharp
public uint RenderingLayerMask
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="Omni_BatchRendering_RadialBatchRendererConfiguration_ResidentInstanceCount"></a> ResidentInstanceCount

sentinelを除く固定Resident粒子数です。

```csharp
public int ResidentInstanceCount
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialBatchRendererConfiguration_ShadowCastingMode"></a> ShadowCastingMode

draw range の shadow casting 設定です。

```csharp
public ShadowCastingMode ShadowCastingMode
```

#### 値（Field Value）

 ShadowCastingMode

### <a id="Omni_BatchRendering_RadialBatchRendererConfiguration_SubmeshIndex"></a> SubmeshIndex

描画するmesh submeshの0始まりindexです。

```csharp
public int SubmeshIndex
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)
