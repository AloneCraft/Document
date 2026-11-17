# <a id="Omni_Editor_Manager_BakeTab"></a> Class BakeTab

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

Radial ベイク（<xref href="Omni.Editor.Manager.RadialBaker" data-throw-if-not-resolved="false"></xref>）を実行し、現在のシーンのベイク状態を表示するタブです。

```csharp
public sealed class BakeTab : IOmniManagerTab
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[BakeTab](Omni.Editor.Manager.BakeTab.md)

#### 実装するインターフェース（Implements）

[IOmniManagerTab](Omni.Editor.Manager.IOmniManagerTab.md)

## プロパティ（Properties）

### <a id="Omni_Editor_Manager_BakeTab_DisplayName"></a> DisplayName

タブの表示名です。

```csharp
public string DisplayName { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Editor_Manager_BakeTab_OnDisable"></a> OnDisable\(\)

タブが非選択になったときに呼ばれます。

```csharp
public void OnDisable()
```

### <a id="Omni_Editor_Manager_BakeTab_OnEnable"></a> OnEnable\(\)

タブが選択されたときに呼ばれます。

```csharp
public void OnEnable()
```

### <a id="Omni_Editor_Manager_BakeTab_OnGUI"></a> OnGUI\(\)

タブの内容を描画します。

```csharp
public void OnGUI()
```

### <a id="Omni_Editor_Manager_BakeTab_Refresh"></a> Refresh\(\)

表示データを再読み込みします。

```csharp
public void Refresh()
```

### <a id="Omni_Editor_Manager_BakeTab_SetHostWindow_UnityEditor_EditorWindow_"></a> SetHostWindow\(EditorWindow\)

ホストウィンドウを設定します。即時再描画用です。

```csharp
public void SetHostWindow(EditorWindow window)
```

#### 引数（Parameters）

`window` EditorWindow
