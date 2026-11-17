# <a id="Omni_Converter_RadialSceneMaterialState"></a> Class RadialSceneMaterialState

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

シーン内の Renderer / Terrain / DecalProjector を走査して、適用・復元の可否を判断します。

```csharp
public static class RadialSceneMaterialState
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialSceneMaterialState](Omni.Converter.RadialSceneMaterialState.md)

## メソッド（Methods）

### <a id="Omni_Converter_RadialSceneMaterialState_Describe_Omni_Converter_RadialSceneState__"></a> Describe\(in RadialSceneState\)

適用状態を、PostValidation失敗時に原因を失わない形式で説明します。

```csharp
public static string Describe(in RadialSceneState state)
```

#### 引数（Parameters）

`state` [RadialSceneState](Omni.Converter.RadialSceneState.md)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_RadialSceneMaterialState_Describe_Omni_Converter_RadialSceneMaterialState_RevertResult__"></a> Describe\(in RevertResult\)

復元結果を人間向けの文字列にします。

```csharp
public static string Describe(in RadialSceneMaterialState.RevertResult r)
```

#### 引数（Parameters）

`r` [RadialSceneMaterialState](Omni.Converter.RadialSceneMaterialState.md).[RevertResult](Omni.Converter.RadialSceneMaterialState.RevertResult.md)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_RadialSceneMaterialState_EnumerateDecalProjectors"></a> EnumerateDecalProjectors\(\)

シーンのDecal Projectorを、Rendererと同じ永続性規則で列挙します。
DecalProjectorはRenderer派生ではないため、明示的に含めないとRadial生成Materialが
存在しても元の非対応ShaderGraphを描画し続けます。

```csharp
public static IEnumerable<DecalProjector> EnumerateDecalProjectors()
```

#### 戻り値（Returns）

 [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<DecalProjector\>

### <a id="Omni_Converter_RadialSceneMaterialState_EnumerateRenderers"></a> EnumerateRenderers\(\)

シーンの Renderer を列挙します。

<p>
<b>非アクティブを含めます。</b>既定の <code>FindObjectsByType</code> は非アクティブを除外するため、
従来は「適用時に非アクティブだった物」が Revert でも漏れ、生成マテリアルを
持ったまま取り残されていました。
</p>
<p>
<b>Prefab Stage は除外します。</b>Prefab を開いていると走査がその中身も返し、
書き込むとプレハブアセット本体が書き換わってしまいます。
</p>

```csharp
public static IEnumerable<Renderer> EnumerateRenderers()
```

#### 戻り値（Returns）

 [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<Renderer\>

### <a id="Omni_Converter_RadialSceneMaterialState_EnumerateTerrains"></a> EnumerateTerrains\(\)

```csharp
public static IEnumerable<Terrain> EnumerateTerrains()
```

#### 戻り値（Returns）

 [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<Terrain\>

### <a id="Omni_Converter_RadialSceneMaterialState_FindBrokenPrefabMaterialSlots"></a> FindBrokenPrefabMaterialSlots\(\)

プレハブインスタンスの Renderer で、対応するプレハブ側は非 null なのにインスタンス側が
null になっているスロットを探します。

<p>
<xref href="Omni.Converter.RadialSceneMaterialState.Revert(System.Boolean)" data-throw-if-not-resolved="false"></xref> 自体はもう他インスタンスを巻き添えにしませんが、それでも将来
別の経路（Inspector操作・別ツール等）で同種の破損が起きたときに、保存前に気付ける
ようにするための最終チェックです。呼び出し元（<code>RadialRenderingSwitch.SwitchToUnity</code>）
が結果をログへ出します。
</p>

```csharp
public static List<string> FindBrokenPrefabMaterialSlots()
```

#### 戻り値（Returns）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Converter_RadialSceneMaterialState_IsPrefabStageOpen"></a> IsPrefabStageOpen\(\)

Prefab Stage が開いているか。開いている間は適用・復元を拒否します。

```csharp
public static bool IsPrefabStageOpen()
```

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_RadialSceneMaterialState_Revert_System_Boolean_"></a> Revert\(bool\)

シーンのマテリアルを元へ戻します。

```csharp
public static RadialSceneMaterialState.RevertResult Revert(bool dryRun)
```

#### 引数（Parameters）

`dryRun` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

true なら何も書き込まず、件数と未解決だけを返します。

#### 戻り値（Returns）

 [RadialSceneMaterialState](Omni.Converter.RadialSceneMaterialState.md).[RevertResult](Omni.Converter.RadialSceneMaterialState.RevertResult.md)

### <a id="Omni_Converter_RadialSceneMaterialState_Scan"></a> Scan\(\)

シーンの適用状態を数えます。

```csharp
public static RadialSceneState Scan()
```

#### 戻り値（Returns）

 [RadialSceneState](Omni.Converter.RadialSceneState.md)

### <a id="Omni_Converter_RadialSceneMaterialState_Scan_UnityEngine_SceneManagement_Scene_"></a> Scan\(Scene\)

指定した1つのSceneだけの適用状態を数えます（VFXは含めません）。
他のSceneが同時に開いていても、そのSceneのRenderer／Terrain／DecalProjectorだけを見ます。
「このSceneのMaterialは対数か」の判定（RadialCameraの自動付与の可否）に使います。

```csharp
public static RadialSceneState Scan(Scene scene)
```

#### 引数（Parameters）

`scene` Scene

#### 戻り値（Returns）

 [RadialSceneState](Omni.Converter.RadialSceneState.md)

### <a id="Omni_Converter_RadialSceneMaterialState_VerifyAndHealMaterialSlots_System_String_System_Collections_Generic_IReadOnlyList_System_ValueTuple_UnityEngine_Renderer_UnityEngine_Material_____"></a> VerifyAndHealMaterialSlots\(string, IReadOnlyList<\(Renderer renderer, Material\[\] intended\)\>\)

<b>暫定の安全網です。根本原因が特定・修正され、十分な期間この警告が出なくなったことが
確認できたら、この関数ごと削除して構いません。</b>
<p>
<xref href="Omni.Converter.RadialMaterialApplier.ApplyToScene" data-throw-if-not-resolved="false"></xref>・<xref href="Omni.Converter.RadialSceneMaterialState.Revert(System.Boolean)" data-throw-if-not-resolved="false"></xref>
それぞれの書き込みループ直後に、実際に書き込んだ (Renderer, 意図した値) の一覧を渡して
呼び出します。両者とも自身のロジックは解決失敗時に既存の値を保持するだけでnullを
書き込む分岐は無いことを確認済みですが、多段ネストしたプレハブ（RoomScreens_Prefab
のように同じソースプレハブを複数の兄弟インスタンスが共有する構造）では、Unity側の
プレハブオーバーライド記録機構そのものの副作用と見られる原因不明の巻き添えで、
意図した値のはずのスロットが書き込み直後に null へ変わっていることが
2026-08-02・2026-08-04、および本関数を追加するきっかけとなった再発時に確認されています。
</p>
<p>
ここでは書き込み直後に同じRendererを読み直し、意図した値と食い違うスロットを
その場で書き戻して自己修復した上で、AIによる原因調査にそのまま使える詳細度で
<xref href="UnityEngine.Debug.LogError(System.Object)" data-throw-if-not-resolved="false"></xref> します（保存されるまで誰も気付かない、という事態を防ぐため）。
</p>

```csharp
public static void VerifyAndHealMaterialSlots(string context, IReadOnlyList<(Renderer renderer, Material[] intended)> written)
```

#### 引数（Parameters）

`context` [string](https://learn.microsoft.com/dotnet/api/system.string)

呼び出し元の識別（例: "ApplyToScene (Unity→Radial)"）。ログに含めます。

`written` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<\(Renderer [renderer](https://learn.microsoft.com/dotnet/api/system.valuetuple\-unityengine.renderer,unityengine.material\[\]\-.renderer), Material\[\] [intended](https://learn.microsoft.com/dotnet/api/system.valuetuple\-unityengine.renderer,unityengine.material\[\]\-.intended)\)\>

今回書き込んだ (Renderer, 意図した sharedMaterials) の一覧。
