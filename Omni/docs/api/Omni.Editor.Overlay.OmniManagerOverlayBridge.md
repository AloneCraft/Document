# <a id="Omni_Editor_Overlay_OmniManagerOverlayBridge"></a> Class OmniManagerOverlayBridge

Namespace: [Omni.Editor.Overlay](Omni.Editor.Overlay.md)  
Assembly: Omni.Editor.dll  

Scene View の Omni Navigator と Omni Manager ウィンドウの表示状態を仲介します。
アセンブリ循環を避けるため、Manager はウィンドウを登録し、Navigator はこの橋渡しを呼び出します。

```csharp
public static class OmniManagerOverlayBridge
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniManagerOverlayBridge](Omni.Editor.Overlay.OmniManagerOverlayBridge.md)

## フィールド（Fields）

### <a id="Omni_Editor_Overlay_OmniManagerOverlayBridge_GuideLogarithmicRendering"></a> GuideLogarithmicRendering

案内で示す、Omni Managerの「対数レンダリング」ラジオの識別子です。

```csharp
public const string GuideLogarithmicRendering = "logarithmic-rendering"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Overlay_OmniManagerOverlayBridge_GuideProjectLogarithmicRendering"></a> GuideProjectLogarithmicRendering

案内で示す、「プロジェクト全体」の対象範囲と「対数レンダリング」のラジオの識別子です。
案内を受けたManagerは対象範囲をプロジェクト全体にして、両方を枠で示します。

```csharp
public const string GuideProjectLogarithmicRendering = "project-logarithmic-rendering"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## プロパティ（Properties）

### <a id="Omni_Editor_Overlay_OmniManagerOverlayBridge_IsVisible"></a> IsVisible

Omni Manager が少なくとも1つ表示されているかを返します。

```csharp
public static bool IsVisible { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_Editor_Overlay_OmniManagerOverlayBridge_OpenGuide_System_String_"></a> OpenGuide\(string\)

Omni Managerを開き、<code class="paramref">target</code>の操作を点滅枠と「ここを選択」で示します。
案内処理が未登録ならManagerを開くだけにします。

```csharp
public static void OpenGuide(string target)
```

#### 引数（Parameters）

`target` [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Overlay_OmniManagerOverlayBridge_Register_UnityEditor_EditorWindow_"></a> Register\(EditorWindow\)

Omni Manager ウィンドウを表示状態の追跡対象へ登録します。
Omni Manager の OnEnable から呼び出します。

```csharp
public static void Register(EditorWindow window)
```

#### 引数（Parameters）

`window` EditorWindow

登録する Omni Manager の EditorWindow。null は無視します。

### <a id="Omni_Editor_Overlay_OmniManagerOverlayBridge_RegisterGuideHandler_System_Action_System_String__"></a> RegisterGuideHandler\(Action<string\>\)

Omni Managerを開いて操作する場所を枠で示す処理を登録します（Managerアセンブリから呼びます）。

```csharp
public static void RegisterGuideHandler(Action<string> guideHandler)
```

#### 引数（Parameters）

`guideHandler` [Action](https://learn.microsoft.com/dotnet/api/system.action\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Editor_Overlay_OmniManagerOverlayBridge_SetVisible_System_Boolean_"></a> SetVisible\(bool\)

Navigator の Manager トグルから表示・非表示を切り替えます。
表示時はManagerアセンブリが登録した処理を実行し、非表示時は追跡中の窓を閉じます。

```csharp
public static void SetVisible(bool visible)
```

#### 引数（Parameters）

`visible` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

表示する場合は true、閉じる場合は false。

### <a id="Omni_Editor_Overlay_OmniManagerOverlayBridge_Unregister_UnityEditor_EditorWindow_"></a> Unregister\(EditorWindow\)

Omni Manager ウィンドウを表示状態の追跡対象から解除します。
Omni Manager の OnDisable から呼び出します。

```csharp
public static void Unregister(EditorWindow window)
```

#### 引数（Parameters）

`window` EditorWindow

解除する Omni Manager の EditorWindow。null は無視します。

### <a id="Omni_Editor_Overlay_OmniManagerOverlayBridge_VisibilityChanged"></a> VisibilityChanged

Manager の表示状態が変化したときに通知します。

```csharp
public static event Action<bool> VisibilityChanged
```

#### 型（Event Type）

 [Action](https://learn.microsoft.com/dotnet/api/system.action\-1)<[bool](https://learn.microsoft.com/dotnet/api/system.boolean)\>
