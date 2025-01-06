from osscar.license import License

class Component:
    def __init__(self, name: str, version: str, license: License) -> None:
        self.name: str = name
        self.version: str = version
        self.license: License = license

    def __repr__(self) -> str:
        return f"Component(name={self.name}, version={self.version}, license={self.license})" 