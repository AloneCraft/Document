# <a id="Omni_Rendering_Radial_Frustum"></a> Struct Frustum

Namespace: [Omni.Rendering.Radial](Omni.Rendering.Radial.md)  
Assembly: Radial.Runtime.dll  

Logical座標系で解釈するカメラ錐台です。巨大な絶対float座標を使わず、
<xref href="Omni.Rendering.Radial.Frustum.Origin" data-throw-if-not-resolved="false"></xref>と方向・投影値だけでBRGの安全な入力を表します。
SaturnシーンのMesoリングセル判定で使用します。

```csharp
public readonly struct Frustum
```

## コンストラクター（Constructors）

### <a id="Omni_Rendering_Radial_Frustum__ctor_Omni_Logical_Position3__UnityEngine_Vector3_UnityEngine_Vector3_System_Single_System_Single_System_Boolean_System_Single_System_Boolean_"></a> Frustum\(in Position3, Vector3, Vector3, float, float, bool, float, bool\)

論理錐台を構築します。

```csharp
public Frustum(in Position3 origin, Vector3 forward, Vector3 up, float verticalFieldOfViewDegrees, float aspect, bool isOrthographic, float orthographicSize, bool isValid)
```

#### 引数（Parameters）

`origin` [Position3](Omni.Logical.Position3.md)

`forward` Vector3

`up` Vector3

`verticalFieldOfViewDegrees` [float](https://learn.microsoft.com/dotnet/api/system.single)

`aspect` [float](https://learn.microsoft.com/dotnet/api/system.single)

`isOrthographic` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`orthographicSize` [float](https://learn.microsoft.com/dotnet/api/system.single)

`isValid` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## フィールド（Fields）

### <a id="Omni_Rendering_Radial_Frustum_Aspect"></a> Aspect

横幅/縦幅のアスペクト比です。

```csharp
public readonly float Aspect
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Rendering_Radial_Frustum_Forward"></a> Forward

論理錐台の前方向です。

```csharp
public readonly Vector3 Forward
```

#### 値（Field Value）

 Vector3

### <a id="Omni_Rendering_Radial_Frustum_IsOrthographic"></a> IsOrthographic

平行投影かどうかです。

```csharp
public readonly bool IsOrthographic
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Rendering_Radial_Frustum_IsValid"></a> IsValid

すべての錐台入力が安全に利用可能かどうかです。

```csharp
public readonly bool IsValid
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Rendering_Radial_Frustum_Origin"></a> Origin

論理錐台の原点、すなわち描画カメラのLogical eyeです。
<xref href="Omni.Rendering.Radial.ViewSnapshot.WarpCenter" data-throw-if-not-resolved="false"></xref>とは別の値であり、Observerでは一致しません。

```csharp
public readonly Position3 Origin
```

#### 値（Field Value）

 [Position3](Omni.Logical.Position3.md)

### <a id="Omni_Rendering_Radial_Frustum_OrthographicSize"></a> OrthographicSize

平行投影時の縦方向半サイズです。

```csharp
public readonly float OrthographicSize
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Rendering_Radial_Frustum_Up"></a> Up

論理錐台の上方向です。

```csharp
public readonly Vector3 Up
```

#### 値（Field Value）

 Vector3

### <a id="Omni_Rendering_Radial_Frustum_VerticalFieldOfViewDegrees"></a> VerticalFieldOfViewDegrees

透視投影の垂直視野角です。

```csharp
public readonly float VerticalFieldOfViewDegrees
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

## メソッド（Methods）

### <a id="Omni_Rendering_Radial_Frustum_CreateFailOpen_Omni_Logical_Position3__"></a> CreateFailOpen\(in Position3\)

カリング不能時に使う無効錐台を返します。呼び出し側はこの値を見て全表示へ倒します。

```csharp
public static Frustum CreateFailOpen(in Position3 origin)
```

#### 引数（Parameters）

`origin` [Position3](Omni.Logical.Position3.md)

#### 戻り値（Returns）

 [Frustum](Omni.Rendering.Radial.Frustum.md)

### <a id="Omni_Rendering_Radial_Frustum_TryCreate_UnityEngine_Camera_Omni_Logical_Position3__Omni_Rendering_Radial_Frustum__"></a> TryCreate\(Camera, in Position3, out Frustum\)

Unityカメラから有限な論理錐台を構築します。

```csharp
public static bool TryCreate(Camera camera, in Position3 origin, out Frustum frustum)
```

#### 引数（Parameters）

`camera` Camera

描画中のカメラ。nullなら失敗します。

`origin` [Position3](Omni.Logical.Position3.md)

Logical座標上の描画カメラeyeです。ワープ中心は渡しません。

`frustum` [Frustum](Omni.Rendering.Radial.Frustum.md)

成功時の有限な錐台。失敗時はfail-open用の無効値です。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

BRGのカリング入力として安全な錐台を作れた場合はtrueです。
