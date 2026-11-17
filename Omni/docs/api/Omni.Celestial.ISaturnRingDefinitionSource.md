# <a id="Omni_Celestial_ISaturnRingDefinitionSource"></a> Interface ISaturnRingDefinitionSource

Namespace: [Omni.Celestial](Omni.Celestial.md)  
Assembly: Omni.Celestial.Core.dll  

Saturn RuntimeのAuthoring assetをCelestial層へ中立的に公開する境界です。
Galaxyは具体的なSaturn型ではなく、このinterface経由で不変物理Snapshotを取得します。

```csharp
public interface ISaturnRingDefinitionSource
```

## メソッド（Methods）

### <a id="Omni_Celestial_ISaturnRingDefinitionSource_TryCreateSnapshot_Omni_Celestial_SaturnRingSnapshot__System_String__"></a> TryCreateSnapshot\(out SaturnRingSnapshot, out string\)

現在のAuthoring値から物理Snapshotを検証付きで作成します。

```csharp
bool TryCreateSnapshot(out SaturnRingSnapshot snapshot, out string error)
```

#### 引数（Parameters）

`snapshot` [SaturnRingSnapshot](Omni.Celestial.SaturnRingSnapshot.md)

成功時の物理Snapshot。

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

失敗時の日本語エラー。成功時は空文字。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

物理寸法が有効な場合はtrue。
