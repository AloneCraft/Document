# <a id="Omni_Editor_Diagnostics_OmniSceneNoiseProbe"></a> Class OmniSceneNoiseProbe

Namespace: [Omni.Editor.Diagnostics](Omni.Editor.Diagnostics.md)  
Assembly: Omni.Editor.dll  

現在の比較Sceneを保存せず、指定した列だけのGPU出力を取得します。

```csharp
[InitializeOnLoad]
public static class OmniSceneNoiseProbe
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniSceneNoiseProbe](Omni.Editor.Diagnostics.OmniSceneNoiseProbe.md)

## メソッド（Methods）

### <a id="Omni_Editor_Diagnostics_OmniSceneNoiseProbe_Begin_System_String_System_Action_System_Boolean_System_String__"></a> Begin\(string, Action<bool, string\>\)

```csharp
public static void Begin(string filter, Action<bool, string> completed)
```

#### 引数（Parameters）

`filter` [string](https://learn.microsoft.com/dotnet/api/system.string)

`completed` [Action](https://learn.microsoft.com/dotnet/api/system.action\-2)<[bool](https://learn.microsoft.com/dotnet/api/system.boolean), [string](https://learn.microsoft.com/dotnet/api/system.string)\>
