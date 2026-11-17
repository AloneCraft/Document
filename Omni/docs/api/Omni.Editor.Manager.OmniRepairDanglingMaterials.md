# <a id="Omni_Editor_Manager_OmniRepairDanglingMaterials"></a> Class OmniRepairDanglingMaterials

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

シーン内の壊れたマテリアル参照（PrefabInstanceのオーバーライドが実体の無いGUIDを
指しているケース）を、プレハブ本来のデフォルトマテリアルへ安全に戻します。

<p>
2026-08-01、<code>Assets/Radial/</code> を削除して再生成した際にGUIDが変わり、
TerminalScene.unity の "Center Floor Trim" 等、約20オブジェクト・約120箇所の
マテリアル参照が永久にダングリングした事故の復旧手段として用意した。
</p>
<p>
<xref href="UnityEditor.PrefabUtility.RevertPropertyOverride(UnityEditor.SerializedProperty%2cUnityEditor.InteractionMode)" data-throw-if-not-resolved="false"></xref> は使いません。多段ネストした
プレハブ（内側のプレハブ自身の既定値と外側のプレハブインスタンス側のオーバーライドが
別々の階層に記録されている場合）では、処理対象ではない兄弟インスタンスのスロットを
巻き添えで空にすることが実際に確認されています（詳細は
<xref href="Omni.Converter.RadialSceneMaterialState.Revert(System.Boolean)" data-throw-if-not-resolved="false"></xref> 直下のコメント参照）。同じ理由で
本クラスも <xref href="UnityEditor.PrefabUtility.GetCorrespondingObjectFromSource%60%601(%60%600)" data-throw-if-not-resolved="false"></xref> でプレハブ側の
実効デフォルト値を読み、<xref href="UnityEngine.Renderer.sharedMaterials" data-throw-if-not-resolved="false"></xref> への通常の配列代入で
書き戻します。
</p>

```csharp
public static class OmniRepairDanglingMaterials
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniRepairDanglingMaterials](Omni.Editor.Manager.OmniRepairDanglingMaterials.md)

## メソッド（Methods）

### <a id="Omni_Editor_Manager_OmniRepairDanglingMaterials_RepairAll"></a> RepairAll\(\)

現在開いているシーンに対して修復を実行します。バッチドライバー等、
複数シーンを連続処理する呼び出し元向けに <xref href="UnityEditor.EditorApplication.Exit(System.Int32)" data-throw-if-not-resolved="false"></xref> を
呼ばない形で公開しています。

```csharp
public static (int repaired, int skipped) RepairAll()
```

#### 戻り値（Returns）

 \([int](https://learn.microsoft.com/dotnet/api/system.int32) [repaired](https://learn.microsoft.com/dotnet/api/system.valuetuple\-system.int32,system.int32\-.repaired), [int](https://learn.microsoft.com/dotnet/api/system.int32) [skipped](https://learn.microsoft.com/dotnet/api/system.valuetuple\-system.int32,system.int32\-.skipped)\)

### <a id="Omni_Editor_Manager_OmniRepairDanglingMaterials_Run"></a> Run\(\)

```csharp
public static void Run()
```
