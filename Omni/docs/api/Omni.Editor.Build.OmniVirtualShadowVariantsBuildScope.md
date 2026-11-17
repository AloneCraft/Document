# <a id="Omni_Editor_Build_OmniVirtualShadowVariantsBuildScope"></a> Class OmniVirtualShadowVariantsBuildScope

Namespace: [Omni.Editor.Build](Omni.Editor.Build.md)  
Assembly: Omni.Editor.dll  

仮想シャドウマップ（<xref href="Omni.OmniVirtualShadowsFeature" data-throw-if-not-resolved="false"></xref>）を使う Player ビルドの間だけ、画面空間の影を受ける Shader の組合せ
（<code>_MAIN_LIGHT_SHADOWS_SCREEN</code>）を Player に残します。

<p>
仮想シャドウマップは、結果を URP の画面空間の影のテクスチャへ書き、標準の受け手（URP Lit・Radial Lit）にはこのキーワードで受けさせます。
URP は、ビルドに入る URP 資産の Renderer のどれにも有効な URP の ScreenSpaceShadows Feature が無いと、この組合せを Player から外します
（ShaderBuildPreprocessor・ShaderScriptableStripper）。外れると、仮想シャドウマップが働く間、標準の受け手が正しく描かれません
（2026-11-12、EarthToMoon の Windows Player で施設と乗り物が青一色になった。Editor は組合せをその場で作るので起きない）。
</p>
<p>
そこで、有効な ScreenSpaceShadows Feature だけを持つ Renderer を作り、ビルドの間だけ URP 資産の Renderer の一覧の末尾へ足します。
この Renderer はどのカメラも使わないので、実行時の描画は変わりません（URP の画面空間の影のパスは走りません）。
Dispose で一覧から外し、作った Renderer を消します。仮想シャドウマップの Feature が無い URP 資産と、もともと ScreenSpaceShadows を
持つ URP 資産は触りません。
</p>

```csharp
public sealed class OmniVirtualShadowVariantsBuildScope : IDisposable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniVirtualShadowVariantsBuildScope](Omni.Editor.Build.OmniVirtualShadowVariantsBuildScope.md)

#### 実装するインターフェース（Implements）

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

## プロパティ（Properties）

### <a id="Omni_Editor_Build_OmniVirtualShadowVariantsBuildScope_PatchedAssetCount"></a> PatchedAssetCount

足した URP 資産の数（0 なら何も変えていません）。

```csharp
public int PatchedAssetCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_Editor_Build_OmniVirtualShadowVariantsBuildScope_Begin_UnityEditor_BuildTarget_"></a> Begin\(BuildTarget\)

ビルド先の品質レベルが参照する URP 資産を対象にします。品質レベルを絞るときは、絞ったあとに呼びます。

```csharp
public static OmniVirtualShadowVariantsBuildScope Begin(BuildTarget target)
```

#### 引数（Parameters）

`target` BuildTarget

#### 戻り値（Returns）

 [OmniVirtualShadowVariantsBuildScope](Omni.Editor.Build.OmniVirtualShadowVariantsBuildScope.md)

### <a id="Omni_Editor_Build_OmniVirtualShadowVariantsBuildScope_Dispose"></a> Dispose\(\)

```csharp
public void Dispose()
```
