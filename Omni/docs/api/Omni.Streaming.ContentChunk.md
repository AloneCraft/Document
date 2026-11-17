# <a id="Omni_Streaming_ContentChunk"></a> Struct ContentChunk

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

1個の独立した配信ファイル。ContainerはHTTP/FileByteSourceへ登録した番号。

```csharp
public readonly struct ContentChunk
```

## コンストラクター（Constructors）

### <a id="Omni_Streaming_ContentChunk__ctor_System_Int32_System_Int32_System_String_"></a> ContentChunk\(int, int, string\)

```csharp
public ContentChunk(int container, int length, string sha256)
```

#### 引数（Parameters）

`container` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`length` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`sha256` [string](https://learn.microsoft.com/dotnet/api/system.string)

## フィールド（Fields）

### <a id="Omni_Streaming_ContentChunk_Container"></a> Container

```csharp
public readonly int Container
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_ContentChunk_Length"></a> Length

```csharp
public readonly int Length
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_ContentChunk_Sha256"></a> Sha256

```csharp
public readonly string Sha256
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
