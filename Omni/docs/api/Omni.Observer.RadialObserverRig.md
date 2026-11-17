# <a id="Omni_Observer_RadialObserverRig"></a> Class RadialObserverRig

Namespace: [Omni.Observer](Omni.Observer.md)  
Assembly: Omni.RadialObserver.dll  

<xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref>が見ている「変形後の世界」を、別のカメラ（観察枠）から外側へ引いて見るためのRigです。

<p>
観察枠のCameraには<xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref>を付けません。<xref href="Omni.RadialGlobalWarpSourceRegistry" data-throw-if-not-resolved="false"></xref>へ
「ワープ中心＝ソースのRadialCamera」「仮想論理視点＝Pivotがソース位置C、PhysicalPivotがこのRigの原点」と登録し、
比較表示と同じ契約（対象だけを<code>C+F(P-C)</code>へ圧縮し、視点Eは物理位置のまま）で描かせます。
</p>
<p>
Rig配下は有限な描画空間です（原点がC）。LogicalTransformを付けないため、Cinemachineと同居できます。
Rig自体は動かさず、Cへの追従はPivot（論理）側で行います。既定ではPlayモードだけで動作します。
<xref href="Omni.Observer.RadialObserverRig.RunInEditMode" data-throw-if-not-resolved="false"></xref>をオンにしたRigだけ、Editモードでも登録と枠の表示を行います（オフのRigはEditモードで何も変えません）。
</p>

```csharp
[ExecuteAlways]
[DisallowMultipleComponent]
[DefaultExecutionOrder(100)]
[AddComponentMenu("Omni/Radial Observer Rig")]
public sealed class RadialObserverRig : MonoBehaviour
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[RadialObserverRig](Omni.Observer.RadialObserverRig.md)

## プロパティ（Properties）

### <a id="Omni_Observer_RadialObserverRig_ActiveSource"></a> ActiveSource

現在のソースRadialCameraです。見つからなければnull。

```csharp
public RadialCamera ActiveSource { get; }
```

#### 値（Property Value）

 RadialCamera

### <a id="Omni_Observer_RadialObserverRig_Corner"></a> Corner

```csharp
public ObserverCorner Corner { get; set; }
```

#### 値（Property Value）

 [ObserverCorner](Omni.Observer.ObserverCorner.md)

### <a id="Omni_Observer_RadialObserverRig_DistanceInScale"></a> DistanceInScale

Cからカメラまでの距離をSの何倍にするかです。

```csharp
public float DistanceInScale { get; set; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Observer_RadialObserverRig_Focus"></a> Focus

注視点（Rig原点＝Cに対する変形後の位置）の親Transformです。

```csharp
public Transform Focus { get; }
```

#### 値（Property Value）

 Transform

### <a id="Omni_Observer_RadialObserverRig_Layout"></a> Layout

```csharp
public ObserverLayoutPreset Layout { get; set; }
```

#### 値（Property Value）

 [ObserverLayoutPreset](Omni.Observer.ObserverLayoutPreset.md)

### <a id="Omni_Observer_RadialObserverRig_RunInEditMode"></a> RunInEditMode

Editモード（Playしていないとき）でも動作するかです。既定はオフ（Playモードだけ）。

```csharp
public bool RunInEditMode { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_Observer_RadialObserverRig_Configure_UnityEngine_Transform_Omni_Observer_RadialObserverSlot___Omni_RadialCamera_"></a> Configure\(Transform, RadialObserverSlot\[\], RadialCamera\)

コードからRigを構成します（Prefab生成とテスト用）。

```csharp
public void Configure(Transform focus, RadialObserverSlot[] slots, RadialCamera source = null)
```

#### 引数（Parameters）

`focus` Transform

`slots` [RadialObserverSlot](Omni.Observer.RadialObserverSlot.md)\[\]

`source` RadialCamera

### <a id="Omni_Observer_RadialObserverRig_TryGetFrame_Omni_Observer_ObserverFrame__"></a> TryGetFrame\(out ObserverFrame\)

直近のフレームで有効な枠取り結果を得られているかを返します。

```csharp
public bool TryGetFrame(out ObserverFrame frame)
```

#### 引数（Parameters）

`frame` [ObserverFrame](Omni.Observer.ObserverFrame.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
