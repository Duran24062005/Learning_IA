class AuthService:
    ADMIN_PASSWORD = "admin123"
    RESIDENT_PASSWORD = "residente123"

    def login(self, option: int, password: str) -> str | None:
        if option == 1 and password == self.ADMIN_PASSWORD:
            return "admin"
        if option == 2 and password == self.RESIDENT_PASSWORD:
            return "residente"
        return None
