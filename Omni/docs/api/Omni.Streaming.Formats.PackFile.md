# <a id="Omni_Streaming_Formats_PackFile"></a> Class PackFile

Namespace: [Omni.Streaming.Formats](Omni.Streaming.Formats.md)  
Assembly: Omni.Streaming.Formats.dll  

メモリ上の pack を同期で読む(書き出しの検証、小さな pack、ツール用)。

```csharp
public sealed class PackFile
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PackFile](Omni.Streaming.Formats.PackFile.md)

## コンストラクター（Constructors）

### <a id="Omni_Streaming_Formats_PackFile__ctor_System_Byte___"></a> PackFile\(byte\[\]\)

```csharp
public PackFile(byte[] bytes)
```

#### 引数（Parameters）

`bytes` [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\]

## プロパティ（Properties）

### <a id="Omni_Streaming_Formats_PackFile_Header"></a> Header

```csharp
public PackHeader Header { get; }
```

#### 値（Property Value）

 [PackHeader](Omni.Streaming.Formats.PackHeader.md)

### <a id="Omni_Streaming_Formats_PackFile_Metadata"></a> Metadata

```csharp
public IReadOnlyDictionary<string, string> Metadata { get; }
```

#### 値（Property Value）

 [IReadOnlyDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlydictionary\-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [string](https://learn.microsoft.com/dotnet/api/system.string)\>

## メソッド（Methods）

### <a id="Omni_Streaming_Formats_PackFile_Content_Omni_Streaming_Formats_PackEntry__"></a> Content\(in PackEntry\)

```csharp
public ReadOnlySpan<byte> Content(in PackEntry entry)
```

#### 引数（Parameters）

`entry` [PackEntry](Omni.Streaming.Formats.PackEntry.md)

#### 戻り値（Returns）

 [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[byte](https://learn.microsoft.com/dotnet/api/system.byte)\>

### <a id="Omni_Streaming_Formats_PackFile_TryFind_System_Int32_System_UInt32_System_UInt32_Omni_Streaming_Formats_PackEntry__"></a> TryFind\(int, uint, uint, out PackEntry\)

```csharp
public bool TryFind(int level, uint x, uint y, out PackEntry entry)
```

#### 引数（Parameters）

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`x` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`y` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`entry` [PackEntry](Omni.Streaming.Formats.PackEntry.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
