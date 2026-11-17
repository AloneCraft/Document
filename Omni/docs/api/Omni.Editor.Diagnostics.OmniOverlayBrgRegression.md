# <a id="Omni_Editor_Diagnostics_OmniOverlayBrgRegression"></a> Class OmniOverlayBrgRegression

Namespace: [Omni.Editor.Diagnostics](Omni.Editor.Diagnostics.md)  
Assembly: Omni.Editor.dll  

LogicalOriginalTransformの実Scene ViewでBRGの標準描画と座標保持を検証します。
実オーバーレイイベントとGPU描画を通し、終了時には元の視点・表示状態へ戻します。

```csharp
public static class OmniOverlayBrgRegression
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniOverlayBrgRegression](Omni.Editor.Diagnostics.OmniOverlayBrgRegression.md)

## メソッド（Methods）

### <a id="Omni_Editor_Diagnostics_OmniOverlayBrgRegression_Begin_System_Action_System_Boolean_System_String__"></a> Begin\(Action<bool, string\>\)

開いている再現シーンで近距離・安全域外の表示往復とGPU比較を実行します。

```csharp
public static void Begin(Action<bool, string> completion)
```

#### 引数（Parameters）

`completion` [Action](https://learn.microsoft.com/dotnet/api/system.action\-2)<[bool](https://learn.microsoft.com/dotnet/api/system.boolean), [string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Editor_Diagnostics_OmniOverlayBrgRegression_BeginComparisonDisplay_System_Action_System_Boolean_System_String__"></a> BeginComparisonDisplay\(Action<bool, string\>\)

LogicalOriginalTransformの観察モードを一時的に有効化し、BRG所有対象の比較描画を
実Scene ViewのRepaintとGPUキャプチャで検証します。完了時は表示設定とbackendを戻します。

```csharp
public static void BeginComparisonDisplay(Action<bool, string> completion)
```

#### 引数（Parameters）

`completion` [Action](https://learn.microsoft.com/dotnet/api/system.action\-2)<[bool](https://learn.microsoft.com/dotnet/api/system.boolean), [string](https://learn.microsoft.com/dotnet/api/system.string)\>
