# <a id="Omni_Celestial_CelestialCatalogValidationIssue"></a> Struct CelestialCatalogValidationIssue

Namespace: [Omni.Celestial](Omni.Celestial.md)  
Assembly: Omni.Celestial.Core.dll  

1件のカタログ検証エラーです。<xref href="Omni.Celestial.CelestialCatalogValidationIssue.BodyIndex" data-throw-if-not-resolved="false"></xref>が-1の場合はカタログ全体のエラーです。

```csharp
public readonly struct CelestialCatalogValidationIssue
```

## コンストラクター（Constructors）

### <a id="Omni_Celestial_CelestialCatalogValidationIssue__ctor_System_Int32_System_String_Omni_Celestial_CelestialCatalogValidationCode_System_String_"></a> CelestialCatalogValidationIssue\(int, string, CelestialCatalogValidationCode, string\)

検証エラーを構築します。

```csharp
public CelestialCatalogValidationIssue(int bodyIndex, string bodyKey, CelestialCatalogValidationCode code, string message)
```

#### 引数（Parameters）

`bodyIndex` [int](https://learn.microsoft.com/dotnet/api/system.int32)

Authoring配列上の添字。全体エラーでは-1。

`bodyKey` [string](https://learn.microsoft.com/dotnet/api/system.string)

対象の天体キー。

`code` [CelestialCatalogValidationCode](Omni.Celestial.CelestialCatalogValidationCode.md)

エラー種別。

`message` [string](https://learn.microsoft.com/dotnet/api/system.string)

原因説明。

## フィールド（Fields）

### <a id="Omni_Celestial_CelestialCatalogValidationIssue_BodyIndex"></a> BodyIndex

失敗したレコードのAuthoring配列上の添字。全体エラーでは-1です。

```csharp
public readonly int BodyIndex
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Celestial_CelestialCatalogValidationIssue_BodyKey"></a> BodyKey

失敗したレコードのキー。キー自体が不正な場合は空文字です。

```csharp
public readonly string BodyKey
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Celestial_CelestialCatalogValidationIssue_Code"></a> Code

エラー種別です。

```csharp
public readonly CelestialCatalogValidationCode Code
```

#### 値（Field Value）

 [CelestialCatalogValidationCode](Omni.Celestial.CelestialCatalogValidationCode.md)

### <a id="Omni_Celestial_CelestialCatalogValidationIssue_Message"></a> Message

人間が読める原因説明です。

```csharp
public readonly string Message
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Celestial_CelestialCatalogValidationIssue_ToString"></a> ToString\(\)

```csharp
public override string ToString()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
