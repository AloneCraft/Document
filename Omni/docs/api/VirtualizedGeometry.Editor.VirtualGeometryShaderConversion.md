# <a id="VirtualizedGeometry_Editor_VirtualGeometryShaderConversion"></a> Class VirtualGeometryShaderConversion

Namespace: [VirtualizedGeometry.Editor](VirtualizedGeometry.Editor.md)  
Assembly: Omni.VirtualGeometry.Editor.dll  

変換結果。失敗時はErrorに理由を入れ、Sourceはnullにする。

```csharp
public sealed class VirtualGeometryShaderConversion
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryShaderConversion](VirtualizedGeometry.Editor.VirtualGeometryShaderConversion.md)

## フィールド（Fields）

### <a id="VirtualizedGeometry_Editor_VirtualGeometryShaderConversion_Dependencies"></a> Dependencies

```csharp
public readonly List<string> Dependencies
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="VirtualizedGeometry_Editor_VirtualGeometryShaderConversion_Error"></a> Error

```csharp
public string Error
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualizedGeometry_Editor_VirtualGeometryShaderConversion_ShaderName"></a> ShaderName

```csharp
public string ShaderName
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualizedGeometry_Editor_VirtualGeometryShaderConversion_Source"></a> Source

```csharp
public string Source
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualizedGeometry_Editor_VirtualGeometryShaderConversion_Warnings"></a> Warnings

作れなかった追加の pass(DepthOnly など)と理由。forward pass は作れている。

```csharp
public readonly List<string> Warnings
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>
