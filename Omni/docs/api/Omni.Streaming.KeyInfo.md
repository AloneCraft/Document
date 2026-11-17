# <a id="Omni_Streaming_KeyInfo"></a> Struct KeyInfo

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

ストリーミングの調停役。利用者は <xref href="Omni.Streaming.IInterestWriter" data-throw-if-not-resolved="false"></xref> で欲しいキーを宣言し、<code>TryAcquire</code> で展開済みの中身を借りる。
host は Tick ごとに、カタログで場所を引き、ストアに無ければ取得元から取り(隣り合う範囲は1回にまとめ、不要になった要求は取り消し)、
中身の ID を照合してストアへ入れ、frame の予算の範囲で展開し、メモリ予算を超えれば使われていない展開済みを古い順に追い出す。
単一 thread(Tick を呼ぶ thread)で使う。ワーカーや別の仕組みで完了する取得元は、<xref href="Omni.Streaming.IByteRequest.IsDone" data-throw-if-not-resolved="false"></xref> を安全に公開すること。

```csharp
public readonly struct KeyInfo
```

## コンストラクター（Constructors）

### <a id="Omni_Streaming_KeyInfo__ctor_Omni_Streaming_PayloadState_System_Boolean_System_Boolean_System_Boolean_System_Boolean_System_Int32_System_String_"></a> KeyInfo\(PayloadState, bool, bool, bool, bool, int, string\)

```csharp
public KeyInfo(PayloadState state, bool wanted, bool inFlight, bool decoding, bool hasEntry, int attempts, string error)
```

#### 引数（Parameters）

`state` [PayloadState](Omni.Streaming.PayloadState.md)

`wanted` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`inFlight` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`decoding` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`hasEntry` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`attempts` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

## フィールド（Fields）

### <a id="Omni_Streaming_KeyInfo_Attempts"></a> Attempts

```csharp
public readonly int Attempts
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_KeyInfo_Decoding"></a> Decoding

取得は済み、展開を待っている。

```csharp
public readonly bool Decoding
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_KeyInfo_Error"></a> Error

```csharp
public readonly string Error
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Streaming_KeyInfo_HasEntry"></a> HasEntry

カタログから中身の場所を得ている。

```csharp
public readonly bool HasEntry
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_KeyInfo_InFlight"></a> InFlight

取得(転送)が進行中。

```csharp
public readonly bool InFlight
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_KeyInfo_State"></a> State

```csharp
public readonly PayloadState State
```

#### 値（Field Value）

 [PayloadState](Omni.Streaming.PayloadState.md)

### <a id="Omni_Streaming_KeyInfo_Wanted"></a> Wanted

直近の Tick で、誰かに欲しがられている。

```csharp
public readonly bool Wanted
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
