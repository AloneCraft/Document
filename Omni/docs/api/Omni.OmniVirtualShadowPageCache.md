# <a id="Omni_OmniVirtualShadowPageCache"></a> Class OmniVirtualShadowPageCache

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

仮想シャドウマップの物理ページの割り当て。ページの番号は Unity の座標に固定した格子(段・X・Y)で、物理ページ(スロット)へ対応させる。

<p>
1 フレーム: 画面が要るページの印(GPU のビット列。要求したときの窓の相対位置)を受け取り、まだ無いページを数え、
1 フレームの上限まで割り当てて描くページの一覧を作る。粗い段から先に割り当てる(どの画素にも早く何かの影が出るように)。
置き場が足りなければ、しばらく要求されていないページから外す(LRU)。今のフレームで要求されたページは外さない。
</p>

光の向きが変わったときは、描いたページを「古い」として残しながら描き直す(<xref href="Omni.OmniVirtualShadowPageCache.MarkAllStale" data-throw-if-not-resolved="false"></xref>)。
Unity の座標の原点が動いたときは、番号の意味が変わるので全部捨てる(<xref href="Omni.OmniVirtualShadowPageCache.Clear" data-throw-if-not-resolved="false"></xref>)。

```csharp
public sealed class OmniVirtualShadowPageCache
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniVirtualShadowPageCache](Omni.OmniVirtualShadowPageCache.md)

## コンストラクター（Constructors）

### <a id="Omni_OmniVirtualShadowPageCache__ctor_Omni_OmniVirtualShadowSettings__"></a> OmniVirtualShadowPageCache\(in OmniVirtualShadowSettings\)

```csharp
public OmniVirtualShadowPageCache(in OmniVirtualShadowSettings settings)
```

#### 引数（Parameters）

`settings` [OmniVirtualShadowSettings](Omni.OmniVirtualShadowSettings.md)

## プロパティ（Properties）

### <a id="Omni_OmniVirtualShadowPageCache_LastPlanBurst"></a> LastPlanBurst

前の計画が、上限を外して足りないページを全部描く計画だったか。

```csharp
public bool LastPlanBurst { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_OmniVirtualShadowPageCache_PendingCount"></a> PendingCount

要求されたのに、まだ描いていないページの数(前のフレームの計画の後)。

```csharp
public int PendingCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_OmniVirtualShadowPageCache_RenderList"></a> RenderList

```csharp
public IReadOnlyList<OmniVirtualShadowPageCache.RenderRequest> RenderList { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[OmniVirtualShadowPageCache](Omni.OmniVirtualShadowPageCache.md).[RenderRequest](Omni.OmniVirtualShadowPageCache.RenderRequest.md)\>

### <a id="Omni_OmniVirtualShadowPageCache_RequestedCount"></a> RequestedCount

```csharp
public int RequestedCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_OmniVirtualShadowPageCache_UsedSlots"></a> UsedSlots

```csharp
public int UsedSlots { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_OmniVirtualShadowPageCache_BuildTable_System_UInt32___System_Int64___System_Int64___"></a> BuildTable\(uint\[\], long\[\], long\[\]\)

ページ表(段 × PagesPerAxis² の uint)を作る。値は 0 = 無し、それ以外 = スロット + 1。窓は今のフレームの各段の窓。
描き終えたページだけを載せる(古いページも載せる)。

```csharp
public void BuildTable(uint[] table, long[] windowX, long[] windowY)
```

#### 引数（Parameters）

`table` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]

`windowX` [long](https://learn.microsoft.com/dotnet/api/system.int64)\[\]

`windowY` [long](https://learn.microsoft.com/dotnet/api/system.int64)\[\]

### <a id="Omni_OmniVirtualShadowPageCache_Clear"></a> Clear\(\)

全部捨てる(Unity の座標の原点が動いたとき)。

```csharp
public void Clear()
```

### <a id="Omni_OmniVirtualShadowPageCache_IsRendered_System_Int32_"></a> IsRendered\(int\)

```csharp
public bool IsRendered(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_OmniVirtualShadowPageCache_IsStale_System_Int32_"></a> IsStale\(int\)

```csharp
public bool IsStale(int slot)
```

#### 引数（Parameters）

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_OmniVirtualShadowPageCache_MarkAllStale"></a> MarkAllStale\(\)

描いたページを全部「古い」にする(光の向きが変わったとき)。中身は描き直すまで使う。

```csharp
public void MarkAllStale()
```

### <a id="Omni_OmniVirtualShadowPageCache_MarkRendered"></a> MarkRendered\(\)

描き終えたページを記録する(<xref href="Omni.OmniVirtualShadowPageCache.Plan(System.Int32%2cSystem.Boolean)" data-throw-if-not-resolved="false"></xref> の一覧を全部描いた後)。

```csharp
public void MarkRendered()
```

### <a id="Omni_OmniVirtualShadowPageCache_MarkRendered_System_Collections_Generic_IReadOnlyList_Omni_OmniVirtualShadowPageCache_RenderRequest__"></a> MarkRendered\(IReadOnlyList<RenderRequest\>\)

実際に描いたページだけを記録する。計画に入れたが描かなかったページ(今の窓の外など)は「まだ描いていない」のまま残す
(描いた扱いにすると、置き場に残っていた前のページの中身が影として使われる)。

```csharp
public void MarkRendered(IReadOnlyList<OmniVirtualShadowPageCache.RenderRequest> drawn)
```

#### 引数（Parameters）

`drawn` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[OmniVirtualShadowPageCache](Omni.OmniVirtualShadowPageCache.md).[RenderRequest](Omni.OmniVirtualShadowPageCache.RenderRequest.md)\>

### <a id="Omni_OmniVirtualShadowPageCache_MarkStale_System_Double_System_Double_System_Double_System_Double_"></a> MarkStale\(double, double, double, double\)

光の座標(右・上、m。ページの格子と同じ原点)の範囲に重なる、描いたページを「古い」にする(動いた物・形が変わった物の範囲)。
中身は描き直すまで使う。古いページは次の計画で、足りないページの次に描き直される。戻り値は古くしたページの数。

```csharp
public int MarkStale(double minX, double maxX, double minY, double maxY)
```

#### 引数（Parameters）

`minX` [double](https://learn.microsoft.com/dotnet/api/system.double)

`maxX` [double](https://learn.microsoft.com/dotnet/api/system.double)

`minY` [double](https://learn.microsoft.com/dotnet/api/system.double)

`maxY` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_OmniVirtualShadowPageCache_Plan_System_Int32_System_Boolean_"></a> Plan\(int, bool\)

このフレームに描くページを決める。要求されたページのうち、まだ無いもの(粗い段から)、次に古いもの(光の向きが変わった)、の順に上限まで。
さらに refreshBudget 枚まで、要求されている描画済みのページを、描いてから長いものから描き直す
(動く物の影は、描いたページを使い回すと古い位置に残る。全部のページが順に描き直され、数秒以内に追いつく)。

<p>
burstWhenMostlyMissing: 要求されたページのうち描画済み(古いものも含む)が半分未満のとき(起動直後、カメラが飛んだ直後、全部捨てた直後)は、
1 フレームの上限を外して足りないページを全部描く(影が何十フレームもかけて徐々に出るのを避ける)。
光の向きが変わって描画済みが「古い」になっただけのときは、描画済みが残っているので上限は外れない。
</p>

```csharp
public IReadOnlyList<OmniVirtualShadowPageCache.RenderRequest> Plan(int refreshBudget = 0, bool burstWhenMostlyMissing = false)
```

#### 引数（Parameters）

`refreshBudget` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`burstWhenMostlyMissing` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[OmniVirtualShadowPageCache](Omni.OmniVirtualShadowPageCache.md).[RenderRequest](Omni.OmniVirtualShadowPageCache.RenderRequest.md)\>

### <a id="Omni_OmniVirtualShadowPageCache_RequestedByLevel"></a> RequestedByLevel\(\)

要求されたページを段ごとに数えた文字列(診断用。"段:数" を並べる)。

```csharp
public string RequestedByLevel()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_OmniVirtualShadowPageCache_SetRequests_System_UInt32___System_Int64___System_Int64___"></a> SetRequests\(uint\[\], long\[\], long\[\]\)

画面が要るページの印を受け取る。bits は段 × ページ数のビット列(段 k の窓の (x, y) は k×PagesPerLevel + y×PagesPerAxis + x 番目)。
windowX/windowY は、要求したフレームの各段の窓の左下のページの番号。

```csharp
public void SetRequests(uint[] bits, long[] windowX, long[] windowY)
```

#### 引数（Parameters）

`bits` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]

`windowX` [long](https://learn.microsoft.com/dotnet/api/system.int64)\[\]

`windowY` [long](https://learn.microsoft.com/dotnet/api/system.int64)\[\]

### <a id="Omni_OmniVirtualShadowPageCache_TryGetSlot_Omni_OmniVirtualShadowPageCache_PageKey_System_Int32__"></a> TryGetSlot\(PageKey, out int\)

スロットのページの番号(検証用)。

```csharp
public bool TryGetSlot(OmniVirtualShadowPageCache.PageKey key, out int slot)
```

#### 引数（Parameters）

`key` [OmniVirtualShadowPageCache](Omni.OmniVirtualShadowPageCache.md).[PageKey](Omni.OmniVirtualShadowPageCache.PageKey.md)

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
