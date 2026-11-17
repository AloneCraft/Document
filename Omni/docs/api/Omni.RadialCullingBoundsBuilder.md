# <a id="Omni_RadialCullingBoundsBuilder"></a> Class RadialCullingBoundsBuilder

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

Logical AABB を GPU の Radial 写像後にも必ず包む、Unity 標準カリング用のワールド Bounds を構築します。
Galaxy と Saturn の通常 MeshRenderer 経路で使い、BRG の独自カリングには使いません。

```csharp
public static class RadialCullingBoundsBuilder
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialCullingBoundsBuilder](Omni.RadialCullingBoundsBuilder.md)

## メソッド（Methods）

### <a id="Omni_RadialCullingBoundsBuilder_CreateFailOpen_UnityEngine_Vector3_Omni_RadialCullingBoundsFailure_System_UInt64_System_UInt64_"></a> CreateFailOpen\(Vector3, RadialCullingBoundsFailure, ulong, ulong\)

```csharp
public static RadialCullingBoundsResult CreateFailOpen(Vector3 requestedCenter, RadialCullingBoundsFailure failure, ulong cameraRevision, ulong contentRevision)
```

#### 引数（Parameters）

`requestedCenter` Vector3

`failure` [RadialCullingBoundsFailure](Omni.RadialCullingBoundsFailure.md)

`cameraRevision` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

`contentRevision` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

#### 戻り値（Returns）

 [RadialCullingBoundsResult](Omni.RadialCullingBoundsResult.md)

### <a id="Omni_RadialCullingBoundsBuilder_CreateOutsideShell_System_UInt64_System_UInt64_"></a> CreateOutsideShell\(ulong, ulong\)

shell判定で完全範囲外と確定した場合の結果を作成します。
呼び出し側はこの結果をRegistryへ適用せず、既存の一時Boundsを復元します。

```csharp
public static RadialCullingBoundsResult CreateOutsideShell(ulong cameraRevision, ulong contentRevision)
```

#### 引数（Parameters）

`cameraRevision` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

カメラ状態のrevisionです。

`contentRevision` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

Renderer論理姿勢のrevisionです。

#### 戻り値（Returns）

 [RadialCullingBoundsResult](Omni.RadialCullingBoundsResult.md)

範囲外を表す不変結果です。

### <a id="Omni_RadialCullingBoundsBuilder_TryBuild_Omni_Logical_Aabb__Omni_Logical_Position3__UnityEngine_Vector3_Omni_RadialSettings__System_Boolean_Omni_RadialCullingBoundsResult__"></a> TryBuild\(in Aabb, in Position3, Vector3, in RadialSettings, bool, out RadialCullingBoundsResult\)

Logical AABB をRadial頂点ワープ後に包むワールド Bounds を構築します。

```csharp
public static bool TryBuild(in Aabb logicalBounds, in Position3 logicalWarpCenter, Vector3 physicalWarpCenter, in RadialSettings settings, bool includeUnwarpedCullingVolume, out RadialCullingBoundsResult result)
```

#### 引数（Parameters）

`logicalBounds` [Aabb](Omni.Logical.Aabb.md)

Renderer の Logical ワールド AABB。null相当の値は持てないため、構築不能ならfail-openになります。

`logicalWarpCenter` [Position3](Omni.Logical.Position3.md)

GPUが距離計算の基準にする Logical ワープ中心です。

`physicalWarpCenter` Vector3

描画空間における同じワープ中心です。通常は描画中 Camera の物理位置を渡します。

`settings` [RadialSettings](Omni.RadialSettings.md)

GPUと同一のRadial写像設定です。

`includeUnwarpedCullingVolume` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

Observerなどで非ワープの候補範囲も保持する場合はtrueです。

`result` [RadialCullingBoundsResult](Omni.RadialCullingBoundsResult.md)

常に有限な Bounds を返します。falseの場合もFailOpen Boundsを適用して可視側へ倒します。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

厳密な保守 Bounds を構築できた場合はtrueです。

### <a id="Omni_RadialCullingBoundsBuilder_TryBuild_Omni_Logical_Aabb__Omni_Logical_Position3__UnityEngine_Vector3_Omni_RadialSettings__System_Boolean_System_UInt64_System_UInt64_Omni_RadialCullingBoundsResult__"></a> TryBuild\(in Aabb, in Position3, Vector3, in RadialSettings, bool, ulong, ulong, out RadialCullingBoundsResult\)

revision付きでLogical AABBをRadial頂点ワープ後に包むワールド Bounds を構築します。

```csharp
public static bool TryBuild(in Aabb logicalBounds, in Position3 logicalWarpCenter, Vector3 physicalWarpCenter, in RadialSettings settings, bool includeUnwarpedCullingVolume, ulong cameraRevision, ulong contentRevision, out RadialCullingBoundsResult result)
```

#### 引数（Parameters）

`logicalBounds` [Aabb](Omni.Logical.Aabb.md)

Renderer の Logical ワールド AABBです。

`logicalWarpCenter` [Position3](Omni.Logical.Position3.md)

GPUが距離計算の基準にする Logical ワープ中心です。

`physicalWarpCenter` Vector3

描画空間における同じワープ中心です。

`settings` [RadialSettings](Omni.RadialSettings.md)

GPUと同一のRadial写像設定です。

`includeUnwarpedCullingVolume` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

非ワープ候補範囲もBoundsへ和集合で含める場合はtrueです。

`cameraRevision` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

カメラ状態の単調増加revisionです。不明な呼び出しでは0を渡します。

`contentRevision` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

Renderer論理姿勢のrevisionです。不明な呼び出しでは0を渡します。

`result` [RadialCullingBoundsResult](Omni.RadialCullingBoundsResult.md)

常に有限な Bounds を返します。falseの場合もFailOpen Boundsを適用して可視側へ倒します。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

厳密な保守 Bounds を構築できた場合はtrueです。

### <a id="Omni_RadialCullingBoundsBuilder_TryBuild_Omni_Logical_Aabb__Omni_Logical_Position3__Omni_Logical_Position3__UnityEngine_Vector3_Omni_RadialSettings__System_Boolean_System_UInt64_System_UInt64_Omni_RadialCullingBoundsResult__"></a> TryBuild\(in Aabb, in Position3, in Position3, Vector3, in RadialSettings, bool, ulong, ulong, out RadialCullingBoundsResult\)

Observerのcamera-relative写像を包むBoundsを構築します。
object側の写像距離に加え、GPUが引くeye側の写像距離も半径へ加算します。

```csharp
public static bool TryBuild(in Aabb logicalBounds, in Position3 logicalWarpCenter, in Position3 logicalEye, Vector3 physicalCameraCenter, in RadialSettings settings, bool includeUnwarpedCullingVolume, ulong cameraRevision, ulong contentRevision, out RadialCullingBoundsResult result)
```

#### 引数（Parameters）

`logicalBounds` [Aabb](Omni.Logical.Aabb.md)

Renderer の Logical ワールド AABBです。

`logicalWarpCenter` [Position3](Omni.Logical.Position3.md)

GPUが距離計算の基準にするLogicalワープ中心です。

`logicalEye` [Position3](Omni.Logical.Position3.md)

描画中CameraのLogical eye位置です。

`physicalCameraCenter` Vector3

Unity標準カリング上でBoundsを置く描画Cameraの物理位置です。

`settings` [RadialSettings](Omni.RadialSettings.md)

GPUと同一のRadial写像設定です。

`includeUnwarpedCullingVolume` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

非ワープ候補範囲も和集合へ含める場合はtrueです。

`cameraRevision` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

カメラ状態のrevisionです。

`contentRevision` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

Renderer論理姿勢のrevisionです。

`result` [RadialCullingBoundsResult](Omni.RadialCullingBoundsResult.md)

常に有限な結果です。失敗時はcamera近傍へfail-openします。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

厳密な保守Boundsを構築できた場合はtrueです。
