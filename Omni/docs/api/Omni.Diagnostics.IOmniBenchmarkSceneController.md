# <a id="Omni_Diagnostics_IOmniBenchmarkSceneController"></a> Interface IOmniBenchmarkSceneController

Namespace: [Omni.Diagnostics](Omni.Diagnostics.md)  
Assembly: Radial.Runtime.dll  

Benchmark Runnerからシーン固有の設定・実測カウンターを取得する公開契約です。

```csharp
public interface IOmniBenchmarkSceneController
```

## 補足（Remarks）

Saturnなどのシーンは、このインターフェースを実装する単一の<xref href="UnityEngine.MonoBehaviour" data-throw-if-not-resolved="false"></xref>
をScene内へ置きます。Runnerはwarmup前に一度だけ要求を渡し、採取フレームごとに
<xref href="Omni.Diagnostics.IOmniBenchmarkSceneController.CaptureBenchmarkCounters" data-throw-if-not-resolved="false"></xref>を呼びます。

## メソッド（Methods）

### <a id="Omni_Diagnostics_IOmniBenchmarkSceneController_CaptureBenchmarkCounters"></a> CaptureBenchmarkCounters\(\)

現フレームのカリング・描画カウンターをallocationなしで返します。

```csharp
OmniBenchmarkCounters CaptureBenchmarkCounters()
```

#### 戻り値（Returns）

 [OmniBenchmarkCounters](Omni.Diagnostics.OmniBenchmarkCounters.md)

現フレームの実測カウンターです。

### <a id="Omni_Diagnostics_IOmniBenchmarkSceneController_TryPrepareBenchmark_Omni_Diagnostics_OmniBenchmarkRequest_Omni_Diagnostics_OmniBenchmarkSceneDescriptor__System_String__"></a> TryPrepareBenchmark\(OmniBenchmarkRequest, out OmniBenchmarkSceneDescriptor, out string\)

計測開始前に要求を適用し、実際に成立したbackend・content情報を返します。

```csharp
bool TryPrepareBenchmark(OmniBenchmarkRequest request, out OmniBenchmarkSceneDescriptor descriptor, out string rejectionReason)
```

#### 引数（Parameters）

`request` [OmniBenchmarkRequest](Omni.Diagnostics.OmniBenchmarkRequest.md)

不変のベンチマーク要求です。

`descriptor` [OmniBenchmarkSceneDescriptor](Omni.Diagnostics.OmniBenchmarkSceneDescriptor.md)

適用後の不変シーン記述子です。

`rejectionReason` [string](https://learn.microsoft.com/dotnet/api/system.string)

適用不能な場合の機械可読な理由です。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

要求を計測前に完全適用できた場合はtrueです。
