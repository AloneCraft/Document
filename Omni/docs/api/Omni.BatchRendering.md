# <a id="Omni_BatchRendering"></a> Namespace Omni.BatchRendering

### クラス（Classes）

 [AllResidentRadialBatchContentProvider](Omni.BatchRendering.AllResidentRadialBatchContentProvider.md)

診断専用のAllResidentVisible providerです。

<p>
Saturnの性能比較ではFrustumOnly/Omniを主比較とし、本providerはBRG配線、GPU capture、
false-negative調査だけに使います。benchmark JSONではこのproviderを使った結果を
validForComparison=falseとして記録します。
</p>

 [OmniForwardLightingNotice](Omni.BatchRendering.OmniForwardLightingNotice.md)

URP の Forward の Renderer で描いているとき、Scene BRG（一括描画）を止めて通常の描画へ戻している理由を、利用者へ知らせる文言です。
デモの HUD と Omni Manager が使います。

 [RadialBatchInstanceWriter](Omni.BatchRendering.RadialBatchInstanceWriter.md)

BRG instance dataへ書き込める値の受け口です。

 [RadialBatchRendererAdapter](Omni.BatchRendering.RadialBatchRendererAdapter.md)

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

 [RadialBatchRendererRegistry](Omni.BatchRendering.RadialBatchRendererRegistry.md)

ランタイム生成MeshRendererをScene BRGへ登録する公開窓口です。
Sceneに保存されたMeshRendererはbackendが自動登録するため、このAPIは生成物専用です。

 [RadialBrgGpuLayout](Omni.BatchRendering.RadialBrgGpuLayout.md)

Saturn Meso粒子の32 byte recordとBRG RawBufferの固定レイアウトです。

<p>
record自体の生成責務はSaturn Coreにあり、この型はDOTS metadataとbyte offsetだけを唯一の
真実源として管理します。Shaderは同じoffsetをRadialBrgParticle.hlslから読むため、
C#とHLSLのlayoutずれを検出できます。
</p>

 [RadialBrgMaterialManifest](Omni.BatchRendering.RadialBrgMaterialManifest.md)

BRG material sidecarと依存Hashの生成Manifestです。

 [RadialBrgMaterialManifestEntry](Omni.BatchRendering.RadialBrgMaterialManifestEntry.md)

元Materialと生成BRG sidecarの対応です。

 [RadialBrgRuntimeMaterialCache](Omni.BatchRendering.RadialBrgRuntimeMaterialCache.md)

動的textureを持つ材質を検証済みBRG shaderへ複製し、backendの寿命中所有します。

 [RadialBrgSceneManifest](Omni.BatchRendering.RadialBrgSceneManifest.md)

Player Build時のSceneコピーへEditorが付加する、Scene単位のBRG Material対応表です。
GardenSceneでは元Sceneを変更せず、同Sceneで参照するsidecarだけをPlayerへ含めます。

 [RadialSceneBatchRendererExclusion](Omni.BatchRendering.RadialSceneBatchRendererExclusion.md)

外部のMaterialPropertyBlockを維持するScene Renderer（Animatorがmaterialのプロパティを書くもの等）を
Scene BRGの自動所有から除外し、通常のOmni Radial MeshRenderer経路へ残します。

 [RadialSceneBatchRendererService](Omni.BatchRendering.RadialSceneBatchRendererService.md)

Scene Mesh BRGのLifecycleを1か所で管理します。
Rebuild通知はdirty flagへ集約し、Renderer収集は安全なUpdate境界で1回だけ実行します。

### 構造体（Structs）

 [RadialBatchCullingInput](Omni.BatchRendering.RadialBatchCullingInput.md)

BRG callbackから粒子可視IDをJobとして求めるための安全な入力です。

<p>
この値はUnity Object、Material、GraphicsBuffer、unsafe pointerを含みません。
Saturn Coreはこの入力と不変Simulation Snapshotだけを読み、adapterが確保した出力領域へ
1始まりのinstance IDを書き込みます。ID 0はBRG direct drawの最小2件制約を満たす
退化sentinel専用です。
</p>

 [RadialBatchInstanceHandle](Omni.BatchRendering.RadialBatchInstanceHandle.md)

ランタイム生成したMeshRendererをScene BRGへ登録した結果です。
Garden/OasisなどのScene Meshを、再利用されたslotの古い参照から保護するためgenerationを持ちます。

 [RadialBatchRendererConfiguration](Omni.BatchRendering.RadialBatchRendererConfiguration.md)

1つのMeso粒子contentをBRGで描画するための不変設定です。
Saturnシーンの <code>SaturnMesoBatchRenderer</code> がBuilderからMesh、専用Material、保守的な
global boundsを渡して構築します。Meso粒子はv1で動的影を落とさないため、adapterは
常にShadowCastingMode.Offのdraw rangeを生成します。

 [RadialBatchRuntimeCounters](Omni.BatchRendering.RadialBatchRuntimeCounters.md)

BRGのfail-open判断をbenchmark・検証へ渡すための不変カウンターです。
Saturnシーンの複数Camera検証では、A→B→Aの各callback数とstale view数を照合します。

 [RadialBatchViewDrawDiagnostics](Omni.BatchRendering.RadialBatchViewDrawDiagnostics.md)

Camera viewごとの最後に確定したDirect draw command数を表す不変診断値です。
A→B→A検証ではview keyとframe revisionを一緒に比較し、他Cameraの結果が混ざらないことを確認します。

 [RadialBatchViewKey](Omni.BatchRendering.RadialBatchViewKey.md)

BRG callbackのviewを識別する不変キーです。

<p>
Unity 6000のCamera cullingで実測したBRG viewIDは対象Camera componentの
<xref href="UnityEngine.EntityId" data-throw-if-not-resolved="false"></xref>と一致するため、その64bit表現を保持します。
SaturnシーンのGame View、Scene View、比較用CameraはこのキーごとにGPU bufferとBatchIDを分離します。
</p>

 [RadialBrgViewHeader](Omni.BatchRendering.RadialBrgViewHeader.md)

CameraごとのBRG RawBuffer先頭に置く208 byteのヘッダーです。

<p>
各viewは同じResident粒子recordを持っても、このヘッダーだけはCamera固有です。
そのためGame View→Scene View→Game ViewでShader.SetGlobal*の競合を起こさず、
Saturnシーンの比較Cameraが互いの投影行列を上書きしません。
</p>

 [RadialPackedMatrix](Omni.BatchRendering.RadialPackedMatrix.md)

Unity標準GPUDrivenと同じ48 byteのDOTS packed matrixです。

 [RadialSceneBatchGpuLayout](Omni.BatchRendering.RadialSceneBatchGpuLayout.md)

Scene BRGが共有するRaw GraphicsBufferのSoA配置です。
Instance 0は0行列sentinel、実Renderer submeshは1始まりで格納します。

 [RadialSceneBatchKey](Omni.BatchRendering.RadialSceneBatchKey.md)

同じBRG Draw CommandへまとめられるMeshRenderer submeshの不変キーです。
Rendererの位置はinstance dataなのでキーに含めません。

### インターフェース（Interfaces）

 [IRadialBatchContentProvider](Omni.BatchRendering.IRadialBatchContentProvider.md)

Radial BRGへ安全なJob入力だけを公開するMeso粒子content providerです。

<p>
draw command、TempJob native pointer、GraphicsBuffer、BatchIDの確保・破棄は一切行わず、
<xref href="Omni.BatchRendering.RadialBatchRendererAdapter" data-throw-if-not-resolved="false"></xref> が所有します。可視IDは必ず1..ResidentInstanceCountで、
0はadapterの退化sentinelとして予約されます。
</p>

 [IRadialBatchInstanceDataProvider](Omni.BatchRendering.IRadialBatchInstanceDataProvider.md)

非標準のper-instance値をBRGへ渡すProviderです。
Textureはinstance overrideできないため、floatとVectorだけを登録時またはMarkDirty時に書きます。

 [IRadialBatchMaterialDependencyProvider](Omni.BatchRendering.IRadialBatchMaterialDependencyProvider.md)

Play時に生成するbatch MaterialのAuthoring依存をEditor生成器へ申告します。

### 列挙型（Enums）

 [RadialBatchBackendState](Omni.BatchRendering.RadialBatchBackendState.md)

SaturnのMesoリングをBRGで描画するバックエンドの状態です。

<p>
<code>MacroOnly</code> はMacroリングだけを描く安全な縮退であり、BRG描画の成功を意味しません。
Saturnシーンの <code>SaturnMesoBatchRenderer</code> がこの値を通信UIとbenchmark JSONへ公開します。
</p>

 [RadialBatchDirtyFlags](Omni.BatchRendering.RadialBatchDirtyFlags.md)

BRG instanceのどの入力が変わったかを表します。

 [RadialSceneBatchBackendMode](Omni.BatchRendering.RadialSceneBatchBackendMode.md)

Scene Mesh描画に使う内部A/B backendです。

 [RadialSceneBatchRebuildReason](Omni.BatchRendering.RadialSceneBatchRebuildReason.md)

Scene BRG backend全再構築を要求した原因です。複数通知は同じUpdateまで合成します。
