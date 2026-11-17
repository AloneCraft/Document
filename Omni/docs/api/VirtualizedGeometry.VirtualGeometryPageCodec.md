# <a id="VirtualizedGeometry_VirtualGeometryPageCodec"></a> Class VirtualGeometryPageCodec

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

バージョン・範囲・CRC・階層不変条件を検証し、破損ページをGPUへ渡さない。

```csharp
public static class VirtualGeometryPageCodec
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryPageCodec](VirtualizedGeometry.VirtualGeometryPageCodec.md)

## フィールド（Fields）

### <a id="VirtualizedGeometry_VirtualGeometryPageCodec_BuilderVersion"></a> BuilderVersion

```csharp
public const uint BuilderVersion = 3
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualizedGeometry_VirtualGeometryPageCodec_FormatVersion"></a> FormatVersion

```csharp
public const uint FormatVersion = 3
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualizedGeometry_VirtualGeometryPageCodec_HeaderSize"></a> HeaderSize

```csharp
public const int HeaderSize = 112
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryPageCodec_Magic"></a> Magic

```csharp
public const uint Magic = 1196443478
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometryPageCodec_Read_System_Byte___"></a> Read\(byte\[\]\)

```csharp
public static VirtualGeometryPage Read(byte[] data)
```

#### 引数（Parameters）

`data` [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\]

#### 戻り値（Returns）

 [VirtualGeometryPage](VirtualizedGeometry.VirtualGeometryPage.md)

### <a id="VirtualizedGeometry_VirtualGeometryPageCodec_Write_VirtualizedGeometry_VirtualGeometryPage_"></a> Write\(VirtualGeometryPage\)

```csharp
public static byte[] Write(VirtualGeometryPage page)
```

#### 引数（Parameters）

`page` [VirtualGeometryPage](VirtualizedGeometry.VirtualGeometryPage.md)

#### 戻り値（Returns）

 [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\]
