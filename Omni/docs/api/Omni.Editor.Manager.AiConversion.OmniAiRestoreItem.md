# <a id="Omni_Editor_Manager_AiConversion_OmniAiRestoreItem"></a> Class OmniAiRestoreItem

Namespace: [Omni.Editor.Manager.AiConversion](Omni.Editor.Manager.AiConversion.md)  
Assembly: Omni.Manager.dll  

退避から戻すときの 1 ファイルの説明です。

```csharp
public sealed class OmniAiRestoreItem
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniAiRestoreItem](Omni.Editor.Manager.AiConversion.OmniAiRestoreItem.md)

## フィールド（Fields）

### <a id="Omni_Editor_Manager_AiConversion_OmniAiRestoreItem_AfterAiKnown"></a> AfterAiKnown

AI の作業の後の状態を記録してある。false のときは <xref href="Omni.Editor.Manager.AiConversion.OmniAiRestoreItem.HumanEditedAfterAi" data-throw-if-not-resolved="false"></xref> を判定できない。

```csharp
public bool AfterAiKnown
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiRestoreItem_Change"></a> Change

```csharp
public OmniAiRestoreChange Change
```

#### 値（Field Value）

 [OmniAiRestoreChange](Omni.Editor.Manager.AiConversion.OmniAiRestoreChange.md)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiRestoreItem_HumanEditedAfterAi"></a> HumanEditedAfterAi

AI の作業の後の状態を記録してあり、今がそれと違う（AI の後に人が直した）。戻すと人の変更も失う。

```csharp
public bool HumanEditedAfterAi
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiRestoreItem_Path"></a> Path

```csharp
public string Path
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
