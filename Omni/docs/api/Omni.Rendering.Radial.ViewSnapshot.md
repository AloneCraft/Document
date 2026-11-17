# <a id="Omni_Rendering_Radial_ViewSnapshot"></a> Struct ViewSnapshot

Namespace: [Omni.Rendering.Radial](Omni.Rendering.Radial.md)  
Assembly: Radial.Runtime.dll  

1回のカメラ描画に対応する不変Radialビュー状態です。
BRGは<xref href="Omni.RadialViewRegistry" data-throw-if-not-resolved="false"></xref>からこの値を取得し、Shader.SetGlobal*を
正本として参照しません。SaturnシーンのMesoリングBRG描画で使用します。

```csharp
public readonly struct ViewSnapshot
```

## コンストラクター（Constructors）

### <a id="Omni_Rendering_Radial_ViewSnapshot__ctor_UnityEngine_EntityId_UnityEngine_EntityId_Omni_Rendering_Radial_ViewKind_Omni_Logical_Position3__Omni_Rendering_Radial_Frustum__Omni_Logical_Scalar__Omni_Logical_Scalar__System_Single_System_Single_Omni_RadialSettings__Omni_Rendering_Radial_GpuFrame__System_Boolean_System_Boolean_System_Boolean_"></a> ViewSnapshot\(EntityId, EntityId, ViewKind, in Position3, in Frustum, in Scalar, in Scalar, float, float, in RadialSettings, in GpuFrame, bool, bool, bool\)

Radialビュー状態の草案を構築します。revisionとUnityフレーム番号は
<xref href="Omni.RadialViewRegistry.Publish(UnityEngine.Camera%2cUnityEngine.EntityId%2cOmni.Rendering.Radial.ViewSnapshot%40%2cOmni.Rendering.Radial.ViewSnapshot%40)" data-throw-if-not-resolved="false"></xref>
が採番します。

```csharp
public ViewSnapshot(EntityId cameraInstanceId, EntityId viewId, ViewKind viewKind, in Position3 warpCenter, in Frustum logicalFrustum, in Scalar logicalNearClip, in Scalar logicalFarClip, float renderNearClip, float renderFarClip, in RadialSettings settings, in GpuFrame gpuFrame, bool isRadialActive, bool isEyeAtWarpCenter, bool isFailOpen)
```

#### 引数（Parameters）

`cameraInstanceId` EntityId

`viewId` EntityId

`viewKind` [ViewKind](Omni.Rendering.Radial.ViewKind.md)

`warpCenter` [Position3](Omni.Logical.Position3.md)

`logicalFrustum` [Frustum](Omni.Rendering.Radial.Frustum.md)

`logicalNearClip` [Scalar](Omni.Logical.Scalar.md)

`logicalFarClip` [Scalar](Omni.Logical.Scalar.md)

`renderNearClip` [float](https://learn.microsoft.com/dotnet/api/system.single)

`renderFarClip` [float](https://learn.microsoft.com/dotnet/api/system.single)

`settings` [RadialSettings](Omni.RadialSettings.md)

`gpuFrame` [GpuFrame](Omni.Rendering.Radial.GpuFrame.md)

`isRadialActive` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`isEyeAtWarpCenter` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`isFailOpen` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## フィールド（Fields）

### <a id="Omni_Rendering_Radial_ViewSnapshot_CameraInstanceId"></a> CameraInstanceId

Unity 6.5のCamera.GetEntityId()です。旧GetInstanceIDは使いません。

```csharp
public readonly EntityId CameraInstanceId
```

#### 値（Field Value）

 EntityId

### <a id="Omni_Rendering_Radial_ViewSnapshot_FarClip"></a> FarClip

論理Far Clipです。

```csharp
public readonly Scalar FarClip
```

#### 値（Field Value）

 [Scalar](Omni.Logical.Scalar.md)

### <a id="Omni_Rendering_Radial_ViewSnapshot_FrameRevision"></a> FrameRevision

Registryが発行する単調増加の描画revisionです。

```csharp
public readonly ulong FrameRevision
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Rendering_Radial_ViewSnapshot_Frustum"></a> Frustum

BRGのCPUカリングに渡す論理錐台です。

```csharp
public readonly Frustum Frustum
```

#### 値（Field Value）

 [Frustum](Omni.Rendering.Radial.Frustum.md)

### <a id="Omni_Rendering_Radial_ViewSnapshot_GpuFrame"></a> GpuFrame

BRG専用シェーダーへ渡すカメラ相対GPU frameです。

```csharp
public readonly GpuFrame GpuFrame
```

#### 値（Field Value）

 [GpuFrame](Omni.Rendering.Radial.GpuFrame.md)

### <a id="Omni_Rendering_Radial_ViewSnapshot_IsEyeAtWarpCenter"></a> IsEyeAtWarpCenter

描画cameraとRadialワープ中心が同じ意味上のeyeかどうかです。
浮動小数点位置の比較ではなく、Radial sourceの自己中心・所有関係から公開されます。

```csharp
public readonly bool IsEyeAtWarpCenter
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Rendering_Radial_ViewSnapshot_IsFailOpen"></a> IsFailOpen

カリング不能時に全表示へ倒す必要があるかどうかです。

```csharp
public readonly bool IsFailOpen
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Rendering_Radial_ViewSnapshot_IsRadialActive"></a> IsRadialActive

このカメラでRadialワープが有効かどうかです。

```csharp
public readonly bool IsRadialActive
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Rendering_Radial_ViewSnapshot_NearClip"></a> NearClip

論理Near Clipです。CPU除外へ使う場合は、<xref href="Omni.Logical.NearClipMath" data-throw-if-not-resolved="false"></xref>で
下方向へ保守化済みの値です。

```csharp
public readonly Scalar NearClip
```

#### 値（Field Value）

 [Scalar](Omni.Logical.Scalar.md)

### <a id="Omni_Rendering_Radial_ViewSnapshot_RenderFarClip"></a> RenderFarClip

Unity描画空間のFar Clipです。

```csharp
public readonly float RenderFarClip
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Rendering_Radial_ViewSnapshot_RenderNearClip"></a> RenderNearClip

Unity描画空間のNear Clipです。

```csharp
public readonly float RenderNearClip
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Rendering_Radial_ViewSnapshot_Settings"></a> Settings

CPU側のRadial写像設定です。

```csharp
public readonly RadialSettings Settings
```

#### 値（Field Value）

 [RadialSettings](Omni.RadialSettings.md)

### <a id="Omni_Rendering_Radial_ViewSnapshot_UnityFrameIndex"></a> UnityFrameIndex

このSnapshotを公開したUnityフレーム番号です。

```csharp
public readonly int UnityFrameIndex
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Rendering_Radial_ViewSnapshot_ViewId"></a> ViewId

Unity 6000のBatchCullingContext.viewIDと対応するEntityIdです。

```csharp
public readonly EntityId ViewId
```

#### 値（Field Value）

 EntityId

### <a id="Omni_Rendering_Radial_ViewSnapshot_ViewKey"></a> ViewKey

EntityId.ToULongで正規化したBRG用ビューキーです。

```csharp
public readonly ulong ViewKey
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Rendering_Radial_ViewSnapshot_ViewKind"></a> ViewKind

このビューの種別です。

```csharp
public readonly ViewKind ViewKind
```

#### 値（Field Value）

 [ViewKind](Omni.Rendering.Radial.ViewKind.md)

### <a id="Omni_Rendering_Radial_ViewSnapshot_WarpCenter"></a> WarpCenter

Logical座標上のRadialワープ中心です。

```csharp
public readonly Position3 WarpCenter
```

#### 値（Field Value）

 [Position3](Omni.Logical.Position3.md)

## プロパティ（Properties）

### <a id="Omni_Rendering_Radial_ViewSnapshot_CanUseConeCulling"></a> CanUseConeCulling

通常の論理視錐台のside planeを使えるかを返します。
Radial activeかつObserverの場合はワープ後の可視領域が通常錐台と一致しないためfalseです。
Near/farの除外には、別途<xref href="Omni.RadialShellPolicy" data-throw-if-not-resolved="false"></xref>の保守的な関係値を使います。

```csharp
public bool CanUseConeCulling { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Rendering_Radial_ViewSnapshot_CanUseShellCulling"></a> CanUseShellCulling

Radialシェルの厳密除外を許可できるかを返します。
Observerの非線形な逆写像領域では、eye距離だけで可視性を証明できないためfalseです。

```csharp
public bool CanUseShellCulling { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Rendering_Radial_ViewSnapshot_Eye"></a> Eye

Logical座標上の描画カメラeyeです。
<xref href="Omni.Rendering.Radial.ViewSnapshot.WarpCenter" data-throw-if-not-resolved="false"></xref>とは別のカメラ固有値であり、Observerではこの値を
論理距離・錐台の基準として使います。

```csharp
public Position3 Eye { get; }
```

#### 値（Property Value）

 [Position3](Omni.Logical.Position3.md)

### <a id="Omni_Rendering_Radial_ViewSnapshot_IsBatchCameraView"></a> IsBatchCameraView

Saturn v1のBRGが描画を許可する通常カメラかどうかです。

```csharp
public bool IsBatchCameraView { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Rendering_Radial_ViewSnapshot_IsCullingDataUsable"></a> IsCullingDataUsable

正確なカリングに必要な全入力が利用可能かどうかです。

```csharp
public bool IsCullingDataUsable { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_Rendering_Radial_ViewSnapshot_Matches_UnityEngine_EntityId_System_UInt64_"></a> Matches\(EntityId, ulong\)

viewIDと描画revisionがこのSnapshotに一致するかを返します。

```csharp
public bool Matches(EntityId viewId, ulong frameRevision)
```

#### 引数（Parameters）

`viewId` EntityId

`frameRevision` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
