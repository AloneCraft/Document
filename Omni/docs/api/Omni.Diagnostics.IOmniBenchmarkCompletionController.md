# <a id="Omni_Diagnostics_IOmniBenchmarkCompletionController"></a> Interface IOmniBenchmarkCompletionController

Namespace: [Omni.Diagnostics](Omni.Diagnostics.md)  
Assembly: Radial.Runtime.dll  

ベンチマークの完走・中断・Runner破棄時に、Scene固有の一時構成を復帰する任意契約です。

```csharp
public interface IOmniBenchmarkCompletionController
```

## 補足（Remarks）

実装は複数回呼ばれても安全でなければなりません。既存Scene Controllerは本契約を実装しなくても、
Runnerとの互換性を維持します。

## メソッド（Methods）

### <a id="Omni_Diagnostics_IOmniBenchmarkCompletionController_EndBenchmark"></a> EndBenchmark\(\)

ベンチマーク用に一時変更したCamera、再生状態、その他のScene構成を通常状態へ復帰します。

```csharp
void EndBenchmark()
```
