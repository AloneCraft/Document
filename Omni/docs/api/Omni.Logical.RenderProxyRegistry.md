# <a id="Omni_Logical_RenderProxyRegistry"></a> Class RenderProxyRegistry

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

```csharp
[MovedFrom(true, "Omni", null, "LogicalRenderProxyRegistry")]
public static class RenderProxyRegistry
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RenderProxyRegistry](Omni.Logical.RenderProxyRegistry.md)

## プロパティ（Properties）

### <a id="Omni_Logical_RenderProxyRegistry_ProxyCount"></a> ProxyCount

現在カリング用Boundsを上書きしているRenderer数です。

```csharp
public static int ProxyCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_RenderProxyRegistry_UnsupportedCount"></a> UnsupportedCount

現在隔離している未対応Renderer数です。

```csharp
public static int UnsupportedCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_RenderProxyRegistry_UnsupportedDescriptions"></a> UnsupportedDescriptions

未対応RendererまたはMaterialの説明です。

```csharp
public static IReadOnlyCollection<string> UnsupportedDescriptions { get; }
```

#### 値（Property Value）

 [IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

## メソッド（Methods）

### <a id="Omni_Logical_RenderProxyRegistry_IsCullingBoundsOverridden_UnityEngine_Renderer_"></a> IsCullingBoundsOverridden\(Renderer\)

指定Rendererのカリング用Boundsを上書き中であればtrueです。
この対象はUnityから見ると実際の描画位置と無関係な箱なので、Unity標準編集空間の
位置しきい値で非表示にしてはいけません（隠すと安全域外のコンテンツが全て消えます）。

```csharp
public static bool IsCullingBoundsOverridden(Renderer renderer)
```

#### 引数（Parameters）

`renderer` Renderer

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_RenderProxyRegistry_IsSourceSuppressed_UnityEngine_Renderer_"></a> IsSourceSuppressed\(Renderer\)

元Rendererを未対応隔離で隠し続ける必要がある場合はtrueです。

```csharp
public static bool IsSourceSuppressed(Renderer source)
```

#### 引数（Parameters）

`source` Renderer

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_RenderProxyRegistry_Restore_UnityEngine_Renderer_"></a> Restore\(Renderer\)

指定元Rendererの一時状態を復元し、プロキシを破棄します。

```csharp
public static void Restore(Renderer source)
```

#### 引数（Parameters）

`source` Renderer

### <a id="Omni_Logical_RenderProxyRegistry_RestoreAll"></a> RestoreAll\(\)

全ての元状態を復元し、保存されないプロキシを破棄します。

```csharp
public static void RestoreAll()
```

### <a id="Omni_Logical_RenderProxyRegistry_RestoreMissing_System_Collections_Generic_ISet_UnityEngine_Renderer__"></a> RestoreMissing\(ISet<Renderer\>\)

現在の収集対象から外れた元Rendererだけを復元します。

```csharp
public static void RestoreMissing(ISet<Renderer> activeSources)
```

#### 引数（Parameters）

`activeSources` [ISet](https://learn.microsoft.com/dotnet/api/system.collections.generic.iset\-1)<Renderer\>

#### 補足（Remarks）

<xref href="Omni.Logical.RenderProxyRegistry.s_LastResults" data-throw-if-not-resolved="false"></xref> も同じ基準で捨てます。ここを掃除しないと、収集対象から
外れて<xref href="Omni.Logical.RenderProxyRegistry.TryPrepare(UnityEngine.Renderer%2cUnityEngine.Camera%2cOmni.Logical.RenderPose%40%2cUnityEngine.Renderer%40%2cOmni.Logical.PhysicalSafetyResult%40)" data-throw-if-not-resolved="false"></xref>が呼ばれなくなったRendererの判定が残り続け、
Omni Debugパネルの「経路 / 理由 / 実距離」が<b>更新の止まった古い値を出し続けます</b>
（エントリが在る限り「判定待ち」にもならないので、画面からは止まっていることが
分からない）。実際にこれで何度も誤った原因へ誘導されました。判定は毎フレーム
<xref href="Omni.Logical.RenderProxyRegistry.TryPrepare(UnityEngine.Renderer%2cUnityEngine.Camera%2cOmni.Logical.RenderPose%40%2cUnityEngine.Renderer%40%2cOmni.Logical.PhysicalSafetyResult%40)" data-throw-if-not-resolved="false"></xref>が作り直すので、捨てても次のフレームで復活します。

### <a id="Omni_Logical_RenderProxyRegistry_TryGetLastResult_UnityEngine_Renderer_Omni_Logical_PhysicalSafetyResult__"></a> TryGetLastResult\(Renderer, out PhysicalSafetyResult\)

直近の安全域判定を取得します。

```csharp
public static bool TryGetLastResult(Renderer source, out PhysicalSafetyResult result)
```

#### 引数（Parameters）

`source` Renderer

`result` [PhysicalSafetyResult](Omni.Logical.PhysicalSafetyResult.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_RenderProxyRegistry_TryGetLocalBounds_UnityEngine_Renderer_UnityEngine_Bounds__"></a> TryGetLocalBounds\(Renderer, out Bounds\)

RendererのMeshアセットからローカルBoundsを取得します。

```csharp
public static bool TryGetLocalBounds(Renderer source, out Bounds localBounds)
```

#### 引数（Parameters）

`source` Renderer

`localBounds` Bounds

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_RenderProxyRegistry_TryGetProxyDiagnostics_UnityEngine_Renderer_Omni_Logical_RenderProxyDiagnostics__"></a> TryGetProxyDiagnostics\(Renderer, out RenderProxyDiagnostics\)

選択対象の診断用に、有限描画プロキシの現在状態を返します。
プロキシ経路の対象が見えないとき、「同期が止まっている」「プロキシがカメラの至近にいない」
「元Rendererだけ抑制されてプロキシが無い」を切り分けるために使います。

```csharp
public static bool TryGetProxyDiagnostics(Renderer source, out RenderProxyDiagnostics diagnostics)
```

#### 引数（Parameters）

`source` Renderer

`diagnostics` [RenderProxyDiagnostics](Omni.Logical.RenderProxyDiagnostics.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_RenderProxyRegistry_TryPrepare_UnityEngine_Renderer_UnityEngine_Camera_Omni_Logical_RenderPose__UnityEngine_Renderer__Omni_Logical_PhysicalSafetyResult__"></a> TryPrepare\(Renderer, Camera, in RenderPose, out Renderer, out PhysicalSafetyResult\)

Rendererの論理AABBを評価し、安全域外なら有限プロキシを返します。
元RendererのTransform、Material、Scene、Prefabは変更しません。

```csharp
public static bool TryPrepare(Renderer source, Camera camera, in RenderPose pose, out Renderer renderTarget, out PhysicalSafetyResult safetyResult)
```

#### 引数（Parameters）

`source` Renderer

`camera` Camera

`pose` [RenderPose](Omni.Logical.RenderPose.md)

`renderTarget` Renderer

`safetyResult` [PhysicalSafetyResult](Omni.Logical.PhysicalSafetyResult.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_RenderProxyRegistry_TryPrepare_UnityEngine_Renderer_UnityEngine_Camera_Omni_Logical_RenderPose__UnityEngine_Vector3_UnityEngine_Renderer__Omni_Logical_PhysicalSafetyResult__"></a> TryPrepare\(Renderer, Camera, in RenderPose, Vector3, out Renderer, out PhysicalSafetyResult\)

旧cullingAnchorOffset引数を受け取る互換オーバーロードです。
引数は無視し、カメラ中心の有限プロキシBoundsへ委譲します。

```csharp
public static bool TryPrepare(Renderer source, Camera camera, in RenderPose pose, Vector3 _legacyCullingAnchorOffset, out Renderer renderTarget, out PhysicalSafetyResult safetyResult)
```

#### 引数（Parameters）

`source` Renderer

`camera` Camera

`pose` [RenderPose](Omni.Logical.RenderPose.md)

`_legacyCullingAnchorOffset` Vector3

`renderTarget` Renderer

`safetyResult` [PhysicalSafetyResult](Omni.Logical.PhysicalSafetyResult.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
