# <a id="Omni_Core"></a> Namespace Omni.Core

### クラス（Classes）

 [RadialDistanceBounds](Omni.Core.RadialDistanceBounds.md)

Logicalカメラ位置またはLogical可動領域とLogical AABBから、放射距離の保守的な範囲を求めます。
GPU側のRadial Warpが再写像するのはこのEuclidean距離であり、Unity行列のZ深度ではありません。
ここで扱う空間値はすべてLogicalであり、失敗時の呼び出し側は可視側へ倒さなければなりません。
