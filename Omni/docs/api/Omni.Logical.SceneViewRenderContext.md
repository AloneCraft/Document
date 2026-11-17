# <a id="Omni_Logical_SceneViewRenderContext"></a> Struct SceneViewRenderContext

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

1台のScene Viewが描画中に使う仮想論理視点です。
Editor側がカメラ単位で供給し、Runtimeの描画処理はLogicalPivotを正本として
オブジェクト相対座標を作ります。

```csharp
public readonly struct SceneViewRenderContext
```

## コンストラクター（Constructors）

### <a id="Omni_Logical_SceneViewRenderContext__ctor_Omni_Logical_Position3__UnityEngine_Vector3_System_Boolean_"></a> SceneViewRenderContext\(in Position3, Vector3, bool\)

Scene Viewの仮想論理視点を構築します。

```csharp
public SceneViewRenderContext(in Position3 logicalPivot, Vector3 physicalPivot, bool isComparisonMode)
```

#### 引数（Parameters）

`logicalPivot` [Position3](Omni.Logical.Position3.md)

`physicalPivot` Vector3

`isComparisonMode` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_SceneViewRenderContext__ctor_Omni_Logical_Position3__UnityEngine_Vector3_System_Boolean_System_Boolean_"></a> SceneViewRenderContext\(in Position3, Vector3, bool, bool\)

Scene Viewの仮想論理視点と、カメラ単位の比較対象抑止を構築します。

```csharp
public SceneViewRenderContext(in Position3 logicalPivot, Vector3 physicalPivot, bool isComparisonMode, bool suppressRadialComparisonTargets)
```

#### 引数（Parameters）

`logicalPivot` [Position3](Omni.Logical.Position3.md)

`physicalPivot` Vector3

`isComparisonMode` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`suppressRadialComparisonTargets` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_SceneViewRenderContext__ctor_Omni_Logical_Position3__UnityEngine_Vector3_System_Boolean_Omni_Logical_Position3__"></a> SceneViewRenderContext\(in Position3, Vector3, bool, in Position3\)

Editorが相対基準から求めた論理Eyeを描画時点で凍結します。

```csharp
public SceneViewRenderContext(in Position3 logicalPivot, Vector3 physicalPivot, bool isComparisonMode, in Position3 logicalCameraPosition)
```

#### 引数（Parameters）

`logicalPivot` [Position3](Omni.Logical.Position3.md)

`physicalPivot` Vector3

`isComparisonMode` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`logicalCameraPosition` [Position3](Omni.Logical.Position3.md)

### <a id="Omni_Logical_SceneViewRenderContext__ctor_Omni_Logical_Position3__UnityEngine_Vector3_System_Boolean_Omni_Logical_Position3__System_Boolean_"></a> SceneViewRenderContext\(in Position3, Vector3, bool, in Position3, bool\)

Editorが相対基準から求めた論理Eyeと、カメラ単位の比較対象抑止を凍結します。

```csharp
public SceneViewRenderContext(in Position3 logicalPivot, Vector3 physicalPivot, bool isComparisonMode, in Position3 logicalCameraPosition, bool suppressRadialComparisonTargets)
```

#### 引数（Parameters）

`logicalPivot` [Position3](Omni.Logical.Position3.md)

`physicalPivot` Vector3

`isComparisonMode` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`logicalCameraPosition` [Position3](Omni.Logical.Position3.md)

`suppressRadialComparisonTargets` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## フィールド（Fields）

### <a id="Omni_Logical_SceneViewRenderContext_IsActive"></a> IsActive

仮想論理視点が有効かどうかです。

```csharp
public readonly bool IsActive
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_SceneViewRenderContext_IsComparisonMode"></a> IsComparisonMode

比較モード中かどうかです。

```csharp
public readonly bool IsComparisonMode
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_SceneViewRenderContext_None"></a> None

無効なコンテキストです。

```csharp
public static readonly SceneViewRenderContext None
```

#### 値（Field Value）

 [SceneViewRenderContext](Omni.Logical.SceneViewRenderContext.md)

### <a id="Omni_Logical_SceneViewRenderContext_PhysicalPivot"></a> PhysicalPivot

描画用の物理ピボットです。現行のUnity Scene Viewとの互換用に保持します。

```csharp
public readonly Vector3 PhysicalPivot
```

#### 値（Field Value）

 Vector3

### <a id="Omni_Logical_SceneViewRenderContext_Pivot"></a> Pivot

Scene Viewピボットの固定小数点論理位置です。

```csharp
public readonly Position3 Pivot
```

#### 値（Field Value）

 [Position3](Omni.Logical.Position3.md)

### <a id="Omni_Logical_SceneViewRenderContext_SuppressRadialComparisonTargets"></a> SuppressRadialComparisonTargets

このScene ViewカメラではRadial比較対象を描画・Picking・影から除外するかどうかです。

```csharp
public readonly bool SuppressRadialComparisonTargets
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_Logical_SceneViewRenderContext_TryGetCameraPosition_UnityEngine_Transform_Omni_Logical_Position3__"></a> TryGetCameraPosition\(Transform, out Position3\)

カメラ位置をScene Viewピボットの論理位置へ加えた、実際の仮想論理視点を返します。

```csharp
public bool TryGetCameraPosition(Transform cameraTransform, out Position3 logicalCameraPosition)
```

#### 引数（Parameters）

`cameraTransform` Transform

`logicalCameraPosition` [Position3](Omni.Logical.Position3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_SceneViewRenderContext_TryGetObjectRelativeHiLo_UnityEngine_Transform_UnityEngine_Vector3__UnityEngine_Vector3__System_Boolean__"></a> TryGetObjectRelativeHiLo\(Transform, out Vector3, out Vector3, out bool\)

指定Transformの原点を、仮想論理ピボットからのHi/Lo相対座標へ変換します。

```csharp
public bool TryGetObjectRelativeHiLo(Transform target, out Vector3 relativeHi, out Vector3 relativeLo, out bool precisionGuaranteed)
```

#### 引数（Parameters）

`target` Transform

描画対象Transform。nullなら失敗します。

`relativeHi` Vector3

float化した相対座標の上位値です。

`relativeLo` Vector3

上位値からこぼれた残差です。

`precisionGuaranteed` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

論理位置プロバイダーを使えた場合はtrueです。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

有限な相対座標を構築できた場合はtrueです。
