# <a id="Omni_Streaming_Unity_FileSystemSync"></a> Class FileSystemSync

Namespace: [Omni.Streaming.Unity](Omni.Streaming.Unity.md)  
Assembly: Omni.Streaming.Unity.dll  

ブラウザ(WebGL)の persistentDataPath の保存を促す。他のプラットフォームでは何もしない。
<xref href="Omni.Streaming.Unity.FileSystemSync.Request" data-throw-if-not-resolved="false"></xref> は何度呼んでもよい(間引いて、最後の呼びから <xref href="Omni.Streaming.Unity.FileSystemSync.MinimumIntervalSeconds" data-throw-if-not-resolved="false"></xref> 以上あけて1回保存する)。
保存の呼び出しは <xref href="Omni.Streaming.Unity.StreamingBehaviour" data-throw-if-not-resolved="false"></xref> の Update が行う。

```csharp
public static class FileSystemSync
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[FileSystemSync](Omni.Streaming.Unity.FileSystemSync.md)

## フィールド（Fields）

### <a id="Omni_Streaming_Unity_FileSystemSync_MinimumIntervalSeconds"></a> MinimumIntervalSeconds

```csharp
public static float MinimumIntervalSeconds
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

## プロパティ（Properties）

### <a id="Omni_Streaming_Unity_FileSystemSync_IsPending"></a> IsPending

```csharp
public static bool IsPending { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_Unity_FileSystemSync_SyncCount"></a> SyncCount

```csharp
public static int SyncCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_Streaming_Unity_FileSystemSync_Flush"></a> Flush\(\)

保留があり、前回から間隔があいていれば保存を実行する。

```csharp
public static void Flush()
```

### <a id="Omni_Streaming_Unity_FileSystemSync_Request"></a> Request\(\)

```csharp
public static void Request()
```
