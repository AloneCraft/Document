# <a id="VirtualizedGeometry_VirtualGeometryRefineMode"></a> Enum VirtualGeometryRefineMode

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

cluster の DAG の細分化（どの group の出力を描くか）の決め方。値は選択の compute の <code>_VGIndependentCut</code> と同じ。
どの方式でも、cut は閉包を取り、穴も重なりも作らない（CPU 参照 <xref href="VirtualizedGeometry.VirtualGeometryCpuReferenceSelector" data-throw-if-not-resolved="false"></xref> が同じ規則を持つ）。

```csharp
public enum VirtualGeometryRefineMode
```

## フィールド（Fields）

`Chained = 0` 

段ごとに順に決める: 出力を使う group（消費者）がすべて細分化したときだけ、自分を細分化する。段の数だけ dispatch が直列になる。変換器の版が古い asset（親の誤差が子の 1.25 倍以上でない）は常にこの方式。



`Independent = 1` 

group ごとに独立に決める（ヒステリシスなし）。誤差が単調で、常駐から求めた ready を使うので、閉包が成り立つ。



`IndependentWithHysteresis = 2` 

group ごとに独立に決め、前フレームの状態で閾値を ±ヒステリシス動かす（既定）。変換器が親の誤差を子の 1.25 倍以上にした asset で、Chained と同じ cut になる。
