# <a id="Omni_BatchRendering_RadialBrgViewHeader"></a> Struct RadialBrgViewHeader

Namespace: [Omni.BatchRendering](Omni.BatchRendering.md)  
Assembly: Omni.BatchRendering.Runtime.dll  

CameraごとのBRG RawBuffer先頭に置く208 byteのヘッダーです。

<p>
各viewは同じResident粒子recordを持っても、このヘッダーだけはCamera固有です。
そのためGame View→Scene View→Game ViewでShader.SetGlobal*の競合を起こさず、
Saturnシーンの比較Cameraが互いの投影行列を上書きしません。
</p>

```csharp
public struct RadialBrgViewHeader
```

## フィールド（Fields）

### <a id="Omni_BatchRendering_RadialBrgViewHeader_EyeRelative"></a> EyeRelative

warp中心から見たlogical eyeのmantissa xyzとexponent wです。

```csharp
public Vector4 EyeRelative
```

#### 値（Field Value）

 Vector4

### <a id="Omni_BatchRendering_RadialBrgViewHeader_OrbitLocalToWorld"></a> OrbitLocalToWorld

Saturn ringのorbit local座標をRadial warpが受け取るworld logical座標へ変換する行列です。
平行移動は粒子中心に、3x3部分はquadのoffsetへ適用します。

```csharp
public Matrix4x4 OrbitLocalToWorld
```

#### 値（Field Value）

 Matrix4x4

### <a id="Omni_BatchRendering_RadialBrgViewHeader_Projection"></a> Projection

camera-relative mapped座標をclip座標へ変換するGPU投影行列です。

```csharp
public Matrix4x4 Projection
```

#### 値（Field Value）

 Matrix4x4

### <a id="Omni_BatchRendering_RadialBrgViewHeader_RadialSettings"></a> RadialSettings

RadialScale、mode、linearRadius、log2ViewScaleの順に並べた値です。

```csharp
public Vector4 RadialSettings
```

#### 値（Field Value）

 Vector4

### <a id="Omni_BatchRendering_RadialBrgViewHeader_ViewRow0"></a> ViewRow0

camera-relative mapped座標をview空間へ回す1行目です。

```csharp
public Vector4 ViewRow0
```

#### 値（Field Value）

 Vector4

### <a id="Omni_BatchRendering_RadialBrgViewHeader_ViewRow1"></a> ViewRow1

camera-relative mapped座標をview空間へ回す2行目です。

```csharp
public Vector4 ViewRow1
```

#### 値（Field Value）

 Vector4

### <a id="Omni_BatchRendering_RadialBrgViewHeader_ViewRow2"></a> ViewRow2

camera-relative mapped座標をview空間へ回す3行目です。

```csharp
public Vector4 ViewRow2
```

#### 値（Field Value）

 Vector4

## プロパティ（Properties）

### <a id="Omni_BatchRendering_RadialBrgViewHeader_Identity"></a> Identity

最小のidentityヘッダーを返します。BRG単体のdiagnostic sceneで使い、
実際のSaturn描画ではRadialViewSnapshotから作成した値へ必ず置き換えます。

```csharp
public static RadialBrgViewHeader Identity { get; }
```

#### 値（Property Value）

 [RadialBrgViewHeader](Omni.BatchRendering.RadialBrgViewHeader.md)

## メソッド（Methods）

### <a id="Omni_BatchRendering_RadialBrgViewHeader_IsFinite"></a> IsFinite\(\)

全フィールドがGPUへ安全に渡せる有限値かを返します。

```csharp
public bool IsFinite()
```

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_BatchRendering_RadialBrgViewHeader_TryCreate_Omni_Rendering_Radial_ViewSnapshot__UnityEngine_Matrix4x4_UnityEngine_Matrix4x4_Omni_BatchRendering_RadialBrgViewHeader__"></a> TryCreate\(in ViewSnapshot, Matrix4x4, Matrix4x4, out RadialBrgViewHeader\)

公開済みのCamera SnapshotとGPU投影行列からCamera固有headerを作成します。
Saturnシーンの <code>SaturnMesoBatchRenderer</code> が各Camera描画前に呼び、
Shader.SetGlobal*を経由せずper-view RawBufferへ渡します。

```csharp
public static bool TryCreate(in ViewSnapshot snapshot, Matrix4x4 gpuProjection, Matrix4x4 orbitLocalToWorld, out RadialBrgViewHeader header)
```

#### 引数（Parameters）

`snapshot` ViewSnapshot

RadialViewRegistryが同じCamera viewへ公開した不変Snapshotです。

`gpuProjection` Matrix4x4

Camera.projectionMatrixをGPU座標へ変換した有限の行列です。

`orbitLocalToWorld` Matrix4x4

orbit localをworld logical座標へ変換する有限行列です。

`header` [RadialBrgViewHeader](Omni.BatchRendering.RadialBrgViewHeader.md)

成功時の208 byte header。失敗時はIdentityで、呼び出し側は全Resident可視へ倒します。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

Camera限定のBRG描画に安全なheaderを作れた場合はtrueです。

### <a id="Omni_BatchRendering_RadialBrgViewHeader_TryCreate_Omni_Rendering_Radial_ViewSnapshot__UnityEngine_Matrix4x4_Omni_BatchRendering_RadialBrgViewHeader__"></a> TryCreate\(in ViewSnapshot, Matrix4x4, out RadialBrgViewHeader\)

互換用にidentityのorbit local変換でheaderを作成します。
実際のSaturn描画では、orbit originの <xref href="UnityEngine.Transform.localToWorldMatrix" data-throw-if-not-resolved="false"></xref> を渡す
4引数版を使わなければなりません。

```csharp
public static bool TryCreate(in ViewSnapshot snapshot, Matrix4x4 gpuProjection, out RadialBrgViewHeader header)
```

#### 引数（Parameters）

`snapshot` ViewSnapshot

RadialViewRegistryが同じCamera viewへ公開した不変Snapshotです。

`gpuProjection` Matrix4x4

Camera.projectionMatrixをGPU座標へ変換した有限の行列です。

`header` [RadialBrgViewHeader](Omni.BatchRendering.RadialBrgViewHeader.md)

成功時の208 byte headerです。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

Camera限定のBRG描画に安全なheaderを作れた場合はtrueです。
