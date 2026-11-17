# <a id="Omni_Logical_OmniNearClip"></a> Struct OmniNearClip

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

そのフレームにカメラへ適用した論理 Near Clip の実値と、その決め方です。

<p>
「手前が切れすぎる／切れなさすぎる」の切り分けには、論理 Near（設定値）だけでなく
<b>実際に投影行列へ入った描画空間 near</b> と、それが厳密な平面だったのか保守的な
近似だったのかが要ります。<xref href="Omni.Logical.OmniCullingDebug.NoteCullingMatrix(UnityEngine.Camera%2cUnityEngine.Matrix4x4%40%2cSystem.String)" data-throw-if-not-resolved="false"></xref> と同じ理由で、
描画後に <xref href="UnityEngine.Camera.projectionMatrix" data-throw-if-not-resolved="false"></xref> を読み直しても復元できない情報
（恒等領域だったので<b>上書きしなかった</b>、など）を含むため、<b>決めた時点で</b>記録します。
</p>

```csharp
public readonly struct OmniNearClip
```

## フィールド（Fields）

### <a id="Omni_Logical_OmniNearClip_CameraNear"></a> CameraNear

<xref href="UnityEngine.Camera.nearClipPlane" data-throw-if-not-resolved="false"></xref> の値です。

```csharp
public readonly float CameraNear
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Logical_OmniNearClip_CenterUnderClipRatio"></a> CenterUnderClipRatio

画面中央での過小クリップ率です。厳密な構成では 0 です。

```csharp
public readonly float CenterUnderClipRatio
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Logical_OmniNearClip_CosMinAngle"></a> CosMinAngle

安全 near の評価に使った、視錐台対角方向のコサインです。

```csharp
public readonly float CosMinAngle
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Logical_OmniNearClip_HardwarePlaneMatches"></a> HardwarePlaneMatches

ハードウェア Near 平面が論理 Near 平面と厳密に一致する構成なら true です。

```csharp
public readonly bool HardwarePlaneMatches
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_OmniNearClip_Near"></a> Near

設定された論理 Near 距離（論理メートル）です。

```csharp
public readonly Scalar Near
```

#### 値（Field Value）

 [Scalar](Omni.Logical.Scalar.md)

### <a id="Omni_Logical_OmniNearClip_Orthographic"></a> Orthographic

平行投影として解決した場合は true です。

```csharp
public readonly bool Orthographic
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_OmniNearClip_RenderNear"></a> RenderNear

実際に投影行列へ入れた描画空間 near です。

```csharp
public readonly float RenderNear
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Logical_OmniNearClip_Resolved"></a> Resolved

論理 Near Clip の解決に成功した場合は true です。

```csharp
public readonly bool Resolved
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
