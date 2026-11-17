# <a id="Omni_Editor_Build_OmniRadialBuildPreparation"></a> Class OmniRadialBuildPreparation

Namespace: [Omni.Editor.Build](Omni.Editor.Build.md)  
Assembly: Omni.Editor.dll  

Player Buildの前に、対数（Radial）版の標準URP Shaderが利用者の環境に揃っていることを保証します。
標準URP Shaderの対数版は同梱せず、対数への切替の準備の段で<code>Assets/Radial</code>（追跡しない）へ生成するため、
新しく取得したプロジェクトやCIの作業ツリーでは、ビルドの前に生成が要ります。

```csharp
public static class OmniRadialBuildPreparation
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniRadialBuildPreparation](Omni.Editor.Build.OmniRadialBuildPreparation.md)

## 補足（Remarks）

<p>
入口は2つあります。通常のビルド（Build Settings／Build And Run）は、<xref href="UnityEditor.BuildPlayerWindow" data-throw-if-not-resolved="false"></xref>のハンドラが
自動で<xref href="Omni.Editor.Build.OmniRadialBuildPreparation.Prepare(System.Collections.Generic.IReadOnlyList%7bSystem.String%7d)" data-throw-if-not-resolved="false"></xref>を呼びます。CIやデモのビルダーが<code>BuildPipeline.BuildPlayer</code>を直接呼ぶときは、
その前に<xref href="Omni.Editor.Build.OmniRadialBuildPreparation.Prepare(System.Collections.Generic.IReadOnlyList%7bSystem.String%7d)" data-throw-if-not-resolved="false"></xref>を呼びます。
</p>
<p>
<xref href="Omni.Editor.Build.OmniRadialBuildPreparation.Prepare(System.Collections.Generic.IReadOnlyList%7bSystem.String%7d)" data-throw-if-not-resolved="false"></xref>を通らずに足りない状態でビルドを始めると、<xref href="Omni.Editor.Build.OmniRadialBuildPreparationGuard" data-throw-if-not-resolved="false"></xref>が
理由を示してビルドを止めます（Fail Closed）。「変換不能」の判定があるときも止めます。ビルドの最中には生成しません。
</p>
<p>
変換保証の判定（保証済み／検査のみ合格／変換不能）は、ビルドログの<code>[Omni][Build Preparation]</code>に系統ごとの1行で出します。
「検査のみ合格」ではビルドを止めません。
</p>
<p>
対数が要るかは<xref href="Omni.Converter.OmniBuildRadialScope" data-throw-if-not-resolved="false"></xref>の判定で決めます（Managerが対数を記録している／ビルドするSceneが有効な
RadialCameraやRadialCameraToggleを持つ／<code>Assets/Radial</code>の生成物を参照している、のどれか。判定できないSceneは対数とみなす）。
対数を使わないビルドでは何もしません（Omniはそのビルドに関与しない）。
</p>

## メソッド（Methods）

### <a id="Omni_Editor_Build_OmniRadialBuildPreparation_Prepare_System_Collections_Generic_IReadOnlyList_System_String__"></a> Prepare\(IReadOnlyList<string\>\)

対数が要るビルドの前に、対数版を今の変換器で作り直し、変換保証の判定をビルドログへ系統ごとに1行で出し、
読み込み済みのSSAO featureのshader cacheを共有resourceへ揃えます。
生成できない、「変換不能」がある、または生成後も揃わないときは<xref href="UnityEditor.Build.BuildFailedException" data-throw-if-not-resolved="false"></xref>を投げます
（ビルドを始めてはいけません）。「検査のみ合格」では止めません。対数が要らなければ何もしません。

```csharp
public static void Prepare(IReadOnlyList<string> scenePaths = null)
```

#### 引数（Parameters）

`scenePaths` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

ビルドするScene。nullまたは空ならBuild Settingsで有効なSceneです。

### <a id="Omni_Editor_Build_OmniRadialBuildPreparation_RegisterRadialModeProbe_System_Func_System_Boolean__"></a> RegisterRadialModeProbe\(Func<bool\>\)

対数の描画方式が記録されているかを返す関数を登録します（Omni.Managerが登録します。Omni.EditorはManagerを参照しないため）。
判定は<xref href="Omni.Converter.OmniBuildRadialScope" data-throw-if-not-resolved="false"></xref>が持ちます。

```csharp
public static void RegisterRadialModeProbe(Func<bool> probe)
```

#### 引数（Parameters）

`probe` [Func](https://learn.microsoft.com/dotnet/api/system.func\-1)<[bool](https://learn.microsoft.com/dotnet/api/system.boolean)\>

### <a id="Omni_Editor_Build_OmniRadialBuildPreparation_RequiresRadial_System_Collections_Generic_IReadOnlyList_System_String__System_String__"></a> RequiresRadial\(IReadOnlyList<string\>, out string\)

指定したSceneのビルドに対数が要るかを返します（<xref href="Omni.Converter.OmniBuildRadialScope.Evaluate(System.Collections.Generic.IReadOnlyList%7bSystem.String%7d)" data-throw-if-not-resolved="false"></xref>）。<code class="paramref">scenePaths</code>が
nullまたは空なら、Build Settingsで有効なSceneを使います。判定できないSceneがあれば、対数が要るものとして理由つきでtrueを返します。

```csharp
public static bool RequiresRadial(IReadOnlyList<string> scenePaths, out string why)
```

#### 引数（Parameters）

`scenePaths` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

`why` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
