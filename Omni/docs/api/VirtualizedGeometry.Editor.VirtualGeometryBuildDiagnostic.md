# <a id="VirtualizedGeometry_Editor_VirtualGeometryBuildDiagnostic"></a> Struct VirtualGeometryBuildDiagnostic

Namespace: [VirtualizedGeometry.Editor](VirtualizedGeometry.Editor.md)  
Assembly: Omni.VirtualGeometry.Editor.dll  

```csharp
public readonly struct VirtualGeometryBuildDiagnostic
```

## コンストラクター（Constructors）

### <a id="VirtualizedGeometry_Editor_VirtualGeometryBuildDiagnostic__ctor_System_String_VirtualizedGeometry_Editor_VirtualGeometryDiagnosticSeverity_System_String_"></a> VirtualGeometryBuildDiagnostic\(string, VirtualGeometryDiagnosticSeverity, string\)

```csharp
public VirtualGeometryBuildDiagnostic(string code, VirtualGeometryDiagnosticSeverity severity, string message)
```

#### 引数（Parameters）

`code` [string](https://learn.microsoft.com/dotnet/api/system.string)

`severity` [VirtualGeometryDiagnosticSeverity](VirtualizedGeometry.Editor.VirtualGeometryDiagnosticSeverity.md)

`message` [string](https://learn.microsoft.com/dotnet/api/system.string)

## プロパティ（Properties）

### <a id="VirtualizedGeometry_Editor_VirtualGeometryBuildDiagnostic_Code"></a> Code

```csharp
public string Code { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualizedGeometry_Editor_VirtualGeometryBuildDiagnostic_Message"></a> Message

```csharp
public string Message { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualizedGeometry_Editor_VirtualGeometryBuildDiagnostic_Severity"></a> Severity

```csharp
public VirtualGeometryDiagnosticSeverity Severity { get; }
```

#### 値（Property Value）

 [VirtualGeometryDiagnosticSeverity](VirtualizedGeometry.Editor.VirtualGeometryDiagnosticSeverity.md)
