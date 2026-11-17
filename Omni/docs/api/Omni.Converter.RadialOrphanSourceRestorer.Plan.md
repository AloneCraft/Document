# <a id="Omni_Converter_RadialOrphanSourceRestorer_Plan"></a> Struct RadialOrphanSourceRestorer.Plan

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

1件分の復元計画です。

```csharp
public readonly struct RadialOrphanSourceRestorer.Plan
```

## コンストラクター（Constructors）

### <a id="Omni_Converter_RadialOrphanSourceRestorer_Plan__ctor_System_String_System_String_System_String_"></a> Plan\(string, string, string\)

```csharp
public Plan(string generatedPath, string sourcePath, string blocker)
```

#### 引数（Parameters）

`generatedPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`sourcePath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`blocker` [string](https://learn.microsoft.com/dotnet/api/system.string)

## フィールド（Fields）

### <a id="Omni_Converter_RadialOrphanSourceRestorer_Plan_Blocker"></a> Blocker

復元できない場合の理由。復元可能なら null。

```csharp
public readonly string Blocker
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_RadialOrphanSourceRestorer_Plan_GeneratedPath"></a> GeneratedPath

孤児になっている生成マテリアルのパス。

```csharp
public readonly string GeneratedPath
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_RadialOrphanSourceRestorer_Plan_SourcePath"></a> SourcePath

復元先の元マテリアルのパス。復元できない場合は null。

```csharp
public readonly string SourcePath
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## プロパティ（Properties）

### <a id="Omni_Converter_RadialOrphanSourceRestorer_Plan_CanRestore"></a> CanRestore

復元可能かどうか。

```csharp
public bool CanRestore { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
