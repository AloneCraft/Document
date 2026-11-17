# <a id="Omni_Logical_IRadialRigidAnchorProvider"></a> Interface IRadialRigidAnchorProvider

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

Radial写像後も局所形状を剛体として維持するRendererの明示契約です。

```csharp
public interface IRadialRigidAnchorProvider
```

## 補足（Remarks）

惑星地形のように面内でもRadial写像を連続評価すべき対象には実装しないでください。
建築物、機械、UIラベルなど、アンカーから見て狭い距離比・立体角に収まり、単一アンカーを基準に形を保つ対象だけが使用します。
