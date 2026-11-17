# <a id="Omni_Celestial_CelestialCatalogValidationResult"></a> Class CelestialCatalogValidationResult

Namespace: [Omni.Celestial](Omni.Celestial.md)  
Assembly: Omni.Celestial.Core.dll  

カタログ検証の不変結果です。エラー配列は外部から変更できません。

```csharp
public sealed class CelestialCatalogValidationResult
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[CelestialCatalogValidationResult](Omni.Celestial.CelestialCatalogValidationResult.md)

## プロパティ（Properties）

### <a id="Omni_Celestial_CelestialCatalogValidationResult_IsValid"></a> IsValid

エラーがない場合はtrueです。

```csharp
public bool IsValid { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Celestial_CelestialCatalogValidationResult_Issues"></a> Issues

検出したエラーの不変一覧です。

```csharp
public ReadOnlyCollection<CelestialCatalogValidationIssue> Issues { get; }
```

#### 値（Property Value）

 [ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection\-1)<[CelestialCatalogValidationIssue](Omni.Celestial.CelestialCatalogValidationIssue.md)\>

## メソッド（Methods）

### <a id="Omni_Celestial_CelestialCatalogValidationResult_Contains_Omni_Celestial_CelestialCatalogValidationCode_"></a> Contains\(CelestialCatalogValidationCode\)

指定したエラー種別を含むかを返します。

```csharp
public bool Contains(CelestialCatalogValidationCode code)
```

#### 引数（Parameters）

`code` [CelestialCatalogValidationCode](Omni.Celestial.CelestialCatalogValidationCode.md)

検索するエラー種別。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

該当するエラーがある場合はtrue。

### <a id="Omni_Celestial_CelestialCatalogValidationResult_ToDisplayString"></a> ToDisplayString\(\)

ログやテスト失敗メッセージに使える不変の表示文字列を返します。

```csharp
public string ToDisplayString()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

有効時は短い成功文、それ以外は全エラーを改行結合した文字列。
