# <a id="Omni_Streaming_ContentId"></a> Struct ContentId

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

中身(何)の識別子。SHA-256 の先頭 128 bit。同じ中身なら同じ ID になるので、版の更新・重複の排除・取得元をまたぐキャッシュの共有・
整合性の検査(<xref href="Omni.Streaming.StreamingOptions.VerifyIntegrity" data-throw-if-not-resolved="false"></xref>)が、すべて「ID が同じなら同じ」に帰着する。default は空(中身なし)。

```csharp
public readonly struct ContentId : IEquatable<ContentId>, IComparable<ContentId>
```

#### 実装するインターフェース（Implements）

[IEquatable<ContentId\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1), 
[IComparable<ContentId\>](https://learn.microsoft.com/dotnet/api/system.icomparable\-1)

## コンストラクター（Constructors）

### <a id="Omni_Streaming_ContentId__ctor_System_UInt64_System_UInt64_"></a> ContentId\(ulong, ulong\)

```csharp
public ContentId(ulong high, ulong low)
```

#### 引数（Parameters）

`high` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

`low` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

## フィールド（Fields）

### <a id="Omni_Streaming_ContentId_ByteCount"></a> ByteCount

```csharp
public const int ByteCount = 16
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_ContentId_High"></a> High

```csharp
public readonly ulong High
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_Streaming_ContentId_Low"></a> Low

```csharp
public readonly ulong Low
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

## プロパティ（Properties）

### <a id="Omni_Streaming_ContentId_IsEmpty"></a> IsEmpty

```csharp
public bool IsEmpty { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_Streaming_ContentId_CompareTo_Omni_Streaming_ContentId_"></a> CompareTo\(ContentId\)

```csharp
public int CompareTo(ContentId other)
```

#### 引数（Parameters）

`other` [ContentId](Omni.Streaming.ContentId.md)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_ContentId_Compute_System_ReadOnlySpan_System_Byte__"></a> Compute\(ReadOnlySpan<byte\>\)

```csharp
public static ContentId Compute(ReadOnlySpan<byte> data)
```

#### 引数（Parameters）

`data` [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[byte](https://learn.microsoft.com/dotnet/api/system.byte)\>

#### 戻り値（Returns）

 [ContentId](Omni.Streaming.ContentId.md)

### <a id="Omni_Streaming_ContentId_Equals_Omni_Streaming_ContentId_"></a> Equals\(ContentId\)

```csharp
public bool Equals(ContentId other)
```

#### 引数（Parameters）

`other` [ContentId](Omni.Streaming.ContentId.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_ContentId_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object obj)
```

#### 引数（Parameters）

`obj` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_ContentId_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_ContentId_Read_System_ReadOnlySpan_System_Byte__"></a> Read\(ReadOnlySpan<byte\>\)

16 byte(big endian)から読む。

```csharp
public static ContentId Read(ReadOnlySpan<byte> bytes)
```

#### 引数（Parameters）

`bytes` [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[byte](https://learn.microsoft.com/dotnet/api/system.byte)\>

#### 戻り値（Returns）

 [ContentId](Omni.Streaming.ContentId.md)

### <a id="Omni_Streaming_ContentId_ToString"></a> ToString\(\)

```csharp
public override string ToString()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Streaming_ContentId_TryParse_System_String_Omni_Streaming_ContentId__"></a> TryParse\(string, out ContentId\)

```csharp
public static bool TryParse(string text, out ContentId id)
```

#### 引数（Parameters）

`text` [string](https://learn.microsoft.com/dotnet/api/system.string)

`id` [ContentId](Omni.Streaming.ContentId.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_ContentId_Write_System_Span_System_Byte__"></a> Write\(Span<byte\>\)

```csharp
public void Write(Span<byte> bytes)
```

#### 引数（Parameters）

`bytes` [Span](https://learn.microsoft.com/dotnet/api/system.span\-1)<[byte](https://learn.microsoft.com/dotnet/api/system.byte)\>

## 演算子（Operators）

### <a id="Omni_Streaming_ContentId_op_Equality_Omni_Streaming_ContentId_Omni_Streaming_ContentId_"></a> operator ==\(ContentId, ContentId\)

```csharp
public static bool operator ==(ContentId a, ContentId b)
```

#### 引数（Parameters）

`a` [ContentId](Omni.Streaming.ContentId.md)

`b` [ContentId](Omni.Streaming.ContentId.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_ContentId_op_Inequality_Omni_Streaming_ContentId_Omni_Streaming_ContentId_"></a> operator \!=\(ContentId, ContentId\)

```csharp
public static bool operator !=(ContentId a, ContentId b)
```

#### 引数（Parameters）

`a` [ContentId](Omni.Streaming.ContentId.md)

`b` [ContentId](Omni.Streaming.ContentId.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
