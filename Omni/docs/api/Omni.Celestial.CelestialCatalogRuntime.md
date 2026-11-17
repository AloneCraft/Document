# <a id="Omni_Celestial_CelestialCatalogRuntime"></a> Class CelestialCatalogRuntime

Namespace: [Omni.Celestial](Omni.Celestial.md)  
Assembly: Omni.Celestial.Core.dll  

Resourcesに置いた共有CelestialCatalogAssetを、検証済み不変Snapshotとして提供します。
GalaxyとSaturnは同じAuthoring assetを参照し、物理定数を個別の静的表へ複製しません。

```csharp
public static class CelestialCatalogRuntime
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[CelestialCatalogRuntime](Omni.Celestial.CelestialCatalogRuntime.md)

## フィールド（Fields）

### <a id="Omni_Celestial_CelestialCatalogRuntime_ResourcePath"></a> ResourcePath

Playerで使うResources相対パスです。

```csharp
public const string ResourcePath = "Omni/CelestialCatalog"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## プロパティ（Properties）

### <a id="Omni_Celestial_CelestialCatalogRuntime_AssetPath"></a> AssetPath

Editor Builderが同一GUIDを維持して読み書きするassetパスです。

```csharp
public static string AssetPath { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Celestial_CelestialCatalogRuntime_GetSnapshotOrThrow"></a> GetSnapshotOrThrow\(\)

共有Authoring assetからSnapshotを取得し、失敗時は原因を含む例外を送出します。

```csharp
public static CelestialCatalogSnapshot GetSnapshotOrThrow()
```

#### 戻り値（Returns）

 [CelestialCatalogSnapshot](Omni.Celestial.CelestialCatalogSnapshot.md)

検証済みの共有Celestial Snapshot。

### <a id="Omni_Celestial_CelestialCatalogRuntime_InvalidateCacheForEditor"></a> InvalidateCacheForEditor\(\)

Editor Builderが同一revisionのassetを更新した直後に、次回読み込みを強制します。

```csharp
public static void InvalidateCacheForEditor()
```

### <a id="Omni_Celestial_CelestialCatalogRuntime_TryGetSnapshot_Omni_Celestial_CelestialCatalogSnapshot__System_String__"></a> TryGetSnapshot\(out CelestialCatalogSnapshot, out string\)

共有Authoring assetから検証済みSnapshotを取得します。
同一asset・同一revisionでは前回の不変Snapshotを再利用します。

```csharp
public static bool TryGetSnapshot(out CelestialCatalogSnapshot snapshot, out string error)
```

#### 引数（Parameters）

`snapshot` [CelestialCatalogSnapshot](Omni.Celestial.CelestialCatalogSnapshot.md)

成功時の共有Celestial Snapshot。

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

失敗時の日本語エラー。成功時は空文字。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

assetと内容が有効な場合はtrue。
