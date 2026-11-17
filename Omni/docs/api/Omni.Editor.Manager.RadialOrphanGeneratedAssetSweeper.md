# <a id="Omni_Editor_Manager_RadialOrphanGeneratedAssetSweeper"></a> Class RadialOrphanGeneratedAssetSweeper

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

元のShader／Materialが消えた <code>Assets/Radial</code> の生成物（孤児）を、対数レンダリングへの
切替完了後にOSのごみ箱へ移します。

```csharp
public static class RadialOrphanGeneratedAssetSweeper
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialOrphanGeneratedAssetSweeper](Omni.Editor.Manager.RadialOrphanGeneratedAssetSweeper.md)

## 補足（Remarks）

<p>
<b>許可リスト方式。</b>旧コピーMaterial（Project／Packages／User の <code>*_Materials</code>）、
User生成Shader、BRG sidecar／BRG Shader、管理Material（ManagedBuiltIn／Diagnostic）だけを
対象にします。Bake、Resources、Mappings、PlanetSurfaceBuild などには触れません。
</p>
<p>
<b>削除は元の消失を証明できたときだけ。</b>判定できないもの（コンテナはあるが名前が一致
しない、Package自体が見つからない等）は残して報告します。
</p>
<p>
<b>参照中は残す。</b>候補以外のアセット、ロード済みScene（未保存状態を含む）、Prefab Stage
から参照される候補は削除せず、参照元と一緒に報告します。参照中の孤児は
<xref href="Omni.Converter.RadialOrphanSourceRestorer" data-throw-if-not-resolved="false"></xref> で元を作り直せる場合があります。
候補どうしの参照は数えないため、孤児Materialだけが使う孤児Shaderはまとめて削除されます。
</p>

## プロパティ（Properties）

### <a id="Omni_Editor_Manager_RadialOrphanGeneratedAssetSweeper_LastResult"></a> LastResult

直近の実行結果です。Manager上部の表示に使います。

```csharp
public static RadialOrphanGeneratedAssetSweeper.Result LastResult { get; }
```

#### 値（Property Value）

 [RadialOrphanGeneratedAssetSweeper](Omni.Editor.Manager.RadialOrphanGeneratedAssetSweeper.md).[Result](Omni.Editor.Manager.RadialOrphanGeneratedAssetSweeper.Result.md)

## メソッド（Methods）

### <a id="Omni_Editor_Manager_RadialOrphanGeneratedAssetSweeper_CollectPlan"></a> CollectPlan\(\)

何も変更せずに判定結果を返します。

```csharp
public static RadialOrphanGeneratedAssetSweeper.Plan CollectPlan()
```

#### 戻り値（Returns）

 [RadialOrphanGeneratedAssetSweeper](Omni.Editor.Manager.RadialOrphanGeneratedAssetSweeper.md).[Plan](Omni.Editor.Manager.RadialOrphanGeneratedAssetSweeper.Plan.md)

### <a id="Omni_Editor_Manager_RadialOrphanGeneratedAssetSweeper_Execute_Omni_Editor_Manager_RadialOrphanGeneratedAssetSweeper_Plan_"></a> Execute\(Plan\)

<xref href="Omni.Editor.Manager.RadialOrphanGeneratedAssetSweeper.Decision.Delete" data-throw-if-not-resolved="false"></xref> の生成物をごみ箱へ移し、削除に成功した分だけ
GUID manifest、台帳、BRG manifest から記録を取り除きます。

```csharp
public static RadialOrphanGeneratedAssetSweeper.Result Execute(RadialOrphanGeneratedAssetSweeper.Plan plan)
```

#### 引数（Parameters）

`plan` [RadialOrphanGeneratedAssetSweeper](Omni.Editor.Manager.RadialOrphanGeneratedAssetSweeper.md).[Plan](Omni.Editor.Manager.RadialOrphanGeneratedAssetSweeper.Plan.md)

#### 戻り値（Returns）

 [RadialOrphanGeneratedAssetSweeper](Omni.Editor.Manager.RadialOrphanGeneratedAssetSweeper.md).[Result](Omni.Editor.Manager.RadialOrphanGeneratedAssetSweeper.Result.md)

### <a id="Omni_Editor_Manager_RadialOrphanGeneratedAssetSweeper_RunAfterRadialSwitch"></a> RunAfterRadialSwitch\(\)

対数レンダリングへの切替が完了した直後に呼びます。失敗しても例外を外へ出さず、
切替結果を変えません。

```csharp
public static RadialOrphanGeneratedAssetSweeper.Result RunAfterRadialSwitch()
```

#### 戻り値（Returns）

 [RadialOrphanGeneratedAssetSweeper](Omni.Editor.Manager.RadialOrphanGeneratedAssetSweeper.md).[Result](Omni.Editor.Manager.RadialOrphanGeneratedAssetSweeper.Result.md)
