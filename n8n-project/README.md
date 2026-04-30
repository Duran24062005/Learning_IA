# HelpDeskBot n8n workflow

Este modulo contiene el workflow portable de n8n para HelpDeskBot:

- `helpdeskbot_gemini_sin_credenciales.json`

El workflow integra Telegram, Google Sheets y Gemini para gestionar solicitudes de soporte desde Telegram. Permite validar usuarios, crear tickets, consultar estados, listar solicitudes del usuario, generar reportes para roles administrativos y actualizar estados de tickets.

## Requisitos

- n8n con nodos de Telegram, Google Sheets y HTTP Request.
- Credencial de Telegram configurada en n8n.
- Credencial OAuth2 de Google Sheets configurada en n8n.
- Variable de entorno `GEMINI_API_KEY` disponible para n8n.
- Un Google Spreadsheet con las hojas `USUARIOS`, `SOLICITUDES` y `LOGS`.

## Configuracion necesaria

Antes de activar el workflow importado:

1. Importa `helpdeskbot_gemini_sin_credenciales.json` en n8n.
2. Asigna la credencial de Telegram a los nodos de Telegram.
3. Asigna la credencial OAuth2 de Google Sheets a los nodos de Google Sheets.
4. Reemplaza `YOUR_HELPDESKBOT_DB_SPREADSHEET_ID` por el ID del spreadsheet operativo.
5. Verifica que `GEMINI_API_KEY` este definida en el entorno donde corre n8n.
6. Revisa que las hojas usen estos nombres exactos: `USUARIOS`, `SOLICITUDES` y `LOGS`.

## Modelo de datos esperado

`USUARIOS` debe incluir al menos:

- `telegram_user`
- `activo`
- `rol`
- `nombre`

`SOLICITUDES` debe incluir al menos:

- `id_ticket`
- `tipo`
- `prioridad`
- `estado`
- `descripcion`
- `fecha_creacion`
- `creado_por`
- `row_number`

`LOGS` debe incluir al menos:

- `timestamp`
- `telegram_user`
- `pantalla`
- `opcion`
- `resultado`

## Seguridad y trazabilidad

No versionar exports directos de n8n que incluyan IDs reales de credenciales, correos personales, IDs de spreadsheets productivos, webhook IDs o metadatos especificos del workspace. El archivo versionado debe permanecer portable y usar placeholders o variables de entorno.
