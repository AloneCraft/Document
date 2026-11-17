# <a id="Omni_Streaming_IByteRequest"></a> Interface IByteRequest

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

進行中の1回の取得。完了の通知は <xref href="Omni.Streaming.IByteRequest.IsDone" data-throw-if-not-resolved="false"></xref> のポーリング(host の Tick が見る)。別スレッドや別の仕組みで完了する実装は、
結果を書いてから IsDone を立てる(他のスレッドから安全に公開する)こと。

```csharp
public interface IByteRequest
```

## プロパティ（Properties）

### <a id="Omni_Streaming_IByteRequest_Error"></a> Error

```csharp
string Error { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Streaming_IByteRequest_IsDone"></a> IsDone

```csharp
bool IsDone { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_IByteRequest_IsSuccess"></a> IsSuccess

```csharp
bool IsSuccess { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_IByteRequest_ReceivedBytes"></a> ReceivedBytes

これまでに受け取ったバイト数(進捗の表示用)。

```csharp
long ReceivedBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

## メソッド（Methods）

### <a id="Omni_Streaming_IByteRequest_Cancel"></a> Cancel\(\)

取り消す。まだ完了していなければ以後 <xref href="Omni.Streaming.IByteRequest.IsDone" data-throw-if-not-resolved="false"></xref> が true になる(IsSuccess は false)。完了済みで結果が未回収なら捨てる。

```csharp
void Cancel()
```

### <a id="Omni_Streaming_IByteRequest_TakeResult"></a> TakeResult\(\)

完了(成功)後に1回だけ呼べる。結果のバッファの所有権(参照1つ)が呼び手へ移る。

```csharp
PooledBuffer TakeResult()
```

#### 戻り値（Returns）

 [PooledBuffer](Omni.Streaming.PooledBuffer.md)
