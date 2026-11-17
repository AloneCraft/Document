# <a id="Omni_Streaming_CompletedByteRequest"></a> Class CompletedByteRequest

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

1回で完了する取得(同期的に作った結果を返す)。取得元の実装や、メモリ・ファイルの取得元が使う。

```csharp
public sealed class CompletedByteRequest : IByteRequest
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[CompletedByteRequest](Omni.Streaming.CompletedByteRequest.md)

#### 実装するインターフェース（Implements）

[IByteRequest](Omni.Streaming.IByteRequest.md)

## プロパティ（Properties）

### <a id="Omni_Streaming_CompletedByteRequest_Error"></a> Error

```csharp
public string Error { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Streaming_CompletedByteRequest_IsDone"></a> IsDone

```csharp
public bool IsDone { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_CompletedByteRequest_IsSuccess"></a> IsSuccess

```csharp
public bool IsSuccess { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_CompletedByteRequest_ReceivedBytes"></a> ReceivedBytes

これまでに受け取ったバイト数(進捗の表示用)。

```csharp
public long ReceivedBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

## メソッド（Methods）

### <a id="Omni_Streaming_CompletedByteRequest_Cancel"></a> Cancel\(\)

取り消す。まだ完了していなければ以後 <xref href="Omni.Streaming.IByteRequest.IsDone" data-throw-if-not-resolved="false"></xref> が true になる(IsSuccess は false)。完了済みで結果が未回収なら捨てる。

```csharp
public void Cancel()
```

### <a id="Omni_Streaming_CompletedByteRequest_Failure_System_String_"></a> Failure\(string\)

```csharp
public static CompletedByteRequest Failure(string error)
```

#### 引数（Parameters）

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [CompletedByteRequest](Omni.Streaming.CompletedByteRequest.md)

### <a id="Omni_Streaming_CompletedByteRequest_Success_Omni_Streaming_PooledBuffer_"></a> Success\(PooledBuffer\)

```csharp
public static CompletedByteRequest Success(PooledBuffer result)
```

#### 引数（Parameters）

`result` [PooledBuffer](Omni.Streaming.PooledBuffer.md)

#### 戻り値（Returns）

 [CompletedByteRequest](Omni.Streaming.CompletedByteRequest.md)

### <a id="Omni_Streaming_CompletedByteRequest_TakeResult"></a> TakeResult\(\)

完了(成功)後に1回だけ呼べる。結果のバッファの所有権(参照1つ)が呼び手へ移る。

```csharp
public PooledBuffer TakeResult()
```

#### 戻り値（Returns）

 [PooledBuffer](Omni.Streaming.PooledBuffer.md)
