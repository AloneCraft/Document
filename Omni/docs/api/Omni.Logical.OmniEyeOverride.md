# <a id="Omni_Logical_OmniEyeOverride"></a> Struct OmniEyeOverride

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

そのフレームにカメラの目（<xref href="UnityEngine.Camera.worldToCameraMatrix" data-throw-if-not-resolved="false"></xref>）をワープ中心基準へ
上書きしたかどうかと、その判断材料です。

<p>
自己中心モードでこの上書きが誤って適用されると、目とワープ中心が別々の座標系で解決されて
食い違い、本来ゼロであるべき相対位置が非ゼロになって画面が変形します。この構造体は
「目とワープ中心の距離」を1行で読めるようにし、変形が残ったときに「まだ乖離があるのか」
「乖離0なのに崩れているのか（別の既知問題）」を推測せず切り分けるためのものです。
<xref href="Omni.Logical.OmniCullingDebug.NoteCullingMatrix(UnityEngine.Camera%2cUnityEngine.Matrix4x4%40%2cSystem.String)" data-throw-if-not-resolved="false"></xref>と同じ理由で、<b>適用した時点で</b>記録します。
</p>

```csharp
public readonly struct OmniEyeOverride
```

## フィールド（Fields）

### <a id="Omni_Logical_OmniEyeOverride_Applied"></a> Applied

目の位置をワープ後の値へ上書きした場合はtrueです。

```csharp
public readonly bool Applied
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_OmniEyeOverride_EyeRenderPosition"></a> EyeRenderPosition

上書き後（または上書きしなかった場合はカメラの物理位置）の目の位置です。

```csharp
public readonly Vector3 EyeRenderPosition
```

#### 値（Field Value）

 Vector3

### <a id="Omni_Logical_OmniEyeOverride_WarpCenter"></a> WarpCenter

ワープ中心（driverの物理位置）です。

```csharp
public readonly Vector3 WarpCenter
```

#### 値（Field Value）

 Vector3

## プロパティ（Properties）

### <a id="Omni_Logical_OmniEyeOverride_Distance"></a> Distance

目とワープ中心の距離です。

```csharp
public float Distance { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)
