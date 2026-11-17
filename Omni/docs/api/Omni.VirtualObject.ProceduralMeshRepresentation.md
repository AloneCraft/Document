# <a id="Omni_VirtualObject_ProceduralMeshRepresentation"></a> Class ProceduralMeshRepresentation

Namespace: [Omni.VirtualObject](Omni.VirtualObject.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

プロシージャルなメッシュを 1 つの段の表現にする。<xref href="Omni.VirtualObject.ProceduralMeshRepresentation.Prepare" data-throw-if-not-resolved="false"></xref> 1 回で足す三角形を絞り（<code>trianglesPerPrepare</code>）、全部できたらメッシュと
非アクティブな GameObject を作る（IsReady）。全体の三角形とバイトの上限（<code>maxTriangles</code>、<code>maxBytes</code>）を超えたら Fail Closed:
<xref href="Omni.VirtualObject.ProceduralMeshRepresentation.Failure" data-throw-if-not-resolved="false"></xref> に理由を残して資源を捨て、準備できた状態にならない（<xref href="Omni.VirtualObject.ProceduralMeshRepresentation.ResetFailure" data-throw-if-not-resolved="false"></xref> までやり直さない）。

```csharp
public sealed class ProceduralMeshRepresentation : IVirtualRepresentation
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[ProceduralMeshRepresentation](Omni.VirtualObject.ProceduralMeshRepresentation.md)

#### 実装するインターフェース（Implements）

[IVirtualRepresentation](Omni.VirtualObject.IVirtualRepresentation.md)

## コンストラクター（Constructors）

### <a id="Omni_VirtualObject_ProceduralMeshRepresentation__ctor_Omni_VirtualObject_ProceduralMeshStep_UnityEngine_Material_UnityEngine_Transform_System_Int32_System_Int32_System_Int64_System_String_"></a> ProceduralMeshRepresentation\(ProceduralMeshStep, Material, Transform, int, int, long, string\)

```csharp
public ProceduralMeshRepresentation(ProceduralMeshStep step, Material material, Transform parent, int trianglesPerPrepare, int maxTriangles, long maxBytes, string name = "VO Procedural Mesh")
```

#### 引数（Parameters）

`step` [ProceduralMeshStep](Omni.VirtualObject.ProceduralMeshStep.md)

`material` Material

`parent` Transform

`trianglesPerPrepare` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`maxTriangles` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`maxBytes` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`name` [string](https://learn.microsoft.com/dotnet/api/system.string)

## プロパティ（Properties）

### <a id="Omni_VirtualObject_ProceduralMeshRepresentation_ByteCount"></a> ByteCount

この表現が今持つ資源の大きさ（バイト。診断と見積もり用）。

```csharp
public long ByteCount { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_VirtualObject_ProceduralMeshRepresentation_Failure"></a> Failure

最後の失敗の理由（なければ null）。

```csharp
public string Failure { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_VirtualObject_ProceduralMeshRepresentation_Host"></a> Host

```csharp
public GameObject Host { get; }
```

#### 値（Property Value）

 GameObject

### <a id="Omni_VirtualObject_ProceduralMeshRepresentation_IsReady"></a> IsReady

描ける状態か（資源が揃っている）。false の間は、この表現へは上がらない（今の表現を描き続ける）。
描いている間（IsShown が true の間）は true のままにする。

```csharp
public bool IsReady { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_VirtualObject_ProceduralMeshRepresentation_IsShown"></a> IsShown

いま描かれているか（Show 済みで Hide されていない）。

```csharp
public bool IsShown { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_VirtualObject_ProceduralMeshRepresentation_Mesh"></a> Mesh

作ったメッシュ（できる前と解放後は null）。

```csharp
public Mesh Mesh { get; }
```

#### 値（Property Value）

 Mesh

### <a id="Omni_VirtualObject_ProceduralMeshRepresentation_TriangleCount"></a> TriangleCount

この表現が描く三角形の数（診断と見積もり用）。

```csharp
public int TriangleCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_VirtualObject_ProceduralMeshRepresentation_Hide"></a> Hide\(\)

描くのをやめる（冪等）。資源の解放は表現が決める（遅延破棄など）。

```csharp
public void Hide()
```

### <a id="Omni_VirtualObject_ProceduralMeshRepresentation_Prepare"></a> Prepare\(\)

準備を進める。この表現が望まれているのに IsReady が false の間、毎回の Tick で呼ばれる（冪等）。
一度に作る量は表現が自分で絞る（1 フレームに 1 区画など。長い停止を作らない）。

```csharp
public void Prepare()
```

### <a id="Omni_VirtualObject_ProceduralMeshRepresentation_Release"></a> Release\(\)

描くのをやめ、メッシュと GameObject と材料を捨てる（再び Prepare すると最初から作る）。

```csharp
public void Release()
```

### <a id="Omni_VirtualObject_ProceduralMeshRepresentation_ResetFailure"></a> ResetFailure\(\)

失敗の記録を消して、最初から作り直せるようにする（上限を変えたときなど）。

```csharp
public void ResetFailure()
```

### <a id="Omni_VirtualObject_ProceduralMeshRepresentation_Show"></a> Show\(\)

描き始める。IsReady のときだけ呼ばれる（冪等）。

```csharp
public void Show()
```
