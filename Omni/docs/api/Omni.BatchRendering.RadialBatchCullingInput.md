# <a id="Omni_BatchRendering_RadialBatchCullingInput"></a> Struct RadialBatchCullingInput

Namespace: [Omni.BatchRendering](Omni.BatchRendering.md)  
Assembly: Omni.BatchRendering.Runtime.dll  

BRG callbackから粒子可視IDをJobとして求めるための安全な入力です。

<p>
この値はUnity Object、Material、GraphicsBuffer、unsafe pointerを含みません。
Saturn Coreはこの入力と不変Simulation Snapshotだけを読み、adapterが確保した出力領域へ
1始まりのinstance IDを書き込みます。ID 0はBRG direct drawの最小2件制約を満たす
退化sentinel専用です。
</p>

```csharp
public readonly struct RadialBatchCullingInput
```

## コンストラクター（Constructors）

### <a id="Omni_BatchRendering_RadialBatchCullingInput__ctor_Omni_BatchRendering_RadialBatchViewKey__System_UInt64_Omni_Rendering_Radial_Frustum__Omni_Logical_Scalar__Omni_Logical_Scalar__Unity_Collections_NativeArray_UnityEngine_Plane__Unity_Collections_NativeArray_UnityEngine_Rendering_CullingSplit__UnityEngine_Rendering_BatchCullingProjectionType_UnityEngine_Matrix4x4_System_Boolean_"></a> RadialBatchCullingInput\(in RadialBatchViewKey, ulong, in Frustum, in Scalar, in Scalar, NativeArray<Plane\>, NativeArray<CullingSplit\>, BatchCullingProjectionType, Matrix4x4, bool\)

入力を構築します。

```csharp
public RadialBatchCullingInput(in RadialBatchViewKey viewKey, ulong frameRevision, in Frustum logicalFrustum, in Scalar logicalNearClip, in Scalar logicalFarClip, NativeArray<Plane> cullingPlanes, NativeArray<CullingSplit> cullingSplits, BatchCullingProjectionType projectionType, Matrix4x4 localToWorldMatrix, bool forceAllVisible)
```

#### 引数（Parameters）

`viewKey` [RadialBatchViewKey](Omni.BatchRendering.RadialBatchViewKey.md)

現在のCamera viewを表すEntityId由来キー。無効値ではadapterがMacroOnlyへ縮退します。

`frameRevision` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

Camera SnapshotとGPU headerが一致すべきフレームrevisionです。

`logicalFrustum` Frustum

RadialViewSnapshot由来の論理錐台。無効値ならproviderは全Resident可視へ倒します。

`logicalNearClip` Scalar

RadialViewSnapshot由来の論理near clip。0以下ならfail-openです。

`logicalFarClip` Scalar

RadialViewSnapshot由来の論理far clip。0以下ならfail-openです。

`cullingPlanes` NativeArray<Plane\>

Unityが渡す読み取り専用錐台平面。Jobは返却するJobHandleへ必ず依存させます。

`cullingSplits` NativeArray<CullingSplit\>

Cameraのculling split。v1のCamera viewでは通常1件ですが配列長を仮定しません。

`projectionType` BatchCullingProjectionType

透視・平行投影を表すUnityのview種別です。

`localToWorldMatrix` Matrix4x4

Unity culling contextの局所→world行列です。粒子のlogical SoTはここへ依存しません。

`forceAllVisible` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

trueならNaN・stale context等のfail-openとして全Resident可視を返します。

## プロパティ（Properties）

### <a id="Omni_BatchRendering_RadialBatchCullingInput_CullingPlanes"></a> CullingPlanes

Unityが所有する読み取り専用のculling平面です。

```csharp
public NativeArray<Plane> CullingPlanes { get; }
```

#### 値（Property Value）

 NativeArray<Plane\>

### <a id="Omni_BatchRendering_RadialBatchCullingInput_CullingSplits"></a> CullingSplits

Unityが所有する読み取り専用のculling splitです。

```csharp
public NativeArray<CullingSplit> CullingSplits { get; }
```

#### 値（Property Value）

 NativeArray<CullingSplit\>

### <a id="Omni_BatchRendering_RadialBatchCullingInput_FarClip"></a> FarClip

RadialViewSnapshot由来の論理far clipです。0以下はfail-openとして扱います。

```csharp
public Scalar FarClip { get; }
```

#### 値（Property Value）

 Scalar

### <a id="Omni_BatchRendering_RadialBatchCullingInput_ForceAllVisible"></a> ForceAllVisible

adapterが精密判定を使わず全Resident表示を要求しているかです。

```csharp
public bool ForceAllVisible { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_BatchRendering_RadialBatchCullingInput_FrameRevision"></a> FrameRevision

Camera Snapshotと照合するフレームrevisionです。

```csharp
public ulong FrameRevision { get; }
```

#### 値（Property Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_BatchRendering_RadialBatchCullingInput_Frustum"></a> Frustum

RadialViewSnapshot由来の論理錐台です。無効値ならproviderは全Resident可視へ倒します。

```csharp
public Frustum Frustum { get; }
```

#### 値（Property Value）

 Frustum

### <a id="Omni_BatchRendering_RadialBatchCullingInput_LocalToWorldMatrix"></a> LocalToWorldMatrix

Unity culling contextの局所→world行列です。

```csharp
public Matrix4x4 LocalToWorldMatrix { get; }
```

#### 値（Property Value）

 Matrix4x4

### <a id="Omni_BatchRendering_RadialBatchCullingInput_NearClip"></a> NearClip

RadialViewSnapshot由来の論理near clipです。0以下はfail-openとして扱います。

```csharp
public Scalar NearClip { get; }
```

#### 値（Property Value）

 Scalar

### <a id="Omni_BatchRendering_RadialBatchCullingInput_ProjectionType"></a> ProjectionType

Cameraの投影種別です。

```csharp
public BatchCullingProjectionType ProjectionType { get; }
```

#### 値（Property Value）

 BatchCullingProjectionType

### <a id="Omni_BatchRendering_RadialBatchCullingInput_ViewKey"></a> ViewKey

現在のCamera viewキーです。

```csharp
public RadialBatchViewKey ViewKey { get; }
```

#### 値（Property Value）

 [RadialBatchViewKey](Omni.BatchRendering.RadialBatchViewKey.md)
