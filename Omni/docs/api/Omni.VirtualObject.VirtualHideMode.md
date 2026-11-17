# <a id="Omni_VirtualObject_VirtualHideMode"></a> Enum VirtualHideMode

Namespace: [Omni.VirtualObject](Omni.VirtualObject.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

<xref href="Omni.VirtualObject.GameObjectRepresentation" data-throw-if-not-resolved="false"></xref> が、描くのをやめたときに instance をどうするか。

```csharp
public enum VirtualHideMode
```

## フィールド（Fields）

`Deactivate = 0` 

SetActive(false) にして持ち続ける（再び上がるときは準備が要らない。メモリは残る）。



`Destroy = 1` 

破棄する（メモリは返る。再び上がるときは準備し直す）。
