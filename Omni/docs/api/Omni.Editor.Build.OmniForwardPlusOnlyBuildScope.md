# <a id="Omni_Editor_Build_OmniForwardPlusOnlyBuildScope"></a> Class OmniForwardPlusOnlyBuildScope

Namespace: [Omni.Editor.Build](Omni.Editor.Build.md)  
Assembly: Omni.Editor.dll  

Forward+ しか使わない開発用の Player ビルド（EarthToMoon、SolarSystem のデモ）の間だけ、ビルドに入る URP 資産の
Forward の Renderer を Forward+ に切り替えます。URP は資産の Renderer に1つでも Forward があると、Lit 系の
ForwardLit に Forward 用の組合せ（<code>_CLUSTER_LIGHT_LOOP</code> なし）を残すので、Forward+ だけなら約 4分の1 になります。
ビルドする Scene のカメラが Forward の Renderer を使っていたら、見た目が変わるので切り替えずに止めます。
製品と回帰 Player は Forward と Forward+ の両方を対象にするので使いません。Dispose で元の設定へ戻して保存します。
戻せない Renderer があれば、戻せた分を戻してから LogError と <xref href="System.InvalidOperationException" data-throw-if-not-resolved="false"></xref> でビルドを失敗させます
（黙って飛ばすと、Renderer が Forward+ のまま残る）。

```csharp
public sealed class OmniForwardPlusOnlyBuildScope : IDisposable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniForwardPlusOnlyBuildScope](Omni.Editor.Build.OmniForwardPlusOnlyBuildScope.md)

#### 実装するインターフェース（Implements）

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

## プロパティ（Properties）

### <a id="Omni_Editor_Build_OmniForwardPlusOnlyBuildScope_Enabled"></a> Enabled

測定用。false の間は <xref href="Omni.Editor.Build.OmniForwardPlusOnlyBuildScope.Begin(UnityEditor.BuildTarget%2cSystem.Collections.Generic.IEnumerable%7bSystem.String%7d)" data-throw-if-not-resolved="false"></xref> が何も切り替えず、Forward の Renderer のまま
ビルドします（切り替えた場合との Shader variant 数・サイズの比較に使います）。既定は true です。

```csharp
public static bool Enabled { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Build_OmniForwardPlusOnlyBuildScope_SwitchedRendererNames"></a> SwitchedRendererNames

切り替えた Renderer の名前。

```csharp
public IReadOnlyList<string> SwitchedRendererNames { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

## メソッド（Methods）

### <a id="Omni_Editor_Build_OmniForwardPlusOnlyBuildScope_Begin_UnityEditor_BuildTarget_System_Collections_Generic_IEnumerable_System_String__"></a> Begin\(BuildTarget, IEnumerable<string\>\)

ビルド先の品質レベルが参照する URP 資産の Forward の Renderer を、ビルドの間だけ Forward+ にします。
品質レベルを絞るときは、絞ったあとに呼びます。

```csharp
public static OmniForwardPlusOnlyBuildScope Begin(BuildTarget target, IEnumerable<string> scenePaths)
```

#### 引数（Parameters）

`target` BuildTarget

`scenePaths` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

#### 戻り値（Returns）

 [OmniForwardPlusOnlyBuildScope](Omni.Editor.Build.OmniForwardPlusOnlyBuildScope.md)

### <a id="Omni_Editor_Build_OmniForwardPlusOnlyBuildScope_Dispose"></a> Dispose\(\)

切り替えた Renderer を元の方式へ戻し、ファイルへ保存し直します。資産は資産パスから読み直して戻します。
戻せない Renderer（資産が消えた、資産でない Renderer が破棄された）があれば、残りを全部戻してから LogError を出し、
<xref href="System.InvalidOperationException" data-throw-if-not-resolved="false"></xref> を投げます（ビルドを失敗させる）。

```csharp
public void Dispose()
```
