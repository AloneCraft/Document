# <a id="Omni_Streaming_PreloadHandle"></a> Class PreloadHandle

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

メモリに余裕があるときの一括読み込み。Dispose するまで、キーを低い優先度で欲しがり続ける。

```csharp
public sealed class PreloadHandle : IDisposable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PreloadHandle](Omni.Streaming.PreloadHandle.md)

#### 実装するインターフェース（Implements）

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

## プロパティ（Properties）

### <a id="Omni_Streaming_PreloadHandle_Count"></a> Count

```csharp
public int Count { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_PreloadHandle_HasFailures"></a> HasFailures

再試行を使い切って失敗したキーがあるか。

```csharp
public bool HasFailures { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_PreloadHandle_IsComplete"></a> IsComplete

```csharp
public bool IsComplete { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_PreloadHandle_Progress"></a> Progress

Resident または Absent になったキーの割合(0〜1)。キーが無ければ 1。

```csharp
public float Progress { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

## メソッド（Methods）

### <a id="Omni_Streaming_PreloadHandle_Dispose"></a> Dispose\(\)

```csharp
public void Dispose()
```
