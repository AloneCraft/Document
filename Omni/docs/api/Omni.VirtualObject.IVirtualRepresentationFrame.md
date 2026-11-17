# <a id="Omni_VirtualObject_IVirtualRepresentationFrame"></a> Interface IVirtualRepresentationFrame

Namespace: [Omni.VirtualObject](Omni.VirtualObject.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

毎フレームの世話が要る表現が実装する任意の契約（例: VG のセルを退避させないための Touch）。
<xref href="Omni.VirtualObject.VirtualObjectController" data-throw-if-not-resolved="false"></xref> は呼ばない。呼ぶのは持ち主（<xref href="Omni.VirtualObject.VirtualObjectBehaviour" data-throw-if-not-resolved="false"></xref> など）で、Tick の後に全表現へ呼ぶ。
描かれていない間に何をするかは表現が決める（普通は何もしない）。

```csharp
public interface IVirtualRepresentationFrame
```

## メソッド（Methods）

### <a id="Omni_VirtualObject_IVirtualRepresentationFrame_OnFrame"></a> OnFrame\(\)

```csharp
void OnFrame()
```
