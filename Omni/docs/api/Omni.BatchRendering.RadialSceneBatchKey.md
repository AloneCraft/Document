# <a id="Omni_BatchRendering_RadialSceneBatchKey"></a> Struct RadialSceneBatchKey

Namespace: [Omni.BatchRendering](Omni.BatchRendering.md)  
Assembly: Omni.BatchRendering.Runtime.dll  

同じBRG Draw CommandへまとめられるMeshRenderer submeshの不変キーです。
Rendererの位置はinstance dataなのでキーに含めません。

```csharp
public readonly struct RadialSceneBatchKey : IEquatable<RadialSceneBatchKey>, IComparable<RadialSceneBatchKey>
```

#### 実装するインターフェース（Implements）

[IEquatable<RadialSceneBatchKey\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1), 
[IComparable<RadialSceneBatchKey\>](https://learn.microsoft.com/dotnet/api/system.icomparable\-1)

## コンストラクター（Constructors）

### <a id="Omni_BatchRendering_RadialSceneBatchKey__ctor_System_Int32_System_Int32_System_Int32_System_Int32_System_Int32_System_UInt32_System_Int32_UnityEngine_Rendering_ShadowCastingMode_System_Boolean_System_Boolean_UnityEngine_MotionVectorGenerationMode_System_Int32_System_Boolean_System_Int32_System_Int32_System_UInt64_"></a> RadialSceneBatchKey\(int, int, int, int, int, uint, int, ShadowCastingMode, bool, bool, MotionVectorGenerationMode, int, bool, int, int, ulong\)

描画状態からBatch keyを作成します。

```csharp
public RadialSceneBatchKey(int meshInstanceId, int materialInstanceId, int submeshIndex, int renderQueue, int layer, uint renderingLayerMask, int lightmapIndex, ShadowCastingMode shadowCastingMode, bool receiveShadows, bool staticShadowCaster, MotionVectorGenerationMode motionMode, int rendererPriority, bool transparent, int lightProbeUsage = 0, int reflectionProbeUsage = 0, ulong sceneCullingMask = 0)
```

#### 引数（Parameters）

`meshInstanceId` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`materialInstanceId` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`submeshIndex` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`renderQueue` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`layer` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`renderingLayerMask` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`lightmapIndex` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`shadowCastingMode` ShadowCastingMode

`receiveShadows` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`staticShadowCaster` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`motionMode` MotionVectorGenerationMode

`rendererPriority` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`transparent` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`lightProbeUsage` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`reflectionProbeUsage` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`sceneCullingMask` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

## プロパティ（Properties）

### <a id="Omni_BatchRendering_RadialSceneBatchKey_Layer"></a> Layer

GameObject layerです。

```csharp
public int Layer { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchKey_LightProbeUsage"></a> LightProbeUsage

Light Probe利用方式の整数値です。

```csharp
public int LightProbeUsage { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchKey_LightmapIndex"></a> LightmapIndex

Unity lightmap indexです。未使用は負数です。

```csharp
public int LightmapIndex { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchKey_MaterialInstanceId"></a> MaterialInstanceId

BRG sidecar MaterialのUnity instance IDです。

```csharp
public int MaterialInstanceId { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchKey_MeshInstanceId"></a> MeshInstanceId

共有MeshのUnity instance IDです。

```csharp
public int MeshInstanceId { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchKey_MotionMode"></a> MotionMode

Motion Vector生成方式です。

```csharp
public MotionVectorGenerationMode MotionMode { get; }
```

#### 値（Property Value）

 MotionVectorGenerationMode

### <a id="Omni_BatchRendering_RadialSceneBatchKey_ReceiveShadows"></a> ReceiveShadows

影を受けるかどうかです。

```csharp
public bool ReceiveShadows { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_BatchRendering_RadialSceneBatchKey_ReflectionProbeUsage"></a> ReflectionProbeUsage

Reflection Probe利用方式の整数値です。

```csharp
public int ReflectionProbeUsage { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchKey_RenderQueue"></a> RenderQueue

Materialのrender queueです。

```csharp
public int RenderQueue { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchKey_RendererPriority"></a> RendererPriority

URP renderer priorityです。

```csharp
public int RendererPriority { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchKey_RenderingLayerMask"></a> RenderingLayerMask

URP rendering layer maskです。

```csharp
public uint RenderingLayerMask { get; }
```

#### 値（Property Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="Omni_BatchRendering_RadialSceneBatchKey_SceneCullingMask"></a> SceneCullingMask

Editor Scene可視性に使用するAuthoring GameObjectのmaskです。

```csharp
public ulong SceneCullingMask { get; }
```

#### 値（Property Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_BatchRendering_RadialSceneBatchKey_ShadowCastingMode"></a> ShadowCastingMode

Shadow caster設定です。

```csharp
public ShadowCastingMode ShadowCastingMode { get; }
```

#### 値（Property Value）

 ShadowCastingMode

### <a id="Omni_BatchRendering_RadialSceneBatchKey_StaticShadowCaster"></a> StaticShadowCaster

cached shadow map向けのstatic casterかどうかです。

```csharp
public bool StaticShadowCaster { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_BatchRendering_RadialSceneBatchKey_SubmeshIndex"></a> SubmeshIndex

Mesh内のsubmesh indexです。

```csharp
public int SubmeshIndex { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchKey_Transparent"></a> Transparent

透明ソートが必要なMaterialかどうかです。

```csharp
public bool Transparent { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_BatchRendering_RadialSceneBatchKey_CompareTo_Omni_BatchRendering_RadialSceneBatchKey_"></a> CompareTo\(RadialSceneBatchKey\)

```csharp
public int CompareTo(RadialSceneBatchKey other)
```

#### 引数（Parameters）

`other` [RadialSceneBatchKey](Omni.BatchRendering.RadialSceneBatchKey.md)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchKey_Equals_Omni_BatchRendering_RadialSceneBatchKey_"></a> Equals\(RadialSceneBatchKey\)

```csharp
public bool Equals(RadialSceneBatchKey other)
```

#### 引数（Parameters）

`other` [RadialSceneBatchKey](Omni.BatchRendering.RadialSceneBatchKey.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_BatchRendering_RadialSceneBatchKey_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object obj)
```

#### 引数（Parameters）

`obj` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_BatchRendering_RadialSceneBatchKey_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchKey_WithSubmeshIndex_System_Int32_"></a> WithSubmeshIndex\(int\)

submeshだけを置き換えたkeyを返します。

```csharp
public RadialSceneBatchKey WithSubmeshIndex(int submeshIndex)
```

#### 引数（Parameters）

`submeshIndex` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [RadialSceneBatchKey](Omni.BatchRendering.RadialSceneBatchKey.md)

### <a id="Omni_BatchRendering_RadialSceneBatchKey_WithTransparency_System_Boolean_System_Int32_"></a> WithTransparency\(bool, int\)

透明状態とrender queueだけを置き換えたkeyを返します。

```csharp
public RadialSceneBatchKey WithTransparency(bool transparent, int renderQueue)
```

#### 引数（Parameters）

`transparent` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`renderQueue` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [RadialSceneBatchKey](Omni.BatchRendering.RadialSceneBatchKey.md)

## 演算子（Operators）

### <a id="Omni_BatchRendering_RadialSceneBatchKey_op_Equality_Omni_BatchRendering_RadialSceneBatchKey_Omni_BatchRendering_RadialSceneBatchKey_"></a> operator ==\(RadialSceneBatchKey, RadialSceneBatchKey\)

2つのkeyが同じBatchを表すかを返します。

```csharp
public static bool operator ==(RadialSceneBatchKey left, RadialSceneBatchKey right)
```

#### 引数（Parameters）

`left` [RadialSceneBatchKey](Omni.BatchRendering.RadialSceneBatchKey.md)

`right` [RadialSceneBatchKey](Omni.BatchRendering.RadialSceneBatchKey.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_BatchRendering_RadialSceneBatchKey_op_Inequality_Omni_BatchRendering_RadialSceneBatchKey_Omni_BatchRendering_RadialSceneBatchKey_"></a> operator \!=\(RadialSceneBatchKey, RadialSceneBatchKey\)

2つのkeyが異なるBatchを表すかを返します。

```csharp
public static bool operator !=(RadialSceneBatchKey left, RadialSceneBatchKey right)
```

#### 引数（Parameters）

`left` [RadialSceneBatchKey](Omni.BatchRendering.RadialSceneBatchKey.md)

`right` [RadialSceneBatchKey](Omni.BatchRendering.RadialSceneBatchKey.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
