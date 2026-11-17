# <a id="Omni_VirtualObject_IVirtualRepresentation"></a> Interface IVirtualRepresentation

Namespace: [Omni.VirtualObject](Omni.VirtualObject.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

Virtual Object の「表現」1 つ（段 1 つぶん）。段 0 が最も粗い表現（点・基材のメッシュなど）、段が上がるほど細かい。
表現は自分で資源（メッシュ・BRG 登録・VG の cell など）を作って持つ。VirtualObjectController が、画素の大きさと IsReady から、描く表現を 1 つ選ぶ。
Asteria の型には依存しない（VG の地形を R1 の表現として包むときも、この契約をそのまま使う）。

```csharp
public interface IVirtualRepresentation
```

## プロパティ（Properties）

### <a id="Omni_VirtualObject_IVirtualRepresentation_ByteCount"></a> ByteCount

この表現が今持つ資源の大きさ（バイト。診断と見積もり用）。

```csharp
long ByteCount { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_VirtualObject_IVirtualRepresentation_IsReady"></a> IsReady

描ける状態か（資源が揃っている）。false の間は、この表現へは上がらない（今の表現を描き続ける）。
描いている間（IsShown が true の間）は true のままにする。

```csharp
bool IsReady { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_VirtualObject_IVirtualRepresentation_IsShown"></a> IsShown

いま描かれているか（Show 済みで Hide されていない）。

```csharp
bool IsShown { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_VirtualObject_IVirtualRepresentation_TriangleCount"></a> TriangleCount

この表現が描く三角形の数（診断と見積もり用）。

```csharp
int TriangleCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_VirtualObject_IVirtualRepresentation_Hide"></a> Hide\(\)

描くのをやめる（冪等）。資源の解放は表現が決める（遅延破棄など）。

```csharp
void Hide()
```

### <a id="Omni_VirtualObject_IVirtualRepresentation_Prepare"></a> Prepare\(\)

準備を進める。この表現が望まれているのに IsReady が false の間、毎回の Tick で呼ばれる（冪等）。
一度に作る量は表現が自分で絞る（1 フレームに 1 区画など。長い停止を作らない）。

```csharp
void Prepare()
```

### <a id="Omni_VirtualObject_IVirtualRepresentation_Show"></a> Show\(\)

描き始める。IsReady のときだけ呼ばれる（冪等）。

```csharp
void Show()
```
