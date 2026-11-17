# <a id="Omni_Units"></a> Namespace Omni.Units

### 構造体（Structs）

 [Angle](Omni.Units.Angle.md)

1回転を2^64分割した循環角です。0を含み1 turnを含まないQ0.64表現です。

 [AngularVelocity](Omni.Units.AngularVelocity.md)

角速度を保持する符号付きQ31.96固定小数点値です。
公開入出力はrad/s、内部値は位相加算を正確に行えるturn/sです。

 [Duration](Omni.Units.Duration.md)

秒を保持する符号付きQ63.64固定小数点値です。
シーケンス・物理・音声時刻のCPU側Source of Truthに使用します。

 [Energy](Omni.Units.Energy.md)

ジュールをSI正規単位とする非負のエネルギーです。
光子、電子ボルト、質量エネルギー、宇宙規模の総エネルギーを同じ型で扱います。

 [GravitationalParameter](Omni.Units.GravitationalParameter.md)

重力パラメータμをm³/s²で保持する10進科学表記型です。
桁域はScientific128、軌道演算への変換先はScalar（Q95.96）です。

 [Mass](Omni.Units.Mass.md)

キログラムをSI正規単位とする非負の質量です。
座標用の固定小数点とは分離し、128-bit係数と10進指数で広い桁域を保持します。

 [TimeScale](Omni.Units.TimeScale.md)

時間倍率を保持する符号付きQ31.96固定小数点値です。

 [UnitInterval](Omni.Units.UnitInterval.md)

0以上1以下の比率を保持するQ1.126固定小数点値です。
