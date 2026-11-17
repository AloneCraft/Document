# <a id="Omni_ViewportVetoKind"></a> Enum ViewportVetoKind

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

Scene Viewの高精度（仮想）ビューポートを使えない理由の種類です。
UIはこの種類から利用者へ対処（対数レンダリングへの切替など）を案内します。

```csharp
public enum ViewportVetoKind
```

## フィールド（Fields）

`NoRadialTargets = 2` 

読み込み中のSceneに対数(Radial)で描ける物体が1つもありません。



`None = 0` 

拒否はありません。



`Pending = 1` 

対象の収集・判定が未完了、または破棄済みの対象を収集した一時状態です。



`StandardMaterial = 3` 

LogicalTransform外のRenderer／Terrainが標準マテリアルのままです。
