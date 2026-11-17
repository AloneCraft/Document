# <a id="Omni_OmniHudTooltipLogic"></a> Class OmniHudTooltipLogic

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

<xref href="Omni.OmniHudTooltip" data-throw-if-not-resolved="false"></xref> の、UI Toolkit の実体に依らない部分（探索・置き位置・表示の状態）。EditMode で試せる。

```csharp
public static class OmniHudTooltipLogic
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniHudTooltipLogic](Omni.OmniHudTooltipLogic.md)

## フィールド（Fields）

### <a id="Omni_OmniHudTooltipLogic_DefaultDelaySeconds"></a> DefaultDelaySeconds

表示を始めるまでの既定の遅れ（秒）。

```csharp
public const float DefaultDelaySeconds = 0.35
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

## メソッド（Methods）

### <a id="Omni_OmniHudTooltipLogic_FindOwner_UnityEngine_UIElements_VisualElement_UnityEngine_UIElements_VisualElement_"></a> FindOwner\(VisualElement, VisualElement\)

start から root へ親をたどって、最初に <xref href="UnityEngine.UIElements.VisualElement.tooltip" data-throw-if-not-resolved="false"></xref> が空でない要素を返す（無ければ null）。
ボタンの中のラベルの上にポインタがあっても、ボタンの説明が見つかる。

```csharp
public static VisualElement FindOwner(VisualElement start, VisualElement root)
```

#### 引数（Parameters）

`start` VisualElement

`root` VisualElement

#### 戻り値（Returns）

 VisualElement

### <a id="Omni_OmniHudTooltipLogic_Place_UnityEngine_Rect_UnityEngine_Vector2_UnityEngine_Vector2_System_Single_System_Single_"></a> Place\(Rect, Vector2, Vector2, float, float\)

説明の板の左上の位置。対象の下に出し、下に収まらなければ上、上にも収まらなければ画面の下端に寄せる。
横は対象の左端にそろえ、画面の外へ出るなら内側へ寄せる。bounds は画面（パネル）の大きさ。

```csharp
public static Vector2 Place(Rect target, Vector2 size, Vector2 bounds, float gap = 6, float margin = 4)
```

#### 引数（Parameters）

`target` Rect

`size` Vector2

`bounds` Vector2

`gap` [float](https://learn.microsoft.com/dotnet/api/system.single)

`margin` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 Vector2
