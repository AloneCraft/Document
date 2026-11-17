# <a id="Omni_Converter_OmniGeneratedAssetPaths"></a> Class OmniGeneratedAssetPaths

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

配布物とプロジェクト固有の生成物を分離するための正規パスです。

```csharp
public static class OmniGeneratedAssetPaths
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniGeneratedAssetPaths](Omni.Converter.OmniGeneratedAssetPaths.md)

## フィールド（Fields）

### <a id="Omni_Converter_OmniGeneratedAssetPaths_GeneratedRoot"></a> GeneratedRoot

再生成可能な変換、Bake、BRG、Shader出力のルートです。

```csharp
public const string GeneratedRoot = "Assets/Radial"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniGeneratedAssetPaths_GuidManifestPath"></a> GuidManifestPath

再生成時もGUIDを維持するためのプロジェクト固有マニフェストです。

```csharp
public const string GuidManifestPath = "ProjectSettings/Omni/Generated.manifest.json"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniGeneratedAssetPaths_LegacyGuidManifestPath"></a> LegacyGuidManifestPath

初回移行時だけ読み取る旧GUIDマニフェストです。書込み・削除は行いません。

```csharp
public const string LegacyGuidManifestPath = "Assets/Radial/Generated.manifest.json"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniGeneratedAssetPaths_ManagedBuiltInMaterialRoot"></a> ManagedBuiltInMaterialRoot

読取専用のBuiltinRP Materialから作る管理Materialの保存先です。

```csharp
public const string ManagedBuiltInMaterialRoot = "Assets/Radial/ManagedBuiltInMaterials"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniGeneratedAssetPaths_ManagedDiagnosticMaterialRoot"></a> ManagedDiagnosticMaterialRoot

対応先がないShaderを可視化し、元参照へ復元するための管理Material保存先です。

```csharp
public const string ManagedDiagnosticMaterialRoot = "Assets/Radial/DiagnosticMaterials"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniGeneratedAssetPaths_MaterialMappingPath"></a> MaterialMappingPath

既存Materialを直接切り替えたときの復元情報です。

```csharp
public const string MaterialMappingPath = "Assets/Radial/Mappings/MaterialShaderMappings.asset"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniGeneratedAssetPaths_PackagesRoot"></a> PackagesRoot

パッケージ（<code>Packages/&lt;名前&gt;/…</code>）にあるものを変換した出力先です。URP などの Shader／Shader Graph と、
パッケージ内の Material の変換物が、元と同じ相対パスで置かれます。

```csharp
public const string PackagesRoot = "Assets/Radial/Packages"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniGeneratedAssetPaths_ProjectSettingsRoot"></a> ProjectSettingsRoot

Unity AssetではないOmniのプロジェクト設定データのルートです。

```csharp
public const string ProjectSettingsRoot = "ProjectSettings/Omni"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniGeneratedAssetPaths_UserDataRoot"></a> UserDataRoot

購入者のプロジェクト内でOmniが生成するRadial成果物のルートです。

```csharp
public const string UserDataRoot = "Assets/Radial"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniGeneratedAssetPaths_UserHlslRoot"></a> UserHlslRoot

購入者の独自HLSL変換物の出力先です。

```csharp
public const string UserHlslRoot = "Assets/Radial/Hlsl"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniGeneratedAssetPaths_UserShaderRoot"></a> UserShaderRoot

購入者のプロジェクト（<code>Assets/</code>）にある Shader／Shader Graph を変換した出力先です。

```csharp
public const string UserShaderRoot = "Assets/Radial/User"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
