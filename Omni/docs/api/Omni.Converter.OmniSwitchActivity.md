# <a id="Omni_Converter_OmniSwitchActivity"></a> Class OmniSwitchActivity

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

描画切替の最中に、進捗バーと段階ごとの所要時間を出します。
切替は1回の同期処理で数分かかることがあり、その間ウィンドウは再描画されないため、
固まっていないことを進捗バーで示します。途中までの適用は安全でないため、キャンセルは用意しません。
入れ子の呼び出しは最も外側の <xref href="Omni.Converter.OmniSwitchActivity.Begin(System.String)" data-throw-if-not-resolved="false"></xref> / <xref href="Omni.Converter.OmniSwitchActivity.End" data-throw-if-not-resolved="false"></xref> だけが表示とログを担当します。

```csharp
public static class OmniSwitchActivity
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniSwitchActivity](Omni.Converter.OmniSwitchActivity.md)

## プロパティ（Properties）

### <a id="Omni_Converter_OmniSwitchActivity_IsActive"></a> IsActive

切替（最も外側の Begin から End まで）の中かどうかです。

```csharp
public static bool IsActive { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniSwitchActivity_Session"></a> Session

切替1回ごとに増える番号です。索引などを、同じ切替の中だけで使い回すために使います。

```csharp
public static int Session { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_Converter_OmniSwitchActivity_Begin_System_String_"></a> Begin\(string\)

切替の開始です。最も外側の呼び出しだけが計測を開始します。

```csharp
public static void Begin(string title)
```

#### 引数（Parameters）

`title` [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniSwitchActivity_End"></a> End\(\)

切替の終了です。最も外側で、進捗バーを消して段階ごとの所要時間を1行でログに出します。

```csharp
public static void End()
```

### <a id="Omni_Converter_OmniSwitchActivity_Measure_System_String_"></a> Measure\(string\)

段階の所要時間を計ります。<code>using</code> で囲みます。計測中でなければ何もしません。

```csharp
public static IDisposable Measure(string stage)
```

#### 引数（Parameters）

`stage` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

### <a id="Omni_Converter_OmniSwitchActivity_Report_System_String_System_Int32_System_Int32_"></a> Report\(string, int, int\)

進捗を表示します。<code class="paramref">total</code> が 0 以下のときは、段階名だけを出します。
表示は一定間隔に間引くので、繰り返しの中で毎回呼んで構いません。

```csharp
public static void Report(string stage, int done, int total)
```

#### 引数（Parameters）

`stage` [string](https://learn.microsoft.com/dotnet/api/system.string)

`done` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`total` [int](https://learn.microsoft.com/dotnet/api/system.int32)
