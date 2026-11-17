# <a id="Omni_Converter_OmniBuildRadialScope"></a> Class OmniBuildRadialScope

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

Player Build が対数（Radial）レンダリングを使うかの判定を 1 か所にまとめます。対数を使わないビルドでは、Omni の
ビルドの準備・検査（Scene BRG、Render Objects の検査、BRG sidecar と manifest、対数版の Shader の準備、variant の予算など）は
何もせず、ビルドに関与しません（2026-10-09 のユーザー判断）。各入口は <xref href="Omni.Converter.OmniBuildRadialScope.IsStandardPlayerBuild(UnityEditor.Build.Reporting.BuildReport)" data-throw-if-not-resolved="false"></xref> が true なら何もせずに戻ります。

```csharp
public static class OmniBuildRadialScope
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniBuildRadialScope](Omni.Converter.OmniBuildRadialScope.md)

## 補足（Remarks）

<p>
対数を使うビルドは、ビルドする Scene のどれかが次のどれかに当たるものです。Omni Manager が対数を記録している（ビルドの Scene の写しへ
RadialCamera を付ける、<code>OmniRenderingModeSceneProcessor</code>）／有効な RadialCamera を持つ（Component の有効だけを見て、GameObject の
有効は見ない。実行中に有効にされ得るため）／RadialCameraToggle を持つ（実行中に RadialCamera を有効にする）／RadialCamera を含む Prefab などの
資産を参照する（Scene ファイルからは有効かどうかを読まない）／<code>Assets/Radial</code> の生成物を参照する。
標準へ戻す切替は RadialCamera を消さずに無効にするので、無効な RadialCamera だけを持つ Scene は対数を使わないものとして扱います。
</p>
<p>
Scene は開きません。<xref href="UnityEditor.AssetDatabase.GetDependencies(System.String%2cSystem.Boolean)" data-throw-if-not-resolved="false"></xref>（取り込み済みの依存の記録。Prefab の入れ子と
バイナリの Scene も含む）で RadialCamera の script と生成物の参照を調べ、RadialCamera があるときだけ、保存された Scene の YAML から
その Component の <code>m_Enabled</code> を読みます。Scene を Preview や Additive で開くと、全ての資産を読み込み、[ExecuteAlways] の
OnEnable（RadialCamera の有効化の通知から Scene BRG の検査し直し）が走り、Additive では利用者の Scene の構成まで変わるためです。
</p>
<p>
判定は Fail Closed です。Scene が見つからない・テキストで保存されていない・RadialCamera の script が見つからない・Component の
有効を読めない、のどれかなら、対数を使うものとみなして従来どおり準備と検査をします。
</p>
<p>
ビルドの Scene は <xref href="UnityEditor.Build.BuildPlayerProcessor" data-throw-if-not-resolved="false"></xref> の <xref href="UnityEditor.Build.BuildPlayerContext.BuildPlayerOptions" data-throw-if-not-resolved="false"></xref> から取ります（Build Settings
からのビルドも、<code>BuildPipeline.BuildPlayer</code> を直接呼ぶビルドも同じ）。取れなかったときは、Build Settings の有効な Scene と、
<code>OmniRadialBuildPreparation.Prepare</code> が受けた Scene の和で判定します。どちらでも、対数を使わないと判定したビルドで実際に処理された
Scene が対数を使うと分かったら、ビルドを止めます（<xref href="Omni.Converter.OmniBuildRadialSceneBackstop" data-throw-if-not-resolved="false"></xref>）。
</p>

## メソッド（Methods）

### <a id="Omni_Converter_OmniBuildRadialScope_ClassifyScene_System_String_"></a> ClassifyScene\(string\)

Scene 1つを、開かずに判定します。依存の記録で RadialCamera・RadialCameraToggle・生成物の参照を調べ、RadialCamera が Scene ファイル
自身にあるときだけ、保存された YAML から <code>m_Enabled</code> を読みます。

```csharp
public static OmniSceneRadialClassification ClassifyScene(string scenePath)
```

#### 引数（Parameters）

`scenePath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [OmniSceneRadialClassification](Omni.Converter.OmniSceneRadialClassification.md)

### <a id="Omni_Converter_OmniBuildRadialScope_Evaluate_System_Collections_Generic_IReadOnlyList_System_String__"></a> Evaluate\(IReadOnlyList<string\>\)

指定した Scene のビルドが対数を使うかを判定します。<code class="paramref">scenePaths</code> はそのまま使います（null や空は判定できない）。

```csharp
public static OmniBuildRadialDecision Evaluate(IReadOnlyList<string> scenePaths)
```

#### 引数（Parameters）

`scenePaths` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

#### 戻り値（Returns）

 [OmniBuildRadialDecision](Omni.Converter.OmniBuildRadialDecision.md)

### <a id="Omni_Converter_OmniBuildRadialScope_ForBuild_UnityEditor_Build_Reporting_BuildReport_"></a> ForBuild\(BuildReport\)

このビルドの判定です。同じビルドの中では同じ結果を返します。<code class="paramref">report</code> が null なら、
<xref href="Omni.Converter.OmniBuildRadialScope.ScenesWithoutBuildOptions" data-throw-if-not-resolved="false"></xref> をその場で判定します（覚えません）。

```csharp
public static OmniBuildRadialDecision ForBuild(BuildReport report)
```

#### 引数（Parameters）

`report` BuildReport

#### 戻り値（Returns）

 [OmniBuildRadialDecision](Omni.Converter.OmniBuildRadialDecision.md)

### <a id="Omni_Converter_OmniBuildRadialScope_IsStandardPlayerBuild_UnityEditor_Build_Reporting_BuildReport_"></a> IsStandardPlayerBuild\(BuildReport\)

Player Build で、対数を使わないと判定したビルドなら true です（入口はこのとき何もせずに戻ります）。
<code class="paramref">report</code> が null（Play の開始、テストからの直接の呼び出し）や AssetBundle のビルドでは false で、従来どおりです。

```csharp
public static bool IsStandardPlayerBuild(BuildReport report)
```

#### 引数（Parameters）

`report` BuildReport

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniBuildRadialScope_NotePreparedScenes_System_Collections_Generic_IEnumerable_System_String__"></a> NotePreparedScenes\(IEnumerable<string\>\)

<code>OmniRadialBuildPreparation.Prepare</code> が受けた Scene を覚えます。ビルドの Scene が取れなかったときの判定に加えます。
資産として無い Scene（ビルドできない）は覚えません。

```csharp
public static void NotePreparedScenes(IEnumerable<string> scenePaths)
```

#### 引数（Parameters）

`scenePaths` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Converter_OmniBuildRadialScope_RegisterRadialModeProbe_System_Func_System_Boolean__"></a> RegisterRadialModeProbe\(Func<bool\>\)

対数の描画方式が記録されているかを返す関数を登録します（Omni.Manager が登録します。記録されている間は、ビルドの Scene の写しへ
RadialCamera が付くため、ビルドは対数を使います）。

```csharp
public static void RegisterRadialModeProbe(Func<bool> probe)
```

#### 引数（Parameters）

`probe` [Func](https://learn.microsoft.com/dotnet/api/system.func\-1)<[bool](https://learn.microsoft.com/dotnet/api/system.boolean)\>

### <a id="Omni_Converter_OmniBuildRadialScope_ResolveRequestedScenes_System_String___"></a> ResolveRequestedScenes\(string\[\]\)

BuildPlayerOptions の Scene です。空のとき Unity は開いている Scene をビルドするので、読み込み済みの Scene と、
念のため Build Settings の有効な Scene も加えます（多く判定する側へ倒す）。

```csharp
public static List<string> ResolveRequestedScenes(string[] requested)
```

#### 引数（Parameters）

`requested` [string](https://learn.microsoft.com/dotnet/api/system.string)\[\]

#### 戻り値（Returns）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Converter_OmniBuildRadialScope_ScenesWithoutBuildOptions"></a> ScenesWithoutBuildOptions\(\)

ビルドの Scene が分からないときに判定する Scene です。<xref href="Omni.Converter.OmniBuildRadialScope.NotePreparedScenes(System.Collections.Generic.IEnumerable%7bSystem.String%7d)" data-throw-if-not-resolved="false"></xref> で覚えた Scene と、Build Settings の有効な Scene の和です。

```csharp
public static List<string> ScenesWithoutBuildOptions()
```

#### 戻り値（Returns）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>
