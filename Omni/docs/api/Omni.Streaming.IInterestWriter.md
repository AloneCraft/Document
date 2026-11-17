# <a id="Omni_Streaming_IInterestWriter"></a> Interface IInterestWriter

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

欲しいキーの集合を毎フレーム宣言する口(複数の利用者が別々に持てる。host は全員の宣言を優先度の最大値で合成する)。

```csharp
public interface IInterestWriter : IDisposable
```

#### 実装するインターフェース（Implements）

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

## メソッド（Methods）

### <a id="Omni_Streaming_IInterestWriter_Begin"></a> Begin\(\)

宣言の組み立てを始める(前回 End した宣言は、End するまで有効なまま)。

```csharp
void Begin()
```

### <a id="Omni_Streaming_IInterestWriter_End"></a> End\(\)

組み立てた宣言を有効にする。以後、前の宣言は無効。

```csharp
void End()
```

### <a id="Omni_Streaming_IInterestWriter_Want_Omni_Streaming_StreamKey__System_Single_"></a> Want\(in StreamKey, float\)

```csharp
void Want(in StreamKey key, float priority)
```

#### 引数（Parameters）

`key` [StreamKey](Omni.Streaming.StreamKey.md)

`priority` [float](https://learn.microsoft.com/dotnet/api/system.single)
