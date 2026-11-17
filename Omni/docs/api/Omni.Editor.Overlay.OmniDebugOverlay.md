# <a id="Omni_Editor_Overlay_OmniDebugOverlay"></a> Class OmniDebugOverlay

Namespace: [Omni.Editor.Overlay](Omni.Editor.Overlay.md)  
Assembly: Omni.Editor.dll  

有限描画プロキシの状態をScene View単位で確認・上書きする、セッション限定の診断パネルです。

```csharp
[InitializeOnLoad]
public sealed class OmniDebugOverlay : Overlay
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Overlay ← 
[OmniDebugOverlay](Omni.Editor.Overlay.OmniDebugOverlay.md)

## メソッド（Methods）

### <a id="Omni_Editor_Overlay_OmniDebugOverlay_CreatePanelContent"></a> CreatePanelContent\(\)

<p>Implement this method to return your visual element content.</p>

```csharp
public override VisualElement CreatePanelContent()
```

#### 戻り値（Returns）

 VisualElement

<p>Visual element containing the content of your overlay.</p>
