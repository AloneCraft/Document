# <a id="Omni_Editor_Manager_TerrainShaderClosureResult"></a> Class TerrainShaderClosureResult

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

TerrainLit の依存 Shader 閉包を生成した結果です。

<p>
この型は Editor 専用です。Runtime の Terrain や Material を変更せず、呼び出し側が
<xref href="Omni.Editor.Manager.TerrainShaderClosureResult.IsReady" data-throw-if-not-resolved="false"></xref> を確認してから置換をコミットするための診断値だけを返します。
</p>

```csharp
public sealed class TerrainShaderClosureResult
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[TerrainShaderClosureResult](Omni.Editor.Manager.TerrainShaderClosureResult.md)

## フィールド（Fields）

### <a id="Omni_Editor_Manager_TerrainShaderClosureResult_CurrentSchemaVersion"></a> CurrentSchemaVersion

生成スキーマの版です。URP 由来の参照契約を変えた場合に更新します。

```csharp
public const string CurrentSchemaVersion = "omni-terrain-radial-closure-v4"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## プロパティ（Properties）

### <a id="Omni_Editor_Manager_TerrainShaderClosureResult_Diagnostics"></a> Diagnostics

ユーザーへ表示可能な失敗・縮退理由です。

```csharp
public string[] Diagnostics { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)\[\]

### <a id="Omni_Editor_Manager_TerrainShaderClosureResult_GeneratedPaths"></a> GeneratedPaths

今回の閉包に属する生成 Shader のアセットパスです。

```csharp
public string[] GeneratedPaths { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)\[\]

### <a id="Omni_Editor_Manager_TerrainShaderClosureResult_GeneratedShaderCount"></a> GeneratedShaderCount

閉包内の Shader 数です。ファイルが既に最新でも閉包の完全性はこの数で表します。

```csharp
public int GeneratedShaderCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Manager_TerrainShaderClosureResult_IsReady"></a> IsReady

全依存が生成・import 済みで、Terrain Material の置換を安全に開始できるかを返します。

```csharp
public bool IsReady { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_TerrainShaderClosureResult_MissingDependencies"></a> MissingDependencies

読めなかった、または URP 契約から外れた依存の一覧です。

```csharp
public string[] MissingDependencies { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)\[\]

### <a id="Omni_Editor_Manager_TerrainShaderClosureResult_SchemaVersion"></a> SchemaVersion

生成時に固定したスキーマ版です。

```csharp
public string SchemaVersion { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_TerrainShaderClosureResult_SourceFingerprint"></a> SourceFingerprint

URP 入力・参照書換え規則・生成テンプレートを含む SHA-256 指紋です。
同一入力から同一の閉包が生成されたかを診断できます。

```csharp
public string SourceFingerprint { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_TerrainShaderClosureResult_Status"></a> Status

閉包の現在状態です。

```csharp
public TerrainShaderClosureStatus Status { get; }
```

#### 値（Property Value）

 [TerrainShaderClosureStatus](Omni.Editor.Manager.TerrainShaderClosureStatus.md)

### <a id="Omni_Editor_Manager_TerrainShaderClosureResult_TerrainLitShaderPath"></a> TerrainLitShaderPath

生成済み TerrainLit のアセットパスです。失敗時は null です。

```csharp
public string TerrainLitShaderPath { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
