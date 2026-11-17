# <a id="Omni_VirtualObject_ScriptRepresentation"></a> Class ScriptRepresentation

Namespace: [Omni.VirtualObject](Omni.VirtualObject.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

<xref href="Omni.VirtualObject.ScriptRepresentation.Behaviour" data-throw-if-not-resolved="false"></xref>（MonoBehaviour など）を 1 つの段の表現にする。描く物を持たず、振る舞い（Script）の有効化だけを段に結びつける:
Show で <code>enabled = true</code> にして開始のコールバック、Hide で終了のコールバックを呼んで <code>enabled = false</code> にする。
既存の Behaviour を渡すか、準備で作る関数を渡す（作った Behaviour は無効のまま受け取る）。
開始のコールバックが例外を投げたときは、有効化を取り消して例外を投げ直す（Fail Closed。コントローラが今の段を保つ）。

```csharp
public sealed class ScriptRepresentation : IVirtualRepresentation
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[ScriptRepresentation](Omni.VirtualObject.ScriptRepresentation.md)

#### 実装するインターフェース（Implements）

[IVirtualRepresentation](Omni.VirtualObject.IVirtualRepresentation.md)

## コンストラクター（Constructors）

### <a id="Omni_VirtualObject_ScriptRepresentation__ctor_UnityEngine_Behaviour_System_Action_UnityEngine_Behaviour__System_Action_UnityEngine_Behaviour__"></a> ScriptRepresentation\(Behaviour, Action<Behaviour\>, Action<Behaviour\>\)

```csharp
public ScriptRepresentation(Behaviour behaviour, Action<Behaviour> onStart = null, Action<Behaviour> onStop = null)
```

#### 引数（Parameters）

`behaviour` Behaviour

`onStart` [Action](https://learn.microsoft.com/dotnet/api/system.action\-1)<Behaviour\>

`onStop` [Action](https://learn.microsoft.com/dotnet/api/system.action\-1)<Behaviour\>

### <a id="Omni_VirtualObject_ScriptRepresentation__ctor_System_Func_UnityEngine_Behaviour__System_Action_UnityEngine_Behaviour__System_Action_UnityEngine_Behaviour__"></a> ScriptRepresentation\(Func<Behaviour\>, Action<Behaviour\>, Action<Behaviour\>\)

```csharp
public ScriptRepresentation(Func<Behaviour> factory, Action<Behaviour> onStart = null, Action<Behaviour> onStop = null)
```

#### 引数（Parameters）

`factory` [Func](https://learn.microsoft.com/dotnet/api/system.func\-1)<Behaviour\>

`onStart` [Action](https://learn.microsoft.com/dotnet/api/system.action\-1)<Behaviour\>

`onStop` [Action](https://learn.microsoft.com/dotnet/api/system.action\-1)<Behaviour\>

## プロパティ（Properties）

### <a id="Omni_VirtualObject_ScriptRepresentation_Behaviour"></a> Behaviour

```csharp
public Behaviour Behaviour { get; }
```

#### 値（Property Value）

 Behaviour

### <a id="Omni_VirtualObject_ScriptRepresentation_ByteCount"></a> ByteCount

この表現が今持つ資源の大きさ（バイト。診断と見積もり用）。

```csharp
public long ByteCount { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_VirtualObject_ScriptRepresentation_IsReady"></a> IsReady

描ける状態か（資源が揃っている）。false の間は、この表現へは上がらない（今の表現を描き続ける）。
描いている間（IsShown が true の間）は true のままにする。

```csharp
public bool IsReady { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_VirtualObject_ScriptRepresentation_IsShown"></a> IsShown

いま描かれているか（Show 済みで Hide されていない）。

```csharp
public bool IsShown { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_VirtualObject_ScriptRepresentation_TriangleCount"></a> TriangleCount

この表現が描く三角形の数（診断と見積もり用）。

```csharp
public int TriangleCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_VirtualObject_ScriptRepresentation_Hide"></a> Hide\(\)

描くのをやめる（冪等）。資源の解放は表現が決める（遅延破棄など）。

```csharp
public void Hide()
```

### <a id="Omni_VirtualObject_ScriptRepresentation_Prepare"></a> Prepare\(\)

準備を進める。この表現が望まれているのに IsReady が false の間、毎回の Tick で呼ばれる（冪等）。
一度に作る量は表現が自分で絞る（1 フレームに 1 区画など。長い停止を作らない）。

```csharp
public void Prepare()
```

### <a id="Omni_VirtualObject_ScriptRepresentation_Show"></a> Show\(\)

描き始める。IsReady のときだけ呼ばれる（冪等）。

```csharp
public void Show()
```
