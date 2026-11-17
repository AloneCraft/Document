# <a id="Omni_Observer_Editor_RadialObserverTerminalInstaller"></a> Class RadialObserverTerminalInstaller

Namespace: [Omni.Observer.Editor](Omni.Observer.Editor.md)  
Assembly: Omni.RadialObserver.Editor.dll  

sceneへ観察Rigを置きます。sceneの<code>SceneMetaData</code>は、Awakeで
Root・PlayerRig・自分以外のシーンルートを全て非アクティブにします（複数シーン構成のため）。
シーンルート直下に置いたRigは消されるので、必ず<code>SceneMetaData.Root</code>の子へ置きます。

```csharp
public static class RadialObserverTerminalInstaller
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialObserverTerminalInstaller](Omni.Observer.Editor.RadialObserverTerminalInstaller.md)

## メソッド（Methods）

### <a id="Omni_Observer_Editor_RadialObserverTerminalInstaller_Install_System_String_"></a> Install\(string\)

```csharp
public static void Install(string ScenePath)
```

#### 引数（Parameters）

`ScenePath` [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Observer_Editor_RadialObserverTerminalInstaller_InstallFromCommandLine"></a> InstallFromCommandLine\(\)

-executeMethod用。コマンドライン <code>-observerScenes a.unity;b.unity</code> のSceneへ置きます。

```csharp
public static void InstallFromCommandLine()
```
