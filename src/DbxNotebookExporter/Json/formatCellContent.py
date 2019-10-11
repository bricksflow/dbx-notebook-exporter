def formatCellContent(source):
    return (
        source
            .replace('\\', '\\\\')
            .replace('\n', '\\n')
            .replace('"', '\\"')
    )
