# <a id="Omni_Converter_RadialOrphanSourceRestorer"></a> Class RadialOrphanSourceRestorer

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

元アセットが削除された生成マテリアル（孤児）から、元マテリアルを作り直します。

```csharp
public static class RadialOrphanSourceRestorer
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialOrphanSourceRestorer](Omni.Converter.RadialOrphanSourceRestorer.md)

## 補足（Remarks）

<p>
<b>解決する問題。</b>生成後に元マテリアルを削除すると、生成物だけがシーンに残り
「標準レンダリングへ戻せない」状態になります。<xref href="Omni.Converter.RadialSourceResolver" data-throw-if-not-resolved="false"></xref> の
3経路（マニフェストの guid+localId / guid+名前 / パス規則からの逆算）は
どれも「既にある元アセットを探す」ものなので、元が消えていると全滅します。
</p>
<p>
<b>なぜバックフィルでは直らないか。</b>
<xref href="Omni.Converter.RadialSourceResolver.BackfillSourceIds" data-throw-if-not-resolved="false"></xref> は
<xref href="Omni.Converter.OmniGuidManifest.EnumeratePaths" data-throw-if-not-resolved="false"></xref>（＝既存エントリ）だけを回ります。
マニフェストにエントリ自体が無い孤児は<b>一度も訪問されません</b>。
実測（CameraCombinationVerification）では、生成 .mat 394件のうち孤児は1件でしたが、
それがシーンの101スロットから参照されていたため未解決100件として現れていました。
</p>
<p>
<b>復元内容が一意に決まる理由。</b>生成マテリアルは元マテリアルからプロパティを
コピーして作られており、そのシェーダーは「元シェーダーの生成版」です。生成シェーダーの
マニフェストエントリから元シェーダーを引けるので、<code>元シェーダー + 生成物のプロパティ</code>
で元マテリアルを再構成できます。推測は入りません。
</p>
<p>
どこからも参照されていない孤児は、対数レンダリングへの切替完了後に
<code>RadialOrphanGeneratedAssetSweeper</code>（Omni.Manager）がごみ箱へ移します。
この復元が意味を持つのは、Scene等から参照されていて残された孤児です。
</p>
<p>
アセットを新規作成するため、必ず確認ダイアログを挟みます（ベイクと違い、間違えると
意図しないファイルが増えます）。
</p>

## メソッド（Methods）

### <a id="Omni_Converter_RadialOrphanSourceRestorer_CollectPlans"></a> CollectPlans\(\)

マニフェストにエントリの無い生成マテリアルを集め、復元可否を判定します。

```csharp
public static List<RadialOrphanSourceRestorer.Plan> CollectPlans()
```

#### 戻り値（Returns）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[RadialOrphanSourceRestorer](Omni.Converter.RadialOrphanSourceRestorer.md).[Plan](Omni.Converter.RadialOrphanSourceRestorer.Plan.md)\>

### <a id="Omni_Converter_RadialOrphanSourceRestorer_Run"></a> Run\(\)

```csharp
public static void Run()
```
