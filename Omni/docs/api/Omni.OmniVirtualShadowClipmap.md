# <a id="Omni_OmniVirtualShadowClipmap"></a> Class OmniVirtualShadowClipmap

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

仮想シャドウマップの段(クリップマップ)。光の向きの正射影で、基準点を中心に段を重ねる。各段はページの格子に合わせた窓(PagesPerAxis² ページ)を持つ。

<p>
座標: 基準点(warp center。Radial を使わない Camera ではカメラ)の Unity の座標を double で受け取り、光の座標の格子番号の整数部と端数を CPU で求める。
GPU は「端数 + 基準点からの相対位置 ÷ テクセル」だけを float で足す(巨大な値どうしを float で引かない)。
ページの番号は Unity の座標に固定した格子の番号なので、Unity の座標の原点が動かない限り、フレームをまたいで同じページを使い回せる。
</p>

```csharp
public sealed class OmniVirtualShadowClipmap
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniVirtualShadowClipmap](Omni.OmniVirtualShadowClipmap.md)

## コンストラクター（Constructors）

### <a id="Omni_OmniVirtualShadowClipmap__ctor_Omni_OmniVirtualShadowSettings__"></a> OmniVirtualShadowClipmap\(in OmniVirtualShadowSettings\)

```csharp
public OmniVirtualShadowClipmap(in OmniVirtualShadowSettings settings)
```

#### 引数（Parameters）

`settings` [OmniVirtualShadowSettings](Omni.OmniVirtualShadowSettings.md)

## フィールド（Fields）

### <a id="Omni_OmniVirtualShadowClipmap_MaximumLevels"></a> MaximumLevels

```csharp
public const int MaximumLevels = 16
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="Omni_OmniVirtualShadowClipmap_Anchor"></a> Anchor

```csharp
public ShadowVector3d Anchor { get; }
```

#### 値（Property Value）

 [ShadowVector3d](Omni.ShadowVector3d.md)

### <a id="Omni_OmniVirtualShadowClipmap_Forward"></a> Forward

```csharp
public ShadowVector3d Forward { get; }
```

#### 値（Property Value）

 [ShadowVector3d](Omni.ShadowVector3d.md)

### <a id="Omni_OmniVirtualShadowClipmap_IsValid"></a> IsValid

```csharp
public bool IsValid { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_OmniVirtualShadowClipmap_Right"></a> Right

```csharp
public ShadowVector3d Right { get; }
```

#### 値（Property Value）

 [ShadowVector3d](Omni.ShadowVector3d.md)

### <a id="Omni_OmniVirtualShadowClipmap_Settings"></a> Settings

```csharp
public OmniVirtualShadowSettings Settings { get; }
```

#### 値（Property Value）

 [OmniVirtualShadowSettings](Omni.OmniVirtualShadowSettings.md)

### <a id="Omni_OmniVirtualShadowClipmap_Up"></a> Up

```csharp
public ShadowVector3d Up { get; }
```

#### 値（Property Value）

 [ShadowVector3d](Omni.ShadowVector3d.md)

## メソッド（Methods）

### <a id="Omni_OmniVirtualShadowClipmap_GetLevel_System_Int32_"></a> GetLevel\(int\)

```csharp
public ref readonly OmniVirtualShadowClipmap.Level GetLevel(int level)
```

#### 引数（Parameters）

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [OmniVirtualShadowClipmap](Omni.OmniVirtualShadowClipmap.md).[Level](Omni.OmniVirtualShadowClipmap.Level.md)

### <a id="Omni_OmniVirtualShadowClipmap_LevelViewProjection_System_Int32_System_Int32_System_Int32_"></a> LevelViewProjection\(int, int, int\)

段 k の窓を、基準点からの相対位置の正射影にする行列(光の座標の窓 → クリップ座標、奥行きは基準点の前後 DepthRange)。
影を落とす物を描くときは、これに Unity の座標からの平行移動(−基準点)を掛ける。GPU のクリップ座標の規約(反転 Z)は呼び出し側が GL.GetGPUProjectionMatrix で合わせる。

```csharp
public Matrix4x4 LevelViewProjection(int level, int pageX = -1, int pageY = -1)
```

#### 引数（Parameters）

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`pageX` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`pageY` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 Matrix4x4

### <a id="Omni_OmniVirtualShadowClipmap_SelectLevel_Omni_OmniVirtualShadowSettings__System_Double_"></a> SelectLevel\(in OmniVirtualShadowSettings, double\)

画素の地上の大きさ(光の座標で測った 1 画素の幅、m)から段を選ぶ。1 テクセルが画素の大きさ以下になる、最も粗い段(=最も細かい段から数えて最初に足りる段)。
範囲外は -1。shader の VsmSelectLevel と同じ式。

```csharp
public static int SelectLevel(in OmniVirtualShadowSettings settings, double pixelMeters)
```

#### 引数（Parameters）

`settings` [OmniVirtualShadowSettings](Omni.OmniVirtualShadowSettings.md)

`pixelMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_OmniVirtualShadowClipmap_Update_Omni_ShadowVector3d_UnityEngine_Quaternion_"></a> Update\(ShadowVector3d, Quaternion\)

基準点(Unity の座標、double)と光の回転(光は +Z の向きへ進む)から、各段の窓を決める。
窓は基準点のページを中心に、PagesPerAxis/2 ページずつ左右・上下へ広げる。

```csharp
public void Update(ShadowVector3d anchorUnity, Quaternion lightRotation)
```

#### 引数（Parameters）

`anchorUnity` [ShadowVector3d](Omni.ShadowVector3d.md)

`lightRotation` Quaternion

### <a id="Omni_OmniVirtualShadowClipmap_WindowPosition_System_Int32_Omni_ShadowVector3d_"></a> WindowPosition\(int, ShadowVector3d\)

基準点からの相対位置(Unity の座標の差、m)の、段 k の窓の中の位置(ページの単位、0〜PagesPerAxis)。

```csharp
public ShadowVector2d WindowPosition(int level, ShadowVector3d relative)
```

#### 引数（Parameters）

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`relative` [ShadowVector3d](Omni.ShadowVector3d.md)

#### 戻り値（Returns）

 [ShadowVector2d](Omni.ShadowVector2d.md)
