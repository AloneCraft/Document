# <a id="Omni_Editor_Manager_RadialBaker"></a> Class RadialBaker

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

Radial ワープのカメラ非依存な静的データ（<xref href="Omni.Rendering.Radial.BakeData" data-throw-if-not-resolved="false"></xref>）を生成する
Editor ツールです。運用感は Unity の Lightmap ベイクに準じます
（明示実行 → ディスクへアセット保存 → シーン/ワープ設定の変更で再ベイクが要る）。

<p>
ここでベイクするのはカメラ非依存の静的な材料だけです。ワープ後の座標そのものは
保存しません（カメラは毎フレーム動くため、保存してもカメラが動いた瞬間に無効になります）。
</p>

```csharp
public static class RadialBaker
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialBaker](Omni.Editor.Manager.RadialBaker.md)

## フィールド（Fields）

### <a id="Omni_Editor_Manager_RadialBaker_DefaultAngularTolerance"></a> DefaultAngularTolerance

遠景キャッシュの許容角度誤差ε（ラジアン）。既定値は60°FOV/1080p相当の画素サイズ目安です。

```csharp
public const float DefaultAngularTolerance = 0.001
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Editor_Manager_RadialBaker_DefaultFarFieldFactor"></a> DefaultFarFieldFactor

遠景分類の閾値係数k。MinDistance &gt; k * characteristicScale を FarField とみなします。

```csharp
public const float DefaultFarFieldFactor = 10
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

## メソッド（Methods）

### <a id="Omni_Editor_Manager_RadialBaker_BakeActiveSceneMenuItem"></a> BakeActiveSceneMenuItem\(\)

```csharp
public static void BakeActiveSceneMenuItem()
```

### <a id="Omni_Editor_Manager_RadialBaker_BakeAllLoadedScenes"></a> BakeAllLoadedScenes\(\)

現在ロード済みの全シーンをベイクします。プロジェクト全体（未ロードのシーン）は対象外です
（対象を広げたい場合は呼び出し側でシーンを開いてから呼んでください）。

```csharp
public static int BakeAllLoadedScenes()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Manager_RadialBaker_BakeAllLoadedScenesMenuItem"></a> BakeAllLoadedScenesMenuItem\(\)

```csharp
public static void BakeAllLoadedScenesMenuItem()
```

### <a id="Omni_Editor_Manager_RadialBaker_BakeScene_UnityEngine_SceneManagement_Scene_System_Nullable_Omni_Logical_Aabb__"></a> BakeScene\(Scene, Aabb?\)

指定シーンをベイクします。<code class="paramref">cameraRegion</code> を省略した場合、
シーン内 Radial 対象 Renderer の合成 Bounds を使います。
シーン内に有効な <xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref> が1つも無い場合はベイクせず null を返します
（ワープ設定が定まらないため）。

```csharp
public static BakeData BakeScene(Scene scene, Aabb? cameraRegion = null)
```

#### 引数（Parameters）

`scene` Scene

`cameraRegion` Aabb?

#### 戻り値（Returns）

 BakeData

### <a id="Omni_Editor_Manager_RadialBaker_ComputeCurrentSceneContentHash_UnityEngine_SceneManagement_Scene_"></a> ComputeCurrentSceneContentHash\(Scene\)

現在のシーン内容から、ベイク時と同じ規則でハッシュを計算します。
<xref href="Omni.Rendering.Radial.BakeData.SceneContentHash" data-throw-if-not-resolved="false"></xref> と比較すれば陳腐化を検出できます
（<code>OmniValidator</code> が使用）。

```csharp
public static string ComputeCurrentSceneContentHash(Scene scene)
```

#### 引数（Parameters）

`scene` Scene

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_RadialBaker_IsBakeStale_UnityEngine_SceneManagement_Scene_Omni_RadialCamera_Omni_Editor_Manager_RadialBakeStaleReason__System_String__"></a> IsBakeStale\(Scene, RadialCamera, out RadialBakeStaleReason, out string\)

指定シーンのベイクデータが、指定ドライバの現在設定に対して有効かどうかを判定します。

```csharp
public static bool IsBakeStale(Scene scene, RadialCamera driver, out RadialBakeStaleReason reasonCode, out string reason)
```

#### 引数（Parameters）

`scene` Scene

判定対象のシーン。

`driver` RadialCamera

現在の設定を持つ RadialCamera。

`reasonCode` [RadialBakeStaleReason](Omni.Editor.Manager.RadialBakeStaleReason.md)

無効・陳腐化している場合はその分類。呼び出し側はこれで分岐し、<code class="paramref">reason</code>の
文字列内容には依存しないでください（表示文言はローカライズ対象で変わり得ます）。

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

無効・陳腐化している場合はその理由（人間向け表示専用）。有効なら null。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

再ベイクが必要なら true。

### <a id="Omni_Editor_Manager_RadialBaker_RebakeGardenRadialData"></a> RebakeGardenRadialData\(\)

Gardenの既存Bake assetだけをschema v2で再生成します。既存BindingとRegistryが
同じassetを指す場合に限り実行し、Scene・Binding・Registryは保存しません。

```csharp
public static string RebakeGardenRadialData()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_RadialBaker_RebakeRadialData"></a> RebakeRadialData\(\)

Logical移行対象7 Sceneを明示的に走査し、既存Bindingがそのまま使えるSceneだけを
再ベイクします。BindingがないSceneに新規コンポーネントを追加したり、Sceneを保存したりは
しません。Bindingを安全に復元できない旧Bake assetはschemaを推測して移行せず、
fail-openのまま明示的な完全再ベイクを要求します。

```csharp
public static string RebakeRadialData()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 補足（Remarks）

特にCameraCombinationVerificationは利用者のdirty差分を保護するため、Bindingを自動追加しません。
Binding追加とScene保存は明示承認を要する別作業です。

### <a id="Omni_Editor_Manager_RadialBaker_RebakeRadialDataMenuItem"></a> RebakeRadialDataMenuItem\(\)

```csharp
public static void RebakeRadialDataMenuItem()
```
