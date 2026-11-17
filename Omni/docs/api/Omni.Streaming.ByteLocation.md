# <a id="Omni_Streaming_ByteLocation"></a> Struct ByteLocation

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

コンテナ内の範囲。Container は取得元が解釈する番号(ファイル、URL の配列の番号など)。

```csharp
public readonly struct ByteLocation : IEquatable<ByteLocation>
```

#### 実装するインターフェース（Implements）

[IEquatable<ByteLocation\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1)

## コンストラクター（Constructors）

### <a id="Omni_Streaming_ByteLocation__ctor_System_Int32_System_Int64_System_Int32_"></a> ByteLocation\(int, long, int\)

```csharp
public ByteLocation(int container, long offset, int length)
```

#### 引数（Parameters）

`container` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`offset` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`length` [int](https://learn.microsoft.com/dotnet/api/system.int32)

## フィールド（Fields）

### <a id="Omni_Streaming_ByteLocation_Container"></a> Container

```csharp
public readonly int Container
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_ByteLocation_Length"></a> Length

```csharp
public readonly int Length
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_ByteLocation_Offset"></a> Offset

```csharp
public readonly long Offset
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

## プロパティ（Properties）

### <a id="Omni_Streaming_ByteLocation_End"></a> End

```csharp
public long End { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

## メソッド（Methods）

### <a id="Omni_Streaming_ByteLocation_Equals_Omni_Streaming_ByteLocation_"></a> Equals\(ByteLocation\)

```csharp
public bool Equals(ByteLocation other)
```

#### 引数（Parameters）

`other` [ByteLocation](Omni.Streaming.ByteLocation.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_ByteLocation_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object obj)
```

#### 引数（Parameters）

`obj` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_ByteLocation_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_ByteLocation_ToString"></a> ToString\(\)

```csharp
public override string ToString()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
