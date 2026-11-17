# <a id="Omni_Editor_State_OmniViewState"></a> Class OmniViewState

Namespace: [Omni.Editor.State](Omni.Editor.State.md)  
Assembly: Omni.Editor.dll  

1つのScene Viewに属する表示状態です。RadialCamera選択と探索モードは
Scene ViewのEntity IDごとにEditor Sessionへ保存します。

```csharp
public sealed class OmniViewState
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniViewState](Omni.Editor.State.OmniViewState.md)

## プロパティ（Properties）

### <a id="Omni_Editor_State_OmniViewState_AutomaticNear"></a> AutomaticNear

編集尺度と撮影距離からNearを調整します。既定は固定です。

```csharp
public bool AutomaticNear { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_State_OmniViewState_ComparisonMode"></a> ComparisonMode

互換用の旧プロパティです。trueは実カメラ基準の観察モードを表します。

```csharp
public bool ComparisonMode { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_State_OmniViewState_ConnectionWireEnabled"></a> ConnectionWireEnabled

Standard-Radial間の接続ワイヤー表示です。

```csharp
public bool ConnectionWireEnabled { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_State_OmniViewState_ExploreFromSceneView"></a> ExploreFromSceneView

選択したRadialCameraの設定を使い、このScene View自身を圧縮基準として探索するかどうかです。
falseでは選択したRadialCamera本体を圧縮基準にした形状を、このScene Viewから観察します。

```csharp
public bool ExploreFromSceneView { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_State_OmniViewState_FollowSourceCamera"></a> FollowSourceCamera

ONの間、毎フレームScene Viewの目の位置だけを設定元カメラの位置へ合わせ続けます
（Play中にカメラが動いても追従します）。向きと画角は変えません。

```csharp
public bool FollowSourceCamera { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 補足（Remarks）

向きを毎フレーム合わせると、XYZ視点ギズモや手動オービットで向きを変えても
1リペイントで戻されます（実機で確認済み）。位置だけを固定し、向きは
<xref href="Omni.Editor.State.OmniViewState.PendingRotationSync" data-throw-if-not-resolved="false"></xref>（「向きを合わせる」）で必要なときだけ合わせます。

### <a id="Omni_Editor_State_OmniViewState_GridScaleExponent"></a> GridScaleExponent

標準・対数Scene Viewで共有する基準格子の10進指数です。
Scene ViewごとにEditor起動中だけ保持します。

```csharp
public int GridScaleExponent { get; set; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_State_OmniViewState_GridShowPlaneXY"></a> GridShowPlaneXY

XY平面（Z軸色）の格子を描くかどうかです。

```csharp
public bool GridShowPlaneXY { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_State_OmniViewState_GridShowPlaneXZ"></a> GridShowPlaneXZ

XZ平面（Y軸色）の格子を描くかどうかです。

```csharp
public bool GridShowPlaneXZ { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_State_OmniViewState_GridShowPlaneYZ"></a> GridShowPlaneYZ

YZ平面（X軸色）の格子を描くかどうかです。

```csharp
public bool GridShowPlaneYZ { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_State_OmniViewState_GridXAxisColor"></a> GridXAxisColor

グリッド上でX方向に平行な線の色です。アルファ成分がそのまま不透明度です
（専用のStrengthは持たず、ColorFieldのアルファスライダーが唯一の正本です）。

```csharp
public Color GridXAxisColor { get; set; }
```

#### 値（Property Value）

 Color

### <a id="Omni_Editor_State_OmniViewState_GridYAxisColor"></a> GridYAxisColor

グリッド上でY方向に平行な線の色です。アルファ成分がそのまま不透明度です
（専用のStrengthは持たず、ColorFieldのアルファスライダーが唯一の正本です）。

```csharp
public Color GridYAxisColor { get; set; }
```

#### 値（Property Value）

 Color

### <a id="Omni_Editor_State_OmniViewState_GridZAxisColor"></a> GridZAxisColor

グリッド上でZ方向に平行な線の色です。アルファ成分がそのまま不透明度です
（専用のStrengthは持たず、ColorFieldのアルファスライダーが唯一の正本です）。

```csharp
public Color GridZAxisColor { get; set; }
```

#### 値（Property Value）

 Color

### <a id="Omni_Editor_State_OmniViewState_NearClip"></a> NearClip

このScene Viewだけの論理Nearです。描画proxyのNearとは独立です。

```csharp
public Scalar NearClip { get; set; }
```

#### 値（Property Value）

 Scalar

### <a id="Omni_Editor_State_OmniViewState_OrthoIdentityHalfHeightFraction"></a> OrthoIdentityHalfHeightFraction

恒等領域の半高（Hh）を、画面半高（<code>orthographicSize</code>）に対する比率で
表したものです。既定は0.5（画面中央50%）。四隅ドラッグ（ScaleView_Plan K節）で
上書きされます。

```csharp
public float OrthoIdentityHalfHeightFraction { get; set; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Editor_State_OmniViewState_OrthoIdentityHalfWidthFraction"></a> OrthoIdentityHalfWidthFraction

恒等領域の半幅（Hw）を、画面半幅（<code>orthographicSize * aspect</code>）に対する比率で
表したものです。既定は0.5（画面中央50%）。四隅ドラッグ（ScaleView_Plan K節）で
上書きされます。

```csharp
public float OrthoIdentityHalfWidthFraction { get; set; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Editor_State_OmniViewState_OrthoLogGridDataType"></a> OrthoLogGridDataType

対数グリッドの画面端が対応するデータ型です（<code>float</code>または<code>Logic</code>、
ScaleView_Plan Q節）。K節の各フラクションと同じ理由でSessionStateへ永続化します。

```csharp
public OrthoLogGridDataType OrthoLogGridDataType { get; set; }
```

#### 値（Property Value）

 [OrthoLogGridDataType](Omni.Editor.State.OrthoLogGridDataType.md)

### <a id="Omni_Editor_State_OmniViewState_OrthoLogGridEnabled"></a> OrthoLogGridEnabled

Orthographic Scene View専用の対数グリッド表示（画面中央50%が無歪みの矩形、
その外側を対数圧縮）を有効にするかどうかです。Perspective側では参照されません。

```csharp
public bool OrthoLogGridEnabled { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_State_OmniViewState_RadialDisplayMode"></a> RadialDisplayMode

Radial側（ワープ後）の比較表示方式です。

```csharp
public OmniMeshDisplayMode RadialDisplayMode { get; set; }
```

#### 値（Property Value）

 [OmniMeshDisplayMode](Omni.Editor.State.OmniMeshDisplayMode.md)

### <a id="Omni_Editor_State_OmniViewState_SceneViewMode"></a> SceneViewMode

旧Perspective UIとOrthographic経路の互換状態です。PerspectiveでOmni描画を
実際に有効にする条件は、Overlay表示中かつ有効な設定元RadialCameraがあることです。

```csharp
public SceneViewWarpMode SceneViewMode { get; set; }
```

#### 値（Property Value）

 [SceneViewWarpMode](Omni.Editor.State.SceneViewWarpMode.md)

### <a id="Omni_Editor_State_OmniViewState_ShowSafetyBoundaryFaces"></a> ShowSafetyBoundaryFaces

Scene Viewの有限な安全境界を半透明の面で表示するかどうかです。
通常編集ではシーンを覆わないよう既定OFFとし、境界線はこの設定に関係なく表示します。

```csharp
public bool ShowSafetyBoundaryFaces { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_State_OmniViewState_StandardDisplayMode"></a> StandardDisplayMode

Standard側（ワープ前）の比較表示方式です。

```csharp
public OmniMeshDisplayMode StandardDisplayMode { get; set; }
```

#### 値（Property Value）

 [OmniMeshDisplayMode](Omni.Editor.State.OmniMeshDisplayMode.md)

### <a id="Omni_Editor_State_OmniViewState_UseGameCameraAsWarpCenter"></a> UseGameCameraAsWarpCenter

互換用の旧プロパティです。trueは選択したRadialCamera本体を圧縮基準にする
（＝<xref href="Omni.Editor.State.OmniViewState.ExploreFromSceneView" data-throw-if-not-resolved="false"></xref>がfalse）ことを表します。

```csharp
public bool UseGameCameraAsWarpCenter { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_State_OmniViewState_WarpCameraOverride"></a> WarpCameraOverride

設定元として使うシーン内のRadialCameraを持つCameraを明示的に指定します。
<code>null</code>の場合はOmni描画を適用しません。明示的な設定は未選択を含めて
初期自動選択を完了させるため、後から別カメラへ勝手に切り替わりません。

```csharp
public Camera WarpCameraOverride { get; set; }
```

#### 値（Property Value）

 Camera

### <a id="Omni_Editor_State_OmniViewState_Changed"></a> Changed

状態が変更されたときに発生します。

```csharp
public event Action Changed
```

#### 型（Event Type）

 [Action](https://learn.microsoft.com/dotnet/api/system.action)
