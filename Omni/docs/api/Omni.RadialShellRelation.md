# <a id="Omni_RadialShellRelation"></a> Enum RadialShellRelation

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

2つの論理シェル境界の比較結果です。<xref href="Omni.RadialShellRelation.Indeterminate" data-throw-if-not-resolved="false"></xref>は演算失敗・
overflow・非有限入力を表し、描画判定では必ず可視側へ倒します。

```csharp
public enum RadialShellRelation
```

## フィールド（Fields）

`Equal = 1` 

左辺と右辺が同じ状態です。



`Greater = 2` 

左辺が右辺より大きい状態です。



`Indeterminate = 3` 

比較不能な状態です。描画では可視側へ倒します。



`Less = 0` 

左辺が右辺より小さい状態です。
