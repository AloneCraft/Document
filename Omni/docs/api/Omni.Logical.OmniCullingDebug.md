# <a id="Omni_Logical_OmniCullingDebug"></a> Class OmniCullingDebug

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

```csharp
[MovedFrom(true, "Omni", null, "OmniCullingDebug")]
public static class OmniCullingDebug
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniCullingDebug](Omni.Logical.OmniCullingDebug.md)

## プロパティ（Properties）

### <a id="Omni_Logical_OmniCullingDebug_DisableCulling"></a> DisableCulling

旧設定との互換用の否定形プロパティです。新規コードとUIは
<xref href="Omni.Logical.OmniCullingDebug.UseCulling" data-throw-if-not-resolved="false"></xref>を使用してください。

```csharp
public static bool DisableCulling { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_OmniCullingDebug_LayerCount"></a> LayerCount

集計対象の層数です。

```csharp
public static int LayerCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_OmniCullingDebug_UseCulling"></a> UseCulling

Omni由来のカリングと非表示を使用するかどうかです。既定は<code>true</code>です。
<code>false</code>の間は全てfail-openへ倒して表示し、欠落がカリング由来かを診断できます。
有限描画プロキシだけは維持します（隠す仕組みではなく描く仕組みであり、
外すと巨大TransformがUnityネイティブへ直接渡ってInvalid worldAABBを踏むため）。

```csharp
public static bool UseCulling { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_Logical_OmniCullingDebug_BeginFrame"></a> BeginFrame\(\)

フレーム境界を検出し、蓄積中の集計を「直近フレーム」として確定します。
描画開始のたびに呼んでください。同一フレーム内の再呼び出しは何もしません。

```csharp
public static void BeginFrame()
```

### <a id="Omni_Logical_OmniCullingDebug_GetLastFrameCount_Omni_Logical_OmniHideLayer_"></a> GetLastFrameCount\(OmniHideLayer\)

直近に確定したフレームで、その層が非表示にした件数です。

```csharp
public static int GetLastFrameCount(OmniHideLayer layer)
```

#### 引数（Parameters）

`layer` [OmniHideLayer](Omni.Logical.OmniHideLayer.md)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_OmniCullingDebug_GetLayerDisplayName_Omni_Logical_OmniHideLayer_"></a> GetLayerDisplayName\(OmniHideLayer\)

層のローカライズ済み表示名です。

```csharp
public static string GetLayerDisplayName(OmniHideLayer layer)
```

#### 引数（Parameters）

`layer` [OmniHideLayer](Omni.Logical.OmniHideLayer.md)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Logical_OmniCullingDebug_NoteCullingMatrix_UnityEngine_Camera_UnityEngine_Matrix4x4__System_String_"></a> NoteCullingMatrix\(Camera, in Matrix4x4, string\)

そのフレームでカメラへ実際に適用したカリング行列と、その出所を記録します。
同一フレーム内で複数回適用された場合は<b>最後の適用</b>が残ります
（実際に描画へ効くのも最後の適用のため）。

```csharp
public static void NoteCullingMatrix(Camera camera, in Matrix4x4 matrix, string source)
```

#### 引数（Parameters）

`camera` Camera

`matrix` Matrix4x4

`source` [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Logical_OmniCullingDebug_NoteCullingRange_UnityEngine_Camera_System_Single_System_Single_System_Single_System_Single_System_Boolean_"></a> NoteCullingRange\(Camera, float, float, float, float, bool\)

第1層が実際に使ったカリング範囲を記録します。

```csharp
public static void NoteCullingRange(Camera camera, float renderNear, float renderFar, float cullNear, float cullFar, bool unmapFailed)
```

#### 引数（Parameters）

`camera` Camera

`renderNear` [float](https://learn.microsoft.com/dotnet/api/system.single)

`renderFar` [float](https://learn.microsoft.com/dotnet/api/system.single)

`cullNear` [float](https://learn.microsoft.com/dotnet/api/system.single)

`cullFar` [float](https://learn.microsoft.com/dotnet/api/system.single)

`unmapFailed` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_OmniCullingDebug_NoteEyeOverride_UnityEngine_Camera_System_Boolean_UnityEngine_Vector3_UnityEngine_Vector3_"></a> NoteEyeOverride\(Camera, bool, Vector3, Vector3\)

そのフレームにカメラの目をワープ中心基準へ上書きしたかどうかと、その判断材料を記録します。
上書きの適否を決めた直後に呼んでください。

```csharp
public static void NoteEyeOverride(Camera camera, bool applied, Vector3 warpCenter, Vector3 eyeRenderPosition)
```

#### 引数（Parameters）

`camera` Camera

`applied` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`warpCenter` Vector3

`eyeRenderPosition` Vector3

### <a id="Omni_Logical_OmniCullingDebug_NoteHidden_UnityEngine_Renderer_Omni_Logical_OmniHideLayer_"></a> NoteHidden\(Renderer, OmniHideLayer\)

ある層がRendererを非表示にしたことを記録します。
同一フレーム内で複数の層が同じRendererを消した場合は、最初の層だけを残します。

```csharp
public static void NoteHidden(Renderer renderer, OmniHideLayer layer)
```

#### 引数（Parameters）

`renderer` Renderer

`layer` [OmniHideLayer](Omni.Logical.OmniHideLayer.md)

### <a id="Omni_Logical_OmniCullingDebug_NoteNearClip_UnityEngine_Camera_System_Boolean_System_Boolean_System_Boolean_Omni_Logical_Scalar__System_Single_System_Single_System_Single_System_Single_"></a> NoteNearClip\(Camera, bool, bool, bool, in Scalar, float, float, float, float\)

そのフレームにカメラへ適用した論理 Near Clip の実値を記録します。
near を決めた直後に呼んでください。

```csharp
public static void NoteNearClip(Camera camera, bool resolved, bool hardwarePlaneMatches, bool orthographic, in Scalar logicalNear, float renderNear, float cameraNear, float cosMinAngle, float centerUnderClipRatio)
```

#### 引数（Parameters）

`camera` Camera

`resolved` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`hardwarePlaneMatches` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`orthographic` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`logicalNear` [Scalar](Omni.Logical.Scalar.md)

`renderNear` [float](https://learn.microsoft.com/dotnet/api/system.single)

`cameraNear` [float](https://learn.microsoft.com/dotnet/api/system.single)

`cosMinAngle` [float](https://learn.microsoft.com/dotnet/api/system.single)

`centerUnderClipRatio` [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Logical_OmniCullingDebug_NoteProjectionClip_UnityEngine_Camera_System_Single_System_Single_System_Single_System_Boolean_System_Boolean_System_Boolean_"></a> NoteProjectionClip\(Camera, float, float, float, bool, bool, bool\)

Far Clip拡張の判断値を、Camera状態を復元する前に記録します。

```csharp
public static void NoteProjectionClip(Camera camera, float neededFar, float inputFar, float appliedFar, bool includedRadialIdentityBounds, bool hadRadialIdentityBounds, bool overridden)
```

#### 引数（Parameters）

`camera` Camera

`neededFar` [float](https://learn.microsoft.com/dotnet/api/system.single)

`inputFar` [float](https://learn.microsoft.com/dotnet/api/system.single)

`appliedFar` [float](https://learn.microsoft.com/dotnet/api/system.single)

`includedRadialIdentityBounds` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`hadRadialIdentityBounds` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`overridden` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_OmniCullingDebug_NoteWarpMode_UnityEngine_Camera_System_Boolean_System_Boolean_System_Boolean_System_Boolean_"></a> NoteWarpMode\(Camera, bool, bool, bool, bool\)

そのフレームにカメラへ適用したワープ経路と、その判断材料を記録します。
恒等かどうかを決めた直後に呼んでください。

```csharp
public static void NoteWarpMode(Camera camera, bool identity, bool warpEnabled, bool hasDriver, bool orthographic)
```

#### 引数（Parameters）

`camera` Camera

`identity` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`warpEnabled` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`hasDriver` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`orthographic` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_OmniCullingDebug_ResetDefaults"></a> ResetDefaults\(\)

デバッグ上書きと集計を既定値へ戻します。

```csharp
public static void ResetDefaults()
```

### <a id="Omni_Logical_OmniCullingDebug_TryGetLastFrameCullingMatrix_UnityEngine_Camera_UnityEngine_Matrix4x4__System_String__"></a> TryGetLastFrameCullingMatrix\(Camera, out Matrix4x4, out string\)

直近に確定したフレームで、そのカメラへ適用したカリング行列を取得します。

```csharp
public static bool TryGetLastFrameCullingMatrix(Camera camera, out Matrix4x4 matrix, out string source)
```

#### 引数（Parameters）

`camera` Camera

`matrix` Matrix4x4

`source` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_OmniCullingDebug_TryGetLastFrameCullingRange_UnityEngine_Camera_Omni_Logical_OmniCullingRange__"></a> TryGetLastFrameCullingRange\(Camera, out OmniCullingRange\)

直近に確定したフレームで、そのカメラに使ったカリング範囲を取得します。

```csharp
public static bool TryGetLastFrameCullingRange(Camera camera, out OmniCullingRange range)
```

#### 引数（Parameters）

`camera` Camera

`range` [OmniCullingRange](Omni.Logical.OmniCullingRange.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_OmniCullingDebug_TryGetLastFrameEyeOverride_UnityEngine_Camera_Omni_Logical_OmniEyeOverride__"></a> TryGetLastFrameEyeOverride\(Camera, out OmniEyeOverride\)

直近に確定したフレームで、そのカメラの目の上書き状況を取得します。

```csharp
public static bool TryGetLastFrameEyeOverride(Camera camera, out OmniEyeOverride value)
```

#### 引数（Parameters）

`camera` Camera

`value` [OmniEyeOverride](Omni.Logical.OmniEyeOverride.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_OmniCullingDebug_TryGetLastFrameLayer_UnityEngine_Renderer_Omni_Logical_OmniHideLayer__"></a> TryGetLastFrameLayer\(Renderer, out OmniHideLayer\)

直近に確定したフレームで、そのRendererを消した層を取得します。

```csharp
public static bool TryGetLastFrameLayer(Renderer renderer, out OmniHideLayer layer)
```

#### 引数（Parameters）

`renderer` Renderer

`layer` [OmniHideLayer](Omni.Logical.OmniHideLayer.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_OmniCullingDebug_TryGetLastFrameNearClip_UnityEngine_Camera_Omni_Logical_OmniNearClip__"></a> TryGetLastFrameNearClip\(Camera, out OmniNearClip\)

直近に確定したフレームで、そのカメラへ適用した論理 Near Clip を取得します。

```csharp
public static bool TryGetLastFrameNearClip(Camera camera, out OmniNearClip value)
```

#### 引数（Parameters）

`camera` Camera

`value` [OmniNearClip](Omni.Logical.OmniNearClip.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_OmniCullingDebug_TryGetLastFrameProjectionClip_UnityEngine_Camera_Omni_Logical_OmniProjectionClip__"></a> TryGetLastFrameProjectionClip\(Camera, out OmniProjectionClip\)

```csharp
public static bool TryGetLastFrameProjectionClip(Camera camera, out OmniProjectionClip value)
```

#### 引数（Parameters）

`camera` Camera

`value` [OmniProjectionClip](Omni.Logical.OmniProjectionClip.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_OmniCullingDebug_TryGetLastFrameWarpMode_UnityEngine_Camera_Omni_Logical_OmniWarpMode__"></a> TryGetLastFrameWarpMode\(Camera, out OmniWarpMode\)

直近に確定したフレームで、そのカメラへ適用したワープ経路を取得します。

```csharp
public static bool TryGetLastFrameWarpMode(Camera camera, out OmniWarpMode mode)
```

#### 引数（Parameters）

`camera` Camera

`mode` [OmniWarpMode](Omni.Logical.OmniWarpMode.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
