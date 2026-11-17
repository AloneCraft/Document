# <a id="Omni_Celestial_CelestialCatalogValidationCode"></a> Enum CelestialCatalogValidationCode

Namespace: [Omni.Celestial](Omni.Celestial.md)  
Assembly: Omni.Celestial.Core.dll  

天体カタログを不変Snapshotへ変換する前に検出した不正値の種別です。

```csharp
public enum CelestialCatalogValidationCode
```

## フィールド（Fields）

`DuplicateKey = 5` 

天体キーが重複しています。



`EccentricityOutOfRange = 20` 

離心率が0以上1未満ではありません。



`EmptyCatalog = 2` 

天体レコードがありません。



`InvalidAxialTilt = 11` 

自転軸傾斜角の数値表現を解析できません。



`InvalidDiameter = 7` 

直径の数値表現を解析できません。



`InvalidDisplayName = 6` 

表示名が空、または正規化されていません。



`InvalidEccentricity = 19` 

離心率の数値表現を解析できません。



`InvalidKey = 4` 

天体キーが空、または正規化されていません。



`InvalidMass = 9` 

質量の数値表現を解析できません。



`InvalidOrbitCenter = 12` 

軌道中心天体キーが空、または正規化されていません。



`InvalidOrbitalInclination = 21` 

軌道傾斜角の数値表現を解析できません。



`InvalidOrbitalPeriod = 17` 

軌道周期の数値表現を解析できません。



`InvalidRevision = 1` 

カタログ改訂番号が1未満です。



`InvalidSemiMajorAxis = 15` 

軌道長半径の数値表現を解析できません。



`NonPositiveDiameter = 8` 

直径が正ではありません。



`NonPositiveMass = 10` 

質量が正ではありません。



`NonPositiveOrbitalPeriod = 18` 

軌道周期が正ではありません。



`NonPositiveSemiMajorAxis = 16` 

軌道長半径が正ではありません。



`None = 0` 

不正値がありません。



`NullBody = 3` 

天体レコード自体がnullです。



`SelfOrbitCenter = 14` 

天体自身を軌道中心に指定しています。



`UnknownOrbitCenter = 13` 

軌道中心天体がカタログ内に存在しません。
