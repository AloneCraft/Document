# <a id="Omni_Logical_ISceneViewPositionProvider"></a> Interface ISceneViewPositionProvider

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

Scene View の高精度表示に使うワールド論理位置を提供します。

<p>
CameraCombinationVerification など、Unity の <code>Transform.position</code> だけでは
下位ビットを保持できない対象に付く <xref href="Omni.Logical.Transform" data-throw-if-not-resolved="false"></xref> と同じ契約です。
実装しない対象は描画を継続できますが、Scene View 上では精度保証外として扱われます。
</p>

```csharp
public interface ISceneViewPositionProvider
```

## メソッド（Methods）

### <a id="Omni_Logical_ISceneViewPositionProvider_TryGetWorld_Omni_Logical_Position3__Omni_Logical_Quaternion__Omni_Logical_Scalar__"></a> TryGetWorld\(out Position3, out Quaternion, out Scalar\)

固定小数点のワールド論理姿勢を取得します。

```csharp
bool TryGetWorld(out Position3 worldPosition, out Quaternion worldRotation, out Scalar worldScale)
```

#### 引数（Parameters）

`worldPosition` [Position3](Omni.Logical.Position3.md)

論理ワールド位置。失敗時はゼロです。

`worldRotation` [Quaternion](Omni.Logical.Quaternion.md)

論理ワールド回転。失敗時は恒等回転です。

`worldScale` [Scalar](Omni.Logical.Scalar.md)

論理ワールド一様スケール。失敗時は1です。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

精密な論理姿勢を取得できた場合はtrueです。
