# <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStatusText"></a> Class OmniAiConversionStatusText

Namespace: [Omni.Editor.Manager.AiConversion](Omni.Editor.Manager.AiConversion.md)  
Assembly: Omni.Manager.dll  

状態の表示（見出し・アイコン名・ツールチップ）です。アイコンは Unity 組込み（<code>EditorGUIUtility.IconContent</code> の名前）で、
色は呼び出し側が <xref href="Omni.Editor.Manager.AiConversion.OmniAiConversionIconColor" data-throw-if-not-resolved="false"></xref> から決めます。

```csharp
public static class OmniAiConversionStatusText
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniAiConversionStatusText](Omni.Editor.Manager.AiConversion.OmniAiConversionStatusText.md)

## メソッド（Methods）

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStatusText_ColorOf_Omni_Editor_Manager_AiConversion_OmniAiConversionStatus_"></a> ColorOf\(OmniAiConversionStatus\)

アイコンの色の分類（実際の色は呼び出し側の配色に合わせる）。

```csharp
public static OmniAiConversionIconColor ColorOf(OmniAiConversionStatus status)
```

#### 引数（Parameters）

`status` [OmniAiConversionStatus](Omni.Editor.Manager.AiConversion.OmniAiConversionStatus.md)

#### 戻り値（Returns）

 [OmniAiConversionIconColor](Omni.Editor.Manager.AiConversion.OmniAiConversionIconColor.md)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStatusText_IconName_Omni_Editor_Manager_AiConversion_OmniAiConversionStatus_"></a> IconName\(OmniAiConversionStatus\)

Unity 組込みアイコンの名前（<code>None</code> は空文字＝アイコンなし）。

```csharp
public static string IconName(OmniAiConversionStatus status)
```

#### 引数（Parameters）

`status` [OmniAiConversionStatus](Omni.Editor.Manager.AiConversion.OmniAiConversionStatus.md)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStatusText_Label_Omni_Editor_Manager_AiConversion_OmniAiConversionStatus_System_Int32_"></a> Label\(OmniAiConversionStatus, int\)

状態の短い名前（表の「状態」欄・詳細欄の見出し）。

```csharp
public static string Label(OmniAiConversionStatus status, int attempt = 0)
```

#### 引数（Parameters）

`status` [OmniAiConversionStatus](Omni.Editor.Manager.AiConversion.OmniAiConversionStatus.md)

`attempt` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStatusText_ShowsAttempt_Omni_Editor_Manager_AiConversion_OmniAiConversionStatus_"></a> ShowsAttempt\(OmniAiConversionStatus\)

アイコンに数字（n 回目）を添える状態か。

```csharp
public static bool ShowsAttempt(OmniAiConversionStatus status)
```

#### 引数（Parameters）

`status` [OmniAiConversionStatus](Omni.Editor.Manager.AiConversion.OmniAiConversionStatus.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStatusText_Tooltip_Omni_Editor_Manager_AiConversion_OmniAiConversionStatus_System_Int32_System_Boolean_System_String_"></a> Tooltip\(OmniAiConversionStatus, int, bool, string\)

ツールチップ。状態名に、実験的経路の印と、最初の失敗の理由を添えます。

```csharp
public static string Tooltip(OmniAiConversionStatus status, int attempt, bool experimental, string firstFailure)
```

#### 引数（Parameters）

`status` [OmniAiConversionStatus](Omni.Editor.Manager.AiConversion.OmniAiConversionStatus.md)

`attempt` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`experimental` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`firstFailure` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
