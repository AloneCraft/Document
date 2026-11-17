# <a id="Omni_Editor_Manager_OmniRenderingModeAutoApply"></a> Class OmniRenderingModeAutoApply

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

対数が記録されている間、Editorで開いたSceneのCameraへ <xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref> を付けて有効にします。

<p>
Undoへ記録せず、Sceneを未保存（dirty）にもしません。開くたびに保存を求めないためと、
未保存のSceneがあるとテストが始まらないためです。PlayとPlayer Buildでは
<xref href="Omni.Editor.Manager.OmniRenderingModeSceneProcessor" data-throw-if-not-resolved="false"></xref> が毎回付け直すので、保存されなくても困りません。
</p>
<p>
付けるのはMaterialが対数のSceneだけです（<xref href="Omni.Editor.Manager.OmniCameraScanner.IsSceneMaterialsRadial(UnityEngine.SceneManagement.Scene)" data-throw-if-not-resolved="false"></xref>）。
標準のMaterialのSceneは標準のまま表示します。
自動で付けた分はSceneファイルへ保存しません。新しく付けたComponentは
<xref href="UnityEngine.HideFlags.DontSaveInEditor" data-throw-if-not-resolved="false"></xref> にし、保存済みの無効なRadialCameraを有効にした分は
保存の直前に無効へ戻して保存後に有効へ戻します。Omni自身がScene参照を書き換えて保存するとき
（Project範囲の切替）に、自動付与まで書き込まれて標準へ戻しても残る不具合がありました。
記録が対数でなくなったら、自動で付けた分を外します。
</p>

```csharp
[InitializeOnLoad]
public static class OmniRenderingModeAutoApply
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniRenderingModeAutoApply](Omni.Editor.Manager.OmniRenderingModeAutoApply.md)

## メソッド（Methods）

### <a id="Omni_Editor_Manager_OmniRenderingModeAutoApply_ApplyToLoadedScenes"></a> ApplyToLoadedScenes\(\)

ロード済みの全Sceneへ反映します。対数でなければ自動で付けた分を外します。
Play中は何もしません（Playは別経路で付けます）。

```csharp
public static void ApplyToLoadedScenes()
```
