# <a id="Omni_RadialCullingBoundsResult"></a> Struct RadialCullingBoundsResult

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

1 Renderer・1 カメラ描画スコープに対する標準カリング用 Bounds の不変結果です。

```csharp
public readonly struct RadialCullingBoundsResult
```

## フィールド（Fields）

### <a id="Omni_RadialCullingBoundsResult_CameraRevision"></a> CameraRevision

呼び出し側が渡したカメラ状態の revision です。

```csharp
public readonly ulong CameraRevision
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_RadialCullingBoundsResult_ContentRevision"></a> ContentRevision

呼び出し側が渡した Renderer 論理姿勢の revision です。

```csharp
public readonly ulong ContentRevision
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_RadialCullingBoundsResult_Failure"></a> Failure

FailOpen の原因です。<xref href="Omni.RadialCullingBoundsStatus.Ready" data-throw-if-not-resolved="false"></xref>ではNoneです。

```csharp
public readonly RadialCullingBoundsFailure Failure
```

#### 値（Field Value）

 [RadialCullingBoundsFailure](Omni.RadialCullingBoundsFailure.md)

### <a id="Omni_RadialCullingBoundsResult_Status"></a> Status

構築の最終状態です。

```csharp
public readonly RadialCullingBoundsStatus Status
```

#### 値（Field Value）

 [RadialCullingBoundsStatus](Omni.RadialCullingBoundsStatus.md)

### <a id="Omni_RadialCullingBoundsResult_WorldBounds"></a> WorldBounds

Unity の標準カリングへ設定する有限なワールド AABB です。

```csharp
public readonly Bounds WorldBounds
```

#### 値（Field Value）

 Bounds

## プロパティ（Properties）

### <a id="Omni_RadialCullingBoundsResult_IsReady"></a> IsReady

厳密な保守 Bounds を使える場合はtrueです。

```csharp
public bool IsReady { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_RadialCullingBoundsResult_IsVisibleCandidate"></a> IsVisibleCandidate

可視候補として Unity カリングへ渡してよい場合はtrueです。

```csharp
public bool IsVisibleCandidate { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
