# <a id="VirtualizedGeometry_VirtualGeometryPagePaths"></a> Class VirtualGeometryPagePaths

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

page archiveの置き場所を解決する。Editorではモデルのインポート時に生成した変換キャッシュ(Library/VirtualGeometry)を読み、
Playerではbuild時に参照分だけ収録したStreamingAssets/VirtualGeometryを読む。相対パスはどちらも"VirtualGeometry/&lt;名前&gt;.vgpage"。

```csharp
public static class VirtualGeometryPagePaths
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryPagePaths](VirtualizedGeometry.VirtualGeometryPagePaths.md)

## フィールド（Fields）

### <a id="VirtualizedGeometry_VirtualGeometryPagePaths_Folder"></a> Folder

```csharp
public const string Folder = "VirtualGeometry"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## プロパティ（Properties）

### <a id="VirtualizedGeometry_VirtualGeometryPagePaths_Root"></a> Root

相対パスの基点。Editorはproject直下のLibrary、PlayerはStreamingAssets。

```csharp
public static string Root { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometryPagePaths_Resolve_System_String_"></a> Resolve\(string\)

相対パスを絶対パスへ解決する。基点の外を指すパスは拒否する。

```csharp
public static string Resolve(string relativePath)
```

#### 引数（Parameters）

`relativePath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
