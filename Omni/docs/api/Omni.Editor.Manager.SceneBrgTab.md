# <a id="Omni_Editor_Manager_SceneBrgTab"></a> Class SceneBrgTab

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

ロード済みSceneのScene BRG sidecar準備状態を表示し、利用者が再確認・再生成を
要求するタブです。生成は <xref href="Omni.Editor.BatchRendering.RadialSceneBrgEditorIntegration" data-throw-if-not-resolved="false"></xref> が次の安全な
Editor更新で行い、このタブのOnGUIは結果を読むだけです。

```csharp
public sealed class SceneBrgTab : IOmniManagerTab
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[SceneBrgTab](Omni.Editor.Manager.SceneBrgTab.md)

#### 実装するインターフェース（Implements）

[IOmniManagerTab](Omni.Editor.Manager.IOmniManagerTab.md)

## プロパティ（Properties）

### <a id="Omni_Editor_Manager_SceneBrgTab_DisplayName"></a> DisplayName

タブの表示名です。

```csharp
public string DisplayName { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Editor_Manager_SceneBrgTab_OnDisable"></a> OnDisable\(\)

タブが非選択になったときに呼ばれます。

```csharp
public void OnDisable()
```

### <a id="Omni_Editor_Manager_SceneBrgTab_OnEnable"></a> OnEnable\(\)

タブが選択されたときに呼ばれます。

```csharp
public void OnEnable()
```

### <a id="Omni_Editor_Manager_SceneBrgTab_OnGUI"></a> OnGUI\(\)

タブの内容を描画します。

```csharp
public void OnGUI()
```

### <a id="Omni_Editor_Manager_SceneBrgTab_Refresh"></a> Refresh\(\)

表示データを再読み込みします。

```csharp
public void Refresh()
```

### <a id="Omni_Editor_Manager_SceneBrgTab_SetHostWindow_UnityEditor_EditorWindow_"></a> SetHostWindow\(EditorWindow\)

ホストウィンドウを設定します。即時再描画用です。

```csharp
public void SetHostWindow(EditorWindow window)
```

#### 引数（Parameters）

`window` EditorWindow
