# <a id="Omni_VirtualObject_GameObjectRepresentation"></a> Class GameObjectRepresentation

Namespace: [Omni.VirtualObject](Omni.VirtualObject.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

GameObject を 1 つの段の表現にする。準備は供給元（<xref href="Omni.VirtualObject.IGameObjectSource" data-throw-if-not-resolved="false"></xref>）が生成し、Show で SetActive(true)、Hide で非アクティブか破棄。
三角形と資源の大きさは診断用の見積もりを渡す（実測ではない）。

```csharp
public sealed class GameObjectRepresentation : IVirtualRepresentation
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[GameObjectRepresentation](Omni.VirtualObject.GameObjectRepresentation.md)

#### 実装するインターフェース（Implements）

[IVirtualRepresentation](Omni.VirtualObject.IVirtualRepresentation.md)

## コンストラクター（Constructors）

### <a id="Omni_VirtualObject_GameObjectRepresentation__ctor_Omni_VirtualObject_IGameObjectSource_Omni_VirtualObject_VirtualHideMode_System_Int32_System_Int64_"></a> GameObjectRepresentation\(IGameObjectSource, VirtualHideMode, int, long\)

```csharp
public GameObjectRepresentation(IGameObjectSource source, VirtualHideMode hideMode = VirtualHideMode.Deactivate, int triangleCount = 0, long byteCount = 0)
```

#### 引数（Parameters）

`source` [IGameObjectSource](Omni.VirtualObject.IGameObjectSource.md)

`hideMode` [VirtualHideMode](Omni.VirtualObject.VirtualHideMode.md)

`triangleCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`byteCount` [long](https://learn.microsoft.com/dotnet/api/system.int64)

## プロパティ（Properties）

### <a id="Omni_VirtualObject_GameObjectRepresentation_ByteCount"></a> ByteCount

この表現が今持つ資源の大きさ（バイト。診断と見積もり用）。

```csharp
public long ByteCount { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_VirtualObject_GameObjectRepresentation_Instance"></a> Instance

生成済みのインスタンス（準備前と破棄後は null）。

```csharp
public GameObject Instance { get; }
```

#### 値（Property Value）

 GameObject

### <a id="Omni_VirtualObject_GameObjectRepresentation_IsReady"></a> IsReady

描ける状態か（資源が揃っている）。false の間は、この表現へは上がらない（今の表現を描き続ける）。
描いている間（IsShown が true の間）は true のままにする。

```csharp
public bool IsReady { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_VirtualObject_GameObjectRepresentation_IsShown"></a> IsShown

いま描かれているか（Show 済みで Hide されていない）。

```csharp
public bool IsShown { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_VirtualObject_GameObjectRepresentation_TriangleCount"></a> TriangleCount

この表現が描く三角形の数（診断と見積もり用）。

```csharp
public int TriangleCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_VirtualObject_GameObjectRepresentation_Hide"></a> Hide\(\)

描くのをやめる（冪等）。資源の解放は表現が決める（遅延破棄など）。

```csharp
public void Hide()
```

### <a id="Omni_VirtualObject_GameObjectRepresentation_Prepare"></a> Prepare\(\)

準備を進める。この表現が望まれているのに IsReady が false の間、毎回の Tick で呼ばれる（冪等）。
一度に作る量は表現が自分で絞る（1 フレームに 1 区画など。長い停止を作らない）。

```csharp
public void Prepare()
```

### <a id="Omni_VirtualObject_GameObjectRepresentation_Release"></a> Release\(\)

描くのをやめ、準備中の生成も捨てて、資源を返す（対象が不要になったとき）。

```csharp
public void Release()
```

### <a id="Omni_VirtualObject_GameObjectRepresentation_Show"></a> Show\(\)

描き始める。IsReady のときだけ呼ばれる（冪等）。

```csharp
public void Show()
```
