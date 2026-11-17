# <a id="Omni_Celestial_CelestialCatalogAsset"></a> Class CelestialCatalogAsset

Namespace: [Omni.Celestial](Omni.Celestial.md)  
Assembly: Omni.Celestial.Core.dll  

天体の物理定数を保持する唯一のAuthoring Source of Truthです。

<p>
SaturnやGalaxyのPrefab・Scene・描画用データは半径、質量、軌道を複製してはなりません。
起動時には必ず<xref href="Omni.Celestial.CelestialCatalogAsset.TryCreateSnapshot(Omni.Celestial.CelestialCatalogSnapshot%40%2cOmni.Celestial.CelestialCatalogValidationResult%40)" data-throw-if-not-resolved="false"></xref>で検証済みの
<xref href="Omni.Celestial.CelestialCatalogSnapshot" data-throw-if-not-resolved="false"></xref>へ変換してから利用してください。
</p>

```csharp
[CreateAssetMenu(fileName = "CelestialCatalog", menuName = "Omni/Celestial/Catalog")]
public sealed class CelestialCatalogAsset : ScriptableObject
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
ScriptableObject ← 
[CelestialCatalogAsset](Omni.Celestial.CelestialCatalogAsset.md)

## プロパティ（Properties）

### <a id="Omni_Celestial_CelestialCatalogAsset_Revision"></a> Revision

内容を意図して更新したときに増やすAuthoring改訂番号です。

```csharp
public int Revision { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_Celestial_CelestialCatalogAsset_ConfigureForEditor_System_Int32_Omni_Celestial_CelestialBodyAuthoring___"></a> ConfigureForEditor\(int, CelestialBodyAuthoring\[\]\)

BuilderとEditModeテストだけが使用する、Authoringレコードの原子的な差し替え口です。
入力配列と各レコードを複製するため、呼び出し後の外部変更はAssetに影響しません。

```csharp
public void ConfigureForEditor(int revision, CelestialBodyAuthoring[] bodies)
```

#### 引数（Parameters）

`revision` [int](https://learn.microsoft.com/dotnet/api/system.int32)

新しい改訂番号。

`bodies` [CelestialBodyAuthoring](Omni.Celestial.CelestialBodyAuthoring.md)\[\]

差し替える天体レコード。

### <a id="Omni_Celestial_CelestialCatalogAsset_CreateSnapshotOrThrow"></a> CreateSnapshotOrThrow\(\)

現在の内容からSnapshotを作成し、失敗時は原因を含む例外を送出します。

```csharp
public CelestialCatalogSnapshot CreateSnapshotOrThrow()
```

#### 戻り値（Returns）

 [CelestialCatalogSnapshot](Omni.Celestial.CelestialCatalogSnapshot.md)

検証済み不変Snapshot。

#### 例外（Exceptions）

 [InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception)

Authoring内容が不正な場合。

### <a id="Omni_Celestial_CelestialCatalogAsset_TryCreateSnapshot_Omni_Celestial_CelestialCatalogSnapshot__Omni_Celestial_CelestialCatalogValidationResult__"></a> TryCreateSnapshot\(out CelestialCatalogSnapshot, out CelestialCatalogValidationResult\)

現在のAuthoring内容を検証済み不変Snapshotへ変換します。

```csharp
public bool TryCreateSnapshot(out CelestialCatalogSnapshot snapshot, out CelestialCatalogValidationResult validation)
```

#### 引数（Parameters）

`snapshot` [CelestialCatalogSnapshot](Omni.Celestial.CelestialCatalogSnapshot.md)

成功時のSnapshot。失敗時はnull。

`validation` [CelestialCatalogValidationResult](Omni.Celestial.CelestialCatalogValidationResult.md)

全検証エラー。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

全入力が有効な場合はtrue。

### <a id="Omni_Celestial_CelestialCatalogAsset_Validate"></a> Validate\(\)

現在のAuthoring内容の検証だけを実行します。

```csharp
public CelestialCatalogValidationResult Validate()
```

#### 戻り値（Returns）

 [CelestialCatalogValidationResult](Omni.Celestial.CelestialCatalogValidationResult.md)

検証結果。
