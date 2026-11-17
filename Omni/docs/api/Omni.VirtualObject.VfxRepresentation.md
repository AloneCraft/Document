# <a id="Omni_VirtualObject_VfxRepresentation"></a> Class VfxRepresentation

Namespace: [Omni.VirtualObject](Omni.VirtualObject.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

VFX（<xref href="UnityEngine.VFX.VisualEffect" data-throw-if-not-resolved="false"></xref>）を 1 つの段の表現にする。準備で非アクティブな GameObject に VisualEffect を作り、Show で有効にして再生、Hide で停止して無効にする。
粒子の数や寿命は資産が決める。ここでは資源の大きさの見積もり（<code>byteCount</code>）だけを診断用に受け取る。

```csharp
public sealed class VfxRepresentation : IVirtualRepresentation
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VfxRepresentation](Omni.VirtualObject.VfxRepresentation.md)

#### 実装するインターフェース（Implements）

[IVirtualRepresentation](Omni.VirtualObject.IVirtualRepresentation.md)

## コンストラクター（Constructors）

### <a id="Omni_VirtualObject_VfxRepresentation__ctor_UnityEngine_VFX_VisualEffectAsset_UnityEngine_Transform_System_Action_UnityEngine_VFX_VisualEffect__System_Int64_System_String_"></a> VfxRepresentation\(VisualEffectAsset, Transform, Action<VisualEffect\>, long, string\)

```csharp
public VfxRepresentation(VisualEffectAsset asset, Transform parent = null, Action<VisualEffect> configure = null, long byteCount = 0, string name = "VO VFX")
```

#### 引数（Parameters）

`asset` VisualEffectAsset

再生する VFX 資産（null でも作れる。テストと、後から割り当てる使い方）。

`parent` Transform

生成する GameObject の親（null なら Scene の直下）。

`configure` [Action](https://learn.microsoft.com/dotnet/api/system.action\-1)<VisualEffect\>

作った直後（非アクティブの間）に呼ぶ。プロパティの初期値を入れる。

`byteCount` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`name` [string](https://learn.microsoft.com/dotnet/api/system.string)

## プロパティ（Properties）

### <a id="Omni_VirtualObject_VfxRepresentation_ByteCount"></a> ByteCount

この表現が今持つ資源の大きさ（バイト。診断と見積もり用）。

```csharp
public long ByteCount { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_VirtualObject_VfxRepresentation_Effect"></a> Effect

作った VisualEffect（準備前と破棄後は null）。

```csharp
public VisualEffect Effect { get; }
```

#### 値（Property Value）

 VisualEffect

### <a id="Omni_VirtualObject_VfxRepresentation_IsReady"></a> IsReady

描ける状態か（資源が揃っている）。false の間は、この表現へは上がらない（今の表現を描き続ける）。
描いている間（IsShown が true の間）は true のままにする。

```csharp
public bool IsReady { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_VirtualObject_VfxRepresentation_IsShown"></a> IsShown

いま描かれているか（Show 済みで Hide されていない）。

```csharp
public bool IsShown { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_VirtualObject_VfxRepresentation_TriangleCount"></a> TriangleCount

この表現が描く三角形の数（診断と見積もり用）。

```csharp
public int TriangleCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_VirtualObject_VfxRepresentation_Hide"></a> Hide\(\)

描くのをやめる（冪等）。資源の解放は表現が決める（遅延破棄など）。

```csharp
public void Hide()
```

### <a id="Omni_VirtualObject_VfxRepresentation_Prepare"></a> Prepare\(\)

準備を進める。この表現が望まれているのに IsReady が false の間、毎回の Tick で呼ばれる（冪等）。
一度に作る量は表現が自分で絞る（1 フレームに 1 区画など。長い停止を作らない）。

```csharp
public void Prepare()
```

### <a id="Omni_VirtualObject_VfxRepresentation_Release"></a> Release\(\)

描くのをやめて GameObject を破棄する（対象が不要になったとき）。

```csharp
public void Release()
```

### <a id="Omni_VirtualObject_VfxRepresentation_Show"></a> Show\(\)

描き始める。IsReady のときだけ呼ばれる（冪等）。

```csharp
public void Show()
```
