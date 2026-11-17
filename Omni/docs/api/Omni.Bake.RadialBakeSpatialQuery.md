# <a id="Omni_Bake_RadialBakeSpatialQuery"></a> Class RadialBakeSpatialQuery

Namespace: [Omni.Bake](Omni.Bake.md)  
Assembly: Radial.Runtime.dll  

検証済みBake BVHから、静的候補と動的live setを分けて取得します。
古いschema、fingerprint不一致、Binding欠落、構造破損はすべてFailOpenへ倒します。

```csharp
public static class RadialBakeSpatialQuery
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialBakeSpatialQuery](Omni.Bake.RadialBakeSpatialQuery.md)

## メソッド（Methods）

### <a id="Omni_Bake_RadialBakeSpatialQuery_CollectDynamicLiveEntryIndices_Omni_Bake_RadialBakeBinding_System_Collections_Generic_List_System_Int32__"></a> CollectDynamicLiveEntryIndices\(RadialBakeBinding, List<int\>\)

動的Entryのlive setを収集します。動的EntryはBake BVHに含めず、各フレームの
実位置に基づく別経路で扱うため、FarFieldGroupを参照しません。

```csharp
public static RadialBakeSpatialQueryResult CollectDynamicLiveEntryIndices(RadialBakeBinding binding, List<int> dynamicEntryIndices)
```

#### 引数（Parameters）

`binding` [RadialBakeBinding](Omni.Bake.RadialBakeBinding.md)

`dynamicEntryIndices` [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[int](https://learn.microsoft.com/dotnet/api/system.int32)\>

#### 戻り値（Returns）

 [RadialBakeSpatialQueryResult](Omni.Bake.RadialBakeSpatialQueryResult.md)

### <a id="Omni_Bake_RadialBakeSpatialQuery_CollectStaticCandidateEntryIndices__1_Omni_Bake_RadialBakeBinding___0__System_Collections_Generic_List_System_Int32__"></a> CollectStaticCandidateEntryIndices<T\>\(RadialBakeBinding, ref T, List<int\>\)

静的Entryの候補IDを収集します。<xref href="Omni.Bake.RadialBakeSpatialRelation.Outside" data-throw-if-not-resolved="false"></xref> の
ノードだけを除外し、IndeterminateとFallbackは必ず残します。

```csharp
public static RadialBakeSpatialQueryResult CollectStaticCandidateEntryIndices<T>(RadialBakeBinding binding, ref T evaluator, List<int> candidateEntryIndices) where T : struct, IRadialBakeSpatialRelationEvaluator
```

#### 引数（Parameters）

`binding` [RadialBakeBinding](Omni.Bake.RadialBakeBinding.md)

`evaluator` T

`candidateEntryIndices` [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[int](https://learn.microsoft.com/dotnet/api/system.int32)\>

#### 戻り値（Returns）

 [RadialBakeSpatialQueryResult](Omni.Bake.RadialBakeSpatialQueryResult.md)

#### 型引数（Type Parameters）

`T` 

### <a id="Omni_Bake_RadialBakeSpatialQuery_CollectStaticCandidateEntryIndices__1_Omni_Bake_RadialBakeSpatialQueryContext____0__System_Collections_Generic_List_System_Int32__"></a> CollectStaticCandidateEntryIndices<T\>\(in RadialBakeSpatialQueryContext, ref T, List<int\>\)

完全検証済みcontextから静的候補IDを非割当で収集します。contextが陳腐化した場合は
旧BVHを使わず、検証時Dataの全静的IDを返して可視側へ倒します。

```csharp
public static RadialBakeSpatialQueryResult CollectStaticCandidateEntryIndices<T>(in RadialBakeSpatialQueryContext context, ref T evaluator, List<int> candidateEntryIndices) where T : struct, IRadialBakeSpatialRelationEvaluator
```

#### 引数（Parameters）

`context` [RadialBakeSpatialQueryContext](Omni.Bake.RadialBakeSpatialQueryContext.md)

`evaluator` T

`candidateEntryIndices` [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[int](https://learn.microsoft.com/dotnet/api/system.int32)\>

#### 戻り値（Returns）

 [RadialBakeSpatialQueryResult](Omni.Bake.RadialBakeSpatialQueryResult.md)

#### 型引数（Type Parameters）

`T` 

### <a id="Omni_Bake_RadialBakeSpatialQuery_HasValidSpatialIndex_Omni_Bake_RadialBakeBinding_"></a> HasValidSpatialIndex\(RadialBakeBinding\)

Bindingとschema v2の空間索引が安全に使えるかを返します。

```csharp
public static bool HasValidSpatialIndex(RadialBakeBinding binding)
```

#### 引数（Parameters）

`binding` [RadialBakeBinding](Omni.Bake.RadialBakeBinding.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Bake_RadialBakeSpatialQuery_TryCreateValidatedContext_Omni_Bake_RadialBakeBinding_Omni_Bake_RadialBakeSpatialQueryContext__"></a> TryCreateValidatedContext\(RadialBakeBinding, out RadialBakeSpatialQueryContext\)

Binding、fingerprint、Renderer参照、BVH構造を完全検証し、Camera間で再利用する
非保存contextを作ります。target refresh等のcold pathからだけ呼びます。

```csharp
public static bool TryCreateValidatedContext(RadialBakeBinding binding, out RadialBakeSpatialQueryContext context)
```

#### 引数（Parameters）

`binding` [RadialBakeBinding](Omni.Bake.RadialBakeBinding.md)

`context` [RadialBakeSpatialQueryContext](Omni.Bake.RadialBakeSpatialQueryContext.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
