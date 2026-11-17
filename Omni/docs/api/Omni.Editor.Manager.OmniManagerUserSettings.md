# <a id="Omni_Editor_Manager_OmniManagerUserSettings"></a> Class OmniManagerUserSettings

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

Omni Manager のユーザー個別設定です。EditorPrefs に保存されます。

```csharp
public static class OmniManagerUserSettings
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniManagerUserSettings](Omni.Editor.Manager.OmniManagerUserSettings.md)

## プロパティ（Properties）

### <a id="Omni_Editor_Manager_OmniManagerUserSettings_AutoRefresh"></a> AutoRefresh

```csharp
public static bool AutoRefresh { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_OmniManagerUserSettings_ExperimentalDeferredConversion"></a> ExperimentalDeferredConversion

実験的機能: Deferred 専用の URP 自作 Shader に UniversalForward Pass を足す経路（振り分け I）を、AI への依頼に含めるか。
既定は無効で、利用者ごとの設定（EditorPrefs。他のプロジェクトにも効く）です。無効の間、プロンプトにも結果 JSON の検査にも I は現れません。

```csharp
public static bool ExperimentalDeferredConversion { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_OmniManagerUserSettings_RefreshInterval"></a> RefreshInterval

```csharp
public static float RefreshInterval { get; set; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Editor_Manager_OmniManagerUserSettings_ShowConfirmDialogs"></a> ShowConfirmDialogs

```csharp
public static bool ShowConfirmDialogs { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
