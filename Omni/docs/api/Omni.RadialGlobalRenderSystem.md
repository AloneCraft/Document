# <a id="Omni_RadialGlobalRenderSystem"></a> Class RadialGlobalRenderSystem

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

RadialGlobal対数ワープのcamera共有packetと、Logical/特殊Renderer用の精密
MaterialPropertyBlockを配布する描画システムです。ordinary opaque MeshRendererは
unity_ObjectToWorldを使う共有経路へ移し、CameraごとのRenderer走査を行いません。

対象 Renderer は「RadialGlobal シェーダーのマテリアルを持つ Renderer」を
自動収集します（マーカーコンポーネント不要）。シーン読み込み・Hierarchy 変更・
初回に再スキャンし、通常フレームでは既存の収集結果を使い回します。

<xref href="UnityEngine.Terrain" data-throw-if-not-resolved="false"></xref> は <xref href="UnityEngine.Renderer" data-throw-if-not-resolved="false"></xref> ではなく <xref href="UnityEngine.Behaviour" data-throw-if-not-resolved="false"></xref> 派生の
ため上記の走査には原理的に掛かりません。そこで Terrain だけは別に収集し、
<xref href="UnityEngine.Terrain.SetSplatMaterialPropertyBlock(UnityEngine.MaterialPropertyBlock)" data-throw-if-not-resolved="false"></xref>（Terrain 版の MPB API）へ
まったく同じ値を書き込みます。判定は Renderer と共通の <xref href="Omni.RadialGlobalRenderSystem.IsRadialMaterial(UnityEngine.Material)" data-throw-if-not-resolved="false"></xref> です。

かつては <xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref> / RadialGlobalEditorDriver が
Shader.SetGlobal* でグローバル設定していましたが、当該 uniform が
UnityPerMaterial CBUFFER 内にあると SRP Batcher がマテリアル値を優先して
無視され、かつグローバルは複数カメラ（Game/Scene 同時）で「最後に書いた
カメラが勝つ」共有状態になります。MaterialPropertyBlock は Unity が
beginCameraRendering → DrawRenderers のカメラごとの記録時に読み取るため、
カメラごとに正しくスコープされます。

```csharp
public static class RadialGlobalRenderSystem
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialGlobalRenderSystem](Omni.RadialGlobalRenderSystem.md)

## フィールド（Fields）

### <a id="Omni_RadialGlobalRenderSystem_SceneViewContextProvider"></a> SceneViewContextProvider

Editorの仮想論理Scene View状態を描画カメラへ供給します。Runtimeはこの値を
読み取るだけで、Scene Viewの選択状態を変更しません。

```csharp
public static Func<Camera, SceneViewRenderContext> SceneViewContextProvider
```

#### 値（Field Value）

 [Func](https://learn.microsoft.com/dotnet/api/system.func\-2)<Camera, [SceneViewRenderContext](Omni.Logical.SceneViewRenderContext.md)\>

### <a id="Omni_RadialGlobalRenderSystem_SceneViewDriverProvider"></a> SceneViewDriverProvider

RadialCamera を自身に持たないカメラ（Scene View 等）へワープ元の
<xref href="Omni.RadialWarpSource" data-throw-if-not-resolved="false"></xref> を供給するオプションのフックです。
Driver が無い（<xref href="Omni.RadialWarpSource.HasDriver" data-throw-if-not-resolved="false"></xref> が false の）場合は
ワープ設定を行いません。Editor 側（RadialGlobalEditorDriver）から設定されます。

<p>
<xref href="Omni.RadialWarpSource.ApplyCullingMatrixOverride" data-throw-if-not-resolved="false"></xref> は、位置が一致する場合に
Owner相当のnear/far補正を許可します。位置が異なる場合は、この許可の有無にかかわらず
変形後の描画錐台を包む保守的なObserverカリングへフォールバックします。
基準カメラを切り替えて別カメラのRadialCameraを借りる場合も、見える物体を欠落させない
代わりに広めのカリングボリュームを使います。ただしScene Viewの基準カメラ比較は
実物URP描画の欠落を避けるため、Observerカリングを適用せず標準のカリングへ戻します。
</p>
<p>
<xref href="Omni.RadialWarpSource.ApplyShellCulling" data-throw-if-not-resolved="false"></xref> はさらに厳しい条件です。
<xref href="UnityEngine.Renderer.forceRenderingOff" data-throw-if-not-resolved="false"></xref> はカメラ非依存のグローバルなフラグなので、
Play モード中のように Game カメラと Scene View が同一フレーム内で両方描画される状況では、
Scene View 側がこれを true にしてはいけません（Game カメラのシェルカリング結果を
毎フレーム打ち消してしまいます）。Play 中の Scene View はシェルカリングを実カメラへ
譲り、Owner相当または保守的ObserverのcullingMatrixだけを行ってください。
</p>

```csharp
public static Func<Camera, RadialWarpSource> SceneViewDriverProvider
```

#### 値（Field Value）

 [Func](https://learn.microsoft.com/dotnet/api/system.func\-2)<Camera, [RadialWarpSource](Omni.RadialWarpSource.md)\>

## プロパティ（Properties）

### <a id="Omni_RadialGlobalRenderSystem_DedicatedWorldSpaceFallbackCount"></a> DedicatedWorldSpaceFallbackCount

専用頂点変換を持たずfloat経路へ倒すworld-space Renderer数です。

```csharp
public static int DedicatedWorldSpaceFallbackCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_RadialGlobalRenderSystem_Targets"></a> Targets

現在の変形対象 Renderer 一覧（自動収集結果）です。
未収集（dirty）なら参照時に収集します。

```csharp
public static IReadOnlyList<Renderer> Targets { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<Renderer\>

### <a id="Omni_RadialGlobalRenderSystem_TerrainTargets"></a> TerrainTargets

現在の変形対象 Terrain 一覧（自動収集結果）です。
未収集（dirty）なら参照時に収集します。

```csharp
public static IReadOnlyList<Terrain> TerrainTargets { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<Terrain\>

### <a id="Omni_RadialGlobalRenderSystem_WarpEnabled"></a> WarpEnabled

ワープ全体のキルスイッチです。false の間は<b>マテリアルを一切触らずに</b>
恒等パラメータを配布し、見た目を圧縮なしへ戻します。

<p>
ビューごとに切ることはできません。<code>Shader.SetGlobal*</code> と共有ランタイム
インスタンスは構造的にグローバルなので、per-view の恒等は原理的に嘘になります。
Game View も含めて全部止まる、という前提で使ってください。
</p>
<p>
素の static なので、ドメインリロードやビルドされたプレイヤーでは常に true に戻ります。
常設の製品GUIには公開しません。テストコード、またはFunctions検証Scene限定の
Editor比較セッションで一時的に使用し、終了・Scene切替・Reload時に復元します。
対象Shaderだけを元URP版へ戻す機能ではなく、全Camera共通の診断スイッチです。
</p>

```csharp
public static bool WarpEnabled { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_RadialGlobalRenderSystem_ApplyForCamera_UnityEngine_Camera_"></a> ApplyForCamera\(Camera\)

明示的なCamera.Render経路でもカメラごとのRadial値を適用します。

```csharp
public static void ApplyForCamera(Camera camera)
```

#### 引数（Parameters）

`camera` Camera

### <a id="Omni_RadialGlobalRenderSystem_ClearAll"></a> ClearAll\(\)

収集済み対象を破棄します（テスト用）。

```csharp
public static void ClearAll()
```

### <a id="Omni_RadialGlobalRenderSystem_ClearRadialTransformParameters_UnityEngine_MaterialPropertyBlock_"></a> ClearRadialTransformParameters\(MaterialPropertyBlock\)

MPBから一時RadialTransformの使用フラグを解除します。

```csharp
public static void ClearRadialTransformParameters(MaterialPropertyBlock block)
```

#### 引数（Parameters）

`block` MaterialPropertyBlock

#### 補足（Remarks）

剛体アンカーは<code>_RadialGlobal_RadialTransform*</code>のサブモードなので、ここで
一緒に解除します。片方だけ残すと、恒等化したカメラで剛体指定が居座ります。

### <a id="Omni_RadialGlobalRenderSystem_EnsureTargetsCollected"></a> EnsureTargetsCollected\(\)

対象一覧が未収集なら収集します。

<p>
収集はもともとカメラ描画（beginCameraRendering）のタイミングでしか走らないため、
「まだ一度も描画していない」状態で一覧を読むと空が返ります。Editor の UI は
描画とは無関係に一覧を参照する（例: シーンが System A 構成かどうかの判定）ので、
参照側から見て常に正しい内容になるよう、ここで必要なら収集します。
</p>

```csharp
public static void EnsureTargetsCollected()
```

### <a id="Omni_RadialGlobalRenderSystem_IsDedicatedWorldSpaceFallback_UnityEngine_Renderer_"></a> IsDedicatedWorldSpaceFallback\(Renderer\)

指定Rendererが事前分類済みworld-space fallback対象かを返します。

```csharp
public static bool IsDedicatedWorldSpaceFallback(Renderer renderer)
```

#### 引数（Parameters）

`renderer` Renderer

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_RadialGlobalRenderSystem_IsRigidAnchorWarp_UnityEngine_Renderer_"></a> IsRigidAnchorWarp\(Renderer\)

この Renderer が剛体アンカーワープ対象かを返します。

```csharp
public static bool IsRigidAnchorWarp(Renderer renderer)
```

#### 引数（Parameters）

`renderer` Renderer

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_RadialGlobalRenderSystem_IsWarpExcluded_UnityEngine_Renderer_"></a> IsWarpExcluded\(Renderer\)

この Renderer が <xref href="Omni.RadialGlobalRenderSystem.SetWarpExcluded(UnityEngine.Renderer%2cSystem.Boolean)" data-throw-if-not-resolved="false"></xref> によって対象収集から除外されているかを
返します。除外された Renderer は <xref href="Omni.RadialGlobalRenderSystem.s_Targets" data-throw-if-not-resolved="false"></xref> に載らず、ワープ値を
一切書き込まれません（診断・テスト用の読み取り専用アクセサです）。

```csharp
public static bool IsWarpExcluded(Renderer renderer)
```

#### 引数（Parameters）

`renderer` Renderer

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_RadialGlobalRenderSystem_MarkDirty"></a> MarkDirty\(\)

対象一覧を次回カメラ描画時に再スキャンさせます。

```csharp
public static void MarkDirty()
```

### <a id="Omni_RadialGlobalRenderSystem_NotifyRendererCompatibilityChanged_UnityEngine_Renderer_"></a> NotifyRendererCompatibilityChanged\(Renderer\)

RuntimeコードがRenderer.sharedMaterials/renderQueue、またはfast対象のscale階層を差し替えた後に呼び、
互換分類を次Cameraで再構築します。位置・回転はunity_ObjectToWorldから直接読むため通知不要です。
Inspector/Scene変更は既存Editor hookが検知しますが、任意のRuntime代入はこの通知が正本です。

```csharp
public static void NotifyRendererCompatibilityChanged(Renderer renderer)
```

#### 引数（Parameters）

`renderer` Renderer

### <a id="Omni_RadialGlobalRenderSystem_RestoreAllCameraOverrides"></a> RestoreAllCameraOverrides\(\)

<xref href="UnityEngine.Camera.cullingMatrix" data-throw-if-not-resolved="false"></xref> / <xref href="UnityEngine.Camera.projectionMatrix" data-throw-if-not-resolved="false"></xref> の上書きが
残っている全カメラを復元します。これらは非シリアライズのネイティブ実行時プロパティなので、
明示的に解除しない限り、上書きしたカメラが二度と描画されなくても残り続けます。

```csharp
public static void RestoreAllCameraOverrides()
```

### <a id="Omni_RadialGlobalRenderSystem_RestoreCameraOverrides_UnityEngine_Camera_"></a> RestoreCameraOverrides\(Camera\)

指定カメラの <xref href="UnityEngine.Camera.cullingMatrix" data-throw-if-not-resolved="false"></xref> / <xref href="UnityEngine.Camera.projectionMatrix" data-throw-if-not-resolved="false"></xref> の
上書きを復元します。
上書きされていなければ何もしません（no-op）。

```csharp
public static void RestoreCameraOverrides(Camera camera)
```

#### 引数（Parameters）

`camera` Camera

### <a id="Omni_RadialGlobalRenderSystem_SetRigidAnchorWarp_UnityEngine_Renderer_System_Boolean_"></a> SetRigidAnchorWarp\(Renderer, bool\)

この Renderer を「アンカー1点だけ写像し、局所形状は剛体＋等方スケールで運ぶ」
対象にします。

```csharp
public static void SetRigidAnchorWarp(Renderer renderer, bool rigid)
```

#### 引数（Parameters）

`renderer` Renderer

対象。null は無視します。

`rigid` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

剛体アンカーにするなら true。

#### 補足（Remarks）

<p>
<b>アンカーから見て狭い距離比・立体角に収まる対象（ラベル・UI・小さな構造物）用です。</b>
地形のように広がる対象には使いません。
<code>RadialWarp</code> は非線形写像なので、per-vertex に任せると頂点ごとに圧縮率が変わって
形が変わります。球のような実体ではその変形こそが見せたい絵ですが、文字は読めなくなります。
</p>
<p>
崩れ量を決めるのはメッシュの絶対サイズではなく、ワープ中心から見た<b>距離比と立体角</b>です。
半径方向の局所倍率は対数域で <code>S/(d*ln2)</code> なので d1〜d2 を跨ぐと比 <code>d2/d1</code> だけ
厚みの縮み方が変わり、接線方向は実寸倍率 <code>mapped(d)/d</code> が d 依存なので広い立体角の
平面は球殻へ曲がります。
</p>
<p>
これは順序の入れ替えではなく<b>近似</b>です（<code>warp(S*p) != S*warp(p)</code>）。アンカー点に
おける写像の線形化を局所形状全体へ適用しているだけなので、対象がアンカーから見て狭い
距離比・立体角に収まっているときだけ妥当です。
</p>
<p>
<xref href="Omni.RadialGlobalRenderSystem.SetWarpExcluded(UnityEngine.Renderer%2cSystem.Boolean)" data-throw-if-not-resolved="false"></xref> と<b>併用しないでください</b>。除外された Renderer は
<code>s_Targets</code> に載らず、剛体パラメータを書く経路
（<code>WriteCameraScopedRadialTransform</code>）自体が走りません。
</p>
<p>
ShaderGraph 経路は非対応です（<code>_RadialGlobal_UseRadialTransform</code> と同じ制約。
ShaderGraph は <code>OmniRadialObjectToWarpedWorld</code> を経由しません）。
手書き／パッチ済みシェーダーでは、CBUFFER 宣言が共有 include の
<code>RadialInject.hlsl</code> 側にあるため再パッチ不要で有効になります。
</p>
<p>
<b>一時的な指定です。</b>マテリアルの SubShader タグ
（<code>"OmniRadialRigidAnchor" = "True"</code>、Manager生成TMP sidecar等）が
唯一の真実であり、次回の <xref href="Omni.RadialGlobalRenderSystem.RefreshTargets" data-throw-if-not-resolved="false"></xref>（Hierarchy 変更・シーン読込等で
dirty になったとき）で正式契約どおりに上書きされます。恒常的に剛体アンカーへ
したい場合は、Rendererと同じGameObjectへ
<xref href="Omni.Logical.IRadialRigidAnchorProvider" data-throw-if-not-resolved="false"></xref>を実装するComponentを付けるか、
マテリアルへタグを持つ手書きシェーダーを割り当ててください。
このメソッドは診断・テスト用です。
</p>

### <a id="Omni_RadialGlobalRenderSystem_SetWarpExcluded_UnityEngine_Renderer_System_Boolean_"></a> SetWarpExcluded\(Renderer, bool\)

指定 Renderer を対象収集から除外するかどうかを設定します。

```csharp
public static void SetWarpExcluded(Renderer renderer, bool excluded)
```

#### 引数（Parameters）

`renderer` Renderer

`excluded` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 補足（Remarks）

<p>
<xref href="Omni.RadialGlobalRenderSystem.RefreshTargets" data-throw-if-not-resolved="false"></xref> は<b>シーン中の全 Renderer を走査してマテリアルだけで</b>
判定するため、Radial マテリアルを載せた一時オブジェクトは作った瞬間に対象へ入ります。
Scene View の比較表示が置く「ワープ前の位置のプロキシ」は、まさに元マテリアルを
そのまま使うのでこれに該当し、除外しないとワープ値を書き込まれて実物と重なります。
</p>
<p>
除外は<b>その場で</b>効かせます（再収集を待ちません）。待つと1フレームだけワープ値を
書かれ、プロキシが実物へ吸い寄せられて見えるためです。
</p>

### <a id="Omni_RadialGlobalRenderSystem_SupportsSceneViewViewport"></a> SupportsSceneViewViewport\(\)

現在収集されている「実際に描かれる」Radial対象が、Scene View用の高精度オブジェクト
相対座標を解釈できるかを返します。未対応シェーダーが1つでもあれば仮想原点へ移行せず、
従来のfloat描画を維持します。

```csharp
public static bool SupportsSceneViewViewport()
```

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 補足（Remarks）

<p>
<b>この経路で必ず隠される対象は拒否権を持ちません。</b>
<xref href="Omni.RadialGlobalRenderSystem.ApplyMaterialCompatibility(System.Boolean%2cUnityEngine.Camera%2cOmni.Logical.SceneViewRenderContext%40)" data-throw-if-not-resolved="false"></xref>は、LogicalTransform配下で
<code>SupportsLogicalRadialMaterial</code>がfalseのRendererを
<xref href="UnityEngine.Renderer.forceRenderingOff" data-throw-if-not-resolved="false"></xref>で必ず隠します。仮想ビューポートを使うのは
対数(Radial)・比較モードのScene View、つまりその隠蔽が働く非identity経路だけなので、
隠される対象が誤配置されることは原理的にありません。
</p>
<p>
以前はこの除外が無く、<b>一度も描かれない1個のRenderer</b>（実機では非Radialマテリアルの
<code>Cube</code>）が仮想ビューポート全体を拒否していました。その結果Scene Viewは
安全域(<code>LogicalPhysicalSafety.Limit</code>)の外を表現する手段を失い、
論理ピボットが安全域外へ出た瞬間に物理ピボットが原点へピン留めされて
「飛行するとワールド原点が画面中央へ吸い寄せられ、いくら速度を上げても進まない」という
症状になっていました（実機のEditor.logで確定済み）。
</p>
<p>
LogicalTransform配下<b>でない</b>未対応Rendererは素のfloat座標でそのまま描かれるため、
従来どおり拒否権を持ちます。仮想原点へ移ると位置が破綻するのはこちらです。
</p>

### <a id="Omni_RadialGlobalRenderSystem_TryGetRadialFarRequirement_Omni_RadialCamera_System_Single__"></a> TryGetRadialFarRequirement\(RadialCamera, out float\)

論理Far Clipを描画空間へ写した実クリップfar要求を返します。

```csharp
public static bool TryGetRadialFarRequirement(RadialCamera driver, out float neededFar)
```

#### 引数（Parameters）

`driver` [RadialCamera](Omni.RadialCamera.md)

`neededFar` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_RadialGlobalRenderSystem_TryGetRuntimeOriginalMaterial_UnityEngine_Renderer_System_Int32_UnityEngine_Material__"></a> TryGetRuntimeOriginalMaterial\(Renderer, int, out Material\)

Play中に共有runtime Materialへ差し替えたRendererについて、
指定slotのAuthoring正本Materialを返します。参照の書き換えは行いません。

```csharp
public static bool TryGetRuntimeOriginalMaterial(Renderer renderer, int materialIndex, out Material original)
```

#### 引数（Parameters）

`renderer` Renderer

`materialIndex` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`original` Material

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_RadialGlobalRenderSystem_TryGetViewportVeto_System_String__"></a> TryGetViewportVeto\(out string\)

仮想ビューポートを拒否している対象があれば、その名前とともにtrueを返します。
拒否理由をUIへ名指しで出すための診断APIです。

```csharp
public static bool TryGetViewportVeto(out string reason)
```

#### 引数（Parameters）

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

拒否理由。拒否が無い場合は<code>null</code>です。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_RadialGlobalRenderSystem_TryGetViewportVeto_Omni_ViewportVetoKind__UnityEngine_Object__"></a> TryGetViewportVeto\(out ViewportVetoKind, out Object\)

仮想ビューポートを拒否している理由を、UIが対処を案内できる種類と対象で返します。

```csharp
public static bool TryGetViewportVeto(out ViewportVetoKind kind, out Object culprit)
```

#### 引数（Parameters）

`kind` [ViewportVetoKind](Omni.ViewportVetoKind.md)

拒否の種類。拒否が無い場合は<xref href="Omni.ViewportVetoKind.None" data-throw-if-not-resolved="false"></xref>です。

`culprit` Object

原因のRenderer／Terrain。特定できない場合は<code>null</code>です。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_RadialGlobalRenderSystem_TryResolveRenderPose_UnityEngine_Renderer_UnityEngine_Camera_Omni_Logical_SceneViewRenderContext__Omni_Logical_RenderPose__"></a> TryResolveRenderPose\(Renderer, Camera, in SceneViewRenderContext, out RenderPose\)

GPU本体、TMP、Editor補助描画が共有する論理描画姿勢を解決します。

```csharp
public static bool TryResolveRenderPose(Renderer renderer, Camera camera, in SceneViewRenderContext context, out RenderPose pose)
```

#### 引数（Parameters）

`renderer` Renderer

`camera` Camera

`context` [SceneViewRenderContext](Omni.Logical.SceneViewRenderContext.md)

`pose` [RenderPose](Omni.Logical.RenderPose.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_RadialGlobalRenderSystem_WriteGpuFrameParameters_UnityEngine_MaterialPropertyBlock_Omni_Rendering_Radial_GpuFrame__"></a> WriteGpuFrameParameters\(MaterialPropertyBlock, in GpuFrame\)

Editor の自己中心 Radial GPU Picking と検証の撮影へ、描画と同じ camera-relative frame を
MaterialPropertyBlock へ書き込みます。検証アセンブリが内部メンバーを参照しないよう公開しています。

```csharp
public static void WriteGpuFrameParameters(MaterialPropertyBlock block, in GpuFrame frame)
```

#### 引数（Parameters）

`block` MaterialPropertyBlock

値を書き込む一時 MaterialPropertyBlock。null は無視します。

`frame` [GpuFrame](Omni.Rendering.Radial.GpuFrame.md)

直近の描画で確定した有限な Radial GPU frame。

### <a id="Omni_RadialGlobalRenderSystem_WriteIdentityWarpParameters_UnityEngine_MaterialPropertyBlock_"></a> WriteIdentityWarpParameters\(MaterialPropertyBlock\)

恒等ワープのパラメータを <xref href="UnityEngine.MaterialPropertyBlock" data-throw-if-not-resolved="false"></xref> へ書き出します。

```csharp
public static void WriteIdentityWarpParameters(MaterialPropertyBlock block)
```

#### 引数（Parameters）

`block` MaterialPropertyBlock

#### 補足（Remarks）

<p>
Radial マテリアルを載せたまま<b>ワープさせたくない</b> Renderer のための入口です。
Scene View の比較表示が、ワープ前の位置に実物と同じマテリアルでプロキシを置くために
使います（<code>LogicalLinearReferenceMeshRenderer.EnsureStandardProxy</code>）。
</p>
<p>
<xref href="Omni.RadialGlobalRenderSystem.IdentityModeValue" data-throw-if-not-resolved="false"></xref> のとき <code>RadialWarp.hlsl</code> は入力座標をそのまま
返すため、ワープ中心の指定には意味がありません。呼び出し側が中心を知らなくても
正しく恒等になるよう、引数は取りません。
</p>
<p>
この呼び出しは <xref href="Omni.RadialGlobalRenderSystem.SetWarpExcluded(UnityEngine.Renderer%2cSystem.Boolean)" data-throw-if-not-resolved="false"></xref> と対で使ってください。除外していないと、
次の収集で <code>s_Targets</code> に載って <code>beginCameraRendering</code> がワープ値で
上書きします。
</p>

### <a id="Omni_RadialGlobalRenderSystem_WriteRadialTransformParameters_UnityEngine_MaterialPropertyBlock_Omni_Rendering_Radial_DrawTransform__"></a> WriteRadialTransformParameters\(MaterialPropertyBlock, in DrawTransform\)

カスタムRenderer向けに、カメラ単位の一時RadialTransformをMPBへ書き込みます。

```csharp
public static void WriteRadialTransformParameters(MaterialPropertyBlock block, in DrawTransform radialTransform)
```

#### 引数（Parameters）

`block` MaterialPropertyBlock

`radialTransform` [DrawTransform](Omni.Rendering.Radial.DrawTransform.md)

### <a id="Omni_RadialGlobalRenderSystem_WriteRadialTransformParametersForPicking_UnityEngine_MaterialPropertyBlock_Omni_Rendering_Radial_DrawTransform__System_Boolean_"></a> WriteRadialTransformParametersForPicking\(MaterialPropertyBlock, in DrawTransform, bool\)

Editor の GPU Picking 用に RadialTransform と剛体アンカー指定を書き込みます。

```csharp
public static void WriteRadialTransformParametersForPicking(MaterialPropertyBlock block, in DrawTransform radialTransform, bool rigidAnchor)
```

#### 引数（Parameters）

`block` MaterialPropertyBlock

値を書き込む一時 MaterialPropertyBlock。

`radialTransform` [DrawTransform](Omni.Rendering.Radial.DrawTransform.md)

対象 Renderer の論理姿勢から作った変換。

`rigidAnchor` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

剛体アンカー用シェーダーなら true。
