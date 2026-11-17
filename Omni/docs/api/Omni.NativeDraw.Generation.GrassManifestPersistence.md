# <a id="Omni_NativeDraw_Generation_GrassManifestPersistence"></a> Class GrassManifestPersistence

Namespace: [Omni.NativeDraw.Generation](Omni.NativeDraw.Generation.md)  
Assembly: Omni.Manager.dll  

Grass の復元情報を、既存ファイルを途中で切り詰めずに保存する。

```csharp
public static class GrassManifestPersistence
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[GrassManifestPersistence](Omni.NativeDraw.Generation.GrassManifestPersistence.md)

## メソッド（Methods）

### <a id="Omni_NativeDraw_Generation_GrassManifestPersistence_Save_System_String_System_Byte___System_Boolean_System_Action_"></a> Save\(string, byte\[\], bool, Action\)

新規作成または既存 manifest の置換を同一ディレクトリーで行う。

```csharp
public static void Save(string path, byte[] bytes, bool createNew, Action beforeCommit = null)
```

#### 引数（Parameters）

`path` [string](https://learn.microsoft.com/dotnet/api/system.string)

`bytes` [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\]

`createNew` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`beforeCommit` [Action](https://learn.microsoft.com/dotnet/api/system.action)
