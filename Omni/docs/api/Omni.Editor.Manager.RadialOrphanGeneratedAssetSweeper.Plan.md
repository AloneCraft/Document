# <a id="Omni_Editor_Manager_RadialOrphanGeneratedAssetSweeper_Plan"></a> Class RadialOrphanGeneratedAssetSweeper.Plan

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

```csharp
public sealed class RadialOrphanGeneratedAssetSweeper.Plan
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialOrphanGeneratedAssetSweeper.Plan](Omni.Editor.Manager.RadialOrphanGeneratedAssetSweeper.Plan.md)

## フィールド（Fields）

### <a id="Omni_Editor_Manager_RadialOrphanGeneratedAssetSweeper_Plan_Items"></a> Items

```csharp
public readonly List<RadialOrphanGeneratedAssetSweeper.Item> Items
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[RadialOrphanGeneratedAssetSweeper](Omni.Editor.Manager.RadialOrphanGeneratedAssetSweeper.md).[Item](Omni.Editor.Manager.RadialOrphanGeneratedAssetSweeper.Item.md)\>

### <a id="Omni_Editor_Manager_RadialOrphanGeneratedAssetSweeper_Plan_ManifestEntriesToRemove"></a> ManifestEntriesToRemove

生成物も元も消えたGUID manifestのエントリです。

```csharp
public readonly List<string> ManifestEntriesToRemove
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Editor_Manager_RadialOrphanGeneratedAssetSweeper_Plan_SkipReason"></a> SkipReason

実行しない理由。null なら実行できます。

```csharp
public string SkipReason
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_RadialOrphanGeneratedAssetSweeper_Plan_StoreRecordsToRemove"></a> StoreRecordsToRemove

元Materialが消えた台帳の記録数（ファイルを伴わないもの）です。

```csharp
public int StoreRecordsToRemove
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_Editor_Manager_RadialOrphanGeneratedAssetSweeper_Plan_Count_Omni_Editor_Manager_RadialOrphanGeneratedAssetSweeper_Decision_"></a> Count\(Decision\)

```csharp
public int Count(RadialOrphanGeneratedAssetSweeper.Decision decision)
```

#### 引数（Parameters）

`decision` [RadialOrphanGeneratedAssetSweeper](Omni.Editor.Manager.RadialOrphanGeneratedAssetSweeper.md).[Decision](Omni.Editor.Manager.RadialOrphanGeneratedAssetSweeper.Decision.md)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)
