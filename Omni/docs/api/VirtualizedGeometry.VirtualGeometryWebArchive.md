# <a id="VirtualizedGeometry_VirtualGeometryWebArchive"></a> Class VirtualGeometryWebArchive

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

page archive(streaming 形式)の先頭から metadata を取り、streaming の controller を作るための入力を返す。

```csharp
public sealed class VirtualGeometryWebArchive
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryWebArchive](VirtualizedGeometry.VirtualGeometryWebArchive.md)

## プロパティ（Properties）

### <a id="VirtualizedGeometry_VirtualGeometryWebArchive_Metadata"></a> Metadata

```csharp
public VirtualGeometryStreamMetadata Metadata { get; }
```

#### 値（Property Value）

 [VirtualGeometryStreamMetadata](VirtualizedGeometry.VirtualGeometryStreamMetadata.md)

### <a id="VirtualizedGeometry_VirtualGeometryWebArchive_Store"></a> Store

```csharp
public VirtualGeometryWebPageStore Store { get; }
```

#### 値（Property Value）

 [VirtualGeometryWebPageStore](VirtualizedGeometry.VirtualGeometryWebPageStore.md)

### <a id="VirtualizedGeometry_VirtualGeometryWebArchive_Url"></a> Url

```csharp
public string Url { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometryWebArchive_OpenAsync_System_String_"></a> OpenAsync\(string\)

同じ url の読み込みは 1 つにまとめる。終わったら登録を外す(次の呼び出しは取り直す)。

```csharp
public static Task<VirtualGeometryWebArchive> OpenAsync(string url)
```

#### 引数（Parameters）

`url` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task\-1)<[VirtualGeometryWebArchive](VirtualizedGeometry.VirtualGeometryWebArchive.md)\>
