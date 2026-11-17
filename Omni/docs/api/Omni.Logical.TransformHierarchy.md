# <a id="Omni_Logical_TransformHierarchy"></a> Class TransformHierarchy

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

```csharp
[MovedFrom(true, "Omni", null, "LogicalTransformHierarchy")]
public static class TransformHierarchy
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[TransformHierarchy](Omni.Logical.TransformHierarchy.md)

## メソッド（Methods）

### <a id="Omni_Logical_TransformHierarchy_DescribeViolation_Omni_Logical_Transform_Omni_Logical_Transform_"></a> DescribeViolation\(Transform, Transform\)

違反内容を人間向けの文章で返します。ログ・Inspector・ダイアログで共用します。

```csharp
public static string DescribeViolation(Transform logicalTransform, Transform offendingAncestor)
```

#### 引数（Parameters）

`logicalTransform` [Transform](Omni.Logical.Transform.md)

違反している対象。

`offendingAncestor` [Transform](Omni.Logical.Transform.md)

直接の親ではない祖先。

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

説明文。

### <a id="Omni_Logical_TransformHierarchy_IsRoot_Omni_Logical_Transform_"></a> IsRoot\(Transform\)

この <xref href="Omni.Logical.Transform" data-throw-if-not-resolved="false"></xref> が論理合成の起点（論理ルート）かを判定します。

<p>
上の規則により、祖先に <xref href="Omni.Logical.Transform" data-throw-if-not-resolved="false"></xref> があるならそれは必ず直接の親です。
よって「直接の親が LogicalTransform でない」ことがそのまま論理ルートの定義になり、
祖先を遡らずに O(1) で判定できます。
</p>

<p>
禁止配置（間に素の Transform が挟まる）の場合も true を返します。そのとき
<code>LogicalTransform.GetLogicalParent()</code> は合成を打ち切って null を返すため、
当人が自分で絶対姿勢を書くしかなく、起点として扱うのが正しいためです。
この一致は意図的です。
</p>
<p>
<b>現在このメソッドの呼び出し元はありません。</b>階層規則はLogical座標合成の基礎概念であり、
将来の階層検証・ツールから使用できるため、公開 API として残しています。
</p>

```csharp
public static bool IsRoot(Transform logicalTransform)
```

#### 引数（Parameters）

`logicalTransform` [Transform](Omni.Logical.Transform.md)

判定対象。null の場合は false（対象なし）。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

論理ルートであれば true。

### <a id="Omni_Logical_TransformHierarchy_IsValid_Omni_Logical_Transform_Omni_Logical_Transform__"></a> IsValid\(Transform, out Transform\)

この <xref href="Omni.Logical.Transform" data-throw-if-not-resolved="false"></xref> の階層が規則を満たすかを判定します。

```csharp
public static bool IsValid(Transform logicalTransform, out Transform offendingAncestor)
```

#### 引数（Parameters）

`logicalTransform` [Transform](Omni.Logical.Transform.md)

判定対象。null の場合は true（対象なし）。

`offendingAncestor` [Transform](Omni.Logical.Transform.md)

違反時、直接の親ではない位置にある祖先の <xref href="Omni.Logical.Transform" data-throw-if-not-resolved="false"></xref>。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

規則を満たす場合は true。
