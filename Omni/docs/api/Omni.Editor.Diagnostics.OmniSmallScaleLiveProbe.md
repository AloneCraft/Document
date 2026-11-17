# <a id="Omni_Editor_Diagnostics_OmniSmallScaleLiveProbe"></a> Class OmniSmallScaleLiveProbe

Namespace: [Omni.Editor.Diagnostics](Omni.Editor.Diagnostics.md)  
Assembly: Omni.Editor.dll  

専用の追加SceneとViewで、実OS入力後の表示・視点を記録する調査用入口です。

```csharp
[InitializeOnLoad]
public static class OmniSmallScaleLiveProbe
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniSmallScaleLiveProbe](Omni.Editor.Diagnostics.OmniSmallScaleLiveProbe.md)

## メソッド（Methods）

### <a id="Omni_Editor_Diagnostics_OmniSmallScaleLiveProbe_Begin_System_String_System_Action_System_Boolean_System_String__"></a> Begin\(string, Action<bool, string\>\)

キーとクリックは既存の外部入力プロセスへ依頼し、製品の操作関数は直接呼びません。

```csharp
public static void Begin(string command, Action<bool, string> callback)
```

#### 引数（Parameters）

`command` [string](https://learn.microsoft.com/dotnet/api/system.string)

`callback` [Action](https://learn.microsoft.com/dotnet/api/system.action\-2)<[bool](https://learn.microsoft.com/dotnet/api/system.boolean), [string](https://learn.microsoft.com/dotnet/api/system.string)\>
