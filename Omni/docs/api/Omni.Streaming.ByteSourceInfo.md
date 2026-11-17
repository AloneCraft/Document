# <a id="Omni_Streaming_ByteSourceInfo"></a> Struct ByteSourceInfo

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

```csharp
public readonly struct ByteSourceInfo
```

## コンストラクター（Constructors）

### <a id="Omni_Streaming_ByteSourceInfo__ctor_System_String_System_Boolean_System_Int32_"></a> ByteSourceInfo\(string, bool, int\)

```csharp
public ByteSourceInfo(string name, bool supportsRange, int preferredConcurrency = 0)
```

#### 引数（Parameters）

`name` [string](https://learn.microsoft.com/dotnet/api/system.string)

`supportsRange` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`preferredConcurrency` [int](https://learn.microsoft.com/dotnet/api/system.int32)

## フィールド（Fields）

### <a id="Omni_Streaming_ByteSourceInfo_Name"></a> Name

```csharp
public readonly string Name
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Streaming_ByteSourceInfo_PreferredConcurrency"></a> PreferredConcurrency

取得元が望む同時要求数の上限(host の設定と小さい方を使う)。0 は指定なし。

```csharp
public readonly int PreferredConcurrency
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_ByteSourceInfo_SupportsRange"></a> SupportsRange

範囲だけを取れるか。false の取得元には、範囲の結合をせず、キーごとに1回ずつ要求する(取得元は位置を目印として使う)。

```csharp
public readonly bool SupportsRange
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
