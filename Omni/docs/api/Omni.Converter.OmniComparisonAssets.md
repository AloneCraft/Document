# <a id="Omni_Converter_OmniComparisonAssets"></a> Class OmniComparisonAssets

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

標準と対数を見比べる比較Sceneと、その元（URP）のMaterialを、全体の標準／対数の切替から守ります。

```csharp
public static class OmniComparisonAssets
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniComparisonAssets](Omni.Converter.OmniComparisonAssets.md)

## 補足（Remarks）

<p>
比較Sceneは全ての列で元のMaterialを保存し、Radialの列は比較スコープ（撮影・Play・Player Build）だけが
Radial版へ差し替えます。全体の切替で元のMaterialをその場で対数へ書き換えると、URPの列までRadialになり比較が
成り立たないため、ロード済みScene範囲の対数切替は比較Sceneがあれば止め（HardBlocker）、Project範囲では
比較用のMaterialを「対象外」にします。
</p>
<p>
どれが比較Scene・比較用Materialかは、それを所有する検証側（<code>Omni.Verification.Editor</code>）が登録します。
Converterは検証の型を参照しません。
</p>

## メソッド（Methods）

### <a id="Omni_Converter_OmniComparisonAssets_IsComparisonMaterial_UnityEngine_Material_"></a> IsComparisonMaterial\(Material\)

全体の切替から守る比較用のMaterialならtrueです。

```csharp
public static bool IsComparisonMaterial(Material material)
```

#### 引数（Parameters）

`material` Material

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniComparisonAssets_IsComparisonScene_UnityEngine_SceneManagement_Scene_"></a> IsComparisonScene\(Scene\)

比較Sceneならtrueです。

```csharp
public static bool IsComparisonScene(Scene scene)
```

#### 引数（Parameters）

`scene` Scene

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniComparisonAssets_Register_System_Func_UnityEngine_Material_System_Boolean__System_Func_UnityEngine_SceneManagement_Scene_System_Boolean__"></a> Register\(Func<Material, bool\>, Func<Scene, bool\>\)

比較用Materialと比較Sceneの判定を登録します。

```csharp
public static void Register(Func<Material, bool> isComparisonMaterial, Func<Scene, bool> isComparisonScene)
```

#### 引数（Parameters）

`isComparisonMaterial` [Func](https://learn.microsoft.com/dotnet/api/system.func\-2)<Material, [bool](https://learn.microsoft.com/dotnet/api/system.boolean)\>

`isComparisonScene` [Func](https://learn.microsoft.com/dotnet/api/system.func\-2)<Scene, [bool](https://learn.microsoft.com/dotnet/api/system.boolean)\>

### <a id="Omni_Converter_OmniComparisonAssets_SuspendForTests"></a> SuspendForTests\(\)

テストが比較Sceneを全体切替の題材に使う間だけ、保護を止めます（Disposeで戻します）。

```csharp
public static IDisposable SuspendForTests()
```

#### 戻り値（Returns）

 [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

### <a id="Omni_Converter_OmniComparisonAssets_TryFindLoadedComparisonScene_System_String__"></a> TryFindLoadedComparisonScene\(out string\)

ロード済みの比較Sceneを1つ探します。無ければfalseです。

```csharp
public static bool TryFindLoadedComparisonScene(out string scenePath)
```

#### 引数（Parameters）

`scenePath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
