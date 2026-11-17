# <a id="Omni_Logical_IRadialBatchCameraFacingLabelProvider"></a> Interface IRadialBatchCameraFacingLabelProvider

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

BRG上でカメラ正対するラベルへ、カメラ非依存の論理アンカー姿勢を供給します。

```csharp
public interface IRadialBatchCameraFacingLabelProvider : IRadialRigidAnchorProvider
```

#### 実装するインターフェース（Implements）

[IRadialRigidAnchorProvider](Omni.Logical.IRadialRigidAnchorProvider.md)

## 補足（Remarks）

カメラごとの表面位置とbillboard基底はGPUの共有カメラpacketから導出します。
そのため、ProviderはRendererのTransformを書き換えず、親球などの安定した正本だけを
返してください。

## メソッド（Methods）

### <a id="Omni_Logical_IRadialBatchCameraFacingLabelProvider_TryGetBatchAnchorPose_Omni_Logical_RenderPose__"></a> TryGetBatchAnchorPose\(out RenderPose\)

カメラ非依存の論理アンカー姿勢を返します。

```csharp
bool TryGetBatchAnchorPose(out RenderPose pose)
```

#### 引数（Parameters）

`pose` [RenderPose](Omni.Logical.RenderPose.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
