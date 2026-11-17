# <a id="Omni_Editor_Manager_OmniValidator"></a> Class OmniValidator

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

プロジェクトとシーンの Omni 関連問題を検出します。

```csharp
public static class OmniValidator
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniValidator](Omni.Editor.Manager.OmniValidator.md)

## メソッド（Methods）

### <a id="Omni_Editor_Manager_OmniValidator_RunAndLog"></a> RunAndLog\(\)

<xref href="Omni.Editor.Manager.OmniValidator.ValidateAll" data-throw-if-not-resolved="false"></xref> を直接実行し、結果をログへ出力するEditor自動化用の入口です。
Omni Managerの表示状態に関わらず検証できます。

```csharp
public static void RunAndLog()
```

### <a id="Omni_Editor_Manager_OmniValidator_ValidateAll"></a> ValidateAll\(\)

現在のシーンとプロジェクト設定の全検査を実行します。

```csharp
public static List<OmniIssue> ValidateAll()
```

#### 戻り値（Returns）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[OmniIssue](Omni.Editor.Manager.OmniIssue.md)\>
