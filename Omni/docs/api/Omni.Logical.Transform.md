# <a id="Omni_Logical_Transform"></a> Class Transform

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

Logical位置・回転・符号付きXYZ Scaleを固定小数点で保持するRuntimeコンポーネントです。
Unity Transformは描画・編集境界の有限プロキシであり、空間の正本にはなりません。
親子合成、Bounds、距離判定はすべてLogical型で行います。

```csharp
[ExecuteAlways]
[DisallowMultipleComponent]
[AddComponentMenu("Omni/Logical Transform")]
[MovedFrom(true, "Omni", null, "LogicalTransform")]
public sealed class Transform : MonoBehaviour, ISceneViewPositionProvider, ISerializationCallbackReceiver
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[Transform](Omni.Logical.Transform.md)

#### 実装するインターフェース（Implements）

[ISceneViewPositionProvider](Omni.Logical.ISceneViewPositionProvider.md), 
ISerializationCallbackReceiver

## プロパティ（Properties）

### <a id="Omni_Logical_Transform_HasDetectedConflictingWriter"></a> HasDetectedConflictingWriter

<xref href="Omni.Logical.Transform.CheckSingleWriterInvariant" data-throw-if-not-resolved="false"></xref>が、このインスタンスについて
単一書き手の不変条件違反を検出済みならtrueです。Inspector等の診断表示から、
Consoleを見ずにこの状態を確認できるようにするためのものです。

```csharp
public bool HasDetectedConflictingWriter { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Transform_IsPoseNeutralizedForFiniteProxy"></a> IsPoseNeutralizedForFiniteProxy

直近の<xref href="Omni.Logical.Transform.SyncUnityTransform" data-throw-if-not-resolved="false"></xref>が、安全域(<xref href="Omni.Logical.PhysicalSafety.Limit" data-throw-if-not-resolved="false"></xref>)を
超えたためUnity Transformを論理姿勢の正本として扱えない状態にした場合にtrueです。

<p>
この状態では Unity Transform の値は精度を落とした写し、Radial Camera用の
camera-relative原点proxy、または表現不能なプレースホルダのいずれかであり、
どの場合も論理姿勢の正本ではありません。位置しきい値の判定や
ギズモのロック可否は、Transform の値ではなくこのプロパティで判断してください
（プレースホルダの場合は <code>position=0</code> なので、値で見ると「安全域内」に
見えてしまいます）。実際にプレースホルダが書かれたかどうかは
<xref href="Omni.Logical.Transform.IsUnityTransformPlaceholder" data-throw-if-not-resolved="false"></xref>で区別してください。
</p>

```csharp
public bool IsPoseNeutralizedForFiniteProxy { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Transform_IsUnityTransformPlaceholder"></a> IsUnityTransformPlaceholder

直近の<xref href="Omni.Logical.Transform.SyncUnityTransform" data-throw-if-not-resolved="false"></xref>が、world姿勢が<xref href="Omni.Logical.Transform.WorldPoseNativeLimit" data-throw-if-not-resolved="false"></xref>を
超えて表現不能だったため、Unity Transformへ中立値
（<code>localPosition=0</code> / <code>localScale=1</code>）のプレースホルダを書き込んだ状態ならtrueです。

<p>
<xref href="Omni.Logical.Transform.IsPoseNeutralizedForFiniteProxy" data-throw-if-not-resolved="false"></xref>がtrueでもこちらがfalseの場合、
Transformには安全域(<xref href="Omni.Logical.PhysicalSafety.Limit" data-throw-if-not-resolved="false"></xref>)は超えているものの
<xref href="Omni.Logical.Transform.WorldPoseNativeLimit" data-throw-if-not-resolved="false"></xref>には収まる、精度を落とした実値または
Radial Camera用のcamera-relative原点proxyが入っています。
</p>

```csharp
public bool IsUnityTransformPlaceholder { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Transform_LocalPosition"></a> LocalPosition

論理ローカル位置を、浮動小数へ変換せず固定小数点のまま取得・設定します。
<xref href="Omni.Logical.Transform.LocalPosition" data-throw-if-not-resolved="false"></xref> 自体が固定小数点の正本です。旧floatビューは存在せず、
Inspector等でもこのAPIを使ってフル精度で編集・表示します。

```csharp
public Vector3 LocalPosition { get; set; }
```

#### 値（Property Value）

 [Vector3](Omni.Logical.Vector3.md)

### <a id="Omni_Logical_Transform_LocalRotation"></a> LocalRotation

論理ローカル回転を、浮動小数へ変換せず固定小数点のまま取得・設定します。
設定値は正規化して保持します。

```csharp
public Quaternion LocalRotation { get; set; }
```

#### 値（Property Value）

 [Quaternion](Omni.Logical.Quaternion.md)

### <a id="Omni_Logical_Transform_LocalScale"></a> LocalScale

符号付きXYZ Scaleを、浮動小数へ変換せず固定小数点のまま取得・設定します。

```csharp
public Vector3 LocalScale { get; set; }
```

#### 値（Property Value）

 [Vector3](Omni.Logical.Vector3.md)

## メソッド（Methods）

### <a id="Omni_Logical_Transform_CaptureFromTransform_UnityEngine_Transform_"></a> CaptureFromTransform\(Transform\)

Unity Transformの現在のワールド姿勢を取り込み、
論理親を考慮してローカル論理値へ変換します。

```csharp
public bool CaptureFromTransform(Transform source)
```

#### 引数（Parameters）

`source` Transform

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Transform_IsInForbiddenHierarchyPlacement"></a> IsInForbiddenHierarchyPlacement\(\)

このLogicalTransformが仕様上禁止されたUnity Hierarchy配置
（LogicalTransform → 通常Transform → LogicalTransformの再開）にあるかどうかを判定します。

```csharp
public bool IsInForbiddenHierarchyPlacement()
```

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Transform_OnAfterDeserialize"></a> OnAfterDeserialize\(\)

<p>Implement this callback to transform data back into runtime data types after an object is deserialized.</p>

```csharp
public void OnAfterDeserialize()
```

### <a id="Omni_Logical_Transform_OnBeforeSerialize"></a> OnBeforeSerialize\(\)

<p>Implement this callback to transform data into serializable data types immediately before an object is serialized.</p>

```csharp
public void OnBeforeSerialize()
```

### <a id="Omni_Logical_Transform_SetWorld_Omni_Logical_Position3__Omni_Logical_Quaternion__Omni_Logical_Vector3__"></a> SetWorld\(in Position3, in Quaternion, in Vector3\)

ワールド論理TRSを固定小数点のまま設定します。
親のゼロScaleなどで逆変換できない場合は何も変更せず失敗します。

```csharp
public bool SetWorld(in Position3 worldPositionFixed, in Quaternion worldRotation, in Vector3 worldScaleFixed)
```

#### 引数（Parameters）

`worldPositionFixed` [Position3](Omni.Logical.Position3.md)

`worldRotation` [Quaternion](Omni.Logical.Quaternion.md)

`worldScaleFixed` [Vector3](Omni.Logical.Vector3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Transform_SyncUnityTransform"></a> SyncUnityTransform\(\)

ローカル論理姿勢（<xref href="Omni.Logical.Transform.LocalPosition" data-throw-if-not-resolved="false"></xref>・<xref href="Omni.Logical.Transform.LocalScale" data-throw-if-not-resolved="false"></xref>、
camera-relative Radialの減算は行いません——ローカル値はそもそもOrigin非依存です）をUnity
Transformへ書き出します。安全域（<xref href="Omni.Logical.PhysicalSafety.Limit" data-throw-if-not-resolved="false"></xref>）を超える
対象は、Unityネイティブが破綻する限界（<xref href="Omni.Logical.Transform.WorldPoseNativeLimit" data-throw-if-not-resolved="false"></xref>）までは
精度を落とした実値を、それを超える場合は有限な代理値（プレースホルダ）を書きます。
ただしRadial Cameraは、論理位置が安全域外ならcamera-relative描画の正本を
<xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref>へ残し、Unity native Cameraの位置だけを原点へ固定します。
巨大なnative Camera位置をUnityのmouse ray・UI・cullingへ渡さないためです。
このLogicalTransformの唯一の正当な書き手です
（他に書き手がいないことをOnEnableのチェックとウォッチドッグで検査しています）。

```csharp
public void SyncUnityTransform()
```

### <a id="Omni_Logical_Transform_TranslateWorld_Omni_Logical_Vector3__"></a> TranslateWorld\(in Vector3\)

固定小数点のワールド差分をローカル論理位置へ変換して加算します。
巨大な絶対位置を浮動小数へ出さないため、Radialギズモの微小移動に使用します。

```csharp
public bool TranslateWorld(in Vector3 worldDelta)
```

#### 引数（Parameters）

`worldDelta` [Vector3](Omni.Logical.Vector3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Transform_TryBakeToUnityTransformLossy_Omni_Logical_DetachResult__"></a> TryBakeToUnityTransformLossy\(out DetachResult\)

現在の論理ローカルTRSを有限なUnity Transformへlossy Bakeします。
float範囲外なら何も変更せず失敗します。

```csharp
public bool TryBakeToUnityTransformLossy(out DetachResult result)
```

#### 引数（Parameters）

`result` [DetachResult](Omni.Logical.DetachResult.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Transform_TryDetach_Omni_Logical_DetachResult__"></a> TryDetach\(out DetachResult\)

LogicalTransformを通常Unity TransformへBakeしてから削除します。
直接のLogical子は1段上へ昇格し、現在のワールド論理姿勢を維持します。

```csharp
public bool TryDetach(out DetachResult result)
```

#### 引数（Parameters）

`result` [DetachResult](Omni.Logical.DetachResult.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Transform_TryGetWorld_Omni_Logical_Position3__Omni_Logical_Quaternion__Omni_Logical_Scalar__"></a> TryGetWorld\(out Position3, out Quaternion, out Scalar\)

論理親を考慮したワールド論理値を、固定小数点のまま（浮動小数へ変換せず）取得します。
カメラ相対差の計算を固定小数点精度のまま行うために使います。

```csharp
public bool TryGetWorld(out Position3 worldPosition, out Quaternion worldRotation, out Scalar worldScale)
```

#### 引数（Parameters）

`worldPosition` [Position3](Omni.Logical.Position3.md)

`worldRotation` [Quaternion](Omni.Logical.Quaternion.md)

`worldScale` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Transform_TryGetWorldAffine_Omni_Logical_Position3__Omni_Logical_Matrix3x3__"></a> TryGetWorldAffine\(out Position3, out Matrix3x3\)

論理親を含むワールド位置と、回転・非均一Scale・Shearを保持する基底を返します。

```csharp
public bool TryGetWorldAffine(out Position3 worldPosition, out Matrix3x3 worldBasis)
```

#### 引数（Parameters）

`worldPosition` [Position3](Omni.Logical.Position3.md)

`worldBasis` [Matrix3x3](Omni.Logical.Matrix3x3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Transform_TryGetWorldTrs_Omni_Logical_Position3__Omni_Logical_Quaternion__Omni_Logical_Vector3__"></a> TryGetWorldTrs\(out Position3, out Quaternion, out Vector3\)

符号付きXYZ Scaleを含むワールド論理TRSを固定小数点のまま返します。

```csharp
public bool TryGetWorldTrs(out Position3 worldPosition, out Quaternion worldRotation, out Vector3 worldScale)
```

#### 引数（Parameters）

`worldPosition` [Position3](Omni.Logical.Position3.md)

`worldRotation` [Quaternion](Omni.Logical.Quaternion.md)

`worldScale` [Vector3](Omni.Logical.Vector3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
