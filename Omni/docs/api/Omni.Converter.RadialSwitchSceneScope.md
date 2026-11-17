# <a id="Omni_Converter_RadialSwitchSceneScope"></a> Class RadialSwitchSceneScope

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

統合切替（標準／対数）が走査・変更するSceneを一時的に限定します。限定していない間は、
従来どおりロード済みの全Sceneが対象です。ほかのSceneを開いたまま特定のSceneだけを
切り替える検証（Radialの生成物は追跡せず、保存済みSceneは標準状態）で使います。

```csharp
public static class RadialSwitchSceneScope
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialSwitchSceneScope](Omni.Converter.RadialSwitchSceneScope.md)

## メソッド（Methods）

### <a id="Omni_Converter_RadialSwitchSceneScope_Includes_UnityEngine_SceneManagement_Scene_"></a> Includes\(Scene\)

指定Sceneが現在の切替対象かを返します。

```csharp
public static bool Includes(Scene scene)
```

#### 引数（Parameters）

`scene` Scene

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_RadialSwitchSceneScope_Limit_System_Collections_Generic_IEnumerable_UnityEngine_SceneManagement_Scene__"></a> Limit\(IEnumerable<Scene\>\)

Disposeまでの間、切替の対象を指定したSceneだけにします。入れ子にはできません。

```csharp
public static IDisposable Limit(IEnumerable<Scene> scenes)
```

#### 引数（Parameters）

`scenes` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<Scene\>

#### 戻り値（Returns）

 [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
