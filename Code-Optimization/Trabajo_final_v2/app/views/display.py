def print_categories(records: list[dict]) -> None:
    for record in records:
        print(
            f"""
            *********************************************************
            id:             {record.get('id', 'clave erronea')}
            categoria:      {record.get('nombre', 'clave erronea')}
            """
        )


def print_users(records: list[dict]) -> None:
    for record in records:
        print(
            f"""
            ****************************
            ID:             {record.get('id', 'Clave no encontrada')}
            Nombre:         {record.get('nombre', 'Clave no encontrada')}
            Apellido:       {record.get('apellido', 'clave erronea')}
            Telefono:       {record.get('telefono', 'clave erronea')}
            Direccion:      {record.get('direccion', 'Clave no encontrada')}
            Tipo Usuario:   {record.get('tipo', 'Clave no encontrada')}
            """
        )


def print_tools(records: list[dict]) -> None:
    for record in records:
        categoria = record.get("categoria", {})
        print(
            f"""
            ****************************
            ID:             {record.get('id', 'Clave no encontrada')}
            Nombre:         {record.get('nombre', 'Clave no encontrada')}
            Id Categoria:   {categoria.get('id', 'Clave no encontrada')}
            Categoria:      {categoria.get('categoria', 'Clave nombre categoria no encontrada')}
            Cantidad:       {record.get('cantidad', 'Cantidad no encontrada')}
            Estado:         {record.get('estado', 'Clave no encontrada')}
            Precio:         {record.get('precio', 'Clave no encontrada')}
            """
        )


def print_loans(records: list[dict]) -> None:
    for record in records:
        usuario = record.get("usuario", {})
        herramienta = record.get("herramienta", {})
        print(
            f"""
            ****************************
            ID:             {record.get('id', 'Clave no encontrada')}
            Usuario:        {usuario.get('nombre', 'clave no encontrada')}
            ID Usuario:     {usuario.get('id', 'Clave no encontrada')}
            Herramienta:    {herramienta.get('nombre', 'Clave no encontrada')}
            ID Herramienta: {herramienta.get('id', 'Clave no encontrada')}
            Fecha Inicio:   {record.get('fecha_inicio', 'Clave no encontrada')}
            Fecha Entrega:  {record.get('fecha_final', 'Clave no encontrada')}
            Cantidad:       {record.get('cantidad', 'Clave no encontrada')}
            Estado:         {record.get('estado', 'Clave no encontrada')}
            Observaciones:  {record.get('observaciones', 'Clave no encontrada')}
            """
        )


def print_lines(lines: list[str]) -> None:
    print(*lines, sep="")
