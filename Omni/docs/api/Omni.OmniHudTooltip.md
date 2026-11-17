# <a id="Omni_OmniHudTooltip"></a> Class OmniHudTooltip

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

実行時の UI Toolkit の HUD で、要素の <xref href="UnityEngine.UIElements.VisualElement.tooltip" data-throw-if-not-resolved="false"></xref> をマウスオーバーで出す。
実行時のパネルは tooltip を自動では出さない（Editor のパネルだけ）ので、HUD の root へ <xref href="Omni.OmniHudTooltip.Attach(UnityEngine.UIElements.VisualElement%2cSystem.Single%2cSystem.Int32%2cSystem.Func%7bSystem.Single%7d)" data-throw-if-not-resolved="false"></xref> を 1 回呼ぶ。
ボタンなどには <code>button.tooltip = "説明"</code> を設定するだけ。説明の板は root の最前面の浮いたラベル（ポインタを受けず、レイアウトに影響しない）。
文字は呼び出し側が渡した言語のまま（この部品は言語を持たない）。HUD を作り直す（root が替わる）ときは、新しい root へ Attach し直す。

```csharp
public sealed class OmniHudTooltip
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniHudTooltip](Omni.OmniHudTooltip.md)

## フィールド（Fields）

### <a id="Omni_OmniHudTooltip_LabelName"></a> LabelName

```csharp
public const string LabelName = "OmniHudTooltip"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## プロパティ（Properties）

### <a id="Omni_OmniHudTooltip_IsShown"></a> IsShown

説明の板が出ているか（確認用）。

```csharp
public bool IsShown { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_OmniHudTooltip_Label"></a> Label

説明の板の要素（確認用）。

```csharp
public Label Label { get; }
```

#### 値（Property Value）

 Label

### <a id="Omni_OmniHudTooltip_Text"></a> Text

いま出している（または出す予定の）説明の文字。

```csharp
public string Text { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_OmniHudTooltip_Attach_UnityEngine_UIElements_VisualElement_System_Single_System_Int32_System_Func_System_Single__"></a> Attach\(VisualElement, float, int, Func<float\>\)

root の下のどの要素の tooltip でも、マウスオーバーで出すようにする。

```csharp
public static OmniHudTooltip Attach(VisualElement root, float delaySeconds = 0.35, int fontSize = 14, Func<float> clock = null)
```

#### 引数（Parameters）

`root` VisualElement

`delaySeconds` [float](https://learn.microsoft.com/dotnet/api/system.single)

`fontSize` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`clock` [Func](https://learn.microsoft.com/dotnet/api/system.func\-1)<[float](https://learn.microsoft.com/dotnet/api/system.single)\>

秒を返す関数（null なら <xref href="UnityEngine.Time.realtimeSinceStartup" data-throw-if-not-resolved="false"></xref>）。

#### 戻り値（Returns）

 [OmniHudTooltip](Omni.OmniHudTooltip.md)

### <a id="Omni_OmniHudTooltip_Detach"></a> Detach\(\)

登録を外し、説明の板を消す。

```csharp
public void Detach()
```

### <a id="Omni_OmniHudTooltip_Hover_UnityEngine_UIElements_VisualElement_"></a> Hover\(VisualElement\)

説明を持つ要素を、呼び出し側が直接指す（マウスを自分で読んでいる HUD 用。ポインタのイベントを受けない要素や pickingMode=Ignore の要素にも使える）。
owner が null なら消す。毎フレーム呼んでよい。

```csharp
public void Hover(VisualElement owner)
```

#### 引数（Parameters）

`owner` VisualElement
