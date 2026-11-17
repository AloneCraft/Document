# <a id="Omni_Streaming_TransferInfo"></a> Struct TransferInfo

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

```csharp
public readonly struct TransferInfo
```

## コンストラクター（Constructors）

### <a id="Omni_Streaming_TransferInfo__ctor_Omni_Streaming_ByteLocation__System_Boolean_System_Int64_System_Double_System_Int32_System_String_"></a> TransferInfo\(in ByteLocation, bool, long, double, int, string\)

```csharp
public TransferInfo(in ByteLocation location, bool success, long bytes, double seconds, int contents, string error)
```

#### 引数（Parameters）

`location` [ByteLocation](Omni.Streaming.ByteLocation.md)

`success` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`bytes` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`seconds` [double](https://learn.microsoft.com/dotnet/api/system.double)

`contents` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

## フィールド（Fields）

### <a id="Omni_Streaming_TransferInfo_Bytes"></a> Bytes

```csharp
public readonly long Bytes
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Streaming_TransferInfo_Contents"></a> Contents

```csharp
public readonly int Contents
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_TransferInfo_Error"></a> Error

```csharp
public readonly string Error
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Streaming_TransferInfo_Location"></a> Location

```csharp
public readonly ByteLocation Location
```

#### 値（Field Value）

 [ByteLocation](Omni.Streaming.ByteLocation.md)

### <a id="Omni_Streaming_TransferInfo_Seconds"></a> Seconds

```csharp
public readonly double Seconds
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Streaming_TransferInfo_Success"></a> Success

```csharp
public readonly bool Success
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
