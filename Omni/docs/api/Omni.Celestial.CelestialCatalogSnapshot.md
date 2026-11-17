# <a id="Omni_Celestial_CelestialCatalogSnapshot"></a> Class CelestialCatalogSnapshot

Namespace: [Omni.Celestial](Omni.Celestial.md)  
Assembly: Omni.Celestial.Core.dll  

<xref href="Omni.Celestial.CelestialCatalogAsset" data-throw-if-not-resolved="false"></xref>から一度だけ生成する、検証済みの読み取り専用カタログです。
Unity Objectを含まず、同じAuthoring内容から必ず同じ<xref href="Omni.Celestial.CelestialCatalogSnapshot.Fingerprint" data-throw-if-not-resolved="false"></xref>を生成します。

```csharp
public sealed class CelestialCatalogSnapshot
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[CelestialCatalogSnapshot](Omni.Celestial.CelestialCatalogSnapshot.md)

## フィールド（Fields）

### <a id="Omni_Celestial_CelestialCatalogSnapshot_FingerprintSchemaVersion"></a> FingerprintSchemaVersion

content fingerprintの正規化形式の版です。

```csharp
public const int FingerprintSchemaVersion = 2
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="Omni_Celestial_CelestialCatalogSnapshot_Bodies"></a> Bodies

キー昇順に正規化された天体一覧です。

```csharp
public ReadOnlyCollection<CelestialBodySnapshot> Bodies { get; }
```

#### 値（Property Value）

 [ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection\-1)<[CelestialBodySnapshot](Omni.Celestial.CelestialBodySnapshot.md)\>

### <a id="Omni_Celestial_CelestialCatalogSnapshot_Count"></a> Count

検証済み天体数です。

```csharp
public int Count { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Celestial_CelestialCatalogSnapshot_Fingerprint"></a> Fingerprint

カタログ内容を表すSHA-256 hex文字列です。

```csharp
public string Fingerprint { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Celestial_CelestialCatalogSnapshot_Revision"></a> Revision

Authoring側で明示した改訂番号です。

```csharp
public int Revision { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_Celestial_CelestialCatalogSnapshot_GetAt_System_Int32_"></a> GetAt\(int\)

添字で天体Snapshotを取得します。

```csharp
public CelestialBodySnapshot GetAt(int index)
```

#### 引数（Parameters）

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

キー昇順の添字。

#### 戻り値（Returns）

 [CelestialBodySnapshot](Omni.Celestial.CelestialBodySnapshot.md)

天体Snapshot。

#### 例外（Exceptions）

 [ArgumentOutOfRangeException](https://learn.microsoft.com/dotnet/api/system.argumentoutofrangeexception)

添字が範囲外の場合。

### <a id="Omni_Celestial_CelestialCatalogSnapshot_TryCreate_System_Int32_System_Collections_Generic_IReadOnlyList_Omni_Celestial_CelestialBodyAuthoring__Omni_Celestial_CelestialCatalogSnapshot__Omni_Celestial_CelestialCatalogValidationResult__"></a> TryCreate\(int, IReadOnlyList<CelestialBodyAuthoring\>, out CelestialCatalogSnapshot, out CelestialCatalogValidationResult\)

Authoringレコードを検証し、完全に有効なときだけ不変Snapshotを作成します。

```csharp
public static bool TryCreate(int revision, IReadOnlyList<CelestialBodyAuthoring> bodyAuthoring, out CelestialCatalogSnapshot snapshot, out CelestialCatalogValidationResult validation)
```

#### 引数（Parameters）

`revision` [int](https://learn.microsoft.com/dotnet/api/system.int32)

Authoring改訂番号。1以上が必要です。

`bodyAuthoring` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[CelestialBodyAuthoring](Omni.Celestial.CelestialBodyAuthoring.md)\>

天体Authoringレコード。

`snapshot` [CelestialCatalogSnapshot](Omni.Celestial.CelestialCatalogSnapshot.md)

成功時のSnapshot。失敗時はnull。

`validation` [CelestialCatalogValidationResult](Omni.Celestial.CelestialCatalogValidationResult.md)

失敗理由を含む検証結果。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

検証に成功しSnapshotを生成した場合はtrue。

### <a id="Omni_Celestial_CelestialCatalogSnapshot_TryGet_System_String_Omni_Celestial_CelestialBodySnapshot__"></a> TryGet\(string, out CelestialBodySnapshot\)

キーで天体Snapshotを取得します。

```csharp
public bool TryGet(string key, out CelestialBodySnapshot body)
```

#### 引数（Parameters）

`key` [string](https://learn.microsoft.com/dotnet/api/system.string)

大文字小文字を区別する天体キー。

`body` [CelestialBodySnapshot](Omni.Celestial.CelestialBodySnapshot.md)

見つかったSnapshot。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

存在する場合はtrue。
