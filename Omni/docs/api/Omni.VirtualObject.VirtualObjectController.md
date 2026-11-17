# <a id="Omni_VirtualObject_VirtualObjectController"></a> Class VirtualObjectController

Namespace: [Omni.VirtualObject](Omni.VirtualObject.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

Virtual Object 1 つの状態（今の段）と、表現の切り替え。段の選択は <xref href="Omni.VirtualObject.VirtualObjectSelector" data-throw-if-not-resolved="false"></xref>（画素基準・ヒステリシス）に任せ、
ここでは「上がるときは準備ができた表現だけ」「新しい表現を先に出し、古い表現を後で外す」を守る。
表現の配列 levels[i] が段 i。null は「その段では何も描かない」（準備不要・常に描ける）。
失敗は Fail Closed: Show が例外を投げたら今の表現を描き続け、<xref href="Omni.VirtualObject.VirtualObjectController.LastFailure" data-throw-if-not-resolved="false"></xref> に残す。

```csharp
public sealed class VirtualObjectController
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualObjectController](Omni.VirtualObject.VirtualObjectController.md)

## コンストラクター（Constructors）

### <a id="Omni_VirtualObject_VirtualObjectController__ctor_Omni_VirtualObject_VirtualObjectSelector_Omni_VirtualObject_IVirtualRepresentation___"></a> VirtualObjectController\(VirtualObjectSelector, IVirtualRepresentation\[\]\)

```csharp
public VirtualObjectController(VirtualObjectSelector selector, IVirtualRepresentation[] levels)
```

#### 引数（Parameters）

`selector` [VirtualObjectSelector](Omni.VirtualObject.VirtualObjectSelector.md)

`levels` [IVirtualRepresentation](Omni.VirtualObject.IVirtualRepresentation.md)\[\]

## プロパティ（Properties）

### <a id="Omni_VirtualObject_VirtualObjectController_DesiredLevel"></a> DesiredLevel

最後の Tick で望まれた段（準備待ちで Level より高いことがある）。

```csharp
public int DesiredLevel { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_VirtualObject_VirtualObjectController_LastFailure"></a> LastFailure

最後の Show の失敗（なければ null）。

```csharp
public Exception LastFailure { get; }
```

#### 値（Property Value）

 [Exception](https://learn.microsoft.com/dotnet/api/system.exception)

### <a id="Omni_VirtualObject_VirtualObjectController_Level"></a> Level

いま描いている段（Tick の前は 0）。

```csharp
public int Level { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_VirtualObject_VirtualObjectController_ResidentBytes"></a> ResidentBytes

全ての表現が持つ資源の合計（バイト）。

```csharp
public long ResidentBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_VirtualObject_VirtualObjectController_ShownTriangleCount"></a> ShownTriangleCount

いま描いている表現の三角形の数（まだ何も描いていないとき、null の段は 0）。

```csharp
public int ShownTriangleCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_VirtualObject_VirtualObjectController_Transitions"></a> Transitions

段が替わった回数（最初に描き始めた Tick は数えない）。

```csharp
public int Transitions { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_VirtualObject_VirtualObjectController_ReleaseAll"></a> ReleaseAll\(\)

描いている表現を外す（対象が不要になったとき）。

```csharp
public void ReleaseAll()
```

### <a id="Omni_VirtualObject_VirtualObjectController_Tick_System_Double_"></a> Tick\(double\)

対象の画面上の大きさ（画素）から段を決め、表現を切り替える。毎フレーム 1 回呼ぶ。
最初の Tick は理想の段（ヒステリシスなし）から始め、準備ができた中でいちばん高い段を描く（どれも描けなければ何も描かない = 段 0 が null なら空）。
上がるとき: 望まれた段までの準備できていない表現の Prepare を呼び、準備できた中でいちばん高い段へ上がる。
下がるとき: 望まれた段より上で、準備できた中でいちばん低い段へ下がる（準備できていなければ今の段のまま）。

```csharp
public void Tick(double pixels)
```

#### 引数（Parameters）

`pixels` [double](https://learn.microsoft.com/dotnet/api/system.double)
