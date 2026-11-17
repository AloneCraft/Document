# <a id="Omni_Editor_Diagnostics_OmniInputDeliveryEvidence"></a> Struct OmniInputDeliveryEvidence

Namespace: [Omni.Editor.Diagnostics](Omni.Editor.Diagnostics.md)  
Assembly: Omni.Editor.dll  

入力到達ログを、入力の前後で読んだ値です。

```csharp
[Serializable]
public struct OmniInputDeliveryEvidence
```

## フィールド（Fields）

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryEvidence_assemblyReloaded"></a> assemblyReloaded

セッションが assembly の再読み込みで終わったことが記録されていました。

```csharp
public bool assemblyReloaded
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryEvidence_deliveredEventCount"></a> deliveredEventCount

入力の開始時刻以降に記録された、期待した操作のイベントの数です（期待が無ければ全イベント）。

```csharp
public int deliveredEventCount
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryEvidence_droppedEventCount"></a> droppedEventCount

リングバッファから捨てた記録の数です（診断用）。

```csharp
public long droppedEventCount
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryEvidence_otherAutomationRequestsDuringSession"></a> otherAutomationRequestsDuringSession

セッションの間に受理された、状態の照会とログの操作以外の自動化の要求の数です。

```csharp
public int otherAutomationRequestsDuringSession
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryEvidence_sessionMatched"></a> sessionMatched

読んだセッションが、入力の前に始めたセッションと同じで、まだ有効でした。

```csharp
public bool sessionMatched
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryEvidence_testRunDuringSession"></a> testRunDuringSession

セッションの間にテスト実行が進行していました（合成イベントが混ざり得ます）。

```csharp
public bool testRunDuringSession
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
