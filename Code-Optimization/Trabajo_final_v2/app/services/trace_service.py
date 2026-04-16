from datetime import datetime


class TraceService:
    def __init__(self, log_repository) -> None:
        self.log_repository = log_repository

    def log(self, module: str, action: str, detail: str, level: str = "INFO", echo: bool = True) -> str:
        timestamp = datetime.now().isoformat(sep=" ", timespec="seconds")
        message = f"[{level}] [{module}.{action}] {detail} | fecha={timestamp}"
        if echo:
            print(message)
        self.log_repository.append(message)
        return message
