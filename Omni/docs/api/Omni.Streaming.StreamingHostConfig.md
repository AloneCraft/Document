# <a id="Omni_Streaming_StreamingHostConfig"></a> Class StreamingHostConfig

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

host の組み立て(必須は Catalog と Source。Store・Decoders・Options・Clock・Pool は省略できる)。

```csharp
public sealed class StreamingHostConfig
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[StreamingHostConfig](Omni.Streaming.StreamingHostConfig.md)

## フィールド（Fields）

### <a id="Omni_Streaming_StreamingHostConfig_Catalog"></a> Catalog

```csharp
public ICatalog Catalog
```

#### 値（Field Value）

 [ICatalog](Omni.Streaming.ICatalog.md)

### <a id="Omni_Streaming_StreamingHostConfig_Clock"></a> Clock

```csharp
public IClock Clock
```

#### 値（Field Value）

 [IClock](Omni.Streaming.IClock.md)

### <a id="Omni_Streaming_StreamingHostConfig_Decoders"></a> Decoders

```csharp
public readonly List<IPayloadDecoder> Decoders
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[IPayloadDecoder](Omni.Streaming.IPayloadDecoder.md)\>

### <a id="Omni_Streaming_StreamingHostConfig_Diagnostics"></a> Diagnostics

```csharp
public StreamingTraceContext Diagnostics
```

#### 値（Field Value）

 [StreamingTraceContext](Omni.Streaming.StreamingTraceContext.md)

### <a id="Omni_Streaming_StreamingHostConfig_Options"></a> Options

```csharp
public StreamingOptions Options
```

#### 値（Field Value）

 [StreamingOptions](Omni.Streaming.StreamingOptions.md)

### <a id="Omni_Streaming_StreamingHostConfig_Pool"></a> Pool

```csharp
public BufferPool Pool
```

#### 値（Field Value）

 [BufferPool](Omni.Streaming.BufferPool.md)

### <a id="Omni_Streaming_StreamingHostConfig_Source"></a> Source

```csharp
public IByteSource Source
```

#### 値（Field Value）

 [IByteSource](Omni.Streaming.IByteSource.md)

### <a id="Omni_Streaming_StreamingHostConfig_Store"></a> Store

省略すると 64 MiB の <xref href="Omni.Streaming.MemoryStore" data-throw-if-not-resolved="false"></xref>。

```csharp
public IContentStore Store
```

#### 値（Field Value）

 [IContentStore](Omni.Streaming.IContentStore.md)
