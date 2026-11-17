# <a id="VirtualizedGeometry_VirtualGeometryRenderer"></a> Class VirtualGeometryRenderer

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

通常のMeshFilter/MeshRendererとVirtual Geometryの描画をつなぐ非表示の部品。モデルのインポートで自動で付き、Inspectorには表示しない。
MeshFilterには低密度の代替Mesh(UE5のFallback Mesh相当)が入り、影・当たり判定・カリング・VGが使えないときの表示を受け持つ。

```csharp
[ExecuteAlways]
[DisallowMultipleComponent]
[RequireComponent(typeof(MeshFilter), typeof(MeshRenderer))]
[AddComponentMenu("")]
public sealed class VirtualGeometryRenderer : MonoBehaviour
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[VirtualGeometryRenderer](VirtualizedGeometry.VirtualGeometryRenderer.md)

## プロパティ（Properties）

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_DebugView"></a> DebugView

```csharp
public VirtualGeometryDebugView DebugView { get; }
```

#### 値（Property Value）

 [VirtualGeometryDebugView](VirtualizedGeometry.VirtualGeometryDebugView.md)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_DiagnosticCameraStateCount"></a> DiagnosticCameraStateCount

```csharp
public int DiagnosticCameraStateCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_DiagnosticDrewVirtualRecently"></a> DiagnosticDrewVirtualRecently

直近の数 frame に、この部品の専用描画(階層選択の描画)の項目を作ったか(Player の受入の確認用。GPU の読み戻しをしない)。

```csharp
public bool DiagnosticDrewVirtualRecently { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_DiagnosticGeometryAllocatedBytes"></a> DiagnosticGeometryAllocatedBytes

```csharp
public long DiagnosticGeometryAllocatedBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_DiagnosticMetadataAllocatedBytes"></a> DiagnosticMetadataAllocatedBytes

```csharp
public long DiagnosticMetadataAllocatedBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_DiagnosticReason"></a> DiagnosticReason

```csharp
public string DiagnosticReason { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_DiagnosticSelectionAllocatedBytes"></a> DiagnosticSelectionAllocatedBytes

```csharp
public long DiagnosticSelectionAllocatedBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_DiagnosticStatus"></a> DiagnosticStatus

専用描画に入れない理由や、読み込みの状況(診断用)。

```csharp
public string DiagnosticStatus { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_EnableFrustumCulling"></a> EnableFrustumCulling

```csharp
public bool EnableFrustumCulling { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_EnableOcclusionCulling"></a> EnableOcclusionCulling

```csharp
public bool EnableOcclusionCulling { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_IsFallbackVisible"></a> IsFallbackVisible

```csharp
public bool IsFallbackVisible { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_IsProxyForced"></a> IsProxyForced

検証・比較用に通常Proxy表示を強制する。compute未対応の検証overrideは変更しない。

```csharp
public bool IsProxyForced { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_IsStreamingRootReady"></a> IsStreamingRootReady

```csharp
public bool IsStreamingRootReady { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_LastVirtualDrawFrame"></a> LastVirtualDrawFrame

VG で描く項目を最後に出した frame(Time.frameCount、どの camera でも)。まだなら −1。表示の切り替えで、実際に描かれたかを知るのに使う。

```csharp
public int LastVirtualDrawFrame { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_LodErrorThresholdPixels"></a> LodErrorThresholdPixels

```csharp
public float LodErrorThresholdPixels { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_LodHysteresis"></a> LodHysteresis

```csharp
public float LodHysteresis { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_Materials"></a> Materials

```csharp
public Material[] Materials { get; }
```

#### 値（Property Value）

 Material\[\]

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_MeshAsset"></a> MeshAsset

```csharp
public VirtualGeometryMeshAsset MeshAsset { get; }
```

#### 値（Property Value）

 [VirtualGeometryMeshAsset](VirtualizedGeometry.VirtualGeometryMeshAsset.md)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_Ordinary"></a> Ordinary

```csharp
public MeshRenderer Ordinary { get; }
```

#### 値（Property Value）

 MeshRenderer

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_PhysicsProxy"></a> PhysicsProxy

```csharp
public MeshCollider PhysicsProxy { get; }
```

#### 値（Property Value）

 MeshCollider

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_Placement"></a> Placement

同じ GameObject の配置の差し込み口。無ければ null(Transform の行列で描く)。

```csharp
public IVirtualGeometryInstancePlacement Placement { get; }
```

#### 値（Property Value）

 [IVirtualGeometryInstancePlacement](VirtualizedGeometry.IVirtualGeometryInstancePlacement.md)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_ProxyFallback"></a> ProxyFallback

VG が描けない camera で、代替 Mesh(通常の MeshRenderer)を描くか。既定は true。
false にすると、VG が描けない間は何も描かない(通常の MeshRenderer が正しい位置に描けない配置、例えば Omni の対数描画で使う)。

```csharp
public bool ProxyFallback { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_SharedResourceCount"></a> SharedResourceCount

```csharp
public static int SharedResourceCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_SharedResourceKey"></a> SharedResourceKey

```csharp
public string SharedResourceKey { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_StreamingStatistics"></a> StreamingStatistics

```csharp
public VirtualGeometryStreamingStatistics StreamingStatistics { get; }
```

#### 値（Property Value）

 [VirtualGeometryStreamingStatistics](VirtualizedGeometry.VirtualGeometryStreamingStatistics.md)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_UseVirtualShadows"></a> UseVirtualShadows

主光源(Directional)の影を、Proxyではなく VG 自身の cluster で落とす。切ると Proxy の影に戻る。追加光源(Spot、Point)の影は VG では落とさない。

```csharp
public bool UseVirtualShadows { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_VirtualShadowActiveForDiagnostics"></a> VirtualShadowActiveForDiagnostics

```csharp
public bool VirtualShadowActiveForDiagnostics { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_WorldBounds"></a> WorldBounds

```csharp
public Bounds WorldBounds { get; }
```

#### 値（Property Value）

 Bounds

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_DiagnosticBatchTotals_UnityEngine_Camera_System_Int32__System_Int64__"></a> DiagnosticBatchTotals\(Camera, out int, out long\)

この page を camera で描く全 instance の、描いた三角形の合計と、描いた instance の数(診断用。1 回の読み戻し)。

```csharp
public void DiagnosticBatchTotals(Camera camera, out int drawnInstances, out long drawnTriangles)
```

#### 引数（Parameters）

`camera` Camera

`drawnInstances` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`drawnTriangles` [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_DiagnosticRequestArguments_UnityEngine_Camera_System_Action_System_UInt32____"></a> DiagnosticRequestArguments\(Camera, Action<uint\[\]\>\)

直近の描画の引数の行(1 パス目、2 パス目の順に、material ごとの 4 つ)を非同期に取る(Player の受入の確認用)。

```csharp
public void DiagnosticRequestArguments(Camera camera, Action<uint[]> completed)
```

#### 引数（Parameters）

`camera` Camera

`completed` [Action](https://learn.microsoft.com/dotnet/api/system.action\-1)<[uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]\>

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_DiagnosticRequestStatistics_UnityEngine_Camera_System_Action_System_UInt32____"></a> DiagnosticRequestStatistics\(Camera, Action<uint\[\]\>\)

直近の描画の統計(考慮・Frustum棄却・HZB棄却・可視)を非同期に取る。WebGPU でも使える(Player の受入の確認用)。

```csharp
public void DiagnosticRequestStatistics(Camera camera, Action<uint[]> completed)
```

#### 引数（Parameters）

`camera` Camera

`completed` [Action](https://learn.microsoft.com/dotnet/api/system.action\-1)<[uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]\>

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_DiagnosticSlot_UnityEngine_Camera_"></a> DiagnosticSlot\(Camera\)

この camera の batch の中の slot(診断用)。無ければ -1。

```csharp
public int DiagnosticSlot(Camera camera)
```

#### 引数（Parameters）

`camera` Camera

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_GetMaterial_System_Int32_"></a> GetMaterial\(int\)

slotのMaterial。通常MeshRendererに無ければ変換assetの白いURP Lit。

```csharp
public Material GetMaterial(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 Material

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_ReadDebugVerticesForDiagnostics_UnityEngine_Camera_"></a> ReadDebugVerticesForDiagnostics\(Camera\)

```csharp
public Vector4[] ReadDebugVerticesForDiagnostics(Camera camera)
```

#### 引数（Parameters）

`camera` Camera

#### 戻り値（Returns）

 Vector4\[\]

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_ReadMetricsForDiagnostics_UnityEngine_Camera_"></a> ReadMetricsForDiagnostics\(Camera\)

明示的な診断用同期readback。通常の描画/streamingからは呼ばない。

```csharp
public VirtualGeometryInstanceMetrics ReadMetricsForDiagnostics(Camera camera = null)
```

#### 引数（Parameters）

`camera` Camera

#### 戻り値（Returns）

 [VirtualGeometryInstanceMetrics](VirtualizedGeometry.VirtualGeometryInstanceMetrics.md)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_ReadbackSelectionForDiagnostics"></a> ReadbackSelectionForDiagnostics\(\)

```csharp
public VirtualGeometryGpuSelectionSnapshot ReadbackSelectionForDiagnostics()
```

#### 戻り値（Returns）

 [VirtualGeometryGpuSelectionSnapshot](VirtualizedGeometry.VirtualGeometryGpuSelectionSnapshot.md)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_ReadbackSelectionForDiagnostics_UnityEngine_Camera_"></a> ReadbackSelectionForDiagnostics\(Camera\)

```csharp
public VirtualGeometryGpuSelectionSnapshot ReadbackSelectionForDiagnostics(Camera camera)
```

#### 引数（Parameters）

`camera` Camera

#### 戻り値（Returns）

 [VirtualGeometryGpuSelectionSnapshot](VirtualizedGeometry.VirtualGeometryGpuSelectionSnapshot.md)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_ReadbackShadowSelectionForDiagnostics_UnityEngine_Camera_"></a> ReadbackShadowSelectionForDiagnostics\(Camera\)

主光源の影の選択状態を同期読み戻しする(診断用。最後に描いた cascade の結果)。

```csharp
public VirtualGeometryGpuSelectionSnapshot ReadbackShadowSelectionForDiagnostics(Camera camera)
```

#### 引数（Parameters）

`camera` Camera

#### 戻り値（Returns）

 [VirtualGeometryGpuSelectionSnapshot](VirtualizedGeometry.VirtualGeometryGpuSelectionSnapshot.md)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_RefreshAsset"></a> RefreshAsset\(\)

```csharp
public void RefreshAsset()
```

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_ReleaseResourcesForReload"></a> ReleaseResourcesForReload\(\)

Domain Reload前と検証の再初期化で、instance/camera資源を先に解放する。

```csharp
public static void ReleaseResourcesForReload()
```

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_RetryStreamingFailures"></a> RetryStreamingFailures\(\)

```csharp
public void RetryStreamingFailures()
```

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_SetCullingSettings_System_Boolean_System_Boolean_"></a> SetCullingSettings\(bool, bool\)

M3検証と比較表示でカリングを個別に切り替える。

```csharp
public void SetCullingSettings(bool frustum, bool occlusion)
```

#### 引数（Parameters）

`frustum` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`occlusion` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_SetDebugView_VirtualizedGeometry_VirtualGeometryDebugView_"></a> SetDebugView\(VirtualGeometryDebugView\)

```csharp
public void SetDebugView(VirtualGeometryDebugView view)
```

#### 引数（Parameters）

`view` [VirtualGeometryDebugView](VirtualizedGeometry.VirtualGeometryDebugView.md)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_SetFallbackOverride_System_Boolean_System_Boolean_"></a> SetFallbackOverride\(bool, bool\)

```csharp
public void SetFallbackOverride(bool forced, bool unsupported = false)
```

#### 引数（Parameters）

`forced` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`unsupported` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_SetLodSettings_System_Single_System_Single_"></a> SetLodSettings\(float, float\)

```csharp
public void SetLodSettings(float errorThresholdPixels, float hysteresis)
```

#### 引数（Parameters）

`errorThresholdPixels` [float](https://learn.microsoft.com/dotnet/api/system.single)

`hysteresis` [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_SetMaterials_UnityEngine_Material___"></a> SetMaterials\(params Material\[\]\)

submesh順のMaterialを通常MeshRendererへ設定する。VG描画も同じMaterialを使う。

```csharp
public void SetMaterials(params Material[] values)
```

#### 引数（Parameters）

`values` Material\[\]

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_SetMeshAsset_VirtualizedGeometry_VirtualGeometryMeshAsset_"></a> SetMeshAsset\(VirtualGeometryMeshAsset\)

```csharp
public void SetMeshAsset(VirtualGeometryMeshAsset asset)
```

#### 引数（Parameters）

`asset` [VirtualGeometryMeshAsset](VirtualizedGeometry.VirtualGeometryMeshAsset.md)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_SetProxyOptions_System_Boolean_System_Boolean_"></a> SetProxyOptions\(bool, bool\)

影の有無を通常MeshRendererへ、低密度の当たり判定をMeshColliderとして設定する。

```csharp
public void SetProxyOptions(bool shadow, bool physics)
```

#### 引数（Parameters）

`shadow` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`physics` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_SetStreamingConfiguration_VirtualizedGeometry_VirtualGeometryStreamingMode_VirtualizedGeometry_VirtualGeometryStreamingSettings_"></a> SetStreamingConfiguration\(VirtualGeometryStreamingMode, VirtualGeometryStreamingSettings\)

```csharp
public void SetStreamingConfiguration(VirtualGeometryStreamingMode mode, VirtualGeometryStreamingSettings settings)
```

#### 引数（Parameters）

`mode` [VirtualGeometryStreamingMode](VirtualizedGeometry.VirtualGeometryStreamingMode.md)

`settings` [VirtualGeometryStreamingSettings](VirtualizedGeometry.VirtualGeometryStreamingSettings.md)

### <a id="VirtualizedGeometry_VirtualGeometryRenderer_SharesStreamingResourceWith_VirtualizedGeometry_VirtualGeometryRenderer_"></a> SharesStreamingResourceWith\(VirtualGeometryRenderer\)

```csharp
public bool SharesStreamingResourceWith(VirtualGeometryRenderer other)
```

#### 引数（Parameters）

`other` [VirtualGeometryRenderer](VirtualizedGeometry.VirtualGeometryRenderer.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
