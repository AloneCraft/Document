# <a id="Omni_BatchRendering_IRadialBatchContentProvider"></a> Interface IRadialBatchContentProvider

Namespace: [Omni.BatchRendering](Omni.BatchRendering.md)  
Assembly: Omni.BatchRendering.Runtime.dll  

Radial BRGへ安全なJob入力だけを公開するMeso粒子content providerです。

<p>
draw command、TempJob native pointer、GraphicsBuffer、BatchIDの確保・破棄は一切行わず、
<xref href="Omni.BatchRendering.RadialBatchRendererAdapter" data-throw-if-not-resolved="false"></xref> が所有します。可視IDは必ず1..ResidentInstanceCountで、
0はadapterの退化sentinelとして予約されます。
</p>

```csharp
public interface IRadialBatchContentProvider
```

## プロパティ（Properties）

### <a id="Omni_BatchRendering_IRadialBatchContentProvider_ResidentInstanceCount"></a> ResidentInstanceCount

sentinelを除くResident粒子数です。

```csharp
int ResidentInstanceCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_BatchRendering_IRadialBatchContentProvider_ScheduleCulling_Omni_BatchRendering_RadialBatchCullingInput__Unity_Collections_NativeArray_System_Int32__Unity_Collections_NativeReference_System_Int32__Unity_Jobs_JobHandle_"></a> ScheduleCulling\(in RadialBatchCullingInput, NativeArray<int\>, NativeReference<int\>, JobHandle\)

可視IDを求めるJobをscheduleします。

```csharp
JobHandle ScheduleCulling(in RadialBatchCullingInput input, NativeArray<int> visibleInstanceIndices, NativeReference<int> visibleInstanceCount, JobHandle dependency)
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
