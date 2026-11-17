# <a id="Omni_Logical_PhysicalSafetyResult"></a> Struct PhysicalSafetyResult

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

論理AABBをUnity標準空間へ置けるか判定した結果です。

```csharp
public readonly struct PhysicalSafetyResult
```

## フィールド（Fields）

### <a id="Omni_Logical_PhysicalSafetyResult_Bounds"></a> Bounds

LogicalワールドAABBです。安全域外でも失われない正本です。

```csharp
public readonly Aabb Bounds
```

#### 値（Field Value）

 [Aabb](Omni.Logical.Aabb.md)

### <a id="Omni_Logical_PhysicalSafetyResult_IsSafe"></a> IsSafe

元RendererとColliderをUnity標準経路で使用できる場合はtrueです。

```csharp
public readonly bool IsSafe
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_PhysicalSafetyResult_Maximum"></a> Maximum

安全域内AABBのfloat描画空間最大値です。

```csharp
public readonly float3 Maximum
```

#### 値（Field Value）

 float3

### <a id="Omni_Logical_PhysicalSafetyResult_Minimum"></a> Minimum

安全域内AABBのfloat描画空間最小値です。

```csharp
public readonly float3 Minimum
```

#### 値（Field Value）

 float3

### <a id="Omni_Logical_PhysicalSafetyResult_Reason"></a> Reason

診断表示用の判定理由です。

```csharp
public readonly string Reason
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
