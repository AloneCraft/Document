# <a id="Omni_Bake_IRadialBakeSpatialRelationEvaluator"></a> Interface IRadialBakeSpatialRelationEvaluator

Namespace: [Omni.Bake](Omni.Bake.md)  
Assembly: Radial.Runtime.dll  

Logical AABBと現在の保守的な可視領域との関係を評価します。

```csharp
public interface IRadialBakeSpatialRelationEvaluator
```

## メソッド（Methods）

### <a id="Omni_Bake_IRadialBakeSpatialRelationEvaluator_Evaluate_Omni_Logical_Aabb__"></a> Evaluate\(in Aabb\)

指定AABBの関係を返します。

```csharp
RadialBakeSpatialRelation Evaluate(in Aabb bounds)
```

#### 引数（Parameters）

`bounds` [Aabb](Omni.Logical.Aabb.md)

#### 戻り値（Returns）

 [RadialBakeSpatialRelation](Omni.Bake.RadialBakeSpatialRelation.md)
