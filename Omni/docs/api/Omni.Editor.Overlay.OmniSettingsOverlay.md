# <a id="Omni_Editor_Overlay_OmniSettingsOverlay"></a> Class OmniSettingsOverlay

Namespace: [Omni.Editor.Overlay](Omni.Editor.Overlay.md)  
Assembly: Omni.Editor.dll  

たまにしか触らない設定をまとめたScene View パネルです。

<p>
常時表示の「Omni Navigator」（座標・角度・Nav状態など操作系）、読み取り専用の
「Omni Debug」（診断系）とは役割を分け、こちらは対話的なコントロールだけを持ちます。
カリング診断はDebugへ戻し、通常設定だけをこちらへ残します。
描画経路（物体の元Renderer／有限描画プロキシの切替）は常にAuto固定で、設定欄はありません。
</p>

```csharp
public sealed class OmniSettingsOverlay : Overlay
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Overlay ← 
[OmniSettingsOverlay](Omni.Editor.Overlay.OmniSettingsOverlay.md)

## メソッド（Methods）

### <a id="Omni_Editor_Overlay_OmniSettingsOverlay_CreatePanelContent"></a> CreatePanelContent\(\)

<p>Implement this method to return your visual element content.</p>

```csharp
public override VisualElement CreatePanelContent()
```

#### 戻り値（Returns）

 VisualElement

<p>Visual element containing the content of your overlay.</p>
