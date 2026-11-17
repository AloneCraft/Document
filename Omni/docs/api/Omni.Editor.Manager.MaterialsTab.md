# <a id="Omni_Editor_Manager_MaterialsTab"></a> Class MaterialsTab

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

Materialタブは切替対象の診断と対応関係を表示します。
生成・適用・復元は上部の標準／対数統合切替だけが行います。

```csharp
public sealed class MaterialsTab : IOmniManagerTab
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[MaterialsTab](Omni.Editor.Manager.MaterialsTab.md)

#### 実装するインターフェース（Implements）

[IOmniManagerTab](Omni.Editor.Manager.IOmniManagerTab.md)

## プロパティ（Properties）

### <a id="Omni_Editor_Manager_MaterialsTab_DisplayName"></a> DisplayName

タブの表示名です。

```csharp
public string DisplayName { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Editor_Manager_MaterialsTab_OnDisable"></a> OnDisable\(\)

タブが非選択になったときに呼ばれます。

```csharp
public void OnDisable()
```

### <a id="Omni_Editor_Manager_MaterialsTab_OnEnable"></a> OnEnable\(\)

タブが選択されたときに呼ばれます。

```csharp
public void OnEnable()
```

### <a id="Omni_Editor_Manager_MaterialsTab_OnGUI"></a> OnGUI\(\)

タブの内容を描画します。

```csharp
public void OnGUI()
```

### <a id="Omni_Editor_Manager_MaterialsTab_Refresh"></a> Refresh\(\)

表示データを再読み込みします。

```csharp
public void Refresh()
```

### <a id="Omni_Editor_Manager_MaterialsTab_SetHostWindow_UnityEditor_EditorWindow_"></a> SetHostWindow\(EditorWindow\)

ホストウィンドウを設定します。即時再描画用です。

```csharp
public void SetHostWindow(EditorWindow window)
```

#### 引数（Parameters）

`window` EditorWindow
