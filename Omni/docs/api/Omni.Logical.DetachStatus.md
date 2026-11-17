# <a id="Omni_Logical_DetachStatus"></a> Enum DetachStatus

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

LogicalTransformのDetach結果です。

```csharp
public enum DetachStatus
```

## フィールド（Fields）

`AlreadyDetached = 1` 

対象が既に削除済みです。



`ConversionFailed = 5` 

論理値の変換に失敗しました。



`FloatRangeExceeded = 2` 

位置またはScaleがfloatの有限範囲を超えています。



`InvalidHierarchy = 3` 

論理階層を安全にBakeできません。



`SingularParent = 4` 

ゼロScale等により親基底の逆変換ができません。



`Success = 0` 

通常Unity TransformへのBakeと削除が完了しました。
