# <a id="Omni_Logical_DetachResult"></a> Struct DetachResult

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

Detachの状態と診断メッセージを返す不変値です。

```csharp
public readonly struct DetachResult
```

## コンストラクター（Constructors）

### <a id="Omni_Logical_DetachResult__ctor_Omni_Logical_DetachStatus_System_String_"></a> DetachResult\(DetachStatus, string\)

結果を構築します。

```csharp
public DetachResult(DetachStatus status, string message)
```

#### 引数（Parameters）

`status` [DetachStatus](Omni.Logical.DetachStatus.md)

`message` [string](https://learn.microsoft.com/dotnet/api/system.string)

## フィールド（Fields）

### <a id="Omni_Logical_DetachResult_Message"></a> Message

診断用の補足メッセージです。呼び出し元は現状すべて<xref href="System.String.Empty" data-throw-if-not-resolved="false"></xref>を渡しており
（分類の判定は<xref href="Omni.Logical.DetachResult.Status" data-throw-if-not-resolved="false"></xref>で行うため）、常に空文字になります。

```csharp
public readonly string Message
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Logical_DetachResult_Status"></a> Status

結果の分類です。

```csharp
public readonly DetachStatus Status
```

#### 値（Field Value）

 [DetachStatus](Omni.Logical.DetachStatus.md)
