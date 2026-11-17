# <a id="Omni_Diagnostics_OmniBenchmarkCullingMode"></a> Enum OmniBenchmarkCullingMode

Namespace: [Omni.Diagnostics](Omni.Diagnostics.md)  
Assembly: Radial.Runtime.dll  

ベンチマーク中に適用する粒子カリング方式を表します。

```csharp
public enum OmniBenchmarkCullingMode
```

## フィールド（Fields）

`AllResidentVisible = 3` 

Resident全件を表示する診断専用方式です。



`FrustumOnly = 1` 

通常の錐台判定だけを使用します。



`Omni = 2` 

Omniの時間窓セル・shell判定を使用します。



`Unspecified = 0` 

シーン固有の既定値を使用します。
