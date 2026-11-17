# <a id="Omni_Editor_Diagnostics_OmniInputDeliveryRecorder"></a> Class OmniInputDeliveryRecorder

Namespace: [Omni.Editor.Diagnostics](Omni.Editor.Diagnostics.md)  
Assembly: Omni.Editor.dll  

実入力が Unity に届いたかを、読み取り専用で記録します。開いている EditorWindow のパネルの visualTree に
TrickleDown で、Scene View には <xref href="UnityEditor.SceneView.beforeSceneGui" data-throw-if-not-resolved="false"></xref> で登録します。イベントを消費も変更もせず
（Use、StopPropagation、PreventDefault、フォーカスや hotControl の変更をしません）、購読は
<xref href="Omni.Editor.Diagnostics.OmniInputDeliveryRecorder.Start(System.String)" data-throw-if-not-resolved="false"></xref> から <xref href="Omni.Editor.Diagnostics.OmniInputDeliveryRecorder.Stop(System.String%2cSystem.String%40)" data-throw-if-not-resolved="false"></xref> までだけです。非アクティブな間にコストはありません。

```csharp
public static class OmniInputDeliveryRecorder
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniInputDeliveryRecorder](Omni.Editor.Diagnostics.OmniInputDeliveryRecorder.md)

## 補足（Remarks）

ホバー移動は記録しません（カーソルが乗っただけで「届いた」と数えないため）。記録は Unity のどこかへ届いたことを示し、
目的の要素へ届いたことや、Overlay に覆われていないことは示しません。

## フィールド（Fields）

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryRecorder_Capacity"></a> Capacity

リングバッファの容量です。

```csharp
public const int Capacity = 512
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryRecorder_MaximumFilterLength"></a> MaximumFilterLength

```csharp
public const int MaximumFilterLength = 64
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryRecorder_MaximumLifetimeSeconds"></a> MaximumLifetimeSeconds

開始からの寿命の上限（秒）です。外部ランナーが止まって <xref href="Omni.Editor.Diagnostics.OmniInputDeliveryRecorder.Stop(System.String%2cSystem.String%40)" data-throw-if-not-resolved="false"></xref> を送れなかったときに、
購読が残り続けるのを防ぎます。

```csharp
public const double MaximumLifetimeSeconds = 300
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryRecorder_ReadObserverName"></a> ReadObserverName

```csharp
public const string ReadObserverName = "pointer-log-read"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryRecorder_StartObserverName"></a> StartObserverName

```csharp
public const string StartObserverName = "pointer-log-start"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## プロパティ（Properties）

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryRecorder_ActiveSession"></a> ActiveSession

有効なセッションの ID（32 桁の小文字 16 進）です。非アクティブなら空文字です。

```csharp
public static string ActiveSession { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryRecorder_IsActive"></a> IsActive

セッションが有効（購読中）なら true です。

```csharp
public static bool IsActive { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryRecorder_Read_System_String_System_Int64_System_String_System_Boolean_System_Int32_"></a> Read\(string, long, string, bool, int\)

記録を読みます（同期。記録は消しません）。<code class="paramref">sinceUtcTicks</code> 以降で、filter と
<code class="paramref">expectations</code> に一致するイベントの数を、<xref href="Omni.Editor.Diagnostics.OmniObservationPreconditions.EvaluateInputDelivery(System.String%2cOmni.Editor.Diagnostics.OmniInputDeliveryEvidence%40)" data-throw-if-not-resolved="false"></xref>
で判定して <xref href="Omni.Editor.Diagnostics.OmniInputDeliveryReadResult.observation" data-throw-if-not-resolved="false"></xref> に入れます。

```csharp
public static OmniInputDeliveryReadResult Read(string requestedSession, long sinceUtcTicks, string expectations, bool testRunDuringSession, int otherAutomationRequestsDuringSession)
```

#### 引数（Parameters）

`requestedSession` [string](https://learn.microsoft.com/dotnet/api/system.string)

読むセッションの ID です。空なら現在のセッションです。

`sinceUtcTicks` [long](https://learn.microsoft.com/dotnet/api/system.int64)

入力の直前の時刻（<xref href="System.DateTime.UtcNow" data-throw-if-not-resolved="false"></xref> の Ticks）です。0 なら全件です。

`expectations` [string](https://learn.microsoft.com/dotnet/api/system.string)

カンマ区切りの <code>Kind:arg</code> です。空なら種類を問いません。

`testRunDuringSession` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

セッションの間にテスト実行が進行していました。

`otherAutomationRequestsDuringSession` [int](https://learn.microsoft.com/dotnet/api/system.int32)

セッションの間に受理された、他の自動化の要求の数です。

#### 戻り値（Returns）

 [OmniInputDeliveryReadResult](Omni.Editor.Diagnostics.OmniInputDeliveryReadResult.md)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryRecorder_Start_System_String_"></a> Start\(string\)

記録を始めます。既に有効なセッションがあれば他人のセッションを奪わず、Unavailable
（<xref href="Omni.Editor.Diagnostics.OmniObservationReason.ObservationAlreadyRunning" data-throw-if-not-resolved="false"></xref>）です。購読したパネルが 0 のときは、
後の読み取りが必ず 0 件になるので、理由なしの Failed です。

```csharp
public static OmniInputDeliveryStartResult Start(string windowFilter)
```

#### 引数（Parameters）

`windowFilter` [string](https://learn.microsoft.com/dotnet/api/system.string)

EditorWindow の型名との完全一致、または題に含まれる文字列（大文字小文字を区別しない）です。空なら全ウィンドウです。

#### 戻り値（Returns）

 [OmniInputDeliveryStartResult](Omni.Editor.Diagnostics.OmniInputDeliveryStartResult.md)

#### 例外（Exceptions）

 [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception)

filter が長すぎる、または制御文字や '|' を含む場合。

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryRecorder_Stop_System_String_System_String__"></a> Stop\(string, out string\)

記録を止めます。何度呼んでもかまいません。有効なセッションがあるのに ID が空、または別のセッションを
指すときは、他人のセッションを止めず false を返します。

```csharp
public static bool Stop(string requestedSession, out string detail)
```

#### 引数（Parameters）

`requestedSession` [string](https://learn.microsoft.com/dotnet/api/system.string)

`detail` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryRecorder_TryValidateFilter_System_String_System_String__"></a> TryValidateFilter\(string, out string\)

filter が 0〜64 文字で、制御文字と '|' を含まないかを返します。空は「全ウィンドウ」で有効です。

```csharp
public static bool TryValidateFilter(string filter, out string error)
```

#### 引数（Parameters）

`filter` [string](https://learn.microsoft.com/dotnet/api/system.string)

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
