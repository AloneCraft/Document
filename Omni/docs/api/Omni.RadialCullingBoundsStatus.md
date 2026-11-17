# <a id="Omni_RadialCullingBoundsStatus"></a> Enum RadialCullingBoundsStatus

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

Radial 頂点ワープ後の Renderer 候補を Unity 標準カリングへ渡すための結果状態です。

```csharp
public enum RadialCullingBoundsStatus
```

## フィールド（Fields）

`FailOpen = 2` 

厳密な構築に失敗したため、カメラ近傍の有限 Bounds へ可視側に倒した状態です。



`OutsideShell = 1` 

呼び出し側の shell 判定で完全に範囲外と確定した状態です。



`Ready = 0` 

写像後の保守 Bounds を正常に構築できました。
