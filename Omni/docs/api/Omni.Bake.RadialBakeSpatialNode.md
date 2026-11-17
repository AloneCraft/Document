# <a id="Omni_Bake_RadialBakeSpatialNode"></a> Struct RadialBakeSpatialNode

Namespace: [Omni.Bake](Omni.Bake.md)  
Assembly: Radial.Runtime.dll  

ベイク済み決定的BVHの1ノードです。

```csharp
[Serializable]
public struct RadialBakeSpatialNode
```

## フィールド（Fields）

### <a id="Omni_Bake_RadialBakeSpatialNode_Bounds"></a> Bounds

このノード配下すべてを含む保守的なLogical AABBです。

```csharp
public Aabb Bounds
```

#### 値（Field Value）

 [Aabb](Omni.Rendering.Radial.Aabb.md)

### <a id="Omni_Bake_RadialBakeSpatialNode_FirstStaticEntryOrderIndex"></a> FirstStaticEntryOrderIndex

<xref href="Omni.Rendering.Radial.BakeData.StaticEntryOrder" data-throw-if-not-resolved="false"></xref>内の先頭位置です。

```csharp
public int FirstStaticEntryOrderIndex
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Bake_RadialBakeSpatialNode_IsLeaf"></a> IsLeaf

子を持たない葉ならtrueです。

```csharp
public bool IsLeaf
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Bake_RadialBakeSpatialNode_LeftChildIndex"></a> LeftChildIndex

左の子ノードの配列インデックスです。葉では-1です。

```csharp
public int LeftChildIndex
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Bake_RadialBakeSpatialNode_RightChildIndex"></a> RightChildIndex

右の子ノードの配列インデックスです。葉では-1です。

```csharp
public int RightChildIndex
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Bake_RadialBakeSpatialNode_SplitAxis"></a> SplitAxis

中央値分割に使った軸です。

```csharp
public RadialBakeSpatialAxis SplitAxis
```

#### 値（Field Value）

 [RadialBakeSpatialAxis](Omni.Bake.RadialBakeSpatialAxis.md)

### <a id="Omni_Bake_RadialBakeSpatialNode_StaticEntryCount"></a> StaticEntryCount

このノード配下の静的Entry数です。

```csharp
public int StaticEntryCount
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_Bake_RadialBakeSpatialNode_TryGetBounds_Omni_Logical_Aabb__"></a> TryGetBounds\(out Aabb\)

保守的なLogical AABBを取得します。

```csharp
public bool TryGetBounds(out Aabb bounds)
```

#### 引数（Parameters）

`bounds` [Aabb](Omni.Logical.Aabb.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
