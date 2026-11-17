# <a id="Omni_Logical_NavigationBounds"></a> Class NavigationBounds

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

Rendererを持たない対象（頂点をGPUで生成する地形など）に付けて、Scene Viewの接近・飛行の基準になる大きさを
Inspectorで宣言するcomponentです。実装は<xref href="Omni.Logical.INavigationBoundsSource" data-throw-if-not-resolved="false"></xref>の標準版です。
実行時の表示やLogical Transformには影響しません。

```csharp
[AddComponentMenu("Omni/Navigation Bounds")]
[DisallowMultipleComponent]
public sealed class NavigationBounds : MonoBehaviour, INavigationBoundsSource
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[NavigationBounds](Omni.Logical.NavigationBounds.md)

#### 実装するインターフェース（Implements）

[INavigationBoundsSource](Omni.Logical.INavigationBoundsSource.md)

## プロパティ（Properties）

### <a id="Omni_Logical_NavigationBounds_Center"></a> Center

この GameObject のローカル空間での中心(m)。

```csharp
public Vector3 Center { get; set; }
```

#### 値（Property Value）

 Vector3

### <a id="Omni_Logical_NavigationBounds_Size"></a> Size

ローカル空間での大きさ(m)。負の値は無効として扱われます。

```csharp
public Vector3 Size { get; set; }
```

#### 値（Property Value）

 Vector3

## メソッド（Methods）

### <a id="Omni_Logical_NavigationBounds_TryGetNavigationLocalBounds_UnityEngine_Bounds__"></a> TryGetNavigationLocalBounds\(out Bounds\)

この対象のTransformを基準にしたローカル空間のBoundsを返します。

```csharp
public bool TryGetNavigationLocalBounds(out Bounds localBounds)
```

#### 引数（Parameters）

`localBounds` Bounds

ローカル座標のBounds（中心とsizeはメートル）。失敗時は未定義です。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

有効なBoundsを返せた場合はtrueです。
