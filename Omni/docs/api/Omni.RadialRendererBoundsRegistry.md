# <a id="Omni_RadialRendererBoundsRegistry"></a> Class RadialRendererBoundsRegistry

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

Radial描画用の保守BoundsをRendererへ適用し、Camera間では再利用しながら
現viewで触られなかった対象だけを元のBoundsへ戻すRegistryです。
Galaxy、Gardenなど通常MeshRendererのUnity標準カリング経路で使い、BRGは扱いません。

```csharp
public static class RadialRendererBoundsRegistry
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialRendererBoundsRegistry](Omni.RadialRendererBoundsRegistry.md)

## プロパティ（Properties）

### <a id="Omni_RadialRendererBoundsRegistry_AppliedCount"></a> AppliedCount

現在保守Boundsを適用しているRenderer数です。

```csharp
public static int AppliedCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_RadialRendererBoundsRegistry_CachedRecordCount"></a> CachedRecordCount

現在再利用可能なRecord数です。

```csharp
public static int CachedRecordCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_RadialRendererBoundsRegistry_CurrentScopeRevision"></a> CurrentScopeRevision

現在のview revisionを返します。

```csharp
public static int CurrentScopeRevision { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_RadialRendererBoundsRegistry_SharedFailOpenCount"></a> SharedFailOpenCount

Camera非依存の有限fail-open world Boundsを保持するshared Renderer数です。

```csharp
public static int SharedFailOpenCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_RadialRendererBoundsRegistry_AbortScope"></a> AbortScope\(\)

未完了viewを破棄し、元Boundsへ完全復元してRecordも解放します。
例外、Scene unload、Assembly Reload、Editor終了の境界で使用します。

```csharp
public static void AbortScope()
```

### <a id="Omni_RadialRendererBoundsRegistry_BeginScope"></a> BeginScope\(\)

1回のCamera viewを開始します。未完了viewがあれば差分確定してから新しいrevisionへ進めます。
通常Camera間ではRecordと適用済みBoundsを保持するため、managed allocationを発生させません。

```csharp
public static void BeginScope()
```

### <a id="Omni_RadialRendererBoundsRegistry_EndScope"></a> EndScope\(\)

現viewを終了します。現viewで触られたBoundsは次のCameraまで保持し、
前viewにだけ存在したmissing Rendererを差分復元します。

```csharp
public static void EndScope()
```

### <a id="Omni_RadialRendererBoundsRegistry_GetDiagnostics"></a> GetDiagnostics\(\)

現在のRegistry診断値を返します。

```csharp
public static RadialRendererBoundsRegistry.Diagnostics GetDiagnostics()
```

#### 戻り値（Returns）

 [RadialRendererBoundsRegistry](Omni.RadialRendererBoundsRegistry.md).[Diagnostics](Omni.RadialRendererBoundsRegistry.Diagnostics.md)

### <a id="Omni_RadialRendererBoundsRegistry_IsApplied_UnityEngine_Renderer_"></a> IsApplied\(Renderer\)

指定Rendererが保守Boundsを適用中かを返します。

```csharp
public static bool IsApplied(Renderer renderer)
```

#### 引数（Parameters）

`renderer` Renderer

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_RadialRendererBoundsRegistry_RelinquishPreservingCurrent_UnityEngine_Renderer_"></a> RelinquishPreservingCurrent\(Renderer\)

Logical proxyなど別のBounds所有者へ移るとき、現在値を一切書き戻さずRadial適用状態を放棄します。
現在値は次回Radial適用時の復元先として保持します。

```csharp
public static void RelinquishPreservingCurrent(Renderer renderer)
```

#### 引数（Parameters）

`renderer` Renderer

### <a id="Omni_RadialRendererBoundsRegistry_Restore_UnityEngine_Renderer_"></a> Restore\(Renderer\)

指定Rendererだけを元Boundsへ戻します。Recordは次回適用のため再利用します。

```csharp
public static void Restore(Renderer renderer)
```

#### 引数（Parameters）

`renderer` Renderer

復元するRenderer。nullなら何もしません。

### <a id="Omni_RadialRendererBoundsRegistry_RestoreActiveBounds"></a> RestoreActiveBounds\(\)

identity／非Radial Cameraへの遷移時に、適用中Boundsだけを元へ戻します。
RecordとList容量は保持するため、次のRadial Cameraで再割当しません。

```csharp
public static void RestoreActiveBounds()
```

### <a id="Omni_RadialRendererBoundsRegistry_RestoreAll"></a> RestoreAll\(\)

全Rendererを元Boundsへ復元し、永続Recordも破棄します。

```csharp
public static void RestoreAll()
```

### <a id="Omni_RadialRendererBoundsRegistry_RestoreMissing_System_Collections_Generic_ISet_UnityEngine_Renderer__"></a> RestoreMissing\(ISet<Renderer\>\)

登録元一覧から外れたRendererを復元し、再利用Recordからも除去します。
一時的なworld Boundsの記録も同じ条件で掃除します。
dirty時専用で、Camera/Repaint Hot Pathからは呼びません。

```csharp
public static void RestoreMissing(ISet<Renderer> activeRenderers)
```

#### 引数（Parameters）

`activeRenderers` [ISet](https://learn.microsoft.com/dotnet/api/system.collections.generic.iset\-1)<Renderer\>

引き続き登録されるRenderer集合。nullなら全破棄します。

### <a id="Omni_RadialRendererBoundsRegistry_TryApply_UnityEngine_Renderer_UnityEngine_Bounds__"></a> TryApply\(Renderer, in Bounds\)

RendererへGPU変形後のワールドBoundsを適用します。同一world/local Boundsがbit一致する場合は、
8点逆変換とRenderer.localBoundsのネイティブ書込みを省略します。

```csharp
public static bool TryApply(Renderer renderer, in Bounds worldBounds)
```

#### 引数（Parameters）

`renderer` Renderer

適用先Renderer。nullならfalseです。

`worldBounds` Bounds

GPU変形後を保守的に包む有限ワールドBoundsです。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

適用済み状態を保証できた場合はtrueです。厳密一致で書込みを省略した場合もtrueです。

### <a id="Omni_RadialRendererBoundsRegistry_TryGetAppliedBounds_UnityEngine_Renderer_UnityEngine_Bounds__"></a> TryGetAppliedBounds\(Renderer, out Bounds\)

指定Rendererへ最後に適用したワールドBoundsを返します。

```csharp
public static bool TryGetAppliedBounds(Renderer renderer, out Bounds worldBounds)
```

#### 引数（Parameters）

`renderer` Renderer

`worldBounds` Bounds

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
