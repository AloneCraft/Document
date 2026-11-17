# <a id="VirtualizedGeometry_VirtualGeometryRenderFeature"></a> Class VirtualGeometryRenderFeature

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

VG の描画を URP の RenderGraph へ接続する。描くものは <xref href="VirtualizedGeometry.IVirtualGeometryDrawable" data-throw-if-not-resolved="false"></xref>(ビルド済みメッシュの <xref href="VirtualizedGeometry.VirtualGeometryRenderer" data-throw-if-not-resolved="false"></xref> と、
地形の Cell のように供給元 <xref href="VirtualizedGeometry.IVirtualGeometryDrawableProvider" data-throw-if-not-resolved="false"></xref> が camera ごとに渡す instance)で、どれも同じ階層選択(GPU)と間接描画を通る。
段は 3 つ。
1. prepass の直後(AfterRenderingPrePasses): 供給元の instance を、VG の深度の pass(DepthNormals か DepthOnly)で URP の prepass と同じ出力先へ描く
   (VG の面が SSAO・Decal(DBuffer)・Depth Priming の深度に入る。遮蔽の判定と 2 パス目は無い)。
2. 主光源の影: ビルド済みメッシュの cluster を cascade ごとに選び、ShadowCaster pass で影の texture へ描く。
3. 不透明の後(AfterRenderingOpaques): 階層選択、2 パスの遮蔽(前 frame に見えた cluster を先に描き、その深度の HZB で残りを判定)、forward pass の描画。
細分化の決め方は <xref href="VirtualizedGeometry.VirtualGeometryRenderFeature.RefineMode" data-throw-if-not-resolved="false"></xref>。対応しない camera では描かず、理由を残す(Fail Closed)。

```csharp
public sealed class VirtualGeometryRenderFeature : ScriptableRendererFeature, IDisposable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
ScriptableObject ← 
ScriptableRendererFeature ← 
[VirtualGeometryRenderFeature](VirtualizedGeometry.VirtualGeometryRenderFeature.md)

#### 実装するインターフェース（Implements）

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

## プロパティ（Properties）

### <a id="VirtualizedGeometry_VirtualGeometryRenderFeature_RefineMode"></a> RefineMode

cluster の DAG の細分化の決め方。変換器の版が古い asset は、この設定によらず <xref href="VirtualizedGeometry.VirtualGeometryRefineMode.Chained" data-throw-if-not-resolved="false"></xref>。

```csharp
public VirtualGeometryRefineMode RefineMode { get; set; }
```

#### 値（Property Value）

 [VirtualGeometryRefineMode](VirtualizedGeometry.VirtualGeometryRefineMode.md)

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometryRenderFeature_AddRenderPasses_UnityEngine_Rendering_Universal_ScriptableRenderer_UnityEngine_Rendering_Universal_RenderingData__"></a> AddRenderPasses\(ScriptableRenderer, ref RenderingData\)

```csharp
public override void AddRenderPasses(ScriptableRenderer renderer, ref RenderingData renderingData)
```

#### 引数（Parameters）

`renderer` ScriptableRenderer

`renderingData` RenderingData

### <a id="VirtualizedGeometry_VirtualGeometryRenderFeature_Create"></a> Create\(\)

```csharp
public override void Create()
```

### <a id="VirtualizedGeometry_VirtualGeometryRenderFeature_Dispose_System_Boolean_"></a> Dispose\(bool\)

```csharp
protected override void Dispose(bool disposing)
```

#### 引数（Parameters）

`disposing` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryRenderFeature_OnCameraPreCull_UnityEngine_Rendering_Universal_ScriptableRenderer_UnityEngine_Rendering_Universal_CameraData__"></a> OnCameraPreCull\(ScriptableRenderer, in CameraData\)

```csharp
public override void OnCameraPreCull(ScriptableRenderer renderer, in CameraData cameraData)
```

#### 引数（Parameters）

`renderer` ScriptableRenderer

`cameraData` CameraData
