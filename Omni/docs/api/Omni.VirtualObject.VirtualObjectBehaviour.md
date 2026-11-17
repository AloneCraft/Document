# <a id="Omni_VirtualObject_VirtualObjectBehaviour"></a> Class VirtualObjectBehaviour

Namespace: [Omni.VirtualObject](Omni.VirtualObject.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

Virtual Object を Scene で組み立てる component。段のリスト（画素の閾値と表現）を持ち、毎フレーム、対象の画面上の大きさ（画素）を
求めて <xref href="Omni.VirtualObject.VirtualObjectController.Tick(System.Double)" data-throw-if-not-resolved="false"></xref> を呼ぶ。位置は Logical が正本: 対象とカメラの Logical 位置の差を固定小数点で引いてから double にし、
大きさは対象の <xref href="Omni.Logical.INavigationBoundsSource" data-throw-if-not-resolved="false"></xref>（なければ <code>radiusMeters</code>）の外接球から求める。
段の表現は、Inspector で選べる種類（GameObject の Prefab、VFX 資産、既存の Behaviour）か、コードから <xref href="Omni.VirtualObject.VirtualObjectBehaviour.SetLevels(Omni.VirtualObject.VirtualObjectSelector%2cOmni.VirtualObject.IVirtualRepresentation%5b%5d)" data-throw-if-not-resolved="false"></xref> で渡す
（プロシージャルメッシュ・VG の地形など、関数や供給元が要る表現はコードから）。

```csharp
[DisallowMultipleComponent]
public sealed class VirtualObjectBehaviour : MonoBehaviour
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[VirtualObjectBehaviour](Omni.VirtualObject.VirtualObjectBehaviour.md)

## プロパティ（Properties）

### <a id="Omni_VirtualObject_VirtualObjectBehaviour_Active"></a> Active

有効な VirtualObjectBehaviour の一覧（デバッグの可視化用）。DontSaveInEditor の階層の物は FindObjectsByType で見つからないので、自分で登録する。

```csharp
public static IReadOnlyList<VirtualObjectBehaviour> Active { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[VirtualObjectBehaviour](Omni.VirtualObject.VirtualObjectBehaviour.md)\>

### <a id="Omni_VirtualObject_VirtualObjectBehaviour_Controller"></a> Controller

```csharp
public VirtualObjectController Controller { get; }
```

#### 値（Property Value）

 [VirtualObjectController](Omni.VirtualObject.VirtualObjectController.md)

### <a id="Omni_VirtualObject_VirtualObjectBehaviour_Failure"></a> Failure

組み立てや大きさの計算に失敗した理由（なければ null）。

```csharp
public string Failure { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_VirtualObject_VirtualObjectBehaviour_HasView"></a> HasView

```csharp
public bool HasView { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_VirtualObject_VirtualObjectBehaviour_LastDirection"></a> LastDirection

最後に測った、カメラから対象への向き（world 軸の単位ベクトル）と物理距離（m）。<xref href="Omni.VirtualObject.VirtualObjectBehaviour.HasView" data-throw-if-not-resolved="false"></xref> が false なら無効。
Radial の写像は向きを変えない（視点から対象への光線の上で距離だけを写す）ので、この向きは対数描画でも標準描画でも画面の位置を決める
（デバッグの表示用。大きな値は float にできず、向きが求められないことがある）。

```csharp
public Vector3 LastDirection { get; }
```

#### 値（Property Value）

 Vector3

### <a id="Omni_VirtualObject_VirtualObjectBehaviour_LastDistance"></a> LastDistance

```csharp
public double LastDistance { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_VirtualObject_VirtualObjectBehaviour_LastPixels"></a> LastPixels

最後に求めた画面上の大きさ（画素）。求められなかったときは 0。

```csharp
public double LastPixels { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_VirtualObject_VirtualObjectBehaviour_RadiusMeters"></a> RadiusMeters

対象の大きさの供給元がないときの外接球の半径（m）。

```csharp
public double RadiusMeters { get; set; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_VirtualObject_VirtualObjectBehaviour_Stages"></a> Stages

```csharp
public VirtualObjectBehaviour.Stage[] Stages { get; set; }
```

#### 値（Property Value）

 [VirtualObjectBehaviour](Omni.VirtualObject.VirtualObjectBehaviour.md).[Stage](Omni.VirtualObject.VirtualObjectBehaviour.Stage.md)\[\]

### <a id="Omni_VirtualObject_VirtualObjectBehaviour_Subject"></a> Subject

```csharp
public Transform Subject { get; set; }
```

#### 値（Property Value）

 Transform

### <a id="Omni_VirtualObject_VirtualObjectBehaviour_ViewCamera"></a> ViewCamera

```csharp
public Camera ViewCamera { get; set; }
```

#### 値（Property Value）

 Camera

## メソッド（Methods）

### <a id="Omni_VirtualObject_VirtualObjectBehaviour_SetLevels_Omni_VirtualObject_VirtualObjectSelector_Omni_VirtualObject_IVirtualRepresentation___"></a> SetLevels\(VirtualObjectSelector, IVirtualRepresentation\[\]\)

表現をコードから渡す（Inspector の段を使わない）。段の数は <code>selector.LevelCount</code> と同じ。frame の世話が要る表現
（<xref href="Omni.VirtualObject.IVirtualRepresentationFrame" data-throw-if-not-resolved="false"></xref>）は、毎フレーム Tick の後に呼ぶ。

```csharp
public void SetLevels(VirtualObjectSelector selector, IVirtualRepresentation[] representations)
```

#### 引数（Parameters）

`selector` [VirtualObjectSelector](Omni.VirtualObject.VirtualObjectSelector.md)

`representations` [IVirtualRepresentation](Omni.VirtualObject.IVirtualRepresentation.md)\[\]

### <a id="Omni_VirtualObject_VirtualObjectBehaviour_Tick"></a> Tick\(\)

1 回ぶんの更新（Update が毎フレーム呼ぶ。EditMode のテストと、手動の更新にも使える）。大きさを測って段を更新できたら true。
段がまだ組み立てられていなければ、Inspector の段から組み立てる（失敗したら <xref href="Omni.VirtualObject.VirtualObjectBehaviour.Failure" data-throw-if-not-resolved="false"></xref> に理由を残して false）。

```csharp
public bool Tick()
```

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_VirtualObject_VirtualObjectBehaviour_TryDistance_Omni_Logical_Position3__Omni_Logical_Position3__System_Double__"></a> TryDistance\(in Position3, in Position3, out double\)

2 つの Logical 位置の距離（m、double）。差は固定小数点で引く。

```csharp
public static bool TryDistance(in Position3 a, in Position3 b, out double meters)
```

#### 引数（Parameters）

`a` Position3

`b` Position3

`meters` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
