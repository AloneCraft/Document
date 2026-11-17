# <a id="Omni_OmniVirtualShadowTiles"></a> Class OmniVirtualShadowTiles

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

仮想シャドウマップの、このフレームに描くページを「タイル」(同じ段の、ページの格子で TilePages × TilePages の区画)にまとめる。

<p>
ページごとに影を落とす物を描くと、描画の回数がページ数に比例する(起動直後は数千ページ)。タイルごとに 1 回だけ作業用の深度へ描き、
要るページだけを置き場へ写すと、描画の回数はタイル数になる。同じ段のページはテクセルの大きさが同じなので、1 つの正射影で描ける。
</p>

```csharp
public static class OmniVirtualShadowTiles
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniVirtualShadowTiles](Omni.OmniVirtualShadowTiles.md)

## フィールド（Fields）

### <a id="Omni_OmniVirtualShadowTiles_DefaultTilePages"></a> DefaultTilePages

タイルの 1 辺のページ数(16 × 128 テクセル = 2048 テクセル)。

```csharp
public const int DefaultTilePages = 16
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_OmniVirtualShadowTiles_FloorDivide_System_Int64_System_Int32_"></a> FloorDivide\(long, int\)

切り捨ての割り算(負の番号でも格子が揃う)。

```csharp
public static long FloorDivide(long value, int divisor)
```

#### 引数（Parameters）

`value` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`divisor` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_OmniVirtualShadowTiles_Group_System_Collections_Generic_IReadOnlyList_Omni_OmniVirtualShadowPageCache_RenderRequest__System_Int32_System_Collections_Generic_List_Omni_OmniVirtualShadowPageCache_RenderRequest__System_Collections_Generic_List_Omni_OmniVirtualShadowTiles_Tile__"></a> Group\(IReadOnlyList<RenderRequest\>, int, List<RenderRequest\>, List<Tile\>\)

plan をタイルごとに並べ替えて sorted へ入れ、タイルの一覧を tiles へ入れる。どのページも、ちょうど 1 つのタイルに入る。

```csharp
public static void Group(IReadOnlyList<OmniVirtualShadowPageCache.RenderRequest> plan, int tilePages, List<OmniVirtualShadowPageCache.RenderRequest> sorted, List<OmniVirtualShadowTiles.Tile> tiles)
```

#### 引数（Parameters）

`plan` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[OmniVirtualShadowPageCache](Omni.OmniVirtualShadowPageCache.md).[RenderRequest](Omni.OmniVirtualShadowPageCache.RenderRequest.md)\>

`tilePages` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`sorted` [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[OmniVirtualShadowPageCache](Omni.OmniVirtualShadowPageCache.md).[RenderRequest](Omni.OmniVirtualShadowPageCache.RenderRequest.md)\>

`tiles` [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[OmniVirtualShadowTiles](Omni.OmniVirtualShadowTiles.md).[Tile](Omni.OmniVirtualShadowTiles.Tile.md)\>
