def retrieval(Intent: 'str', Response: 'str') -> 'str[]':
    ChunkStorage: 'str[]'

    if isRT(Intent, Response):
        Append(ChunkStorage, Response)
        return ChunkStorage

    ParaChunks = ParaChunking(Response)
    ParaIndex = 0
    while ParaIndex<len(ParaChunks):
        ParaChunk = ParaChunks[ParaIndex]
        if isRT(Intent, ParaChunk):
            Append(ChunkStorage, ParaChunk)
        else:
            SentChunks = SentChunking(ParaChunk)
            SentIndex = 0
            while SentIndex<len(SentChunks):
                SentChunk = SentChunks[SentIndex]
                if isRT(Intent, SentChunk):
                    Append(ChunkStorage, SentChunk)
                SentIndex += 1
        ParaIndex += 1

    return ChunkStorage