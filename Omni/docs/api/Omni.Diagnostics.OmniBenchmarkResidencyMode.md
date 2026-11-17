# <a id="Omni_Diagnostics_OmniBenchmarkResidencyMode"></a> Enum OmniBenchmarkResidencyMode

Namespace: [Omni.Diagnostics](Omni.Diagnostics.md)  
Assembly: Radial.Runtime.dll  

ベンチマーク中に適用する粒子常駐方式を表します。

```csharp
public enum OmniBenchmarkResidencyMode
```

## フィールド（Fields）

`Resident = 1` 

全対象粒子を常駐させます。



`Streaming = 2` 

時刻窓に応じて粒子資源をストリーミングします。



`Unspecified = 0` 

シーン固有の既定値を使用します。
