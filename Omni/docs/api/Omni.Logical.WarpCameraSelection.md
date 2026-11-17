# <a id="Omni_Logical_WarpCameraSelection"></a> Class WarpCameraSelection

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Omni.Editor.dll  

```csharp
[MovedFrom(true, "Omni.Editor.SceneViewRadial", null, "LogicalWarpCameraSelection")]
public static class WarpCameraSelection
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[WarpCameraSelection](Omni.Logical.WarpCameraSelection.md)

## プロパティ（Properties）

### <a id="Omni_Logical_WarpCameraSelection_NoRadialCameraChoiceLabel"></a> NoRadialCameraChoiceLabel

ドロップダウンで設定元が未選択であることを表す表示名です。
ワープの有無自体はOmniオーバーレイの表示/非表示で決まります
（非表示＝Unity標準描画。<xref href="Omni.Editor.SceneViewRadial.RadialGlobalEditorDriver" data-throw-if-not-resolved="false"></xref>参照）。

```csharp
public static string NoRadialCameraChoiceLabel { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Logical_WarpCameraSelection_BuildChoices_System_Collections_Generic_List_System_String__System_Collections_Generic_List_UnityEngine_Camera__"></a> BuildChoices\(List<string\>, List<Camera\>\)

「基準カメラ」ドロップダウンの選択肢を組み立てます。

```csharp
public static void BuildChoices(List<string> choices, List<Camera> cameras)
```

#### 引数（Parameters）

`choices` [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

表示名の格納先。呼び出し時にクリアされます。

`cameras` [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<Camera\>

表示名と同じ並びのカメラ。先頭1つは未選択を表す<code>null</code>です。

### <a id="Omni_Logical_WarpCameraSelection_FindSelectedIndex_Omni_Editor_State_OmniViewState_System_Collections_Generic_List_UnityEngine_Camera__"></a> FindSelectedIndex\(OmniViewState, List<Camera\>\)

現在の選択に対応する、<xref href="Omni.Logical.WarpCameraSelection.BuildChoices(System.Collections.Generic.List%7bSystem.String%7d%2cSystem.Collections.Generic.List%7bUnityEngine.Camera%7d)" data-throw-if-not-resolved="false"></xref>が返した並びの中の添字を返します。

```csharp
public static int FindSelectedIndex(OmniViewState state, List<Camera> cameras)
```

#### 引数（Parameters）

`state` [OmniViewState](Omni.Editor.State.OmniViewState.md)

`cameras` [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<Camera\>

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_WarpCameraSelection_FindSelectedIndex_UnityEngine_Camera_System_Collections_Generic_List_UnityEngine_Camera__"></a> FindSelectedIndex\(Camera, List<Camera\>\)

<b>解決済みの</b>実効カメラに対応する、並びの中の添字を返します。

```csharp
public static int FindSelectedIndex(Camera resolved, List<Camera> cameras)
```

#### 引数（Parameters）

`resolved` Camera

`cameras` [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<Camera\>

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_WarpCameraSelection_IsSelectableWarpCamera_UnityEngine_Camera_"></a> IsSelectableWarpCamera\(Camera\)

このカメラを「基準カメラ」として選べるかを返します。

```csharp
public static bool IsSelectableWarpCamera(Camera camera)
```

#### 引数（Parameters）

`camera` Camera

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_WarpCameraSelection_Resolve_Omni_Editor_State_OmniViewState_"></a> Resolve\(OmniViewState\)

指定したScene Viewが設定元として選択した実カメラを返します。

```csharp
public static Camera Resolve(OmniViewState state)
```

#### 引数（Parameters）

`state` [OmniViewState](Omni.Editor.State.OmniViewState.md)

#### 戻り値（Returns）

 Camera

有効な設定元カメラ。未選択または失効時は<code>null</code>。

### <a id="Omni_Logical_WarpCameraSelection_ResolveEffectiveRadialCurve_Omni_Editor_State_OmniViewState_"></a> ResolveEffectiveRadialCurve\(OmniViewState\)

Scene Viewの実効Radialカーブを基準カメラと同じ設定で返します。

```csharp
public static RadialSettings ResolveEffectiveRadialCurve(OmniViewState state)
```

#### 引数（Parameters）

`state` [OmniViewState](Omni.Editor.State.OmniViewState.md)

#### 戻り値（Returns）

 RadialSettings

### <a id="Omni_Logical_WarpCameraSelection_ResolveRadialCamera_Omni_Editor_State_OmniViewState_"></a> ResolveRadialCamera\(OmniViewState\)

指定した Scene View の実効ワープ中心カメラに付いている<xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref>を返します。

```csharp
public static RadialCamera ResolveRadialCamera(OmniViewState state)
```

#### 引数（Parameters）

`state` [OmniViewState](Omni.Editor.State.OmniViewState.md)

#### 戻り値（Returns）

 RadialCamera

### <a id="Omni_Logical_WarpCameraSelection_ResolveSceneViewCurve_Omni_Editor_State_OmniViewState_"></a> ResolveSceneViewCurve\(OmniViewState\)

Scene View探索に使う設定を、選択したRadialCameraから毎回解決します。

<p>
実描画（RadialGlobalEditorDriver）・グリッド（旧OmniGridRenderer、削除済み）・
ステータス表示（OmniSceneOverlay）の3箇所がそれぞれ別にこの判定を持っていたため、
カーブが食い違っていました。自己中心モードのカーブ解決はこのメソッドだけに
限定してください。
</p>

```csharp
public static RadialSettings ResolveSceneViewCurve(OmniViewState state)
```

#### 引数（Parameters）

`state` [OmniViewState](Omni.Editor.State.OmniViewState.md)

#### 戻り値（Returns）

 RadialSettings

### <a id="Omni_Logical_WarpCameraSelection_TryResolveEffectiveRadialCenter_Omni_Editor_State_OmniViewState_UnityEditor_SceneView_Omni_Logical_SceneViewRenderContext__Omni_Logical_Position3__"></a> TryResolveEffectiveRadialCenter\(OmniViewState, SceneView, in SceneViewRenderContext, out Position3\)

Scene Viewが実際に使うRadial中心を解決します。
基準カメラ選択時はそのLogical位置を優先し、未装備時はUnityのfloat位置を
Logicalへ無損失で取り込みます。基準カメラ未選択時だけ凍結コンテキストを使います。

```csharp
public static bool TryResolveEffectiveRadialCenter(OmniViewState state, SceneView sceneView, in SceneViewRenderContext context, out Position3 center)
```

#### 引数（Parameters）

`state` [OmniViewState](Omni.Editor.State.OmniViewState.md)

`sceneView` SceneView

`context` SceneViewRenderContext

`center` Position3

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
