# <a id="Omni_Streaming_CatalogEntry"></a> Struct CatalogEntry

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

```csharp
public readonly struct CatalogEntry
```

## コンストラクター（Constructors）

### <a id="Omni_Streaming_CatalogEntry__ctor_Omni_Streaming_ContentId_Omni_Streaming_ByteLocation_System_UInt16_System_UInt32_"></a> CatalogEntry\(ContentId, ByteLocation, ushort, uint\)

```csharp
public CatalogEntry(ContentId id, ByteLocation location, ushort kind, uint flags = 0)
```

#### 引数（Parameters）

`id` [ContentId](Omni.Streaming.ContentId.md)

`location` [ByteLocation](Omni.Streaming.ByteLocation.md)

`kind` [ushort](https://learn.microsoft.com/dotnet/api/system.uint16)

`flags` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

## フィールド（Fields）

### <a id="Omni_Streaming_CatalogEntry_Flags"></a> Flags

```csharp
public readonly uint Flags
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="Omni_Streaming_CatalogEntry_Id"></a> Id

```csharp
public readonly ContentId Id
```

#### 値（Field Value）

 [ContentId](Omni.Streaming.ContentId.md)

### <a id="Omni_Streaming_CatalogEntry_Kind"></a> Kind

展開器の種別(<xref href="Omni.Streaming.IPayloadDecoder.Kind" data-throw-if-not-resolved="false"></xref>)。

```csharp
public readonly ushort Kind
```

#### 値（Field Value）

 [ushort](https://learn.microsoft.com/dotnet/api/system.uint16)

### <a id="Omni_Streaming_CatalogEntry_Location"></a> Location

```csharp
public readonly ByteLocation Location
```

#### 値（Field Value）

 [ByteLocation](Omni.Streaming.ByteLocation.md)
