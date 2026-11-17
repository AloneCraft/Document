# <a id="Omni_Bake_RadialBakeSpatialIndexBuilder"></a> Class RadialBakeSpatialIndexBuilder

Namespace: [Omni.Bake](Omni.Bake.md)  
Assembly: Radial.Runtime.dll  

静的で有効なLogical AABBだけから、入力順に依存しないBVHを構築します。
動的Entryと境界不明Entryは索引へ入れず、後者はFallbackとして可視側に残します。

```csharp
public static class RadialBakeSpatialIndexBuilder
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialBakeSpatialIndexBuilder](Omni.Bake.RadialBakeSpatialIndexBuilder.md)

## フィールド（Fields）

### <a id="Omni_Bake_RadialBakeSpatialIndexBuilder_LeafEntryCapacity"></a> LeafEntryCapacity

1葉に格納できる最大静的Entry数です。

```csharp
public const int LeafEntryCapacity = 32
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_Bake_RadialBakeSpatialIndexBuilder_Build_Omni_Rendering_Radial_BakeEntry___"></a> Build\(BakeEntry\[\]\)

指定Entry列からschema v2の決定的BVHを構築します。

```csharp
public static RadialBakeSpatialIndex Build(BakeEntry[] entries)
```

#### 引数（Parameters）

`entries` [BakeEntry](Omni.Rendering.Radial.BakeEntry.md)\[\]

#### 戻り値（Returns）

 [RadialBakeSpatialIndex](Omni.Bake.RadialBakeSpatialIndex.md)

### <a id="Omni_Bake_RadialBakeSpatialIndexBuilder_ComputeContentFingerprint_Omni_Rendering_Radial_BakeEntry___Omni_Bake_RadialBakeSpatialNode___System_Int32___System_Int32___"></a> ComputeContentFingerprint\(BakeEntry\[\], RadialBakeSpatialNode\[\], int\[\], int\[\]\)

直列化済みEntryとBVH配列から、内容検証用の決定的fingerprintを再計算します。

```csharp
public static string ComputeContentFingerprint(BakeEntry[] entries, RadialBakeSpatialNode[] nodes, int[] staticEntryOrder, int[] fallbackEntryIndices)
```

#### 引数（Parameters）

`entries` [BakeEntry](Omni.Rendering.Radial.BakeEntry.md)\[\]

`nodes` [RadialBakeSpatialNode](Omni.Bake.RadialBakeSpatialNode.md)\[\]

`staticEntryOrder` [int](https://learn.microsoft.com/dotnet/api/system.int32)\[\]

`fallbackEntryIndices` [int](https://learn.microsoft.com/dotnet/api/system.int32)\[\]

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
