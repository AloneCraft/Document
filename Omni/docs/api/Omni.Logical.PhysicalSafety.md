# <a id="Omni_Logical_PhysicalSafety"></a> Class PhysicalSafety

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

```csharp
[MovedFrom(true, "Omni", null, "LogicalPhysicalSafety")]
public static class PhysicalSafety
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PhysicalSafety](Omni.Logical.PhysicalSafety.md)

## フィールド（Fields）

### <a id="Omni_Logical_PhysicalSafety_DefaultLimit"></a> DefaultLimit

既定のUnity標準Transform安全域です。単位はメートルです。
float の刻み（ulp）は 1e4 m で約 1 mm、1e5 m で約 7.8 mm、1e6 m で約 6.3 cm です。既定は、標準の描画経路で 1 mm の刻みを保てる上限です。
Unity にこの値を問い合わせる API は無いので、固定値としてここで定めます。利用者が変える設定欄はありません（<xref href="Omni.Logical.PhysicalSafety.Limit" data-throw-if-not-resolved="false"></xref>の setter はテストが使います）。

```csharp
public const float DefaultLimit = 10000
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

## プロパティ（Properties）

### <a id="Omni_Logical_PhysicalSafety_Limit"></a> Limit

現在のEditorセッションまたは実行環境で使う安全域です。

```csharp
public static float Limit { get; set; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Logical_PhysicalSafety_Mode"></a> Mode

現在の有限プロキシ強制モードです。

```csharp
public static PhysicalSafetyMode Mode { get; set; }
```

#### 値（Property Value）

 [PhysicalSafetyMode](Omni.Logical.PhysicalSafetyMode.md)

## メソッド（Methods）

### <a id="Omni_Logical_PhysicalSafety_Evaluate_Omni_Logical_RenderPose__UnityEngine_Bounds__"></a> Evaluate\(in RenderPose, in Bounds\)

論理姿勢で変換したローカルBounds全体が、現在の物理安全域へ収まるか判定します。

```csharp
public static PhysicalSafetyResult Evaluate(in RenderPose pose, in Bounds localBounds)
```

#### 引数（Parameters）

`pose` [RenderPose](Omni.Logical.RenderPose.md)

`localBounds` Bounds

#### 戻り値（Returns）

 [PhysicalSafetyResult](Omni.Logical.PhysicalSafetyResult.md)

### <a id="Omni_Logical_PhysicalSafety_ResetDefaults"></a> ResetDefaults\(\)

デバッグ上書きを既定値へ戻します。

```csharp
public static void ResetDefaults()
```
