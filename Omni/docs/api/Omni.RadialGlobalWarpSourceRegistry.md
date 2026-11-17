# <a id="Omni_RadialGlobalWarpSourceRegistry"></a> Class RadialGlobalWarpSourceRegistry

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

「どのカメラを描画するか」と「どこを中心にワープするか」を分離するための
カメラ単位のレジストリです。

<p>
<xref href="Omni.RadialGlobalRenderSystem" data-throw-if-not-resolved="false"></xref> は通常、描画中カメラ自身の
<xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref> をワープ元にします。観察カメラのように
「カメラAの投影を適用した世界を、カメラBから外部観察する」場合は、観察カメラ自身に
ドライバを持たせず、本レジストリで観察カメラと投影中心ドライバを対応付けます
（<code>Omni.Observer.RadialObserverRig</code> が利用します）。
</p>
<p>
観察カメラにドライバを持たせない点が重要です。共有 Unity Transform を書き換える
システムはどれも <code>camera.GetComponent&lt;RadialCamera&gt;()</code> を要求し、
本レジストリを参照しません。したがって観察カメラはそれらの対象外となり、
「観察用の Unity 座標を共有 Transform へ書き込まない」ことが構造的に保証されます。
</p>
<p>
登録時にはワープ元のほかに、カメラ単位の <xref href="Omni.Logical.SceneViewRenderContext" data-throw-if-not-resolved="false"></xref>
の供給元を渡せます。Editor の Scene View は <xref href="Omni.RadialGlobalRenderSystem.SceneViewContextProvider" data-throw-if-not-resolved="false"></xref>
でこれを供給しますが、Game／Player の観察カメラにはそれが無いため、同じ契約
（仮想論理視点と比較モード）をここから渡します。
</p>
<p>
既存の <xref href="Omni.RadialGlobalRenderSystem.SceneViewDriverProvider" data-throw-if-not-resolved="false"></xref>（単一スロット）は
変更しません。本レジストリは解決順序の中間に入り、登録の無いカメラでは
従来どおり Provider が呼ばれます。
</p>

```csharp
public static class RadialGlobalWarpSourceRegistry
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialGlobalWarpSourceRegistry](Omni.RadialGlobalWarpSourceRegistry.md)

## プロパティ（Properties）

### <a id="Omni_RadialGlobalWarpSourceRegistry_Count"></a> Count

登録済みのカメラ数です。0 のときは描画のホットパスが即座に抜けます。

```csharp
public static int Count { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_RadialGlobalWarpSourceRegistry_Register_UnityEngine_Camera_Omni_RadialWarpSource__System_Func_UnityEngine_Camera_Omni_Logical_SceneViewRenderContext__"></a> Register\(Camera, in RadialWarpSource, Func<Camera, SceneViewRenderContext\>\)

指定カメラのワープ元と、描画時に使う仮想論理視点の供給元を登録します。
同じカメラへの再登録は上書きです。

```csharp
public static void Register(Camera camera, in RadialWarpSource source, Func<Camera, SceneViewRenderContext> contextProvider)
```

#### 引数（Parameters）

`camera` Camera

観察カメラ。nullは無視します。

`source` [RadialWarpSource](Omni.RadialWarpSource.md)

ワープ元。ドライバを持たない値（<xref href="Omni.RadialWarpSource.None" data-throw-if-not-resolved="false"></xref>）は登録せず、既存の登録を外します。

`contextProvider` [Func](https://learn.microsoft.com/dotnet/api/system.func\-2)<Camera, [SceneViewRenderContext](Omni.Logical.SceneViewRenderContext.md)\>

描画のたびに呼ぶ仮想論理視点の供給元です。nullなら視点は供給せず、
カメラのTransformから論理位置を解決する従来の経路になります。

### <a id="Omni_RadialGlobalWarpSourceRegistry_TryResolve_UnityEngine_Camera_Omni_RadialWarpSource__"></a> TryResolve\(Camera, out RadialWarpSource\)

指定カメラのワープ元を解決します。

```csharp
public static bool TryResolve(Camera camera, out RadialWarpSource source)
```

#### 引数（Parameters）

`camera` Camera

描画中のカメラ。

`source` [RadialWarpSource](Omni.RadialWarpSource.md)

解決したワープ元。失敗時は <xref href="Omni.RadialWarpSource.None" data-throw-if-not-resolved="false"></xref>。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

有効な登録が見つかった場合は true。

### <a id="Omni_RadialGlobalWarpSourceRegistry_TryResolve_UnityEngine_Camera_Omni_RadialWarpSource__Omni_Logical_SceneViewRenderContext__"></a> TryResolve\(Camera, out RadialWarpSource, out SceneViewRenderContext\)

指定カメラのワープ元と仮想論理視点を解決します。

```csharp
public static bool TryResolve(Camera camera, out RadialWarpSource source, out SceneViewRenderContext context)
```

#### 引数（Parameters）

`camera` Camera

描画中のカメラ。

`source` [RadialWarpSource](Omni.RadialWarpSource.md)

解決したワープ元。失敗時は <xref href="Omni.RadialWarpSource.None" data-throw-if-not-resolved="false"></xref>。

`context` [SceneViewRenderContext](Omni.Logical.SceneViewRenderContext.md)

供給元が登録されていればその値、無ければ <xref href="Omni.Logical.SceneViewRenderContext.None" data-throw-if-not-resolved="false"></xref>。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

有効な登録が見つかった場合は true。

### <a id="Omni_RadialGlobalWarpSourceRegistry_Unregister_UnityEngine_Camera_"></a> Unregister\(Camera\)

登録を外します。登録が無かった場合は false です。

```csharp
public static bool Unregister(Camera camera)
```

#### 引数（Parameters）

`camera` Camera

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
