# <a id="Omni_Bake_RadialBakeSpatialQueryResult"></a> Enum RadialBakeSpatialQueryResult

Namespace: [Omni.Bake](Omni.Bake.md)  
Assembly: Radial.Runtime.dll  

空間索引queryの成否です。

```csharp
public enum RadialBakeSpatialQueryResult : byte
```

## フィールド（Fields）

`FailOpen = 1` 

索引またはBindingが不正なため、全候補を可視側へ倒しました。



`Indexed = 0` 

検証済みの空間索引を使用しました。
