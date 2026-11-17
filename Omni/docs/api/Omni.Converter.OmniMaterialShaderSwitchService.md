# <a id="Omni_Converter_OmniMaterialShaderSwitchService"></a> Class OmniMaterialShaderSwitchService

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

書込可能なMaterialはShaderを切り替え、読取専用のMaterialは管理用の写しへ参照を切り替えます。
解析と変更を分離し、対象が1件でも不正なら書き込み前に停止します。

```csharp
public static class OmniMaterialShaderSwitchService
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniMaterialShaderSwitchService](Omni.Converter.OmniMaterialShaderSwitchService.md)

## フィールド（Fields）

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_DiagnosticShaderName"></a> DiagnosticShaderName

```csharp
public const string DiagnosticShaderName = "Omni/Radial/Diagnostics/UnsupportedConversion"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_Analyze_System_Collections_Generic_IEnumerable_UnityEngine_Material__"></a> Analyze\(IEnumerable<Material\>\)

明示されたMaterial集合だけを解析します。テストと部分適用UIの共通入口です。

```csharp
public static OmniMaterialShaderSwitchService.Plan Analyze(IEnumerable<Material> materials)
```

#### 引数（Parameters）

`materials` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<Material\>

#### 戻り値（Returns）

 [OmniMaterialShaderSwitchService](Omni.Converter.OmniMaterialShaderSwitchService.md).[Plan](Omni.Converter.OmniMaterialShaderSwitchService.Plan.md)

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_AnalyzeLoadedScenes"></a> AnalyzeLoadedScenes\(\)

ロード済みSceneの永続Materialを重複なく収集し、変更せずに解析します。

```csharp
public static OmniMaterialShaderSwitchService.Plan AnalyzeLoadedScenes()
```

#### 戻り値（Returns）

 [OmniMaterialShaderSwitchService](Omni.Converter.OmniMaterialShaderSwitchService.md).[Plan](Omni.Converter.OmniMaterialShaderSwitchService.Plan.md)

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_Apply_Omni_Converter_OmniMaterialShaderSwitchService_Plan_"></a> Apply\(Plan\)

解析済み計画を再検証し、同じMaterialアセットへ一括適用します。

```csharp
public static OmniMaterialShaderSwitchService.Result Apply(OmniMaterialShaderSwitchService.Plan plan)
```

#### 引数（Parameters）

`plan` [OmniMaterialShaderSwitchService](Omni.Converter.OmniMaterialShaderSwitchService.md).[Plan](Omni.Converter.OmniMaterialShaderSwitchService.Plan.md)

#### 戻り値（Returns）

 [OmniMaterialShaderSwitchService](Omni.Converter.OmniMaterialShaderSwitchService.md).[Result](Omni.Converter.OmniMaterialShaderSwitchService.Result.md)

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_CollectLoadedSceneMaterials"></a> CollectLoadedSceneMaterials\(\)

ロード済みSceneの切替対象Materialを重複なく返します（解析や変更はしません）。

```csharp
public static HashSet<Material> CollectLoadedSceneMaterials()
```

#### 戻り値（Returns）

 [HashSet](https://learn.microsoft.com/dotnet/api/system.collections.generic.hashset\-1)<Material\>

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_DiagnosticReplacementCount"></a> DiagnosticReplacementCount\(\)

診断表示の記録の件数です。0なら診断の再評価は要りません。

```csharp
public static int DiagnosticReplacementCount()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_IsApplied_UnityEngine_Material_"></a> IsApplied\(Material\)

```csharp
public static bool IsApplied(Material material)
```

#### 引数（Parameters）

`material` Material

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_IsEmbeddedFullscreenGraphMaterial_UnityEngine_Material_System_String_"></a> IsEmbeddedFullscreenGraphMaterial\(Material, string\)

Fullscreen Shader Graphの既定Materialを判定する既存APIです。

```csharp
public static bool IsEmbeddedFullscreenGraphMaterial(Material material, string path)
```

#### 引数（Parameters）

`material` Material

`path` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_IsEmbeddedShaderGraphMaterial_UnityEngine_Material_System_String_"></a> IsEmbeddedShaderGraphMaterial\(Material, string\)

Shader Graphがインポート時に作る既定Materialかを返します。
メモリ上でShaderを変更しても再インポートで戻るため、管理Materialへ参照を差し替えます。

```csharp
public static bool IsEmbeddedShaderGraphMaterial(Material material, string path)
```

#### 引数（Parameters）

`material` Material

`path` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_PrepareLoadedScenes"></a> PrepareLoadedScenes\(\)

ロード済みSceneを対象に、必要なユーザーShader生成まで行って適用可能な計画を返します。
同梱Shaderは生成器へ渡しません。

```csharp
public static OmniMaterialShaderSwitchService.Plan PrepareLoadedScenes()
```

#### 戻り値（Returns）

 [OmniMaterialShaderSwitchService](Omni.Converter.OmniMaterialShaderSwitchService.md).[Plan](Omni.Converter.OmniMaterialShaderSwitchService.Plan.md)

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_PrepareProjectAssets_System_Collections_Generic_IEnumerable_UnityEngine_Material__"></a> PrepareProjectAssets\(IEnumerable<Material\>\)

Assets配下の書換可能Materialを対象に、必要なユーザーShader生成まで含めて解析します。
呼出し側はFullscreen等の変換不要Materialを除外して渡します。

```csharp
public static OmniMaterialShaderSwitchService.Plan PrepareProjectAssets(IEnumerable<Material> materials)
```

#### 引数（Parameters）

`materials` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<Material\>

#### 戻り値（Returns）

 [OmniMaterialShaderSwitchService](Omni.Converter.OmniMaterialShaderSwitchService.md).[Plan](Omni.Converter.OmniMaterialShaderSwitchService.Plan.md)

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_ReconcileLedger_System_Collections_Generic_IEnumerable_UnityEngine_Material__Omni_Converter_OmniMaterialShaderSwitchService_ReferenceScope_System_Collections_Generic_List_System_String__"></a> ReconcileLedger\(IEnumerable<Material\>, ReferenceScope, List<string\>\)

台帳の記録のうち、現在のMaterialと食い違うものを整理します。切替（対数・標準とも）の
解析の前に呼びます。台帳はUnityの外での変更（フォルダの上書き、git checkout、生成物の削除）
を知らないため、食い違いを残すと切替が両方向とも止まり、利用者には直す手段がありません。
整理の規則:
・Materialが元のShaderに戻っている：記録だけを消す（元の状態がそこにある）。
・対数Shaderが消えた（Shaderが欠落またはエラーShader）：元のShaderと状態へ戻して記録を消す。
・別のRadial Shaderへ替わっている：元の情報を残したまま、記録の対数Shaderを付け替える。
・それ以外のShaderへ替わっている：記録を消し、現在のShaderを元として変換し直させる。
・Materialが消えている：記録を消す。
・管理Material（読取専用Materialの写し／診断表示）が欠けている、または食い違う：
  参照を元のMaterialへ戻し、管理Materialと記録を消す（次の適用で作り直す）。
途中終了した適用（TransactionInProgress）は起動時の復旧に任せ、ここでは触りません。

```csharp
public static int ReconcileLedger(IEnumerable<Material> targetMaterials, OmniMaterialShaderSwitchService.ReferenceScope referenceScope, List<string> details)
```

#### 引数（Parameters）

`targetMaterials` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<Material\>

対象のMaterial。nullなら台帳の全記録が対象です。
    Materialが消えた記録は範囲にかかわらず整理します。

`referenceScope` [OmniMaterialShaderSwitchService](Omni.Converter.OmniMaterialShaderSwitchService.md).[ReferenceScope](Omni.Converter.OmniMaterialShaderSwitchService.ReferenceScope.md)

`details` [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

整理した内容を1件1行で追加します（null可）。

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

整理した記録の数です。

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_RecoverInterruptedRestore_UnityEngine_Material_"></a> RecoverInterruptedRestore\(Material\)

中断後、現在の内容が元ファイルと一致し、差が既知の保存形式だけの場合に復元を完了する。

```csharp
public static OmniMaterialShaderSwitchService.Result RecoverInterruptedRestore(Material material)
```

#### 引数（Parameters）

`material` Material

#### 戻り値（Returns）

 [OmniMaterialShaderSwitchService](Omni.Converter.OmniMaterialShaderSwitchService.md).[Result](Omni.Converter.OmniMaterialShaderSwitchService.Result.md)

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_Revert_System_Collections_Generic_IEnumerable_UnityEngine_Material__System_Boolean_"></a> Revert\(IEnumerable<Material\>, bool\)

明示されたMaterialだけを復元します。限定復元のテストにも使用します。

```csharp
public static OmniMaterialShaderSwitchService.Result Revert(IEnumerable<Material> materials, bool dryRun)
```

#### 引数（Parameters）

`materials` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<Material\>

`dryRun` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [OmniMaterialShaderSwitchService](Omni.Converter.OmniMaterialShaderSwitchService.md).[Result](Omni.Converter.OmniMaterialShaderSwitchService.Result.md)

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_RevertAll_System_Boolean_"></a> RevertAll\(bool\)

台帳内の適用済みMaterialを元Shaderへ戻し、利用者編集を保持します。

```csharp
public static OmniMaterialShaderSwitchService.Result RevertAll(bool dryRun)
```

#### 引数（Parameters）

`dryRun` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [OmniMaterialShaderSwitchService](Omni.Converter.OmniMaterialShaderSwitchService.md).[Result](Omni.Converter.OmniMaterialShaderSwitchService.Result.md)

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_RevertLoadedScenes_System_Boolean_"></a> RevertLoadedScenes\(bool\)

ロード済みSceneで使用中のMaterialだけを標準Shaderへ戻します。
未ロードSceneだけが利用する台帳項目には触れません。

```csharp
public static OmniMaterialShaderSwitchService.Result RevertLoadedScenes(bool dryRun)
```

#### 引数（Parameters）

`dryRun` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [OmniMaterialShaderSwitchService](Omni.Converter.OmniMaterialShaderSwitchService.md).[Result](Omni.Converter.OmniMaterialShaderSwitchService.Result.md)

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_RevertProjectAssets_System_Collections_Generic_IEnumerable_UnityEngine_Material__System_Boolean_"></a> RevertProjectAssets\(IEnumerable<Material\>, bool\)

Assets配下の書換可能な独立Materialを標準Shaderへ戻します。
管理診断MaterialへのProject参照も元Materialへ復元します。

```csharp
public static OmniMaterialShaderSwitchService.Result RevertProjectAssets(IEnumerable<Material> materials, bool dryRun)
```

#### 引数（Parameters）

`materials` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<Material\>

`dryRun` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [OmniMaterialShaderSwitchService](Omni.Converter.OmniMaterialShaderSwitchService.md).[Result](Omni.Converter.OmniMaterialShaderSwitchService.Result.md)

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_TryGetAppliedShaderMapping_UnityEngine_Material_UnityEngine_Shader__UnityEngine_Shader__System_Boolean__"></a> TryGetAppliedShaderMapping\(Material, out Shader, out Shader, out bool\)

台帳に登録された標準／対数Shaderと、現在の割当が競合しているかを返します。

```csharp
public static bool TryGetAppliedShaderMapping(Material material, out Shader sourceShader, out Shader radialShader, out bool conflict)
```

#### 引数（Parameters）

`material` Material

`sourceShader` Shader

`radialShader` Shader

`conflict` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_TryGetDiagnosticReplacement_UnityEngine_Material_UnityEngine_Material__UnityEngine_Shader__System_String__"></a> TryGetDiagnosticReplacement\(Material, out Material, out Shader, out string\)

```csharp
public static bool TryGetDiagnosticReplacement(Material material, out Material original, out Shader originalShader, out string failureReason)
```

#### 引数（Parameters）

`material` Material

`original` Material

`originalShader` Shader

`failureReason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_TryGetManagedBuiltInReplacement_UnityEngine_Material_UnityEngine_Material__UnityEngine_Shader__"></a> TryGetManagedBuiltInReplacement\(Material, out Material, out Shader\)

元Material（Material VariantやPackage内の読取専用Material）を、対数Shaderの管理Material
（Assets/Radial配下の写し）へ置き換え済みかを返します。参照は写しへ差し替わっているので、
一覧では元Materialの行を対数として数えます。

```csharp
public static bool TryGetManagedBuiltInReplacement(Material original, out Material managed, out Shader radialShader)
```

#### 引数（Parameters）

`original` Material

`managed` Material

`radialShader` Shader

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_TryGetManagedDiagnostic_UnityEngine_Material_UnityEngine_Material__UnityEngine_Shader__System_String__"></a> TryGetManagedDiagnostic\(Material, out Material, out Shader, out string\)

元Materialに対応する管理診断Materialを返します。Project走査では元と管理物を
二重計上せず、元Materialの行を診断状態として表示するために使用します。

```csharp
public static bool TryGetManagedDiagnostic(Material original, out Material managed, out Shader originalShader, out string failureReason)
```

#### 引数（Parameters）

`original` Material

`managed` Material

`originalShader` Shader

`failureReason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniMaterialShaderSwitchService_TryGetManagedReplacementSource_UnityEngine_Material_UnityEngine_Material__"></a> TryGetManagedReplacementSource\(Material, out Material\)

管理Material（読取専用MaterialやVariantの代わりに参照させた写し）なら、その元Materialを返します。
管理Materialは生成物の配下にありますが、元はGUID manifestではなく台帳で引きます。

```csharp
public static bool TryGetManagedReplacementSource(Material managed, out Material original)
```

#### 引数（Parameters）

`managed` Material

`original` Material

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
