# <a id="Omni_BatchRendering_RadialBatchRendererAdapter"></a> Class RadialBatchRendererAdapter

Namespace: [Omni.BatchRendering](Omni.BatchRendering.md)  
Assembly: Omni.BatchRendering.Runtime.dll  

Camera viewごとのRawBuffer、BatchID、frame revisionを束ねる共通BRG adapterです。

<p>
BatchRendererGroupのcallbackはCamera viewだけを受け、viewID（EntityId）別にBatchIDと
GPU bufferを分離します。providerは安全なNativeArrayだけへ可視IDを書き、unsafeな
TempJob出力領域、BatchDrawCommand、BRG登録解除はすべて本adapterが所有します。
</p>
<p>
Scene: Assets/Omni/Development/Legacy/Saturn/Saturn.unity の <code>SaturnMesoBatchRenderer</code>。
Builder: SaturnSceneBuilder。Game/Scene/比較CameraのA→B→A描画で資源が混ざらないことを
GPUテストが検証します。
</p>

```csharp
public sealed class RadialBatchRendererAdapter : IDisposable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialBatchRendererAdapter](Omni.BatchRendering.RadialBatchRendererAdapter.md)

#### 実装するインターフェース（Implements）

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

## コンストラクター（Constructors）

### <a id="Omni_BatchRendering_RadialBatchRendererAdapter__ctor_Omni_BatchRendering_RadialBatchRendererConfiguration__Omni_BatchRendering_IRadialBatchContentProvider_"></a> RadialBatchRendererAdapter\(in RadialBatchRendererConfiguration, IRadialBatchContentProvider\)

adapterを作成します。生成時にはGPU資源を確保しません。

```csharp
public RadialBatchRendererAdapter(in RadialBatchRendererConfiguration configuration, IRadialBatchContentProvider contentProvider)
```

#### 引数（Parameters）

`configuration` [RadialBatchRendererConfiguration](Omni.BatchRendering.RadialBatchRendererConfiguration.md)

Mesh、Material、bounds、固定Resident数を含む設定です。

`contentProvider` [IRadialBatchContentProvider](Omni.BatchRendering.IRadialBatchContentProvider.md)

Jobで可視IDだけを生成するprovider。nullでは初期化時にMacroOnlyへ縮退します。

## プロパティ（Properties）

### <a id="Omni_BatchRendering_RadialBatchRendererAdapter_BackendState"></a> BackendState

現在の共通BRG backend状態です。

```csharp
public RadialBatchBackendState BackendState { get; }
```

#### 値（Property Value）

 [RadialBatchBackendState](Omni.BatchRendering.RadialBatchBackendState.md)

### <a id="Omni_BatchRendering_RadialBatchRendererAdapter_Counters"></a> Counters

fail-openおよびview分離の診断カウンターを返します。

```csharp
public RadialBatchRuntimeCounters Counters { get; }
```

#### 値（Property Value）

 [RadialBatchRuntimeCounters](Omni.BatchRendering.RadialBatchRuntimeCounters.md)

### <a id="Omni_BatchRendering_RadialBatchRendererAdapter_ExpectedFrameRevision"></a> ExpectedFrameRevision

現在のCamera Snapshotと照合するframe revisionです。

```csharp
public ulong ExpectedFrameRevision { get; }
```

#### 値（Property Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_BatchRendering_RadialBatchRendererAdapter_IsReady"></a> IsReady

BRGが初期化済みでCamera callbackを受けられるかを返します。

```csharp
public bool IsReady { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_BatchRendering_RadialBatchRendererAdapter_Dispose"></a> Dispose\(\)

全BRG資源を解放します。OnDisable、Scene unload、domain reloadで呼び、
GraphicsBufferやBatchIDを次のSceneへ持ち越しません。

```csharp
public void Dispose()
```

### <a id="Omni_BatchRendering_RadialBatchRendererAdapter_Initialize"></a> Initialize\(\)

BRG、RawBuffer契約、Mesh、Materialを初期化します。

```csharp
public bool Initialize()
```

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

Camera viewの登録を受けられる状態まで到達した場合true。falseならMacroOnlyまたはFaultedです。

### <a id="Omni_BatchRendering_RadialBatchRendererAdapter_RemoveView_Omni_BatchRendering_RadialBatchViewKey__"></a> RemoveView\(in RadialBatchViewKey\)

Camera破棄またはScene unload時にview固有のBatchIDとGPU bufferを解放します。

```csharp
public void RemoveView(in RadialBatchViewKey viewKey)
```

#### 引数（Parameters）

`viewKey` [RadialBatchViewKey](Omni.BatchRendering.RadialBatchViewKey.md)

解放するCameraのEntityId由来キー。未登録なら何もしません。

### <a id="Omni_BatchRendering_RadialBatchRendererAdapter_SetExpectedFrameRevision_System_UInt64_"></a> SetExpectedFrameRevision\(ulong\)

次のCamera Snapshotに対応するrevisionを設定します。
<param name="frameRevision">RadialViewRegistryと同じ単調増加revision。各Cameraのheaderはcallback前に同値へ更新します。</param>

```csharp
public void SetExpectedFrameRevision(ulong frameRevision)
```

#### 引数（Parameters）

`frameRevision` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_BatchRendering_RadialBatchRendererAdapter_TryCreateOrReplaceView__1_Omni_BatchRendering_RadialBatchViewKey__System_UInt64_Omni_BatchRendering_RadialBrgViewHeader__Unity_Collections_NativeArray___0__"></a> TryCreateOrReplaceView<T\>\(in RadialBatchViewKey, ulong, in RadialBrgViewHeader, NativeArray<T\>\)

Camera viewの初回GPU bufferを作成し、sentinelを含む固定32 byte粒子recordをアップロードします。

```csharp
public bool TryCreateOrReplaceView<T>(in RadialBatchViewKey viewKey, ulong frameRevision, in RadialBrgViewHeader header, NativeArray<T> particleRecords) where T : unmanaged
```

#### 引数（Parameters）

`viewKey` [RadialBatchViewKey](Omni.BatchRendering.RadialBatchViewKey.md)

対象CameraのEntityId由来キー。Game ViewとScene Viewで共有してはいけません。

`frameRevision` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

headerが対応するCamera Snapshot revisionです。

`header` [RadialBrgViewHeader](Omni.BatchRendering.RadialBrgViewHeader.md)

Camera固有の投影・warpデータ。非有限値では更新せずMacroOnlyへ縮退します。

`particleRecords` NativeArray<T\>

index 0が退化sentinel、1..NがResident粒子の32 byte blittable recordです。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

view資源の作成または更新に成功した場合trueです。

#### 型引数（Type Parameters）

`T` 

サイズ32 byteのunmanaged粒子record。SaturnParticleGpuRecordを渡します。

### <a id="Omni_BatchRendering_RadialBatchRendererAdapter_TryGetViewDrawDiagnostics_Omni_BatchRendering_RadialBatchViewKey__Omni_BatchRendering_RadialBatchViewDrawDiagnostics__"></a> TryGetViewDrawDiagnostics\(in RadialBatchViewKey, out RadialBatchViewDrawDiagnostics\)

Camera viewごとの最後に確定したDirect draw command診断値を取得します。
callback回数とは独立した、<xref href="UnityEngine.Rendering.BatchCullingOutputDrawCommands.drawCommandCount" data-throw-if-not-resolved="false"></xref> の実出力です。

```csharp
public bool TryGetViewDrawDiagnostics(in RadialBatchViewKey viewKey, out RadialBatchViewDrawDiagnostics diagnostics)
```

#### 引数（Parameters）

`viewKey` [RadialBatchViewKey](Omni.BatchRendering.RadialBatchViewKey.md)

照合するCamera viewのEntityId由来キーです。

`diagnostics` [RadialBatchViewDrawDiagnostics](Omni.BatchRendering.RadialBatchViewDrawDiagnostics.md)

成功時の不変診断値です。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

登録済みviewの診断値を取得できた場合trueです。

### <a id="Omni_BatchRendering_RadialBatchRendererAdapter_TryUpdateViewHeader_Omni_BatchRendering_RadialBatchViewKey__System_UInt64_Omni_BatchRendering_RadialBrgViewHeader__"></a> TryUpdateViewHeader\(in RadialBatchViewKey, ulong, in RadialBrgViewHeader\)

既存viewのCamera固有headerだけを更新します。

```csharp
public bool TryUpdateViewHeader(in RadialBatchViewKey viewKey, ulong frameRevision, in RadialBrgViewHeader header)
```

#### 引数（Parameters）

`viewKey` [RadialBatchViewKey](Omni.BatchRendering.RadialBatchViewKey.md)

更新するCameraのキーです。

`frameRevision` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

このheaderが対応するCamera Snapshot revisionです。

`header` [RadialBrgViewHeader](Omni.BatchRendering.RadialBrgViewHeader.md)

viewごとの投影・warpデータ。粒子recordの再アップロードは行いません。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

登録済みviewを更新できた場合trueです。未登録・非有限値ではfalseです。
