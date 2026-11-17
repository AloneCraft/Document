# <a id="Omni_Bake_RadialBakeSpatialRelation"></a> Enum RadialBakeSpatialRelation

Namespace: [Omni.Bake](Omni.Bake.md)  
Assembly: Radial.Runtime.dll  

空間ノードと視界との保守的な関係です。<xref href="Omni.Bake.RadialBakeSpatialRelation.Outside" data-throw-if-not-resolved="false"></xref> だけが
対象の除外を許可し、それ以外は可視候補として扱います。

```csharp
public enum RadialBakeSpatialRelation : byte
```

## フィールド（Fields）

`Indeterminate = 2` 

比較不能または境界上です。必ず可視候補として扱います。



`Intersecting = 1` 

ノードが対象領域と交差するため、下位を精査します。



`Outside = 0` 

ノード全体が確実に対象外です。
