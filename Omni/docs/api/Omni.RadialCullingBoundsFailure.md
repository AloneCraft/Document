# <a id="Omni_RadialCullingBoundsFailure"></a> Enum RadialCullingBoundsFailure

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

保守 Bounds を厳密に構築できなかった理由です。診断画面では原因別の件数集計に使います。

```csharp
public enum RadialCullingBoundsFailure
```

## フィールド（Fields）

`CullingDisabled = 7` 

診断でカリングを使用しないため、可視側Boundsを強制しました。



`DistanceRangeUnavailable = 3` 

Logical AABB とワープ中心の距離範囲を計算できません。



`EyeDistanceUnavailable = 6` 

ObserverのLogical eyeとワープ中心の距離、またはその写像を解決できません。



`InvalidBounds = 2` 

Logical AABB の最小・最大座標を解決できません。



`InvalidPhysicalWarpCenter = 1` 

物理ワープ中心が有限な Unity 座標でありません。



`MappedBoundsOutOfRange = 5` 

写像済み Bounds が Unity に渡せる有限範囲を超えました。



`MappedDistanceUnavailable = 4` 

最大論理距離を描画距離へ写像できません。



`None = 0` 

失敗はありません。



`UnwarpedVolumeUnavailable = 8` 

要求された非ワープ Bounds を有限な物理座標へ解決できません。
