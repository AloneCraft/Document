# <a id="Omni_Logical_INavigationBoundsSource"></a> Interface INavigationBoundsSource

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

Rendererを持たない対象（頂点を実行時に生成する地形など）が、Scene Viewの接近・飛行の基準になる
大きさを宣言するための契約です。

<p>
Rendererが無いと、Omniは対象をLogical Transformの位置にある直径の小さな点として扱います。
実際の大きさが数百kmあっても、ホイール1ノッチが「遠い点までの距離の一定割合」になり、
面の上にいる目が数十km飛びます。このcomponentを付けると、Rendererの<code>localBounds</code>と同じ規則
（Logical Transformの姿勢で8頂点を包む外接球）で対象の大きさを使います。
</p>

```csharp
public interface INavigationBoundsSource
```

## メソッド（Methods）

### <a id="Omni_Logical_INavigationBoundsSource_TryGetNavigationLocalBounds_UnityEngine_Bounds__"></a> TryGetNavigationLocalBounds\(out Bounds\)

この対象のTransformを基準にしたローカル空間のBoundsを返します。

```csharp
bool TryGetNavigationLocalBounds(out Bounds localBounds)
```

#### 引数（Parameters）

`localBounds` Bounds

ローカル座標のBounds（中心とsizeはメートル）。失敗時は未定義です。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

有効なBoundsを返せた場合はtrueです。
