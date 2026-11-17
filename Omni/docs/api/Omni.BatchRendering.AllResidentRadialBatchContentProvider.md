# <a id="Omni_BatchRendering_AllResidentRadialBatchContentProvider"></a> Class AllResidentRadialBatchContentProvider

Namespace: [Omni.BatchRendering](Omni.BatchRendering.md)  
Assembly: Omni.BatchRendering.Runtime.dll  

診断専用のAllResidentVisible providerです。

<p>
Saturnの性能比較ではFrustumOnly/Omniを主比較とし、本providerはBRG配線、GPU capture、
false-negative調査だけに使います。benchmark JSONではこのproviderを使った結果を
validForComparison=falseとして記録します。
</p>

```csharp
public sealed class AllResidentRadialBatchContentProvider : IRadialBatchContentProvider
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[AllResidentRadialBatchContentProvider](Omni.BatchRendering.AllResidentRadialBatchContentProvider.md)

#### 実装するインターフェース（Implements）

[IRadialBatchContentProvider](Omni.BatchRendering.IRadialBatchContentProvider.md)

## コンストラクター（Constructors）

### <a id="Omni_BatchRendering_AllResidentRadialBatchContentProvider__ctor_System_Int32_"></a> AllResidentRadialBatchContentProvider\(int\)

固定Resident数を指定してproviderを作成します。
<param name="residentInstanceCount">sentinelを除く粒子数。0以下は無効でadapterがMacroOnlyへ縮退します。</param>

```csharp
public AllResidentRadialBatchContentProvider(int residentInstanceCount)
```

#### 引数（Parameters）

`residentInstanceCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="Omni_BatchRendering_AllResidentRadialBatchContentProvider_ResidentInstanceCount"></a> ResidentInstanceCount

sentinelを除くResident粒子数です。

```csharp
public int ResidentInstanceCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_BatchRendering_AllResidentRadialBatchContentProvider_ScheduleCulling_Omni_BatchRendering_RadialBatchCullingInput__Unity_Collections_NativeArray_System_Int32__Unity_Collections_NativeReference_System_Int32__Unity_Jobs_JobHandle_"></a> ScheduleCulling\(in RadialBatchCullingInput, NativeArray<int\>, NativeReference<int\>, JobHandle\)

可視IDを求めるJobをscheduleします。

```csharp
public JobHandle ScheduleCulling(in RadialBatchCullingInput input, NativeArray<int> visibleInstanceIndices, NativeReference<int> visibleInstanceCount, JobHandle dependency)
```

#### 引数（Parameters）

`input` [RadialBatchCullingInput](Omni.BatchRendering.RadialBatchCullingInput.md)

Camera別の安全なculling入力。Unity ObjectやGPU資源は含みません。

`visibleInstanceIndices` NativeArray<[int](https://learn.microsoft.com/dotnet/api/system.int32)\>

adapterが確保した長さResidentInstanceCountの出力配列。1始まりIDだけを書き込みます。

`visibleInstanceCount` NativeReference<[int](https://learn.microsoft.com/dotnet/api/system.int32)\>

adapterが確保した1要素出力。書いた可視ID数を0..ResidentInstanceCountで設定します。

`dependency` JobHandle

既存依存。inputのNativeArrayを読むJobは返却値でこのdependencyへ連結してください。

#### 戻り値（Returns）

 JobHandle

出力配列とinputのNativeArrayへの依存をすべて含むJobHandleです。
