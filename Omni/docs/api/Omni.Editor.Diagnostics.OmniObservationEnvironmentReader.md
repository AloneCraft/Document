# <a id="Omni_Editor_Diagnostics_OmniObservationEnvironmentReader"></a> Class OmniObservationEnvironmentReader

Namespace: [Omni.Editor.Diagnostics](Omni.Editor.Diagnostics.md)  
Assembly: Omni.Editor.dll  

実 Editor から <xref href="Omni.Editor.Diagnostics.OmniObservationEnvironment" data-throw-if-not-resolved="false"></xref> を読む薄いアダプターです。
呼ばれた時点の値を読むだけで、購読・毎フレーム処理・Repaint の要求はしません。

```csharp
public static class OmniObservationEnvironmentReader
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniObservationEnvironmentReader](Omni.Editor.Diagnostics.OmniObservationEnvironmentReader.md)

## フィールド（Fields）

### <a id="Omni_Editor_Diagnostics_OmniObservationEnvironmentReader_UntitledScenePath"></a> UntitledScenePath

無題の Scene を表す path です。

```csharp
public const string UntitledScenePath = "<untitled>"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Editor_Diagnostics_OmniObservationEnvironmentReader_Capture_UnityEditor_SceneView_System_Boolean_"></a> Capture\(SceneView, bool\)

呼ばれた時点の Editor を読みます。<code class="paramref">includeOcclusion</code> が true のときだけ、
Omni Overlay と Scene View に重なる浮いたウィンドウを読みます（EditorWindow の列挙を伴うため）。

```csharp
public static OmniObservationEnvironment Capture(SceneView sceneView, bool includeOcclusion)
```

#### 引数（Parameters）

`sceneView` SceneView

遮蔽と Scene View の有無を読む対象です。null を許します。

`includeOcclusion` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

遮蔽を読む場合は true です。

#### 戻り値（Returns）

 [OmniObservationEnvironment](Omni.Editor.Diagnostics.OmniObservationEnvironment.md)

### <a id="Omni_Editor_Diagnostics_OmniObservationEnvironmentReader_SampleWindow_UnityEngine_Camera_System_Int64_"></a> SampleWindow\(Camera, long\)

観測窓の端点を読みます。<code class="paramref">brgCamera</code> が null なら BRG は読みません。

```csharp
public static OmniObservationWindowSample SampleWindow(Camera brgCamera, long observedFrames)
```

#### 引数（Parameters）

`brgCamera` Camera

BRG の culling 順番を読む Camera です。

`observedFrames` [long](https://learn.microsoft.com/dotnet/api/system.int64)

呼び出し側が数えた描画回数です。

#### 戻り値（Returns）

 [OmniObservationWindowSample](Omni.Editor.Diagnostics.OmniObservationWindowSample.md)
