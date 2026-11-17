# <a id="Omni_Streaming_Formats_PackWriterOptions"></a> Class PackWriterOptions

Namespace: [Omni.Streaming.Formats](Omni.Streaming.Formats.md)  
Assembly: Omni.Streaming.Formats.dll  

```csharp
public sealed class PackWriterOptions
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PackWriterOptions](Omni.Streaming.Formats.PackWriterOptions.md)

## フィールド（Fields）

### <a id="Omni_Streaming_Formats_PackWriterOptions_DefaultKind"></a> DefaultKind

種別を指定しない中身の展開器の種別。

```csharp
public ushort DefaultKind
```

#### 値（Field Value）

 [ushort](https://learn.microsoft.com/dotnet/api/system.uint16)

### <a id="Omni_Streaming_Formats_PackWriterOptions_DeflateDirectories"></a> DeflateDirectories

```csharp
public bool DeflateDirectories
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_Formats_PackWriterOptions_Face"></a> Face

この pack が扱う面(<xref href="Omni.Streaming.Formats.PackHeader.AnyFace" data-throw-if-not-resolved="false"></xref> はどの面も)。

```csharp
public byte Face
```

#### 値（Field Value）

 [byte](https://learn.microsoft.com/dotnet/api/system.byte)

### <a id="Omni_Streaming_Formats_PackWriterOptions_Layer"></a> Layer

```csharp
public uint Layer
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="Omni_Streaming_Formats_PackWriterOptions_MaxLevel"></a> MaxLevel

```csharp
public byte MaxLevel
```

#### 値（Field Value）

 [byte](https://learn.microsoft.com/dotnet/api/system.byte)

### <a id="Omni_Streaming_Formats_PackWriterOptions_Metadata"></a> Metadata

付随情報(出典・量子化・半径など)。キーと値に改行とタブを含めない。

```csharp
public readonly SortedDictionary<string, string> Metadata
```

#### 値（Field Value）

 [SortedDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.sorteddictionary\-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Streaming_Formats_PackWriterOptions_MinLevel"></a> MinLevel

```csharp
public byte MinLevel
```

#### 値（Field Value）

 [byte](https://learn.microsoft.com/dotnet/api/system.byte)

### <a id="Omni_Streaming_Formats_PackWriterOptions_PageEntries"></a> PageEntries

葉の目録の1ページあたりの項目数の下限(根の目録が先頭 16 KiB に収まるよう、必要なら増やす)。

```csharp
public int PageEntries
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_Formats_PackWriterOptions_Spool"></a> Spool

中身の本体の一時置き場。省略するとメモリ(大きい pack ではファイルを渡す)。

```csharp
public Stream Spool
```

#### 値（Field Value）

 [Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)
