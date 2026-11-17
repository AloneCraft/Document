# <a id="Omni_Editor_Manager_IOmniManagerTab"></a> Interface IOmniManagerTab

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

Omni Manager のタブが実装すべきインターフェースです。
新規タブを追加するときはこれを実装し、<code>OmniManagerWindow.s_Tabs</code> に追加してください。

```csharp
public interface IOmniManagerTab
```

## プロパティ（Properties）

### <a id="Omni_Editor_Manager_IOmniManagerTab_DisplayName"></a> DisplayName

タブの表示名です。

```csharp
string DisplayName { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Editor_Manager_IOmniManagerTab_OnDisable"></a> OnDisable\(\)

タブが非選択になったときに呼ばれます。

```csharp
void OnDisable()
```

### <a id="Omni_Editor_Manager_IOmniManagerTab_OnEnable"></a> OnEnable\(\)

タブが選択されたときに呼ばれます。

```csharp
void OnEnable()
```

### <a id="Omni_Editor_Manager_IOmniManagerTab_OnGUI"></a> OnGUI\(\)

タブの内容を描画します。

```csharp
void OnGUI()
```

### <a id="Omni_Editor_Manager_IOmniManagerTab_Refresh"></a> Refresh\(\)

表示データを再読み込みします。

```csharp
void Refresh()
```

### <a id="Omni_Editor_Manager_IOmniManagerTab_SetHostWindow_UnityEditor_EditorWindow_"></a> SetHostWindow\(EditorWindow\)

ホストウィンドウを設定します。即時再描画用です。

```csharp
void SetHostWindow(EditorWindow window)
```

#### 引数（Parameters）

`window` EditorWindow
