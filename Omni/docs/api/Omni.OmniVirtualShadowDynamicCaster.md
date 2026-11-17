# <a id="Omni_OmniVirtualShadowDynamicCaster"></a> Class OmniVirtualShadowDynamicCaster

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

仮想シャドウマップ(OmniVirtualShadowsFeature)へ「この物は動く・形が変わる」と知らせる部品。

<p>
仮想シャドウマップは、描いたページを使い回す。動く物・形が変わる物の影は、その物の範囲に重なるページだけを描き直す必要がある。
この部品を付けた物(と子)の、影を落とす Renderer の範囲が動いたら、前の範囲と今の範囲に重なるページが「古い」になり、すぐ描き直される。
位置は変わらないが中身が変わる物(メッシュを作り直した等)は、<xref href="Omni.OmniVirtualShadowDynamicCaster.MarkChanged" data-throw-if-not-resolved="false"></xref> を呼ぶ。
</p>

付けていない動く物の影は、順番の描き直し(Feature の「描き直すページの数」)で数秒遅れて追いつく。

```csharp
[DisallowMultipleComponent]
[AddComponentMenu("Omni/Rendering/Virtual Shadows Dynamic Caster")]
public sealed class OmniVirtualShadowDynamicCaster : MonoBehaviour
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[OmniVirtualShadowDynamicCaster](Omni.OmniVirtualShadowDynamicCaster.md)

## メソッド（Methods）

### <a id="Omni_OmniVirtualShadowDynamicCaster_MarkChanged"></a> MarkChanged\(\)

位置は同じでも、影の形が変わったことを知らせる(メッシュの作り直しなど)。次のフレームで描き直される。

```csharp
public void MarkChanged()
```

### <a id="Omni_OmniVirtualShadowDynamicCaster_RefreshRenderers"></a> RefreshRenderers\(\)

子の Renderer が増減したときに呼ぶ(有効になったときに 1 回集める)。

```csharp
public void RefreshRenderers()
```
