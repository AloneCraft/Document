# <a id="Omni_RadialCullingSystem"></a> Class RadialCullingSystem

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

ベイク済みのLogical AABB（<xref href="Omni.Rendering.Radial.BakeEntry" data-throw-if-not-resolved="false"></xref>）を使い、near/far方向の
放射距離をLogical正本で判定してカリングする「第2層」です。

<p>
<xref href="Omni.RadialGlobalRenderSystem" data-throw-if-not-resolved="false"></xref> のUnity cullingMatrix 補正（第1層）は保守的broad phaseに限定し、
こちらがベイク済みLogical AABBと現在のLogicalカメラ位置から真の放射距離レンジを求める権威値です。
錐台の側面4平面の判定はワープ不変（レイ上の移動は角度を変えない）なので Unity標準の
カリング（第1層で補正済みの cullingMatrix を使う）にそのまま任せ、
このシステムは near/far のみを <xref href="UnityEngine.Renderer.forceRenderingOff" data-throw-if-not-resolved="false"></xref> で追加カリングします。
</p>
<p>
対象は「静的（<xref href="Omni.Rendering.Radial.BakeEntry.IsStatic" data-throw-if-not-resolved="false"></xref>）」なベイク済みEntryのみです。
動的オブジェクトはベイク時のLogical AABBが現在の実位置と一致する保証が無いため対象外とし、
Unityの保守的broad phaseにのみ委ねます。
</p>
<p>
<xref href="UnityEngine.Renderer.forceRenderingOff" data-throw-if-not-resolved="false"></xref> はカメラ非依存のグローバルなフラグです。
本システムは <xref href="Omni.RadialGlobalRenderSystem" data-throw-if-not-resolved="false"></xref> と同じ前提（1フレーム内でカメラは順次描画され、
同時にアクティブなのは1台）の上で、カメラごとの beginCameraRendering 直前に毎回評価し直すことで
正しく機能します。この前提が崩れる状況（Play モード中に Game カメラと Scene View が同一フレーム内で
両方描画されるなど）では、<xref href="Omni.RadialWarpSource.ApplyShellCulling" data-throw-if-not-resolved="false"></xref> が false のカメラに
<xref href="Omni.RadialCullingSystem.ApplyShellCulling(UnityEngine.Camera%2cOmni.RadialCamera)" data-throw-if-not-resolved="false"></xref> を呼ばせず、代わりに <xref href="Omni.RadialCullingSystem.ClearAll" data-throw-if-not-resolved="false"></xref> を呼ばせます。
</p>
<p>
<xref href="Omni.RadialCullingSystem.ApplyShellCulling(UnityEngine.Camera%2cOmni.RadialCamera)" data-throw-if-not-resolved="false"></xref> と <xref href="Omni.RadialCullingSystem.ClearAll" data-throw-if-not-resolved="false"></xref> は非対称です。前者は
<code>forceRenderingOff = true</code> を含むため、権限の無いカメラが呼ぶと他カメラで見えるべき物が
消えます（fail-closed、危険）。後者は <code>false</code> しか書かないため、権限の無いカメラが呼んでも
実害はありません（fail-open、安全）。呼び出し側（RadialGlobalRenderSystem）はこの非対称性に
従い、権限の無いカメラには常に <xref href="Omni.RadialCullingSystem.ClearAll" data-throw-if-not-resolved="false"></xref> 側を呼ばせます
（前フレームの通常カメラの判定がそのまま残ることを防ぎます）。
</p>

```csharp
public static class RadialCullingSystem
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialCullingSystem](Omni.RadialCullingSystem.md)

## メソッド（Methods）

### <a id="Omni_RadialCullingSystem_ApplyShellCulling_UnityEngine_Camera_Omni_RadialCamera_"></a> ApplyShellCulling\(Camera, RadialCamera\)

指定カメラについて、ベイク済み静的Entryの near/far 厳密シェル判定を適用します。
<xref href="Omni.RadialGlobalRenderSystem" data-throw-if-not-resolved="false"></xref> が cullingMatrix 補正（第1層）と同じタイミングで呼びます。
呼んでよいのは <xref href="Omni.RadialWarpSource.ApplyShellCulling" data-throw-if-not-resolved="false"></xref> が true のカメラだけです。

```csharp
public static void ApplyShellCulling(Camera camera, RadialCamera driver)
```

#### 引数（Parameters）

`camera` Camera

`driver` [RadialCamera](Omni.RadialCamera.md)

### <a id="Omni_RadialCullingSystem_ClearAll"></a> ClearAll\(\)

このシステムが操作した全 Renderer の forceRenderingOff を解除します。
シェルカリング権限を持たないカメラの描画直前、シーン変更時、テストの後始末で呼びます。

```csharp
public static void ClearAll()
```
