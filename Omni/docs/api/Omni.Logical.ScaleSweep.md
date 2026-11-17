# <a id="Omni_Logical_ScaleSweep"></a> Class ScaleSweep

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

```csharp
[MovedFrom(true, "Omni", null, "LogicalScaleSweep")]
public static class ScaleSweep
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[ScaleSweep](Omni.Logical.ScaleSweep.md)

## メソッド（Methods）

### <a id="Omni_Logical_ScaleSweep_NormalizeTime_System_Double_System_Double_System_Boolean_System_Boolean_"></a> NormalizeTime\(double, double, bool, bool\)

経過時間を [0,1] の正規化時間へ畳みます。

```csharp
public static double NormalizeTime(double elapsedSeconds, double durationSeconds, bool loop, bool pingPong)
```

#### 引数（Parameters）

`elapsedSeconds` [double](https://learn.microsoft.com/dotnet/api/system.double)

非負の経過秒数。

`durationSeconds` [double](https://learn.microsoft.com/dotnet/api/system.double)

正の総尺（秒）。

`loop` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

終端で先頭へ戻す場合はtrue。

`pingPong` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

終端で折り返す場合はtrue（<code class="paramref">loop</code>より優先）。

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

[0,1] の正規化時間。
