# <a id="Omni_Editor_Manager_OmniManagerWindow"></a> Class OmniManagerWindow

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

Omni プロジェクト全体を管理する統合 Editor ウィンドウです。

<p>
マテリアルの Radial 変換・シーン適用・復元・検証を一箇所で行えます。
従来の <code>Converter</code> メニュー群を統合した UI です。
</p>

```csharp
[InitializeOnLoad]
public sealed class OmniManagerWindow : EditorWindow
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
ScriptableObject ← 
EditorWindow ← 
[OmniManagerWindow](Omni.Editor.Manager.OmniManagerWindow.md)

## フィールド（Fields）

### <a id="Omni_Editor_Manager_OmniManagerWindow_GuideLogarithmicRendering"></a> GuideLogarithmicRendering

案内（<xref href="Omni.Editor.Manager.OmniManagerWindow.OpenAndHighlight(System.String)" data-throw-if-not-resolved="false"></xref>）が示す、対数レンダリングのラジオです。

```csharp
public const string GuideLogarithmicRendering = "logarithmic-rendering"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_OmniManagerWindow_GuideProjectLogarithmicRendering"></a> GuideProjectLogarithmicRendering

案内が示す、「プロジェクト全体」の対象範囲と「対数レンダリング」のラジオです。
対象範囲はプロジェクト全体に切り替わりますが、描画方式の切替は利用者が選ぶまで実行しません。

```csharp
public const string GuideProjectLogarithmicRendering = "project-logarithmic-rendering"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Editor_Manager_OmniManagerWindow_Open"></a> Open\(\)

Omni Overlayから統合管理ウィンドウを開きます。

```csharp
public static void Open()
```

### <a id="Omni_Editor_Manager_OmniManagerWindow_OpenAndHighlight_System_String_"></a> OpenAndHighlight\(string\)

統合管理ウィンドウを開き、操作する場所を枠と「ここを選択」で数秒間示します（チュートリアルの案内）。

```csharp
public static void OpenAndHighlight(string target)
```

#### 引数（Parameters）

`target` [string](https://learn.microsoft.com/dotnet/api/system.string)
