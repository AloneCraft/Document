# <a id="Omni_RadialRendererBoundsRegistry_Diagnostics"></a> Struct RadialRendererBoundsRegistry.Diagnostics

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

Bounds Registryの累積処理量と直近viewの処理量です。

```csharp
public readonly struct RadialRendererBoundsRegistry.Diagnostics
```

## プロパティ（Properties）

### <a id="Omni_RadialRendererBoundsRegistry_Diagnostics_AppliedCount"></a> AppliedCount

現在保守Boundsを保持しているRenderer数です。

```csharp
public int AppliedCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_RadialRendererBoundsRegistry_Diagnostics_BoundsWriteCount"></a> BoundsWriteCount

Renderer.localBoundsへ適用した総回数です。

```csharp
public long BoundsWriteCount { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_RadialRendererBoundsRegistry_Diagnostics_BoundsWriteSkipCount"></a> BoundsWriteSkipCount

厳密一致によりlocalBounds書込みを省略した総回数です。

```csharp
public long BoundsWriteSkipCount { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_RadialRendererBoundsRegistry_Diagnostics_CachedRecordCount"></a> CachedRecordCount

再利用可能なRecord数です。

```csharp
public int CachedRecordCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_RadialRendererBoundsRegistry_Diagnostics_LastScopeMissingRestoreCount"></a> LastScopeMissingRestoreCount

直近viewでmissingとして差分復元したRenderer数です。

```csharp
public int LastScopeMissingRestoreCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_RadialRendererBoundsRegistry_Diagnostics_LastScopeTouchedCount"></a> LastScopeTouchedCount

直近viewで触ったRenderer数です。

```csharp
public int LastScopeTouchedCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_RadialRendererBoundsRegistry_Diagnostics_RecordCreationCount"></a> RecordCreationCount

起動後に生成したRecord総数です。

```csharp
public long RecordCreationCount { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_RadialRendererBoundsRegistry_Diagnostics_RestoreWriteCount"></a> RestoreWriteCount

元のlocalBoundsへ復元した総回数です。

```csharp
public long RestoreWriteCount { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)
