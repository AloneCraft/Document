# <a id="Omni_Diagnostics_IOmniBenchmarkDescriptorProvider"></a> Interface IOmniBenchmarkDescriptorProvider

Namespace: [Omni.Diagnostics](Omni.Diagnostics.md)  
Assembly: Radial.Runtime.dll  

warmup後や採取フレームの開始時に、実際に成立している描画backendと比較可能性を再取得する任意契約です。

```csharp
public interface IOmniBenchmarkDescriptorProvider
```

## 補足（Remarks）

<xref href="Omni.Diagnostics.IOmniBenchmarkSceneController" data-throw-if-not-resolved="false"></xref>の初回準備時点では、非同期の派生キャッシュやCamera別BRG viewが
まだ準備中であることがあります。Runnerはこの任意契約を実装したControllerに対してだけ、設定を変更せず
実状態を再照会します。準備未完了を比較可能として返してはいけません。

## メソッド（Methods）

### <a id="Omni_Diagnostics_IOmniBenchmarkDescriptorProvider_TryGetBenchmarkDescriptor_Omni_Diagnostics_OmniBenchmarkSceneDescriptor__System_String__"></a> TryGetBenchmarkDescriptor\(out OmniBenchmarkSceneDescriptor, out string\)

現在の不変コンテンツと実backendから、比較可能性を再計算します。

```csharp
bool TryGetBenchmarkDescriptor(out OmniBenchmarkSceneDescriptor descriptor, out string rejectionReason)
```

#### 引数（Parameters）

`descriptor` [OmniBenchmarkSceneDescriptor](Omni.Diagnostics.OmniBenchmarkSceneDescriptor.md)

成功時の現在のScene記述子。失敗時は比較不能な値を返します。

`rejectionReason` [string](https://learn.microsoft.com/dotnet/api/system.string)

再照会不能な場合の機械可読な理由。成功時は空文字列です。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

記述子を安全に取得できた場合はtrueです。
