# <a id="Omni_VirtualObject_VgCellRepresentation"></a> Class VgCellRepresentation

Namespace: [Omni.VirtualObject](Omni.VirtualObject.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

VG の地形（R1）を 1 つの段の表現として包む。描くのは VG 自身（Cell を選んで描く）なので、Show / Hide は描くものを作らず、
「この段が望まれている」という印だけを持つ。つなぐのは準備の状態:
IsReady = 必要な Cell（<code>required</code> が返す <xref href="VirtualGeometry.World.PlanetCellKey" data-throw-if-not-resolved="false"></xref>）がすべて <xref href="VirtualGeometry.World.IPlanetCellResidency" data-throw-if-not-resolved="false"></xref> に常駐していること。
Prepare は、常駐していない Cell の生成を要求する（優先度は <code>priority</code>）。描いている間は <xref href="Omni.VirtualObject.VgCellRepresentation.OnFrame" data-throw-if-not-resolved="false"></xref> で Cell を退避させない（Touch）。
必要な Cell が 1 つも無いとき（空の列）は、待つものが無いので常に準備できている。

```csharp
public sealed class VgCellRepresentation : IVirtualRepresentation, IVirtualRepresentationFrame
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VgCellRepresentation](Omni.VirtualObject.VgCellRepresentation.md)

#### 実装するインターフェース（Implements）

[IVirtualRepresentation](Omni.VirtualObject.IVirtualRepresentation.md), 
[IVirtualRepresentationFrame](Omni.VirtualObject.IVirtualRepresentationFrame.md)

## コンストラクター（Constructors）

### <a id="Omni_VirtualObject_VgCellRepresentation__ctor_VirtualGeometry_World_IPlanetCellResidency_System_Func_System_Collections_Generic_IReadOnlyList_VirtualGeometry_World_PlanetCellKey___System_Single_System_Int32_"></a> VgCellRepresentation\(IPlanetCellResidency, Func<IReadOnlyList<PlanetCellKey\>\>, float, int\)

```csharp
public VgCellRepresentation(IPlanetCellResidency residency, Func<IReadOnlyList<PlanetCellKey>> required, float priority = 1, int trianglesPerCell = 8192)
```

#### 引数（Parameters）

`residency` [IPlanetCellResidency](VirtualGeometry.World.IPlanetCellResidency.md)

`required` [Func](https://learn.microsoft.com/dotnet/api/system.func\-1)<[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)\>\>

`priority` [float](https://learn.microsoft.com/dotnet/api/system.single)

`trianglesPerCell` [int](https://learn.microsoft.com/dotnet/api/system.int32)

## フィールド（Fields）

### <a id="Omni_VirtualObject_VgCellRepresentation_DefaultTrianglesPerCell"></a> DefaultTrianglesPerCell

1 つの Cell の三角形の数の既定（64 × 64 の quad、各 2 三角形）。

```csharp
public const int DefaultTrianglesPerCell = 8192
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="Omni_VirtualObject_VgCellRepresentation_ByteCount"></a> ByteCount

VG の pool が持つので、この表現は資源を持たない。

```csharp
public long ByteCount { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_VirtualObject_VgCellRepresentation_IsReady"></a> IsReady

描ける状態か（資源が揃っている）。false の間は、この表現へは上がらない（今の表現を描き続ける）。
描いている間（IsShown が true の間）は true のままにする。

```csharp
public bool IsReady { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_VirtualObject_VgCellRepresentation_IsShown"></a> IsShown

いま描かれているか（Show 済みで Hide されていない）。

```csharp
public bool IsShown { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_VirtualObject_VgCellRepresentation_MissingCellCount"></a> MissingCellCount

必要な Cell が 1 つでも欠けているとき、その数（診断用）。

```csharp
public int MissingCellCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_VirtualObject_VgCellRepresentation_TriangleCount"></a> TriangleCount

必要な Cell の数 × 1 Cell の三角形（見積もり。VG が実際に描く数ではない）。

```csharp
public int TriangleCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_VirtualObject_VgCellRepresentation_Hide"></a> Hide\(\)

描くのをやめる（冪等）。資源の解放は表現が決める（遅延破棄など）。

```csharp
public void Hide()
```

### <a id="Omni_VirtualObject_VgCellRepresentation_OnFrame"></a> OnFrame\(\)

描いている間、必要な Cell を退避させず、欠けた Cell は要求し直す。

```csharp
public void OnFrame()
```

### <a id="Omni_VirtualObject_VgCellRepresentation_Prepare"></a> Prepare\(\)

準備を進める。この表現が望まれているのに IsReady が false の間、毎回の Tick で呼ばれる（冪等）。
一度に作る量は表現が自分で絞る（1 フレームに 1 区画など。長い停止を作らない）。

```csharp
public void Prepare()
```

### <a id="Omni_VirtualObject_VgCellRepresentation_Show"></a> Show\(\)

描き始める。IsReady のときだけ呼ばれる（冪等）。

```csharp
public void Show()
```
