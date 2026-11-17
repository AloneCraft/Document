# <a id="Omni_Celestial_SaturnRingSnapshotProvider"></a> Class SaturnRingSnapshotProvider

Namespace: [Omni.Celestial](Omni.Celestial.md)  
Assembly: Omni.Celestial.Core.dll  

Resourcesに置いた唯一のSaturnリングAuthoring assetから不変物理Snapshotを読みます。
GalaxyはSaturn Runtimeの具体型を参照せず、このproviderを通じてリング寸法を取得します。
Authoring assetとその型は開発環境（Saturn Legacy Scenario）にだけあり、配布物には含みません。
無い環境では<xref href="Omni.Celestial.SaturnRingSnapshotProvider.TryGetSnapshot(Omni.Celestial.SaturnRingSnapshot%40%2cSystem.String%40)" data-throw-if-not-resolved="false"></xref>が理由付きでfalseを返します。

```csharp
public static class SaturnRingSnapshotProvider
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[SaturnRingSnapshotProvider](Omni.Celestial.SaturnRingSnapshotProvider.md)

## フィールド（Fields）

### <a id="Omni_Celestial_SaturnRingSnapshotProvider_ResourcePath"></a> ResourcePath

Playerで使うResources相対パスです。

```csharp
public const string ResourcePath = "Omni/SaturnRingDefinition"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Celestial_SaturnRingSnapshotProvider_GetSnapshotOrThrow"></a> GetSnapshotOrThrow\(\)

現在のAuthoring assetからSnapshotを取得し、失敗時は原因を含む例外を送出します。

```csharp
public static SaturnRingSnapshot GetSnapshotOrThrow()
```

#### 戻り値（Returns）

 [SaturnRingSnapshot](Omni.Celestial.SaturnRingSnapshot.md)

検証済みのリング物理Snapshot。

### <a id="Omni_Celestial_SaturnRingSnapshotProvider_TryGetSnapshot_Omni_Celestial_SaturnRingSnapshot__System_String__"></a> TryGetSnapshot\(out SaturnRingSnapshot, out string\)

現在のAuthoring assetから検証済み物理Snapshotを取得します。

```csharp
public static bool TryGetSnapshot(out SaturnRingSnapshot snapshot, out string error)
```

#### 引数（Parameters）

`snapshot` [SaturnRingSnapshot](Omni.Celestial.SaturnRingSnapshot.md)

成功時のリング物理Snapshot。

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

失敗時の日本語エラー。成功時は空文字。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

assetと物理値が有効な場合はtrue。
