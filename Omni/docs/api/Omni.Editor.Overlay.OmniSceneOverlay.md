# <a id="Omni_Editor_Overlay_OmniSceneOverlay"></a> Class OmniSceneOverlay

Namespace: [Omni.Editor.Overlay](Omni.Editor.Overlay.md)  
Assembly: Omni.Editor.dll  

各Scene ViewへOmniの簡易操作を追加するUI Toolkit Overlayです。

<p>
Scene Viewの投影方式（Perspective / Orthographic）に応じて中身を丸ごと切り替えます。
Perspectiveは既存のRadial（3D放射対数）操作一式、Orthographicは
Editor専用の2D対数グリッド表示（<code>Omni.Editor.SceneViewOrtho.OrthoLogGridRenderer</code>）の
トグルだけです。両者は独立した機能で、パラメータを共有しません。
</p>
<p>
ScaleSpaceプロジェクトの同名オーバーレイを移植したものです。
Standard/Radial比較描画は System A（GPU頂点ワープ）のみ移植済みで、実体は
<xref href="Omni.Logical.LinearReferenceMeshRenderer" data-throw-if-not-resolved="false"></xref> にあります。ここはその表示モードを
切り替えるUIだけを持ちます。
</p>
<p>
座標編集とナビゲーションはLogical座標を正本とし、Unityの単精度値は描画・GUI境界でのみ使います。
</p>

```csharp
[Overlay(typeof(SceneView), "Omni.SceneOverlay", "Omni", true)]
public sealed class OmniSceneOverlay : Overlay
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Overlay ← 
[OmniSceneOverlay](Omni.Editor.Overlay.OmniSceneOverlay.md)

## メソッド（Methods）

### <a id="Omni_Editor_Overlay_OmniSceneOverlay_CreatePanelContent"></a> CreatePanelContent\(\)

<p>Implement this method to return your visual element content.</p>

```csharp
public override VisualElement CreatePanelContent()
```

#### 戻り値（Returns）

 VisualElement

<p>Visual element containing the content of your overlay.</p>

### <a id="Omni_Editor_Overlay_OmniSceneOverlay_OnCreated"></a> OnCreated\(\)

ツールバーの "SS" を押した時点で中身を出します（collapsed のピル化を防ぎます）。

```csharp
public override void OnCreated()
```

### <a id="Omni_Editor_Overlay_OmniSceneOverlay_OnWillBeDestroyed"></a> OnWillBeDestroyed\(\)

<p>Called when an Overlay is about to be destroyed.</p>

```csharp
public override void OnWillBeDestroyed()
```
